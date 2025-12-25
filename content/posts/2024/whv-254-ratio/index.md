+++
title = "Weekly Head Voices #254: Ratio"
date = 2024-03-31T15:02:00+02:00
lastmod = 2024-04-01T13:21:22+02:00
slug = "weekly-head-voices-254-ratio"
tags = ["backyard philosophy", "garden route", "oliver burkeman", "omnivore", "productivity", "relationships", "st francis", "storms river", "wilderness"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
org = true
ogimage = "wilderness-view-from-the-views.jpg"
+++

Hello there WHV enjoyers, and welcome back! ...ish.

The last official WHV, by name, was [WHV #253, published on September 2, 2023](/2023/09/02/weekly-head-voices-253-weekend-warrior/), although the [2023 to 2024 transition post](/2024/01/04/the-2023-to-2024-transition-post/) certainly deserves its honorary WHV title.

In the meantime, I have been experimenting with the [Daily Head Voices / lifelogs](/categories/lifelog/), which was fun, but ultimately not sufficiently meaty to fill the WHV vacuum.

We are clearly going through a pretty significant WHV-hiatus.

Although I'm still not sure what the new stable state is going to be, I have _some_ extremely modest plans, and in addition to those I've decided to dust off and revive the draft of WHV #254 which was just lying there on my disc since September of last year, all languishing.

{{< figure src="wilderness-view-from-the-views.jpg" caption="<span class=\"figure-number\">Figure 1: </span>The view from our return-journey lunch at The Views in Wilderness was awe-inspiring." link="wilderness-view-from-the-views.jpg" >}}


## Easter break on the Garden Route {#easter-break-on-the-garden-route}

I'm typing these words on my laptop in the family car, moving back home along the N2 after an absolutely fabulous Easter break-away on the Garden Route.

Unfortunately, I have not yet figured out a safe way to drive and type at the same time, so my partner is graciously helping out with the driving bits during this shift.

GOU#1's exchange family "sister" from Germany is currently visiting, and so we have been doing our best to show her some of the best this amazing country has to offer.

Although this makes for a fairly jam-packed holiday programme (almost no time to work on hobby projects), it really has been loads of fun.

Some highlights (ask me in the comments if you're curious about anything):

-   Ebb &amp; Flow rest camp in Wilderness - one of my favourite running routes next to the Serpentine river
-   Sun-down at Salinas Beach restaurant in Wilderness
-   [Elephant encounters at the Knysna Elephant Park](https://knysnaelephantpark.co.za)
-   [Storms River Mouth rest camp (Tsitsikamma)](https://www.sanparks.org/parks/garden-route/camps/storms-river-mouth) - beauty all round, hikes over the hanging bridges up past the view point, also the start of the Otter trail at the other end of the camp
-   Lunch at The Views in Wilderness
-   St Francis, beautiful as always, with specific mention of Etienne's surfing lessons at the main beach for our teenagers, and the super entertaining St Francis Bay canal sunset cruise
-   We were absolutely blessed with balmy later summer weather, except for one rainy morning in Storms


## Two mention-worthy personal knowledge tools {#two-mention-worthy-personal-knowledge-tools}

As is traditional around these parts, we have this nerdy section surprise here to talk about software tools that I really like, after which there will be some backyard philosophy sections.


### miniflux {#miniflux}

My yearly [inoreader](https://www.inoreader.com) rss reader subscription was up for renewal.

It's a really fantastic product that I've been using (and paying for) for years as [a core part of my personal knowledge management approach](/2023/04/11/note-taking-strategy-2023/#mobile), but the renewal email and especially the price tag was a good reminder to review my options, especially since I already have an old Linux laptop serving [Pi-hole](https://pi-hole.net) for family-wide ad-blocking, and [Home Assistant](https://www.home-assistant.io) to track energy production and usage stats of some of our devices at home.

A few minutes of searching fortunately led me to [miniflux](https://miniflux.app), "a minimalist and opinionated feed reader". After a few more minutes, I had the docker-compose up and running (miniflux and postgres containers), and after some more minutes I had a [CloudFlare tunnel](https://www.cloudflare.com/en-gb/products/tunnel/) up so that I can easily access my miniflux's web UI from anywhere via an automatic Cloudflare-supplied SSL certificate. Finally, through the magic of OPML, it was straight-forward to move my 130+ feed subscriptions from inoreader to miniflux.

{{< figure src="screenshot-miniflux.png" caption="<span class=\"figure-number\">Figure 2: </span>miniflux often looks like this" link="screenshot-miniflux.png" >}}

I've been using this setup for the past week or two and so far it looks like a strong keeper!

miniflux has extensive keyboard support on the desktop, but it works great on mobile, which is where I mostly use it.

I really like its minimalism: It shows me a paged view of all my feeds (page size configurable), via which I can easily jump to the source page, or use miniflux's built-in reader mode, and also easily toggle the whole page as read before moving on to the next.

If you're in the market for a self-hosted RSS reader, take this as a strong recommendation for miniflux. Even if you don't want to self-host, [their $15 / year hosted offering](https://miniflux.app/hosting.html) is probably worth a look.


### omnivore {#omnivore}

After years of eschewing "read-it-later" apps like Pocket and friends for the more straight-forward but often klunky  ["just print to PDF and store" approach](/2019/03/21/weekly-head-voices-165-get-in-my-pocket/#replacing-pocket-with-just-a-bunch-of-pdfs-jbop), I had to give [omnivore](https://omnivore.app/) a go, as it offered native support to sync article highlights into Obsidian's markdown, and I thought that I would be able to use this for my Emacs setup as well.

I was indeed able to co-opt the Obsidian integration to get saved article highlights into my Emacs setup, but in the process fell completely for the omnivore app as a whole.

On mobile, which is where I use this most, I am able to import any web-page or post into omnivore with two taps.

On average, it does a great job of extracting the article contents and rendering it in a far more consistent and reading-friendly way.

One can make different coloured highlights in any article, and even add a note to each highlight.

Finally, it also imports PDFs with aplomb, and offers most of its functionality there. There are additional subtle delights, like the fact that you can double-tap on one column of a multi-column PDF, at which point omnivore will zoom to bring only that column into maximum width view.

{{< figure src="screenshot-omnivore-pdf-column-zoom.jpg" caption="<span class=\"figure-number\">Figure 3: </span>Vertically partial screenshot of Omnivore during PDF column zoom. Maps of Bounded Reality is a piece by the great Daniel Kahneman (1934-03-05 - 2024-03-27, rest in peace) which gives an overview of his and Amos Tversky's groundbreaking work making sense of human behaviour." width="320px" link="screenshot-omnivore-pdf-column-zoom.jpg" >}}

For me the only downside of omnivore is that it violates [both my single search interface and plain old files on local drives characteristics](/2023/04/11/note-taking-strategy-2023/#high-level-overview). However, both of these violations are partially mitigated by the aforementioned note-syncing feature. I don't really want to have **all** of my saved articles to be part of my database, so here I should make syncable highlights when something is important enough to go into the primary notes database.

After some months of use, I strongly recommend omnivore as your web-resource-ingestion-and-assimilation tool!


## The three-or-four hours rule for getting creative work done {#the-three-or-four-hours-rule-for-getting-creative-work-done}

Last year, I listened to a short piece by Oliver Burkeman, who has [featured on this blog a number of times](/tags/oliver-burkeman/), which made an impression on me. I made a note of it in the pre-hiatus draft of this post, and then promptly forgot about it.

The core of Burkeman's three-or-four hours rule, which you can [read more about on his website](https://www.oliverburkeman.com/fourhours), is summarised in the following quote:

> ... use whatever freedom you do have over your schedule not to "maximise your
> time" or "optimise your day", in some vague way, but specifically to ringfence
> three or four hours of undisturbed focus (ideally when your energy levels are
> highest).
>
> Stop assuming that the way to make progress on your most important projects is
> to work for longer. And drop the perfectionistic notion that emails, meetings,
> digital distractions and other interruptions ought ideally to be whittled away
> to practically nothing.
>
> Just focus on protecting four hours – and don't worry if the rest of the day is
> characterised by the usual scattered chaos.

I have definitely suffered from the "maximise your time" bug and can attest to its negative effects.

Burkeman suggests to worry only about a core few high-focus hours (he says 3 or 4, I think sometimes depending on your context, even 1 could work) and let the rest be what it wants to be.

I think this is a far better approach which strongly complements [the one main thing philosophy](/2021/01/26/weekly-head-voices-214-one-main-thing/#one-main-thing).

P.S. There's another important tenet of Burkeman's approach, which he talks about in his post linked above, and which also [featured in WHV #230, namely: Know how to put down your work](/2021/08/20/weekly-head-voices-230-follow-your-blisters/#know-how-to-put-down-your-work) (although I just noticed that back then I did not mention the chaos part...). In summary: Guard your focus hours, let "the chaos" fill the rest, but become really good at detaching and walking away at the end of the work day. Thank you [Noeska](http://noeskasmit.com) for the reminder!


## The Magic Relationship Ratio is 5 to 1 {#the-magic-relationship-ratio-is-5-to-1}

I really enjoyed the [fascinating podcast between Lex Fridman and Dr Shannon Curry](https://lexfridman.com/shannon-curry/), a clinical and forensic psychologist, titled "Johnny Depp &amp; Amber Heard Trial, Marriage, Dating &amp; Love", much of it in fact about human relationships ([textual summary here](https://www.podcastworld.io/episodes/366-shannon-curry-johnny-depp-amber-heard-trial-marriage-dat-sz9ltosy)).

Among the many practical and science-based topics that Dr Curry talked about, she mentioned the ["5 to 1magic relationship ratio"](https://www.gottman.com/blog/the-magic-relationship-ratio-according-science/), which refers to the observation that the interactions between happy couples tend to consist of at least 5 positive interactions for each negative interaction.

It should come as no surprise that being able to spend decades together in a permanent state of happiness, by definition continuously facing various internal and external stressors in an often resource-constrained environment, is probably not realistic.

Thus I really like that this observation runs with the knowledge that almost no-one is going to get this right, and that the smart approach is instead to accept that and focus on what you can attain, namely, that more practical but still ambitious 5 to 1 ratio.


## Ratio {#ratio}

This is the part of the post where I try to tie up some of the threads, or at least justify the title.

Burkeman's three-or-four hours rule is all about working towards a practical and healthy _ratio_ between focus time and the rest of the daily chaos, instead of being continuously disappointed because it's not really possible to fill all of your days with pure focus hours.

The 5 to 1 ratio is the same: We make peace with reality, and work towards a healthy ratio between positive and negative interactions.

The third _ratio_ I want to mention here refers to the Dutch word "ratio" ([pronunciation)](https://nl.bab.la/uitspraak/nederlands/ratio), one of whose definitions is "reason" or "logic", or more idiomatically, the noun corresponding to adjective "rationeel", which is the same as the English "rational".

As with all things language, the use of this word implies subtle little differences. Whatever the case may be, I was delighted when I discovered that the Dutch had adopted the original Latin for this. To me it felt like that meant there was a special place for and focus on _ratio_ in their world.

With that trifecta (a neologism, I just learned, for contrast!) of _ratio_ examples, I think that I can now conclude this post with the earnest wish, for you and for me, that we are able to instantiate, maintain and propagate superb levels of _ratio_.
