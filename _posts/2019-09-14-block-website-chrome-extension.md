---
comments: false
date: 2019-09-14
layout: post
permalink: /2019/09/block-website-chrome-extension.html
tags:
- chrome
- extension
- javascript
title: Block Website Chrome Extension
---

I have a problem with a certain online solitaire game. I'm not going to link to it because I wouldn't wish this addiction on anyone. It's haunted me for years. I hadn't played a game in a long time, but recently fell off the wagon. Anyway it's got out of hand again. I'm going to use foxnews.com as my example another site you probably don't want to visit.

I usually stop myself by editing `/etc/hosts` to add a `0.0.0.0 foxnews.com` line and that does the trick. One time I tried to get my fix and it took me ages to realize I'd done that to my hosts file.

But I recently got a new chromebook and you can't edit the hosts file on those so I knocked up a quick chrome extension to stop a website working. All available solutions needed access to all your websites and I understand why, but it's more permissions than I wanted to give away.

Here's the code from [the gist](https://gist.github.com/arkarkark/5b36e92f77c79dd920ee8a6c4c5325a0)

<script src="https://gist.github.com/arkarkark/5b36e92f77c79dd920ee8a6c4c5325a0.js"></script>

Here's what it looks like when it kicks in:
![blocked_website](/assets/images/block_website.png)

I had a terrible time trying to get that text large and centered. Mostly it was the vertical centering and trying to have as few elements as possible. I gave up, but Will saved the day and provided the magic CSS.
I may have played a few games while I was verifying it worked. Hopefully my last for a while.

I continued on my quest to have files auto formatted when I save them and along with Emacs' [json-mode](https://github.com/joshwnj/json-mode) this little snippet of code formats the buffer when I save it.

```lisp
(defun ark-json-mode-hook-function ()
  ;; (flycheck-add-mode 'json-jsonlint 'json-mode)
  (add-hook 'before-save-hook 'json-pretty-print-buffer 't 't))

(add-hook 'json-mode-hook 'ark-json-mode-hook-function)
```
