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
 * [ELRS Configurator](https://github.com/ExpressLRS/ExpressLRS-Configurator/releases)
 * [EdgeTX Companion](https://github.com/EdgeTX/edgetx/releases/)
 * [iNav Configurator](https://github.com/iNavFlight/inav-configurator/releases)
 * [Betaflight](https://github.com/betaflight/betaflight-configurator/releases)

#### ELRS Configurator

For ELRS Configurator I needed to `sudo dpkg -i --path-exclude=*/opt/*/icons/* expresslrs-configurator_*.deb` until [this bug](https://github.com/ExpressLRS/ExpressLRS-Configurator/issues/427) is fixed.

#### EdgeTX Companion

EdgeTX Companion has an `.AppImage` in that zip file. I copied it to `/usr/local/bin/` and `chmod a+x` it then I made this file in `/usr/local/share/applications/EdgeTX Companion.desktop`

```
[Desktop Entry]
Type=Application
Terminal=false
Name=EdgeTX Companion
Icon=/usr/local/share/icons/EdgeTX_StarLogo_Color_Vector.svg
Exec=/usr/local/bin/EdgeTX_Companion_2.10.5-x86_64.AppImage
```

I got the icon from [here](https://github.com/EdgeTX/edgetx.github.io/blob/master/downloads/EdgeTX_logos_svg.zip) (via [here](https://edgetx.org/logos/)).

#### Everything broke, machine hung

At some point during this, everthing broke and I couldn't unlock the machine and then it wouldn't boot into the graphical UI and hung while the last message displayed was about `gdm`. I managed to fix it by booting into recovery mode and uninstalling and reinstalling gdm. I think these are the steps I used:

1. power up and keep pressing the escape key to get into the bootloader menu
1. select the default boot option
1. keep pressing escape again and you'll get a `grub>` prompt
1. type normal and then press enter and press escape one more time
1. you should now be in a simple grpahical grub menu where  you can select recovery mode
1. after recovery mode has started select to drop down into a root shell
1. type `apt purge gdm3`
1. type `apt autoremove`
1. type `apt install gdm3`
1. control-D to exit back and start up as normal.
