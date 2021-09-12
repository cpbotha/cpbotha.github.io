---
title: Zyxel 650R-31 nat loopback
author: cpbotha
type: post
date: 2005-01-24T22:34:57+00:00
url: /2005/01/24/zyxel-650r-31-nat-loopback/
categories:
  - Uncategorized

---
I run a CVS server on a little linux box at home. This box is behind a Zyxel 650R-31 hardware firewall/router thingy that passes ssh connections from the outside to the linux box. I have a static IP, so a CVS spec looks something like: :ext:me@my.box – this works from the big bad internet. However, on my home LAN, the linux box has an internal non-routable IP, so CVS sandboxes on my laptop can’t be updated, as they have the my.box CVS root stored, and the Zyxel router only does port forwarding on its WAN interface.

The solution is to activate “nat loopback”, so that access to my.box will be passed through the LAN interface of the router to the WAN interface and then back again! To do this, telnet to the Zyxel’s admin interface, go to menu 24.8 (the command mode), and type “ip nat loopback on”.

Yay!
