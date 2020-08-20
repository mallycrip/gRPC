import grpc
from concurrent import futures

from grpc_application.proto.example1 import example1_pb2, example1_pb2_grpc
from grpc_application.proto.example2 import example2_pb2, example2_pb2_grpc
from grpc_application.config.app_config import DevLevelConfig

def register_servicers(app):
    example1_pb2_grpc.add_Example1Servicer_to_server(Example1(), app)
    example2_pb2_grpc.add_Example2Servicer_to_server(Example2(), app)


def create_app():
    app = grpc.server(futures.ThreadPoolExecutor(max_workers=DevLevelConfig.worker_node))

    register_servicers(app)

    app.add_insecure_port("localhost:50051")
    return app
