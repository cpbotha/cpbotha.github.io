---
title: Keeping the writer in suspense
author: cpbotha
type: post
date: 2003-03-16T17:27:07+00:00
url: /2003/03/16/keeping-the-writer-in-suspense/
categories:
  - Uncategorized

---
I downgraded my kernel to 2.4.21-pre3 with acpi 20030109, swsusp v16 ([my version of these patches][1]) along with my [hub.c thread kill kludge][2]. The latter is so that USB doesn&#8217;t cause your suspends to hang forever because the frikking khubd thread doesn&#8217;t want to die. It sometimes gets cranky like this after one suspend/resume cycle.

This is the combination that stopped working after my RAM upgrade and incited the upgrade to 2.4.21-pre4, acpi 20030228 and swsusp v19. However, as reported in [a previous posting][3], the swsusp v19 combination can be quite slow and has caused the occasional oops at suspend.

Fortunately, after having come across [this mail][4] again I could get swsusp v16 to work on my increased RAM configuration. v16 was hardcoded for a maximum of 512MB RAM.

So, now I can suspend in about 10 &#8211; 15 seconds (compared to 30 seconds with v19) and resume in just under 60 seconds (compared to 90 seconds with v19).

 [1]: http://lister.fornax.hu/pipermail/swsusp/2003-January/001438.html
 [2]: http://cpbotha.net/thingies/hub.c.thread_kill9.diff
 [3]: http://cpbotha.net/weblogs/cpbotha/archives/000113.html
 [4]: http://lister.fornax.hu/pipermail/swsusp/2002-November/001123.html