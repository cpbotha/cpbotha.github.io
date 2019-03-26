---
title: Running mxit in mpowerplayer on Linux (Ubuntu 7.04)
author: cpbotha
type: post
date: 2007-10-21T08:41:03+00:00
url: /2007/10/21/running-mxit-in-mpowerplayer-on-linux-ubuntu-feisty-704/
categories:
  - tech

---
I&#8217;m peppering this with enough keywords so that other idiots will be able to find this easily. [MXit][1] is a mobile-phone based chat system that&#8217;s very popular in South Africa ([Rugby World Cup champions 2007][2], thank you very much; want to wine about Cueto&#8217;s &#8220;try&#8221;, then first click [here][3]). It is possible to run the MXit Java midlet on a J2ME emulator (am I saying this right?) such as [mpowerplayer][4] or [microemulator][5]. Of course this works on Windows, even the average 12 year-old MXit user can successfully follow the many guides available online and then brag about his technical prowess online to his &#8220;friends&#8221;.

Obviously, I had to get this working on Ubuntu Feisty Fawn (7.04), you really don&#8217;t have to ask why. And obviously, it Just Didn&#8217;t Work(TM). MXit, both versions 3.0.5 and 5.2.x, hang forever at &#8220;Registering&#8221; or &#8220;Logging in&#8221;. After much swearing and trying The Usual Solutions(TM), I dusted off my [ethereal / wireshark][6], and also my trusty old tcpdump and set out analysing TCP packet dumps.

I really hate packet analysis, it&#8217;s such a **pleb** thing to do. Oh well, one does one&#8217;s best to forget one&#8217;s breeding. Temporarily.

It turns out that if you set the maximum TCP receive buffer to 170K (instead of the default 1M on Feisty), everything starts working again. My current hypothesis is that some of the other auto-tuned TCP parameters than rely on the max receive buffer setting, now better accommodate the small MXit packets. For those of you who still don&#8217;t understand what all of this means, run the following as root to get MXit working on Feisty:

_echo &#8220;4096 87380 174760&#8221; > /proc/sys/net/ipv4/tcp_rmem_

To make this permanent across boots, check the man page for sysctl.conf or add the line above to your /etc/rc.local.

Let me know in the comments if this is useful. I optimistically estimate that there has to be at least one (1) other person that will run into this problem. Ever.

 [1]: http://www.mxit.co.za/ "Link to the MXit website."
 [2]: http://en.wikipedia.org/wiki/2007_Rugby_World_Cup "Wikipedia article documenting 2007 Rugby World Cup"
 [3]: http://pienkzuit.wordpress.com/2007/10/21/the-proof/ "No, it was not a try."
 [4]: http://mpowerplayer.com/ "mpowerplayer website"
 [5]: http://microemu.org/ "MicroEmulator website"
 [6]: http://www.wireshark.org/ "WireShark protocol analyzer website"
