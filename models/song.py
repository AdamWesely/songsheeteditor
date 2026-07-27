from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from core.parser import Parser

@dataclass
class Song:

    id: str
    coredata_id: str
    path: str

    title: str = ""
    artist: str = ""
    key: str = ""
    lyrics: str = ""

    raw: dict = field(default_factory=dict)

    @staticmethod
    def path_to_coredata_id(path: str) -> str:

        filename = path.split("/")[-1]
        filename = filename.removesuffix(".json")
        filename = filename.removeprefix("x-coredata---")

        parts = filename.rsplit("-", 2)

        if len(parts) != 3:
            raise ValueError(f"Invalid song filename: {path}")

        guid, entity, page = parts

        return f"x-coredata://{guid}/{entity}/{page}"

    @classmethod
    def from_json(cls, path: str, data: dict):

        return cls(
            id=data["id"],
            coredata_id=cls.path_to_coredata_id(path),
            path=path,
            title=data.get("title", ""),
            artist=data.get("artist", ""),
            key=data.get("key", ""),
            lyrics=Parser.to_editor(
                data.get("rawLyrics", "")
            ),
            raw=deepcopy(data),
        )

    def to_json(self):

        data = deepcopy(self.raw)

        data["id"] = self.id
        data["title"] = self.title
        data["artist"] = self.artist
        data["key"] = self.key
        data["rawLyrics"] = Parser.from_editor(
            self.lyrics
        )

        return data

    def __str__(self):

        if self.artist:
            return f"{self.title} - {self.artist}"

        return self.title