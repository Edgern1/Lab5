import time
import hal.hal_lcd as lcd

if __name__=="__main__":
    l=lcd.lcd()
    while True:
        local_time = time.localtime() # get struct_time
        l.lcd_display_string(time.strftime("%H:%M:%S", local_time),line=1)
        l.lcd_display_string(time.strftime("%d:%m:%Y", local_time),line=2)
        time.sleep(1)


