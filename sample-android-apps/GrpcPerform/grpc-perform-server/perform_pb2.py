# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perform.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='perform.proto',
  package='perform',
  syntax='proto3',
  serialized_options=b'\n\027com.example.grpcperformP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rperform.proto\x12\x07perform\"\n\n\x08\x45mptyMsg\"!\n\tTimeStamp\x12\x14\n\x0cmilliseconds\x18\x01 \x01(\x03\x32r\n\x0bTestService\x12\x32\n\x07GetTime\x12\x11.perform.EmptyMsg\x1a\x12.perform.TimeStamp\"\x00\x12/\n\x04Ping\x12\x12.perform.TimeStamp\x1a\x11.perform.EmptyMsg\"\x00\x42\x1b\n\x17\x63om.example.grpcperformP\x01\x62\x06proto3'
)




_EMPTYMSG = _descriptor.Descriptor(
  name='EmptyMsg',
  full_name='perform.EmptyMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=36,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='TimeStamp',
  full_name='perform.TimeStamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='milliseconds', full_name='perform.TimeStamp.milliseconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['EmptyMsg'] = _EMPTYMSG
DESCRIPTOR.message_types_by_name['TimeStamp'] = _TIMESTAMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyMsg = _reflection.GeneratedProtocolMessageType('EmptyMsg', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMSG,
  '__module__' : 'perform_pb2'
  # @@protoc_insertion_point(class_scope:perform.EmptyMsg)
  })
_sym_db.RegisterMessage(EmptyMsg)

TimeStamp = _reflection.GeneratedProtocolMessageType('TimeStamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'perform_pb2'
  # @@protoc_insertion_point(class_scope:perform.TimeStamp)
  })
_sym_db.RegisterMessage(TimeStamp)


DESCRIPTOR._options = None

_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='perform.TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=73,
  serialized_end=187,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTime',
    full_name='perform.TestService.GetTime',
    index=0,
    containing_service=None,
    input_type=_EMPTYMSG,
    output_type=_TIMESTAMP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='perform.TestService.Ping',
    index=1,
    containing_service=None,
    input_type=_TIMESTAMP,
    output_type=_EMPTYMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
