---
comments: false
date: 2017-10-25
layout: post
permalink: 2017/10/25/merging-photos-libraries.html
tags:
- apple
- photos
title: merging iPhoto and Photos albums into one big thing and deduping them
---

I have a problem organizing my photos. It used to be that iPhoto didn't do well with lots and lots of photos so every year I'd start a new iPhoto library. But I didn't want to lose my favorites so every year I'd copy over my 5* pictures and a few special albums so that they'd follow me around. Couple that with all the pictures I had from the olden days when I used to use php gallery and a quick dalliance with Picasa for Mac.
So my Pictures directory was a mess, 750GB of photos and so many dupes I didn't know what to do.

I heard [Photos.app](https://www.apple.com/macos/photos/) for Mac was a replacement for Aperture which could handle any size of library so decided to give it a shot. I decided to get just everything in the same library and I remember it doing a good job of detecting duplicates as it imported so maybe that would cut things down in size.

First up Update all the iPhoto Libraries by opening them with Photos and letting it do its thing. Sometimes I had to use the [iPhoto Library Upgrader 1.1](https://support.apple.com/kb/dl1523) and then it with Photos.

Then I noticed if I looked in each library by right clicking on the library in Finder and "Show Package Contents" under the Masters directory it was sometimes pretty well organized. I've done super minimal editing on my photos so this was o.k. for me. It might not be for you.

I used [this AppleScript](https://discussions.apple.com/docs/DOC-8931) to load all those directories into my master library and it worked o.k. It was however annoying that for each directory/album it would prompt me to ignore duplicates and if I wasn't at my machine to help it along the script would die and starting again would mean even more dupes warnings (for every album as far as it had got). After all this I had all my photos in one place! I was down from 750GB to 485GB and 125,000 items.

But still there wer lots of duplicates in my albums. I've tried things like this [Duplicate Cleaner For iPhoto](https://itunes.apple.com/us/app/duplicate-cleaner-for-iphoto/id586862299) before and not been super impressed. I've always beeen worried that I was accidentally removing something I only had one copy of and there were just too many pictures to check them all. Since I'd recently used the script editor I thought AppleScript might be the solution to my problem. Now I had two problems.

I broke it down into two stages. First I went through all my Masters files and if I found an image that had the same SIZE as another image, I checked the sha256 hash of that file to see if it was the same file. If so I added it to a list. Then I dumped all that out as json. Here's the script I used: [finddupes.py](https://gist.github.com/arkarkark/42e32ea7c38589092e572e1394f5dd9e).

<script src="https://gist.github.com/arkarkark/42e32ea7c38589092e572e1394f5dd9e.js"></script>

Great, now I have a list of files that are the same. Turns out 21,480 of my files were duplicates and some of them multiple times so I had around 30,000 files to remove from my library. Luckily I had the full path to all the files. This should be really easy. I started off trying to write some AppleScript to do it, but that syntax is awful. Luckily I noticed that I could also write my AppleScript as JavaScript (aka JXA). But nothing seemed to work. `console.log()` helped me sometimes but for anything useful it would just say `Error: Symbol.toPrimitive is not a valid class for _whatever_`. So I was mostly shooting in the dark. One thing I learned was that File -> Open Dictionary allowed you to see the methods and objects available to an application. Also those objects have members that you need to access with getters/setters, but only sometimes of course. The Photos application has albums that you reference like `photos.albums[i]` but each album has a name, but you need to reference that as `photos.albums[i].name()`. They also claim to be ES6 compatible, but none of my `.filter` or `.forEach` seemed to work so I kept my JS super simple. There was also a huge lack of examples becuase Google got iPhoto and photos confused and most examples were in AppleScript not JavaScript.
I did find the [JXA Cookbook](https://github.com/JXA-Cookbook/JXA-Cookbook/wiki/Home) to be super helpful!

After some work I had some code to find a specific album (I was going to put all the duplicates in an album called **DUPES**). I'd worked out it's much easier to work on JXA using a shebang file and my editor and I also worked out that each mediaItem only had access to the base filename not the full path. SHIT. I did have access to something called an `.id()` on each mediaItem and it was a 22 character long string. If I knew the IDs of the files I wanted to find I could first search by filename, then see if a file with that id was in the results.

More sleuthing and I found databases/photos.db in the Photos library package contents and it was a sqlite3 database. `sqlite3 photos.db .dump > dump.sql` on the 1.4GB file and a quick `fgrep Hiv4RFtDTDac6hRfSOXP2A dump.sql` (that being a hash I'd found using my AppleScript). Showed me that that id was in tables called `RKCustomSortOrder` and `RKVersion`. `RKVersion` looked promising but didn't have a file path anywhere in it. I gave up trying to use sqlite3 and used [DB Browser for SQLite](http://sqlitebrowser.org/) (I did a `brew cask install db-browser-for-sqlite`). I found `RKVersion` could go to a `masterUuid` and from there I could look up that uuid in `RKMaster` and get an `imagePath`. A solution was in sight.

I wrote some python to use the sqlite3 python package and open the database, open up my json list of duplicates. Remove the shortest path from each duplicate list (to keep one!) and then look up each `imagePath` of each duplicate to remove in `RKMaster`, then look up that `masterUuid` in `RKVersion` and get a `uuid` that I could use in some JXA later. I then output this as json for later processing...

<script src="https://gist.github.com/arkarkark/6439c585f104c3f95d38ddbaed103662.js"></script>
Here's [processdupes.py](https://gist.github.com/arkarkark/6439c585f104c3f95d38ddbaed103662) that does that.

There's more in that script that's left over from some other processing so you might have to dig through the weeds a little.

Finally and end in sight. I ran it once to make montage contact sheets using [imagemagick](http://brewformulas.org/Imagemagick) just to super double check things out. But I really didn't need to do that if the SHA256 hash is the same I can be pretty sure. Then I fiddled with the code and made it output the ids to a json file. I then just pasted that into my JXA file to add the photos to an album.
If I were doing it again I'd just use two Albums, one where I add everything (where each photo should appear at least twice) and then another album where I can just blow away all the images).

[movephotoswithidtoalbum](https://gist.github.com/arkarkark/fede9d24570f4c866b3b940c70038765)
<script src="https://gist.github.com/arkarkark/fede9d24570f4c866b3b940c70038765.js"></script>

It ran. I selected all the photos in my DUPES album and cmd-option-deleted them into oblivion.

After removing the duplicates I was down 20GB to 465GB. not bad, but still too large to keep on my primary SSD which would make Photos much faster.

Next step was the move all my videos out of Photos and into their own directory, I'll use iMovie to keep track of those. That saved me another 250GB so now my library was down to a manageable 214GB.

I noticed I had a lot of thumbnail images that were effectively useless. I spent ages trying to work out if I had the originals of those, but in effect they were so useless I should have just seached for `sml`, `small`, `thumbnail`, `bak`, `highlight` and blown away those files with a cmd-option-delete.

Next up I had a few tiff images which were huge (10x larger than a similar jpeg and I really couldn't tell the difference). I also had a jpg version of each tiff, but it was a lower resolution! glad I caught that. So I did some work to put all those (high and low res) into my dupes album, converted all the tiff outside of Photos, blew them away and then added the newly converted jpgs back. `convert wedding1.tiff wedding1.jpg` is pretty awesome. Actually it was more like `fgrep tif allfiles.txt  | while read fil; do NF=$(basename "$fil"); echo "$fil"; convert "$fil" "${NF/.tif*/.jpg}"; done` but you get the idea.

During my testing I had used [exiftool](http://brewformulas.org/Exiftool) to make sure the dates were kept during conversion, I was sure they were, but alas when they were loaded into Photos they looked like they had just been taken. Oh well, the Adjust Time menu item under Image was enough to get me close.

I also blew away all the .bmp, .gif, .nef, .psd and .pdf images, they were junk. I left the .aae files.

End result: 93,000 photos in 212GB very manageable.

I lost a LOT of information in this move (Faces, some albums, probably much more), but I feel it's worth it to have a single collection of unique photos. I can always try and add some of that back in with my new found albums.db knowledge.

Talking of which... Next up I'm going to try and look at the data in that photos.db database and work out stuff about my library.
