# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.mdb.mongodb.v1 import user_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__pb2
from yandex.cloud.mdb.mongodb.v1 import user_service_pb2 as yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class UserServiceStub(object):
  """A set of methods for managing MongoDB User resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.UserService/Get',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.GetUserRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__pb2.User.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.UserService/List',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.ListUsersRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.ListUsersResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.UserService/Create',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.UserService/Update',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.UpdateUserRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.UserService/Delete',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.DeleteUserRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.GrantPermission = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.UserService/GrantPermission',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.GrantUserPermissionRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.RevokePermission = channel.unary_unary(
        '/yandex.cloud.mdb.mongodb.v1.UserService/RevokePermission',
        request_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.RevokeUserPermissionRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )


class UserServiceServicer(object):
  """A set of methods for managing MongoDB User resources.
  """

  def Get(self, request, context):
    """Returns the specified MongoDB User resource.

    To get the list of available MongoDB User resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of MongoDB User resources in the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a MongoDB user in the specified cluster.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified MongoDB user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified MongoDB user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GrantPermission(self, request, context):
    """Grants permission to the specified MongoDB user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RevokePermission(self, request, context):
    """Revokes permission from the specified MongoDB user.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.GetUserRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__pb2.User.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.ListUsersRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.ListUsersResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.CreateUserRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.UpdateUserRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.DeleteUserRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'GrantPermission': grpc.unary_unary_rpc_method_handler(
          servicer.GrantPermission,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.GrantUserPermissionRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'RevokePermission': grpc.unary_unary_rpc_method_handler(
          servicer.RevokePermission,
          request_deserializer=yandex_dot_cloud_dot_mdb_dot_mongodb_dot_v1_dot_user__service__pb2.RevokeUserPermissionRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.mdb.mongodb.v1.UserService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
