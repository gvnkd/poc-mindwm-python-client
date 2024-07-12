from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TmuxPaneIoDocument")


@_attrs_define
class TmuxPaneIoDocument:
    """
    Attributes:
        input_ (str): User input
        output (str): Command output (mix of stdout & stderr)
        ps1 (str): ps1 (prompt) AFTER the input and output
    """

    input_: str
    output: str
    ps1: str

    def to_dict(self) -> Dict[str, Any]:
        input_ = self.input_

        output = self.output

        ps1 = self.ps1

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "input": input_,
                "output": output,
                "ps1": ps1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_ = d.pop("input")

        output = d.pop("output")

        ps1 = d.pop("ps1")

        tmux_pane_io_document = cls(
            input_=input_,
            output=output,
            ps1=ps1,
        )

        return tmux_pane_io_document
