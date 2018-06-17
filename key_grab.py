import settings
import pyHook
import pyvjoy
import pythoncom


#   KEYPRESSED EVENT
def OnKeyboardEvent(event):
    # block only the letter A, lower and uppercase
   
    if event.Ascii == ord(settings.autopilot_hotkey):
        settings.controller.set_axis(pyvjoy.HID_USAGE_SL1,0x8000)
        print(event.Ascii)
    else:
        settings.controller.set_axis(pyvjoy.HID_USAGE_SL1,0x0)
    # returning True to pass on event to other applications
    return True

def init():
    # create a hook manager
    hm = pyHook.HookManager()
    # watch for all mouse events
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    try:
        pythoncom.PumpMessages()   #This call will block forever unless interrupted

    except (KeyboardInterrupt, SystemExit) as e: #We will exit cleanly if we are told
        print(e)    
        
    return