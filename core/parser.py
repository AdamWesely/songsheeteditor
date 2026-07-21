from __future__ import annotations

import re
import uuid


STANZA_RE = re.compile(r"^\{stanzaId:[^}]+\}$")
TYPE_RE = re.compile(r"^\{type:[^}]+\}$")


class Parser:

    @staticmethod
    def to_editor(raw: str) -> str:

        lines = []

        for line in raw.splitlines():

            if STANZA_RE.match(line):
                continue

            if TYPE_RE.match(line):
                continue

            lines.append(line)

        return "\n".join(lines)

    @staticmethod
    def from_editor(text: str) -> str:

        blocks = []

        current = []

        for line in text.splitlines():

            if line.strip() == "":

                if current:
                    blocks.append(current)
                    current = []

                continue

            current.append(line)

        if current:
            blocks.append(current)

        out = []

        for block in blocks:

            out.append("{stanzaId:%s}" % uuid.uuid4().hex.upper())

            out.append("{type:verse}")

            out.extend(block)

            out.append("")

        return "\n".join(out).rstrip()