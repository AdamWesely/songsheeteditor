from __future__ import annotations

import json
import zipfile
from pathlib import Path
from copy import deepcopy
from core.library import Library
from models.song import Song
import hashlib
from copy import deepcopy


class Backup:

    def open(self, filename: str | Path) -> Library:

        filename = Path(filename)

        library = Library()
        library.filename = filename

        with zipfile.ZipFile(filename, "r") as archive:

            manifest = self.load_json(archive, "manifest.json")

            library.manifest = manifest

            #
            # Songs
            #
            for index, entry in enumerate(manifest["entries"]["songs"]):

                data = self.load_json(
                    archive,
                    entry["path"],
                )

                if index == 0:
                    library.song_template = deepcopy(data)

                song = Song.from_json(
                    entry["path"],
                    data,
                )

                library.add_song(song)

            #
            # Themes
            #
            for entry in manifest["entries"]["themes"]:

                library.themes[entry["id"]] = {
                    "path": entry["path"],
                    "data": self.load_json(
                        archive,
                        entry["path"],
                    ),
                }

            #
            # Tags
            #
            for entry in manifest["entries"]["tags"]:

                library.tags[entry["id"]] = {
                    "path": entry["path"],
                    "data": self.load_json(
                        archive,
                        entry["path"],
                    ),
                }

            #
            # Setlists
            #
            for entry in manifest["entries"]["setlists"]:

                library.setlists[entry["id"]] = {
                    "path": entry["path"],
                    "data": self.load_json(
                        archive,
                        entry["path"],
                    ),
                }

        library.modified = False

        return library

    def save(self, library: Library, filename: str | Path):

        filename = Path(filename)

        manifest = deepcopy(library.manifest)

        manifest["library"]["songs"] = len(library.songs)
        manifest["library"]["themes"] = len(library.themes)
        manifest["library"]["tags"] = len(library.tags)
        manifest["library"]["setlists"] = len(library.setlists)

        manifest["entries"]["songs"] = []
        manifest["entries"]["themes"] = []
        manifest["entries"]["tags"] = []
        manifest["entries"]["setlists"] = []

        with zipfile.ZipFile(
            filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
        ) as archive:

            #
            # Songs
            #
            for song in library.songs:

                data = song.to_json()

                archive.writestr(
                    song.path,
                    self.json_text(data),
                )

                manifest["entries"]["songs"].append({
                    "id": song.id,
                    "path": song.path,
                    "checksum": self.checksum(data),
                })

            #
            # Themes
            #
            for ident, theme in library.themes.items():

                archive.writestr(
                    theme["path"],
                    self.json_text(theme["data"]),
                )

                manifest["entries"]["themes"].append({
                    "id": ident,
                    "path": theme["path"],
                    "checksum": self.checksum(theme["data"]),
                })

            #
            # Tags
            #
            for ident, tag in library.tags.items():

                archive.writestr(
                    tag["path"],
                    self.json_text(tag["data"]),
                )

                manifest["entries"]["tags"].append({
                    "id": ident,
                    "path": tag["path"],
                    "checksum": self.checksum(tag["data"]),
                })

            #
            # Setlists
            #
            for ident, setlist in library.setlists.items():

                archive.writestr(
                    setlist["path"],
                    self.json_text(setlist["data"]),
                )

                manifest["entries"]["setlists"].append({
                    "id": ident,
                    "path": setlist["path"],
                    "checksum": self.checksum(setlist["data"]),
                })

            archive.writestr(
                "manifest.json",
                self.json_text(manifest),
            )

        library.manifest = manifest
        library.modified = False

    @staticmethod
    def load_json(archive: zipfile.ZipFile, name: str):

        with archive.open(name) as f:
            return json.load(f)

    @staticmethod
    def save_json(archive, name, data):

        archive.writestr(
            name,
            json.dumps(
                data,
                indent=2,
                ensure_ascii=False,
            ),
        )

    @staticmethod
    def json_text(data):

        return json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )


    @staticmethod
    def checksum(data):

        return hashlib.sha256(
            Backup.json_text(data).encode("utf-8")
        ).hexdigest()