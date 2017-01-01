---
layout: post
title: Bike Wheel Lights
date: 2016-12-31
comments: false
tags:
- bike
- lights
- imagemagick
---
In one of my middle of the night shopping binges I ended up with a [YQ8003 Bicycle Light DIY Programmable LED Wheel Light Waterproof for 26 inch Bike Wheel  -  BLACK](http://www.gearbest.com/cycling-gear/pp_196995.html) It was only $25 shipped from CA, no sales tax, go figure. It arrived a few days later. Here's a [demo video](https://youtu.be/oN4Q87aC5l4).

In the middle of the night I fired up a super old windows XP laptop to download [the software](https://youtu.be/LXwR9fj-5N8) ([direct download link](http://www.gearbest.com/index.php?m=index&location_id=https://s3.amazonaws.com/download.appinthestore.com/uploads/201506/YQ8003+spoke.rar)) and then an [UnRar for Windows](http://gnuwin32.sourceforge.net/packages/unrar.htm) and I quickly got some cat pictures uploaded to it. Next thing you know I'm zipping up and down the street at 2am infront of my phone on a tripod trying to capture a video of it working. Alas my phone's too fast and I never got any satisfaction.

Luckily I was heading out for a ride at 6am and my wife indulged me and let me ride around for her with this light on to tell me if it worked or not. IT DID! I had put the light on the front wheel since I wanted cars to miss the front of me and it was least occluded by legs and bits of my bike. That meant that the wheel sensor magnet was on the almost vertical fork and not the horizontal chainstay as it would be for the [recommended rear wheel install](https://youtu.be/ggoLeS1lh04), which would have made testing much easier in a dark garage cranking on the pedals... Anyway, with the wheel sensor in a diffreent position the image shown on the lights was not alligned vertically so I had to find out how much I needed to modify it. I couldn't see it myself while riding so had limited times when people could help me, so I made a bunch of images with arrows at different angles and as it cycled (HA!) through them I asked which one was pointing up. Turns out it's the blue one, so I need to rotate my images 120° before I upload them.

You can [download the zip file](https://drive.google.com/drive/folders/0B93fzA8rfLM1ODFjNjM1ZTYtZTg4Ny00NjFlLWE3NmEtODdmMWIwNGUyZWNl) of all the images I made.

Here's the script I used to generate it:

```python
#!/usr/bin/python

import os

degs = """
0 red
30 yellow
60 green
90 cyan
120 blue
150 magenta
180 orange
210 chartreuse
240 azure
270 violet
300 gray
330 white
"""

for x in degs.split("\n"):
  if not x:
    continue
  deg, col = x.split(" ")
  print "deg %s - col %s" % (deg, col)
  os.system("""convert -size 600x600 xc:transparent -draw "fill %s translate 300,100 rotate -90 scale 30,50 path 'M 0,0  l -15,-5  +5,+5  -5,+5  +15,-5 z'" arrow.png""" % col)
  os.system("""convert -background transparent -fill white -size 600x600 -gravity center label:%s label.png""" % deg)
  os.system("""composite -background transparent label.png arrow.png out.png;  convert -background transparent out.png -rotate -%s +gravity -crop 600x600+0+0 +repage %03d-%s.jpg""" % (deg, int(deg), col))
  # os.system("""display %03d-%s.jpg""" % (int(deg), col))
```

In hindsight I should have just mounted it on the rear wheel and tried it all out there and tited my head while I found the right image and then mounted it on the front wheel, but I have an aversion to wasting zip ties. I'm my own worst enemy sometimes.
