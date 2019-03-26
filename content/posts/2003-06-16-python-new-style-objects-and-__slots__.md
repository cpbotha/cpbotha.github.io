---
title: Python new-style objects and __slots__
author: cpbotha
type: post
date: 2003-06-16T17:37:31+00:00
url: /2003/06/16/python-new-style-objects-and-__slots__/
categories:
  - Uncategorized

---
This should be very useful:
  
`<br />
In [5]: class oldObject:<br />
   ...: ....def __init__(self):<br />
   ...: ........self.someVar = 1<br />
   ...:<br />
In [6]: o1 = oldObject()<br />
In [7]: o1.someVar = 2<br />
In [8]: o1.someOtherVar = 3<br />
` 

This is of course expected behaviour. Have a look at this though:
  
`<br />
In [9]: class newObject(object):<br />
   ...: ....__slots__ = ['someVar']<br />
   ...: ....def __init__(self):<br />
   ...: ........self.someVar = 1<br />
   ...:<br />
In [10]: o2 = newObject()<br />
In [11]: o2.someVar = 2<br />
In [12]: o2.someOtherVar = 3<br />
AttributeError: 'newObject' object has no attribute 'someOtherVar'<br />
` 

Neat huh? In short, deriving from the new Python class &#8216;object&#8217; means you have a &#8220;new-style&#8221; object. Amongs other things, this means that you can define a __slots__ list which will prevent the use of attributes not in that list. These objects are available from Python 2.2 onwards.

No, my books haven&#8217;t arrived yet. :)
