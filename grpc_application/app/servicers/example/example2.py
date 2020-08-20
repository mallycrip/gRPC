class Example2(example2_pb2_grpc.Example2Servicer):
    def CreateData2(self, request, context):
        print("CreatedData1")
        if request.data is None: return example2_pb2.CreateData2Response(message="No Context", code=400)
        return example2_pb2.CreateData2Response(message="Created in 2", code=201)