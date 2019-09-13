---
comments: false
date: 2019-09-02
layout: post
permalink: /2019/09/add_imdb_movie_ratings.html
tags:
- apple
- itunes
- ruby
- appscript
- imdb
- mp4
- id3
- rating
title: Add IMDb Movie Ratings to iTunes
---

I'm please with this one. I rate my music and movies in iTunes but sometimes I have some movies to watch and I don't know which to watch next, or I want to recommend movies for us all to watch but don't know if my ratings are due to my weird taste or if everyone else loves the same movie. I usually end up looking up the movie on [IMDb](https://www.imdb.com) to see what others thought of it too.

I wanted to get the IMDb ratings into iTunes and I found [this gist](https://gist.github.com/catesandrew/942693/) but that 1. didn't work anymore and 2. put the ratings into the comments section as a string. But it was a great start! I did some poking around and there's a Beats Per Minute field that movies have that I'm not using at all, so I decided to put the ratings in there. My daughter also wanted the [movie content ratings (e.g. PG-13)](https://en.wikipedia.org/wiki/Motion_Picture_Association_of_America_film_rating_system#MPAA_film_ratings) besides movies to allow her to choose movies more efffectively.

Here is the end result: [add_imdb_movie_ratings](https://gist.github.com/arkarkark/eef9bb9cfedbc6507a8255e543dd5d1e)

<style type="text/css">
  .gist-data {max-height: 500px;}
</style>

<script src="https://gist.github.com/arkarkark/eef9bb9cfedbc6507a8255e543dd5d1e.js"></script>

Setup involves

```
gem install rb-scpt
brew install atomicparsley
```

You also need to put an API key from [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx) in  `~/.omdbapikey`

Usage: Just select some movies in iTunes and then run the script. For each movie it will search for it and show a list of matches, usually they just show up aligned perfectly and the first choice is the right one and you hit enter and it's updated. If the first one isn't the right one, enter the number of the correct answer and if the correct answer isn't there you can enter a new string to search for the movie you want. Or you can find the movie on IMDb and enter the full url or id (starting with `tt`) of the movie. Or you can even just enter a rating value if it's between 10 and 99.

The content ratings might not show up in iTunes until the script is finished. I usually do about 20 movies at a time.

This is not a script to update all the metadata (titles, descriptions, etc... of a movie) if you want to do that then [MetaZ](https://metaz.io) is fantastic.

Development was a bit of a roller coaster for me. I haven't written much code in almost a year. A while ago I had a go at updating the dependencies on my old appengine app and it was so frustrating that it reminded me right away why I quit my job. Generally I don't like Ruby, but I had an example that at least used to work and it was in Ruby and the AppleScript integration looked really nice. First to get the AppleScript stuff working took a while but I found [rb-script](https://rubygems.org/gems/rb-scpt/) which was a drop in replacement for `appscript`. Of course `imdb_party` also wasn't working anymore and it appeared IMDb was cracking down on APIs and scrapers and sidestepped it all by providing [csv files](https://www.imdb.com/interfaces/) of their data. I started writing stuff to read in the titles csv but it was so slow, I also wrote it in python and it was 3 times faster, but still over 40 seconds on each startup so that was a non starter. Then I looked at [omdbapi](http://www.omdbapi.com) again, I had found it previously but thought it wasn't IMDb data, but it was, complete with ratings! so I was able to use that with the 1000 queries a day free quota.

Updating the content ratings was harder since it wasn't exposed in AppleScript. I knew it was possible because some of my movies had content rating icons added by MetaZ. I found [AtomicParsley](http://atomicparsley.sourceforge.net/) could update content ratings, but when I did it on a file it didn't show up in iTunes unless I got the info on the file. I tried lots of different update a single file AppleScript stuff but none seemed to work other than a `tell application "iTunes" to refresh selection` at the end of my script so that's what I did. Updating the content ratings sometimes took a long time, other times it was quick. So that the flow of the script wasn't slowed down I did it in the background and then waited for it to complete at the end before I refreshed the selection. This was trivial in Ruby with a `@@things_to_wait_for << Thread.new do ...`. Really since all the files are on the same disk I should have used a work queue and a single worker, but it seems to be fine and I like this simplicity.

Pasting in the IMDb url was a nice touch when API errors showed up like when searching for the movie `Up`. I even thought about using readline to get the user data and pre filling the history with the movie choices but it was working so well it seemed unnecessary.

After it was all written I wanted to use some opinionated code formatter and rule applyer so I didn't have to worry about style as much. Sadly [Rufo](https://github.com/ruby-formatter/rufo) didn't support the version of Ruby I was using (2.4.4) so I `gem install rubocop`'d and used [rubocop-emacs](https://github.com/rubocop-hq/rubocop-emacs) which along with [Flymake](https://www.gnu.org/software/emacs/manual/html_node/flymake/) was nice and pointed out a whole bunch of stuff I was doing wrong. Of course I should have started with that, but hopefully I won't have to write much Ruby again. I plan on using [Black](https://github.com/psf/black) for my Python3 development. I didn't start with it because I wanted to get it written and working and I've spent too much time and frustration setting up the coding environment only to lose steam when it came down to actually writing the thing I wanted.

I also had a lot of trouble getting irb to work with readline on my mac. Here's the steps that finally got it to work.

```
brew install readline
rvm pkg install readline
rvm get head
rvm reinstall all --force
```

Publishing as a [gist](https://gist.github.com) seemed ideal for a small script like this. `brew install gist` will allow you to update it from the command line. I almost added command line switches to do it automatically, but that seemed like overkill.

BONUS: You can now run this script from the script menu in iTunes. just add the `run_add_imdb_movie_ratings.scpt` file into the `~/Library/iTunes/Scripts/` directory. You may have to fix the path in that file to point to your home directory or wherever you istalled add_imdb_movie_ratings.

```
tell application "Terminal"
    activate
    set currentTab to do script "/Users/ark/bin/share/add_imdb_movie_ratings; exit 0"
end tell
```
