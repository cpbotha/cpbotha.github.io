---
title: "Weekly Head Voices #173: I know."
slug: "weekly-head-voices-173-i-know"
author: cpbotha
date: 2019-07-17T21:53:00+02:00
tags:
  - aikno
  - compounding
  - devide
  - dogs
  - emacs
  - email
  - eric topol
  - fastmail
  - gou
  - gmail
  - mu4e
  - solar
categories:
  - weekly head voices
type: "post"
---

<figure>
<a href="helderberg_protea.jpg">
{{< img src="helderberg_protea.jpg" >}}
</a>
<figcaption>
Taken on a run in the mountain, on a trail quite aptly called the protea. By
the way, although I have become slightly less terrible at running up hills, I'm
still quite bad.
</figcaption>
</figure>

Let's go for a slightly less anxious start than the previous edition did:

Well hello there folks!

A week ago, I made a deliberate decision not to post a WHV, as I really did not
have much to report on.

However, it's funny how these things go. One week nothing... Then it's just a
single week later and there's almost a bit too much that I would like to talk
about.

It seems to have been a mix of more writing, but also just more doing.

So, looking back at the two weeks from Monday July 1 to Sunday July 14, 2019, I
would like to present the following notes.

# Bullet List of Miscellany (BLoM).

- GOU#1, age 13, is on a week-long school trip in a different time zone
  (GMT+8). I am super happy that she can have this experience, but durnit, one
  misses one's genetic offspring units dearly!
- Remember that I told you about our [solar inverter not talking to the
  battery's BMS](/2019/06/30/weekly-head-voices-172-abc/#solar-powerrrrrrrr)?
  Well, one small recommended firmware upgrade later, from 151507 to 151508,
  and the whole system is completely down. Please cross your fingers, because
  we've tried **everything** else.
- I regularly get accosted by off-leash dogs whilst running. There are
  incredibly clear by-laws down here which absolutely forbid any dog ever being
  off-leash in any public space which is not a designated off-leash zone. I
  recently made the mistake (twice) of trying to explain this to the relevant
  dog-owners. Well, dog-owners seem to be quite sadly under-endowed in the area
  of introspective capability, but at least I'm getting a lot better at
  unprepared debates in public spaces. (Psychologists in the audience, help me
  out here with any tips please!)
- I really enjoyed [this Sam Harris podcast with Eric
  Topol](https://samharris.org/podcasts/162-medical-intelligence/). [Eric
  Topol](https://www.scripps.edu/faculty/topol/) is a cardiologist and the
  founder and director of the Scripps Research Translational Institute in the
  US. Apart from the main topic of the discussion, namely Topol's
  well-developed and articulated view of AI in medicine (well, his books on
  this topic are quite influential, so there's that), I was struck and inspired
  by the humble gentleness of this impressive intellect. Furthermore, although
  we are not supposed to use twitter anymore (in some circles, it has been
  dubbed "road rage of the internet"), [Prof Topol's tweet
  stream](https://twitter.com/EricTopol) is a shining example of how twitter
  could be used more constructively.

# Would you like some more Emacs with that Email?

During the past two weeks I published two blog posts on my nerd blog:

- [Sending queued mails in the background with
  mu4e.](https://vxlabs.com/2019/07/03/send-queued-mails-in-background-with-mu4e/)
- [Is mbsync really faster than offlineimap? A
  measurement.](https://vxlabs.com/2019/07/05/mbsync-vs-offlineimap-speed/)

Based on these, you might come to the conclusion that I'm processing email
inside of Emacs
[again](/2014/05/24/weekly-head-voices-71-vote-for-the-future/).

I can confirm that this is indeed the case.

Probably for a large part due to the popularity of google's gmail, the growth
of the rest of the email ecosystem seems to have been stunted to a significant
degree.

In this specific case, I am referring to the dearth of really good email
clients for Windows.

(By the way, Thunderbird, still my fallback, usually makes the top of any
Windows email client lists. However, if it weren't for GMail, Thunderbird
would probably also be miles better than it is today.)

After losing more hours than I could afford trying to find that perfect email
client (I would have settled for "still has all of its own teeth"), I realised
that I would just have to buckle down and get [mu4e](/tags/mu4e/), my favourite
Emacs email client, working well enough on Windows, which I currently *prefer*
(DID I JUST SAY THAT?!) due to my [ThinkPad X1E
baby](/2019/04/27/new-laptop-2019/).

That was of course a whole different wormhole to get sucked into.

Well, more of those precious hours later, I have a Frankensteined concoction
consisting of Emacs running on the Windows Subsystem for Linux (WSL),
displaying to the Windows desktop via [X410](https://token2shell.com/x410/),
and opening email and orgmode attachments, and dired files, using the native
Windows handlers via an
[xdg-open](https://wiki.archlinux.org/index.php/Xdg-utils#xdg-open) work-alike
I coded up in Python.

(I am planning to release my xdg-open clone along with a more detailed howto
blog post. Let me know if you would like advanced access.)

Soooo.... after all of that effort I am now back more or less to where I
started in 2014.

(To be honest, Emacs is near the top of my list of compounding activities. The
fact that it's back in my email workflow, combined with five years of
compounded Emacs skills, has resulted in further increased efficiency.)

## Sticking it to the Man (GMail) with FastMail.

Wrapping up that email workflow reconfiguration frenzy, I did spend some
minutes doing a quick survey of fastmail alternatives which might have email
servers somewhat closer to the Southern tip of Africa and hence shave off a few
seconds of latency.

I found nothing that came close in terms of features and price. Except for one
outage, [I've been a really happy fastmail camper for the last three
years](/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/).

All of that, together with the fact that gmail's continued dominance is
unhealthy for the world of email, convinced me to stick with fastmail for the
conceivable future.

# Stone Three Healthcare is now a thing.

[Stone Three Healthcare](http://www.stonethree.com/healthcare/), until recently
a business unit within Stone Three Venture Technology, has now been officially
spun out.

In other words, S3HC is now a more-or-less independent company that will
henceforth have to create its own success.

As some of you know, this project has been cooking for a few years now.

We have a really great team, products with customers and a market, and a
respectable patch of runway.

There are worse ways for a startup to start up.

P.S. if you have any golden tips for startup dummies, I (and probably others)
would be super grateful if you could let 'em loose in the comments!

# Always Be Compounding: The side-project edition.

In the previous WHV, I [started going on about the principle of ABC, or Always Be
Compounding](/2019/06/30/weekly-head-voices-172-abc/#always-be-compounding).

Since then, I've been spending a great deal of mental cycles on finding more
ways to ABC.

Besides the more general examples I mentioned there, another method is to
design some long-running project that can function as a container for all of
the work that you'll have to do in any case.

A perhaps slightly flawed personal example is DeVIDE, an open source
visualization and image processing tool that started life somewhere in 2001,
[was renamed to DeVIDE at the end of
2003](/2003/12/19/the-visualisation-and-image-processing-platform-formerly-known-as-dscas3/),
open-sourced in 2007 and had its last release in 2012.

Although it did see some use of that, the project went into hibernation
(weeeelll....) when I left academia.

My point is that, for about 10 years, I had a single technical *artifact* with
a name that became slowly better known (even if it was often by its alias "Not
Responding"), into which I could integrate all the other new work I was doing.

This enabled me to enjoy some of the advantages of compounding effort, in the
shape of DeVIDE, even although the work I was doing over the years necessarily
had to change.

(A really nice additional benefit was that some students sometimes found the
software useful! I do wish that that part could have continued for a little
longer.)

Setting aside my
[DeVIDE-nostalgia](/2019/05/07/weekly-head-voices-170-yeet/#a-strange-thing-happened-this-weekend)
(and a bit of sadness) for a moment, I would like to apply some of this
learning to my current (and perhaps your) situation.

My idea would be to define a new side-project that can act as the slightly
longer-lived container for some of the smaller side-projects and learnings I
sometimes manage to spend time on.

It would have to be a technology / thematic fit for many of my other
side-projects. It would of course constitute a double-whammy if this
side-project had commercial potential.

Well, SURPRISE!

I do have at least one side-project that ticks a number of these boxes, and
could *potentially* serve as such a vehicle.

## AIKNO

The side-project in question is called AIKNO, which is pronounced "I know", but
which somehow expands to *AI organizational knowledge base*. Magic!

It eats all of your organization's emails for breakfast, and then uses
different methods, both algorithmic and crowd/team-sourced, to sort and
organize those emails and all of their attachments, and then makes those easily
and attractively (hey, data visualization!) accessible by that organization.

Think of it as an almost zero-effort always-up-to-date organizational knowledge
base.

Besides having slots for various machine learning and visualization techniques,
it fits nicely into my overgrown knowledge management hobby.

The first commit in the AIKNO repo was in November of 2017. Oof. The prototype
is able to import emails and attachments into its structured database, and
already does funky stuff with similarity searches and whatnot.

Unfortunately, it has also suffered from my regular technology stack
changes, and it's currently languishing while I write blog posts.

My previous failed side-project was called *TableTops*, or *Paradigm Desktop* by
the same people who dubbed DeVIDE "Not Responding".

It was a free-form canvas / whiteboard tool for the free-form storage and
linking of *anything*. For example, it had relational data structures for
linking specific coordinates or regions in photos to centralised concepts, and
other interesting things that will probably never see the light of day.

It went through seven tech-stack-change-induced rewrites before being obsoleted
by [my growing Emacs Orgmode powers](https://vxlabs.com/tags/orgmode/). (first
commit October 2013, last commit August 2017, now on the backest back
burner. the one that's not burning.)

I did learn a *tremendous* amount.

Maybe *that* is the real reason for doing these things?

# Always Be Learning.

Thanks for joining me on that trip folks.

I hope to see you soon. Until then, make an amazing time!

<figure>
<a href="coffee_company_belgian_brownie.jpg">
{{< img src="coffee_company_belgian_brownie.jpg" >}}
</a>
<figcaption>
100% amazing Belgian brownie and delectable flat white at the
Coffee Company on Lourensford this past weekend.
</figcaption>
</figure>
