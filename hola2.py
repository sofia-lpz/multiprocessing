import time
#from threading import Thread
from multiprocessing import Process

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    
    t1 = Process(target=countdown, args=(COUNT/2,))
    t2 = Process(target=countdown, args=(COUNT/2,))

    ti = time.time()
    t1.start()
    t2.start()

    #countdown(COUNT)

    t1.join()
    t2.join()

    tf = time.time()

    print("el programa termino en: " + str(tf - ti) + " segundos" )