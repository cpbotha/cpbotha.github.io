---
title: "Weekly Head Voices #171: ICEMiRB."
slug: "weekly-head-voices-171-icemirb"
author: cpbotha
date: 2019-05-22T22:38:00+02:00
tags:
  - sleep
  - caffeine
  - focus
  - icemirb
  - remarkjs
  - pybtex
  - asciidoc
  - java
  - jpackager
  - emacs
  - ivy
  - helm
categories:
  - weekly head voices
type: "post"
---

<figure>
<a href="fullmetal_baboon.jpg">
{{< img src="fullmetal_baboon.jpg" >}}
</a>

<figcaption>

Down here, you never know what sort of fantastic beasts you could run into. I
met this particular fullmetal creature <a
href="https://goo.gl/maps/KpcQGa6hEcbd87mF7">right about here</a>.

</figcaption>

</figure>

Dear friends,

In this post, I do a particularly lossy review of my trip through time, from
Monday May 6 to Sunday May 19, 2019.

First we talk about sleep, then a long part on technical tricks, then a
slightly more backyard philosophical piece on human tool sharpening, and
finally the announcement of a new academic event somewhere in the far or near
or medium term future.

# Sleep.

If you were one of the people who found themselves in my company for more than
about 10 nanoseconds during the past weeks, I probably tried to get you to
listen to [the 6-hour long podcast between Peter Attia and Matthew Walker on
the topic of
sleep](/2019/05/07/weekly-head-voices-170-yeet/#the-easiest-but-most-high-impact-measure-you-can-take-to-not-die-too-soon-go-to-bed-on-time).

Usually I'm able to get something sufficiently out of my system by writing
about here. I do this quite deliberately to try and spare my innocent
bystanders.

This time, either it didn't really help, or I underestimate how much I would
have blabbed about it had I not let off some of the sleep steam here.

IN ANY CASE...

During the past weeks I have been paying more attention than usual to sleep, in
terms of quality, quantity and consistency.

Because I also decided to take more notes than usual during the day, I could
see quite acutely the effects of good sleep vs bad sleep on my performance and
energy levels the next day.

If sleep was good the night before, my exercise the next day seemed to take
much less effort, I still seemed to have more than enough energy at the end of
the afternoon, and, most importantly, I had almost no trouble with that
ever-important f-word:

> FOCUS.

Conversely, if I let sleep-onset slip by as little as half an hour, my brain
would be in three thousand pieces by three 'o clock the next afternoon.

It is starting to dawn on me that all of those evenings where I tried to borrow
an hour or even two from my sleep had a far greater cost the day after than I
ever realised.

**I can only conclude, that to experience the highest quality and intensity
waking hours, one simply has no choice but to pay the full 33% sleep tax.**

## Damnit coffee.

Caffeine has a quarter life of 12 hours.

If you're positively buzzing at 1PM, 25% of that caffeine is still active in
your system at 1AM and absolutely will interfere with your sleep quality.

I have compromised by having my last shot before lunch, or in extreme cases
right after.

# TIL: Things I learned.

This WHV is one week late, because it seemed like nothing happened in the first week.

However, it seems I did learn quite few new technical tricks. In the
subsections below, I share a selection of these with you.

## remarkjs is great for quickly building technical presentations.

At [my favourite local
meetup](https://www.meetup.com/Helderberg-Software-Developers-and-Entrepreneurs/),
I was planning to give a talk on [Hugo](https://gohugo.io/), the static website
generator which is powering this site, and which I'm increasingly using instead
of wordpress.

Because every new project is an opportunity to check and perhaps upgrade one's
tools (see below for how this can also sometimes backfire), I set aside the
trusty [reveal.js](https://revealjs.com/) and [ox-reveal Emacs orgmode
interface](https://github.com/yjwen/org-reveal) I usually bust out, and paddled
out onto rough internet seas, on the lookout for an alternative solution.

(Now that I think back, I had no good reason to search for an alternative,
except that my pre-configured reveal.js style and formatting never made me
really happy.)

Fortunately, after not too long I ran into [remark](https://remarkjs.com), an
HTML- and markdown-based presentation tool that seems simpler than reveal, but
still quite attractive, as you'll be able to see on the demo site above.

At this point, I was pleasantly surprised that this distraction had not cost
more than about 30 minutes.

At least, that *was* the case until I ran into [remark-mode for
Emacs](https://github.com/torgeir/remark-mode.el)!

As you can see from the screenshot, this enables a pretty smooth
generate-as-you-type workflow.

Also noteworthy, is the great built-in presenter mode. Press `C` to clone the
window into a new linked presentation which you can move off to the external
display, and then press `P` to switch to presenter mode where you can see all
of the comments you have left in the markdown.

I made two small fixes in [my own
fork](https://github.com/cpbotha/remark-mode.el) to enable seeding with your
own HTML template, and to enable the generate-as-you-type to work also on
straight `.md` files. I prefer keeping my presentations as `.md` (vs `.remark`)
as most of the search logic I have built in Emacs assumes `.org` and `.md`
files for my notes.

By choosing remarkjs instead of my existing revealjs workflow I did manage to
exhaust the short block of time I had allocated to prepare for the talk, and so
the talk morphed into a more spontaneous affair, dealing with orgmode, remarkjs
and in the end, also a bit of hugo.

## pybtex is a pure-Python bibtex parser and renderer.

One of the sites getting the wordpress-to-hugo upgrade treatment was my
internet persona placeholder, the almost completely unknown
[charlbotha.com](https://charlbotha.com/).

The upgrade of this tiny site would have gone quite easily, were it not for the
fact that I was using the wordpress papercite plugin to publish a list of all
of the publications, including fulltexts in most cases, that I've had the
pleasure to be involved in over the years.

I could not find any tool which could give me exactly the sort of publication
lists that papercite was able to.

To me it was clear that yet another tool was required. ("my god, it's full of biases!")

Fortunately, [@stefanvdwalt](https://mentat.za.net) very quickly pointed me at
the Python package [pybtex](https://pybtex.org) when he saw that I was
careening off into the dark side with [citation.js](https://citation.js.org).

A few hours later I had built a script which was able to eat my
Zotero-generated bibtex file and spit out different lists of publications with
linked PDFs straight into a Hugo-edible markdown file.

See [charlbotha.com/publications](https://charlbotha.com/publications/) for the
result.

P.S. Making it available to a broader audience is on my todo-list.

## asciidoc is one of your best choices to write software manuals.

We are currently working hard towards the release of version 2.0 of our
flagship FDA-certified cardiology product,
[TeleSensi](https://www.telesensi.com).

Because updating the user manual with every release is not as fun as it could
be, I had the idea to convert the doc-format source file to some text-based
document authoring system.

Again, in spite of past positive experience writing manuals with
[reStructuredText](http://docutils.sourceforge.net) and LaTeX, I made use of
the opportunity to try out
[asciidoc](https://asciidoctor.org/docs/what-is-asciidoc/).

In *this* case, I am happy to report that the choice of asciidoc ended up
beating all of the alternatives by a mile.

I started by [pandoc](https://pandoc.org)-ing the docx to asciidoc, and then
manually (ha ha, it's a joke we writers tell) fine-tuned the document until, in
a few hours, the new manual looked significantly better than the original.

Long story short, our manual is now part of the software source repository and
hence version-locked, it can be automatically built for new releases, and parts
of the manual can be linked programmatically to form parts of our compliance
documentation.

With the manual now essentially being a software construct, there are many more
tricks we can do (and already do, but I'm not allowed to say much more).

## You can build self-contained installers with legacy non-modular apps and recent modular Java.

In a rather surprising (to me) turn of events, I had to convert some legacy
(read: non-modular) Java code from a product component to a self-contained
installer on Windows and macOS so that our users never even have to *think*
about JREs.

It's possible that the following magical recipe could help you, should you ever
find yourself in a similar predicament:

- Install [AdoptOpenJDK](https://adoptopenjdk.net) 11 (LTS)
- Retrieve and extract this [backport of the new
  javapackager](https://mail.openjdk.java.net/pipermail/openjfx-dev/2018-September/022500.html)
  from the yet to be released Java 13 into your OpenJDK 11.
- Build your legacy [uber-JAR](https://imagej.net/Uber-JAR) with the freshly
  installed OpenJDK11.
- Use `jdeps` to determine the list of modular dependencies of your uber-JAR.
- Armed with this knowledge, build a mini java-runtime using `jlink`.
- Now feed your uber-jar and the freshly created java-runtime to `jpackager` in
  order to construct a fully self-contained executable or platform-specific
  installation package.

Much, but not all, of that comes from [this blog
post](https://medium.com/@adam_carroll/java-packager-with-jdk11-31b3d620f4a8).

## You can easily dired-jump to the currently ivy-read'd file in Emacs.

I mix and match [ivy](https://github.com/abo-abo/swiper) and
[helm](https://github.com/emacs-helm/helm) in my Emacs.

When you're helming for a file, you can usually press `F5` to open dired
(Emacs's built-in filemanager) on that file's directory.

This is quite convenient, and something I was missing in ivy, which I use for
example as part of `find-file-in-project`.

Weeeeell, by adding the following to your `init.el`:

```emacs-lisp
;; for any ivy-read, press M-o to get action menu,
;; then 'd' to start dired with that file selected
(ivy-add-actions
 t ;; add for all types
 ;; (cdr x) gets the full filename, not just relative
 `(("d" ,(lambda (x) (dired-jump nil (cdr x))) "dired")
   ))
```

... you get to select `d` from the `M-o` action menu to `dired-jump` (a
wonderful command by itself, usually bound to `C-x C-j`) to the currently
focused file.

# Sharpening these rocks.

All of that brings us to this.

I spent quite a few hours last week performing meta-work: That is, not doing
the work itself, but rather sharpening the tools required to do that work.

As with all important matters, there's an XKCD comic about this topic too:

<figure>
<a href="https://xkcd.com/1205/">
<img src="https://imgs.xkcd.com/comics/is_it_worth_the_time.png" alt="xkcd on
tool sharpening">
</a>
<figcaption>
Incredibly useful visualization by XKCD: How much time will your tool
sharpening save per event, and how frequently does that event occur? The
cross-indexed block is how much time this could save you over 5 years.
</figure>

Besides the mostly defensible tricks mentioned in the previous section, I did
also invest hours in attempting to update the mobile and email-based parts of
my personal knowledge management strategy (because
[Windows](/2019/04/27/new-laptop-2019/)), but these hours led to a less than
satisfactory solution.

If I have to be honest, it feels like those hours were wasted, although it was
impossible to say beforehand that the effort to outcome ratio was going to be
that bad.

(To make it all a bit more interesting, a few days later some of the dead-ends
explored during those wasted hours led to coincidental improvements of other
frequently occurring (on the order of 5 times per day) components of my
workflow.)

Some folks double down on their workflows, rather taking the small hits and
spending the time doing their actual work.

I find it difficult to resist an opportunity for streamlining.

Sometimes this pays off, not in the least because of the compounding effects of
frequently applicable optimisations, and other times I fall down the rabbit
hole.

In my dreams, I am able to reach a sort of workflow optimisation pinnacle,
where all inefficiencies have been excised from the system. In reality, goal
posts like to move it move it, and so the scramble never ends.

How do you approach this?

# ICEMiRB

*The International Conference on Emacs, Minimal Running and Blogging*, or
ICEMiRB, is a new meeting of minds and legs that the aforementioned and
indomitable [@stefanvdwalt](https://mentat.za.net) and I are currently bouncing
around.

I actually just want the t-shirt, but the more I think about this, the more I
think it's something that one day really has to happen.

Please let me know in the comments if you would be interested in taking part.

I imagine we will go all out in terms of the various forms of attendance and
participation that we accommodate.

Have a beautiful week folks, I hope to see you again soon!

## P.S.

@stefanvdwalt just reminded me that Mindfulness is to be the fourth main topic
of the ICEMiRB.

Because the acronym is already of substantial girth (yes, we know that
Mindfulness and Minimal could co-habit the same part of the
acronym. coincidence?!), we will try to settle for one of two conference
taglines:

> ICEMiRB - A Mindful(TM) Conference.

or

> ICEMiRB - The Mindfulness is silent.

or not.

