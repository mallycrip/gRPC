import grpc
from concurrent import futures

from grpc_application.config.app_config import DevLevelConfig
from grpc_application.app.servicers.example import register_example_servicers


def register_servicers(app):
    register_example_servicers(app)


def create_app():
    app = grpc.server(futures.ThreadPoolExecutor(max_workers=DevLevelConfig.worker_node))
    app.add_insecure_port("localhost:50051")

    register_servicers(app)
    return app
