---
title: Lush, OCaml and more, part deux
author: cpbotha
type: post
date: 2005-03-24T15:06:26+00:00
url: /2005/03/24/lush-ocaml-and-more-part-deux/
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
In a [previous blog entry][1], I did some extremely informal benchmarking with Lush, OCaml, Python and C. I&#8217;ve now added two new Python tests: one with [Psyco][2], a JIT-like solution that takes almost no effort to add to existing code, and one with [Pyrex][3], where one can code extension modules in a language that looks just like Python but has types. These modules are then translated to C and compiled into Python usable extension libaries.

With Psyco, one only has to add the lines &#8220;import psyco; psyco.full()&#8221; to one&#8217;s Python code. The performance gains can be huge, but in general are quite modest. It takes far less effort than Pyrex though.

The updated benchmarks table is shown below:

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
      Python 2.3.5 with Psyco
    </td>
    
    <td>
      0.148
    </td>
  </tr>
  
  <tr>
    <td>
      Python 2.3.5 with Pyrex
    </td>
    
    <td>
      0.064
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

The new implementations are available at the [usual place][4].

 [1]: /2004/11/14/lush-ocaml-and-more/
 [2]: http://psyco.sf.net/
 [3]: http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
 [4]: /thingies/lushCompare
