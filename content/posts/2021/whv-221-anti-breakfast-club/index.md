+++
title = "Weekly Head Voices #221: The anti-breakfast club"
date = 2021-04-20T08:54:00+02:00
lastmod = 2021-04-20T08:54:56+02:00
slug = "weekly-head-voices-221-anti-breakfast-club"
tags = ["breakfast", "erlang", "fasting", "health", "time-restricted eating", "TRE"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
ogimage = "vergelegen_entrance_autumn_run_202104.jpg"
org = true
+++

Hello there friends, and welcome to Weekly Head Voices #221, covering the week
from Monday April 12 to Sunday April 18, 2021, and focusing on the programming
language Erlang and the evil that is breakfast.

{{< figure src="vergelegen_entrance_autumn_run_202104.jpg" caption="Figure 1: Entrance to Vergelegen and Morgenster, taken during an Autumn morning long(er) run. I'm three bananas strong." link="vergelegen_entrance_autumn_run_202104.jpg" >}}


## Learn you a tiny bit of Erlang for Great Good! {#learn-you-a-tiny-bit-of-erlang-for-great-good}

Last week I attended a meetup that turned out to be primarily about Erlang and
not so much about automated crypto arbitrage, the other topic of the
talk. Although it's interesting to me that we have a company right here in
this town that has been successfully doing automated crypto arbitrage for a few
years now, using Erlang!

Like many other folks, I became interested in Erlang back in 2013 (I just
checked my notes, but it was also [mentioned on this blog in 2014](/2014/04/21/weekly-head-voices-68-harsh-autumn-weekends/), when I
decided not to learn it) when WhatsApp started becoming well-known. The
WhatsApp backend was famously implemented in Erlang, enabling them to handle
hundreds of millions, and now billions, of users with relatively little
resources.

The first two hours of the talk was a detailed intro to Erlang that did require
a substantial amount focus and grit to keep up with.

However, understanding how light-weight Erlang processes work and talk to each
other was quite interesting. More importantly the speaker both really knew what
he was talking about, and spoke really well.

The last 20 minutes or so after that were great, more about how and why exactly
Shiftly uses Erlang to do their real-time crypto arbitrage.

Their Erlang system is self-healing (when one of the light-weight processes
dies, for whatever reason, its supervisor simply replaces it; there are
supervisors watching the other supervisors!), and usually runs for years on
end, keeping all of its state in memory. They usually only have to stop it to
perform security upgrades on the underlying operating system.

Erlang processes pull in feeds from forex and various other suppliers, monitor
order books in real-time, and then execute movements on crypto trading pairs
that are affected by any order book entry.

My main take-home was that Erlang seems to combine super light-weight processes
(you can run millions of them on a single machine) that are fully isolated (a
process can divide by zero, be killed and a new one takes its place) but can
still easily share code and data via messages.

It seems like the antithesis to the sticky and sometimes over-complicated
micro-services situation we have collectively gotten ourselves into.

All of that being said, the same caveats apply as using another actor platform
like akka.net for example: Everything is unicorns and rainbows if you stay
within the lines (i.e. strict Erlang, or pure .NET managed code in akka's
case).

When you start adding native code, things can still go quite badly awry.

Still, the Erlang actor-based approach to writing highly concurrent and
fault-tolerant code sure looks amazing!


## I really don't like breakfast {#i-really-don-t-like-breakfast}

Some of my friends know that I've been quite angry at breakfast for a while
now.

I'm referring specifically to the idea that has been quite successfully
propagated by the makers of breakfast cereal for as long as I can remember:

> Breakfast is the most important meal of the day.

So they really want you to eat their usually sugar-filled products first thing
in the morning, and they've convinced you, and most of the "field", that this
is healthy.


### Eating causes inflammation {#eating-causes-inflammation}

What many people don't realise, is that every single meal causes inflammation.

Postprandial inflammation, as this is called, is your body's normal response to
any foreign material entering its systems.

Refined foods, and especially sugar, cause much more inflammation per volume
than natural foods, such as fruit and vegetables. Some food types even
counteract the inflammation to a certain extent.

Can you see where this is going?

A few hours after dinner you go to bed, your body still dealing with
the inflammation caused by that dinner.

You _hopefully_ sleep for 8 hours or more, and your body finally gets a break.


### The problem with breakfast {#the-problem-with-breakfast}

What do you do when you get up? You eat breakfast, because it's entrenched in
your brain (thanks to years of marketing) that breakfast is healthy and should
not be skipped, instead starting up a full day's inflammation again.

[This article in Nutrition & Metabolism](https://nutritionandmetabolism.biomedcentral.com/articles/10.1186/s12986-016-0142-6) describes the phenomenon quite nicely:

> The typical Western diet is characterized by sizable portions of highly
> processed foods, large amounts of added sugars, and a high total fat
> content. The average fat content of a Western meal is between 20 and 40 g, and
> three to four meals per day are consumed regularly. Therefore, many individuals
> spend the majority of their day in a postprandial state, characterized by
> elevated levels of circulating triglycerides (TRG) following a meal.

Chronic low-grade inflammation is associated with metabolic disorders that
include obesity, type 2 diabeters and the metabolic syndrome. Furthermore, [low
inflammation predicts successful ageing](https://pubmed.ncbi.nlm.nih.gov/26629551/).

In short, we want as little as possible inflammation, not more.

There are fortunately a few great ways to mitigate feeding's role in
inflammation: 1. Eat the best food you can find, 2. eat less food and,
importantly, 3. try not to eat for the whole dang day.

My anger at breakfast and its cereal-maker proponents is because they have
sabotaged point 3 above, sending a large part of the western populace into
glucose metabolism and inflammation every single morning.


### Skip you some breakfast for great good {#skip-you-some-breakfast-for-great-good}

This [blog post on time-restricted eating](https://www.dietdoctor.com/intermittent-fasting/time-restricted-eating) is definitely worth your time. Here I
would like to reproduce what it has to say about breakfast:

> We have all been told to eat breakfast. Unfortunately this is inaccurate
> advice.
>
> When you first wake up in the morning, your insulin level is quite low and most
> people are just starting to enter the fasted state, 12 hours after eating the
> last meal of the previous day. Eating at this time raises insulin and glucose
> and immediately shuts off fat-burning. This is especially true for a high carb
> breakfast. A potentially better choice would be to push the first meal of your
> day out at least a few hours, during which time you can continue in the fasted
> state and burn stored body fat.
>
> Interestingly, many properly fat-adapted people aren't very hungry in the
> morning and have no problem skipping breakfast.

From personal experience I can confirm this: I usually don't get hungry _at
all_ until lunch-time, at the earliest.

(If I'm planning to go on a morning run, I will usually eat a few bananas right
before the outing to be able to keep up a higher pace. I have also run fasted,
but in that case my pace is automatically more relaxed.)

In this context, it's interesting to look at [Peter Attia's nutritional
framework](https://peterattiamd.com/my-nutritional-framework/) as well. He refers to eating less, eating specific things and
restricting when you eat as three levers that have to be regularly
pulled.

Pulling these levers helps your body to become metabolically flexible, that is,
being able to switch easily between glucose burning and fat burning, the latter
of which many western humans are not capable of anymore.

It is interesting in this regard that our brains, although they can run on fat
when required, strongly prefer glucose (source: fascinating podcast episode
["Hussein Yassine, M.D.: Deep dive into the 'Alzheimer’s gene' (APOE), brain
health, and omega-3s"](https://peterattiamd.com/husseinyassine/)). I'm still working out the implications of this on my
personal intellectual requirements.

Ok friends, thank you for sticking around for this sermon!

Next week: A whole bunch of information that in fact does constitue financial
and investment advice that I take full responsibility for. (haha just
joking. it'll be politics or religion.)
