"""
In this architecture, I used my own input module, Wenjie Luo's Alert Module Xiang Li's AI module and Shilu Wu's
User Interface module. The architecture includes three parts. The Input part is my Input module, and the middle part
includes Alert module and AI module. The Output part is the User Interface. I use four Queues to let each part
communicates with each other. The input part gets data and send it to middle part with BoQinput. The middle part
processes the data and send the prediction data, alert signal and output data like blood pressure to the User Interface.
Then the User Interface will display the data.
"""
from AiModule import AiModule as Ai
from UserInterface_module import userInterface
import Input_Module_lkn as Inp
from Alert_module import Alert
from queue import Queue
import threading
import time


class Medical():
    def __init__(self):
        self.BoQinput = Queue()
        self.BoQoutput = Queue()
        self.Pred = Queue()
        self.AlertQ = Queue()

    def Input(self):
        """
        It's the input Moudle, which gets data from machine and pass data to other modules.
        :param BoQinput: It's a queue for input to communicate input data between modules.
        :return:
        """
        while True:
            # input
            Inp.rand_input(self.BoQinput)  # Generating random data as input.
            time.sleep(2)


    def middle(self):
        """
        Middle part contains several modules, including AI module and Alert module.
        :param BoQinput: It's a input queue.
        :param BoQoutput: It's a queue and it pass data to output module.
        :param Pred: A queue for prediction data.
        :param AlertQ: A queue for alert module.
        :return:
        """
        while True:
            if not self.BoQinput.empty():
                value = self.BoQinput.get_nowait()  # getting data from queue.
                bo = value[0]  # blood oxygen
                bp = value[1]  # blood pressure
                pul = value[2]  # pulse
                # AI
                A = Ai()  # AI module
                A.input_check(bo, bp, pul)  # check the type of input
                predBloodOxygen, predBloodPressure, prePulse = A.predict()  # prediction output
                pred_info = predBloodOxygen, predBloodPressure, prePulse
                self.Pred.put_nowait(pred_info)
                # Alert
                Alt = Alert()  # Alert Module
                boi = bo, 0  # the last number stands for the type of the data
                bpi = bp, 1
                puli = pul, 2
                Alt.Alert_for_three_categories_input(boi)  # data check
                Alt.Alert_for_three_categories_input(bpi)
                Alt.Alert_for_three_categories_input(puli)
                alert = Alt.Alert_Output()  # alert signal
                self.AlertQ.put_nowait(alert)  # send alert signal
                self.BoQoutput.put_nowait(value)  # send data
                time.sleep(2)


    def Output(self):
        """
        It's the output part, could be seen as interface module.
        :param BoQoutput: A queue for output data.
        :param Pred: Queue for prediction data.
        :param AlertQ: Queue for Alert information.
        :return:
        """
        while True:
            # Interface
            if not self.BoQoutput.empty():
                value = self.BoQoutput.get_nowait()  # get data
                pred = self.Pred.get_nowait()  # get prediction data
                bo = value[0]  # display blood oxygen
                bp = value[1]  # display blood pressure
                pul = value[2]  # display pulse
                Alert_info = self.AlertQ.get_nowait()  # get alert signal
                U = userInterface()
                U.getFromData(bo, bp, pul)  # get data
                U.sendToShow()  # display
                print("Prediction:", pred, "\n")
                print("Alert information:", Alert_info, "\n")

                time.sleep(2)


    def runprogram(self):
        """
        To start the program
        :return:  No return
        """
        t1 = threading.Thread(target=self.Input)
        t2 = threading.Thread(target=self.middle)
        t3 = threading.Thread(target=self.Output)
        t1.start()
        t2.start()
        t3.start()


if __name__ == '__main__':
    M = Medical()
    T = threading.Thread(target=M.runprogram)
    T.start()

