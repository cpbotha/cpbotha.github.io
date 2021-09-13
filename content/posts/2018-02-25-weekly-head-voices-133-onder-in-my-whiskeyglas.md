---
title: 'Weekly Head Voices #133: Onder in my Whiskeyglas.'
author: cpbotha
type: post
date: 2018-02-25T21:15:42+00:00
url: /2018/02/25/weekly-head-voices-133-onder-in-my-whiskeyglas/
categories:
  - weekly head voices
tags:
  - backyard philosophy
  - functional programming
  - practice
  - python
  - restructuredtext
  - rust
  - rustlang
  - sphinx
  - windows
  - wxPython

---
{{< figure src="/wp-content/uploads/2018/02/IMG_3288.jpg" link="/wp-content/uploads/2018/02/IMG_3288.jpg" caption="The legendary Koos Kombuis (aka André Letoit) performing with Schalk Joubert on bass and Vernon Swart on percussion in the Helderberg Nature reserve, eponymous mountain visible through the trees on the right. This was a surprisingly amazing end to the week.">}} 

What a week.

It was beautiful to see the whole team step up to the plate and _engineer_ at about 110% throughput (software gets complicated quickly, and there's always one more thing you need to get done before the deliverable is ready), all the while remaining calm and, most importantly, kind.

## Pro-tip Special

I was of course the lucky winner of the manual-writing sub-project. I love writing code, but there's also something quite satisfying about writing documentation for a technical product. Anyways, there are five tiny but hopefully useful lessons I extracted from this exercise which I would like to present here:

  1. [I've lamented the sorry state of the Windows console before][1] (in 2011 to be exact). In a surprise twist, the Windows console still sucks almost 7 years later. At least it's reliable. Anyways, [cmder is a great console replacement][2] which makes some of the stupid go away, somewhat.
  2. The Windows 10 built-in screenshot facility … wait for it… sucks. When you're writing documentation you need a tool that fits into your workflow. Keyboard shortcut – window or region – image ends up in a directory of your choice. [Greenshot is an open source screenshotting tool][3] that does this with aplomb.
  3. You need to show a CHM (Windows Help) file to the user of your wxPython application when they hit F1. How hard could it be? Well, you could spend a number of hours trying to come up with a wx-y cross-platform solution, or you could use that time for something else worth your while and just use the [Python win32 package to call into the official Windows help API][4]. (cross-platform does work, it's just really ugly)
  4. [Sphinx][5] is a much better tool to write technical manuals than is Markdown and related tools. I briefly considered Markdown because I always have to look up reStructuredText syntax, but fortunately ran into enough other places [warning against using Markdown for documentation][6]. For the record, I prefer orgmode over all of these puny formats in most other cases, but the documentation story of Sphinx with reStructuredText is admittedly much better.
  5. Start writing the manual as early as possible. It was amazing to see how this helped me to see the software we are designing at a more integrated (user) level. This knowledge was useful in driving more valuable improvements. If you can't explain the flow of some procedure in a manual, that's a good sign the procedure might need some refinement.

## Humble Book Bundle and Rust

I bought the [Humble Bundle of (O'Reilly) Functional Programming Books][7] for a super affordable $15. I was primarily interested in the [Programming Rust book by Blandy and Orendorff][8], but the other titles on Scala, Clojure, Erlang, Elixir, Haskell, Javascript and general functional programming are welcome additions to my library. Speaking of which, I emailed O'Reilly to ask if the books in the bundle could be added to my member library, which they promptly did!

I have avoided Rust up to now due to natural hype suppression circuitry, and because I grew up with C++, but its zero-overhead memory safety and trustworthy concurrency story makes it hard to ignore any longer. Even although [Andrei Alexandrescu once called Rust the language that skips leg day][9], it's certainly interesting seeing the constructs the language designers have come up to build a really fast compiled language with the lowest number of foot-guns per line of code.

Anyways, when this blog gets published, you should still have about 22 hours to make use of the [Humble Bundle deal][7] if you too see something that you like.

## Life is continuous practice

I wanted to conclude with something that I've been thinking about recently. It has to do with explicitly treating one's life as _continuous practice_. As I've mentioned before on this blog and people much smarter than me have been pointing out since forever, [goals are no good][10] and (lasting) [happiness is probably not attainable][11].

Discarding as many as possible of these sorts of fetters is liberating (you Buddhist), but can seem to leave holes in one's  life narrative. However, treating your life as a super long practice session is an interesting perspective.

There is also no end point, and no real life goal.

The only point of the whole exercise (yes, I see what I did there) is to try to improve continuously. Every day, we try to become a little better at our jobs, or at running, or at being a good human, or a partner, or a parent.

Practice means that you have good days and bad days. It means that you sometimes look back and think that you were a better person then than you are now. Practice means that when you pick one activity, another will temporarily languish until you can make time for it again.

All of this is ok, because tomorrow you have a whole new day to try again.

 [1]: https://vxlabs.com/2011/08/28/a-windows-console-that-does-not-suck/
 [2]: http://cmder.net/
 [3]: http://getgreenshot.org/
 [4]: http://docs.activestate.com/activepython/3.3/pywin32/win32help__HtmlHelp_meth.html
 [5]: http://www.sphinx-doc.org/en/master/
 [6]: http://ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/
 [7]: https://www.humblebundle.com/books/functional-programming-books
 [8]: http://shop.oreilly.com/product/0636920040385.do
 [9]: https://www.quora.com/Which-language-has-the-brightest-future-in-replacement-of-C-between-D-Go-and-Rust-And-Why/answer/Andrei-Alexandrescu
 [10]: /2012/01/28/slow-philosophy-weekly-head-voices-64/
 [11]: /Weekly-Head-Voices-125/#Happy-Not-Happy
