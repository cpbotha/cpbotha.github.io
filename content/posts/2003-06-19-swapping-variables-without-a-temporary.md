---
title: Swapping variables without a temporary
author: cpbotha
type: post
date: 2003-06-19T18:00:36+00:00
url: /2003/06/19/swapping-variables-without-a-temporary/
categories:
  - Uncategorized

---
This is from the first recipe in my brand-new Python cookbook. It&#8217;s quite obvious, but it hasn&#8217;t really struck me before. Well doh.

In most languages, swapping the values in two variables means using an intermediate temporary variable, e.g.:
  
`<br />
int a = 1;<br />
int b = 2;<br />
int temp;<br />
temp = a;<br />
a = b;<br />
b = temp;<br />
` 

With the tuple packing and unpacking in Python however, we don&#8217;t need no steenking temporary variables!
  
`<br />
a = 1<br />
b = 2<br />
b, a = a, b<br />
` 

Obviously this principle scales to any number of variables, e.g.:
  
`<br />
a, b, c, d = d, c, b, a<br />
` 

\*sniff\* That&#8217;s just so sweet.