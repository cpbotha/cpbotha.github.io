---
title: Solving the frikking BadPixmap Firefox/Thunderbird crash on Debian Woody
author: cpbotha
type: post
date: 2005-01-31T18:14:15+00:00
url: /2005/01/31/solving-the-frikking-badpixmap-firefoxthunderbird-crash-on-debian-woody/
categories:
  - Uncategorized

---
Okay, you&#8217;re running Debian Stable 3.0 (it&#8217;s also called woody, or Linux 1958). Because this distribution is older than yer grandpaw, you have the firefox and thunderbird backports from www.backports.org installed.

However, you&#8217;re **not** happy, because these otherwise fine packages crash more often than you can open a window (in fact, that&#8217;s what makes them crash, for example thunderbird&#8217;s login window or the find window in firefox). In fact, you&#8217;re downright homicidal. Even admiring your brand-new mullet in your hand-mirror is not cheering you up!

You scratch around in the logs and find many messages like this:
  
``<br />
Gdk-CRITICAL **: file gdkpixmap-x11.c: line 218 (gdk_bitmap_create_from_data): assertion `window == NULL || GDK_IS_WINDOW (window)' failed<br />
`` 
  
and like this:
  
`<br />
The program 'mozilla-thunderbird-bin/mozilla-firefox-bin' received an X Window System error.<br />
This probably reflects a bug in the program.<br />
The error was 'BadPixmap (invalid Pixmap parameter)'.<br />
` 

You google, but find only requests for help concerning this problem; not an answer in sight. That&#8217;s why I&#8217;m writing this up, for the other two of you Debian 1958 users with this problem. HI THERE!

Add this to your /etc/apt/sources.list:
  
`<br />
deb http://ftp.acc.umu.se/mirror/mirrors.evilgeniuses.org.uk/debian/backports/woody gnome2.2/<br />
` 
  
and do an apt-get update and upgrade. Make sure your X is upgraded to 4.2.1 and your GTK to 2.2.4.

As far as I could see, the root of the problem is with libfreetype6 and libpango weirdness in the stock Debian Woody. This upgrade seems to fix it. It will probably break bunches of other things&#8230; :)
