---
title: All operating systems suck
author: cpbotha
type: post
date: 2002-09-13T16:42:00+00:00
url: /2002/09/13/all-operating-systems-suck/
categories:
  - Uncategorized

---
At least, all operating systems that I’ve worked with suck in some way or another. These are not minor quibbles, but major problems. It seems these fundamental problems are present in both open and closed source OSen.

You’ve probably read [The Cathedral and the Bazaar][1] by Eric Raymond, so you know the difference between the two methodologies. Most of the open source development that I’ve come into contact with adheres to the Bazaar philosophy. The problem with the Bazaar philosophy is that almost anyone is allowed to contribute to the code (of Linux for instance). A few of these contributers are _very_ clever people, but in a maverick kind of way. Whatever the case may be, they do not work together in the close-knit coordinated groups that you find in good software houses with effective leadership, but rather in a hackish manner. This wouldn’t have been such a problem, were it not for the fact that the rest (and the majority) of the contributers are not sufficiently experienced, inept or just plain stupid. Partly due to these phenomena, open source software seems to suffer from a total lack of consistency (in form, function and quality). In addition, one finds hundreds of half-assed software efforts on the web that will NEVER be completed. Compare this image to what you read [here][2] for instance.

Another problem is that everyone contributing to an open-source project can do more or less what they find amusing. This is the reason why documentation is always out-of-date or plain non-existent. Look at the brilliant API documentation of GTK 1.2.x for instance. Formal code testing is often also ignored. There are exceptions to this rule, such as [VTK][3] for instance. VTK makes use of a rather impressive unit testing framework and has excellent documentation. However, VTK is backed by a motivated company consisting of really clever people that coordinate the whole effort.

Hmmm, I started with OSen that suck, but the issues above apply to all OSS efforts, including operating systems. One other problem with OSS operating systems is of course vendor support. When a new video card is released, the first thing the vendor does is to create working drivers for Winblows. In a few cases, vendors have created very good closed source drivers ([NVidia][4]) or have made the specifications available ([ATI][5]) in order to address the non-Windows community. In the former case, however, the drivers have significant problems (the nvidia drivers do not support suspend/resume or power management on laptops, the drivers are exclusive to Linux/X86) and in the latter case, the open source XFree86 driver development effort doesn’t have the manpower or time to create rock-solid drivers in a reasonable time and parts of the specifications (e.g. HyperZ) can’t be released, meaning that the Linux drivers will ALWAYS be outperformed by their Winblows counterparts.

So, you decide to stop wasting time on open source products and buy a copy of M$’s latest and greatest: Winblows XP. Teams of very capable programmers (by all reports) have spent thousands of man-hours on creating this system. However, you now have to deal with a whole new can of worms. The OS might have driver support for every device you can think of and support all your state-of-the-art PC’s most interesting and obscure features, but you have _NO_ idea what this OS is doing behind your back and you are definitely at its mercy. M$ may download “updates” onto you PC automatically; there may be [security problems][6] that are deliberately kept from you; things like Palladium make sure that we live in interesting times; if there is some problem with component or driver, you’re at the mercy of the time-schedule and motivation of the vendor, even if you _do_ have the skills to fix it yourself. This is not such a pretty picture either.

We could go down the list of OSen that are available for the PC and for real UNIX workstations and we could make lists of similar issues. There can be no real 100% reasonable conclusion, but armed with these examples (and many more which I’m too lazy to write down) I can bitch: All operating systems SUCK.

 [1]: http://www.tuxedo.org/~esr/writings/cathedral-bazaar/
 [2]: http://www.fastcompany.com/online/06/writestuff.html
 [3]: http://www.kitware.com/
 [4]: http:/www.nvidia.com/
 [5]: http://www.ati.com/
 [6]: http://www.security.nnov.ru/search/document.asp?docid=3370
