---
title: A quick Python note
author: cpbotha
type: post
date: 2003-06-19T14:50:49+00:00
url: /2003/06/19/a-quick-python-note/
categories:
  - Uncategorized

---
Have a look at this brief snippet:
  
`<br />
In [2]: a = range(10)<br />
In [3]: 3 in a<br />
Out[3]: 1<br />
In [4]: 3 not in a<br />
Out[4]: 0<br />
In [5]: not (3 in a)<br />
Out[5]: 0<br />
` 

Input/output 4 should strike you as a tad strange if you don&#8217;t know Python _that_ well but are familiar with similar constructs in other languages. At first glance, it almost seems like the sense of an operator can be negated with the `not` operator.

Fortunately, this is simply a case of the whole of `not in` being a single operator in Python. `e not in S` is equivalent to `not (e in S)`.