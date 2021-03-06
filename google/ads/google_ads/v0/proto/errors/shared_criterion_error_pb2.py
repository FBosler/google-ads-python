# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/shared_criterion_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/shared_criterion_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v0.errorsB\031SharedCriterionErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors\352\002\"Google::Ads::GoogleAds::V0::Errors'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v0/proto/errors/shared_criterion_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\x84\x01\n\x18SharedCriterionErrorEnum\"h\n\x14SharedCriterionError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x32\n.CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE\x10\x02\x42\xf4\x01\n\"com.google.ads.googleads.v0.errorsB\x19SharedCriterionErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errors\xea\x02\"Google::Ads::GoogleAds::V0::Errorsb\x06proto3')
)



_SHAREDCRITERIONERRORENUM_SHAREDCRITERIONERROR = _descriptor.EnumDescriptor(
  name='SharedCriterionError',
  full_name='google.ads.googleads.v0.errors.SharedCriterionErrorEnum.SharedCriterionError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=130,
  serialized_end=234,
)
_sym_db.RegisterEnumDescriptor(_SHAREDCRITERIONERRORENUM_SHAREDCRITERIONERROR)


_SHAREDCRITERIONERRORENUM = _descriptor.Descriptor(
  name='SharedCriterionErrorEnum',
  full_name='google.ads.googleads.v0.errors.SharedCriterionErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHAREDCRITERIONERRORENUM_SHAREDCRITERIONERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=234,
)

_SHAREDCRITERIONERRORENUM_SHAREDCRITERIONERROR.containing_type = _SHAREDCRITERIONERRORENUM
DESCRIPTOR.message_types_by_name['SharedCriterionErrorEnum'] = _SHAREDCRITERIONERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedCriterionErrorEnum = _reflection.GeneratedProtocolMessageType('SharedCriterionErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDCRITERIONERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.shared_criterion_error_pb2'
  ,
  __doc__ = """Container for enum describing possible shared criterion errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.SharedCriterionErrorEnum)
  ))
_sym_db.RegisterMessage(SharedCriterionErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
