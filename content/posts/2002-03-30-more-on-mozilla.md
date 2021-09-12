---
title: More on Mozilla
author: cpbotha
type: post
date: 2002-03-30T21:03:00+00:00
url: /2002/03/30/more-on-mozilla/
categories:
  - Uncategorized

---
I was getting overly confident with my Mozilla 0.9.9 and decided to install the Blackdown Java J2RE 1.3.1 as well as Macromedia 5.0.43 flash plugins. Well well well… mozilla started crashing all over. So I started cursing like in the old days… then I remembered something: [this entry][1] in the Mozilla bug tracking system.

What it comes down to is that the Flash plugin is buggy… it simply locks up if the /dev/dsp device is busy, whereas previous versions of this plugin would just disable their sound in this case. So, if you’re playing MP3s in the background (like I am) Mozilla will just seem to crash when you go to a Flash site. However, if you kill your mp3 player, Moz will continue. It also seems that certain sound cards and drivers DO allow multiple access to the /dev/dsp, in which case you won’t have this problem.

Another suggested workaround was to make use of the KDE (artsd) or Gnome (esd) sound servers and run both your mp3 player and Mozilla via these. For xmms you can install output plugins to make use of these sound servers and you can run Mozilla by making use of the wrappers (e.g. invoke mozilla with: artsdsp mozilla, in which case its access to /dev/dsp will be redirected to artsd). If you don’t want to install the MP3 player output plugins (or your player doesn’t support something like this) you can start it with the wrapper as well.

 [1]: http://bugzilla.mozilla.org/show_bug.cgi?id=58339
