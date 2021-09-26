import grpc
import threading, time

import maths_pb2_grpc
import maths_pb2

def sum_test(stub):
    a = 5.3
    b = 2.7
    try:
        sum_result = stub.Sum( maths_pb2.SumInput(a=a, b=b) )
        print(f"{a} + {b} = {sum_result.result}")
    except grpc.RpcError:
        print("Sum: Unable to Connect to server!")

def fibonacci_stream(stub, channel):
    f1 = 1
    print(f1)
    f2 = 2
    print(f2)
    fibonacci_start = maths_pb2.FibonacciStart(f1=f1, f2=f2)
    try:
        fibonacci_number_generator =  stub.GetFibonacciNumberStream(fibonacci_start, wait_for_ready=True)
        lock = threading.Lock()
        lock.acquire()
        cancel_thread = threading.Thread(target=cancel_timer, args=(fibonacci_number_generator,lock,))
        cancel_thread.start()
        for fibonacci_number in fibonacci_number_generator:
            print(fibonacci_number.f)
            if fibonacci_number.f > 500:
                lock.release()
    except grpc.RpcError:
        print("End of Fibonacci Number Stream!")
    cancel_thread.join()

def cancel_timer(it, lock):
    lock.acquire()
    print('Canceled!')
    it.cancel()

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = maths_pb2_grpc.MathsStub(channel)

    # sum_test(stub)
    fibonacci_stream(stub, channel)

if __name__ == "__main__":
    main()
