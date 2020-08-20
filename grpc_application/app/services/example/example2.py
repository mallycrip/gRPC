from grpc_application.proto.example2 import example2_pb2, example2_pb2_grpc


class Example2Service:
    @classmethod
    def create_data(cls, request):
        message = f"Create {request.data}"

        return example2_pb2.CreateData2Response(
            message=message, 
            code=201
        )

    @classmethod
    def read_data(cls, request):
        header = "Example2 Header"
        data = "Example2 Data"
        message = "OK"
        code = 200

        return example2_pb2.ReadData2Response(
            header = header,
            data = data,
            message = message,
            code = code
        )