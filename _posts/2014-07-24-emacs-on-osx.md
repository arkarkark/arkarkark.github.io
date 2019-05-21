---
comments: false
date: 2014-07-24
layout: post
permalink: /2014/07/emacs-on-osx.html
tags:
- apple
- emacs
- osx
title: emacs on osx
---


I just switched over to using emacs from [brew](http://brew.sh/) rather than [emacsformacosx.com](http://emacsformacosx.com)

I really wanted 24.4 to fix the annoying distnoted runaway process bug.

It was as easy as:

```bash
brew uninstall emacs
rm -rf ~/Library/Caches/Homebrew/emacs*
brew cask install emacs
```

I removed the Caches directory because if I didn't I kept getting `RPC failed; result=52, HTTP code = 0` errors.

I wanted to note that to run the GUI app I ran:

```bash
open /Applications/Emacs.app
```

I used to run this but they stopped that working sometime in 2019. I hear the version above might not have imagemagick in it.
```bash
brew install emacs --with-cocoa --with-gnutls --with-rsvg --with-imagemagick
```

Then I selected keep in dock from the icon. working. Let me know if I'm doing something wrong. I had tried linkapp
