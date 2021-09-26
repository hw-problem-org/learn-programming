#!/usr/bin/python3
from concurrent import futures
import time
import grpc

import perform_pb2, perform_pb2_grpc


class PerformServicer(perform_pb2_grpc.TestServiceServicer):
    def __init__(self):
        pass


    def GetTime(self, _, context):
        time_now = int(time.time() * 1000)
        return perform_pb2.TimeStamp(milliseconds=time_now)
        
    def Ping(self, timestamp, context):
        time_now = int(time.time() * 1000)
        latency = time_now - timestamp.milliseconds
        print(f"Latency: {latency}")
        return perform_pb2.EmptyMsg()


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=30))
    
    perform_pb2_grpc.add_TestServiceServicer_to_server(PerformServicer(), server)

    ip = "192.168.43.21"
    port = "50051"
    server.add_insecure_port(f"{ip}:{port}")

    server.start()
    print(f"Mobot Server started at {ip}:{port}")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()
