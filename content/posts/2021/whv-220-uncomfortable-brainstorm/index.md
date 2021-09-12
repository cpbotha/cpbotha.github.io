+++
title = "Weekly Head Voices #220: An uncomfortable brainstorm"
date = 2021-04-15T09:11:00+02:00
lastmod = 2021-04-15T20:22:06+02:00
slug = "weekly-head-voices-220-uncomfortable-brainstorm"
tags = ["ideas", "lastpass", "microsoft", "mont marie", "side-projects"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
ogimage = "mont-marie-pano-20210411.jpg"
org = true
+++

Welcome to Weekly Head Voices number Two Twenny!

This edition covers the week from Monday April 5 to Sunday April 11, of which
thankfully only 57.1% of the days (vs the usual 71.4%) were officially
dedicated to work!

{{< figure src="mont-marie-pano-20210411.jpg" caption="Figure 1: A scene from Sunday lunch at Mont Marie in Stellenbosch. Previous visit in [WHV #182](/2019/11/04/weekly-head-voices-182-can-you-predict-what/). Still beautiful." link="mont-marie-pano-20210411.jpg" >}}

The work week was indeed shorter (thanks week!) but perhaps just a bit too high
intensity.


## Why does there have to a discomfort stage? {#why-does-there-have-to-a-discomfort-stage}

You see, we had previously made an important technical improvement to a product
that was supposed to be released two weeks ago.

Fortunately, during pre-release testing on the staging server (this is
completely separate from production), some of our customers discovered issues
that have been there for longer, but were now exacerbated, or rather made more
apparent, by the improvement we had made.

Now that is an interesting tension!

One's first-order reaction is to want to roll-back the improvement, because
we're humans, and we are compelled by our nature to do almost anything to
resolve the discomfort we feel when our fellow humans are not as happy as they
should be using the thing that we have built for them.

That little person in your head is shouting: Go back, go back! You should have
stayed where you were!

However, this is one of those sometimes uncomfortable cases when the
first-order reaction has to be resisted, because you really have to do The
Right Thing.

We started by measuring all the things, in order to understand the whole
problem better.

After that we started chipping away at some of the newly emphasised
issues. Chip chip.

Writing this up now, we are in a much better place than last week, having
seemingly cleared that darned hump in the middle, and we are hopefully on our
way to _the other side_.

(This situation is quite reminiscent of the [five stages of the creative process
I've mentioned before on this blog](/2013/11/11/creative-process-stage-5-whv-67/).)


## Instant switch-off {#instant-switch-off}

With the days as short as they are now, I often go for a mid-afternoon work-day
run.

These have been amazing in terms of switching off, and returning to work
afterwards, refreshed and in a substantially more zen mood.

In addition to this, family time in the evenings, also preceded by a pretty
effective disconnect, made a perceptible difference to stress levels.


## Microsoft has a pretty good password manager going on {#microsoft-has-a-pretty-good-password-manager-going-on}

TL;DR: If you're more on Windows and Linux than on Mac, you could consider
using [Microsoft's password manager](https://blogs.windows.com/windowsexperience/2021/02/05/simplify-and-secure-your-life-with-microsofts-autofill-solution-for-passwords/).

Some time before Lastpass changed their generous free tier, causing many folks
to migrate away or to start paying, I decided to move all of my online password
management to Dropbox Passwords.

This was because I had been using LastPass for years (their free tier really
was too generous. I usually do pay for services, but here there was no
incentive), and thought that I should either start paying or move to a paid
service, which Dropbox Passwords is in my case.

Anyways, this experiment started on Saturday, October 3, 2020 and concluded on
Saturday, April 10, 2021 after I finally made peace with the fact that the
Dropbox Passwords app was indeed too klunky (PK you were right), and especially
when I saw that Microsoft had secretly been putting together a pretty
respectable [password management ecosystem](https://blogs.windows.com/windowsexperience/2021/02/05/simplify-and-secure-your-life-with-microsofts-autofill-solution-for-passwords/).

You see, I've been using the new Microsoft Edge browser (aka Edgium) for a
while now, even on [the shiny new M1 MacBook Air](/2021/03/21/new-emacs-capable-hardware-m1-macbook-air/), where the native M1 build is
great for running the web-app versions of apps that don't have native M1
versions yet.

In addition to that, I'm also already using [Microsoft's Authenticator app](https://apps.apple.com/us/app/microsoft-authenticator/id983156458) for
2FA on my home and work Microsoft accounts.

Between the Edge browser (there's also [a Chrome plugin](https://chrome.google.com/webstore/detail/microsoft-autofill/fiedbfgcleddlbcmgdigjgdfcggjcion?hl=en)) and the Authenticator
app's autofill function, you can haz your passwords on desktop and mobile, with
a similar level of integration as you might see when using icloud with Safari.


## Brainstorm yourself {#brainstorm-yourself}

[Side-projects](/tags/side-projects/) folks!

They're mostly great, but they have this unfortunate side-effect that they're
always multiplying, seemingly even more so when there's a full graveyard of
incomplete previous side-projects to function as fertile breeding ground.

In playing my part in this specific force of nature, I spent some time this
weekend brainstorming new side-project ideas with myself.

(It is not lost on me that "brainstorming" project ideas in your own time, and
not only that, but doing it by yourself, does not fall under "standard weekend
activities" for many people. I have made my peace.)

This time I was quite happy to be using a [sketchnote-inspired](/2018/05/13/weekly-head-voices-142-theory-of-mind/#sketchnote-your-life) technique, trying
to map out the landscape of "skills", "learning", "my pain" (not hurting here,
this just refers to the need that the artifact should address) and "market
pain" in order to find that One Final Side-Project that would satisfy all of
those requirements and allow me to rest. Finally.

After an hour or two, an idea that seemed to satisfy many of the map points did
actually pop out!

_Narrator: It was not a very good idea._

The idea that popped out fit the whole map too easily, in retrospect.

One could say it was a bit like glibness as opposed to intelligence in that
regard.

The idea was to build a document / information retrieval tool for Windows that
was at least as good as Spotlight on macOS.

You'll remember from my [Note-taking strategy 2019](/2019/09/21/note-taking-strategy-2019/) post, that my knowledge-base
has files all over the show. A large part of using this thing effectively, is
being able to call up that relevant article from 5 years ago in a fraction of a
second.

Windows Search is, in spite of years of work and update, still not even in the
same ballpark as Spotlight in terms of retrieval accuracy and speed, so there
is a technical opportunity there.

As these things go, on Saturday evening I had my trusty new Orgmode notes file
for this new project (`WorkingWindowsSearch`, sorry I'm not marketer), and I
was slapping together a C# WPF tool with [Lucene.net](https://lucenenet.apache.org/) (after a bit of a false
start with xapian, which I use for my email on Linux) and [PDFPig](https://uglytoad.github.io/PdfPig/), and had got
it to start indexing a part of my [JBOP collection of PDF references](/2019/03/21/weekly-head-voices-165-get-in-my-pocket/#replacing-pocket-with-just-a-bunch-of-pdfs-jbop).

Fortunately, bed-time arrived sooner rather than later, terminating this
(apparent) fecklessness, and the next morning I woke up with that awkward
morning-after feeling.

"Uh, what was I thinking?!"

During the day, the gears in my head kept on turning by themselves, and the
notes kept on accumulating.

I had arrived at the conclusion that local file search was not going to cut
it.

One would need integration with different cloud services.

This thought further developed into the idea that the side-project could be
merely be "sort of a retrieval hub" that simply talks to all of the relevant
APIs and showing results together.

I had also arrived at the conclusion that I should probably stop right
there.

It had been an entertaining and educational dalliance with a list of
technological artifacts that were new to me, but the longer-term energy did not
seem to be there.

It was back to the drawing board (or rather sketchnotes) for me, as soon as a
sufficient amount of time again become available.


### Death of a side-project: Epilogue {#death-of-a-side-project-epilogue}

On the Tuesday after the weekend (looking into the WHV future here), I ran into
[Raycast](https://raycast.com/), a tool for macOS that combines Spotlight-like file search with a whole
bunch of productivity plugins enabling power-users to perform their tasks from
a single keyboard-driven app.

With a $2.7 million seed round of capital led by Accel, it seems there are at
least some people who think that this has market potential, even on a platform
where the search part is already catered for.


## Read here for possibly life-changing advice {#read-here-for-possibly-life-changing-advice}

I had this scheduled for the next WHV, but this one is in dire need of a
conclusion, so sorry next WHV!

I really enjoyed reading through [Wait But Why's Mailbag #2 post](https://waitbutwhy.com/2021/04/mailbag-2.html). (Tim Urban is
such a human treasure.)

The piece I would like to highlight now, is Tim Urban's reply to the question
"What is the best piece of advice you have ever received?":

> I met Chris Anderson, the head of TED, in 2015. He had read a few WBW posts and
> offered me the opportunity to give a TED Talk at the 2016 conference (which was
> six months away). Immediately full of both gratitude/excitement and
> dread/anxiety, I asked him if it might be better to wait a couple years until I
> had some more speaking experience. He paused thoughtfully for a few seconds
> before saying, ****"There's no time like the present."**** I took his advice. Since
> then, his voice saying those words has popped into my head again and again
> during hard decisions, and I'm yet to regret following them.
>
> Great advice is sometimes great because it's totally original or framed in an
> original way. But, as in my story, a well-known platitude, at the perfect
> moment, can also make a huge impact. What makes Chris's advice so valuable to
> me wasn't that it was something new—it was that the lesson I learned from
> taking the advice in that particular moment turned a cliché into a mantra.

Exactly as he describes, it hit me too when I read it.

Folks, I can't think of a better way to wrap up this post, than just planting
the hopefully well-timed advice above in your head.

Here it is again, for easier eye-ball insertion: ****There's no time like the present.****
