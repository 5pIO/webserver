##Introduction
If you followed the previous post, you can now control you Pi from anywhere in your home network. However, sometimes, we want to be able to control our stuff when we are not at home. This can be done over the Internet, and I'm going to show you how.

##Things Needed
*   Access to your Router's Web Admin page. If your computers IP is w.x.y.x, this is usually found at w.x.y.1, you will also need the login credentials for this. If you have never changed this, you should be able to find it in the Routers manual or by Google-ing your Router model.

* You will need to know the IP address of your Pi.

##Getting Started
To set up remote access, we will be using a concept called Dynamic DNS. As most of you know, when you are connected to the Internet, you have an IP. However for most us, this IP can change without warning. We also know, that every domain on the Internet must point to an IP, and this is what DNS does, it resolves a domain name to an IP. We can always access our home networks through this IP. However, as it changes, we need some way to keep track of when it changes. This is where Dynamic DNS comes in. Basically, it uses a small program to update the IP a domain points to.

My Dynamic DNS services have always been from [No-IP](http://noip.com), but there are many providers out there. No-IP provides a good free tier as well as a large choice of domains.

To get started create a free account, and then add a new host(I called mine 5p-pi.no-ip.org). Leave all the fields to their default values.

The rest of the instructions assume you have a No-IP account, but most providers will have similar steps.

##Warnings
    * The webserver we created earlier has NO SECURITY, and enabling public access to this is potentially VERY DANGEROUS.

    * Make sure running a webserver at home does not violate your ISPs terms of use.

    * I AM NOT RESPONSIBLE OR LIABLE FOR ANY DAMAGE DONE TO YOU OR YOUR DEVICES, EITHER BY A NETWORK BREACH OR BY YOUR ISP. PLEASE CONTINUE AT YOUR OWN RISK.

##Instructions
* First we will install the No-IP client on the Pi. To do this you should follow the No-IP [tutorial](http://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/).

* You will then need to configure your router(for all the features needed, look at your routers manual or search on Google).

    * The first step here will be to give your Pi a static IP address within your network. This involves looking for the equivalent of `Address Reservation` in your router's web interface. 

        * To do this, you will need your Pi's MAC address and IP, this can be found by typing `ifconfig` in your command line. The MAC Address is the `HWAddr` field, and the IP is the `inet addr` field.

        * Once you have these, create an address reservation in your router with that MAC and IP.

    * You will then need to setup `Port Forwarding` on your router. This will redirect an external port to a port on a device on your local device.

        * Once you find the `Port Forwarding` section on your router, create a new Forward, which will forward external port `8080` to internal port `8080` on your Pi's IP address.


* You should now be able to access the webserver running on your Pi through the hostname you added to No-IP. for eg. mine was at `http://5p-pi.no-ip.org:8080`


##Conclusion
You can access your Pi from any browser any where in the World with any device with an Internet connection!!


