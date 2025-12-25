---
title: Windows programming is nasty
author: cpbotha
type: post
date: 2004-01-13T00:39:53+00:00
url: /2004/01/13/windows-programming-is-nasty/
categories:
  - Uncategorized

---
I’ve spent two days trying to figure out how to send an ATA command directly to an IDE hard drive from Windows. I’ve finally succeeded, but with an undocumented and unsupported IOCTL call. It turns out that’s the ONLY way to do what I want, at least until Windows XP SP2 is released when the documented and supported version of a similar IOCTL will be made available.

That’s nasty.

By the way, C’T (an extremely technical German computer magazine, fortunately now with a Dutch edition as well) rules in more ways than one. If you’re looking for concrete information on how to abuse IOCTL_IDE_PASS_THROUGH, they’re the only guys who can help.
