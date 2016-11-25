---
date: 2016-11-25
layout: post
tags:
title: Panoramic Photo Stitching
---

My school created an alumni Facebook page and I had two really old panoramic photo prints of the whole school to share with them. I found the best way to share them was to tape down the print and take a series of landscape photos with my phone. Shared via airdrop to my computer, then I used the `file` command to work out the approximate size of the final image and set that in [AutoStitch](http://matthewalunbrown.com/autostitch/autostitch.html) and imported the images. Then I had to split them up into more manageable chunks. This command split them into 10 images (left to right).

`convert pano.jpg -crop 10%x100% +repage part_%d.jpg`

Then on Facebook I created a new album and uploaded one image - set it to use high quality and then uploaded the rest of the images and the final large pano.jpg image for good measure. Then came the tedious task of tagging everyone or approving other people's tags.

I was stoked how well AutoStitch and [ImageMagick's](https://www.imagemagick.org/script/) `convert` program worked.
