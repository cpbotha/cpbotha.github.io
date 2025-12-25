---
title: Unstable firewall
author: cpbotha
type: post
date: 2001-08-02T05:09:00+00:00
url: /2001/08/02/unstable-firewall/
categories:
  - Uncategorized

---
Well children, my firewall had gone weirdly unstable after I’d added 128MB of new PC133 ram. It’s a Celery 300A (@450 of course) and it was oopsing miserably after years of faithful service. After memtesting it seemed that suddenly there were errors in one of the _existing_ dimms. Hmmm, it turs out that CAS wait state was set on auto in the bios. I’m theorising that the BIOS somehow based its CAS on the new RAM and that the old RAM couldn’t quite accommodate that. So, I set the CAS ws to 3 and 17 hours of memtesting (12 passes) reported 0 errors. The lesson we learn: know your CAS and know your memtest.

memtest86 is a brilliant tool: http://www.memtest86.com/
