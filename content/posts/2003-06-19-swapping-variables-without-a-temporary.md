---
title: Swapping variables without a temporary
author: cpbotha
type: post
date: 2003-06-19T18:00:36+00:00
url: /2003/06/19/swapping-variables-without-a-temporary/
categories:
  - howto
tags:
  - python
  - programming

---
This is from the first recipe in my brand-new Python cookbook. It's quite
obvious, but it hasn't really struck me before. Well doh.

In most languages, swapping the values in two variables means using an
intermediate temporary variable, e.g.:
  
``` c++
int a = 1;
int b = 2;
int temp;
temp = a;
a = b;
b = temp;
```

With the tuple packing and unpacking in Python however, we don't need no steenking temporary variables!
  
``` python
a = 1
b = 2
b, a = a, b
``` 

Obviously this principle scales to any number of variables, e.g.:
  
``` python
a, b, c, d = d, c, b, a
```

\*sniff\* That's just so sweet.
