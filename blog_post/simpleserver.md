This series of posts is going to focus on getting a webserver up and running on a Raspberry Pi/Beaglebone Black. The aim of this series is to be able to remotely control your micro-controller. This is a 3 part series in which I will show you how to create a simple webserver running on your Raspberry Pi I will then show you how to use it to control your GPIO pins, and finally we will create an API(Application Programming Interface, more on that later) so that all control can be done using other devices(like a smart phone).

This post will be short and simple, and will just help us get a simple webserver up and running. I will also end the post with how to get this webserver to automatically start on your Pi whenever it is powered on.

I will be focusing mostly on the Raspberry Pi, but everything can easily be modified to run on a Beaglebone.

##Introduction
In this post we will build a basic web server that will serve a dynamic web page. We will be using Python with the [Bottle](http://bottlepy.org) framework. The reason I picked the bottle framework is because it is lightweight and easy to use. I will not be doing a walk-through on how to install it, but a quick look at the web site will teach you how to do it.

##What is a Web Server
A web server is any program/technology that is able to server HTTP requests to any capable client. I won't go into too much detail because I know Google knows way more than me on this topic.

We will be using the Standard Template Library with Bottle called [SimpleTemplate Engine](http://bottlepy.org/docs/dev/stpl.html) more detail on that can be found at the link.

##Getting Started
To get started with this one, all you need is a computer with a text editor and Python installed(your Raspberry Pi will do). Personally, I use my Mac with Sublime Text, but that is just personal preference(and involves copying code over after every change). You must also install Bottle.


##Creating the Basic Hello World Server
Here's the code:

simpleserver.py
```python
from bottle import route, run, template

@route('/')
@route('/<name>')
def hello(name='World'):
    return template('hello_template', name=name)

run(host='0.0.0.0', port=8080)
```
./views/hello_template.tpl
```html
%if name == 'World':
    <h1>Hello {{name}}!</h1>
    <p>This is a test.</p>
%else:
    <h1>Hello {{name.title()}}!</h1>
    <p>How are you?</p>
%end
```

Now, here's what's happening:

We are using the global `Bottle` and importing whatever we need with:  
`from bottle import route, run, template, view`  

We then declare 2 routes, first the default route, then a parametric route.
```python
@route('/')
@route('/<name>')
```

We then define the function that handles those routes(remember the `@route` automatically calls the next function in the code). Here we define a simple function that just takes name argument(if defined) and passes it to the template before returning it.

```python
def hello(name='World'):
    return template('hello_template', name=name)
```

We then run the webserver on port 8080 and host 0.0.0.0(this is used to allow access for external hosts) with:
```python
run(host='0.0.0.0', port=8080)
```

The template code in `./views/hello_template.tpl` is pretty straightforward. It just displays some html code based on an if condition on the `name` variable.

You can run this with `python simpleserver.py` and test it out, if you point your browser to `http://<IP>:8080` you will see the Hello World page, and if you go to `http://<IP>:8080/name` you will see Hello name.


##Getting the server to run on boot

We are going to use crontab to run a simple startup script to achieve this.

The startup script we will use is:

```bash
#!/bin/sh
# launcher.sh
# This script goes to the webserver directory and starts it using python

cd /home/pi/webserver
sudo python simpleserver.py
cd /
```

We will then make it executable with `chmod +x webserver_launcher.sh`.

If you haven't done this before, you should create a logs directory for your custom crontabs with `mkdir ~/logs`.

We then setup the crontab by bringing up the crontab editor with `sudo crontab -e` and then adding this line:
`@reboot sh /home/pi/webserver/launcher.sh >/home/pi/logs/cronlog 2>&1`


##Conclusion

Thats it!! You now have a simple webserver running on your Raspberry Pi.

