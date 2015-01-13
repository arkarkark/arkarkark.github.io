---
date: 2015-01-13
layout: post
title: Authy Window Size
tags:
- chrome
- extension
- authy
---

I use [Authy](https://chrome.google.com/webstore/detail/authy/gaedmjdfmmahhbjefcbgaolhhanlaolb) for my google authenticator code generation. I like the desktop chrome app and extension, but the popup window is too small and I usually have to scroll it.

I found all the places you have to change to make the window taller.

Open [chrome://extensions/](chrome://extensions/) and find the authy extension and look for the `ID:`. It's a 32 character string. Now you need to go to the extension's directory. Note: my authy is installed in my default chrome profile (also know as People), you might need to replace `Default` with `Profile\ 1` or something.

```bash
cd ~/Library/Application Support/Google/Chrome/Default/Extensions/abcdefghijklmnopqrstuvwxyzabcdefg/1.0.7_0
ADD=410; \
perl -p -i~ -e "s/:(590)/':' . (\$1 + $ADD)/ge" js/background.js js/app.js; \
perl -p -i~ -e "s/(max-height:)(544)(px;)/\$1 . (\$2 + $ADD) . \$3/ge" css/app.css
```

Now hit cmd-r on the chrome extensions page and click the authy button again (authy must be closed).

A height of 1000 (adding 410 pixels to each) worked great for 12 accounts.

If you want to go back to how it was, this should do it. Then you can use your command history to go back and edit the ADD variable.

```bash
for f in js/app.js js/background.js css/app.css; do \mv -fv ${f}~ ${f}; done
```

You'll know when authy gets updated because this'll break and you'll have to go do it again. You _could_ disable updates by messing with the update_url in manifest.json if you like. I'd rather get the update and apply this fix again.

Sorry, I got a bit wanky with the command lines there...
