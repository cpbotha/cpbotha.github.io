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

<img data-attachment-id="679" data-permalink="https://cpbotha.net/2009/11/01/your-gmail-account-can-be-hacked-over-insecure-wifi/https_gmail_url/" data-orig-file="https://cpbotha.net/wp-content/uploads/2009/11/https_gmail_url.jpg" data-orig-size="420,62" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;}" data-image-title="https_gmail_url" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2009/11/https_gmail_url-300x44.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2009/11/https_gmail_url.jpg" class="aligncenter size-full wp-image-679" title="https_gmail_url" src="http://cpbotha.net/wp-content/uploads/2009/11/https_gmail_url.jpg" alt="https_gmail_url" width="420" height="62" srcset="https://cpbotha.net/wp-content/uploads/2009/11/https_gmail_url.jpg 420w, https://cpbotha.net/wp-content/uploads/2009/11/https_gmail_url-300x44.jpg 300w" sizes="(max-width: 420px) 85vw, 420px" />

For those of you still wondering, **I&#8217;d like to confirm that it is indeed possible to hack a GMail account over insecure WiFi**: GMail does indeed always send your password through secure HTTP (SSL) so that this can&#8217;t be directly hacked, BUT, by default, the rest of your session happens through normal clear-text HTTP.  The Watchdog episode of course gives absolutely no technical details, but it&#8217;s most probably the [&#8220;sidejacking&#8221; attack][2] first published by [Robert Graham][3], where the **attacker reads the cookies of the post-authentication HTTP traffic and uses them to fool GMail into thinking that they are in fact the legitimate owners attacked GMail account**.  This attack works on other webmail and -service providers too.

In short, if you EVER use a network connection that you don&#8217;t trust, simply change the &#8220;http:&#8221; in your URL bar to &#8220;https:&#8221;, or, even better, change your browser connection to &#8220;Always use https&#8221; on the GMail Settings &#8211; General page.   **With both of these solutions, the whole connection will use secure HTTPS (SSL), and cookies can&#8217;t be sidejacked**.

The drawback of the secure setting is that your GMail access will be slightly slower than usual:  The encryption costs more compute time at both ends, and the transmission of data is slightly less efficient.

 [1]: http://thenextweb.com/2009/10/31/bbc-hacks-gmail-account-wifi-scary-st/ "Link to The Next Web post concerning GMail WiFi hack"
 [2]: http://www.tgdaily.com/content/view/34324/108/ "Details on sidejacking attack"
 [3]: http://erratasec.blogspot.com/ "Robert Graham's blog"
