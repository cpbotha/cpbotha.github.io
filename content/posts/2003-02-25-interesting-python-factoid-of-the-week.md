---
title: Interesting Python factoid of the week
author: cpbotha
type: post
date: 2003-02-25T14:35:42+00:00
url: /2003/02/25/interesting-python-factoid-of-the-week/
categories:
  - Uncategorized

---
`<br />
>>> def someFunc(someParam, someDict={}):<br />
...    someDict[someParam] = someParam<br />
...    print someDict<br />
...<br />
>>> someFunc('hello1')<br />
{'hello1': 'hello1'}<br />
>>> someFunc('hello2')<br />
{'hello2': 'hello2', 'hello1': 'hello1'}<br />
>>> someFunc('hello3')<br />
{'hello2': 'hello2', 'hello3': 'hello3', 'hello1': 'hello1'}<br />
>>><br />
` 

The moral of this story is: be careful when using default parameters for dictionaries, lists and such like. One could be forgiven for thinking that the default parameter gets initialised with every invocation, but that is clearly not the case.

To emulate the &#8220;faulty&#8221; behaviour, do something like:
  
`<br />
>>> def someFunc(someParam, someDict=None):<br />
...    if someDict is None:<br />
...       someDict = {}<br />
...    someDict[someParam] = someParam<br />
...    print someDict<br />
...<br />
>>> someFunc('hello1')<br />
{'hello1': 'hello1'}<br />
>>> someFunc('hello2')<br />
{'hello2': 'hello2'}<br />
>>><br />
` 

Remember kids, if you think Python is just a scripting language, you should take the time to have a much closer look. If, after your look, you still haven&#8217;t seen the light, natural selection poses a very serious threat to your continued existence.