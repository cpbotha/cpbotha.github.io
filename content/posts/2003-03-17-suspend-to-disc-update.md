---
title: Suspend-to-disc update
author: cpbotha
type: post
date: 2003-03-17T16:09:15+00:00
url: /2003/03/17/suspend-to-disc-update/
categories:
  - Uncategorized

---
As reported earlier, swsusp v19 is slower than v16 and can cause kernel oopses. Well, it seems that the work that Nigel Cunningham has done on v19 [yields much better results][1]. Apply all patches (patch-beta19-01 up to and including patch-beta19-06) over swsusp v19 to enjoy some of this goodness.

The magic combination is now: Linux 2.4.21-pre5, acpi 20030228, swsusp v19, Nigel&#8217;s 19-01 to 19-06, my khubd thread killer workaround and [my DRI resume patches][2].

See, it all Just Works(tm). Ha ha.

 [1]: http://lister.fornax.hu/pipermail/swsusp/2003-March/001930.html
 [2]: http://cpbotha.net/dri_resume.html