---
title: A first whiff of Gutsy Gibbon power-management
author: cpbotha
type: post
date: 2007-09-02T12:06:52+00:00
url: /2007/09/02/a-first-whiff-of-gutsy-gibbon-power-management/
categories:
  - tech

---
_(For The Impatient and Those With Important Things to Do: this is a long story about Ubuntu Gutsy Gibbon and how Linux Powertop can help you to make you laptop battery last longer. It has pictures. At the end.)_ 

One of the main problems I had with Ubuntu 7.04 (Feisty Fawn) [as you will recall][1], was the extremely poor power management. You don’t spend thousands of euros on a laptop to install an operating system on that drains its batteries in half the time it takes Windows to do the same.

Shortly around that time, somebody pointed me at [Linux Powertop][2], a tool developed by Intel’s Arjan van der Ven and that’s able to find the various processes that drain one’s battery. Another important component of the new power saving regime is the [tickless Linux kernel][3]: instead of waking up a set number of times per second like some obsessive-compulsive retard, it wakes up only when necessary and thus has the potential to save you even more power. Neither of these worked out of the box on Feisty. Yes, I know that one can install a backported kernel, I chose not to. Had important stuff to do.

Recently I managed to come into the possession of a 500G USB external hard disc. The temptation was far too great, and I installed [Ubuntu Gutsy Gibbon Tribe 5][4] (an alpha of the forthcoming 7.10) on a partition on this disc. Along with my laptop’s “boot from USB” functionality and GRUB on the MBR of the USB disc, I now have a beautiful bleeding-edge Linux to play with. Of course this only happens when I Don’t Have Important Stuff to Do.

After installing the powertop package with apt, I started it up and was met by the following display (click for a higher resolution version):

[][5]

<p style="text-align: center">
<a href="http://picasaweb.google.com/cpbotha/Screenshots/photo#5103890932568110178"><img src="http://lh6.google.com/cpbotha/RtSpwvgPNGI/AAAAAAAAB7Y/eilkZxStG4I/s400/gutsy_gibbon_PRE-powertop_nc8430.png"/></a>
</p>

Beautiful! This thing tells me what’s eating my battery, and it even gives human-readable tips on how to address the various problems. I did its bidding, and also set my ATI GPU to low-power mode with aticonfig (see my [Feisty review][6]) and this was the result:

[][7]

<p style="text-align: center">
<a href="http://picasaweb.google.com/cpbotha/Screenshots/photo#5103888072119891026"><img src="http://lh4.google.com/cpbotha/RtSnKPgPNFI/AAAAAAAAB7I/kiPqRoUbEFk/s400/gutsy_gibbon_powertop_nc8430.png"/></a>
</p>

In a few minutes, my laptop’s power consumption was reduced from 31.9W (1.7 hours) to 19.7W (3.1 hours), a significant savings. You may again colour me impressed.

So, it seems Gutsy Gibbon will probably address Feisty’s power-consumption issues. If it also delivers on its promise of better dynamic display (i.e. changing display at runtime) support, I will have to find something else to complain about.

_P.S. (added on 2007-10-02): Intel has recently created a website, [lesswatts.org][8], with even more information on power-managing (intel) hardware with Linux.   This [Ubuntu feature request][9] claims that most of the provided tips have been implemented for Gutsy.  I’ll do some more measurements later…_

 [1]: http://cpbotha.net/2007/04/10/a-critical-look-at-ubuntu-feisty-beta-on-an-hp-nc8430-laptop/ "Feisty beta review."
 [2]: http://www.linuxpowertop.org/ "Linux Powertop website"
 [3]: http://kerneltrap.org/node/6750 "Article about tickless kernel."
 [4]: http://www.ubuntu.com/testing "Link to what is now the Gutsy Gibbon page"
 [5]: http://picasaweb.google.com/cpbotha/Screenshots/photo#5103890932568110178
 [6]: http://cpbotha.net/2007/04/10/a-critical-look-at-ubuntu-feisty-beta-on-an-hp-nc8430-laptop/ "feisty review. again."
 [7]: http://picasaweb.google.com/cpbotha/Screenshots/photo#5103888072119891026
 [8]: http://lesswatts.org/ "LessWatts website"
 [9]: https://bugs.launchpad.net/ubuntu/+source/linux-source-2.6.22/+bug/144070 "ubuntu feature request w.r.t. lesswatts"
