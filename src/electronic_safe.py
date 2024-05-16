import time
from threading import Thread
import hal.hal_lcd as lcd
import hal.hal_buzzer as buz
from hal import hal_keypad as keypad

PW=[1,2,3,4]

allow_entering=False
w=0
pw=[]
l=lcd.lcd()
def check_pw(pw):
    if len(pw)!=len(PW):
        return False
    for i in range(len(PW)):
        if PW[i]!=pw[i]:
            return False
    return True

def key_pressed(key):
    global allow_entering
    global pw
    global PW
    global w
    if not allow_entering:
        return
    l.lcd_clear()
    if key=="*"and len(pw)>=1:
        allow_entering=False
        if check_pw(pw):
            l.lcd_display_string("Safe Unlocked")
            return
        else:
            
            w+=1
            if w>=3:
                l.lcd_display_string("Safe Disabled")
                return
            l.lcd_display_string("Wrong PIN")
            buz.init()
            buz.beep(1,0,1)
            l.lcd_clear()
            dis()
            pw=[]
            allow_entering=True
    if key!="#" and key!="*":
        pw.append(key)
        l.lcd_display_string("Safe Lock")
        l.lcd_display_string("*"*len(pw),line=2)
        
def dis():    
    l.lcd_display_string("Safe Lock")
    l.lcd_display_string("Enter Pin:",line=2)

def main():
    global allow_entering
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    dis()
    allow_entering=True



if __name__=="__main__":
    main()

