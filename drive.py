import RPi.GPIO as gpio
import logging


    
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting...')

    gpio.setmode(gpio.BCM)

    in1_pin = 4
    in2_pin = 17

    gpio.setup(in1_pin, gpio.OUT)
    gpio.setup(in2_pin, gpio.OUT)


    def set_(prop, value):
        """Set property to value."""
        try:
            with open('/sys/class/rpi-pwm/pwm0/' + prop, 'w') as f:
                f.write(value)

        except:
            logging.error('Error writing {}={}'.format(prop, value))

    set_('delayed', '0')
    set_('mode', 'pwm')
    set_('frequency', '500')
    set_('active', '1')

    def clockwise():
        gpio.output(in1_pin, True)
        gpio.output(in2_pin, False)

    def counter_clockwise():
        gpio.output(in1_pin, False)
        gpio.output(in2_pin, True)

    clockwise()
