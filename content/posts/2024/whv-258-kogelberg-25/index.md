---
title: "Weekly Head Voices #258: Kogelberg 25"
slug: weekly-head-voices-258-kogelberg-25
author: "Charl P. Botha"
date: 2024-12-19T16:38:35+02:00
draft: false
tags: 
 - anniversary
 - disconnecting
 - kogelberg
 - life partner
 - running
 - similarity
categories: ["weekly head voices"]
type: "post"
# EXCEPTION: keep ogimage as jpg, og.html will convert this to webp when resizing
# DO NOT use .webp here, then you'll git the golang / hugo webp decoding bug
# for the rest of the post, use webp, but keep a same-named jpg/png ok?
ogimage: "palmiet_route.jpg"
---

Welcome everyone to one of the final WHVs of the year!

This one covers the period of time from Monday 9 December to Friday December 20 of the year 2024.

{{< figure src="palmiet_route.webp" link="palmiet_route.webp" caption="Scene from an extremely special hike up the Palmiet river." >}}

## Kogelberg Anniversary

My life partner and I very recently achieved a quarter century of official togetherness.

While we usually do like to do some sort of [hike together to celebrate](/2019/12/18/weekly-head-voices-186-helderberg-20/#anniversary-walk-up-the-mountain), this time due to the significance of the number we wanted to do something a little more special.

After a search to the West, in the direction of Cape Town, did not yield anything special enough that would not require us to re-mortgage our house, we looked to the East, and soon landed on [the Kogelberg Nature Reserve](https://en.wikipedia.org/wiki/Kogelberg_Nature_Reserve) and more specifically the [Oudebosch Eco Cabins](https://www.capenature.co.za/accommodation/oudebosch-eco-cabins), and even more specifically the cabin named *Everlasting Daisy*, off to the side, right on top of the Kogelberg trail.

After the mad rush to get there before the very strict 16:00 cut-off (note!), during which I went into substantial good karma debt navigating slow traffic and stop-n-go situations on the otherwise beautiful [Clarence drive](/tags/clarence-drive/), the arrival inside Kogelberg, after losing all cell phone reception as we descended into the valley, was positively serene.

{{< figure caption="A small part of the view from the Everlasting Daisy eco-cabin" src="everlasting_daisy.webp" link="everlasting_daisy.webp" >}}

It bears repeating here that the switch-over into serenity was almost instant, and it was complete.

I guess being "forcibly" disconnected from the information highway and then being so gently but utterly enfolded by the majesty of nature might have that effect... we will have to go back.

After an absolutely brilliant sunset together, and then falling asleep with the stars and the moon and the quiet pouring in through the large windows, we woke up to some light rain.

This was perfect for our laid-back breakfast,  and it meant that the first part of our hike up the Palmiet river was pleasantly cool.

The views up the river, and then back down with the jeep track were stunning.

In the end, that hike was also *just right*.

When we finally left for home (with a lunch stop at [Café Zest](/2024/01/07/daily-head-voices-2024-01-05/) of course), it really felt like we had spent much more time than that single night and day in the Kogelberg state of calm.

## Similar blog posts based on chunk embedding similarity

Probably due to a much delayed echo of my experience writing the [WHV #256](/2024/11/24/weekly-head-voices-256-word/#shielding-you-from-the-equal-odds-rule) bit about why most of these posts were always going to be just average:

> (Now that I write this, I’m sure I must have mentioned this before on this blog… can you help me find the post(s) in question?)

... on Monday December 9 I briefly looked into finding existing tools that could rummage through the whole WHV post archive, but through the actual sections and not the complete posts, in order to find previous writings that are thematically similar to something I'm currently working on.

After a brief search did not turn up a ready-made tool, I wisely opted to write up the idea in a note titled *Idea: Hugo blog post similarity search* and then walked away from that text analysis catnip.

... until Monday December 16, a vacation day, when I could "quickly" dive in!

You can see [the bluesky thread](https://bsky.app/profile/charlbotha.com/post/3ldfrgk6hik2z) as I got into it, or just [the finished product, named *md-similarity*, on github](https://github.com/cpbotha/md-similarity).

Trying this out on my original question, namely where and in what blog post did I maybe also talk about the general idea of having to produce a bunch of average output in order to have a few winners, we get the following output:

```shell-session
$ mdsim list-similar 2024/whv-256-word/index.md --section-regex "Shielding"
0.765 - 2020/whv-197-on-shipping-a-side-project/index.md - Weekly Head Voices #197: How to ship side-projects - Hello friends! 👉 ## Shielding you from the equal-odds rule
0.776 - 2019-02-06-weekly-head-voices-161-email-equilibrium.md - Weekly Head Voices #161: Email Equilibrium. - {< figure src="/wp-content/uploads/2019/02/screenshot_2019-01-31_06-16-47.png" link="/wp-content/uploads/2019/02/screenshot_2019-01-31_06-16-47.png" >}  👉 ## Shielding you from the equal-odds rule
0.780 - 2022/whv-245-this-too-shall-pass/index.md - Weekly Head Voices #245: This too shall pass - WELL HELLO EVERYONE and welcome back to the Weekly Head Voices, edition #245 to 👉 ## Shielding you from the equal-odds rule
0.785 - 2021/whv-236-surprising-power-of-consistent-chipping/index.md - Weekly Head Voices #236: The surprising power of consistent chipping - This 236th edition of the Weekly Head Voices looks back at the three (sorry!) 👉 ## Shielding you from the equal-odds rule
```

Of those four results, the third one, namely [the introductory section of WHV #256](/2022/08/09/weekly-head-voices-245-this-too-shall-pass/) from 2022, is exactly the sort of similar thought I was after.

I was not able to find that post without having to search many different key phrases.

This is one of the situations where modern embedding models shine: Retrieving text that's vaguely about the same idea. For my purpose here, I am more interested in serendipitous association rather than retrieval precision.

Rather serendipitously (I'm pushing it...), two days later [Jeremy Howard announced their new ModernBERT encoder-only model on Bluesky](https://bsky.app/profile/howard.fm/post/3ldod2afps62x). You can [read more on the huggingface blog](https://huggingface.co/blog/modernbert), but I find this development pretty exciting!

## The beginning of the end

I am currently in the extremely fortunate situation that every run day can be a long[^1] run day.

Although I now know that I'm not going to be able to hit my yearly distance goal, I am still planning to use the above-mentioned good fortune to get as close as I can before the brand new year release "2025" drops.

{{< figure src="bettys_run.webp" link="bettys_run.webp" >}}

[^1]: Ok ok I mean weekend-length!
