from AiModule import AiModule as AI
import UserInterface_module
import Input_Module_lkn as I
from Alert_module import Alert
# from storage import storage as St
while (True):
    #input
    bo = I.read_data("/Users/liuknan/Documents/GitHub/ModuleDesign/example/examplebo.txt")
    bp = I.read_data("/Users/liuknan/Documents/GitHub/ModuleDesign/example/examplebp.txt")
    pul = I.read_data("/Users/liuknan/Documents/GitHub/ModuleDesign/example/examplepul.txt")
    #storage
    # for i in range(len(bo)):
    #     S = St(bo[i],bp[i],pul[i])
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
        Alt.Alert_for_three_categories_input(boi)
        Alt.Alert_for_three_categories_input(bpi)
        Alt.Alert_for_three_categories_input(puli)
    UserInterface_module.userinterface_input(bo,bp,pul,predBloodOxygen,predBloodPressure,prePulse)
    UserInterface_module.userinterface_output(bo,bp,pul,predBloodOxygen,predBloodPressure,prePulse)
