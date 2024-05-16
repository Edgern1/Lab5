from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control as l
#Empty list to store sequence of keypad presses
password = []

lcd = LCD.lcd()
lcd.lcd_clear()
#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    global delay
    password.append(key)
    print(password)
    if key==1:
        l.delay=1
    elif key==0:
        l.delay=0


def main():
    l.led_control_init()
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()
    
    # Display something on LCD
    lcd.lcd_display_string("Led control", 1)
    lcd.lcd_display_string("0: off 1:Blink", 1)
    
    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

# Main entry point
if __name__ == "__main__":
    main()
