
# EC500
It's a readme document for the architecture based on the design of Mohit.

## Requirements
There is no special libraries you need to install, so you may ignore the requirements.txt and setup.py. The main.py is based on all other python files so you just need to import all of the .py files.

## Modules Introduction
This program includes several modules and each of them is important.
### Input Module
The input module control the input of the whole program. Though we do not have a real machine or something else for us to acquire the real input, the Input Module will generate three random float number and put them in a list, then output the list to other modules.t

### Storage Module
Storage Module has not been really impolemented yet since we do not need a database now. But basically it will accept the data from Input Module.

### Alert Module
The Alert Module will receive data from Input Module and analyze the data. If the data is beyond, the Alert Module will send a signal to the UserInterface Module and tell the users that the input data is in an abnormal condition.

### AI Module
The AI Module also get data from the Input Module and analyze the data, then predict the future data output according to the data, which is being analyzing.

### UserInterface Module
The UI Module displays the input data and show these data to the users. 

### Thread
We seperate all the modules into three parts. The first part is the Input Module, the second part is the UI Moudle and the rest of modules are in the last part. We implement three threads for all three parts so each part can work synchronously. And we have two queues for threads to communicate with each other.
![Image Invalid](https://github.com/ec500-software-engineering/exercise-1-modularity-liuknan/raw/master/500.png)

### Output
![Image Invalid](https://github.com/ec500-software-engineering/exercise-1-modularity-liuknan/raw/master/output.png)
The data named blood pressure, blood Oxygen and Pulse are sent by input module, the User Interface will display them. 
The prediction is the output of AI module. And for alert information, if everything goes well, it would be -1. If something
happen, it would go to 0, 1 or 2, which depends on which data exceeds threshold.

