#It's the I/O documentation for the User_Interface_system
#Qinmei Du
#User Interface
def userinterface_input(bo,bp,pul,predBloodOxygen,predBloodPressure,prePulse):
	"""
	Get_data_from_data_base:
		format:(double value, int type)
	Get_data_from_alert_sys:
		format: three flags from alert sys output to trigger alert display
	Get_data_from_user:
	    format: boolean control from user. Such as turn on, turn off
	            user log in information
	"""

def userinterface_output(bo,bp,pul,predBloodOxygen,predBloodPressure,prePulse):
    """
    send input to electron device to show on the screen
    """
