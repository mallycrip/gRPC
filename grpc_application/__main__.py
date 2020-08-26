import time
from grpc_application.app import create_app
from grpc_application.config.app_config import DevLevelConfig


if __name__ == "__main__":
    app = create_app()
    app.start()

    try:
        print("* Running on "+ DevLevelConfig._address)
        while True:
            time.sleep(600)
    except KeyboardInterrupt:
        exit()