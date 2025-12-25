---
title: Python new-style objects and __slots__
author: cpbotha
type: post
date: 2003-06-16T17:37:31+00:00
url: /2003/06/16/python-new-style-objects-and-__slots__/
categories:
  - howto
tags:
  - python
  - programming

---
This should be very useful:
  
```
In [5]: class oldObject:
   ...: ....def __init__(self):
   ...: ........self.someVar = 1
   ...:
In [6]: o1 = oldObject()
In [7]: o1.someVar = 2
In [8]: o1.someOtherVar = 3
```

This is of course expected behaviour. Have a look at this though:
  
```
In [9]: class newObject(object):
   ...: ....__slots__ = ['someVar']
   ...: ....def __init__(self):
   ...: ........self.someVar = 1
   ...:
In [10]: o2 = newObject()
In [11]: o2.someVar = 2
In [12]: o2.someOtherVar = 3
AttributeError: 'newObject' object has no attribute 'someOtherVar'
``` 

Neat huh? In short, deriving from the new Python class `object` means you have
a "new-style" object. Amongs other things, this means that you can define a
`__slots__` list which will prevent the use of attributes not in that
list. These objects are available from Python 2.2 onwards.

No, my books haven't arrived yet. :)
