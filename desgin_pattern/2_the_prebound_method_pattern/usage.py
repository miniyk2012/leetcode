from random import randint, randrange
import threading

print(randint)
print(randrange)


def anther_thread():
    from random import Random
    randint = Random().randint
    print('another', randint)


threading.Thread(target=anther_thread, args=()).start()
