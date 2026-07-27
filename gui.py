from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QInputDialog,
    QListWidgetItem,
)

from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Qt
from core.library import Library
from core.backup import Backup
from models.setlist import SetList

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.setlistSongs.changed_callback = self.update_current_setlist

        self.library = Library()
        self.backup = Backup()

        self.current_song = None
        self.current_setlist = None
        self.library_song_list = []

        self.connect_signals()
        self.visible_songs = []
        self.loading_song = False

    def connect_signals(self):

        self.ui.actionOpen.triggered.connect(self.open_backup)

        self.ui.songList.currentRowChanged.connect(
            self.song_selected
        )

        self.ui.titleEdit.textEdited.connect(self.song_changed)
        self.ui.artistEdit.textEdited.connect(self.song_changed)
        self.ui.keyCombo.currentTextChanged.connect(self.song_changed)
        self.ui.lyricsEdit.textChanged.connect(self.song_changed)
        self.ui.actionSave.triggered.connect(self.save_backup)
        self.ui.actionNewSong.clicked.connect(self.new_song)
        self.ui.actionDeleteSong.clicked.connect(self.delete_song)

        self.ui.searchEdit.textChanged.connect(
            self.refresh_song_list
        )

        self.ui.songLibrarySearch.textChanged.connect(
            self.filter_song_library
        )

        self.ui.setlistList.currentRowChanged.connect(
            self.setlist_selected
        )

        self.ui.actionNewSetlist.clicked.connect(
            self.new_setlist
        )

        self.ui.actionDeleteSetlist.clicked.connect(
            self.delete_setlist
        )

        self.ui.actionRenameSetlist.clicked.connect(
            self.rename_setlist
        )

    def save_backup(self):

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Uložit zálohu",
            "",
            "SongSheet Backup (*.songsheet-backup)",
        )

        if not filename:
            return

        try:
            self.backup.save(
                self.library,
                filename,
            )

            QMessageBox.information(
                self,
                "Success",
                "Library was saved"
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Saving failed:\n\n{e}"
            )

    def refresh_song_list(self):

        current = self.current_song

        self.ui.songList.clear()

        text = self.ui.searchEdit.text().strip().casefold()

        songs = sorted(
            self.library.songs,
            key=lambda s: s.title.casefold()
        )

        if text:
            songs = [
                s for s in songs
                if (
                    text in s.title.casefold()
                    or text in s.artist.casefold()
                )
            ]

        self.visible_songs = songs

        current_row = -1

        for row, song in enumerate(self.visible_songs):

            self.ui.songList.addItem(str(song))

            if song is current:
                current_row = row

        if current_row >= 0:
            self.ui.songList.setCurrentRow(current_row)

    def refresh_setlist_list(self):

        self.ui.setlistList.clear()

        for setlist in sorted(
            self.library.setlists,
            key=lambda s: s.title.casefold()
        ):
            self.ui.setlistList.addItem(setlist.title)

    def song_selected(self, row):

        if row < 0:
            return

        self.loading_song = True

        try:

            self.current_song = self.visible_songs[row]

            self.ui.titleEdit.setText(self.current_song.title)
            self.ui.artistEdit.setText(self.current_song.artist)
            self.ui.keyCombo.setCurrentText(self.current_song.key)
            self.ui.lyricsEdit.setPlainText(self.current_song.lyrics)

        finally:

            self.loading_song = False

    def song_changed(self):

        if self.loading_song:
            return

        if self.current_song is None:
            return

        self.current_song.title = self.ui.titleEdit.text()
        self.current_song.artist = self.ui.artistEdit.text()
        self.current_song.key = self.ui.keyCombo.currentText()
        self.current_song.lyrics = self.ui.lyricsEdit.toPlainText()

        self.library.modified = True

        row = self.ui.songList.currentRow()

        item = self.ui.songList.item(row)

        if item is not None:
            item.setText(str(self.current_song))

    def open_backup(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Otevřít zálohu",
            "",
            "SongSheet Backup (*.songsheet-backup);;Všechny soubory (*)",
        )

        if not filename:
            return

        self.library = self.backup.open(filename)

        self.refresh_song_list()
        self.refresh_setlist_list()
        self.refresh_song_library()

    def new_song(self):

        song = self.library.create_song()

        self.refresh_song_list()

        self.refresh_song_list()

        row = self.visible_songs.index(song)

        self.ui.songList.setCurrentRow(row)

        self.ui.titleEdit.setFocus()
        self.ui.titleEdit.selectAll()

    def delete_song(self):

        if self.current_song is None:
            return

        result = QMessageBox.question(
            self,
            "Smazat skladbu",
            f'Opravdu smazat "{self.current_song.title}"?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if result != QMessageBox.Yes:
            return

        row = self.ui.songList.currentRow()

        self.library.remove_song(self.current_song)

        self.refresh_song_list()

        if self.visible_songs:
            self.ui.songList.setCurrentRow(
                min(row, len(self.visible_songs)-1)
            )
        else:
            self.current_song = None

            self.ui.titleEdit.clear()
            self.ui.artistEdit.clear()
            self.ui.keyCombo.setCurrentIndex(0)
            self.ui.lyricsEdit.clear()

    def filter_song_library(self):

        text = self.ui.songLibrarySearch.text().casefold().strip()

        self.ui.songLibraryList.clear()

        self.library_song_list = []

        for song in sorted(
            self.library.songs,
            key=lambda s: str(s).casefold()
        ):

            if (
                text
                and text not in song.title.casefold()
                and text not in song.artist.casefold()
            ):
                continue

            self.library_song_list.append(song)

            item = QListWidgetItem(str(song))
            item.setData(Qt.ItemDataRole.UserRole, song)

            self.ui.songLibraryList.addItem(item)

    def refresh_setlist_songs(self):

        self.ui.setlistSongs.clear()

        if self.current_setlist is None:
            return

        for i, song in enumerate(self.current_setlist.songs, start=1):

            item = QListWidgetItem(f"{i}. {song}")
            item.setData(Qt.ItemDataRole.UserRole, song)

            self.ui.setlistSongs.addItem(item)

    def refresh_song_library(self):

        self.ui.songLibraryList.clear()

        self.filter_song_library()


    def setlist_selected(self, row):

        if row < 0:
            return

        self.current_setlist = sorted(
            self.library.setlists,
            key=lambda s: s.title.casefold()
        )[row]

        self.refresh_setlist_songs()


    def new_setlist(self):

        title, ok = QInputDialog.getText(
            self,
            "Nový setlist",
            "Název:"
        )

        if not ok or not title.strip():
            return

        setlist = SetList.create(
            self.library,
            title.strip(),
        )

        self.library.setlists.append(setlist)

        self.refresh_setlist_list()

        for i, s in enumerate(
            sorted(
                self.library.setlists,
                key=lambda x: x.title.casefold()
            )
        ):
            if s is setlist:
                self.ui.setlistList.setCurrentRow(i)
                break

        self.library.modified = True

    def delete_setlist(self):

        if self.current_setlist is None:
            return

        answer = QMessageBox.question(
            self,
            "Smazat setlist",
            f"Opravdu smazat setlist '{self.current_setlist.title}'?"
        )

        if answer != QMessageBox.StandardButton.Yes:
            return

        self.library.setlists.remove(
            self.current_setlist
        )

        self.current_setlist = None

        self.library.modified = True

        self.refresh_setlist_list()
        self.ui.setlistSongs.clear()


    def rename_setlist(self):

        if self.current_setlist is None:
            return

        title, ok = QInputDialog.getText(
            self,
            "Přejmenovat setlist",
            "Název:",
            text=self.current_setlist.title
        )

        if not ok or not title.strip():
            return

        title = title.strip()

        self.current_setlist.title = title
        self.current_setlist.raw["title"] = title
        self.current_setlist.raw["sets"][0]["title"] = title

        self.library.modified = True

        self.refresh_setlist_list()

        for i, s in enumerate(
            sorted(
                self.library.setlists,
                key=lambda x: x.title.casefold()
            )
        ):
            if s is self.current_setlist:
                self.ui.setlistList.setCurrentRow(i)
                break

    def update_current_setlist(self):

        if self.current_setlist is None:
            return

        songs = []

        for row in range(self.ui.setlistSongs.count()):

            item = self.ui.setlistSongs.item(row)

            song = item.data(Qt.ItemDataRole.UserRole)

            if song:
                songs.append(song)

        self.current_setlist.songs = songs
        self.library.modified = True