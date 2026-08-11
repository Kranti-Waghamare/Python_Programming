import multiprocessing
import time
import os

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} PPID of SumEven : {os.getpid()}")
    Sum = 0

    for i in range(2, No, 2):
        Sum = Sum + i

    print("Summation of Even is : ", Sum)

def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} PPID of SumOdd : {os.getpid()}")

    Sum = 0

    for i in range(1, No, 2):
        Sum = Sum + i

    print("Summation of Odd is : ", Sum)
     
def main():
    print(f"PID of main : {os.getpid()} PPID of main : {os.getpid()}")

    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target= SumEven, args= (10000000,))
    t2 = multiprocessing.Process(target= SumOdd, args= (10000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time :.4f} seconds")

if __name__ == "__main__":
    main()