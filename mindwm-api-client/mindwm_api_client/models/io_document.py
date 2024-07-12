from typing import TYPE_CHECKING, Any, Dict, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tmux_pane_io_document import TmuxPaneIoDocument


T = TypeVar("T", bound="IoDocument")


@_attrs_define
class IoDocument:
    """
    Attributes:
        subject (Union[Unset, str]):
        type (Union[Literal['IoDocument'], Unset]):
        source (Union[Unset, str]):
        data (Union[Unset, TmuxPaneIoDocument]):
    """

    subject: Union[Unset, str] = UNSET
    type: Union[Literal["IoDocument"], Unset] = UNSET
    source: Union[Unset, str] = UNSET
    data: Union[Unset, "TmuxPaneIoDocument"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject

        type = self.type

        source = self.source

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if type is not UNSET:
            field_dict["type"] = type
        if source is not UNSET:
            field_dict["source"] = source
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tmux_pane_io_document import TmuxPaneIoDocument

        d = src_dict.copy()
        subject = d.pop("subject", UNSET)

        type = cast(Union[Literal["IoDocument"], Unset], d.pop("type", UNSET))
        if type != "IoDocument" and not isinstance(type, Unset):
            raise ValueError(f"type must match const 'IoDocument', got '{type}'")

        source = d.pop("source", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, TmuxPaneIoDocument]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TmuxPaneIoDocument.from_dict(_data)

        io_document = cls(
            subject=subject,
            type=type,
            source=source,
            data=data,
        )

        return io_document
