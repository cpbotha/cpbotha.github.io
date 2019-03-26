---
title: Exporting Visio 2003 illustrations to EPS
author: cpbotha
type: post
date: 2006-09-04T16:58:37+00:00
url: /2006/09/04/exporting-visio-2003-illustrations-to-eps/
categories:
  - tech
tags:
  - eps
  - latex
  - visio

---
_If you&#8217;re interested in the final, working solution, skip to the end of this post (the part where it says &#8220;UPDATE UPDATE UPDATE&#8221; :)._

You&#8217;ve made your award-winning illustration in Visio 2003, and now you&#8217;d like to include it in your award-winning LaTeX proposal. You find [this page][1] with tips, but you&#8217;ve also discovered that none of them work for you, or that you don&#8217;t have the necessary software, or that they half-work in a very frustrating fashion (this was the case for me with visio -> emf -> openoffice draw -> eps and borked transparencies).

Here is Yet Another Improved Solution (the crucial &#8220;windows fonts&#8221; part contributed by Jorik, thanks!!):

  * install PDFCreator
  * In Visio 2003, print your illustration to the PDFCreator, but first remember to click on the &#8220;Properties&#8221; button on the print dialog, then &#8220;Advanced&#8221;, &#8220;PostScript Options&#8221;, set &#8220;PostScript Output Option&#8221; to &#8220;Encapsulated PostScript (EPS)&#8221;.
  * In the PDFCreator dialog that appears after you&#8217;ve clicked on &#8220;print&#8221;, select &#8220;Options&#8221; then section &#8220;Ghostscript&#8221; and UNcheck the &#8220;Use Windows fonts&#8221; checkbox.
  * Save as EPS (and not PDF).

The generated EPS file should work perfectly in your LaTeX.

**UPDATE UPDATE UPDATE**
  
Read [this][2] for more tips about conversion to EPS for use in LaTeX, then get and install [OLETeX][3]. I just tested this, it works perfectly! Ignore the PDFCreator solution above, OLETeX is definitely the best way to do this.  Just remember that you HAVE to install the postscript printer driver shipped with OLETeX and set it up exactly as explained in the instructions, else it won&#8217;t work.

 [1]: http://www.itee.uq.edu.au/~emmerik/visioeps.html
 [2]: http://wiki.lyx.org/Windows/WinGraphics
 [3]: http://oletex.sourceforge.net/
