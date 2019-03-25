---
title: Converting VCARD to LDIF
author: cpbotha
type: post
date: 2004-02-22T00:01:51+00:00
url: /2004/02/22/converting-vcard-to-ldif/
categories:
  - Uncategorized

---
So, you want to export all your addresses from evolution (which I use at work) and to import those addresses into your Mozilla Mail (or Thunderbird) at home. Once again, the software really bites. Evolution is too damn retarded to export anything else than VCARD (VCF) files. Mozilla Mail can import CSV (comma-delimited) or LDIF files.

Fortunately, there&#8217;s [vcf2ldif][1]. It&#8217;s far from perfect, but it&#8217;s miles better than nothing. Oh, BTW, this will probably segfault on your evolution VCARD file. I bashed its head in with my trusty gdb (a &#8220;debugger&#8221; to the less refined readers) and [this patch][2] is the result.

 [1]: http://www.linux.org.tw/~shchang/vcf2ldif/
 [2]: http://cpbotha.net/thingies/vcf2ldif-FNisNULL-fix.diff