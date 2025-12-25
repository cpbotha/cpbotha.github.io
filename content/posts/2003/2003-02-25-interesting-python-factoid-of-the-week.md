---
title: Interesting Python factoid of the week
author: cpbotha
type: post
date: 2003-02-25T14:35:42+00:00
url: /2003/02/25/interesting-python-factoid-of-the-week/
categories:
  - Uncategorized

---
```
>>> def someFunc(someParam, someDict={}):
...    someDict[someParam] = someParam
...    print someDict
...
>>> someFunc('hello1')
{'hello1': 'hello1'}
>>> someFunc('hello2')
{'hello2': 'hello2', 'hello1': 'hello1'}
>>> someFunc('hello3')
{'hello2': 'hello2', 'hello3': 'hello3', 'hello1': 'hello1'}
>>>
```

The moral of this story is: be careful when using default parameters for dictionaries, lists and such like. One could be forgiven for thinking that the default parameter gets initialised with every invocation, but that is clearly not the case.

To emulate the “faulty” behaviour, do something like:
  
```
>>> def someFunc(someParam, someDict=None):
...    if someDict is None:
...       someDict = {}
...    someDict[someParam] = someParam
...    print someDict
...
>>> someFunc('hello1')
{'hello1': 'hello1'}
>>> someFunc('hello2')
{'hello2': 'hello2'}
>>>
```

Remember kids, if you think Python is just a scripting language, you should take the time to have a much closer look. If, after your look, you still haven’t seen the light, natural selection poses a very serious threat to your continued existence.
