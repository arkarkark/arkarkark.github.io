---
comments: false
date: 2024-10-22
layout: post
permalink: /2024/10/chromebook-ubuntu-usr.html
tags:
- chromebook
- ubuntu
title: Moving /usr to a different disk with unbuntu on a chromebook
---

I have a acer c740 chromebook which I take on trips with me. It was one of the fastest cheap chromebooks when it came out and it's still fine for browsing the web and watching movies when I'm travelling. You can still get them for [under $50 on ebay](https://www.ebay.com/sch/i.html?rt=nc&LH_BIN=1&_nkw=acer%20c740%204gb). Make sure you get one with 4GB of ram if you do get one.
I used to use this [chromebook benchmark list](https://zipso.net/chromebook-specs-comparison-table/) to compare various models. The Acer C740 is from Feb 2015!

Unfortunately Chromeos stopped supporting this hardware a few years ago so I used [MrChromebox](https://docs.mrchromebox.tech/docs/supported-devices.html)
to install Gallium and then eventually that ran out of support so I moved over to [ubuntu](https://ubuntu.com/download/desktop) and that went pretty well. The 16GB hard drive was a bit of a problem. I'd have to install updates piecemeal otherwise I'd run out of disk space. I would generally only have 1.5G free at most.

To free up space I'd have to run
```
dpkg -l linux-image
```

and see if I had multiple versions installed and if I did run something like this to remove them.

```
sudo apt remove linux-image-6.8.0-45-generic linux-headers-6.8.0-45-generic
sudo apt autoremove
```

I might have to reboot to get the latest kernel running before I could remove the old packages.

Anyway, I wanted to free up some disk space so I had the genius idea to move /usr to a different disk. I got one of these [128GB USB 3 drives](https://www.amazon.com/dp/B08ZCTPV79) that can just live plugged in all the time. Here's how I made it work.

Plug in the drive and open the apps and under Utilities you'll find Disks or you can just run `gnome-disks` from the terminal command line.
select your 128GB drive and remove the partition on it. Then add a 16GB partition and call it `usr` and make it be for linux. Then add an EXFAT partition for the rest of the disk (I called mine `data`).
now mount your `usr` and this'll show up under `/media/$USER/usr` ($USER is your username).
now copy over `/usr` like this

```
sudo rsync -Phav /usr /media/$USER/usr
```

That'll take ages, but once it's done you can then add this line to `/etc/fstab`


```
UUID=blah-blah /usr ext4 nodev 0 2
```

You need to replace `blah-blah` with the `UUID` of your `usr` partition from the disks program, click on the partition on your 128GB disk and the UUID should appear underneath. You can copy and paste on a chromebook by clicking the bottom right corner of the touchpad.

Now you need to move the old `/usr` so the new disk can mount onto an empty directory. As soon as you do that last command everything is going to stop working. make sure it's the very last thing you do and everything else is set up correctly beforehand. Especially the correct `UUID` in `/etc/fstab`.

```
sudo bash
cd /
mkdir /old.usr
mv /usr/* /old.usr/
```

now reboot and it _should_ start up just fine
verify that you can `ls` files and `sudo ls` too from a terminal and if that works you can

```
sudo rm -rf /old.usr
```

Now you have oodles of space. Which you will see when you run this command.

```
df -h / /usr
```

If you want even more space you can do the same with `/home` I didn't do this because I think the internal disk is faster than a silly USB drive and I wanted `/home` to still be fast.

## If it all goes wrong

If it all goes wrong and your machine no longer boots, you can make an ubuntu bootable USB drive boot from that into safe mode and then mount your chromebook root filesystem and fix whatever is wrong. Good Luck!
