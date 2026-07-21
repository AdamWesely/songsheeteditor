from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from core.parser import Parser

@dataclass
class Song:

    id: str
    path: str

    title: str = ""
    artist: str = ""
    key: str = ""
    lyrics: str = ""

    raw: dict = field(default_factory=dict)

    @classmethod
    def from_json(cls, path: str, data: dict):

        return cls(
            id=data["id"],
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