+++
title = "Weekly Head Voices #211: Table Mountain Run(ish)"
date = 2020-12-12T15:04:00+02:00
lastmod = 2021-11-15T21:25:16+02:00
slug = "weekly-head-voices-211-table-mountain-run-ish"
tags = ["advent of code", "mom", "nim-lang", "table mountain", "twitter"]
categories = ["weekly head voices"]
draft = false
ogimage = "table-mountain-20201204-pano.jpg"
org = true
+++

Welcome back to the Weekly Head Voices friends!

These ones, the two hundred and eleventh (haha, remember at school you always
wondered if anyone would ever really need to be able to write out numbers... IT
WAS ALL FOR ME) edition, will hopefully be talking more or less coherently
about events that took place during the two weeks from Monday November 23 to
Sunday December 6 of the year 2020.

{{< figure src="table-mountain-20201204-pano.jpg" caption="Figure 1: Not the worst spot to eat one's peanut butter sandwiches" link="table-mountain-20201204-pano.jpg" >}}


## Wetware checklist to bootstrap your software checklist {#wetware-checklist-to-bootstrap-your-software-checklist}

My [daily review](/2019/09/21/note-taking-strategy-2019/#daily-review) routine has been taking quite a beating.

The busier it gets, the more easily I somehow skip my whole daily review in the
morning thinking that I can better invest that time into just jumping on the
most urgent things first.

This is of course one of the stupidest things I can do at that point.

It doesn't help that the daily review contains quite a number of points I have
to take care of every morning.

So, what does one do to help sticking to your morning daily review habit?

Logically, one creates yet another, but this time smaller and hopefully more
robust, habit that triggers the larger habit!

(In the end, it's turtles all the way down in any case.)

The one redeeming factor in my morning routine has been the increasing
regularity of meditation exercise. (Thanks PK for putting me back on that
horse, or should I say [elephant](/2018/05/20/weekly-head-voices-143-the-rider-and-the-elephant/#shorter-focus-blocks-work-better), and thanks to Sam Harris and his Waking Up
app.)

What I've now added to my system is a smaller checklist with three items on it:

1.  [X] meditation
2.  [X] deep reading
3.  [X] planning: review + task setting

The difference is that this checkpoint now lives in my brain, and is much
harder to side-step. Also, because of the firmly embedded meditation kernel,
there's a bit of momentum to help me move on to items 2 and 3.

I sneaked in item 2, because reading is basically cheap but really powerful
cybernetic upgrades for normal humans, and I found that it nicely completes
this 30 minutes (or so) of quiet time in the morning before I start with work.

So far, this small addition to my firmware has made quite a positive impact,
although I have to admit that AoC (see further down) is temporarily interfering
with items 2 and/or 3.

Oh well, one just has to keep on keeping on.


## Someone is wrong on the internet, part 972387 {#someone-is-wrong-on-the-internet-part-972387}

Some of you (does 2 out of my total of 5 readers qualify as "some of you",
relatively speaking?) will remember that I sometimes have a fraught
relationship with people being wrong on the internet, or you could just look up
[WHV #76 to read about a previous episode](/2014/07/01/weekly-head-voices-76-someone-is-wrong-on-the-internet/).

Most recently, I was again trying spectacularly unsuccessfully to avoid
twitter, when I ran into a thread where people were arguing about wearing
facemasks or not in these times.

My plan was to pull myself away from my phone, then throw the phone into the
fire, and then start the BBQ, but unfortunately one of the persons who was
arguing on the wrong side carries the same name as I do.

Although I am the **one true Charl Botha**, as is confirmed by the world's
premier reference on everything Charl Botha, namely the website [charlbotha.com](https://charlbotha.com/),
I was still worried that someone somewhere might confuse me with the third-rate
Charl Botha who was putting his lack of humanity on display.

My initial reaction was to go in there with all of my verbal guns blazing in
order to correct the poor sod, and to ensure that people would see there were
more Charls, some of which were not _as_ bad, but fortunately some of the
psychology I have been absorbing from the literature kicked in on time and I
managed to limit my reply tweet to the fact that 1) I was in fact the real
Charl Botha (the one with a brain), and 2) that I thought one should wear a
mask because it's kind to other humans.

This made me think about the observation that mask deniers would always believe
that there were holes in the science of mask-wearing, when the most important
consideration comes down to the fact that even if mask-wearing helped your
fellow humans possibly only a little bit, it's already the kind thing to do.

After that, I made the following tweet to summarise my thinking on this topic:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Folks, remember that
of the 14 mask types tested in <a
href="https://t.co/BrQ6cpCnkk">https://t.co/BrQ6cpCnkk</a> (sensitive to
droplet size all the way down to 0.5um), 13 of them reduced droplet
transmission relative to no mask. SO: Be kind. Wear a multi-layer mask, reduce
droplets, help your fellow humans. <a
href="https://t.co/COyrdksV9K">pic.twitter.com/COyrdksV9K</a></p>&mdash; Charl
Botha 😷 #Masks4All (@cvoxel) <a
href="https://twitter.com/cvoxel/status/1332014932481732608?ref_src=twsrc%5Etfw">November
26, 2020</a></blockquote> <script async
src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

What I learned from this would-be altercation, is that it's better for me to
focus my someone-is-wrong-on-the-internet rage into something that's more
constructive:

Strip the issue down as far as you can. Inject information. Combine that with
the desire that many humans share for a society where we can all just get
along.

It's probably still not going to work, but just maybe, it'll cause less trouble
and result in a little bit more goodwill, and who knows where that may lead?

P.S. On the topic of mask-wearing: Even if there were no COVID-19, don't you
think we'd all be a little better of if the wearing of good masks became the
norm?

There are indications that [mask-wearing and physical distancing basically
stopped flu season in the Southern Hemisphere](https://www.scientificamerican.com/article/flu-season-never-came-to-the-southern-hemisphere1/).

> Never in my 40-year career have we ever seen rates ... so low
>
> -- Greg Poland, influenza expert at the Mayo Clinic


## Advent of Code 2020 {#advent-of-code-2020}

Thanks to this tweet by [@RameezKhanSA](https://twitter.com/RameezKhanSA):

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">My pledge this year is
to do the <a
href="https://twitter.com/hashtag/AdventOfCode?src=hash&amp;ref_src=twsrc%5Etfw">#AdventOfCode</a>
in <a
href="https://twitter.com/hashtag/Clojure?src=hash&amp;ref_src=twsrc%5Etfw">#Clojure</a>. Looking
forward to it. Already started doing some of last years challenges. Want to
keep it simple. No Leiningen just a plain deps.edn.</p>&mdash; Rameez
(@RameezKhanSA) <a
href="https://twitter.com/RameezKhanSA/status/1332692669190074370?ref_src=twsrc%5Etfw">November
28, 2020</a></blockquote> <script async
src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

... I am taking part, for the first time, in [the Advent of Code](https://adventofcode.com/)!

Nerds from the world over get a new two-part programming puzzle every day at 5
AM UTC, from December 1 to December 25, for a total of 50 puzzles.

The idea is that said nerds use any programming language, or combination of
programming languages, to solve the puzzles and enter the answers on the AoC
website.

The quickest nerds, the ones who manage to solve these puzzles in an amazing
minute or three, earn a highly-coveted place on the [leaderboard](https://adventofcode.com/2020/leaderboard).

Just like Rameez, I wanted to use the AoC to get to know a programming language
better, although in my case that language is Nim.

So far, this has been a great deal of fun!

To my non-programmer friends: Solving puzzles is like concentrated cat nip to
programmers. In the case of AoC, you get unadulterated puzzle solving, and none
of the other complications of writing production software.

Besides the fun, Nim _really_ shines at this. As I mentioned in [the previous
WHV](/2020/11/29/weekly-head-voices-210-miniburn-2020/#save-image-from-clipboard), Nim somehow manages to combine the expressivity and development velocity
of Python, with a great dollop of Python's famed batteries-included, with close
to the metal performance.

(My brain is currently spending background cycles figuring out if I could
somehow use this in a product.)

I am sort of expecting to drop out eventually, because, based on past years,
it's going to take up an increasing amount of time.

However, although I'm already happy with what I have (day 6's puzzles completed
on Sunday December 6, ostensibly the end of this WHV's window of reality), I
would be really chuffed reaching the double digits!

_Narrator: He ended up reaching the double digits._


## Table Mountain Run(ish) 2020 {#table-mountain-run--ish--2020}

We thought we were going to do a trail run up Skeleton Gorge.

Well, if one is us, one does not simply run up Skeleton Gorge. Instead, one
huffs and one puffs, for about a kilometre of ascent. It is a substantial
amount of huffing and puffing.

We did get to run on top of the mountain, from the beach at the top of Skeleton
Gorge (yes, there's a beach), to [Maclear's Beacon](https://en.wikipedia.org/wiki/Maclear%27s%5FBeacon), which I've now learned was
used in the calculation of the curvature of he Earth, to the old cable station,
past the reservoirs to end up walking really slowly back down Nursery Gorge.

It was an interesting observation that although I found parts of the route hard
and sometimes maybe even a little unpleasant (coming down Nursery Gorge...)
whilst in the thick of things, the whole memory of the experience started
transmogrifying into _wonderful_ verging on _magical_ extremely soon after we
had reached the finish.

12/10 would do again, but next time a more gradual descent please!


## Hi mom {#hi-mom}

My mom has now seen three quarters of a century.

I am happy to report that she is as fit as a fiddle. Genetics and some really
great habits are a really solid combination.

Importantly, we are truly fortunate to count her as an integral part of our
household.

(Them is some big words for: We have so much fun together! Our GOUs, who are
also her GOUs, will probably never forget these stories with their Oma.)

Here's to the next quarter century!

I've convinced her of the great business opportunity of publishing a book at
100 with tips and tricks for other (aspirant) centenarians, so she really needs
to remain as sharp and as fit as she is today!