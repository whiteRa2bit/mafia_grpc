# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mafia.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='mafia.proto',
    package='mafiaservice',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=
    b'\n\x0bmafia.proto\x12\x0cmafiaservice\"%\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xa2\x01\n\x08Response\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.mafiaservice.StatusCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12.\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32 .mafiaservice.Response.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\"\n\x0f\x42\x61seUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"p\n\x14\x43ommunicationRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x36\n\tdata_type\x18\x03 \x01(\x0e\x32#.mafiaservice.CommunicationDataType\"8\n\x15\x43ommunicationResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\"\x1e\n\x0e\x41\x64\x64UserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"_\n\x10GetUsersResponse\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.mafiaservice.StatusCode\x12!\n\x05users\x18\x02 \x03(\x0b\x32\x12.mafiaservice.User\"F\n\x11\x41\x63\x63useUserRequest\x12\x18\n\x10\x61\x63\x63using_user_id\x18\x01 \x01(\x05\x12\x17\n\x0f\x61\x63\x63used_user_id\x18\x02 \x01(\x05\"#\n\x10\x46inishDayRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05*n\n\x15\x43ommunicationDataType\x12\x11\n\rEMPTY_MESSAGE\x10\x00\x12\x15\n\x11\x42ROADCAST_MESSAGE\x10\x01\x12\x14\n\x10\x44\x45\x43ISION_MESSAGE\x10\x02\x12\x15\n\x11HANDSHAKE_MESSAGE\x10\x03*\xa8\x01\n\nStatusCode\x12\x1a\n\x16StatusCode_UNSPECIFIED\x10\x00\x12\x12\n\rStatusCode_OK\x10\xc8\x01\x12\x17\n\x12StatusCode_CREATED\x10\xc9\x01\x12\x1b\n\x16StatusCode_BAD_REQUEST\x10\x90\x03\x12\x19\n\x14StatusCode_FORBIDDEN\x10\x93\x03\x12\x19\n\x14StatusCode_NOT_FOUND\x10\x94\x03\x32\xd2\x03\n\x05Mafia\x12\x42\n\x08\x61\x64\x64_user\x12\x1c.mafiaservice.AddUserRequest\x1a\x16.mafiaservice.Response\"\x00\x12\x46\n\x0b\x64\x65lete_user\x12\x1d.mafiaservice.BaseUserRequest\x1a\x16.mafiaservice.Response\"\x00\x12:\n\tget_users\x12\x13.mafiaservice.Empty\x1a\x16.mafiaservice.Response\"\x00\x12H\n\x0b\x61\x63\x63use_user\x12\x1f.mafiaservice.AccuseUserRequest\x1a\x16.mafiaservice.Response\"\x00\x12J\n\x0fvote_finish_day\x12\x1d.mafiaservice.BaseUserRequest\x1a\x16.mafiaservice.Response\"\x00\x12k\n\x1ainit_communication_channel\x12\".mafiaservice.CommunicationRequest\x1a#.mafiaservice.CommunicationResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)

_COMMUNICATIONDATATYPE = _descriptor.EnumDescriptor(
    name='CommunicationDataType',
    full_name='mafiaservice.CommunicationDataType',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='EMPTY_MESSAGE',
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='BROADCAST_MESSAGE',
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='DECISION_MESSAGE',
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='HANDSHAKE_MESSAGE',
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=688,
    serialized_end=798,
)
_sym_db.RegisterEnumDescriptor(_COMMUNICATIONDATATYPE)

CommunicationDataType = enum_type_wrapper.EnumTypeWrapper(_COMMUNICATIONDATATYPE)
_STATUSCODE = _descriptor.EnumDescriptor(
    name='StatusCode',
    full_name='mafiaservice.StatusCode',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='StatusCode_UNSPECIFIED',
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='StatusCode_OK',
            index=1,
            number=200,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='StatusCode_CREATED',
            index=2,
            number=201,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='StatusCode_BAD_REQUEST',
            index=3,
            number=400,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='StatusCode_FORBIDDEN',
            index=4,
            number=403,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
        _descriptor.EnumValueDescriptor(
            name='StatusCode_NOT_FOUND',
            index=5,
            number=404,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=801,
    serialized_end=969,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
EMPTY_MESSAGE = 0
BROADCAST_MESSAGE = 1
DECISION_MESSAGE = 2
HANDSHAKE_MESSAGE = 3
StatusCode_UNSPECIFIED = 0
StatusCode_OK = 200
StatusCode_CREATED = 201
StatusCode_BAD_REQUEST = 400
StatusCode_FORBIDDEN = 403
StatusCode_NOT_FOUND = 404

_USER = _descriptor.Descriptor(
    name='User',
    full_name='mafiaservice.User',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='user_id',
            full_name='mafiaservice.User.user_id',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='name',
            full_name='mafiaservice.User.name',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=29,
    serialized_end=66,
)

_RESPONSE_DATAENTRY = _descriptor.Descriptor(
    name='DataEntry',
    full_name='mafiaservice.Response.DataEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='key',
            full_name='mafiaservice.Response.DataEntry.key',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='value',
            full_name='mafiaservice.Response.DataEntry.value',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b'8\001',
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=188,
    serialized_end=231,
)

_RESPONSE = _descriptor.Descriptor(
    name='Response',
    full_name='mafiaservice.Response',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='status',
            full_name='mafiaservice.Response.status',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='message',
            full_name='mafiaservice.Response.message',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='data',
            full_name='mafiaservice.Response.data',
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[
        _RESPONSE_DATAENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=69,
    serialized_end=231,
)

_BASEUSERREQUEST = _descriptor.Descriptor(
    name='BaseUserRequest',
    full_name='mafiaservice.BaseUserRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='user_id',
            full_name='mafiaservice.BaseUserRequest.user_id',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=233,
    serialized_end=267,
)

_COMMUNICATIONREQUEST = _descriptor.Descriptor(
    name='CommunicationRequest',
    full_name='mafiaservice.CommunicationRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='user_id',
            full_name='mafiaservice.CommunicationRequest.user_id',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='message',
            full_name='mafiaservice.CommunicationRequest.message',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='data_type',
            full_name='mafiaservice.CommunicationRequest.data_type',
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=269,
    serialized_end=381,
)

_COMMUNICATIONRESPONSE = _descriptor.Descriptor(
    name='CommunicationResponse',
    full_name='mafiaservice.CommunicationResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='message',
            full_name='mafiaservice.CommunicationResponse.message',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='author',
            full_name='mafiaservice.CommunicationResponse.author',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=383,
    serialized_end=439,
)

_ADDUSERREQUEST = _descriptor.Descriptor(
    name='AddUserRequest',
    full_name='mafiaservice.AddUserRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='name',
            full_name='mafiaservice.AddUserRequest.name',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=441,
    serialized_end=471,
)

_EMPTY = _descriptor.Descriptor(
    name='Empty',
    full_name='mafiaservice.Empty',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=473,
    serialized_end=480,
)

_GETUSERSRESPONSE = _descriptor.Descriptor(
    name='GetUsersResponse',
    full_name='mafiaservice.GetUsersResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='status',
            full_name='mafiaservice.GetUsersResponse.status',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='users',
            full_name='mafiaservice.GetUsersResponse.users',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=482,
    serialized_end=577,
)

_ACCUSEUSERREQUEST = _descriptor.Descriptor(
    name='AccuseUserRequest',
    full_name='mafiaservice.AccuseUserRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='accusing_user_id',
            full_name='mafiaservice.AccuseUserRequest.accusing_user_id',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
        _descriptor.FieldDescriptor(
            name='accused_user_id',
            full_name='mafiaservice.AccuseUserRequest.accused_user_id',
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=579,
    serialized_end=649,
)

_FINISHDAYREQUEST = _descriptor.Descriptor(
    name='FinishDayRequest',
    full_name='mafiaservice.FinishDayRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='user_id',
            full_name='mafiaservice.FinishDayRequest.user_id',
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=651,
    serialized_end=686,
)

_RESPONSE_DATAENTRY.containing_type = _RESPONSE
_RESPONSE.fields_by_name['status'].enum_type = _STATUSCODE
_RESPONSE.fields_by_name['data'].message_type = _RESPONSE_DATAENTRY
_COMMUNICATIONREQUEST.fields_by_name['data_type'].enum_type = _COMMUNICATIONDATATYPE
_GETUSERSRESPONSE.fields_by_name['status'].enum_type = _STATUSCODE
_GETUSERSRESPONSE.fields_by_name['users'].message_type = _USER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['BaseUserRequest'] = _BASEUSERREQUEST
DESCRIPTOR.message_types_by_name['CommunicationRequest'] = _COMMUNICATIONREQUEST
DESCRIPTOR.message_types_by_name['CommunicationResponse'] = _COMMUNICATIONRESPONSE
DESCRIPTOR.message_types_by_name['AddUserRequest'] = _ADDUSERREQUEST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['GetUsersResponse'] = _GETUSERSRESPONSE
DESCRIPTOR.message_types_by_name['AccuseUserRequest'] = _ACCUSEUSERREQUEST
DESCRIPTOR.message_types_by_name['FinishDayRequest'] = _FINISHDAYREQUEST
DESCRIPTOR.enum_types_by_name['CommunicationDataType'] = _COMMUNICATIONDATATYPE
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType(
    'User',
    (_message.Message, ),
    {
        'DESCRIPTOR': _USER,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.User)
    })
_sym_db.RegisterMessage(User)

Response = _reflection.GeneratedProtocolMessageType(
    'Response',
    (_message.Message, ),
    {
        'DataEntry':
            _reflection.GeneratedProtocolMessageType(
                'DataEntry',
                (_message.Message, ),
                {
                    'DESCRIPTOR': _RESPONSE_DATAENTRY,
                    '__module__': 'mafia_pb2'
                    # @@protoc_insertion_point(class_scope:mafiaservice.Response.DataEntry)
                }),
        'DESCRIPTOR':
            _RESPONSE,
        '__module__':
            'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.Response)
    })
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.DataEntry)

BaseUserRequest = _reflection.GeneratedProtocolMessageType(
    'BaseUserRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _BASEUSERREQUEST,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.BaseUserRequest)
    })
_sym_db.RegisterMessage(BaseUserRequest)

CommunicationRequest = _reflection.GeneratedProtocolMessageType(
    'CommunicationRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _COMMUNICATIONREQUEST,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.CommunicationRequest)
    })
_sym_db.RegisterMessage(CommunicationRequest)

CommunicationResponse = _reflection.GeneratedProtocolMessageType(
    'CommunicationResponse',
    (_message.Message, ),
    {
        'DESCRIPTOR': _COMMUNICATIONRESPONSE,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.CommunicationResponse)
    })
_sym_db.RegisterMessage(CommunicationResponse)

AddUserRequest = _reflection.GeneratedProtocolMessageType(
    'AddUserRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _ADDUSERREQUEST,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.AddUserRequest)
    })
_sym_db.RegisterMessage(AddUserRequest)

Empty = _reflection.GeneratedProtocolMessageType(
    'Empty',
    (_message.Message, ),
    {
        'DESCRIPTOR': _EMPTY,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.Empty)
    })
_sym_db.RegisterMessage(Empty)

GetUsersResponse = _reflection.GeneratedProtocolMessageType(
    'GetUsersResponse',
    (_message.Message, ),
    {
        'DESCRIPTOR': _GETUSERSRESPONSE,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.GetUsersResponse)
    })
_sym_db.RegisterMessage(GetUsersResponse)

AccuseUserRequest = _reflection.GeneratedProtocolMessageType(
    'AccuseUserRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _ACCUSEUSERREQUEST,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.AccuseUserRequest)
    })
_sym_db.RegisterMessage(AccuseUserRequest)

FinishDayRequest = _reflection.GeneratedProtocolMessageType(
    'FinishDayRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _FINISHDAYREQUEST,
        '__module__': 'mafia_pb2'
        # @@protoc_insertion_point(class_scope:mafiaservice.FinishDayRequest)
    })
_sym_db.RegisterMessage(FinishDayRequest)

_RESPONSE_DATAENTRY._options = None

_MAFIA = _descriptor.ServiceDescriptor(
    name='Mafia',
    full_name='mafiaservice.Mafia',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=972,
    serialized_end=1438,
    methods=[
        _descriptor.MethodDescriptor(
            name='add_user',
            full_name='mafiaservice.Mafia.add_user',
            index=0,
            containing_service=None,
            input_type=_ADDUSERREQUEST,
            output_type=_RESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='delete_user',
            full_name='mafiaservice.Mafia.delete_user',
            index=1,
            containing_service=None,
            input_type=_BASEUSERREQUEST,
            output_type=_RESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='get_users',
            full_name='mafiaservice.Mafia.get_users',
            index=2,
            containing_service=None,
            input_type=_EMPTY,
            output_type=_RESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='accuse_user',
            full_name='mafiaservice.Mafia.accuse_user',
            index=3,
            containing_service=None,
            input_type=_ACCUSEUSERREQUEST,
            output_type=_RESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='vote_finish_day',
            full_name='mafiaservice.Mafia.vote_finish_day',
            index=4,
            containing_service=None,
            input_type=_BASEUSERREQUEST,
            output_type=_RESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name='init_communication_channel',
            full_name='mafiaservice.Mafia.init_communication_channel',
            index=5,
            containing_service=None,
            input_type=_COMMUNICATIONREQUEST,
            output_type=_COMMUNICATIONRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_MAFIA)

DESCRIPTOR.services_by_name['Mafia'] = _MAFIA

# @@protoc_insertion_point(module_scope)