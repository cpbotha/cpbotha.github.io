---
title: Multi-agent frameworks and Python
author: cpbotha
type: post
date: 2005-01-17T21:32:08+00:00
url: /2005/01/17/multi-agent-frameworks-and-python/
categories:
  - Uncategorized

---
The 3 second status update: I had a truly wunnerful December holiday in South Africa, featuring an abundance of sun, sea, crayfish, beer, meat, fish, various tasty molluscs, a very exciting jaunt in a 4-seater Cessna plane (thanks [Dave][1]!), good friends and fun-loving family.

After re-adjusting to Dutch weather and getting back into the work thing for a few days, we spent a weekend in Koeln (or Cologne; that&#8217;s in Germany for the geographically challenged), worked some more and spent this past weekend debauching terribly with a large group of friends in Bradford-on-Avon, a picturesque little town about an hour&#8217;s drive from Bristol (that&#8217;s in the UK, again for the geographically challenged readers).

I&#8217;ll be spending at least the next few weeks (or months?) investigating the possibilities of multi-agent visualisation and image processing systems. It seems like some of the better multi-agent frameworks have been implemented in Java. At the moment, I&#8217;m leaning towards [Jade][2], mostly because [Cougaar][3], otherwise a good system, doesn&#8217;t support any of the [FIPA (The Foundation for Intelligent Physical Agents)][4] standards.

Now I just have to figure what&#8217;s the thinnest possible layer required to inter-operate with Jade agents. Also, if I&#8217;m seriously going to play with this, I have to make it work with Python. No, [Jython][5] is not the answer. Really. The options seem to be getting Jade to build in GCJ and then wrapping with SWIG (a la [PyLucene][6]). Ouch. I think [JPype][7] might be more what I&#8217;m looking for, but I&#8217;ll keep you up to date.

 [1]: http://www.stonethree.com/
 [2]: http://jade.tilab.com/
 [3]: http://www.cougaar.org
 [4]: http://www.fipa.org
 [5]: http://www.jython.org
 [6]: http://pylucene.osafoundation.org/
 [7]: http://jpype.sf.net/
