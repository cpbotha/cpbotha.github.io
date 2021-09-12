---
title: Extremely narrow text boxes in Movable Type
author: cpbotha
type: post
date: 2003-02-07T16:59:36+00:00
url: /2003/02/07/extremely-narrow-text-boxes-in-movable-type/
categories:
  - Uncategorized

---
It could be because I set something up incorrectly, but people have been seeing unusably narrow text entry boxes (TEXTAREA) in Movable Type 2.51 with Mozilla (1.0 and 1.2.1), Opera 7 and IE 6.0. So I ran:
  
``` shell
mkdir new && for i in *.tmpl; do cat $i | sed -e \
's/<tmpl_if name="AGENT_MOZILLA"> cols=\"\"&lt;\/TMPL_IF&gt;/\
cols=\"80\"/g' &gt; new/$i; done &amp;&amp; cp new/* ./
```
  
in the tmpl directory and it all seems to be usable now. This is probably not the Right Way(tm) but it makes the entry boxes usable.

By the way, if you want to add code snippets to your Movable Type postings, just use <code> and </code> tags.

