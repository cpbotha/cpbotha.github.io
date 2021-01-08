+++
title = "Weekly Head Voices #206: Mount Ceder"
date = 2020-10-10T13:10:00+02:00
lastmod = 2020-10-10T13:34:40+02:00
slug = "weekly-head-voices-206-mount-ceder"
tags = ["101 mind-tricks", "cederberg", "conference", "distraction", "focus", "mindfulness", "vcbm", "wsl"]
categories = ["weekly head voices"]
draft = false
ogimage = "mount_ceder_4873_pano.jpg"
org = true
+++

{{< figure src="mount_ceder_4873_pano.jpg" caption="Figure 1: A view from a run with GOU#1 in Mount Ceder." link="mount_ceder_4873_pano.jpg" >}}

Welcome, dear readers, to the 206th edition of the Weekly Head Voices, covering
the two weeks from Monday September 21 to Sunday October 4, 2020.


## Mount Ceder beauty {#mount-ceder-beauty}

The weather prediction for the September 25 long weekend did not look good at
all.

Temperatures in the low single digits, and rain.

We were unable to reschedule our reservation, and so, with significant
trepidation, we packed our things for the weekend and made the drive to Mount
Ceder.

As we entered the valley right before arriving at our destination, the rugged
and wonderful beauty of the surroundings quickly started dispelling our puny
expectations.

The weather did turn out almost exactly as was predicted, but our time there
ended up being the brilliant opposite of what we had feared.

In between spells of rain, there was plenty of fresh sunshine outside, with a
super effective little closed combustion fireplace inside the house to keep it
toasty.

{{< figure src="mount_ceder_4883_pano_from_hike.jpg" caption="Figure 2: View from a hike up the mountain with the whole fam-jam." link="mount_ceder_4883_pano_from_hike.jpg" >}}

The outside jacuzzi which we discovered late on the Saturday afternoon might
also have played a role in the amount of fun that was had.

It does also need to be said that the fact that there's no telephone reception
is a massive perk for us visitors.

The older I get, the more I enjoy disconnecting.


## VCBM 2020, virtually {#vcbm-2020-virtually}

Thanks to the modern miracle that is virtual conferences, I was able to attend
a large part of the [Visual Computing in Biology and Medicine (VCBM) 2020
conference](https://www.gcpr-vmv-vcbm-2020.uni-tuebingen.de/).

Although I am super interested in the themes and people of this conference, it
is _usually_ not possible for me to fly around the globe to take part in this
or any other relevant academic gathering.

However, the current pandemic has brought with it a whole host of changes, not
least of which is the concept of being able to participate, as a first class
citizen, in an international conference.

It was really great, although slightly nostalgic, connecting with friends and
colleagues from years ago.

Just being able to join in on the post-talk question sessions, and in the
surreal social rooms on discord where you find yourself in a grid of talking
heads, was super enjoyable.

(It has to be noted here that the technical aspects of VCBM 2020 were also
top-class. Everything, from the interactive block-based conference programme
with downloadable papers, to the youtube streams for each session, to the
discord channels for real-time discussion and the discord channels for social
video conferencing, was simply top notch!)


### Multi-tasking virtual meetings: Quo vadis? {#multi-tasking-virtual-meetings-quo-vadis}

What was also interesting to hear, was a possibly less positive aspect of
virtual conferencing, specifically that academic peeps were now in the
situation where they often had to multi-task whilst taking part in the
conference.

In the old days, pre-COVID, it could definitely happen that folks had to take
care of a few emails or perhaps even a video meeting, but the majority of the
day would be spent conferencing.

That is, people from potentially right around the globe would be chatting
face-to-face about anything and everything, an activity which is truly
important for collaboration, and friendship.

Now it seems that this ratio has changed, where most of the time folks are
expected to be available online for additional tasks and interactions, while
conferencing in parallel.

In my day job I've noticed a similar phenomenon, where one can often notice
that people taking part in a meeting are only partially present.

Whilst this is perhaps a good thing for a number of meetings that are by their
nature not that efficient, I think that it's a dangerous habit to
cultivate.

Imagine that by default, every meeting means your poor cognition trying to keep
up with multiple streams of information at the same time. Looking at it from a
different perspective, now you have even less confidence that your
collaborators are paying attention to what is being discussed.

This might be yet another reason to [favour asynchronous offline communication](/2020/09/20/weekly-head-voices-205-real-time-sometimes-async-most-of-the-time/#the-future-of-work-episode-23),
that is, writing long-form messages on message boards, with synchronous
face-time being reserved more and more for purely social reasons.


## On Thursday October 1, too much distraction was too much {#on-thursday-october-1-too-much-distraction-was-too-much}

Seguing right on from the synchronous communication point above, On October 1 I
unfortunately needed to be jacked-in to Teams, WhatsApp _and_ Discord for the
whole day, for various good reasons.

It was only around 16:20 that I was able to snap out of all of this and jack
out again, with [Lazar Focus](https://lazarfocused.com/) helping to bring a bit of welcome rest and,
surprise(!), focus.

Before that, anxiety about possibly missing something kept me from plugging out
for even short bursts to be able to do work.

It's funny how the expectations, real or perhaps more often just perceived, of
one's surroundings make it extremely difficult to disconnect, which leads to
more time lost to these various forms of distraction, which leads to further
anxiety, which further complicates just taking those few steps back and pulling
the plug.

I wish I had a trick to manage all of this better.


## That time I nuked all of my computers with a partition resize and move that should have taken no more than 5 minutes {#that-time-i-nuked-all-of-my-computers-with-a-partition-resize-and-move-that-should-have-taken-no-more-than-5-minutes}

_Massive nerd warning: If you don't want to know about filesystems, feel free_
_to skip this section. Before you do however, take this advice from me: Avoid_
_AOMEI._

My goal was simple: Move the newly appeared recovery partition (in addition to
the one at the start of the disk) to its end, so that I can grow my main system
partition to fill the available space on the drive.

Some years ago I had used EaseUs for something similar, but they wanted payment
for this task, and current reviews were pointing quite convincingly in the
direction of AOMEI.

Narrator: _The reviews were all tragically wrong._

My specific use case is even documented exactly on the AOMEI website, see [this
page](https://www.diskpart.com/windows-10/windows-10-move-recovery-partition-4348.html).

I followed those steps exactly.

My computer rebooted twice in order to perform the two actions:

1.  move recovery partition, and
2.  resize system partition...

... to conclude finally by leaving my laptop in a 100% unusable state.

No boot, no nothing.

I tried various combinations of booting into safe mode, which worked at first
but showed me the full drive's space available, meaning that the filesystem had
probably been damaged.

Hard.

I later booted with Windows installation media, from where I launched various
rescue attempts, including the stalwart `bootrec /rebuildbcd` and all of its
friends.

Nothing.

AOMEI had done a pretty great job in completely destroying my partition table
and filesystem.

Narrator: _He got what he paid for!_

I ended up installing Windows 10 twice, the second time with the
soon-to-be-released 20H2 install media, because installing the old 1909 and
then upgrading was taking far too long.

The whole exercise, or should I say "lesson", cost me about a day.

Stoic narrator: _Fortunately, the situation afterwards was better than it was before._

-   My main WSL2 ubuntu 20.04 image, where most of my development work happens,
    remained untouched on the second SSD and was up and running pretty quickly
    after the Windows re-install.
-   My backups demonstrably work, although Windows File History is truly klunky
    compared to Apple's Time Machine.
-   In the chaos of trying to get my work environment back up and running, I also
    had to upgrade my deep learning Linux desktop machine to Ubuntu 20.04. (It
    started as a Murphy's law situation, where both my laptop _and_ the desktop
    were unusable, the latter due to a stupid Ubuntu bug manifesting as a
    non-working keyboard)
-   A fresh install of Windows feels really fresh.


## My mind is a slippery eel {#my-mind-is-a-slippery-eel}

Recently I had to work on a chunk of software system design.

It starts with nothing laid down, just a general idea of what this pretty
significant feature should be able to do.

Pulling yourself up by your bootstraps, you have to start laying down the
bottom-most levels of the design that will eventually be able to make those
high-level desired features a reality.

This whole growing [Rube Goldberg machine](https://en.wikipedia.org/wiki/Rube%5FGoldberg%5Fmachine) has to stay in your mind for a large
part of the day, as you're mentally twisting, turning and replacing bits here
and there.

Most of these days, getting my brain to stay focused felt a lot like trying to
hold on to a really slippery eel, and, if that wasn't tricky enough, trying to
aim the sporadically working laser, badly mounted on its slippery head, to try
and carve something recognisable from a block of slowly melting ice.

By the end of most days, it would mostly not feel like it had been very
productive.

I tried to make peace with the fact that some sorts of work, coupled with all
of the usual emotional interactions, would often result in this sort of
feeling.

In that moment, this did also help me to get back into the habit of daily
meditation practice. Fortunately there's [the Waking Up app by Sam Harris](https://www.wakingup.com/) which
is perfect for this. Using this, I am usually able to squeeze in a 10 minute
practice before work starts, which subjectively seems to bring a little more
equanimity into each day.

Looking back at this experience now, it also seems like a strong vote for
paying more attention to the daily "done" list.

Although I mostly remember to journal every day, I often forget to look at it
also from the perspective of compactly listing the little tasks that have been
completed.

This could be tricky when working on an amorphous project like "design this
vague thing", but I think that it's more about the ritual of formulating and
then reviewing a small but plausible thing that is now apparently done.

This seems to fool the anxious parts of one's brain into a semblance of
temporary calm, enabling some of the other parts to get back to work.

This too I shall file this under ["101 stupid but effective tricks to fool your
mind into being more useful"](/tags/101-mind-tricks).

P.S. I just discovered that some part of [January-2019-Charl already did](/2019/01/26/weekly-head-voices-160-write-stuff-down/#do-you-write-stuff-down).

P.P.S. "Fool your mind", although it sounds much less awesome than "free your
mind", seems to be a recurring aspect of effectively operating the human
machine.
