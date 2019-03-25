---
title: Ubuntu 5.04 preview on Stoeptegel-1
author: cpbotha
type: post
date: 2005-03-11T21:12:04+00:00
url: /2005/03/11/ubuntu-504-preview-on-stoeptegel-1/
categories:
  - Uncategorized

---
I needed a machine to install [Oracle 10g][1] on and although my 300MHz Celeron [Ubuntu][2] 4.10 server (with 192M of RAM) is just perfect as fileserver and mini linux playground, those specs just don&#8217;t cut it when a real man decides to slap Oracle around for a bit.

Well, stoeptegel-1, my previous 3.7kg weighing 2GHz P4 Northwood (768M RAM) laptop seemed just perfect for the job. I cleared out a 12G partition and installed the brand spanking new Ubuntu 5.04 Hoary Hedgehog preview release. Keep in mind this is only going to be released in April.

Man, this is one slick little OS. It installed without a hitch and without even having to LOOK at a config file, I have a fully 3D accelerated X at 1400&#215;1050 on the laptop&#8217;s Radeon Mobility 9000 (M7). It has also installed for example the cute little battery applet in gnome, and it even works!

I haven&#8217;t tested hibernation, for example, but checking he Xorg.0.log afer a switch to VC and back, I see the following telltale log message:
  
`<br />
(II) RADEON(0): [RESUME] Attempting to re-init Radeon hardware.<br />
(II) RADEON(0): [agp] Mode 0x1f000201 [AGP 0x8086/0x1a30; Card 0x1002/0x4c57]<br />
` 
  
which comes right from [my own Radeon resume code!][3] This almost brings tears to my eyes, as it is the first contact I have with my patch in a stock-standard installation of Linux.

 [1]: http://www.oracle.com/database/index.html
 [2]: http://www.ubuntu.com
 [3]: http://cpbotha.net/dri_resume.html