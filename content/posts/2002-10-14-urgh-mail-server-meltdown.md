---
title: Urgh, mail server meltdown…
author: cpbotha
type: post
date: 2002-10-14T21:20:00+00:00
url: /2002/10/14/urgh-mail-server-meltdown/
categories:
  - Uncategorized

---
A DIMM in one of our mail servers decided to break today&#8230; to make a long story short, I had to install a new imap on my own machine (as I switched incoming MXes) and with the new installation a new SSL key was created. Evolution (the MUA) of course kept on trying the old server key. DOH.

After quite some minutes of swearing, re-installing and doing various other pointless things, I deleted the very suspicious-looking &#8220;cert7.db&#8221; and &#8220;key3.db&#8221; files in ~/evolution. Problem solved. This should be somewhere in the Evolution UI or at the very least help system.
