from AiModule import AiModule as AI
from UserInterface_module import userInterface
import Input_Module_lkn as I
from Alert_module import Alert
from storage import storage as St
while (True):
    #input
    bo = I.read_data("/Users/liuknan/Documents/GitHub/ModuleDesign/example/examplebo.txt")
    bp = I.read_data("/Users/liuknan/Documents/GitHub/ModuleDesign/example/examplebp.txt")
    pul = I.read_data("/Users/liuknan/Documents/GitHub/ModuleDesign/example/examplepul.txt")
    #storage
    for i in range(len(bo)):
        S = St(bo[i],bp[i],pul[i])
    #AI
    A = AI()
    A.input_check(bo,bp,pul)
    predBloodOxygen, predBloodPressure, prePulse = A.predict()
    #Alert
    Alt = Alert()
    for k in range(len(bo)):
        boi = bo[k],0
        bpi = bp[k],1
        puli = pul[k],2
        boa = Alt.Alert_for_three_categories_input(boi)
        bpa = Alt.Alert_for_three_categories_input(bpi)
        pula = Alt.Alert_for_three_categories_input(puli)

    #Interface
    U = userInterface()
    U.getFromData(bo,bp,pul)