from multiprocessing import Queue
import random
def read_data(path):
    time = []
    value = []
    try:
        with open(path,'r') as f:
            data = f.readline()
            if data:
                for i in data:
                    i = i.split()
                    for item in i:
                        value.append(float(item))
                print("Read data successfully\n")
                return value
            else:
                print("Empty data file!\n")
                return 2
    except:
        print("Error:No input data\n")

def rand_input(InputQ):
    while True:
        value1 = random.random()
        value2 = random.random()
        value3 = random.random()
        InputQ.put([value1,value2,value3])

def read_Q(Q):
    while True:
        value = Q.get(True)
