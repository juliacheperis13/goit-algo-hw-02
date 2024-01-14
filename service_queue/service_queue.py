from queue import Queue
import random
import time


class Application:
    def __init__(self, id):
        self.id = id


class ServiceQueue:
    current_id = 0
    queue = Queue()
    start_time = 0
    finish_time = 0

    def generate_request(self):
        self.set_start_time()
        new_application = Application(self.current_id)
        self.imitate_delay()
        self.queue.put(new_application)
        print(f'Application #{self.current_id} was added.')
        self.current_id = self.current_id + 1

    def process_request(self):
        if not self.queue.empty():
            self.imitate_delay()
            self.set_end_time()

            current_application = self.queue.get()
            print(
                f'Application #{current_application.id} was processed. {self.get_time_dif()} seconds.')
            self.reset_time()
        else:
            print(f'Application queue is empty.')

    def imitate_delay(self):
        delay = random.random() * 3 + 1
        time.sleep(delay)

    def set_start_time(self):
        self.start_time = time.time()

    def set_end_time(self):
        self.end_time = time.time()

    def get_time_dif(self):
        return int(self.end_time - self.start_time)

    def reset_time(self):
        self.start_time = 0
        self.end_time = 0
