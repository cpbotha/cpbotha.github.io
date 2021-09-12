---
title: Lush, OCaml and more
author: cpbotha
type: post
date: 2004-11-14T15:32:17+00:00
url: /2004/11/14/lush-ocaml-and-more/
categories:
  - tech
  - Uncategorized
tags:
  - harmonic
  - lush
  - ocaml
  - octave
  - psyco
  - python

---
I took a long hard look at the [OCaml][1] functional (well, mostly) language this weekend. One of the many interesting aspects of OCaml, is that, in addition to offering an interpreted environment, it comes with a REALLY good compiler. So, you can sit there prototyping your latest numerical trick and when you’re happy, you can compile the code to a blazingly fast native binary.

So, whilst reading up on all this, I remembered a question from the [Lush][2] (a lisp-like scientific languages that can also be compiled) [FAQ][3]: “How does Lush compare to Matlab/Octave for speed?”. So the author then shows that Lush is like 50 billion times faster than Octave. (Go look.)

I implemented his little benchmark in Python, C, Octave and OCaml and tested the codes on a P4 2.4GHz running Ubuntu Linux. These were the performance figures for harmonic(1000000):

<table border="1">
<tr>
<th>
      Language
    </th>
<th>
      Time (seconds)
    </th>
</tr>
<tr>
<td>
      Octave 2.1.57
    </td>
<td>
      7.894
    </td>
</tr>
<tr>
<td>
      Python 2.3.4
    </td>
<td>
      0.459
    </td>
</tr>
<tr>
<td>
      OCaml 3.08 interpreted
    </td>
<td>
      0.229
    </td>
</tr>
<tr>
<td>
      OCaml 3.08 compiled
    </td>
<td>
      0.021
    </td>
</tr>
<tr>
<td>
      gcc 3.3.4
    </td>
<td>
      0.017
    </td>
</tr>
</table>

For each benchmark, I obviously called the harmonic() in a loop with sufficient iterations to yield accurate timings. For the compiled tests, 300 iterations did the trick. For Octave, 3 was more than enough. You can find my implementations by clicking [here][4].

This was really just for fun, in other words: DON’T TAKE IT TOO SERIOUSLY. Also, the OCaml snippet I wrote is mostly imperative. However, the results reflect what is also shown by [The Great Computer Language Shootout][5]: OCaml is a good contender when one needs to write very fast code in a more advanced language than C.

 [1]: http://www.ocaml.org/
 [2]: a href=
 [3]: http://lush.sourceforge.net/faq.html
 [4]: http://visualisation.tudelft.nl/~cpbotha/thingies/lushCompare/
 [5]: http://shootout.alioth.debian.org/
