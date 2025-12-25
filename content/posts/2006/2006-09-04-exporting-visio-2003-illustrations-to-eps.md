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
_If you’re interested in the final, working solution, skip to the end of this post (the part where it says “UPDATE UPDATE UPDATE” :)._

You’ve made your award-winning illustration in Visio 2003, and now you’d like to include it in your award-winning LaTeX proposal. You find [this page][1] with tips, but you’ve also discovered that none of them work for you, or that you don’t have the necessary software, or that they half-work in a very frustrating fashion (this was the case for me with visio -> emf -> openoffice draw -> eps and borked transparencies).

Here is Yet Another Improved Solution (the crucial “windows fonts” part contributed by Jorik, thanks!!):

  * install PDFCreator
  * In Visio 2003, print your illustration to the PDFCreator, but first remember to click on the “Properties” button on the print dialog, then “Advanced”, “PostScript Options”, set “PostScript Output Option” to “Encapsulated PostScript (EPS)”.
  * In the PDFCreator dialog that appears after you’ve clicked on “print”, select “Options” then section “Ghostscript” and UNcheck the “Use Windows fonts” checkbox.
  * Save as EPS (and not PDF).

The generated EPS file should work perfectly in your LaTeX.

**UPDATE UPDATE UPDATE**
  
Read [this][2] for more tips about conversion to EPS for use in LaTeX, then get and install [OLETeX][3]. I just tested this, it works perfectly! Ignore the PDFCreator solution above, OLETeX is definitely the best way to do this.  Just remember that you HAVE to install the postscript printer driver shipped with OLETeX and set it up exactly as explained in the instructions, else it won’t work.

 [1]: http://www.itee.uq.edu.au/~emmerik/visioeps.html
 [2]: http://wiki.lyx.org/Windows/WinGraphics
 [3]: http://oletex.sourceforge.net/
