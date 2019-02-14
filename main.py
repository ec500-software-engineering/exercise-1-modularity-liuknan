from AiModule import AiModule as AI
from UserInterface_module import userInterface
import Input_Module_lkn as I
from Alert_module import Alert
from queue import Queue
import threading
import time
# from storage import storage as St
def Input(BoQinput):
    while True:
        #input
        I.rand_input(BoQinput)
        time.sleep(2)

def middle(BoQinput, BoQoutput):
    while True:
        # storage
        # for i in range(len(bo)):
        #     S = St(bo[i],bp[i],pul[i])
        # AI
        if not BoQinput.empty():
            bo = BoQinput.get_nowait()
            # bp = BpQinput.get_nowait()
            # pul = PulQinput.get_nowait()
            #
            #
            # A = AI()
            # A.input_check(bo, bp, pul)
            # predBloodOxygen, predBloodPressure, prePulse = A.predict()
            # # Alert
            # Alt = Alert()
            # for k in range(len(bo)):
            #     boi = bo[k], 0
            #     bpi = bp[k], 1
            #     puli = pul[k], 2
            #     boa = Alt.Alert_for_three_categories_input(boi)
            #     bpa = Alt.Alert_for_three_categories_input(bpi)
            #     pula = Alt.Alert_for_three_categories_input(puli)
            BoQoutput.put_nowait(bo)
            # BpQoutput.put_nowait(bp)
            # PulQoutput.put_nowait(pul)
            time.sleep(2)

def Output(BoQoutput):
    while True:
        #Interface
        if not BoQoutput.empty():
            bo = BoQoutput.get_nowait()
            print(bo)

            U = userInterface()
            # U.getFromData(BoQoutput)
            time.sleep(2)

if __name__ == '__main__':
    BoQinput = Queue()
    BoQoutput = Queue()
    t1 = threading.Thread(target= Input, args= (BoQinput,))
    t2 = threading.Thread(target= middle, args= (BoQinput, BoQoutput,))
    t3 = threading.Thread(target= Output, args= (BoQoutput,))
    t1.start()
    t2.start()
    t3.start()



