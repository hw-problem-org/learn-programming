# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maths.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='maths.proto',
  package='grpc_experimentation',
  syntax='proto3',
  serialized_options=b'\n\037io.example.grpc_experimentationP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmaths.proto\x12\x14grpc_experimentation\"\x07\n\x05\x45mpty\" \n\x08SumInput\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"\x1b\n\tSumResult\x12\x0e\n\x06result\x18\x01 \x01(\x01\"(\n\x0e\x46ibonacciStart\x12\n\n\x02\x66\x31\x18\x01 \x01(\x05\x12\n\n\x02\x66\x32\x18\x02 \x01(\x05\"\x1c\n\x0f\x46ibonacciNumber\x12\t\n\x01\x66\x18\x01 \x01(\x05\"-\n\tTimeStamp\x12 \n\x18milliseconds_since_epoch\x18\x01 \x01(\x03\x32\x86\x02\n\x05Maths\x12H\n\x03Sum\x12\x1e.grpc_experimentation.SumInput\x1a\x1f.grpc_experimentation.SumResult\"\x00\x12k\n\x18GetFibonacciNumberStream\x12$.grpc_experimentation.FibonacciStart\x1a%.grpc_experimentation.FibonacciNumber\"\x00\x30\x01\x12\x46\n\x04Time\x12\x1f.grpc_experimentation.TimeStamp\x1a\x1b.grpc_experimentation.Empty\"\x00\x42#\n\x1fio.example.grpc_experimentationP\x01\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc_experimentation.Empty',
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
  serialized_start=37,
  serialized_end=44,
)


_SUMINPUT = _descriptor.Descriptor(
  name='SumInput',
  full_name='grpc_experimentation.SumInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='grpc_experimentation.SumInput.a', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='grpc_experimentation.SumInput.b', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=46,
  serialized_end=78,
)


_SUMRESULT = _descriptor.Descriptor(
  name='SumResult',
  full_name='grpc_experimentation.SumResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='grpc_experimentation.SumResult.result', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=80,
  serialized_end=107,
)


_FIBONACCISTART = _descriptor.Descriptor(
  name='FibonacciStart',
  full_name='grpc_experimentation.FibonacciStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='grpc_experimentation.FibonacciStart.f1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='f2', full_name='grpc_experimentation.FibonacciStart.f2', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=109,
  serialized_end=149,
)


_FIBONACCINUMBER = _descriptor.Descriptor(
  name='FibonacciNumber',
  full_name='grpc_experimentation.FibonacciNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f', full_name='grpc_experimentation.FibonacciNumber.f', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=151,
  serialized_end=179,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='TimeStamp',
  full_name='grpc_experimentation.TimeStamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='milliseconds_since_epoch', full_name='grpc_experimentation.TimeStamp.milliseconds_since_epoch', index=0,
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
  serialized_start=181,
  serialized_end=226,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['SumInput'] = _SUMINPUT
DESCRIPTOR.message_types_by_name['SumResult'] = _SUMRESULT
DESCRIPTOR.message_types_by_name['FibonacciStart'] = _FIBONACCISTART
DESCRIPTOR.message_types_by_name['FibonacciNumber'] = _FIBONACCINUMBER
DESCRIPTOR.message_types_by_name['TimeStamp'] = _TIMESTAMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'maths_pb2'
  # @@protoc_insertion_point(class_scope:grpc_experimentation.Empty)
  })
_sym_db.RegisterMessage(Empty)

SumInput = _reflection.GeneratedProtocolMessageType('SumInput', (_message.Message,), {
  'DESCRIPTOR' : _SUMINPUT,
  '__module__' : 'maths_pb2'
  # @@protoc_insertion_point(class_scope:grpc_experimentation.SumInput)
  })
_sym_db.RegisterMessage(SumInput)

SumResult = _reflection.GeneratedProtocolMessageType('SumResult', (_message.Message,), {
  'DESCRIPTOR' : _SUMRESULT,
  '__module__' : 'maths_pb2'
  # @@protoc_insertion_point(class_scope:grpc_experimentation.SumResult)
  })
_sym_db.RegisterMessage(SumResult)

FibonacciStart = _reflection.GeneratedProtocolMessageType('FibonacciStart', (_message.Message,), {
  'DESCRIPTOR' : _FIBONACCISTART,
  '__module__' : 'maths_pb2'
  # @@protoc_insertion_point(class_scope:grpc_experimentation.FibonacciStart)
  })
_sym_db.RegisterMessage(FibonacciStart)

FibonacciNumber = _reflection.GeneratedProtocolMessageType('FibonacciNumber', (_message.Message,), {
  'DESCRIPTOR' : _FIBONACCINUMBER,
  '__module__' : 'maths_pb2'
  # @@protoc_insertion_point(class_scope:grpc_experimentation.FibonacciNumber)
  })
_sym_db.RegisterMessage(FibonacciNumber)

TimeStamp = _reflection.GeneratedProtocolMessageType('TimeStamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'maths_pb2'
  # @@protoc_insertion_point(class_scope:grpc_experimentation.TimeStamp)
  })
_sym_db.RegisterMessage(TimeStamp)


DESCRIPTOR._options = None

_MATHS = _descriptor.ServiceDescriptor(
  name='Maths',
  full_name='grpc_experimentation.Maths',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=229,
  serialized_end=491,
  methods=[
  _descriptor.MethodDescriptor(
    name='Sum',
    full_name='grpc_experimentation.Maths.Sum',
    index=0,
    containing_service=None,
    input_type=_SUMINPUT,
    output_type=_SUMRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFibonacciNumberStream',
    full_name='grpc_experimentation.Maths.GetFibonacciNumberStream',
    index=1,
    containing_service=None,
    input_type=_FIBONACCISTART,
    output_type=_FIBONACCINUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Time',
    full_name='grpc_experimentation.Maths.Time',
    index=2,
    containing_service=None,
    input_type=_TIMESTAMP,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MATHS)

DESCRIPTOR.services_by_name['Maths'] = _MATHS

# @@protoc_insertion_point(module_scope)
