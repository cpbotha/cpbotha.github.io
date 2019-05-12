---
title: "meepx1e: I haz new laptop!"
# we specify slug also, because hugo keeps the # in there, breaking routing
slug: "new-laptop-2019"
author: cpbotha
# REMEMBER TO CHANGE BEFORE PUBLISHING!
date: 2019-04-27T14:02:00+02:00
tags:
  - laptop
  - new computer
  - thinkpad
  - windows
  - x1 extreme
categories:
  - nerd
type: "post"

---
_WARNING: **EXTREME** PC hardware-related nerdiness ahead. Read at your own risk._ 

<figure>
<a href="x1_skulking_in_bush.jpg">
{{< img src="x1_skulking_in_bush.jpg" >}}
</a>
<figcaption>Just the new laptop, skulking in the bush.
</figure>

It is tradition around these parts that the welcoming of new computer machines
is celebrated by, amongst many other rituals, a sometimes incomprehensible
amount of customisation-related labour and a mention (or two) in these pages.

Some examples from the past include:

- [Hacking Radeon suspend / resume support into the Linux kernel and the
  X-Server in 2002](/2002/07/26/whoohooo-xfree86-dri-hacked-to-suspendresume/),
  so that my cheap clone laptop could too.
- [Acquiring my first name-brand laptop (HP NC6000) in
  2004](/2004/05/26/laptop-no-2/), with a whole gigabyte of RAM.
- [My first dual-core laptop in 2006](/2006/07/22/new-new-laptop-laptop/).
- [Reviewing Ubuntu Feisty on above-mentioned
  laptop](/2007/04/10/a-critical-look-at-ubuntu-feisty-beta-on-an-hp-nc8430-laptop/)
  led to, as far as I can remember, my first really popular post, with about
  50k visitors in a few days.
- Relatively low-key announcements during my macOS phase, starting with the [2015
  MacBook Pro](/2015/06/14/weekly-head-voices-91-theyre-back/) and then later
  the [2017 MacBook Pro](/2017/09/05/weekly-head-voices-125/) on my birthday in
  2017.

Well folks, this post exists because on Tuesday, April 17, 2019 I became the
new owner of a Lenovo ThinkPad X1 Extreme.

This new device, just like all the previous ones, took up a considerable amount
of mental cycles before, during and after its acquisition.

This does make sense: It's the technical artefact I use for a large part of the
day to interface with and shape the universe around me. This shaping is how I
try to create value, so the main physical tool I used for this should be as
sharp as possible.

# So, tell me, why did your somewhat stylish MacBook phase have to come to an end?

It seems like [just the other day when my mysterous employer bought me that
shiny 2017 top-of-the-line(ish) MacBook
Pro](https://cpbotha.net/2017/09/05/weekly-head-voices-125/#new-laptop).

They grow up so fast!

... at which point they summarily have to be replaced by a slightly different
and hopefully more effective new thing.

The virtual machines I have to use for some of my projects caused the [16GB
2.9GHz 2017 MacBook Pro](https://support.apple.com/kb/SP756?locale=en_US) to
grind to a halt once too often.

I evaluated upgrading to the [2018 model with 32GB RAM and the 8th generation
i7](https://support.apple.com/kb/SP776?locale=en_US), but the disappointing
keyboards on the current MacBook Pro range made it even trickier than usual to
justify the substantial price of the upgrade.

The MacBooks are stellar machines, but only if you can look past the keyboard.

To add to that, after five years of macOS, it was time to check that I was
still able to work just as efficiently with The Other desktop operating
systems.

# Why did you decide to get the ThinkPad X1 Extreme?

When you go searching for laptop workstations that are in the same class as the
15" MacBook Pros, one of the main candidates is the [ThinkPad X1
Extreme](https://www.lenovo.com/za/en/laptops/thinkpad/x-series/ThinkPad-X1-Extreme/p/22TP2TXX1E1),
which, to my delight, was straight-forward to obtain from my favourite local
supplier!

<figure>
<a href="x1e_180.jpg">
{{< img src="x1e_180.jpg" >}}
</a>
<figcaption>Can your workstation do this? (The keyboard is definitely an
improvement. I'm reserving judgement until a few months in. I'm still getting
used to that red mouse nub. In theory, this should be ideal for mostly keyboard
use with Emacs for example.) </figcaption>

</figure>

(Interestingly, the price down here in ZAR is better than the dollar price on
Amazon directly converted to ZAR. This is usually the other way round.)

I made a deliberate choice for the version with the FullHD screen, and *not*
the 4k multi-touch panel.

"WHAT? ARE WE BACK IN THE 1990s?!!" you might ask, tapping away on your
high-resolution touch device with its beautiful screen and superb battery life.

During the 1.5+ years of using the 15" MacBook Pro, with one of the most
beautiful screens in the business, I very rarely used that screen. Furthermore,
when mobile, the significantly longer battery life of the FHD version, along
with the slightly reduced weight, are more important.

Along with the 6-core 8750H i7 CPU, 16GB of RAM and 512GB of SSD ThinkPad, I
ordered an additional 1TB Samsung EVO Plus 970 NVMe SSD and an additional 16GB
RAM module.

One simply unscrews the bottom panel to reveal two accessible DIMM slots, and
two accessible M.2 SSD slots. I added the extra drive and extra RAM, put the
panel back, and booted up to a pretty sweet upgrade.

(Both drives are in the gigabytes per second read and write class. The built-in
WDC PC SN720 SDAQNTW-512G-1001 is only slightly slower than the Samsung 970.)

It's good to know that I will be able to upgrade the RAM to 64GB, and the
storage to multiple terabytes of SSD, should that become necessary, or should I
be able to fabricate some or other good reason for this in the future.

## Pro-tip: Beware duplicate volume IDs when you clone a drive.

I used the free [Samsung Drive Migration Software for Consumer SSD
tool](https://www.samsung.com/semiconductor/minisite/ssd/download/tools/) to
image the factory-install of Windows to the new 1TB Samsung SSD.

After this, I simply changed the boot order in the BIOS (which also swaps C:
and D:, oh Windows!, and Bob was my uncle.

OR WAS HE?!

Only later when diagnosing why the Windows indexer was not picking up any new
files from my drive, did I figure out that the duplicate volume IDs on the
drives was confusing it.

Even later, after I had almost forgotten about the volume IDs, I had huge fun
fighting with the Windows boot loader simply giving up after an Ubuntu install.

You won't guess what the issue was, or will you?

# What are your first impressions?

Although it feels lighter than the MBP, the laptop is thicker and slightly
bigger than the MBP. Due to the shape of the chassis, and especially the
ventilation rib on the bottom, it feels good in the hand.

The fans do come on quite easily in Windows, which can be disturbing. There are
fortunately a number of configuration options to ameliorate this issue.

The Linux support for this laptop is quite good. After a few hours of Manjaro
(I've always wanted to see what an Arch-derivative was like), I installed
Ubuntu 19.04.

With minimal tuning, I can get the idle power consumption (with Emacs running
of course) down to about 7W.

This would in theory give me 10 hours of staring at Emacs, which is epic.

(Shortly after getting the laptop, I had to invest a not inconsiderable number
of hours into fine-tuning my Emacs configuration for Windows. Although Emacs on
Linux is still the ultimate experience, Emacs on Windows comes close
enough. For now.)

Probably due to the reduced weight and due to the laptop being able to keep
itself cool much more easily, the laptop fares significantly better than the
15" MacBook Pro in the official Working in Bed and also Flipping Out Your
Laptop To Do Something Real Quick tests.

Other than that, features like the way the BIOS unlocks both hardware-encrypted
SSDs at boot using my fingerprint, are really quite neat.

# Do you have anything else to say?

No.
