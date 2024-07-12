from typing import TYPE_CHECKING, Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clipboard_payload import ClipboardPayload


T = TypeVar("T", bound="Clipboard")


@_attrs_define
class Clipboard:
    """
    Attributes:
        subject (Union[Unset, str]):
        type (Union[Literal['Clipboard'], Unset]):
        source (Union[Unset, str]):
        data (Union[Unset, ClipboardPayload]):
    """

    subject: Union[Unset, str] = UNSET
    type: Union[Literal["Clipboard"], Unset] = UNSET
    source: Union[Unset, str] = UNSET
    data: Union[Unset, "ClipboardPayload"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject

        type = self.type

        source = self.source

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.clipboard_payload import ClipboardPayload

        d = src_dict.copy()
        subject = d.pop("subject", UNSET)

        type = cast(Union[Literal["Clipboard"], Unset], d.pop("type", UNSET))
        if type != "Clipboard" and not isinstance(type, Unset):
            raise ValueError(f"type must match const 'Clipboard', got '{type}'")

        source = d.pop("source", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ClipboardPayload]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ClipboardPayload.from_dict(_data)

        clipboard = cls(
            subject=subject,
            type=type,
            source=source,
            data=data,
        )

        clipboard.additional_properties = d
        return clipboard

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
