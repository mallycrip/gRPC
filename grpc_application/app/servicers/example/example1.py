from grpc_application.proto.example1 import example1_pb2_grpc, example1_pb2
from grpc_application.app.services.example.example1 import Example1Service


class Example1(example1_pb2_grpc.Example1Servicer):
    def CreateData1(self, request, context):
        return Example1Service.create_data(request)


    def ReadData1(self, request, context):
        return Example1Service.read_data(request)