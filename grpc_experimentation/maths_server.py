from concurrent import futures
import grpc
import time

import maths_pb2_grpc
import maths_pb2

class Servicer(maths_pb2_grpc.Maths):
    def __init__(self):
        pass

    def Sum(self, sum_input, context):
        return maths_pb2.SumResult(result = sum_input.a + sum_input.b)

    def GetFibonacciNumberStream(self, fibonacci_start, context):
        f_tm2 = fibonacci_start.f1
        f_tm1 = fibonacci_start.f2
        print(context.is_active())
        try:
            while True:
                f_t = f_tm1 + f_tm2
                yield maths_pb2.FibonacciNumber(f=f_t)
                time.sleep(1)
                print(f_t)
                f_tm2 = f_tm1
                f_tm1 = f_t
        except:
            print(context.is_active())
            print("End of Fibonacci Number Stream!")

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=30))
    maths_pb2_grpc.add_MathsServicer_to_server(Servicer(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print(f"Maths Server started!")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    main()
