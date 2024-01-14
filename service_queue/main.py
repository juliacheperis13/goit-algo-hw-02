from service_queue import ServiceQueue


def main():
    service_queue = ServiceQueue()
    print("Welcome to the service queue!")

    while True:
        service_queue.generate_request()
        service_queue.process_request()


if __name__ == "__main__":
    main()
