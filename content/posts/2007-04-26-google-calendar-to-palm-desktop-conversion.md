---
title: Google Calendar to Palm Desktop conversion
author: cpbotha
type: post
date: 2007-04-26T07:23:29+00:00
url: /2007/04/26/google-calendar-to-palm-desktop-conversion/
categories:
  - tech

---
_(The short story is: if you want to convert Google Calendar iCal v2 files to vCal v1 files for import into your Palm Desktop, use [this web application][1] I made last night. Please leave a comment on this posting if you use it!_

_If you&#8217;re interested in recent changes to the application, see [the dynamic changelog][2] on Google Code.)_

It&#8217;s amazing how just when you really do need to put all your time into some deadline, you find the perfect WAB, better known as _Work Avoidance Behaviour_.

In any case, last night I was planning to work on two proposals with rapidly approaching deadlines, instead I somehow was convinced that it should be easy to import some of those neat iCal v2 files available on the web (for example as exported from [Google Calendar][3]) into my trusty Palm Desktop 4.1, which I use on my laptop to manage my life and synchronise with my Palm Tungsten C.

It turns out that this is **far more complicated** than necessary. Google Calendar only outputs iCal version 2, Palm Desktop, even the latest version, only imports vCalendar version 1. There are a number of websites that state that simply renaming the .ics file to .vcs, and changing the version tag to 1.0 does the trick. **WRONG.** Google Calendar iCal files actually use iCal version 2.0 features, so this idiot workaround does not, well, work around.

By now it was almost time for bed, and I&#8217;d tried Sunbird (exports ical v2), Evolution (the windows version is the worst POS software I&#8217;ve _ever_ come across) and bunches of other things. No go. Finally I stumbled on [vcal.py][4] by Mark Bucciarelli. This _almost_ worked, except for a few bugs (empty field handling, a.o.) which I fixed, and the fact that it doesn&#8217;t handle RRULEs at all. After reading the vcal standard, I implemented a really ugly RRULE transformation that seems to do the trick, mostly.

I&#8217;ve packaged all of this ugliness in a simple CGI that you can now use to convert Google Calendar iCal version 2.0 files to vCal version 1.0 files for consumption by your Palm Desktop. Use this entirely at your own risk of course, but let me know in a comment on this post (see below) if it works, or if it doesn&#8217;t.

[Click here to convert][1]!

(if you&#8217;re interested in the patch source, go to the [ical2vcal site][5] on googlecode.[][6])

 [1]: http://graphics.tudelft.nl/~cpbotha/cgi-bin/ical2vcal.cgi "ical2vcal CGI URL"
 [2]: http://code.google.com/p/ical2vcal/source/list "ical2vcal change log in Google Code"
 [3]: http://google.com/calendar "Google Calendar URL"
 [4]: http://www.koders.com/python/fid0EB51599456E1DAA3DCEBFE8F007B43F6D51A0DD.aspx?s=calendar "Link to vcal.py"
 [5]: http://code.google.com/p/ical2vcal/ "ical2vcal site on googlecode"
 [6]: http://visualisation.tudelft.nl/~cpbotha/files/ical2vcal-0.1.tar.gz "link to ical2vcal source"
