import hal.hal_adc as a
import hal.hal_servo as s
def main():
    a.init()
    s.init()
    while True:
        s.set_servo_position(a.get_adc_value(1)/5.7)
if __name__=="__main__":
    main()
