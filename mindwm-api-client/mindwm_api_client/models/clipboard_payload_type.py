from enum import Enum


class ClipboardPayloadType(str, Enum):
    CLIPBOARD = "clipboard"
    PRIMARY = "primary"
    SECONDARY = "secondary"

    def __str__(self) -> str:
        return str(self.value)
