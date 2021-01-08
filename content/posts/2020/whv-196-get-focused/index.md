+++
title = "Weekly Head Voices #196: Get focused"
date = 2020-05-31T22:27:00+02:00
lastmod = 2020-05-31T22:31:06+02:00
slug = "weekly-head-voices-196-get-focused"
tags = ["focus", "gou", "gou-2", "lazar focus", "machine learning"]
categories = ["weekly head voices"]
draft = false
ogimage = "charl_portraitai.jpg"
+++

{{< figure src="sylvia_draws_family_20200531.jpg" caption="Figure 1: Our house clan, as drawn by GOU #2. I've blurred out the names of everyone else, but those of you who know us should be able to figure out who's who. Readers might also notice that I'm slightly outnumbered here." link="sylvia_draws_family_20200531.jpg" >}}

Well hello there folks, please make yourself at home!

This WHV looks back at the two weeks from Monday May 18 to Sunday May 31 of the
extremely strange year of 2020.

That effort of looking back has resulted in the following three items.


## When building automatic analysis pipelines, get your batch accuracy testing up as soon as you can {#when-building-automatic-analysis-pipelines-get-your-batch-accuracy-testing-up-as-soon-as-you-can}

A substantial part of my work hours these past two weeks went into working on a
automatic medical image analysis pipeline, with machine learning
inside&trade;. (I mean "AI", of course. And drones.)

I really do love this stuff, but sometimes it ends up coming down to putting
your head down and keeping it down, in order to grind out every percent or two
in improved accuracy.

The tip I wanted to offer here is the following: Even when you think your
pipeline is way too far from "done"&trade;, get your batch accuracy testing up
and running.

It's a double whammy:

1.  You and your team get early and regular feedback on how your performance is
    going.
2.  You are forced to have the whole concept working from end-to-end. It can be
    surprising how many little issues you still need to solve, and running into
    them sooner rather than later is only good.

By the way, the practical machine learning icon [Professor Andrew Ng's](https://en.wikipedia.org/wiki/Andrew%5FNg) free book
[Machine Learning Yearning](https://www.deeplearning.ai/machine-learning-yearning/) is filled to the brim with practical tips for
implementing ML in practice.


## Lazar Focus: The super tiny Windows app and website distraction blocker that you've always wanted {#lazar-focus-the-super-tiny-windows-app-and-website-distraction-blocker-that-you-ve-always-wanted}

Back at the [start of 2018 I wrote the following about the macOS app and website
distraction blocker called Focus](/2018/01/07/weekly-head-voices-126-fleur-de-lis/):

> After years of resisting these types of software tools due to my belief that I
> should simply apply more grit and will power to squeeze out more focus hours,
> I finally broke down and purchased the macOS app called Focus. You click its
> pretty icon, and then your computer goes into focus mode: The Mail application
> and a bunch of other non-focus-related apps all get killed, and a bunch of
> websites (reddit, youtube, work chat, etc) are blocked for a user-configurable
> block of time.

Even if you skipped that extract, please read the following one about the
_idea_ behind such a focus app:

> It usually takes a single moment of weakness for a distraction to terminate a
> valuable block of focus. It takes a single moment of strength for this tool to
> start a valuable block of focus.

Anyways, I was really missing this functionality on Windows, and so I busted
out my trusty [Lazarus IDE](https://www.lazarus-ide.org/) (who _didn't_ make apps back in the day with the old
win32 Delphi?!) and figured out the various required Windows APIs to create
this brand new super tiny but super effective app and website blocker:

{{< figure src="lazar_focused_screenshot.jpg" caption="Figure 2: Screenshot of Lazar Focus 1.0.0.beta1, main window on the left, settings dialog on the right." link="lazar_focused_screenshot.jpg" >}}

As shown in the screenshot, it's sitting at 5 MB of memory use. In the age of
Electron apps, that's really small.

When you activate focus mode, it'll prevent your browser (Chrome, Brave,
Firefox or Edge) from viewing any distracting website (you get to configure the
list) by redirecting to a local web page with an inspiring quote, e.g.:

> Concentration can be cultivated. One can learn to exercise willpower,
> discipline one's body and train one's mind. -- Anil Ambani

It will also terminate any distracting apps, and helpfully prevent you from
starting them up during your focus session.

The convenient progress bar shows how far you are on your way to a 25 minute
pomodoro, but that is purely for motivation, and not enforced.

The total focus blocks and hours at the top should also help to keep us
motivated and... **LAZAR FOCUSED!**

So, because there are probably (hopefully?) at least two other people who'll
find this as useful as I do, and because shipping and selling software that you
made yourself is awesome especially when it's a hobby project, I have decided
to try and sell Lazar Focus using something like [gumroad](https://gumroad.com/).

Hopefully soon with a hobby hour or three I can finish the installer and the
website, and then make the beta available at a reduced rate.

Because I prefer it for apps like this when I am the buyer, I have decided to
make it available as a one-time purchase, no eval but money-back, with
time-limited upgrades (probably a year?), but with your last licensed version
obviously remaining fully functional until the end of The Windows API.


## Art fun with Portrait AI {#art-fun-with-portrait-ai}

Ever since I spent a bit of time better curating my twitter subscriptions,
getting rid of the vitriol and adding much more STEM (shout out to [Eric Topol](https://twitter.com/EricTopol)
-- you could install twitter _just_ for him and you would be great), they often
bring me shiny treasures.

Recently, it was [portraitai.com](https://portraitai.com/) which brought a great deal of mirth to my home
as we made authentic looking portraits of each other. (We're just a bunch of
silly primates with amazing gadgets.)

It didn't seem to work all that well on me however, until I started pulling
funny faces:

{{< figure src="charl_portraitai.jpg" link="charl_portraitai.jpg" >}}

With that, dear friends, I bid you kindness, happiness and health.
