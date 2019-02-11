<<<<<<< HEAD
# EC500
It's a readme document for the architecture based on the design of Mohit.
## AI Module
### Name: AI Module

### Input:
Bo, bp, pul are three lists represent the value of blood oxygen, blood pressure and pulse which are defined as double.
bo, bp, pul: list [float value]
### Output:
Three double values for estimated health score

Data received from storage system is input to the unsupervised AI Module, and will generate the output which are three predicted values for patients’ future health condition estimation by using data as blood oxygen, blood pressure and pulse stored in storage system to make prediction.
=======
# EC500
It's a readme document for the architecture based on the design of Mohit.
## Alert Module
The input of this module should be the three inputs provided by the storage module. Actually the storage module does not change the value of
the input of the patient's data. So the alert module will take the data from the patient. The doctor should set a value when he/she uses the 
product at the first time. While using the product, if the data of the patient pass beyond the value, which is set by the doctor, the alert module will change a global value. Then there will be some alerts because of the change of the value such as the red light shinning or something else.
>>>>>>> Input_lkn
