import multiprocessing
import time

def task():
    print("Empezando tarea")
    time.sleep(2)

if __name__ == '__main__':
    ti = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    tf = time.perf_counter()

    print("el programa termino en: " + str(tf - ti) + " segundos" )