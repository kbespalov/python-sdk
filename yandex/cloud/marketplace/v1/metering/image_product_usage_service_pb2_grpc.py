# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.marketplace.v1.metering import image_product_usage_service_pb2 as yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2


class ImageProductUsageServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Write = channel.unary_unary(
        '/yandex.cloud.marketplace.v1.metering.ImageProductUsageService/Write',
        request_serializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageResponse.FromString,
        )


class ImageProductUsageServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Write(self, request, context):
    """Writes image product's usage (authenticated by user's service account)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ImageProductUsageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Write': grpc.unary_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_marketplace_dot_v1_dot_metering_dot_image__product__usage__service__pb2.WriteImageProductUsageResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.marketplace.v1.metering.ImageProductUsageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
