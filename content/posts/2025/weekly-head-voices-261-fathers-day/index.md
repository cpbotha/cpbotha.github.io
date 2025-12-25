---
title: "Weekly Head Voices #261: Father's day"
slug: weekly-head-voices-261-fathers-day
author: "Charl P. Botha"
date: 2025-06-16T13:45:00+02:00
draft: false
tags:
  - clarence drive
  - fatherhood
  - fitness
  - gou-1
  - gou-2
  - gou-3
  - gous
  - obsidian
  - orgmode
  - productivity
categories: ["weekly head voices"]
type: "post"
# EXCEPTION: keep ogimage as jpg, og.html will convert this to webp when resizing
# DO NOT use .webp here, then you'll git the golang / hugo webp decoding bug
# for the rest of the post, use webp, but keep a same-named jpg/png ok?
ogimage: "20250428_clarence_pano.jpg"
---

This edition of the Weekly Head Voices covers the period from Tuesday, April 22 to Sunday, June 15, 2025.

{{< figure src="20250428_clarence_pano.webp" link="20250428_clarence_pano.webp" caption="Another beautiful view from Clarence Drive" >}}

> The real voyage of discovery consists not in seeking new landscapes, but in having new eyes.
>
> -- Marcel Proust

## Bliss

It's father's day today.

When I woke up and went to say good morning to Genetic Offspring Unit (GOU) #3, she gave me the card she made, with a rainbow and a red heart and a sweet hand-written message in 9-year-old Afrikaans.

Hearing that we were up, GOU #2 came out of her room, with a beautiful illustration she had made for (and of!) me. (GOU #2 has found her passion in drawing. She practises on most days, and her skill and talent are very obvious.)

Soon after, GOU #1 arrived home with flat whites (my favourite), fresh ciabatta and croissants from the bakery, and hugs.

What I'm trying to say here is that when your offspring units all tell you in their different ways that they appreciate you being their dad, when you're fundamentally dedicated to and deeply grateful for being just that, and those very offspring units constitute the whole focus of this important life endeavour, you better hope that you are able to keep those eyes dry.

## VO₂ Max redux

One of my [exercise goals for 2024](/2024/01/04/the-2023-to-2024-transition-post/#running-and-exercise) was to reach a VO₂ Max of at least (HAHAHA) 50.

I didn't make it in 2024, but I also didn't do anything other than just my normal running during the year. I know that I should probably engage in some high intensity interval training of some sort if I really want to move the needle, but I run because I like running and not because I want to be fit, although I do want to be fit. (It's complicated being a teenager.)

At the start of 2025, I stated, much more softly this time, that I would maybe [still like to hit that 50 VO₂ Max](/2025/01/19/the-2024-to-2025-transition-post/#running-and-exercise).

Again I realized I would have probably have to *do* something interval-ly about it, but again I kept on postponing.

WELL KIDS it turns out that postponing can also be a winning strategy! On Monday, May 19, my Garmin reported that I had indeed hit a VO₂ Max of 50, which, [according to its tables](https://www8.garmin.com/manuals/webhelp/GUID-C001C335-A8EC-4A41-AB0E-BAC434259F92/EN-US/GUID-1FBCCD9E-19E1-4E4C-BD60-1793B5B97EB3.html), places me at the bottom of the coveted top-most category for my age and gender, namely *Superior*.

I always knew it, but thanks anyways Garmin!

P.S. I do have to deflate my *superiority* a bit by reminding us all that, in addition to finding myself at the bottom of the superior range, I have also only recently entered my current age section, giving me an extra advantage. Jokes aside, 50 at 50 is not bad, so allow me to bask for a while.

## org-mode timestamps in obsidian

One feature I have really been missing in Obsidian since [my recent break-up with Org-mode](/2025/03/11/weekly-head-voices-259-backbone/#a-bientôt-monsieur-org) is the amazing org timestamps.

There is no real convention in Obsidian, whilst in Org-mode timestamps [are well-defined and quite functional](https://orgmode.org/manual/Timestamps.html). My "old" notes are scattered with them: time ranges, scheduled times, deadlines, random timestamps inside random text notes.

The time logging script [I mentioned previously](/2025/04/22/weekly-head-voices-260-not-your-guy-buddy/#loggin-time) made use of the dataview-convention of adding timestamps to work items for example:

```markdown
## theme 1
- project 1
  - task 1 (start:: 2025-05-20T07:55) - (end:: 2025-05-20T08:10)
```

... which did work but was no fun to work with.

Long story short, I could not resist for much longer, and so I hacked together a new Obsidian plugin called [Org timestamps](https://github.com/cpbotha/obsidian-org-timestamps).

As you can see in the comparative screenshots below, I've copied the org-mode timestamp and time range format verbatim, with the additional bonus of rendering these timestamps nicely in preview mode, inspired by [the Emacs package org-modern](https://github.com/minad/org-modern).

Deviating from org-mode proper, my plugin also renders date-less timestamps -- I often use these when adding entries to daily file. Speaking of which, full org timestamps can have `[[...]]` links around the date parts so that they link back to the relevant daily file.

{{< figure src="obsidian-org-timestamps.webp" link="obsidian-org-timestamps.webp" >}}

In addition to the rendering, the plugin also offers commands to move any timestamps to the nearest 5 minutes forward or backward, similar to what org-mode does with `shift-up/down`, and a feature I have always used multiple times per day.

Putting all of this together, my monthly time logging files now has entries that look like this:

```markdown
## theme 1
- project 1
  - task 1 <2025-05-20 07:55-08:10>
```

... and I can tweak those timestamps with the adjustment commands.

I have adapted the logging script to support both the old dataview-style and org-timestamp-style timestamps, and now the barely usable UX has become a tad less barely. 

*(10 minutes later...)*

Because I keep on mentioning the script, I guess it's time to [put it online](https://github.com/cpbotha/obsidian_dataview_timelogging), albeit extremely barely. Let me know in the comments below if you are the one other user on the planet who would like to try this.

## My friend this is the end again

This was one of the most stubborn WHVs I have pushed out in a very long time.

Before it became this hard, it used to be easier: Somehow there was always something to talk about, either interesting or entertaining, or both.

Although this could also just be another symptom of  me getting older, it does feel like the whole online landscape has changed quite substantially.

Up until recently, it was only dopamine-targeting social media which affected the way people read (or don't) blog posts, but these days I imagine that I'm also detecting a whiff of AI-nihilism. Although I still feel strongly about writing each of these words by myself, the experience of the resultant output happens on the background of machines that can now generate hundreds of perfectly-written versions of this post in an instant.

Anyways, I plan to continue with this labour of love, even as it becomes increasingly difficult.

P.S. My recent reading / book-listening has taken me on fascinating journeys through neuroscience and consciousness. Before reaching this point right here, I mistakenly thought that I would share more about them in this post. Instead I'm going to leave you with:

> I am not a thing in the world; I am the space in which the world is happening.
>
> -- Richard Lang
