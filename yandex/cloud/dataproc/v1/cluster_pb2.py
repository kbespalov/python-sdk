# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/dataproc/v1/cluster.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud.dataproc.v1 import common_pb2 as yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yandex/cloud/dataproc/v1/cluster.proto',
  package='yandex.cloud.dataproc.v1',
  syntax='proto3',
  serialized_options=_b('\n\034yandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataproc'),
  serialized_pb=_b('\n&yandex/cloud/dataproc/v1/cluster.proto\x12\x18yandex.cloud.dataproc.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%yandex/cloud/dataproc/v1/common.proto\x1a\x1dyandex/cloud/validation.proto\"\x91\x05\n\x07\x43luster\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x04name\x18\x04 \x01(\tB\x08\x8a\xc8\x31\x04\x31-63\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05\x30-256\x12G\n\x06labels\x18\x06 \x03(\x0b\x32-.yandex.cloud.dataproc.v1.Cluster.LabelsEntryB\x08\x82\xc8\x31\x04<=64\x12\x38\n\nmonitoring\x18\x07 \x03(\x0b\x32$.yandex.cloud.dataproc.v1.Monitoring\x12\x37\n\x06\x63onfig\x18\x08 \x01(\x0b\x32\'.yandex.cloud.dataproc.v1.ClusterConfig\x12\x30\n\x06health\x18\t \x01(\x0e\x32 .yandex.cloud.dataproc.v1.Health\x12\x38\n\x06status\x18\n \x01(\x0e\x32(.yandex.cloud.dataproc.v1.Cluster.Status\x12\x0f\n\x07zone_id\x18\x0b \x01(\t\x12\x1a\n\x12service_account_id\x18\x0c \x01(\t\x12\x0e\n\x06\x62ucket\x18\r \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"k\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x0c\n\x08\x43REATING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0c\n\x08STARTING\x10\x06\"=\n\nMonitoring\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\"\x97\x03\n\x0cHadoopConfig\x12@\n\x08services\x18\x01 \x03(\x0e\x32..yandex.cloud.dataproc.v1.HadoopConfig.Service\x12J\n\nproperties\x18\x02 \x03(\x0b\x32\x36.yandex.cloud.dataproc.v1.HadoopConfig.PropertiesEntry\x12\x17\n\x0fssh_public_keys\x18\x03 \x03(\t\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xac\x01\n\x07Service\x12\x17\n\x13SERVICE_UNSPECIFIED\x10\x00\x12\x08\n\x04HDFS\x10\x01\x12\x08\n\x04YARN\x10\x02\x12\r\n\tMAPREDUCE\x10\x03\x12\x08\n\x04HIVE\x10\x04\x12\x07\n\x03TEZ\x10\x05\x12\r\n\tZOOKEEPER\x10\x06\x12\t\n\x05HBASE\x10\x07\x12\t\n\x05SQOOP\x10\x08\x12\t\n\x05\x46LUME\x10\t\x12\t\n\x05SPARK\x10\n\x12\x0c\n\x08ZEPPELIN\x10\x0b\x12\t\n\x05OOZIE\x10\x0c\"[\n\rClusterConfig\x12\x12\n\nversion_id\x18\x01 \x01(\t\x12\x36\n\x06hadoop\x18\x02 \x01(\x0b\x32&.yandex.cloud.dataproc.v1.HadoopConfigBe\n\x1cyandex.cloud.api.dataproc.v1ZEgithub.com/yandex-cloud/go-genproto/yandex/cloud/dataproc/v1;dataprocb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2.DESCRIPTOR,yandex_dot_cloud_dot_validation__pb2.DESCRIPTOR,])



_CLUSTER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='yandex.cloud.dataproc.v1.Cluster.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=722,
  serialized_end=829,
)
_sym_db.RegisterEnumDescriptor(_CLUSTER_STATUS)

_HADOOPCONFIG_SERVICE = _descriptor.EnumDescriptor(
  name='Service',
  full_name='yandex.cloud.dataproc.v1.HadoopConfig.Service',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SERVICE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HDFS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YARN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAPREDUCE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIVE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEZ', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZOOKEEPER', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HBASE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SQOOP', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLUME', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPARK', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZEPPELIN', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OOZIE', index=12, number=12,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1130,
  serialized_end=1302,
)
_sym_db.RegisterEnumDescriptor(_HADOOPCONFIG_SERVICE)


_CLUSTER_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='yandex.cloud.dataproc.v1.Cluster.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.dataproc.v1.Cluster.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.dataproc.v1.Cluster.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=675,
  serialized_end=720,
)

_CLUSTER = _descriptor.Descriptor(
  name='Cluster',
  full_name='yandex.cloud.dataproc.v1.Cluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yandex.cloud.dataproc.v1.Cluster.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder_id', full_name='yandex.cloud.dataproc.v1.Cluster.folder_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='yandex.cloud.dataproc.v1.Cluster.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.dataproc.v1.Cluster.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\0041-63'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.dataproc.v1.Cluster.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3101\0050-256'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='yandex.cloud.dataproc.v1.Cluster.labels', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\202\3101\004<=64'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monitoring', full_name='yandex.cloud.dataproc.v1.Cluster.monitoring', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='yandex.cloud.dataproc.v1.Cluster.config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='yandex.cloud.dataproc.v1.Cluster.health', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='yandex.cloud.dataproc.v1.Cluster.status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone_id', full_name='yandex.cloud.dataproc.v1.Cluster.zone_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='yandex.cloud.dataproc.v1.Cluster.service_account_id', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='yandex.cloud.dataproc.v1.Cluster.bucket', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTER_LABELSENTRY, ],
  enum_types=[
    _CLUSTER_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=829,
)


_MONITORING = _descriptor.Descriptor(
  name='Monitoring',
  full_name='yandex.cloud.dataproc.v1.Monitoring',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='yandex.cloud.dataproc.v1.Monitoring.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='yandex.cloud.dataproc.v1.Monitoring.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='yandex.cloud.dataproc.v1.Monitoring.link', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=831,
  serialized_end=892,
)


_HADOOPCONFIG_PROPERTIESENTRY = _descriptor.Descriptor(
  name='PropertiesEntry',
  full_name='yandex.cloud.dataproc.v1.HadoopConfig.PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='yandex.cloud.dataproc.v1.HadoopConfig.PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='yandex.cloud.dataproc.v1.HadoopConfig.PropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1078,
  serialized_end=1127,
)

_HADOOPCONFIG = _descriptor.Descriptor(
  name='HadoopConfig',
  full_name='yandex.cloud.dataproc.v1.HadoopConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='yandex.cloud.dataproc.v1.HadoopConfig.services', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='yandex.cloud.dataproc.v1.HadoopConfig.properties', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssh_public_keys', full_name='yandex.cloud.dataproc.v1.HadoopConfig.ssh_public_keys', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HADOOPCONFIG_PROPERTIESENTRY, ],
  enum_types=[
    _HADOOPCONFIG_SERVICE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=1302,
)


_CLUSTERCONFIG = _descriptor.Descriptor(
  name='ClusterConfig',
  full_name='yandex.cloud.dataproc.v1.ClusterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version_id', full_name='yandex.cloud.dataproc.v1.ClusterConfig.version_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hadoop', full_name='yandex.cloud.dataproc.v1.ClusterConfig.hadoop', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1304,
  serialized_end=1395,
)

_CLUSTER_LABELSENTRY.containing_type = _CLUSTER
_CLUSTER.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLUSTER.fields_by_name['labels'].message_type = _CLUSTER_LABELSENTRY
_CLUSTER.fields_by_name['monitoring'].message_type = _MONITORING
_CLUSTER.fields_by_name['config'].message_type = _CLUSTERCONFIG
_CLUSTER.fields_by_name['health'].enum_type = yandex_dot_cloud_dot_dataproc_dot_v1_dot_common__pb2._HEALTH
_CLUSTER.fields_by_name['status'].enum_type = _CLUSTER_STATUS
_CLUSTER_STATUS.containing_type = _CLUSTER
_HADOOPCONFIG_PROPERTIESENTRY.containing_type = _HADOOPCONFIG
_HADOOPCONFIG.fields_by_name['services'].enum_type = _HADOOPCONFIG_SERVICE
_HADOOPCONFIG.fields_by_name['properties'].message_type = _HADOOPCONFIG_PROPERTIESENTRY
_HADOOPCONFIG_SERVICE.containing_type = _HADOOPCONFIG
_CLUSTERCONFIG.fields_by_name['hadoop'].message_type = _HADOOPCONFIG
DESCRIPTOR.message_types_by_name['Cluster'] = _CLUSTER
DESCRIPTOR.message_types_by_name['Monitoring'] = _MONITORING
DESCRIPTOR.message_types_by_name['HadoopConfig'] = _HADOOPCONFIG
DESCRIPTOR.message_types_by_name['ClusterConfig'] = _CLUSTERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cluster = _reflection.GeneratedProtocolMessageType('Cluster', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTER_LABELSENTRY,
    '__module__' : 'yandex.cloud.dataproc.v1.cluster_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.Cluster.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _CLUSTER,
  '__module__' : 'yandex.cloud.dataproc.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.Cluster)
  })
_sym_db.RegisterMessage(Cluster)
_sym_db.RegisterMessage(Cluster.LabelsEntry)

Monitoring = _reflection.GeneratedProtocolMessageType('Monitoring', (_message.Message,), {
  'DESCRIPTOR' : _MONITORING,
  '__module__' : 'yandex.cloud.dataproc.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.Monitoring)
  })
_sym_db.RegisterMessage(Monitoring)

HadoopConfig = _reflection.GeneratedProtocolMessageType('HadoopConfig', (_message.Message,), {

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _HADOOPCONFIG_PROPERTIESENTRY,
    '__module__' : 'yandex.cloud.dataproc.v1.cluster_pb2'
    # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.HadoopConfig.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _HADOOPCONFIG,
  '__module__' : 'yandex.cloud.dataproc.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.HadoopConfig)
  })
_sym_db.RegisterMessage(HadoopConfig)
_sym_db.RegisterMessage(HadoopConfig.PropertiesEntry)

ClusterConfig = _reflection.GeneratedProtocolMessageType('ClusterConfig', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERCONFIG,
  '__module__' : 'yandex.cloud.dataproc.v1.cluster_pb2'
  # @@protoc_insertion_point(class_scope:yandex.cloud.dataproc.v1.ClusterConfig)
  })
_sym_db.RegisterMessage(ClusterConfig)


DESCRIPTOR._options = None
_CLUSTER_LABELSENTRY._options = None
_CLUSTER.fields_by_name['name']._options = None
_CLUSTER.fields_by_name['description']._options = None
_CLUSTER.fields_by_name['labels']._options = None
_HADOOPCONFIG_PROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
