---
title: Convert Word tables to EPS for inclusion in LaTeX
author: cpbotha
type: post
date: 2010-05-23T13:20:43+00:00
url: /2010/05/23/convert-word-tables-to-eps-for-inclusion-in-latex/
categories:
  - howto
tags:
  - conversion
  - eps
  - latex
  - word

---
_You might want to **skip this post** if any of the following is true:_

  * _You don’t know what [LaTeX][1] is._
  * _You don’t care about typesetting theses._
  * _You’re just generally low on Nerd midi-chlorians._

Recently, we ([Mr Cricket][2] and I) helped a good friend (argh, he might already have an acronym assigned,  I should make a glossary for this blog…) typeset his PhD thesis in LaTeX. Sounds straight-forward, were it not for the fact that most of the material was in MS Word to start off with. :)

It mostly comes down to a simple but laborious process of of taking one LaTeX PhD thesis framework (mine) and copy-pasting loads of text from Word into LaTeX, taking care to sprinkle with sufficient amounts of markup.  There are two slightly more complicated issues: The first is correctly converting figures, taking care to save bitmaps as PNGs (these will be converted to EPS via JPG later) and vector graphics as EPS.  I’ve [written before][3] about how to convert Visio to EPS for inclusion to LaTeX.

This quick post is concerned with the second problem: What is the best way to go about converting tables from Word to LaTeX?  Seeing that this was in actual fact the second PhD thesis I had converted from Word to LaTeX, including numerous tables, I have by now burnt my fingers on 68 different occasions, each time in an excruciating new and interesting way!  I’d like to spare you that pain, so here is, without (too much) further ado, the **Best Way to Convert Word Tables to EPS for Inclusion into LaTeX!**

No, we we are definitely NOT going to recode all Word tables in LaTeX markup, because that would be anti-social.  Instead, we are going to print all tables to EPS, then autocrop them and then simply include them into LaTeX via the includegraphics call inside of a normal table float.  Ok?

Here we go:

  1. Install [PDFCreator][4].
  2. Select the table you want to convert in Word, then select “Print Selection” and select PDFCreator as the destination printer.
  3. Select the “Properties” button on the print dialog, then “Advanced”, “PostScript Options”, set “PostScript Output Option” to “Encapsulated PostScript (EPS)”
  4. Now print to file.
  5. Copy the output file to a linux machine (or use a live CD with ps2eps) and do the following: <pre class="brush: bash; title: ; notranslate" title="">ps2eps -B -C -l &lt; printed_output.prn &gt; result_cropped.eps
</pre>

  6. You can now include result_cropped.eps in your LaTeX document with the following code: <pre class="brush: plain; title: ; notranslate" title="">\begin{table}
\begin{center}
\caption{Your table's caption}
\includegraphics{result_cropped.eps}
\label{tab:your_label}
\end{center}
\end{table}
</pre>

If you took care to match the font you used in Word with your LaTeX font, people will probably not even realise that your tables are not LaTeX-native. That’s a clear-cut case of maximum Nerd street-cred with the minimum of actual fuss…

 [1]: http://en.wikipedia.org/wiki/LaTeX "Wikipedia page on LaTeX"
 [2]: http://www.clinicalgraphics.com/ "Clinical Graphics, BUY THEIR SOFTWARE!"
 [3]: http://cpbotha.net/2006/09/04/exporting-visio-2003-illustrations-to-eps/ "Previous post on converting Visio diagrams to EPS for inclusion in LaTeX."
 [4]: http://sourceforge.net/projects/pdfcreator/ "PDFCreator website"
