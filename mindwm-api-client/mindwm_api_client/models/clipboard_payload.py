from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.clipboard_payload_type import ClipboardPayloadType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clipboard_payload_context import ClipboardPayloadContext


T = TypeVar("T", bound="ClipboardPayload")


@_attrs_define
class ClipboardPayload:
    """
    Attributes:
        start (Union[Unset, List[int]]): Starting position of clipboard selection [x,y]
        stop (Union[Unset, List[int]]): Ending position of clipboard selection [x,y]
        data (Union[Unset, str]): Clipboard data
        type (Union[Unset, ClipboardPayloadType]): Clipboard type
        context (Union[Unset, ClipboardPayloadContext]): Selection context
    """

    start: Union[Unset, List[int]] = UNSET
    stop: Union[Unset, List[int]] = UNSET
    data: Union[Unset, str] = UNSET
    type: Union[Unset, ClipboardPayloadType] = UNSET
    context: Union[Unset, "ClipboardPayloadContext"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start: Union[Unset, List[int]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start

        stop: Union[Unset, List[int]] = UNSET
        if not isinstance(self.stop, Unset):
            stop = self.stop

        data = self.data

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if stop is not UNSET:
            field_dict["stop"] = stop
        if data is not UNSET:
            field_dict["data"] = data
        if type is not UNSET:
            field_dict["type"] = type
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.clipboard_payload_context import ClipboardPayloadContext

        d = src_dict.copy()
        start = cast(List[int], d.pop("start", UNSET))

        stop = cast(List[int], d.pop("stop", UNSET))

        data = d.pop("data", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ClipboardPayloadType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ClipboardPayloadType(_type)

        _context = d.pop("context", UNSET)
        context: Union[Unset, ClipboardPayloadContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = ClipboardPayloadContext.from_dict(_context)

        clipboard_payload = cls(
            start=start,
            stop=stop,
            data=data,
            type=type,
            context=context,
        )

        clipboard_payload.additional_properties = d
        return clipboard_payload

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
