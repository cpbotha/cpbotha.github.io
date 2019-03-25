---
title: Toshiba 2.5″ HDD power management
author: cpbotha
type: post
date: 2003-11-30T15:06:24+00:00
url: /2003/11/30/toshiba-25-hdd-power-management/
categories:
  - Uncategorized

---
Urgh&#8230; the Toshiba MK3018GAS 2.5&#8243; hard drive in my laptop keeps on spinning down every so often _in spite_ of Windows XP being configured only to spin it down after 30 minutes of idle time. This is extremely frustrating.

Under linux, hdparm -S with a suitable time-out did the trick just marvellously. After having investigated this issue with several different diagnostic utilities, it turns out the disc has its own power management as well. However, Toshiba doesn&#8217;t offer any utilities to configure this, nor does my BIOS have the right stuff.

I think I&#8217;m looking for something like the [IBM/Hitachi &#8220;Power Booster&#8221;][1], but for my Toshiba drive. If anyone has any other advice, I would gladly hear it.

 [1]: http://www.alphaworks.ibm.com/tech/powerbooster