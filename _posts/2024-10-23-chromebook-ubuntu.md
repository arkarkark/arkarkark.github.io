---
comments: false
date: 2024-10-23
layout: post
permalink: /2024/10/chromebook-ubuntu.html
tags:
- chromebook
- ubuntu
- rc
- elrs
- edgetx
- inav
- betaflight
title: Setting up my chromebook as a flight computer
---

I set up an old ACER C740 chromebook as my flight laptop and here's the steps I used.I used
[MrChromebox](https://docs.mrchromebox.tech/docs/supported-devices.html) to install
[ubuntu](https://ubuntu.com/download/desktop). I added a 128GB USB drive and set that up as /usr so
I'd have more free space.


libgconf-2-4 was missing so I added `deb http://cz.archive.ubuntu.com/ubuntu lunar main universe` to `/etc/apt/sources.list` and `sudo apt install libgconf-2-4`

download and install

 * `sudo apt install emacs git python3-setuptools fuse`
 * [Google Chrome](https://google.com/chrome)
 * [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher/releases/)
 * [ELRS Configurator](https://github.com/ExpressLRS/ExpressLRS-Configurator/releases)
 * [EdgeTX Companion](https://github.com/EdgeTX/edgetx/releases/)
 * [iNav Configurator](https://github.com/iNavFlight/inav-configurator/releases)
 * [Betaflight](https://github.com/betaflight/betaflight-configurator/releases)

for ELRS Configurator I needed to `sudo dpkg -i --path-exclude=*/icons/* expresslrs-configurator_*.deb` until [this bug](https://github.com/ExpressLRS/ExpressLRS-Configurator/issues/427) is fixed.
