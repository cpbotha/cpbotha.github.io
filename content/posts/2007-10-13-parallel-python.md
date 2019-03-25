---
title: Parallel Python
author: cpbotha
type: post
date: 2007-10-13T12:27:34+00:00
url: /2007/10/13/parallel-python/
categories:
  - tech

---
Somehow I missed this when searching for something like it the previous time, but [Parallel Python][1] (now found via [Bruce Eckel&#8217;s blog][2]) is exactly what I&#8217;ve been looking for.  A simple process pool that can run on multiple cores or on a cluster of machines!

[DeVIDE][3] has recently acquired the ability to run in black-box (gui-less) mode, so that networks can also be executed via some other coordination framework, such as Nimrod (see [our paper][4] on this, mail me if you want the fulltext).  However, seeing that I&#8217;ve neatly abstracted out the interface part of DeVIDE (you can choose between wxPython, simple xml-rpc, command-line with Python driver script, even PyRo), integrating ParallelPython would be a cinch.

I can already see it before me: millions of computers running DeVIDE, all crashing in parallel!

 [1]: http://www.parallelpython.com/ "Parallel Python website"
 [2]: http://www.artima.com/weblogs/index.jsp?blogger=beckel "Bruce Eckel's blog"
 [3]: http://visualisation.tudelft.nl/Projects/DeVIDE "DeVIDE website"
 [4]: http://csdl2.computer.org/persagen/DLAbsToc.jsp?resourcePath=/dl/proceedings/&toc=comp/proceedings/cbms/2007/2905/00/2905toc.xml&DOI=10.1109/CBMS.2007.87 "Link to DeVIDE / blackbox paper at computer.org"