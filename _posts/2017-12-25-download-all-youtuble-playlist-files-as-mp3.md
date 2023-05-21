---
comments: false
date: 2017-12-25
layout: post
permalink: /2017/12/download-all-youtuble-playlist-files-as-mp3.html
tags:
- youtube
title: Download all YouTube playlist files as mp3
---

I use [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download stuff off YouTube and these aliases are superuseful. I installed it with `brew install yt-dlp` you might also need to `brew install id3v2`.

```
alias ya='yt-dlp -w -i -x -o "%(playlist_index)02d-%(title)s.%(ext)s" --add-metadata --audio-format mp3 -I ::-1 --exec "id3v2 -T %(playlist_index)d %(filepath,_filename|)q; mv %(filepath,_filename|)q $HOME/Music/Automatically\ Add\ to\ Music.localized/; sleep 2"'

alias yv='yt-dlp -w -i -o "%(playlist_index)02d-%(title)s.%(ext)s" --format "bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/bestvideo+bestaudio/best" --merge-output-format mp4 --add-metadata -I ::-1 --exec "mv %(filepath,_filename|)q $HOME/TV/Automatically\ Add\ to\ TV.localized/; sleep 2"'
```

`ya` - downloads a youtube file or playlist in mp3 format and sets the id3v2 track number to the track number of the playlist, then moves the file to it's automatically added to Music.app and then waits two seconds before downloading the next file since sometimes it takes a while to notice to get the files to add. It also downloads the playlist in reverse order so that if you show your songs in descending date added they're in the correct order.

`yv` - does similar to `ya`, but downloads an mp4 video file that is compatible with AppleTV and adds it to TV.app
