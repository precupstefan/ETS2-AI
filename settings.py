# Tweak settigns across AI
import pyvjoy


autopilot_hotkey='z'

controller=pyvjoy.VJoyDevice(1)
# Y0,Y1,X0,X1
speed_restriction_ROI=(590,605,1003,1020)
speed_current_ROI=(475,492,1000,1020)
speed_check_interval=0 #in seconds

#viteza procent
acceleration_percentage={5:10,8:15,9:20,15:25,25:30,30:35,45:40,60:45,64:50,65:55,70:60}

#	Y = 0.6016*X + 12.80