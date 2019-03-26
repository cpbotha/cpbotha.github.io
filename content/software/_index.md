---
title: Software
author: cpbotha
type: page
date: 2007-02-16T16:17:02+00:00
layout: single

---
I really love working on software. This page contains a list of the things that I&#8217;ve written over the years, some open source and some not, as well as some of the things I&#8217;ve contributed to. One day, when I&#8217;m grown-up, I&#8217;d really like to return to Writing Really Nice Software.

First the list, not 100% complete, of software I made:

  * [envedit][1] is a user-friendly Windows Environment Editor, for modifying those pesky environment variables. _BSD open source._
  * cv_platform is a C++ framework I designed at [Stone Three][2] in 2000 that enabled simultaneous capture and real-time video processing from a number of cameras (at that time on Linux). It has been used in a number of projects and products. _Proprietary._
  * [DeVIDE][3] is the open-source and cross-platform Delft Visualisation and Image processing Development Environment. I&#8217;ve been working on this in some form or another since about 2001, and it actually gets used by quite a number of people I don&#8217;t even know. The latest release was in February of 2012. _BSD open source._
  * [vtkdevide][4], [vtktudoss][5] and [itktudoss][6] &#8211; low-level C++ algorithmics used mostly by DeVIDE, including volume renderers, data loaders, 3D UI widgets and image processing codes. _BSD open source._
  * [FrothMaster][7] &#8211; Whilst working at Crusader Systems in &#8217;99, now CSense, I designed the full software stack  (design of an embedded Linux distribution to fit in 4MB of flash, also image processing modules) and part of the hardware for this IP65 embedded industrial image processing box. We won a [SABS Design Institute award for this][8]. _Proprietary._
  * [hdstandby][9] is some low-level Windows code that I slapped together to set the hardware standby timeout on ATA hard drives. On some setups, this built-in timeout still causes spindowns even if the Windows power settings have been configured otherwise. This little utility MIGHT help in this regard. It might blow up your computer. Go [here][10] to chat about this utility. [Marty Vona][11] has written a patch that will also disable APM on the drive, just like hdparm -B 255. _Open source._
  * [ical to vcal converter][12] is a webapp with which people convert their google calendar exports to palm desktop compatible files. Used by a surprising number of people judging by the comments (and hits) on the blog post. _Open source._
  * [im2avi][13] is an application for making AVI films/movies from series of images, written in C++ and FLTK. _Not supported anymore._
  * [KMX][14] &#8211; somewhere in 2004 very late at night and on weekends, I architected and implemented the first version of KMX, [Treparel&#8217;s][15] flagship client-server system for the analysis and visualization of high-dimensional data. Many person years of development have gone into it since and now it is a thing of beauty that you too can own! _Proprietary._
  * [Linux kernel watchdog drivers][16] &#8211; In 1999 and 2000 I coded kernel 2.2.x drivers for three different hardware watchdogs for the embebded platforms I was designing for Crusader Systems (now CSense), and they let me put these online. _Open source._
  * [nvPY][17] is my ugly but cross-platform Notational Velocity-inspired simplenote-syncing note-taking tool. If you&#8217;re a nerd with a note-taking fetish, you&#8217;ll love this. _BSD open source._
  * [NyARToolkit Multiple Marker Tracking][18] &#8211; I added multiple marker tracking support to the NyARToolkit augmented reality marker tracking software library. _Open source._
  * [pam_pwdfile][19] is a Pluggable Authentication Module that you can use to authenticate users for any service with flat text username:password files. _Open source._
  * [The Paper CD Cover generator][20] is a webapp with which you can generate nifty PDFs that can be printed on an A4 and then printed to form a CD cover.
  * [TimeRank][21] is a next-generation personalized time-management system. I am the main architect, and designed this Django-backbone.js-jQuery-jQuery-UI web-app together with company co-founder Gerwin de Haan. _Proprietary._
  * [vtkFlRenderWindowInteractor][22] is a C++ class for combining FLTK and VTK. This was integrated with ITK quite some years ago. _Open source._

Then the list of software that I&#8217;ve contributed to:

  * doc++ &#8211; Donkey years ago (I estimate around &#8217;98 or &#8217;99) I fixed global  overloaded function parsing in this C++ document generation tool.
  * [ITK][23] &#8211; I worked mostly on the Python wrapping layer of Insight segmentation and Registration Toolkit, introducing  [exceptions][24], [observers][25] and [the ITK-VTK connection][26]. The wrapping layer has since been completely revamped in WrapITK by Gaetan Lehman and Zachary Pincus.
  * [JED][27] &#8211; I used to be the Debian Developer (around 2000) responsible for this emacs-like text editor and also contributed a number of patches, for example implementing font anti-aliasing on XFree86, improving bibtex support, and whatnot.
  * Linux kernel &#8211; low-level fixes I made to the 2.4.4 kernel for the VT82C686A south bridge in 2001, as well as [for the ov7620 camera sensor chip in &#8217;99][28], are in the kernel source.
  * [VTK][29] &#8211; When I was still working on my Ph.D., I had plenty of time to commit regularly to the Visualization ToolKit source repository. I worked on aspects of the Python wrapping, and a number of small changes here and there. For example, that Finalize() call in all vtk*RenderWindow  classes is MINE. :)
  * XFree86 &#8211; Somewhere in 2003, I designed and implemented [low-level S3 suspend/resume support for the ATI Radeon in XFree86][30], the dominant open source X Window System at the time. My code was integrated with mainline XFree86.

BTW, I make available (sometimes slightly modified) Python-enabled Windows builds of VTK and ITK:

  * [Latest VTK binaries][31].

&#8230; but you should rather just get the [DeVIDE Runtime Environment][32], it&#8217;s much better and more up to date.

 [1]: /software/envedit "envedit webpage"
 [2]: http://stonethree.com/ "Stone Three corporate website"
 [3]: http://visualisation.tudelft.nl/Projects/DeVIDE "DeVIDE homepage"
 [4]: http://code.google.com/p/devide/source/browse/?repo=vtkdevide "vtkdevide source repo"
 [5]: http://code.google.com/p/vtktudoss/ "vtktudoss project page"
 [6]: http://code.google.com/p/itktudoss/ "itktudoss project page"
 [7]: http://www.outotec.com/37010.epibrw "link to frothmaster"
 [8]: https://www.sabs.co.za/index.php?page=diaw00 "SABS design institute award"
 [9]: http://cpbotha.net/files/hdstandby/ "Link to hdstandby binary and source code."
 [10]: http://cpbotha.net/2004/01/13/windows-programming-is-nasty/ "Link to blog posting discussing this utility."
 [11]: http://www.mit.edu/~vona/ "Marty Vona's homepage."
 [12]: http://graphics.tudelft.nl/~cpbotha/cgi-bin/ical2vcal.cgi "ical2vcal cgi"
 [13]: /software/im2avi "im2avi webpage"
 [14]: http://treparel.com/uk/technology/kmx_technology/kmx_knowledge_mapping_and_extraction/ "link to KMX"
 [15]: http://treparel.com/ "Treparel website"
 [16]: http://cpbotha.net/files/watchdogs/ "linux kernel watchdog drivers"
 [17]: https://github.com/cpbotha/nvpy "nvPY page on github"
 [18]: /2010/06/05/processing-nyartoolkit-multiple-marker-tracking/ "nyartoolkit multiple marker tracking blog post"
 [19]: pam_pwdfile "pam_pwdfile homepage"
 [20]: http://cpbotha.net/pcdc/ "paper cd cover generator webapp"
 [21]: http://timescapers.com/ "link to timescapers website"
 [22]: /software/vtkflrenderwindowinteractor "vtkFlRenderWindowInteractor home page"
 [23]: http://itk.org/ "Insight Segmentation and Registration Toolkit"
 [24]: http://www.itk.org/pipermail/insight-users/2003-July/004316.html "itk python exceptions"
 [25]: http://www.itk.org/pipermail/insight-users/2003-July/004331.html "itk python observers"
 [26]: http://www.itk.org/pipermail/insight-users/2003-July/004388.html "itkvtk python connection"
 [27]: http://www.jedsoft.org/jed/ "JED text editor webpage"
 [28]: http://alpha.dyndns.org/ov511/download/2.xx/ov511-2.25/ov7x20.c "link to ov7620 source file"
 [29]: http://www.vtk.org/ "Visualization ToolKit website"
 [30]: http://cpbotha.net/software/dri_resume "historical page with dri_resume work"
 [31]: http://cpbotha.net/software/latest-vtk-windows-binaries/ "Latest VTK Windows binaries page"
 [32]: http://graphics.tudelft.nl/Projects/DeVIDE "DeVIDE website"
