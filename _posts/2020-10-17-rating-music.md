---
comments: false
date: 2021-06-17
layout: post
permalink: /2020/10/rating-music.html
tags:
- itunes
title: Rating Music in iTunes on iOS
---
## History

You can skip down to my [current solution](#current-solution) to find out how I currently do it if you don't want to read this boring bit.

In the olden days when I used to take the bus to work I would rate my music on an iPod Photo. I rated them using this scale

* 0 stars - not yet rated
* 1 star - terrible, I should delete this song
* 2 stars - I don't like this song but should keep it - maybe for a complete album
* 3 stars - I don't hate it, but I'd be fine if I never heard it again. worth listening to when listening to a whole album or all works by an artist.
* 4 stars - should be featured on a best of a genre, best of a musician.
* 5 stars - absolute banger, I would always listen to this song.

Then I could make playlists of 4 stars and above and they'd be sure to be great music to listen to.

In hindsight I should probably stretch it more so that 3 stars and above was the threshold then I could be a little more granular with my ratings.

Once all my music was rated, keeping it updated when new stuff was added was easy. Then I wanted a way to know if music was safe for work or not, i.e. it had rude words or questionable topics. I took all my 5 star music and added it to a manual playlist called `was 5 star` and then made a smart playlist that had the rules `playlist is "was 5 star"` and `rating is *****` then I went through that and all songs that were safe for work got rated 4 stars and those that had rude words in them were rated 3 stars. Finally I made my way through the songs and could then manually go and sort my `was 5 star` playlist by rating and add all the 3 stars to my `NSFW` playlist and the 4 stars to `SFW` and when I was finally done I could put everything back to 5 stars. Then I worked through the 4 star songs genre by genre. It took a while but I was just sat on the bus commuting anyway and it helped me discover some songs in my library I'd forgotten about.

Eventually I got an iPhone and using that was a little easier. Then I finally worked out that I could both rate songs with stars and also mark if I loved or disliked songs with the heart thing. So now I could rate them in the star rating and use hearts and dislikes to rate as Safe for Work and Not Safe for Work. I'd later grab the hearts and add to SFW and the dislikes into my NSFW playlist and then reset them.

Then I relized I could do this using Siri on bike rides although it was a little annoying. I'd have to say "I like this song", then I'd say "rate this song 5 stars", then I'd have the press the remote button (to turn off siri) and tben double press it to move to the next song. Each step could go wrong and I'd have to work out what was happening, but I was able to rate my music, as long as I had internet access where I was riding.

Finally I discovered [shortcuts](https://support.apple.com/guide/shortcuts/welcome/ios) this allowed me to make a shortcut that would rate a song and make it as NSFW or SFW and then move to the next song. Of course it wasn't as easy as that. There were no shortcut actions to rate a song. I ddin't want to sync my whole NSFW and SFW playlists either. Also empty playlists don't sync to my phone either. This all led me to the...
You can also run the shortcuts using the phone app and pressing big buttons on the screen. This works even if you don't have internet access. Sometimes the music doesn't start playing when you move to the next track when you do it this way, so you have to explicitly start the music once you move to the next track.

## Current Solution


I have a system that works but it's ugly. I made 5 playlists with a small song in it called `__` (one playlist for each star rating) called "zp 1" to "zp 5". I also made 2 playlists "zp rude" and "zp safe" with similar small `__` songs on them. Finally I made a "zp Needs Work" for me to deal with songs that might have the wrong genre or I had mistated.

![a](/assets/images/2020-10-rate/Music.png)

I then make 5 shortcuts that adds the current song to the right rating playlist and the SFW list and another 5 that did the ratings and added it to the NSFW list. It then moves to the next song and makes sure it is playing.

![a](/assets/images/2020-10-rate/banger.sml.png)

Then after my phone has synced to my mac at home. I run a python script that takes all the songs (except the small `__` one) and rates them and removes them from the playlists. Then I need to sync again. I need to leave the small song there so the playlist ends up on my phone (empty playlists are not synced).

Here's [the script](https://gist.github.com/arkarkark/def0cb52b3972639d29b11eeec492368) you might need to pip3 install appscript

I told you it was ugly, but it does work.

If you don't mind having those playlists around you could do the script stuff by hand occasionally.

I had to have a unique title for each shortcut that was not likley to be confused with something else. Tryone came about because I used to try and call Traffic Info and it would always try and call Patrick which was annoying when stuck in traffic on the highway. The format of the naming is Tyrone _rating_ _safe/rude_. I changed the rating word depending on if it is safe or rude to further reduce the risk is the phone just fudging a guess since I'm riding my bike when yelling this into the mic. I also changed the reply to amuse me and get confirmation of where it is added. If it adds the track to the wrong list the order in which I add things in my script allows you to upgrade tracks  to a higher rating or making sure they are NSFW. If anything is screwed up you can always "Tyrone Later" and it'll get added to the Needs Work playlist to be updated at your leisure. Here's the order I have them in on my phone. SFW are colored Greena nd NSFW are colored Red, the ordering allows me to easily see where I am in the list depending on how many red/green ones I can see.

| Shortcut | Rating | (not) safe for work | reply |
|---|---|---|---|
| Tryone Banger Safe | 5 | SFW  | Banger!|
| Tryone Good Safe   | 4 | SFW  | Good!|
| Tryone 3 Safe      | 3 | SFW  | Meh|
| Tryone 5 Rude      | 5 | NSFW | Fookin' A!|
| Tryone 4 Rude      | 4 | NSFW | The Sheet!|
| Tryone 3 Rude      | 3 | NSFW | Mediocre|
| Tryone 2 Safe      | 2 | SFW  | Bad|
| Tryone 2 Rude      | 2 | NSFW | Shyte|
| Tryone 1 Safe      | 1 | SFW  | Awful|
| Tryone 1 Rude      | 1 | NSFW | Foo kin awful|

Bonus: I added two more actions called "Jesus Christ" and "Hail Satan" that allow me to mark if a song is overly religious or not (especially for Xmas music).
