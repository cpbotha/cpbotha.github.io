---
title: Porting woes
author: cpbotha
type: post
date: 2002-12-22T23:31:00+00:00
url: /2002/12/22/porting-woes/
categories:
  - Uncategorized

---
[This][1] is brilliant. Microsoft Visual C++ violates the ISO C++ standard (at least as far as my 1998 document is concerned) with regards to this very fundamental and simple scoping behaviour, but they do not admit that this is a violation as such. Instead they claim that one can work around this &#8220;problem&#8221; by using a special compiler switch that disables &#8220;language extensions&#8221;. However, depending on your configuration, making use of this switch will break compilation of certain Visual C++ headers (ntheader.h IIRC). You have to love this.

 [1]: http://support.microsoft.com/default.aspx?scid=KB;en-us;q167748