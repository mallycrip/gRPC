import grpc
from concurrent import futures

from grpc_application.proto.example1 import example1_pb2, example1_pb2_grpc
from grpc_application.proto.example2 import example2_pb2, example2_pb2_grpc
from grpc_application.config.app_config import DevLevelConfig

class Example1(example1_pb2_grpc.Example1Servicer):
    def CreateData1(self, request, context):
        print("CreatedData1")
        if request.data is None: return example1_pb2.CreateData1Response(message="No Context", code=400)
        return example1_pb2.CreateData1Response(message="Created in 1", code=201)

class Example2(example2_pb2_grpc.Example2Servicer):
    def CreateData2(self, request, context):
        print("CreatedData1")
        if request.data is None: return example2_pb2.CreateData2Response(message="No Context", code=400)
        return example2_pb2.CreateData2Response(message="Created in 2", code=201)

def create_app():
    app = grpc.server(futures.ThreadPoolExecutor(max_workers=DevLevelConfig.worker_node))
    example1_pb2_grpc.add_Example1Servicer_to_server(Example1(), app)
    example2_pb2_grpc.add_Example2Servicer_to_server(Example2(), app)
    app.add_insecure_port("localhost:50051")
    return app
