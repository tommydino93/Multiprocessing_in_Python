import multiprocessing as mp
import time


def wait(seconds: int):
    """This function takes as input an int number N, wait for N seconds and prints the number of seconds waited
    Args:
        seconds (int): number of seconds to wait
    Returns:
        None
    """
    time.sleep(seconds)
    print("Slept {0} seconds".format(seconds))


# ------------------------------------------- SEQUENTIAL APPROACH ------------------------------------------------------
start_sequential = time.time()  # start timer of sequential approach
for i in range(1, 5):  # call function 4 times sequentially (i.e. without multiprocessing)
    wait(2)  # wait 2 seconds
end_sequential = time.time()  # stop timer of sequential approach
print("Sequential approach took {:.2f} seconds\n".format(end_sequential-start_sequential))

# ----------------------------------------- MULTIPROCESSING APPROACH ----------------------------------------------------
num_workers = mp.cpu_count()  # save number of available CPUs (threads)
pool = mp.Pool(processes=num_workers)  # create pool object and set as many processes as there are CPUs
start_mp = time.time()  # start timer of multiprocessing approach
results = [pool.apply_async(wait, args=(2,)) for i in range(1, 5)]  # apply function asyncronously using pool of processes
pool.close()  # prevent any more tasks from being submitted to the pool.
pool.join()  # wait for everything on the queue to be processed
end_mp = time.time()  # stop timer of multiprocessing approach
print("Multiprocessing approach took {:.2f} seconds".format(end_mp-start_mp))
