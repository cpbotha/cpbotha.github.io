---
title: Python new-style object method resolution order
author: cpbotha
type: post
date: 2004-02-28T21:10:41+00:00
url: /2004/02/28/python-new-style-object-method-resolution-order/
categories:
  - Uncategorized

---
Caveat emptor! Due to the diamond-like inheritance structures frequently seen with new-style Python objects (i.e. all objects are derived from the &#8220;object&#8221; class), the Python method resolution order (MRO) has been slightly adapted.

It used to be left-to-right, depth first. With old-style objects, this almost never caused problems. With new-style, because of the common &#8220;object&#8221; ancestor, this could cause redundant occurrences (obviously due to the diamond structure). Typically Python, this has been solved in a simple yet effective manner.

When trying to determine which method will be invoked when working with multiply-inherited (or mixed-in) objects, use the left-to-right depth first rule. However, if you see any repeated occurrences, delete all but the last. This is the new Python MRO.

Oh bugger, just read [this][1].

 [1]: http://www.python.org/2.2/descrintro.html
