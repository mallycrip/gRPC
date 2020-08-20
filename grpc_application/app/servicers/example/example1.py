class Example1(example1_pb2_grpc.Example1Servicer):
    def CreateData1(self, request, context):
        print("CreatedData1")
        if request.data is None: return example1_pb2.CreateData1Response(message="No Context", code=400)
        return example1_pb2.CreateData1Response(message="Created in 1", code=201)