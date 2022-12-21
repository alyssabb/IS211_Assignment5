# Part 1

import csv


class Request:
    def __init__(self, time, path, processing_time):
        self.time = time
        self.path = path
        self.processing_time = processing_time


class Server:
    def __init__(self):
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.processing_time


def simulateOneServer(filename):
    server = Server()
    requests = []
    waiting_times = []

    # Read input file and create Request objects
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            requests.append(Request(int(row[0]), row[1], int(row[2])))

    # Track the time and process requests
    for request in requests:
        server.start_next(request)
        waiting_times.append(server.time_remaining)
        server.tick()

    # Calculate and return average waiting time
    return sum(waiting_times) / len(waiting_times)


def main(filename):
    average_wait_time = simulateOneServer(filename)
    print(f'Average wait time: {average_wait_time} seconds')


if __name__ == '__main__':
    main(sys.argv[1])



# PART 2
import csv


class Request:
    def __init__(self, time, path, processing_time):
        self.time = time
        self.path = path
        self.processing_time = processing_time


class Server:
    def __init__(self):
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.processing_time


def simulateOneServer(filename):
    server = Server()
    requests = []
    waiting_times = []

    # Read input file and create Request objects
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            requests.append(Request(int(row[0]), row[1], int(row[2])))

    # Track the time and process requests
    for request in requests:
        server.start_next(request)
        waiting_times.append(server.time_remaining)
        server.tick()

    # Calculate and return average waiting time
    return sum(waiting_times) / len(waiting_times)


def simulateManyServers(filename, num_servers):
    servers = []
    for i in range(num_servers):
        servers.append(Server())
    requests = []
    waiting_times = []

    # Read input file and create Request objects
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            requests.append(Request(int(row[0]), row[1], int(row[2])))

    # Track the time and process requests
    for request in requests:
        # Find the next available server
        server = next(s for s in servers if not s.busy())
        server.start_next(request)
        waiting_times.append(server.time_remaining)
        for s in servers:
            s.tick()

    # Calculate and return average waiting time
    return sum(waiting_times) / len(waiting_times)


def main(filename, num_servers=1):
    if num_servers == 1:
        average_wait_time = simulateOneServer(filename)
    else:
        average_wait_time = simulateManyServers(filename, num_servers)
    print(f'Average wait time: {average_wait_time} seconds')


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
