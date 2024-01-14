from service_queue import ServiceQueue


def catch_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("Thank you for using the service queue!")
        except:
            print("Something went wrong.")

    return inner


@catch_error
def main():
    service_queue = ServiceQueue()
    print("Welcome to the service queue!")

    while True:
        service_queue.generate_request()
        service_queue.process_request()


if __name__ == "__main__":
    main()
