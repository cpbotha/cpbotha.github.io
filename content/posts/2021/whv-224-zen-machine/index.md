+++
title = "Weekly Head Voices #224: Zen machine"
date = 2021-05-29T08:30:00+02:00
lastmod = 2021-05-31T14:01:48+02:00
slug = "weekly-head-voices-224-zen-machine"
tags = ["autumn", "new computer", "running", "yarn"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
ogimage = "vergelegen_camphors_20210523.jpg"
org = true
+++

Dear friends,

You are reading the 224th edition of the Weekly Head Voices, covering the week
from Monday May 17 to Sunday May 23 of the year 2021.

{{< figure src="vergelegen_camphors_20210523.jpg" caption="Figure 1: Scene from a truly fabulous autumn Sunday lunch with the family. As I've mentioned before, Autumn weekends down here can be rough." link="vergelegen_camphors_20210523.jpg" >}}


## Fasted runs are not as scary as I thought {#fasted-runs-are-not-as-scary-as-i-thought}

At the time of drawing my [anti-breakfast line in the sand in WHV #221](/2021/04/20/weekly-head-voices-221-anti-breakfast-club/#skip-you-some-breakfast-for-great-good), I did
still make the exception of eating a banana or three before a morning run, with
the reasoning that I would burn through much of the resultant glucose during
the run, and that runs without all those sweet sweet carbs were probably
quite difficult.

However, shortly after publishing that post, I decided that I would like to put
even more money where my mouth is, and started doing morning runs in the fasted
state.

I am happy to report that not only are fasted runs not scary at all, they are
actually quite enjoyable.

There's no recently ingested food jostling around in your insides, which means
one less distraction from focusing on the running.

Perhaps most importantly, perceived energy did not seem to be a problem at all,
at least for the runs of up to an hour and a half that I have tried, some of
them over lunch time.

(It's possible that glycogen stores from the previous day were still
sufficient. I'm hoping that at least some of those highly energy-dense fat
cells were involved. [This blog post about fasting and exercise](https://www.dietdoctor.com/fasting-and-exercise) is a good read
and clearly explains the relevant concepts.)

I do need to caveat all of this with the remark that all of these runs have
been in the relative cool of autumn. I don't know (yet) how a longer, much more
sweaty run will go in the fasted state.

Stay tuned for the next few months to find out!

NB: Please see [Pieter's comments below](./#isso-2776). The text above is me talking about how
I experience my training (non-race) runs in the fasted state. If you decide to
exert yourself in the fasted state, please be careful, read what you can, and
measure carefully how your body responds to smaller doses initially.


## Yarn PnP will rescue you from `node_modules` hell {#yarn-pnp-will-rescue-you-from-node-modules-hell}

_NERD WARNING: `if not(nerd) skip_section();`_

The other day as I opened a laptop after having worked on the new zen machine
(see below) setting up some of our frontend development environments, its tiny
little metal frame almost creaked as dropbox started syncing, on all cores, the
many thousands of files from one of the cursed `node_modules` directories that
I had forgotten to exclude from syncing on the new machine.

My thoughts at that moment: "YARGH! THAT DOES IT! we're going to try that shiny
new thing that we have been avoiding because the current solution was OK until
it absolutely wasn't."

That new thing is [Yarn 2's PnP](https://yarnpkg.com/features/pnp).

(That page describes the various other issues with `node_modules`, besides your
laptop creaking.)

Instead of downloading a thousand dependencies and then unpacking those
thousand dependencies to easily one hundred thousand tiny little files, right
in your source directory (and that's `node_modules` folks!), PnP creates a
single `.pnp.js` file along with a local cache of the one thousand packages
which it keeps neatly zipped up.

In terms of numbers of tiny files, this is an improvement of one to two orders
of magnitude, which is significant. With `enableGlobalCache`, you can even move
these out of your source dir, keeping just the `.pnp.js`.

In addition to this, because of this new structure, the PnP can be much more
strict in resolving dependencies, resulting in builds that are **actually**
reproducible.

I followed [the step-by-step instructions for migrating the project in question
to Yarn PnP](https://yarnpkg.com/getting-started/migration), and before you could say dependency-resolution 58 times, the
project in question was cured of the hundred thousand file problem, and IDEs
like Visual Studio Code or any of the JetBrains family were perfectly capable
of navigating through the new dependency structure, right down to lines of code
inside the package zips.

Based on this experience, and the momentum and support that PnP has, my advice
is to convert at your soonest convenience.

The feeling of relief and increased build speed are worth it!


## New machine zen {#new-machine-zen}

The tradition around here is to write something about any new computers in the
family.

However, as this new one was not entirely planned, I almost wanted to keep it a
secret.

Weird instinct that.

As a compromise, I'll hide it in this section down here.

So, as I said, I was not yet planning to get a new workstation to complement
the [the new M1-powered mobile device](https://cpbotha.net/2021/03/21/new-emacs-capable-hardware-m1-macbook-air/), because [the ThinkPad](/2019/04/27/new-laptop-2019/) is still a very
capable machine.

However, [the new AMD Zen3 architecture](https://en.wikipedia.org/wiki/Zen%5F3) was proving far too hard for me to
resist, and so I started _fantasy_ shopping for my next Zen3-powered workstation.

This continued for quite a while in the evenings, with me swapping in and out
different components in my local retailer's online shop, reading reviews, and
generally enjoying the process of putting together my _imaginary_ workstation,
with real parts, from a real store, and with the fairly specific rule (for some
or other reason) that I could only use parts that were in stock at the retailer
in question...

What could possibly go wrong, right?!

Well, what could go wrong, is that I'm typing these words on a new Zen3
workstation with 12 cores (24 threads, I think you can guess the chip now?), a
really fast PCIe 4.0 SSD (around 7Gbytes/s read and write) and the "old"
RTX2070 GPU salvaged from the upgraded [meepz97, the desktop that joined this
club back in 2015](/2015/02/15/meepz97-i-haz-a-new-computar-machine/).

(Back then the Samsung 850 Pro was indeed "STUPID FAST" at about 500MB/s. The
new drive, Sabrent's Rocket 4 Plus, is 7 times that speed, and 4 times as
large.)

Just a few years back, this sort of raw computing power could only be found in
well-guarded and relatively secret government facilities.

Now all of that is standing on my desk, running Emacs, a 40 year old text
editor.

Although getting my old friend Emacs running smoothly on [the bleeding edge WSLg](https://github.com/microsoft/wslg)
has been causing a great deal of teeth gnashing, and although clearly many
other things have changed since then, I would like to conclude this post in the
same way as [the one for meepz97](/2015/02/15/meepz97-i-haz-a-new-computar-machine/#are-you-happy-now):


## Are you happy now? {#are-you-happy-now}

Yes.
