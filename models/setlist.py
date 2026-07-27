from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field

from models.song import Song

import uuid


@dataclass
class SetList:

    id: str
    path: str

    title: str = ""

    songs: list[Song] = field(default_factory=list)

    raw: dict = field(default_factory=dict)

    @classmethod
    def from_json(
        cls,
        path: str,
        data: dict,
        library,
    ):

        obj = cls(
            id=data["id"],
            path=path,
            title=data.get("title", ""),
            raw=deepcopy(data),
        )

        #
        # načtení skladeb
        #

        for s in data["sets"][0]["songIDs"]:

            song = next(
                (
                    x
                    for x in library.songs
                    if x.coredata_id == s
                ),
                None,
            )

            if song:
                obj.songs.append(song)

        return obj

    def to_json(self):

        data = deepcopy(self.raw)

        data["id"] = self.id
        data["title"] = self.title

        data["sets"][0]["songIDs"] = [
            s.id
            for s in self.songs
        ]

        return data

    def __str__(self):

        return self.title


    @classmethod
    def create(cls, library, title: str):

        numbers = []

        for s in library.setlists:

            try:
                numbers.append(
                    int(s.path.rsplit("p", 1)[1].split(".")[0])
                )
            except Exception:
                pass

        next_page = max(numbers, default=0) + 1

        guid = str(uuid.uuid4()).upper()

        coredata_id = (
            f"x-coredata://{guid}/SetList/p{next_page}"
        )

        path = (
            f"setlists/"
            f"x-coredata---{guid}-SetList-p{next_page}.json"
        )

        raw = {
            "id": coredata_id,
            "title": title,
            "sets": [
                {
                    "title": title,
                    "songIDs": [],
                }
            ],
        }

        return cls(
            id=coredata_id,
            path=path,
            title=title,
            raw=raw,
        )