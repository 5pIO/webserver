##Introduction
In this post we will focus on implementing GPIO control into our webserver. We will be using toggling simple LED's in this example.

##Getting Started
You will need to hook up the GPIO pins on your Pi to LEDs, I will be using 3 in the example.

You will also need the `RPi.GPIO` library installed.

##Building the Webserver
Here we will create 2 files:

`gpioserver.py`
```python
from bottle import route, run, template, request
import RPi.GPIO as GPIO

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
```
and `gpio_template.tpl`
```html
<table>
<tr>
    <td>Pin Number</td>
    <td>Current Value</td>
    <td></td>
</tr>   
% for key, value in current_values.iteritems():
    <form action="/toggle?pin={{key}}" method="post">
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
        <td><input type="submit" value="Toggle"/></td>
    </tr>
    </form>
% end   
</table>
```

As you can see, the code is very similar to the first part in this series. I will walkthrough all the differences below:

*   Here we just setting up the GPIO, you can see I will be using GPIO pins 18, 23 and 24.    
        
```python
        import RPi.GPIO as GPIO

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
```

    
* We then store the states of each pin in a variable  
    `current_values = {18: False, 23: False, 24: False}`  

* We then declare a new POST route, that toggles the pin number specified in the `pin` query param.
```python
        @route('/toggle', method='POST')
        def toggle():
            pin = int(request.query.pin)
            current_values[pin] = not current_values[pin]
            GPIO.output(pin, current_values[pin])
            return template('gpio_template', current_values=current_values)
```
* Finally we catch the Ctrl+c interrupt to perform the GPIO cleanup before shutting down

```python
        try:
            run(host='0.0.0.0', port=8080)
        except KeyboardInterrupt:
            GPIO.cleanup()
            raise            
```

* You can see that in the template file, we first iterate through all the current values, and then for each of them we create a new table row that has the pin number, value and a form with 1 button that POST's to the toggle route.

You can now run this with `sudo python gpioserver.py` and access it in your browser, You will see that clicking on each of the toggle buttons toggles the corresponding GPIO pin on the Pi.


##Conclusion

And there you have it, you now have a web server that controls your Pi, you can access this from anywhere on your local network form any device with a browser. Have a look at the next part to have this accessible from anywhere on the Internet.
