---
title: 'ati2evxx is evil.  bad_pool_caller evil.'
author: cpbotha
type: post
date: 2007-09-26T22:48:25+00:00
url: /2007/09/26/ati2evxx-is-evil-bad_pool_caller-evil/
categories:
  - tech

---
This is really one of those notes to self one leaves all around the show and is later so surprised about when Google finds it in a few years time, thus saving one&#8217;s hide. Again. It&#8217;s like Back to the Future, only different.

So today I was plagued by BAD\_POOL\_CALLER BSODs at every single restart on my XP SP2 HP NC8430 laptop (acronyms rule o.k.). I fired up my windbg, pointed its symbol file path at &#8220;SRV\* c:\dbgsymbols\* http://msdl.microsoft.com/download/symbols&#8221; (you should probably remove the spaces after the *s) and loaded the latest memory minidump from windows\minidump (XP makes these by default). The backtrace pointed out the culprit: It was ati2evxx.exe, the infamous i&#8217;m-not-sure-what-exactly-i&#8217;m-doing-on-your-system ATI hotkey poller. First I nuked it with the brilliant sysinternals procexp, and then permanently nuked it with the equally brilliant sysinternals autoruns. My problems are over. I also feel better after nuking ati2evxx. TAKE THAT, YOU SOULLESS STEAMING P.O.S. SOFTWARE!

P.S. I&#8217;m really starting to frighten myself with Windows know-how. I should consider switching primary operating systems again.

P.P.S. Of course it was not that simple. ati2evxx turns out to be more important than &#8220;hot key poller&#8221; after all. It&#8217;s also responsible for updating PowerPlay settings, especially important for laptop users. So, I had to un-nuke it&#8230; after some more crashing and crash dump analysis, &#8220;avipbb.sys&#8221; rears its ugly head. Turns out this is part of the Avira Anti-Rootkit component. I&#8217;ve disabled this and can now reboot again without the BAD\_POOL\_CALLER BSOD. When I have more time, I&#8217;ll analyse this in some more detail and let you know.

Update on 2007-12-26: Even after having disabled the rootkit scanner in Control Panel | Add or Remove Programs | Avira | Change, I still experienced bad\_pool\_caller errors every now and then. Based on information in [this forum thread][1], and the fact that crash dump analysis still pointed at avipbb.sys, I then noticed that avipbb.sys was still running as a service. Using sysinternals autoruns, I&#8217;ve now disabled this. I&#8217;ll keep you posted.

 [1]: http://forum.avira.com/thread.php?threadid=26395&sid=1c673688365ac8931aeb6e5b297da506 "Avira form thread concerning avipbb.sys crashes."