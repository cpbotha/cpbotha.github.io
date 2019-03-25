---
title: Problem solved?
author: cpbotha
type: post
date: 2001-08-07T00:37:00+00:00
url: /2001/08/07/problem-solved/
categories:
  - Uncategorized

---
Weird&#8230; I&#8217;m going to quote from a mail I sent:

In anycase, these have been some of the weirdest hardware moments I&#8217;ve ever had: it seems that an existing 32MB DIMM was right on the edge of giving up at the moment that I installed a new 128MB DIMM in the firewall and converted it to reiserfs.

It was on the edge in such a manner that it survived 12 consecutive passes of complete memtest86 test-sets (and 40 3-parallel process kernel compiles without a sig11)&#8230;. this morning however, the BIOS caught a memory error at bootup (the machine had crashed during the night); a subsequent run of memtest86 caught the error within the first 30 seconds. I&#8217;ve established with some DIMM-swapping that the problem is with the DIMM and not the slot it was in.

So, the DIMM was in the process of dying as it were&#8230; it was being sporadically flakey at a time when many variables were being added to the equation, which made the fault all the more difficult to confirm.