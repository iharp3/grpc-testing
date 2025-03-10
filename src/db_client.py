import logging

import grpc
import testing_pb2
import testing_pb2_grpc


def run():
    print("Attempting to connect to DBNode...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = testing_pb2_grpc.DBNodeStub(channel)
        response = stub.Count(testing_pb2.RangeRequest(idStart=0, idEnd=3))
        response2 = stub.Sum(testing_pb2.RangeRequest(idStart=0, idEnd=3))
    print("Result for Count: " + str(response.result))
    print("Result for Sum: " + str(response2.result))


if __name__ == "__main__":
    logging.basicConfig()
    run()