+++
title = "Daily Head Voices for week 3 of 2024"
date = 2024-01-21T20:21:00+02:00
lastmod = 2024-01-21T20:30:31+02:00
slug = "daily-head-voices-2024-01-15_21"
tags = ["lifelog", "braai", "copilot", "gou-1", "gou-2", "gou", "omnivore", "openai", "planning", "productivity", "running"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

## Monday 2024-01-15 {#monday-2024-01-15}

-   Discovered that we (at work) now have access to GPT-4 Turbo via Azure OpenAI: 128K context and much cheaper than the old GPT-4. Will have to upgrade our private internal assistant, code name StoneGPT.
-   Inspired by stefanv, carefully trying out weekly planning, but in a slight deviation I'm doing this _in addition_ to my daily planning, which I only get around to a fraction of the time in any case. I think that this sort of multi-scalar examination and planning will help.
-   Went to Bloemhof for the welcoming of the new grade 8 learners. Was really great to see GOU#1 _and_ GOU#2 there, on two very opposite ends of the spectrum.


## Tuesday 2024-01-16 {#tuesday-2024-01-16}

-   MS Copilot Pro ($20) has been announced, and also Copilot 365 is now available for businesses of all sizes (not just enterprises who can commit to 300 seats): <https://blogs.microsoft.com/blog/2024/01/15/bringing-the-full-power-of-copilot-to-more-people-and-businesses/>
    -   Copilot Pro not yet available in South Africa 😥
        -   $20 per month for integration with some Office apps (which could be useful, will have to see), priority access to latest models such as GPT-4 Turbo, and custom Copilots. I'm not convinced, will stick to my [perplexity.ai](https://www.perplexity.ai/) for now.
    -   Copilot for 365 can be purchased per seat, but minimum 1 year commitment which is $360 per person per year. Ouch.
-   In addition to many meetings (Tuesday = meetings day), did manage to spend some quality time with a new visualization project. Slowly starting to use [webcola](https://ialab.it.monash.edu/webcola/) again, but this time with d3@latest -- sorta works, but no dragging. Have found work-around, still need to test.
-   Went to bed really early, because must be up at 5:30 to help GOU#2 get ready for school and get to the bus stop on time. (Slept super badly thanks.)


## Wednesday 2024-01-17 {#wednesday-2024-01-17}

-   Up at 5:30 after a pretty restless night. GOU#2 on the bus at 6 after some serious morning prep multi-tasking, GOU#3 (age 7) so organized and independent, ready to leave for school at 7!
-   Nice and early(ish) slightly longer weekday run before work. My hip sent me a Teams message "Hi..." at about 80% of the route somewhere, but fortunately no follow-up. Colleagues on chat, haha.
-   Got caught up in [GEKKO Optimization Suite]({{< relref "#d41d8c" >}}) due to meetings with colleagues about various simulations. My initial enthusiasm was somewhat dampened upon learning that behind the Python API lies an admittedly useful but quite black-box compiled binary called apm.exe.
-   TIL: John Lasseter drew the BSD daemon! See <https://www.jacobelder.com/2024/01/17/director-of-toy-story-also-drew-bsd-daemon.html> -- I remember that daemon from the time when I had FreeBSD on my machine at home instead of Linux (somewhere in the 90s). You might remember that name from the [Creativity Inc.](/2020/12/22/book-notes-creativity-inc/#the-story-is-more-important-than-the-technology) book (the one about Pixar!) notes post on this blog


## Thursday 2024-01-18 {#thursday-2024-01-18}

-   **AlphaGeometry from Google DeepMind is great work** combining a symbolic math engine with a language model to solve Olympiad geometry math problems at just under gold-medalist level. See below for my breathless tweet. (twitter is still the uncontested ML firehose)
-   News on our in-house GPT-wrapper front:
    -   Discovered that I now have to upgrade to the new `tool_call` api as the old `functions` one has been deprecated. Made use of the opportunity to improve our implementation of the supplied OpenAI type annotations
    -   Note to self, and to you: The `*Params` types are `TypedDict` declarations which you can use to work directly with JSON requests and responses, while the non-`*Params` types are pydantic models which you can use to (de)serialize JSON.
-   Went to see a really good [Mohs surgery](https://www.mayoclinic.org/tests-procedures/mohs-surgery/about/pac-20385222) dermatologist who will soon be removing my basal cell carcinomas. As always, AMA in the comments or via email.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">This is such fantastic work! Symbolic engine + language model working together to solve Olympiad geometry math problems at just under gold-medalist level. Also, beautiful illustrations in the paper and posts. <a href="https://t.co/DtREuQK5k7">https://t.co/DtREuQK5k7</a></p>&mdash; @cpbotha@emacs.ch (@cvoxel) <a href="https://twitter.com/cvoxel/status/1747857845356298739?ref_src=twsrc%5Etfw">January 18, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## Friday 2024-01-19 {#friday-2024-01-19}

-   Spent most of my working hours wrappng up and deploying the brand new version of our internal GPT. I read somewhere that you should _always_ deploy on a Friday, as late as possible.
-   I was stressing quite a bit, as I had a great task before me:
-   Braaiing 200 boeries in the 39 degrees Celsius heat at the school in Stellenbosch, in order to feed the new grade 8 learners on the evening of their initiation.
    -   All thanks to the fellow dad who joined me, the stress transformed completely into an enjoyable few hours taking care of this important duty, and I made a new friend!
-   The kids, including our very own GOU#2, were facing the challenging night before them...


## Saturday 2024-01-20 {#saturday-2024-01-20}

-   woke up at 5:40 because was planning to fetch GOU#1 and GOU#2 after their eventful and successful night, but thankfully partner was willing to go!
-   me very tired the whole day, just hanging (literally) around with family, and spending too much time on twitter / threads / reddit / inoreader! (brain was not willing to do much else, at least learned new things, some of which are mentioned below)
-   Based on [this HN discussion](https://news.ycombinator.com/item?id=39055139) about [this blog post comparing Delta Lake and Parquet](https://delta.io/blog/delta-lake-vs-parquet-comparison/), learned that Delta Parquet aka Delta Tables (which I've read about in the context of Azure) is just a bunch of parquet files with some json metadata!
    -   I've been enjoying [parquet](https://parquet.apache.org/) for years now, in the context of scipy and specifically pandas.
    -   Indeed, OneLake, also part of Microsoft Fabric, has Delta Parquet at its core.
    -   Apache Iceberg is a similar but more open source implemenation: <https://iceberg.apache.org/>
    -   Based on [this comparison between Iceberg, Delta Lake and Hudi](https://www.dremio.com/blog/exploring-the-architecture-of-apache-iceberg-delta-lake-and-apache-hudi/) it looks like all of these data lake storage layers are just parquet files with metadata, and then some logic, to give database like semantics over distributed object stores. Neat!
-   In bed last night, falling asleep, I had the following idea:
    -   _My Current Life Canvas_ is a 3D bubble (off to my right for some reason... and moving with me as I walk) the interior of which I can view using my phone via AR (have to move phone in space to view inside of bubble, with current topics arranged in familiar spots; I thought having a world map would help, because well-known and memorable locations for your topics / priorities / ideas) or any of these amazing new VR headsets, BUT you can also interact with it via computer because inside of bubble can just be projected to surface using any of the well-known [map projection techniques](https://en.wikipedia.org/wiki/Map_projection).
    -   CLC does not have a regular cadence like the daily or weekly plan, but is revised or redone a few times per year. It focuses on your major life priorities at any one point in time.
    -   Although this was just a dreamy idea, I do like that it offers multi-modal interaction on the spectrum from AR/VR to more conventional desktop paradigms
    -   ... of course there should be some kind of friendly AI floating in the bubble with you :P (Microsoft Bob?)


## Sunday 2024-01-21 {#sunday-2024-01-21}

-   Super enjoyable weekend long(ish) run.
-   Tried out Omnivore's PDF annotation support, see screenshot below. Pretty impressive, and very cool that the highlights sync into my Emacs-based notes setup via markdown. Have slightly mixed feelings, because now will have to come up with new rule for when a paper goes into Zotero (fully local, full citations, but no automatic highlights sync) and when it goes into Omnivore (good sort of cloud but not local, no full citations, automatic sync into my notes)
-   Extended family Sunday lunch at our place was great, but me not at normal energy levels yet.
-   One of my goals for this week was "Get through the week, especially Friday braai". Mission successful!

{{< figure src="20240121-screenshot-omnivore-pdf-emacs.png" link="20240121-screenshot-omnivore-pdf-emacs.png" >}}
