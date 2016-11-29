---
date: 2016-11-29
layout: post
tags: [appengine, https]
title: App Engine https
---

I've wanted to get https on [my url shortener](https://github.com/arkarkark/snippy/) for ages now. Especially since I use it as my browser's search engine so all my search history goes over it (proxied to Google or Amazon or IMDB or ...). [Let's Encrypt](https://letsencrypt.org/) will give you free certs that last for 3 months. So they have automated software to keep requesting them and updating the server, neat! But those scripts need to run on the server as root which cleary isn't going to work for App Engine apps. There's a few issues open to support app engine ([letsencrypt](https://github.com/letsencrypt/letsencrypt/issues/1480) and [appengine](https://code.google.com/p/googleappengine/issues/detail?id=12535)) but nothing automatic works just yet.

There is also [letsencrypt-nosudo](https://github.com/diafygi/letsencrypt-nosudo) that will do the cert request without needing sudo, which is good. It tells you to make a file available on your server or it gives you a python command that runs a server that returns the file, neither of which works well on App Engine. So I wrote a litle handler that will allow you to post facts to store and store them back. It's password protected so you can set facts with a script but not allow just anyone to store facts on your server. Then I modified [my fork of letsencrypt-nosudo](https://github.com/arkarkark/letsencrypt-nosudo) to run the signing commands (since it's not running on the server) and also post the data to app engine using my new api. I'm happy with how it works. So now I just need to run that every 3 months and paste the resulting file into [Google Cloud Console App Engine Certificates Settings](https://console.cloud.google.com/appengine/settings/certificates).

I modified the README.md of [my fork of letsencrypt-nosudo](https://github.com/arkarkark/letsencrypt-nosudo) which should have enough instructions to get you up and running.
