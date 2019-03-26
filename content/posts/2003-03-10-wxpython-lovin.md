---
title: wxPython lovin’
author: cpbotha
type: post
date: 2003-03-10T00:47:00+00:00
url: /2003/03/10/wxpython-lovin/
categories:
  - tech
  - Uncategorized
tags:
  - GTK
  - python
  - wxPython
  - wxWindows

---
In other news, I was able to put time in on Friday and do some
  
[PyColourChooser hacking][1]. Michael Gilfix (the author) has integrated my patches. You know it&#8217;s a good patch when it removes far more code than it adds, yet increases the functionality. :)

I&#8217;m still wondering why wxWindows doesn&#8217;t wrap the [GTK colour wheel][2] though. The wxWindows generic colour selector (used on GTK setups) isn&#8217;t worth the photons it was coded with. PyColourChooser alleviates this deficiency in wxPython to some extent, but that durn colour wheel would have been nice too!

 [1]: https://github.com/svn2github/wxPython/blob/master/Phoenix/trunk/wx/lib/colourchooser/pypalette.py#L145
 [2]: http://wxpython-users.1045709.n5.nabble.com/gtk-color-selection-td2289462.html
