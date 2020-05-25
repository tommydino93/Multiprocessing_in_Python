import multiprocessing as mp
import time

"""In this script we see how to get the returned outputs of a function called with a Pool of processes"""


def wait(seconds: int):
    """This function takes as input an int number N, waits for N seconds, prints N,
    and returns both N and its double.
    Args:
        seconds (int): number of seconds to wait
    Returns:
        seconds (int): number of seconds waited
        double (int): double the number of seconds waited
    """
    time.sleep(seconds)
    print("Slept {0} seconds".format(seconds))
    double = seconds * 2
    return seconds, double


start_mp = time.time()  # start timer
num_workers = mp.cpu_count()  # save number of available CPUs (threads)
pool = mp.Pool(processes=num_workers)  # create pool object and set as many processes as there are CPUs
results = [pool.apply_async(wait, args=(i,)) for i in range(1, 5)]  # invoke function asyncronously with Pool
pool.close()  # prevent any more tasks from being submitted to the pool
pool.join()  # wait for everything on the queue to be processed
end_mp = time.time()  # stop timer
print("\nOutputs:")
for result in results:
    print(result.get())
print("\nRunning time: {:.2f} seconds".format(end_mp-start_mp))

