---
title: Laptop causes Labour of Love
author: cpbotha
type: post
date: 2002-07-24T23:34:00+00:00
url: /2002/07/24/laptop-causes-labour-of-love/
categories:
  - nerd

---
I’ve [ported][1] the XFree86 Synaptics touchpad driver to GPM.
  
I’ve spent too many hours trying to diagnose the VT switch bug and finally [fixed][2] it with the help of Michel Daenzer.

Now I’m trying to get the Radeon to survive a suspend-to-disk and resume whilst in DRI mode. I can suspend and resume (with swsusp) out of X successfully if I’m not using DRI. With DRI I resume into a frozen X. I would really like to be able to suspend with DRI, as I do “3d thingies” often. At the moment I’m scratching in the Radeon kernel DRM to see what can be done. As always, I’ll keep you posted.

 [1]: http://cpbotha.net/gpm_wmode_alt.html
 [2]: http://sourceforge.net/mailarchive/message.php?msg_id=1862068
