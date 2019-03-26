---
title: Disabled trackback script
author: cpbotha
type: post
date: 2006-03-14T10:28:07+00:00
url: /2006/03/14/disabled-trackback-script/
categories:
  - Uncategorized

---
In just 14 days, my Movable Type trackback script, mt-tb.cgi, has generated 500MB of traffic. Thank you, idiot trackback spammers!

Since we don&#8217;t really use this feature (I think), I&#8217;ve disabled this script and added the following rewrite rule to my htaccess:
  
`<br />
RewriteRule ^weblogs/mt-tb.cgi - [F]<br />
` 

This way the spam scripts get a 403 without being handled by the wiki.
