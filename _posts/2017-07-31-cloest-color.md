---
comments: false
date: 2017-07-31
layout: post
permalink: /2017/07/closest-color.html
tags:
- python
title: Closest Color in a list of json colors
---
I recently got a shed built and I want to paint it the same color as my house. Unfortunately the house is covered in colored stucco and the shed has wood siding. I managed to find an online image of the stucco color. But stucco has bumps and isn't a uniform color. So I used this [average color finder](http://matkl.github.io/average-color/) to work out the target color.

My preferred paint is [Kelly Moore](http://kellymoore.com/mycolorstudio-color-palette/) and so I went to their site hoping to be able to search based on some RGB values, but alas that wasn't going to work out. Their color picker is fancy but there didn't seem a way to find a color close to a particular color. I did some digging and found out that all their colors were being sent to the browser in a [json file](http://kellymoore.com/mycolorstudio-color-palette/data/colors.json). So I grabbed that and wrote a little closest color script to find the color closest to the one I wanted.
You can get the [closest color script here](https://gist.github.com/arkarkark/b5d0c92d643454ea9e66de94641197fe).

I could have gone nuttty and converted it to HSV colorspace and found an even better match, but there are so many colors that just finding the minimum of the differences of red, green, blue got me close enough.

But, lo, plot twist. Turns out the painter wanted to use [Behr paints](http://www.behr.com/consumer/colors/paint#paint), their color picker was different and I couldn't see any specific request that had all the colors in it. Luckily they throw them on the window object in JavaScript as window.colorData so it was easy to put that in my clipboard using the `copy()` JavaScript console function. Of course the format is different so I had to modify that. It's all in the gist file. Check it out.

If I thought more than 2 people a year would use it, you could easily make this a nice webapp, mapping from one paint manufacturer's colors to another or just from any RGB code to a paint name.
