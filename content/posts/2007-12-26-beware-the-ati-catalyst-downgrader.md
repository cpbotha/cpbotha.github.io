---
title: Beware the ATI Catalyst downgrader!
author: cpbotha
type: post
date: 2007-12-26T12:22:22+00:00
url: /2007/12/26/beware-the-ati-catalyst-downgrader/
categories:
  - tech

---
Non-technical or non-interested people:

  1. Good for you!
  2. I&#8217;m posting this so that others with similar problems have more joy with google than I did.

Two days ago I made the mistake of even wanting to downgrade my laptop&#8217;s (HP NC8430) Windows XP SP2 video drivers from ATI Catalyst 7.10 to the latest HP-blessed version (8.391.3-070626a-050362C). My reason for wanting to downgrade was that all the ATI drivers suck (on all operating systems), but downgrading to the HP version at least gets me HP support, which I still have on this corporate grade laptop.

In retrospect, I probably expected too much by just running the new installer instead of completely uninstalling the Catalyst drivers first. I spent the next few hours vociferously cursing away as I found myself in a position where the existing Catalyst Control Center (CCC) refused to uninstall and the new CCC refused to install. After applying all known registry and driver cleaners as well as some gratuitously overzealous manual registry destruction, I eventually did manage to remove all traces (or so I thought) of the old driver and CCC.

However, still no go from the new CCC.

I stumbled upon the official ATI Catalyst Uninstaller tool (cat-uninstaller). My troubles were over!

No. Recall that ATI sucks. Hard. Of course the official ATI Catalyst Uninstaller tool is exceedingly effective at not uninstalling anything from ATI. CCC just continued repeating the following helpful message:

> CCC &#8211; InstallShield Wizard
  
> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;
  
> The setup has detected that version 2.07.928 of CCC is already installed.
  
> This setup installs an earlier version of CCC (2.007.0629.2228).
  
> You will have to uninstall the previous version before installing this version.

At this stage, I was seriously contemplating ripping my laptop from its docking station and launching it into orbit right through the double-paned glass window, just so that I could feel slightly better. Fortunately, that very cold and logical little man living in my head (one of the more unpleasant voices) suggested [regmon][1]. After setting up some search strings, letting CCC spew the above message and examining the logs, I finally found the culprit: HKLM\ SOFTWARE\ Microsoft\ Windows\ CurrentVersion\ Uninstall\ {055EE59D-217B-43A7-ABFF-507B966405D8}

Just delete the complete key. I believe the ID belongs to the ATI CCC crap, you should find it if you search for a sub-key &#8220;Comments&#8221; containing the text string &#8220;ATI products&#8221;.

After successfully installing the new driver and CCC, I was still unpleasantly surprised with:

> Could not load file or assembly &#8216;CLI.Implementation, Version=2.0.2736.38315, Culture=neutral, PublicKeyToken=90ba9c70f846762e&#8217; or one of its dependencies. The system cannot find the file specified.

Which was fortunately easily solved by re-installing the WHOLE driver package, including the bundled .NET 2.0 runtime. This was quite strange, as .NET 2.0 was already installed on the system.

The punchline of this story is threefold:

  1. UNINSTALL any form of ATI Catalyst software crap BEFORE attempting to install any other ATI Catalyst software crap.
  2. ATI sucks. I also have more stories concerning the suckage of the ATI fglrx drivers on Linux (shortly: the latest 7.12 ones simply aren&#8217;t able to do 1680&#215;1050 although 7.11 was (known issue); don&#8217;t even try to connect your laptop to different displays dynamically; finally, don&#8217;t get me started on the crappy suspend / resume support unless you have the day off), but that&#8217;s a topic for another rainy day.
  3. When selecting new hardware, avoid ATI like the plague. Get NVidia if you need a GPU. I&#8217;m sorry AMD, you used to be cool, but you&#8217;ve now been infected by the suckage that is ATI.

And now for something completely different: [this beautiful movie][2] visually summarises my thoughts on Vista. It was linked from Bruce Eckel&#8217;s [blog posting][3] on why he&#8217;s also dumping Vista for XP. My experiences so far on Microsoft&#8217;s Most Disappointing Operating System EVAR (fortunately on other people&#8217;s machines) have been similarly negative.

P.S. If this by any chance helps you solve your ATI downgrade / upgrade / crossgrade problem, leave a comment man!

 [1]: http://www.microsoft.com/technet/sysinternals/SystemInformation/Regmon.mspx "Regmon homepage"
 [2]: http://blip.tv/file/340692 "Vista Sucks movie"
 [3]: http://www.artima.com/weblogs/viewpost.jsp?thread=221497 "Bruce Eckel's end of Vista experiment"