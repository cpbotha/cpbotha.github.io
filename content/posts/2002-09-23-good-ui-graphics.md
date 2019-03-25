---
title: Good UI != Graphics?
author: cpbotha
type: post
date: 2002-09-23T23:26:00+00:00
url: /2002/09/23/good-ui-graphics/
categories:
  - Uncategorized

---
I tried out [Ximian Evolution][1] today. It&#8217;s an email client, actually more a personal information manager, that looks a lot like Outlook, except that Ximian is free, runs on *ix and will probably not get your computer infected with 298374987 different interesting yet unfriendly viruses.

Hey, interestingly, it seems the correct plural _is_ &#8220;viruses&#8221; and NOT &#8220;viri&#8221;. If you&#8217;re a pedant, dodge [this][2].

In anycase, usually I use [mutt][3] which, unlike Evolution, is exclusively text-based and 100% hot-key (shortcut) driven. For example, to compose a mail, I would go &#8220;m&#8221;, type the address, the subject and the body of the mail, then ctrl-x-s-x-c and finally &#8220;y&#8221;. The mail is sent in record-time.

With Evolution, I seem to be doing a considerable amount of clicking with my mouse, which definitely slows one down. For instance, with mutt I can type &#8220;c&#8221; and it will show me the first mail folder with unread mail (all my mail is of course sorted with procmail); simply typing enter takes me directly to the unread message itself. With Evolution, I have to click on some drop down list, then click on a folder with unread mail (at least it&#8217;s rendered in bold), then click on the message listing pane, then type &#8220;n&#8221; to go to the unread message. Maybe I&#8217;m just not going about this the right way? Whatever the case may be, at the moment MUTT with its far uglier text-based appearance has a _MUCH_ better user-interface than Evolution.

My interest in the Ximian product lies in its calendar and to-do lists however. I hear that syncing with my Palm Pilot is implemented really well. It would have been nice however if the mail client was somewhat more hotkey driven as this really impacts greatly on its usability. I hope 1. that there are some more hidden hotkeys I don&#8217;t know about OR 2. that this gets added in the next release.

BTW, I had to set up uw-imapd (so all my folders can remain in native mbox format; Evolution does support mbox, but in a very limited fashion) but my inbox is in a non-standard location. With debian, you can drop something similar to [this patch][4] into the source package&#8217;s patches directory before rebuilding it to do the non-standard inbox location thing. uw-imapd is NOT very hot on configuration.

 [1]: http://www.ximian.com/products/evolution/
 [2]: http://homepages.tesco.net/~J.deBoynePollard/FGA/plural-of-virus.html
 [3]: http://www.mutt.org/
 [4]: http://cpbotha.net/thingies/10_sysinbox.diff