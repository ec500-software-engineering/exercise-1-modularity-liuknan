"""
In this architecture, I used my own input module, Wenjie Luo's Alert Module Xiang Li's AI module and Shilu Wu's
User Interface module. The architecture includes three parts. The Input part is my Input module, and the middle part
includes Alert module and AI module. The Output part is the User Interface. I use four Queues to let each part
communicates with each other. The input part gets data and send it to middle part with BoQinput. The middle part
processes the data and send the prediction data, alert signal and output data like blood pressure to the User Interface.
Then the User Interface will display the data.
"""
from AiModule import AiModule as AI
from UserInterface_module import userInterface
import Input_Module_lkn as Inp
from Alert_module import Alert
from queue import Queue
import threading
import time


def Input(BoQinput):
    """
    It's the input Moudle, which gets data from machine and pass data to other modules.
    :param BoQinput: It's a queue for input to communicate input data between modules.
    :return:
    """
    while True:
        # input
        Inp.rand_input(BoQinput)  # Generating random data as input.
        time.sleep(2)


def middle(BoQinput, BoQoutput, Pred, AlertQ):
    """
    Middle part contains several modules, including AI module and Alert module.
    :param BoQinput: It's a input queue.
    :param BoQoutput: It's a queue and it pass data to output module.
    :param Pred: A queue for prediction data.
    :param AlertQ: A queue for alert module.
    :return:
    """
    while True:
        if not BoQinput.empty():
            value = BoQinput.get_nowait()  # getting data from queue.
            bo = value[0]  # blood oxygen
            bp = value[1]  # blood pressure
            pul = value[2]  # pulse
            # AI
            A = AI()  # AI module
            A.input_check(bo, bp, pul)  # check the type of input
            predBloodOxygen, predBloodPressure, prePulse = A.predict()  # prediction output
            pred_info = predBloodOxygen, predBloodPressure, prePulse
            Pred.put_nowait(pred_info)
            # Alert
            Alt = Alert()  # Alert Module
            boi = bo, 0  # the last number stands for the type of the data
            bpi = bp, 1
            puli = pul, 2
            Alt.Alert_for_three_categories_input(boi)  # data check
            Alt.Alert_for_three_categories_input(bpi)
            Alt.Alert_for_three_categories_input(puli)
            alert = Alt.Alert_Output()
            AlertQ.put_nowait(alert)
            BoQoutput.put_nowait(value)
            time.sleep(2)


def Output(BoQoutput, Pred, AlertQ):
    """
    It's the output part, could be seen as interface module.
    :param BoQoutput: A queue for output data.
    :param Pred: Queue for prediction data.
    :param AlertQ: Queue for Alert information.
    :return:
    """
    while True:
        # Interface
        if not BoQoutput.empty():
            value = BoQoutput.get_nowait()
            pred = Pred.get_nowait()
            bo = value[0]
            bp = value[1]
            pul = value[2]
            Alert_info = AlertQ.get_nowait()
            print("Blood Oxygen:%f\nBlood presure:%f\nPulse:%f\n" % (bo, bp, pul))
            print("Prediction:", pred, "\n")
            print("Alert information:", Alert_info, "\n")
            U = userInterface()
            U.getFromData(bo, bp, pul)
            time.sleep(2)


if __name__ == '__main__':
    BoQinput = Queue()
    BoQoutput = Queue()
    Pred = Queue()
    AlertQ = Queue()
    t1 = threading.Thread(target=Input, args=(BoQinput,))
    t2 = threading.Thread(target=middle, args=(BoQinput, BoQoutput, Pred, AlertQ,))
    t3 = threading.Thread(target=Output, args=(BoQoutput, Pred, AlertQ,))
    t1.start()
    t2.start()
    t3.start()
