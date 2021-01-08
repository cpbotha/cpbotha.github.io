+++
title = "Weekly Head Voices #204: What is your purpose?"
date = 2020-09-16T22:22:00+02:00
lastmod = 2020-09-17T09:55:59+02:00
slug = "weekly-head-voices-204-what-is-your-purpose"
tags = ["altra", "backyard philosophy", "emacs", "goals", "keyboards", "purpose", "sleep", "wsl"]
categories = ["weekly head voices"]
draft = false
ogimage = "guardian_peak_20200910_cpb_cfs_1280.jpg"
org = true
+++

Welcome back here folks, to the 204th edition of the Weekly Head Voices,
examining a sample of life from Monday September 7 to Sunday September
13, 2020.

Summer is starting to make an appearance down here, albeit with a bit more
subtlety, some would say difficulty, than usual.

Fortunately, the week in question offered plenty of opportunities for being
outside, opportunities that some of us made grateful use of.

{{< figure src="guardian_peak_20200910_cpb_cfs.jpg" caption="Figure 1: Random scene from a lunch at Guardian Peak with one of my most long-time friends who as a bonus is also brilliant company. What you see is the result of three iPhone photos stitched together with [Microsoft Research's Image Composite Editor](https://www.microsoft.com/en-us/research/product/computational-photography-applications/image-composite-editor/), and the power of math." link="guardian_peak_20200910_cpb_cfs.jpg" >}}


## Sleep update {#sleep-update}

With our teenager back in school, we have to get up at 5:45, mercifully only
for two days of the week with the school in COVID-19-mode.

On other days we get to sleep in until 6:45. LUXURY!

(The lock-down also saved us from a few months of 5:45 wake-ups 5 time per
week during the darkest part of the winter, so there's that.)

This, together with increased pressure at work, has again brought into sharp
focus my sleep hygiene.

I haven't been doing too badly during the past months, but the current period
seemed to require a tad more attention to good sleep.

After reading the disappointing news that the promised first-party (Apple, in
other words) sleep-tracking in the new WatchOS 6 release was not going to be
much more than tracking time in bed, I searched around for the best third-party
sleep tracking app.

Well folks, after a few weeks of testing, I think that [AutoSleep](http://autosleep.tantsissa.com/) is it!

(Beware, there's a straight rip-off app in the Google Play store. It's not even
in the same reality as the real thing, although the scammers have stolen a
bunch of visual elements and even copy from the real autosleep website. Oh
Android...)

The app appears to be almost too full of complicated-looking visual gizmos, so
much so that initially I was not as positive about it. See below for an example
of my sleep history overview:

{{< figure src="autosleep_screenshot.png" width="240px" link="autosleep_screenshot.png" >}}

However, after using it for a while, and coming to grips with the various
pieces of feedback, this app has turned out to be a great tool in my quest for
sleep hygiene nirvana.

Furthermore, I did have to change my watch charging habits by charging my watch
in the evening hours, so that I can sleep with it on my wrist, and I also have
to remember to tap the "lights out" button when I attempt to start my sleep
(you don't have to do this, but it gives more accurate tracking that way).

Now I have measurements to show how important the wind-down routine is (if I
can fit in some book-reading in bed, I can fall asleep after that in almost no
time); how some nights when it feels like I'm quite restless, I actually do get
quite an amount of sleep; and finally how a drink or two on a weekend night can
affect my average heart rate through the night (+5 beats, oof), and more.


## WSL2 and nativecomp Emacs workflow update {#wsl2-and-nativecomp-emacs-workflow-update}

The following is for my more nerdy readers.

After running into [this comment](https://github.com/microsoft/WSL/issues/4619#issuecomment-678652118) on a github issue I am subscribed to, I learned
that you can use the versatile [socat](http://www.dest-unreach.org/socat/) tool to forward connections from a unix
socket on WSL2, via the WSL bridge and a WSL1 instance, to a TCP port on
localhost.

The upshot of this is that I now have a robust X11 connection from WSL2 to X410
running on my Windows laptop.

This is possible without socat, but you either need to forward ports using SSH
(which I've done), or punch holes in the firewall, and then, as if that's not
bad enough, deal with a connection that breaks every time the laptop goes into
suspend.

With the socat X11 connection in place, I decided that it was time to go
further around the WSL2 bend and replace my complicated rsync-based scripts for
copying source code from the Windows host to the WSL2-native filesystem with a
second instance of dropbox running directly on WSL2, with a severe selective
sync configuration.

By the way, after [Dropbox rewrote their sync engine (in Rust)](https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine), nothing else
even comes close in terms of performance.

Thanks to this perfect storm of socat-X11-boosted WSL2 and MULTI-dropbox, I
decided that it was finally time to commit to [the new nativecomp Emacs "capable
of compiling and running Emacs Lisp as native code"](https://akrl.sdf.org/gccemacs.html), so I busted out my
slightly modified version of [Mickey Petersen's](https://masteringemacs.org/article/speed-up-emacs-libjansson-native-elisp-compilation) Dockerfile and compiled me one.

This very post is being written on native-compiled Emacs Lisp, running on WSL2,
displaying via socat to X410.

`#feelsgoodman`

(P.S. I've been running like this for about three weeks, with nary an
issue. The future is now.)


## Keyboard update: Unicorns-with-RGB {#keyboard-update-unicorns-with-rgb}

You might remember from [WHV #200 how I carefully started dipping my toes in the
clickity-clackety waters of mechanical keyboards](/2020/07/19/weekly-head-voices-200-we-are-extremely-pleased-to-be-here/#my-attempt-at-dipping-my-toes-carefully-into-the-world-of-mechanical-keyboards) by acquiring a cheap keyboard
with hot-swappable [Outemu blue switches](https://input.club/the-comparative-guide-to-mechanical-switches/tactile-clicky/outemu-blue/).

What I did not tell you then, was that shortly after acquiring that keyboard, I
had already ordered the [Womier K87 all-acrylic RGB-overload keyboard](https://youtu.be/e9gRESbY-e8) from
Banggood.

My reason for ordering that specific board was not so much the lighting (WHICH
IS FREAKING SPECTACULAR BUT BACK THEN I DID NOT KNOW THIS), but rather because
it was the most affordable mechanical keyboard with universal(-ish)
hotswappable switches.

You see, the Outemu board can only take Outemu switches, while with a board
with universal sockets, you have access to a whole smorgas(key)bord of
different switches!

The Womier finally arrived after slightly more than a month, with [Gateron brown
switches](https://input.club/the-comparative-guide-to-mechanical-switches/tactile/gateron-brown/) installed as I had requested.

Probably due to both the brown switches (rated 45g actuation force but probably
less, tactile but not clicky) and due to the board's far more solid
composition, my typing comfort and speed on this thing are close to what I
usually have on my Microsoft Sculpt ergonomic.

Because of this, I don't swap back to the Sculpt nearly as often.

Together with the fact that the keyboard has an impressive and varied
collection of intricate animated lighting patterns thanks to the RGB LED behind
each and every single key, and a whole bunch of extra LEDs in the acrylic body,
this leads to a great deal of typing fun.

`#feelsbrightman`


## Running update {#running-update}

Back in [WHV #177](/2019/09/09/weekly-head-voices-177-streakers/) I embraced the space and acquired my first pair of Altras, a
pair of road shoes named Escalante 1.0, for a good price, because the 1.5 had
already been released.

Recently I was again in the fortunate position to buy a pair of 1.5s for a good
price, as, you guessed it, the 2.0 had already been released.

The new babies look like this:

{{< figure src="altra_escalante_1.5.jpg" link="altra_escalante_1.5.jpg" >}}

Running in them has been super enjoyable.

(The 1.0s are at about 700km, which is usually a good time to retire them from
running. Now they are just for cocktail parties and business meetings.)

On a more philosophical note, with the aforementioned improving weather, the
aforementioned increased pressure at work, and the non-aforementioned abundance
of mountains all around me, I have taken to randomly taking a few hours off
from aforementioned work to go run in the now aforementioned mountains.

`#feelslifeaffirmingman`


## What is your purpose? {#what-is-your-purpose}

We have a great tradition here at the WHV of revising our official and utterly
complete life philosophy based on discussions with wise friends.

See for example [WHV #124](/2017/07/30/weekly-head-voices-124-ceci-nest-pas-dennui/) where I had to add a third rule to _WHV's Two Rules
for Achieving Great Success in Life, or Just Surviving, Whichever Comes First_.

Quite poetically, the additional rule was "Evolve".

(FYI, the current official WHV approach to life, the universe and everyhing is
summarised in [WHV #198](/2020/06/16/weekly-head-voices-198-short-update-for-future-me/#post-scriptum-the-whv-approach-to-life-the-universe-and-everything).)

During the beautifully-surrounded lunch discussion with longest-time friend
(LTF, henceforth), as depicted in the panoramic photo at the start of this
post, we also spent some time talking about life directions vs. goals.

As you know, I am [not a fan of life goals, instead opting for life directions](/2012/01/28/slow-philosophy-weekly-head-voices-64/).

LTF agreed with some of my reasoning, but made the valid point that goals were
required to measure and maintain velocity along one's chosen directions, or
[systems](/2020/01/12/the-2019-to-2020-transition-post/#plans-and-life-directions-for-2020).

In principle we agree on this point also, but I believe that the conversation
will have to continue, as we still need to define and then articulate a
closed-form solution to the directions vs goals issue, or rather a guideline
that can be used to determine the correct relative dosage.

Probably more important was LTF's contribution of the concept of "purpose".

One could argue that life directions form one's purpose, but that would be
missing an opportunity I think.

As LTF later quipped:

> Purpose = the reason you get up in the morning. Goals = help you go to sleep at
> night.

At least in my case, I have a number of life directions, but I think a purpose
is a higher-level, mostly singular, desired outcome of your life's work.

Ideally, _life directions_ should be set in order to orient one towards
fulfilling one's _purpose_, with continuously evolving _goals_ punctuating the way
there.

What is _your_ purpose?
