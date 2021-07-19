---
comments: false
date: 2021-02-25
layout: post
permalink: /2021/02/webcam-light-ring.html
tags:
- webcam
- ws2812
- esp8266
- led
title: Webcam Light Ring
---
I quickly put together a webcam light ring. It's a [16 x ws2812 ring](https://www.aliexpress.com/item/1005001425289349.html) connected to a [LED adapter and ESP01](https://www.aliexpress.com/item/32958295046.html) powered by a cut off USB cable. It's in a little black box with slightly filed clothespins to hold it to the screen.

[![installed light ring](/assets/images/2021-02-webcamring/IMG_3282.sml.jpg)](/assets/images/2021-02-webcamring/IMG_3282.jpeg)

In the end I wasn't super happy with the results. The led lights reflected too much off my glasses. I've since got some good diffuser plastic (some LED garage lights died) so I might try again, but I was thinking maybe the diffuse lgiht should come in from the side.

I was going to put a webserver on it to allow you to choose the colors but I was still paralyzed with the whole LUA or MicroPython thing and since I wasn't happy with the glasses reflection I just abandonned it.

If I pick it up again I'll use this [light color/temperature and makeup](https://spectrum-brand.com/blogs/news/colour-of-lighting-and-make-up-the-facts) reference and a handy dandy [rgb to color temp](https://andi-siess.de/rgb-to-color-temperature/). I realized it depends on the LEDs but it'd be a good starting point. I guess I could actually [measure it](https://www.sparkfun.com/products/12829) but this'd have to be way more successful for me to put that much effort into it.
