from grpc_application.app.servicers.example.example1 import Example1
from grpc_application.app.servicers.example.example2 import Example2

from grpc_application.proto.example1 import example1_pb2_grpc
from grpc_application.proto.example2 import example2_pb2_grpc

def register_example_servicers(app):
    example1_pb2_grpc.add_Example1Servicer_to_server(Example1(), app)
    example2_pb2_grpc.add_Example2Servicer_to_server(Example2(), app)