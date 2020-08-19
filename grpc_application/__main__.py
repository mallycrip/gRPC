import time
from grpc_application.app import create_app



if __name__ == "__main__":
    app = create_app()
    app.start()

    try:
        print("[-] Server run")
        while True:
            time.sleep(600)
    except KeyboardInterrupt:
        exit()