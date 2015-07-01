from bottle import route, run, template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
current_values = {18: False, 23: False, 24: False}


@route('/')
def index():
    return template('gpio_template', current_values=current_values)


@route('/toggle', method='POST')
def toggle():
    pin = int(request.query.pin)
    current_values[pin] = not current_values[pin]
    GPIO.output(pin, current_values[pin])
    return template('gpio_template', current_values=current_values)

try:
    run(host='0.0.0.0', port=8080)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
