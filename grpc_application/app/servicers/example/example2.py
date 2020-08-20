from grpc_application.proto.example2 import example2_pb2, example2_pb2_grpc
from grpc_application.app.services.example.example1 import Example1Service


class Example2(example2_pb2_grpc.Example2Servicer):
    def CreateData2(self, request, context):
        return Example1Service.create_data(request)


    def ReadData2(self, request, context):
        return Example1Service.read_data(request)