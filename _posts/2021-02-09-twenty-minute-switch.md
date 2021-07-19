---
comments: false
date: 2021-02-09
layout: post
permalink: /2021/02/20minswitch.html
tags:
- esp8266
- make
title: 20 Minute Switch
---


After shoulder surgery, we're borrowing a [cold therapy machine](https://mycoldtherapy.com/products/breg-polar-care-kodiak-shoulder) you use it 20 minutes on, 20 off. but to turn it off you need to unplug it. With a simple esp01 and a [relay module](https://www.aliexpress.com/item/4000348370586.html) it's all automatic now and tidy!

[![inside](/assets/images/2021-02-switch/IMG_3211.sml.jpg)](/assets/images/2021-02-switch/IMG_3211.jpeg)

Here's what it looks like inside. Luckily for me the machine was powered by 6V which is not too much to power the relay board and ESP01 so I just leeched the power off that and so the device fits inline with the power plug. Luckily I had a plug and socket that fitted because I take apart everything and keep what might be useful before I throw it out for e-recycling. Here's [the code](https://gist.github.com/arkarkark/2cfd35b8fc94d3b2ae3e219186feef00). Of course it wasn't all trivial, the relay board had a problem that needed [a simple fix](https://www.esp8266.com/viewtopic.php?p=79484#p79484).

[![in use](/assets/images/2021-02-switch/IMG_3214.sml.jpg)](/assets/images/2021-02-switch/IMG_3214.jpeg)

Here it is in use!

It could be much better but it works fine enough and we included it when we returned the unit we were borrowing. Hopefully the owner still uses it. I wish it didn't double click the relays when you first plug it in and ideally I'd like the ability to change the timing (both on and off time periods). I had planned to play around with putting a webserver in it, but then I discovered [micropython on the esp8266](https://docs.micropython.org/en/latest/esp8266/quickref.html) was getting more mature and wanted to play with that for a different project so didn't want to do it twice in two languages. I don't particularly enjoy writing LUA code.

I made another of these for a friend who also had surgery. His needed 30 minutes on and 60 minutes off. The code was easy to change. Also I didn't know what power was available so I just used a USB cord to power the ESP01/relays and then it was just a simple switch. Not quite as tidy, but I was doing it all remotely without access to the machine. He said it worked great for him.
