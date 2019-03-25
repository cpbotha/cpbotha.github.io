---
title: Amazingly crap print support in Ubuntu 6.06
author: cpbotha
type: post
date: 2006-09-03T17:19:52+00:00
url: /2006/09/03/amazingly-crap-print-support-in-ubuntu-606/
categories:
  - Uncategorized

---
Hi there kids!

Remember, all operating systems suck completely, even Loonix, the shareware system written by Luunis Torvaldez, the Mexican hacker responsible for other shareware greats, such as the desktop environment Gloom.

Because this is a long(ish) text, I&#8217;ll subtly hint at the conclusion: print support in Ubuntu sucks really badly, which is all the more crappy because Ubuntu is otherwise a fine distribution. Now back to my story&#8230;

In any case, today I lost a few precious hours of my life (I really had more important things to do) trying to configure the printer on my Ubuntu 6.06 server as a public / guest access printer. In other words, **anyone** attached to my network should be able to print to this printer.

First attempt: get the Ubuntu CUPS installation to accept print requests from remote clients via IPP. This was working just fine under CentOS 4.x, thank you. After much gnashing of teeth and editing of config files (necessary &#8220;allow&#8221; clauses and what not), clients could get printer status and could even access the admin pages on :631, but could not print. Nothing helpful in the log files, even with higher log levels. It turns out that Ubuntu doesn&#8217;t really support this setup: they prefer that one comes in through Samba.

Second attempt: configure the samba printer for public access. This FINALLY worked when I set &#8220;security = share&#8221;, but the samba manuals warn against this and strongly discourage its use. ARGH. Can you configure a public printer with security = user? It seems not.

So, Linux has been around in some form or another for 15 years&#8230; every year we are promised that &#8220;This year will be the year of Linux! Ready for the desktop I say!&#8221; and every year it still sucks in new and original ways. Yes, nerdy administrators itching to leave a comment, Linux works well if you&#8217;re an *nally retentive git with nothing else to do but read manuals and browse source code (or just an otherwise well-adjusted student with too much time), but for the rest of us with Real Work and Other Things To Do, **this just doesn&#8217;t cut it**.