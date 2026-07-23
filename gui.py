from PySide6.QtWidgets import (
    QMainWindow,
    QFileDialog,
    QMessageBox,
)

from ui_mainwindow import Ui_MainWindow

from core.library import Library
from core.backup import Backup
from PySide6.QtWidgets import QFileDialog

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.library = Library()
        self.backup = Backup()

        self.current_song = None

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

    def save_backup(self):

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Uložit zálohu",
            "",
            "SongSheet Backup (*.songsheet-backup)",
        )

        if not filename:
            return

        self.backup.save(
            self.library,
            filename,
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