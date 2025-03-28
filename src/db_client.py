import logging

import grpc
import testing_pb2
import testing_pb2_grpc

def streamData(dataDict):
    for x in dataDict.keys():
        yield testing_pb2.DataRequest(key=x, value=dataDict[x])

def run():
    node1Data = {0: 12, 1: 34, 2: -7}
    node2Data = {3: 68, 4: 0, 5: 24}

    print("Attempting to connect to DBNode...")
    # Node 1
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = testing_pb2_grpc.DBNodeStub(channel)
        _ = stub.Insert(streamData(node1Data))
        response = stub.Count(testing_pb2.RangeRequest(idStart=0, idEnd=3))
        response2 = stub.Sum(testing_pb2.RangeRequest(idStart=0, idEnd=1))
    print("Result for Node 1 Count: " + str(response.result))
    print("Result for Node 1 Sum: " + str(response2.result))

    
    # Node 2
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = testing_pb2_grpc.DBNodeStub(channel)
        _ = stub.Insert(streamData(node2Data))
        response = stub.Count(testing_pb2.RangeRequest(idStart=5, idEnd=6))
        response2 = stub.Sum(testing_pb2.RangeRequest(idStart=4, idEnd=6))
    print("Result for Node 2 Count: " + str(response.result))
    print("Result for Node 2 Sum: " + str(response2.result))


if __name__ == "__main__":
    logging.basicConfig()
    run()