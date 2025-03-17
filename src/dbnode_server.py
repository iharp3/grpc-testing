from concurrent import futures
import logging

import sys
import grpc
import testing_pb2
import testing_pb2_grpc

class DBNode(testing_pb2_grpc.DBNodeServicer):
    data = dict()

    def Count(self, request, context):
        count = 0

        for x in self.data.keys():
            if request.idStart <= x <= request.idEnd:
                count += 1 

        return testing_pb2.SingleResponse(result=count)


    def Sum(self, request, context):
        sum = 0
        
        for x in self.data.keys():
            if request.idStart <= x <= request.idEnd:
                sum += self.data[x] 
        
        return testing_pb2.SingleResponse(result=sum)
    
    def Insert(self, request_iterator, context):
        for request in request_iterator:
            self.data[request.key] = request.value
        return testing_pb2.InsertDataAcknowledgement()



def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    testing_pb2_grpc.add_DBNodeServicer_to_server(DBNode(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    if len(sys.argv) < 2:
        print("Usage: python dbnode_server.py [Port Number]")
    port = sys.argv[1]
    serve(port)