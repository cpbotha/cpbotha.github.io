---
title: Your GMail account CAN be hacked over insecure WiFi
author: cpbotha
type: post
date: 2009-11-01T08:39:32+00:00
url: /2009/11/01/your-gmail-account-can-be-hacked-over-insecure-wifi/
categories:
  - life
  - nerd
  - tech
tags:
  - bbc
  - gmail
  - hacking
  - insecure
  - wifi

---
Today [The Next Web posted an episode of BBC Watchdog][1] where it was demonstrated how a GMail account was hacked through insecure (WEP) WiFi.

{{< figure src="/wp-content/uploads/2009/11/https_gmail_url.jpg" >}}


For those of you still wondering, **I’d like to confirm that it is indeed possible to hack a GMail account over insecure WiFi**: GMail does indeed always send your password through secure HTTP (SSL) so that this can’t be directly hacked, BUT, by default, the rest of your session happens through normal clear-text HTTP.  The Watchdog episode of course gives absolutely no technical details, but it’s most probably the [“sidejacking” attack][2] first published by [Robert Graham][3], where the **attacker reads the cookies of the post-authentication HTTP traffic and uses them to fool GMail into thinking that they are in fact the legitimate owners attacked GMail account**.  This attack works on other webmail and -service providers too.

In short, if you EVER use a network connection that you don’t trust, simply change the “http:” in your URL bar to “https:”, or, even better, change your browser connection to “Always use https” on the GMail Settings – General page.   **With both of these solutions, the whole connection will use secure HTTPS (SSL), and cookies can’t be sidejacked**.

The drawback of the secure setting is that your GMail access will be slightly slower than usual:  The encryption costs more compute time at both ends, and the transmission of data is slightly less efficient.

 [1]: http://thenextweb.com/2009/10/31/bbc-hacks-gmail-account-wifi-scary-st/ "Link to The Next Web post concerning GMail WiFi hack"
 [2]: http://www.tgdaily.com/content/view/34324/108/ "Details on sidejacking attack"
 [3]: http://erratasec.blogspot.com/ "Robert Graham's blog"
