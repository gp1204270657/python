from concurrent.futures import ThreadPoolExecutor


def say_hello():
    print("hello")

excute=ThreadPoolExecutor(10)
for i in range(0,7):
    excute.submit(say_hello)