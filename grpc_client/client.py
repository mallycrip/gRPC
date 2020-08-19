from __future__ import print_function

import grpc
from proto.example1 import example1_pb2, example1_pb2_grpc
from proto.example2 import example2_pb2, example2_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = example1_pb2_grpc.Example1Stub(channel)
    response = stub.CreateData1(example1_pb2.CreateData1Request(header="hello", data="mally"))

    print("Greeter client received : " + response.message)

if __name__ == "__main__":
    run()