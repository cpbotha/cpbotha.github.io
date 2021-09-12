---
title: 'F*ck off Murphy'
author: cpbotha
type: post
date: 2003-02-28T17:00:07+00:00
url: /2003/02/28/fck-off-murphy/
categories:
  - Uncategorized

---
As I was slaving away at my trusty Linux workstation today, the 30G [IBM][1] DTLA 307030 IDE hard drive started making extremely upsetting noises. These are not the kind of noises one expects from a smoothly operating hard-drive, but rather from some mechanical device in the throes of a messy death. Yes, this is one of [_those_][2] IBM hard drives and [Paul][3] confirmed that it was exactly this noise that his IBM hard drive made shortly before it went to heaven…
  
Fortunately, the main drives in this system are two 10K RPM U160 SCSIs and the 30G IDE is mainly for research data. However, research data are almost as important as research conclusions. I managed to backup all the important bits to Paul’s far-too-large new hard drive, interrupted at several nerve-wracking moments by the kernel complaining hysterically about the dying hard drive.

It was time to boot into the IBM [Drive Fitness Test][4]. It confirmed that there were corrupted sectors and proceeded to try and repair them for the subsequent hour or so. It _seems_ to have succeeded. I had to repartition the drive and took the opportunity to install EXT3 instead of ReiserFS.

All seems to be well now, but I haven’t written in the region of the affected areas yet. Cross yer fingers please.

 [1]: http://www.ibm.nl/
 [2]: http://www.anandtech.com/guides/viewfaq.html?i=71
 [3]: http://cpbotha.net/weblogs/paul/
 [4]: http://www.hgst.com/hdd/technolo/dft/dft.htm
