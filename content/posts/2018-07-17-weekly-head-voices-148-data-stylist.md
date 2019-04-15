---
title: 'Weekly Head Voices #148: Data stylist.'
author: cpbotha
type: post
date: 2018-07-17T07:22:30+00:00
url: /2018/07/17/weekly-head-voices-148-data-stylist/
categories:
  - weekly head voices
tags:
  - barefoot
  - d3.js
  - fsharp
  - functional programming
  - golang
  - jupyter
  - luna
  - programming
  - pycharm
  - python
  - running
  - rustlang
  - scipy
  - vega
  - xero

---
<figure id="attachment_3217" aria-describedby="caption-attachment-3217" style="width: 840px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail.jpg" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="3217" data-permalink="https://cpbotha.net/2018/07/17/weekly-head-voices-148-data-stylist/drakenstein_trail/" data-orig-file="https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail.jpg" data-orig-size="7981,1882" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;1.8&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;iPhone 7&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1531562172&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;3.99&quot;,&quot;iso&quot;:&quot;20&quot;,&quot;shutter_speed&quot;:&quot;0.00064683053040103&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="drakenstein_trail" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail-300x71.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail-1024x241.jpg" class="wp-image-3217 size-large" src="https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail-1024x241.jpg" alt="" width="840" height="198" srcset="https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail-1024x241.jpg 1024w, https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail-300x71.jpg 300w, https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail-768x181.jpg 768w, https://cpbotha.net/wp-content/uploads/2018/07/drakenstein_trail-1200x283.jpg 1200w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" /></a><figcaption id="caption-attachment-3217" class="wp-caption-text">Ridiculously fun trail in Paarl somewhere. (Photo taken by Trail Friend #1. Trail Friend #2 cropped from picture, because no permission to appear on the internets!)</figcaption></figure> 

This post covers the week from Monday July 9 to Sunday July 15.

The business part of my week was unfairly dominated by far too much after-work obsessing over programming languages, with which I seem to have an unhealthy (or perhaps not) obsession.

I will externalise some of these thoughts further down in this post.

I&#8217;m starting with a weekend / running update, which should be reasonably safe for non-nerds to read. However, after that, the nerd dial will go up to 11 with stuff about tools and programming languages right up to the end of the post.

I would have wanted to use the adjective &#8220;face-melting&#8221;, but I&#8217;m not sure if any intensity of nerdery could ever reach that level.

We can dream.

# Weekend running update

Most fortunately the weekend had other plans and supplied us with at least 2.5 parties, the first of which even culminated in a _ridiculously_ fun trail run in the mountains on the winter morning after.

The winter morning sun was just perfect, the company was great, and I had forgotten all forms of performance tracking devices at home.

Readers with bionic eyes might notice the Lunas on my feet.

I have now ran just over 260km in them, but, in a surprise twist to the regular readers of this blog, my biological equipment has still not yet completely adjusted to the new style of locomotion.

The latest victim seems to be one of Tom, Dick and Harry, the tendons running under the medial [malleolus][1] of my left foot, also known as that big knob on your inside ankle. Tom (the primary suspect in this case according to Trail Friend #1 who is knowledgable with regard to these matters, being a running foot surgeon and all), Dick and Harry [are also known as the \*T\*ibialis posterior, flexor \*D\*igitorum longus and the flexor \*H\*allucis longus][2].

They currently have to work extra hard to stabilise my feet while running, because, you know, no shoes.

Because doing this thing was not hard enough already, and because the Lunas are perhaps still a bit too cushiony, and because my friend the Very Flat Cat forgot that I&#8217;m very suggestible after 11:00 in the morning when my prefrontal cortex takes the rest of the day off, I am now also the very shy owner of a pair of [Xero Genesis running sandals][3]:

![Image result for xero genesis][4]

The soles are only 5mm thick, and quite hard, being [rated for a few thousand miles][5] and all. The upshot of this is that one&#8217;s feet have to work even harder than in the Lunas.

My first run in these was amazing: I could feel my feet reacting to every little pebble, and my running style having to adapt even more to the terrain.

However, there was a price to pay for all of that additional terrain feel (and the fact that I took a much longer maiden run than I should have): The next day, the tendons in my feet felt even more (ab)used than usual.

WITH GREAT POWER COMES GREAT RESPONSIBILITY, it seems.

Due to these shoes being so powerful, I have had to resign to introducing Xero running far more gradually than I had initially thought.

# Vacation-based-thinking-driven tool sharpening aka The WVV 2018 Data Science Toolbox(tm).

During the [previously blogged-about][6] Mpumalanga vacation, the lack of alarms, devices, and other work accoutrements, resulted in there being ample time for staring-into-space-grade thinking sessions.

During one of these thinking sessions, I realised that I had somehow neglected my data science toolbox for a while.

At some point a few years back, I was so into ipython notebooks (what has now become jupyter) that I used them as my main work lab notes modality.

However, in the meantime I had fallen slightly out of love with the computational notebook style of data programming, because I had begun to develop doubts about their role in the analysis pipeline.

**interlude 1:** _jupyter notebooks are nice for initial data exploration, and they&#8217;re especially useful for remote computation with embedded graphics. However, that initial momentum of discovery risks devolving into an unwieldy monolith of code snippets, data transformations and experiments. There&#8217;s a fine line to be walked between flexible experimentation on the one hand, and version-controlled, time-stamped, permutational and scientific rigour on the other._

**interlude 2:** _I have to apologise for using the term &#8220;data science&#8221; in a non-comedic context. In spite of the inherent humour, it has turned into a usable blanket term for computational data understanding._

Due to my growing doubts in the order of Jupyter, and due to being occupied with less traditionally data sciencey work projects, I had unfortunately let my data science toolbox gather perhaps a bit too much dust.

Slightly more worrying than falling out of love with the Jupyter Notebooks (I still like them, I&#8217;m just not that madly in love anymore), was the more specific issue that I&#8217;d even let the datavis parts get a bit dusty.

Anyways.

Although I should probably write a more complete post about this, here is the list of ingredients of the official _**2018 WHV Data Science Toolbox(tm)**_:

## Programming language and library ecosystem: Python.

This language, in spite of its shortcomings, _dominates_ the data science / machine learning world thanks to its STELLAR ecosystem.

numpy, pandas, scipy, scikit-*, tensorflow, pytorch, keras, cython&#8230; this snowball has turned into a pretty sizeable planet.

For this reason, it would be hard to justify any other choice for data science.

However, since I&#8217;ve been seeing more of Lisp and the rest of the ever-expanding programming language landscape, I can see (Python&#8217;s shortcomings as a programming language) clearly now.

In terms of interactive programming, Python beats the majority of practical programming languages, with Common Lisp being one notable exception.

However, it&#8217;s not functional enough, which engenders unnecessarily imperative, side-effecting code.  More specifically, it&#8217;s not expression-oriented.

More about this slightly further down. Maybe.

## Datavis: Anything, as long as it&#8217;s Vega or Vega-Lite.

I spent a few years of my life wrangling [d3.js][7], down to INNARD-LEVEL.

Mike Bostock&#8217;s idea of [data-element-joins][8] is genius, and internalising it was intellectually satisfying.

I thought that these d3 skillz would serve me well for decades (that&#8217;s WEEKS in javascript-time), but it turns out that there&#8217;s a new, even smarter kid in town.

(if it&#8217;s any consolation, the new kid can be considered the grand-child of d3.js.)

[vega and vega-lite][9] are so-called visualization grammars, or visualization DSLs (domain specific languages).

The upshot is that one codes up a chart, or a whole set of linked charts and their interactive behaviour, using a language that was designed for this purpose.

This chart code can be easily shared, or converted into interactive visual representations that can be embedded in applications, online or in print quality documents.

Genius!

With [Altair][10], you can even send your pandas dataframes to vega and vega-lite charts all from the comfort of your slightly defective Python armchair.

## Development Environment: PyCharm.

You knew it was not going to be Jupyter Notebooks, but you probably expected it to be [Emacs][11].

Well it&#8217;s not. Surprise!

The remote interpreter support in PyCharm enables me to connect to a Python virtual environment anywhere on the planet, which I often do.

The JetBrains wizards have optimised the remote communication of code intelligence, so completion, documentation and general code understanding is almost indistinguishable from that on a completely local project.

Being able to step through a [_remote_ PyTorch neural network training iteration with the PyCharm debugger][12] or any other remote Python algorithmics is insightful.

Two notable drawbacks are visualization and long-running jobs.

For the long-running jobs I do tend to use Jupyter Notebooks or when at all possible [mosh][13], which is amazing. However, because the primary modality is not the notebook, my code is versioned and organised into separate libraries which I can call into from notebook or mosh.

For visualization, it&#8217;s either connecting to the altair chart server via SSH pipe, dumping the chart to the unison-synced project, and/or a Jupyter Notebook.

## The rest.

Of course you use Postgres on an SSD for your data, and of course you know enough SQL to make short work of most of the heavy-weight transformations often required at the start your data crunching pipeline.

For all of my lab notes, reports, books, papers and blog posts, I use [Emacs Org mode][14].

LaTeX math with live preview, live code snippets, SVG graphics, bibtex references, export to anything. This is one of the best ways to document your science.

# Programming language addiction update.

I spend far too much obsessing over programming languages, old and new.

For the past two weeks, I wasted even more precious time than usual reading up about programming languages.

Because I would really like to spend more of my time on other, perhaps more valuable activities, I&#8217;ve been trying to better define what it is I&#8217;m actually looking for.

Of course there is no single best programming language, but a whole set of good languages that map in intricate ways to different problem domains.

In spite of this, I have been pining for a language with, in order of importance:

  1. A Functional Programming DNA, with which I&#8217;m referring to a) [expression-orientedness][15], b) a preference for [pure functions][16], and at a higher level, c) the modelling of reality as more or less explicit dataflows.
  2. Interactive programming, with Common Lisp being the textbook example of this.
  3. Great tooling and IDEs, meaning first-class support by something from JetBrains, Microsoft or Emacs.
  4. Great concurrency and parallelism stories.
  5. A great library ecosystem.
  6. Modest memory use.

Having just explicitly written this down for the first time (!! &#8211; it was consuming so much glucose just being kept amorphously swirling around in my brain) I can now mentally map some of my most recent language dalliances to these points.

## go

This language is far too simple for my taste, but probably really great for teams.

I did recently take a more serious look when [setting up a telegram bot using tbot][17] and being amazed at how simple it was building web services like these using goroutines and channels.

Go satisfies points 3 to 6 from the list above. Makes sense that I decided to file this experiment away under &#8220;check when you need to put a webservice together REALLY QUICKLY&#8221;.

## rust

When I saw up that rust, surprisingly, is an expression-oriented language, I flew through the O&#8217;Reilly Programming Rust book I had bought previously as part of a bundle.

Evaluating rust by the list above, we award it a fractional 1 because expression-oriented, 3 due to jetbrains plugin amongst others, 4(ish) &#8211; great memory safety, but compared to clojure, concurrency and parallelism stories still have much room to grow, a solid 5 thanks to cargo and a very strong 6.

I filed this one away under &#8220;re-evaluate whenever you reach for your trusty C++&#8221;. (also, [actix-web][18] looks amazing for super high performance microservices.)

## f\#

You didn&#8217;t see this one coming, did you?

Very strong 1 to 5 and a solid 6.

WAT?!

I&#8217;m currently working my way through [Domain Modeling Made Functional][19] by Scott Wlaschin, who is also the author of the brilliant [f# for fun and profit][20] website.

In addition to f# hitting all 6 of my 2018 PL-requirements above, I&#8217;m slowly starting to see the advantages of having a real type system under the hood.

f# is a member of the [ML-family][21] of functional languages, which have their origin in Lisp (some very naughty person removed all of the lovely parentheses I&#8217;m afraid&#8230;).

I hope that at some point I&#8217;ll have the opportunity to use f# in anger, at which point I&#8217;ll be able to report more concretely as to its suitability.

# The End

Let me know in the comments what you think about any of this, or anything else.

I hope to meet you again in a few days, here or elsewhere.

 [1]: https://en.wikipedia.org/wiki/Malleolus
 [2]: https://radiopaedia.org/articles/posterior-ankle-tendons-mnemonic
 [3]: https://xeroshoes.com/shop/genesis/genesis-men/
 [4]: https://xeroshoes.com/wp-content/uploads/2018/03/Genesis_Limeade-3-4-770x500.jpg
 [5]: https://xeroshoes.com/warranty/
 [6]: /2018/07/10/weekly-head-voices-147-the-yearly-post-mpumalanga-post/
 [7]: https://d3js.org/
 [8]: https://bost.ocks.org/mike/join/
 [9]: https://vega.github.io/
 [10]: https://altair-viz.github.io/
 [11]: https://vxlabs.com/tag/emacs/
 [12]: https://vxlabs.com/2017/12/08/variational-autoencoder-in-pytorch-commented-and-annotated/
 [13]: https://mosh.org/
 [14]: https://vxlabs.com/tag/orgmode/
 [15]: https://en.wikipedia.org/wiki/Expression-oriented_programming_language
 [16]: https://en.wikipedia.org/wiki/Pure_function
 [17]: https://tutorials.botsfloor.com/develop-your-own-telegram-bot-with-golang-and-tbot-de726883b83c
 [18]: https://github.com/actix/actix-web
 [19]: https://pragprog.com/book/swdddf/domain-modeling-made-functional
 [20]: https://fsharpforfunandprofit.com/
 [21]: https://en.wikipedia.org/wiki/ML_(programming_language)
