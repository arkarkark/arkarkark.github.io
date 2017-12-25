---
comments: false
date: 2017-12-25
layout: post
permalink: /2017/12/download-all-youtuble-playlist-files-as-mp3.html
tags:
- youtube
title: Download all YouTube playlist files as mp3
---

Here's how I downloaded all the songs from a youtube playlist as mp3 files.
You need to have [youtube-dl](https://rg3.github.io/youtube-dl/) instaled (I just used `brew install youtube-dl`)

First you need the playlist Id, it's in the URL of the playlist, then visit a url like this:

[https://developers.google.com/apis-explorer/?hl=en_US#p/youtube/v3/youtube.playlistItems.list?part=snippet&maxResults=50&playlistId=PL-ODR7uRLzL8VgaHR6S6h4KIkpNXUoccL&_h=1&](https://developers.google.com/apis-explorer/?hl=en_US#p/youtube/v3/youtube.playlistItems.list?part=snippet&maxResults=50&playlistId=PL-ODR7uRLzL8VgaHR6S6h4KIkpNXUoccL&_h=1&)

Then cmd-a, cmd-c to copy the whole page.

```
pbpaste | fgrep 'videoId":' | cut -d '"' -f 4 | while read fil; do youtube-dl -x --audio-format mp3 https://youtu.be/$fil; done
```

bam! all files downloaded!
