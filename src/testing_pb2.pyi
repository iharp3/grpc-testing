from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RangeRequest(_message.Message):
    __slots__ = ("idStart", "idEnd")
    IDSTART_FIELD_NUMBER: _ClassVar[int]
    IDEND_FIELD_NUMBER: _ClassVar[int]
    idStart: int
    idEnd: int
    def __init__(self, idStart: _Optional[int] = ..., idEnd: _Optional[int] = ...) -> None: ...

class SingleResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class DataRequest(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: int
    value: int
    def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class InsertDataAcknowledgement(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
