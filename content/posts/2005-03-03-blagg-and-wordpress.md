---
title: Blagg and WordPress
author: cpbotha
type: post
date: 2005-03-03T22:11:59+00:00
url: /2005/03/03/blagg-and-wordpress/
categories:
  - Uncategorized

---
My infamous [weblog aggregator][1] relies on [Bloxsom Blagg][2] to do the grunt work.

The [WordPress][3] blogs of some of my friends were generating feeds with a [CDATA][4] tag in the description field. Blagg let this tag get through into the aggregator post, resulting in these posts not showing any description body. Oh, the tragedy!

The small change needed to fix this can be found [here][5]. Astute readers will see, in the lines of this patch, that Perl really does suck.

At some stage, I will _have_ to see about a possible migration to wordpress.

 [1]: http://cpbotha.net/weblogs/
 [2]: http://www.raelity.org/lang/perl/blagg/
 [3]: http://www.wordpress.org/
 [4]: http://msdn.microsoft.com/library/default.asp?url=/library/en-us/xmlsdk/html/xmconCDATAMArkedSections.asp
 [5]: http://cpbotha.net/thingies/blagg-20050303.diff
