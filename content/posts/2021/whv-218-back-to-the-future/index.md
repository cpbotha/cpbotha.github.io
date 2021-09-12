+++
title = "Weekly Head Voices #218: Back to the future"
date = 2021-03-29T21:41:00+02:00
lastmod = 2021-03-29T22:00:05+02:00
slug = "weekly-head-voices-218-back-to-the-future"
tags = ["forerunner", "garmin", "programming", "sharepoint", "zstd"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
ogimage = "vergelegen_somewhere.jpg"
org = true
+++

WELL HELLO DERE FRIENDS!

Welcome to the Weekly Head Voices #218, looking back at the week from Monday
March 22 to Sunday March 28 of the year 2021.

{{< figure src="vergelegen_somewhere.jpg" caption="Figure 1: A little forest on Vergelegen farm, close to where we had just enjoyed an absolutely fabulous Sunday lunch, with wine." link="vergelegen_somewhere.jpg" >}}


## Two worlds collide! {#two-worlds-collide}

On the one hand I do worry about the number of hours I spent on this, but on
the other hand it's one of those time investments that should pay off
handsomely over the coming years.

My dream is that one day we'll have an organizational knowledge management
system in place that will enable the almost effortless creation, maintenance
and especially the effective retrieval of relevant documentation.

Because the organization in question lives in the Microsoft ecosystem, the
first laborious steps I have been taking were figuring out the various ways of
getting technical documentation from the hands of engineers all the way into
the company SharePoint.

(I hope you can forgive me, Charl of the past... I do have my reasons.)

Here I would like to share just one of the many dirty tricks I've learned so
far: The easiest way to host a static (Hugo) web site on SharePoint, and hence
having it fully indexed by Microsoft Search, is simply to dump the whole thing
into any modern site's `Site Assets` library, but only after renaming all html
files to aspx.

As soon as I can get [PnP PowerShell](https://docs.microsoft.com/en-us/powershell/sharepoint/sharepoint-pnp/sharepoint-pnp-cmdlets?view=sharepoint-ps) to push updates to full sites a bit more
quickly, I'll hopefully be able to hook it up to [Azure pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines).

Engineers write markdown, documentation magically appear on company SharePoint!


## Let's keep it compact {#let-s-keep-it-compact}

On Thursday November 14, 2019 at 17:48 I made a mental note, where by "mental"
I mean "in my Emacs", to prefer [Zstandard (or zstd) compression](https://en.wikipedia.org/wiki/Zstandard) for everything,
based on a number of posts I had read when I was actually intending to look
into when xz should be preferred over bz2.

In the meantime, zstd's compression ratios, along with its multi-threaded
compression speed and especially its decompression speed, have helped me more
than once, which is why I'm mentioning it here.

Here's the 2 second guide:

```shell
# compress using as many threads as there are CPU cores
tar cf - giant_directory | zstd -T0 -o giant_directory.tar.zst
# decompress REALLY TERRIBLY QUICKLY
zstd -dc giant_directory.tar.zst | tar x
```

You can even get zstd to train on your type of data in order to build up a
domain-specific compression dictionary!


## Can type systems catch bugs? Science says yes! {#can-type-systems-catch-bugs-science-says-yes}

Thanks to [this forum post by Araq, the creator of the Nim programming language](https://forum.nim-lang.org/t/7705#48894),
I read [this conference paper](https://earlbarr.com/publications/typestudy.pdf) describing this really neat research project where
the researchers retroactively type-annotated a random selection of publically
available bugs in un-typed JavaScript code, and then showed that about 15% of
of those bugs would have been caught.

In their words:

> Evaluating static type systems against public bugs, which have survived testing
> and review, is conservative: it understates their effectiveness at detecting
> bugs during private development, not to mention their other benefits such as
> facilitating code search/completion and serving as documentation. Despite this
> uneven playing field, our central finding is that both static type systems find
> an important percentage of public bugs: both Flow 0.30 and TypeScript 2.0
> successfully detect 15%!

I found the simple but quite solid experimental methodology in the paper
delightful, over and above the fact that this is a great one to have in my
database for arguments about the utility of type systems.

(This would possibly have made dynamic-type-slinging Charl from the past go red
in the face.)


## Science doesn't give a s\*\*\*t about my beliefs either {#science-doesn-t-give-a-s-t-about-my-beliefs-either}

That makes for two (2) points in this short blog post that would have caused
Charl from the past to get _quite_ unhappy.

That's science for you folks: Reality develops, or it just stands there, really
really still, and/or observations yield new data, and then all of your models
have to be updated!

{{< figure src="science_and_your_beliefs.jpg" link="science_and_your_beliefs.jpg" >}}


## Forerunner hot takes {#forerunner-hot-takes}

The more-or-less free [Apple Watch 3 that I acquired in July of 2018](/2018/07/24/weekly-head-voices-149/#the-apple-watch-vitality-and-you) has served
me really well over the years, but for mysterious reasons that I can't explain,
the time had come to upgrade to a _real_ running watch.

After weeks of reading reviews, creating little comparison tables and
complaining to friend LM about the utterly devious way in which Garmin has
segmented their market into tiny little pieces with frustrating borders, I
finally settled on [the Garmin Forerunner 245 (without music)](https://www.dcrainmaker.com/2019/04/garmin-forerunner-245-music-gps-watch-in-depth-review.html).

I made sure that the watch would be delivered this past Friday so that I could
take it for a spin or two over the weekend.

My first observations are:

-   One really notices all of the Apple polish when you have to give it up. It's
    clear that the Forerunner is a robust tool for running, but heck is it
    klunky. Every time I push one of the four physical buttons, I imagine the
    watch going "hooooonk!".
-   The device includes a whole bunch of advanced-looking new-to-me metrics by
    [FirstBeat](https://www.firstbeat.com/) (recently acquired by Garmin) like Stress measurement, the Body
    Battery (taking into account sleep and stress to predict how much energy you
    should have), advanced recovery time (this is pretty useful: how many hours
    before my next run, based on how hard the previous one was, stress levels and
    also on sleep quality in the meantime) and so on.
    -   I knew about FirstBeat because the [TomTom Runner 3](/2017/02/03/weekly-head-voices-115/#the-dutch-watch) I had before the Apple
        Watch 3 used [their VO2 max estimation algorithm](https://www.firstbeat.com/en/science-and-physiology/fitness-level/). However, what I **just**
        learned was that specifically [heart rate variability (HRV)](https://www.firstbeat.com/en/blog/what-is-heart-rate-variability-hrv/) seems to play an
        important role in much of FirstBeat's work.
-   I now have an optical [pulse oximeter](https://www8.garmin.com/manuals/webhelp/forerunner245/EN-US/GUID-2EE28BB8-91F1-4BCE-AE13-6CAEF50AD5C4.html) on my arm, which, although far from
    accurate, does give at least some estimate of my blood oxygen. This is
    important to me especially to ensure that that aspect of my sleep is also
    going as it should.
-   About that sleep tracking... the sleep onset detection must be a bit of an
    embarrassment for at least some of the folks at Garmin. For example, last
    night the watch detected onset of sleep while it was lying on the bedside
    table during my pre-bedtime shower. Surely with that HR and PulseOx sensor,
    the watch should know that it's not even on my arm? Apple Watch 3 does this
    with 100% accuracy with only its HR sensor. (To add insult to injury, the
    Garmin detected that onset an hour before my configured bedtime.)
-   On the other hand, the battery life on this thing is, as is to be expected
    from a Garmin, quite phenomenal. (this is probably partly due to all of the
    half-implemented algorithms haha)
-   More generally speaking, I've disabled most of the notification features, so
    that the thing on my arm is more like an old-fashioned, mild-mannered watch
    that transforms into super-watch when running-related activities have to be
    undertaken. That in itself is an improvement that is not to be sneezed at.
-   In summary: Acknowledging the multitude of biases at play, I am really
    enjoying the new device. In addition, my Apple Watch 3 could hereby enter the
    family pool, freeing up another AW3 which now lives on the proud arm of my
    first running GOU.


## Pompiedom {#pompiedom}

Thank you folks for reading these words, and especially for reconstituting
thoughts that are probably similar to the ones that happened at my end before
and during the production of said words.

You're more than welcome to add some words of your own in the comments section
below. (I literally installed and configured it for you. No pressure
though. You know me.)

On that note (specifically the note of adding your own words): A part of my
brain has been entertaining the idea of setting up a [discord server](https://www.businessinsider.com/what-is-discord?IR=T) called _The
Church of Love and Science and/or Friends of Charl_.

The brain part in question claims that it would be a place for friends, and for
any other fans of Love and Science, to hang out and sometimes make interesting
new connections, and to enjoy the existing ones.

What do you think?

Err, let me know in the comments, or via Signal, or via discord?
