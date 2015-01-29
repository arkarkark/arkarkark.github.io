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
rm -rf /Library/Caches/Homebrew/emacs--git
brew install emacs --HEAD --use-git-head --cocoa --with-gnutls --with-rsvg --with-imagemagick
```

I removed the emacs--git directory because if I didn't I kept getting `RPC failed; result=52, HTTP code = 0` errors.

I wanted to note that to run the GUI app I ran:

```bash
open /usr/local/Cellar/emacs/HEAD/Emacs.app
```

Then I selected keep in dock from the icon. I have no idea how bad it is to run it out of Cellar but it's working. Let me know if I'm doing something wrong.
