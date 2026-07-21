from __future__ import annotations

import json
import zipfile
from pathlib import Path

from core.library import Library
from models.song import Song


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
            for entry in manifest["entries"]["songs"]:

                data = self.load_json(
                    archive,
                    entry["path"],
                )

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

        with zipfile.ZipFile(
            filename,
            "w",
            compression=zipfile.ZIP_DEFLATED,
        ) as archive:

            #
            # Manifest
            #
            self.save_json(
                archive,
                "manifest.json",
                library.manifest,
            )

            #
            # Songs
            #
            for song in library.songs:

                self.save_json(
                    archive,
                    song.path,
                    song.to_json(),
                )

            #
            # Themes
            #
            for theme in library.themes.values():

                self.save_json(
                    archive,
                    theme["path"],
                    theme["data"],
                )

            #
            # Tags
            #
            for tag in library.tags.values():

                self.save_json(
                    archive,
                    tag["path"],
                    tag["data"],
                )

            #
            # Setlists
            #
            for setlist in library.setlists.values():

                self.save_json(
                    archive,
                    setlist["path"],
                    setlist["data"],
                )

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