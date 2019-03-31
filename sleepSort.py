import time
import threading


class SleeperThread (threading.Thread):

    def __init__(self, line, results):
        threading.Thread.__init__(self)
        self.line = line
        self.results = results

    def run(self):
        return sleep_sort(self.line, self.results)


def sleep_sort(amount, results):
    time.sleep(amount)
    results.append(amount)
    return amount

def issorted(list_of_numbers):
    test = list_of_numbers.copy()
    test.sort()
    return list_of_numbers == test

def min_max(data):

    results = [(item - min(data)) / (max(data) - min(data)) for item in data]
    # results = [item / max(data) for item in data]

    return results

def scale_between(data, start = 0, end = 10):
    width = end - start
    res = [(item - min(data))/(max(data) - min(data)) * width + start for item in data]

    return res


def start_sort(data, results):
    threads = []

    # normed_data = [float(i)/sum(data) for i in data]
    # normed_data = min_max(data)
    normed_data = scale_between(data, end = 5)

    for index, line in enumerate(normed_data):
        thread = SleeperThread(line, results)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for threads in threads:
        threads.join()

if __name__ == "__main__":
    import random

    items = [2,4,5,2,10,100, 2303, 3040]
    size_of_array = 1000


    items = [random.randint(1, 100) for i in range(size_of_array)]

    results = []

    start_sort(items, results)

    #print(results)
    print(issorted(results))
