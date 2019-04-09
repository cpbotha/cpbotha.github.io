---
title: "Weekly Head Voices #168: Postcards from the edge."
# we specify slug also, because hugo keeps the # in there, breaking routing
slug: "weekly-head-voices-168-postcards-from-the-edge"
author: cpbotha
# REMEMBER TO CHANGE BEFORE PUBLISHING!
date: 2019-04-08T22:43:00+02:00
tags:
  - focus
  - isso
  - glymphatic system
  - postcard cafe
  - jonkershoek
  - stellenbosch
  - mitch hedberg
  - stark condé
  - wine
categories:
  - weekly head voices
type: "post"
---

<figure>
<a href="postcard_cafe_view.jpg">
{{< img src="postcard_cafe_view.jpg" alt="photo taken at postcard cafe" >}}
</a>
<figcaption> 
Sometimes it feels like the place is falling apart, and sometimes
you find yourself in a heavenly corner like this. Postcard Café, Jonkershoek,
Stellenbosch.
</figcaption>
</figure>

> My friend showed me a photo and said "Here's a picture of me when I was
> younger". Every picture is of you when you were younger.
> -- Mitch Hedberg (RIP)

In this edition of the WHV, I cast my now older eyes back on the week starting
on Monday, April 1 and ending on Sunday, April 7, 2019.

I have to apologise for the extremely high nerd content. There will be wine at
the end to make up for it!

# Working late like it's 1998.

At the start of the week, I had resolved to get more sleep.

It seems that when I have a good night's sleep, really working that
[glymphatic system](https://en.wikipedia.org/wiki/Glymphatic_system) (I'm
currently fascinated by the glymphatic system, I hope you like it too),
amongst other nightly repair activities, there is a greater probability that I
am able to hold my focus the next day.

This was going swimmingly.

At least that was the case until Wednesday, when I decided that the time had
come to port [vxlabs](https://vxlabs.com/), the far more nerdy sister of this
blog, from [wordpress to hugo as
well](https://cpbotha.net/2019/03/31/wordpress-to-hugo/).

One thing led to another, and by 1:00AM (on a school night no less!) I was
busy wrapping up the isso commenting system configuration.

(We're able to use free and ad-free disqus over here because this is a
personal blog. vxlabs on the other hand is strictly speaking a commercial
site, even although it's filled with non-commercial blog posts.)

One of the many funny things about being a nerd, is that it's almost
impossible to go to bed before a technical thing like this has been
convincingly put to bed.

Fortunately this late night indiscretion yielded a working self-hosted
commenting system, and, far more importantly, a [rather attractively styled
post, thanks to the Hugo-port, detailing the whole
installation](/2019/04/06/isso-on-webfaction/).

In entirely predictable fashion, the next day was not the best focus-wise.

P.S. 1998 - first postgrad year in the DSP lab. All-nighters all the way down...

<figure>
{{< img src="dsp_lab_photo4.jpg" alt="photo taken at postcard cafe" >}}
<figcaption>DSP lab, somewhen between 97 - 99.</figcaption>
</figure>

# nim-surprise.

I chose Isso because it's Python.

DayJob(tm) is all about Python, so this was a great choice in terms of time
savings.

With all of the time I had saved, I decided that I would experiment with
re-implementing parts of Isso in [f#](https://fsharp.org/), my current hobby
functional language.

Setting aside the irony here, I learned after some time that getting f#, the
impresive looking [SQLProvider](https://fsprojects.github.io/SQLProvider/) and
sqlite (isso's database) all working together on Linux was ["probably the
single most complicated thing that you can do with a F# project, when it comes
to
tooling"](https://www.reddit.com/r/fsharp/comments/8ufvzz/how_can_i_add_sqlprovider_to_my_existing_project/e1idy1o/).

In this case, I was thankfully able to switch gears and did a brief review of
possible candidates for a functional(ish), memory efficient, fast(ish)
compilation languages that could be used to implement an Isso web-service
replacement.

Somehow I ended up with [nim](https://nim-lang.org/).

This has been on my radar for a while now, but there were always shinier
things to try.

I think what might have put me off was the similarity to Python.

So, with the rest of the time I had saved choosing Isso, I got up to
speed(ish) with nim by starting to implement a replacement for parts of the
isso commenting system.

I was quite positively surprised by the following:

- Compilation speed: The nim compiler transforms my webservice code into C and
  then compiles that in about 1.2 seconds.
- Performance and memory size of resultant binary: This is not a fair
  comparison to Python, but the multi-threaded nim service consumes a few
  megabytes in total.
- Availability of packages especially for building a web service like this:
  Using the nimble package manager, I could install
  [jester](https://github.com/dom96/jester) and had my first running
  web-service in a few minutes.
- Built-in sqlite support.
- Real macros: I used the list comprehension one in the `sugar` module.

This was really just an exercise (for now), but I have a new tool for whenever
I need to write a fast and compact compiled web-service again!

P.S. Learning new programming languages is one of my favourite things.

P.P.S. Thanks to the internet and open source, and especially tools like
github, we are currently going through a sort of programming language Cambrian
explosion. See this [Fledgling Languages List](http://fll.presidentbeef.com/)
for example. Pony!

# Decompression.

On Sunday, we made the drive out to Jonkershoek in Stellenbosch.

Even although it's only 40 minutes away, I haven't been there in far too
long. It's a truly beautiful corner of the planet.

At the Postcard Café, after some internal deliberation, I made the decision
that the moment was special enough to interrupt LAZ
(lifestyle-alcohol-zero(tm)) with an all the more special glass of the
[Stark-Condé Field Blend white
wine](https://winemag.co.za/stark-conde-the-field-blend-2014/).

This is a hyper-local blend of Chenin Blanc, Rousanne, Verdelho and Viognier,
all four varietals which grow on the mountain-side right across from the
Café's veranda.

It really was divine.
