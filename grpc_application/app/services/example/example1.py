from grpc_application.proto.example1 import example1_pb2_grpc, example1_pb2


class Example1Service:
    @classmethod
    def create_data(cls, request):
        message = f"Create {request.data}"

        return example1_pb2.CreateData1Response(
            message=message, 
            code=201
        )

    @classmethod
    def read_data(cls, request):
        header = "Example Header"
        data = "Example Data"
        message = "OK"
        code = 200

        return example1_pb2.ReadData1Response(
            header = header,
            data = data,
            message = message,
            code = code
        )