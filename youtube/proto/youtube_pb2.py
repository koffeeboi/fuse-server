# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/youtube.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/youtube.proto',
  package='youtube',
  syntax='proto3',
  serialized_pb=_b('\n\x13proto/youtube.proto\x12\x07youtube\x1a\x1cgoogle/api/annotations.proto\"\x1d\n\x0eYtMusicRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"z\n\x0cYtMusicReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x06status\x18\x02 \x01(\x0e\x32\x1c.youtube.YtMusicReply.Status\".\n\x06Status\x12\x0f\n\x0bMUSIC_EXIST\x10\x00\x12\x13\n\x0fMUSIC_NOT_EXIST\x10\x01\x32s\n\x0eYoutubeService\x12\x61\n\x10\x46indYoutubeMusic\x12\x17.youtube.YtMusicRequest\x1a\x15.youtube.YtMusicReply\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/youtube/music/get:\x01*b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_YTMUSICREPLY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='youtube.YtMusicReply.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MUSIC_EXIST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MUSIC_NOT_EXIST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=169,
  serialized_end=215,
)
_sym_db.RegisterEnumDescriptor(_YTMUSICREPLY_STATUS)


_YTMUSICREQUEST = _descriptor.Descriptor(
  name='YtMusicRequest',
  full_name='youtube.YtMusicRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='youtube.YtMusicRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=91,
)


_YTMUSICREPLY = _descriptor.Descriptor(
  name='YtMusicReply',
  full_name='youtube.YtMusicReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='youtube.YtMusicReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='youtube.YtMusicReply.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _YTMUSICREPLY_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=215,
)

_YTMUSICREPLY.fields_by_name['status'].enum_type = _YTMUSICREPLY_STATUS
_YTMUSICREPLY_STATUS.containing_type = _YTMUSICREPLY
DESCRIPTOR.message_types_by_name['YtMusicRequest'] = _YTMUSICREQUEST
DESCRIPTOR.message_types_by_name['YtMusicReply'] = _YTMUSICREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

YtMusicRequest = _reflection.GeneratedProtocolMessageType('YtMusicRequest', (_message.Message,), dict(
  DESCRIPTOR = _YTMUSICREQUEST,
  __module__ = 'proto.youtube_pb2'
  # @@protoc_insertion_point(class_scope:youtube.YtMusicRequest)
  ))
_sym_db.RegisterMessage(YtMusicRequest)

YtMusicReply = _reflection.GeneratedProtocolMessageType('YtMusicReply', (_message.Message,), dict(
  DESCRIPTOR = _YTMUSICREPLY,
  __module__ = 'proto.youtube_pb2'
  # @@protoc_insertion_point(class_scope:youtube.YtMusicReply)
  ))
_sym_db.RegisterMessage(YtMusicReply)



_YOUTUBESERVICE = _descriptor.ServiceDescriptor(
  name='YoutubeService',
  full_name='youtube.YoutubeService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=217,
  serialized_end=332,
  methods=[
  _descriptor.MethodDescriptor(
    name='FindYoutubeMusic',
    full_name='youtube.YoutubeService.FindYoutubeMusic',
    index=0,
    containing_service=None,
    input_type=_YTMUSICREQUEST,
    output_type=_YTMUSICREPLY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\027\"\022/youtube/music/get:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_YOUTUBESERVICE)

DESCRIPTOR.services_by_name['YoutubeService'] = _YOUTUBESERVICE

# @@protoc_insertion_point(module_scope)
