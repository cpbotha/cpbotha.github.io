---
title: What I did this, err, summer
author: cpbotha
type: post
date: 2008-11-17T21:20:15+00:00
url: /2008/11/17/what-i-did-this-err-summer/
categories:
  - entertainment
  - life
  - meta
  - tech
tags:
  - e71
  - efs
  - life
  - security
  - windows

---
Taking a hint from Joe, aka [Swimgeek][1], here&#8217;s a summary of my life since the previous time we spoke:

  * The [VCBM 2008 workshop][2], my first attempt at playing the organising conference chair, went swimmingly.  Two days of solid presentations, a lovely dinner at Van der Dussen (no Ronald McDonald in sight!) and meeting up with many old friends.  I stopped stressing during the conference dinner.
  * I joined the ranks of the intelligentsia (As opposed to the millions of plebs with iPhones &#8211; oh stop whining and look at the stats.  Can&#8217;t find the stats?  Go figure out how to copy and paste, then get back to me. :) ) and acquired a Nokia E71.  _Best. Gadget. EVAR._ 
  * Had a fan-tas-tic holiday in South Africa.  Had profound conversations and the most raucous get-togethers with best friends and family.  Realised again how extremely lucky I am with people I&#8217;m this close with, on two different continents.  Linked up with my dad for the first time in too many years, which was cool.
  * Migrated my extremely complex todo system (I&#8217;m a foaming-at-the-mouth [GTD][3] follower) from [todoist][4] to a local installation of the open-source RoR-based [Tracks][5] software.  Todoist is really cool, but it&#8217;s very much deadline-oriented, whilst in the GTD world deadlines are just so passé.  DAMN I&#8217;m with it.
  * My laptop was sort of stolen and then returned 5 minutes later.  Besides the acute trauma that this caused, it got me wondering about the security of the Windows XP Encrypted File System thingy that I use to encrypt some of the more sensitive, err, documents on my laptop.  On Windows 2000, the fact that on a local install the administrator was the default data recovery agent (DRA), made it possible to decrypt a user&#8217;s files without having to crack that user&#8217;s password.  On a local install of XP, this is fortunately NOT the case.  I repeat, [**on a local install of XP there is no default recovery policy**][6].  In other words, a laptop thief needs to **crack your password to decrypt your EFS encryption**.  You can double check this by [downloading efsinfo][7] and running it on your files with &#8220;efsinfo /u /r your_files&#8221;.  It should confirm that there&#8217;s no recovery agent.  You should also check the strength of your Windows passwords with [ophcrack][8].  Your EFS is only as strong as the user password protecting it.  After my little episode, I&#8217;ve deleted most of those sensitive, err, documents from my laptop (they&#8217;re duplicated on a server at home) and encrypted even larger parts of my laptop hard drive, just in case.

Now I&#8217;m supposed to conclude this blow-by-blow with something profound.  I know, I&#8217;ll end with a quote attributed to Plato that I first saw in the PhD thesis of a friendly colleague.  At the time it made quite an impression on me:

> <span class="huge">Be kind, for everyone you meet is fighting a hard battle.</span>

Heck, it still does.

 [1]: http://www.swimgeek.com/blog/ "Link to Swimgeek's blog"
 [2]: http://vcbm.org/2008 "Link to VCBM 2008 website"
 [3]: http://en.wikipedia.org/wiki/Getting_Things_Done "Link to Wikipedia article on GTD"
 [4]: http://todoist.com/ "Link to Todoist"
 [5]: http://www.rousette.org.uk/projects/ "Link to Tracks website."
 [6]: http://support.microsoft.com/kb/887414 "Link to MS KB article concerning DRA on XP."
 [7]: http://www.microsoft.com/downloads/details.aspx?FamilyID=9c70306d-0ef3-4b0c-ab61-81da208f5c47&displaylang=en "Link to efsinfo"
 [8]: http://ophcrack.sourceforge.net/ "Link to ophcrack."
