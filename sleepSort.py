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

def start_sort(inp, results):
    threads = []

    for index, line in enumerate(inp):
        thread = SleeperThread(line, results)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for threads in threads:
        threads.join()




if __name__ == "__main__":

    items = [2,4,5,2,10,1]

    normed_data = [float(i)/sum(items) for i in items]


    results = []
    #np.interp(a, (a.min(), a.max()), (-1, +1))

    start_sort(normed_data, results)

    print(results)
    print(issorted(results))
