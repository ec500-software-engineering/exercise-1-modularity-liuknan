from AiModule import AiModule as AI
from UserInterface_module import userInterface
import Input_Module_lkn as Inp
from Alert_module import Alert
from queue import Queue
import threading
import time

# from storage import storage as St
def Input(BoQinput):
    while True:
        #input
        Inp.rand_input(BoQinput)
        time.sleep(2)

def middle(BoQinput, BoQoutput, Pred, AlertQ):
    while True:

        if not BoQinput.empty():
            value = BoQinput.get_nowait()
            bo = value[0]
            bp = value[1]
            pul = value[2]
            #AI
            A = AI()
            A.input_check(bo, bp, pul)
            predBloodOxygen, predBloodPressure, prePulse = A.predict()
            pred_info = predBloodOxygen, predBloodPressure, prePulse
            Pred.put_nowait(pred_info)
            # Alert
            Alt = Alert()
            boi = bo, 0
            bpi = bp, 1
            puli = pul, 2
            Alt.Alert_for_three_categories_input(boi)
            Alt.Alert_for_three_categories_input(bpi)
            Alt.Alert_for_three_categories_input(puli)
            alert = Alt.Alert_Output()
            AlertQ.put_nowait(alert)
            BoQoutput.put_nowait(value)
            time.sleep(2)


def Output(BoQoutput, Pred, AlertQ):
    while True:
        #Interface
        if not BoQoutput.empty():
            value = BoQoutput.get_nowait()
            pred = Pred.get_nowait()
            bo = value[0]
            bp = value[1]
            pul = value[2]
            Alert_info = AlertQ.get_nowait()
            print("Blood Oxygen:%f\nBlood presure:%f\nPulse:%f\n" % (bo,bp,pul))
            print("Prediction:",pred,"\n")
            print("Alert information:",Alert_info,"\n")
            U = userInterface()
            U.getFromData(bo,bp,pul)
            time.sleep(2)

if __name__ == '__main__':
    BoQinput = Queue()
    BoQoutput = Queue()
    Pred = Queue()
    AlertQ = Queue()
    t1 = threading.Thread(target= Input, args= (BoQinput,))
    t2 = threading.Thread(target= middle, args= (BoQinput, BoQoutput,Pred, AlertQ,))
    t3 = threading.Thread(target= Output, args= (BoQoutput, Pred, AlertQ,))
    t1.start()
    t2.start()
    t3.start()



