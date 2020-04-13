---
title: 'meepz97: I haz a new computar machine!'
author: cpbotha
type: post
date: 2015-02-15T07:36:00+00:00
url: /2015/02/15/meepz97-i-haz-a-new-computar-machine/
categories:
  - nerd
tags:
  - nerdy
  - new computer
  - very nerdy

---
_WARNING: **EXTREME** PC hardware-related nerdiness ahead. Read at your own risk._ 

My most awesome employer to date (that&#8217;s [the vxlabs][1] of course!) decided to treat me with a brand new workstation. On Tuesday, February 10 of the year 2015 the new desktop PC arrived. (Around these parts, we have a long tradition of writing about new computer acquisitions, see for example [2002][2], [2004][3], [2006][4], [2008][5], [2009][6], [2010][7], [2011][8] or [2013][9].) 

Because this event has sparked quite some interest amongst the various groups reading this blog, management has decided to present workstation-related information in a Q and A format. 

<div class="figure">
  <p>
    <a href="http://cpbotha.net/wp-content/uploads/2015/02/wpid-meepz97_exposed.jpg" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title=""><img src="http://cpbotha.net/wp-content/uploads/2015/02/wpid-meepz97_exposed-249x300.jpg" /></a>
  </p></p>
</div>

## Say what?! A desktop PC and not a laptop??!

Yes people, it&#8217;s an actual desktop PC, not a laptop. They&#8217;re big boxy things that eat laptops for breakfast and they really appeal to old-school nerds like me. Plus, when I go to work at the coffee shop around the corner with a ginormous black midtower PC under my arm instead of some far-too-easy-to-carry mac laptop, the other hipsters have no choice but to concede that <i>I</i> am their new king.

(Beautiful and thin laptops have become completely mainstream. Even that erstwhile PC-toting bro with his suit supply suit and his excel spreadsheets and his outlook email now has one. Hehe.)

## What exactly do you have in that big black box?

I&#8217;m so happy you asked. Sensitive readers might want to look away, because this is going to get fairly graphical. I hand-picked all components from the limited set available to us this far south on the African continent. This is what I came up with:

- One hundred and twenty rainbows.
- Fifty growth-hormone boosted angry unicorns, with twenty spares.
- <a href="http://www.technologyx.com/featured/gigabyte-ga-z97-d3h-motherboard-review/">Gigabyte Z97-D3H motherboard</a> (Intel LAN, Realtek ALC1150 audio)
- <a href="http://www.guru3d.com/articles-pages/core-i7-4790-processor-review,1.html">Intel Core i7 4790</a>
- 16 JIJABYTES of Corsair DDR3 RAM
- <a href="http://www.guru3d.com/articles-pages/gigabyte-geforce-gtx-750-ti-windforce-review,1.html">Gigabyte GeForce GTX750Ti Windforce</a> graphics
- <a href="http://www.techradar.com/reviews/pc-mac/pc-components/storage/disk-drives-hdd-ssd/samsung-850-pro-512gb-1255900/review">Samsung 850 PRO 512GB SSD</a>
- <a href="http://www.guru3d.com/articles-pages/cooler-master-cm-690-iii-review,1.html">Cooler Master 690 iii chassis</a> with 550W Cooler Master Vanguard power supply
- More rainbows.

As nerdiness-fuelled retail fixes go, this rated 23 on a scale of 1 to 10, with 10 being multiple head asplosions. Even now, multiple days later, when I look sideways at the beautiful black box, my knees turn into jelly and I blush a little bit.

## What operating system have you installed on this machine?

Emacs and Linux, software of the gods.

(By the way, if you run into kernel GPFs in <code>__slab_alloc</code> with this hardware, remember to add <code>intremap=no_x2apic_optout</code> to the kernel boot parameters. It seems the BIOS is being naughty and reporting that it does not have x2apic when it in fact does.)

## How fast is the Samsung 850 PRO SSD?

This SSD is STUPID FAST, there is just no other way to describe it.

Anandtech <a href="http://www.anandtech.com/show/8216/samsung-ssd-850-pro-128gb-256gb-1tb-review-enter-the-3d-era/13">has this to say about the drive</a>:

> To be honest, there is not a single thing missing in the 850 Pro because
> regardless of the angle you look at the drive from, it will still top the
> charts.

(My employer is still smarting a little bit from the cost angle however. I&#8217;ll work extra hard to compensate.)

## Are you disappointed that having to encrypt the SSD will slow it down?

Fortunately, this drive also has hardware-based full disc encryption built right in. A further major improvement over my previously favourite drives which also have hardware support for encryption, the Intel 520 SSDs, is that the Samsung 850 PRO supports the TCG Opal 2.0 standard for the configuration and unlocking of the drive encryption.

In short, all data that touches the drive is transparently encrypted, at over 500 megabytes / second (!!). When the PC boots up, it asks me for my decryption password. If I get it right, the drive unlocks itself; if I don&#8217;t it does not. If anyone (I&#8217;m not paranoid, they really ARE out to get me!) gets access to my PC by whichever means, they will most probably not be able see one bit of my or my client&#8217;s data.

If you&#8217;re interested, you can find much more detail about how this works, and I how I configured it using open source tools, in <a href="http://vxlabs.com/2015/02/11/use-the-hardware-based-full-disk-encryption-your-tcg-opal-ssd-with-msed/">this other post I wrote over at vxlabs.com</a>.

## Are you happy now?

Yes.

 [1]: http://www.vxlabs.com/
 [2]: http://cpbotha.net/2002/07/17/toe-matj-toe-sei-not-enaf-taim/
 [3]: http://cpbotha.net/2004/05/26/laptop-no-2/
 [4]: http://cpbotha.net/2006/07/22/new-new-laptop-laptop/
 [5]: http://cpbotha.net/2008/07/15/pleasure-apparatus-2008/
 [6]: http://cpbotha.net/2009/09/05/weekly-head-voices-for-week-36/
 [7]: http://cpbotha.net/2010/11/21/an-inside-job-weekly-head-voices-33/
 [8]: http://cpbotha.net/2011/08/16/new-samsung-np300v3a-laptop-is-welcomed-into-the-family/
 [9]: http://vxlabs.com/2013/03/24/acer-v3-571g-fullhd-ips-superb-priceperformance-linux-development-laptop/
