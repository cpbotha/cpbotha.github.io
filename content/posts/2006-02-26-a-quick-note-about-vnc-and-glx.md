---
title: A quick note about VNC and GLX
author: cpbotha
type: post
date: 2006-02-26T16:23:52+00:00
url: /2006/02/26/a-quick-note-about-vnc-and-glx/
categories:
  - Uncategorized

---
I’m doing some image processing heavy-lifting this weekend with [DeVIDE ng1.phase1][1] (that’s the not-yet-released next generation). The Windows XP scheduler is quite crappy, so on my laptop (1.6GHz Banias, 1G ram, 5400 RPM HDD) this kind of work tends to slow everything else down. So, I upgraded my Linux server box’s RAM to 1G as well (it has an Athlon64 2800+ and is running Centos 4.2 Linux, 7200 RPM HDD) in order to use this for some of the heavy processing.

Because it’s a headless server (and has the ATI Radeon 7000/VE to show for it), I needed some graphical remote access software, such as VNC. Turns out that most VNCs (Real, Tight, Ultra) do not support GLX out of the box, so not even software-3D rendering is possible. Yes, I know that I could have used a more traditional X server based setup, but I like the idea of resuming my running session from everywhere.

After a brief stint with (Free)NX and discovering that its resume support (Linux server, Windows client, 1.5.0) is completely borked (after resume, your wallpaper is turned into the remote desktop, no interaction allowed), I came across [xf4vnc][2]. I took the Xvnc from this package and copied it over my existing realvnc Xvnc and now I have GLX. Yay!

(I’ve posted this so that others googling for “vnc glx” will find information more quickly than I did.)

 [1]: http://cpbotha.net/DeVIDE
 [2]: http://xf4vnc.sourceforge.net/
