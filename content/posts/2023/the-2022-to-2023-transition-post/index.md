+++
title = "The 2022 to 2023 transition post"
date = 2023-01-01T16:17:00+02:00
lastmod = 2023-01-06T09:55:44+02:00
slug = "the-2022-to-2023-transition-post"
tags = ["backyard philosophy", "blogging", "dropbox", "habits", "mindfulness", "reading", "running", "transition"]
categories = ["life"]
draft = false
author = "Charl P. Botha"
org = true
ogimage = "20221220-cape-st-francis-walk.jpg"
+++

Welcome to 2023 everyone, and to the [traditional yearly year transition post](/tags/transition/)!

{{< figure src="20221220-cape-st-francis-walk.jpg" caption="<span class=\"figure-number\">Figure 1: </span>Scene from a recent windy family walk in Cape St Francis" link="20221220-cape-st-francis-walk.jpg" >}}

I wish all of you all of the best for this shiny new year twenty-twenty-three!

(By the way, this, the first day of the year, is the earliest that the
yearly transition post has ever appeared!)


## Blogging {#blogging}

Over the past year, I published fifteen posts on this blog, 14 of which were
"weekly" head voices posts (#237 to #250), and one [the 2022 transition post](/2022/01/23/the-2021-to-2022-transition-post/).

In an ideal world where I get to divide up my time between family and friends,
blogging, running and Emacs, I might be able to get close to the mythical 52
WHVs per year.

However, for me 2022 was definitely The Year of a Whole Lot of Work.

You might remember [WHV #239 Embarrassing finitude](/2022/03/01/weekly-head-voices-239-embarrassing-finitude/#the-rickety-raft-of-life-directions-and-priorities), in which I observed that you
only get to choose a really small number (probably only two: family and
friends, and one additional project) of significant priorities that you can
effectively contribute to over any given stretch of time.

I mostly remember that I've made peace with this limitation, and I am realising
that (good) Work might be a crucial and substantial component of a long and
good life.


### Some stats {#some-stats}

Invoking the goaccess log analysis tool using the incantation below reports that
this site was visited by just over 126 thousand unique visitor IP numbers in
the year up to December 27.

```shell
export DOMAIN=cpbotha.net
(for i in {1..11}; do echo $DOMAIN.access.log.$i.gz; done; echo $DOMAIN.access.log) | xargs zcat -f -- | goaccess --ignore-crawlers --log-format=COMBINED -
```

The most popular posts also over 2022 were the very old [2013 usa my data has
left your building](/2013/09/15/dear-usa-my-data-has-left-your-building/), the still quite relevant [2016 migrating from gmail to
fastmail](/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/) and my [2019 note-taking strategy post](/2019/09/21/note-taking-strategy-2019/).

From this it's clear that I really have to get around to completing that
started-month-ago-but-languishing 202x note-taking strategy update, as my
system has evolved quite substantially.

I did also publish five posts on [vxlabs.com](https://vxlabs.com/), this site's nerdy sibling, which
in its turn attracted just over 147 thousand unique visitor IPs over the year.

The most popular posts from vxlabs were the following, in descending order:

-   [TypeScript development with Emacs, tree-sitter and LSP in 2022](https://vxlabs.com/2022/06/12/typescript-development-with-emacs-tree-sitter-and-lsp-in-2022/) - with
    tree-sitter having been merged with Emacs core in the meantime, this post
    also needs a substantial update. Emacs is developing faster than ever!
-   [Comparing WSL1 and WSL2 filesystem I/O performance on local and host files](https://vxlabs.com/2019/12/06/wsl2-io-measurements/) --
    still reasonably accurate, still relevant.
-   [Using Kubernetes for development containers](https://vxlabs.com/2021/11/21/using-kubernetes-for-development-containers/) - I'm surprised that this is
    relatively popular. I thought that it would be super niche.


### Selected learnings from 2022 {#selected-learnings-from-2022}

I went through all of 2022's WHVs to make an _extremely critical_ (haha)
selection of learnings that bear mention in this yearly overview.

Because I think all of them are worthy of a retrospection, they are
chronologically ordered.

-   [WHV #237 Don't step over the thing](/2022/02/03/weekly-head-voices-237-dont-step-over-the-thing/#i-don-t-want-to-step-over-the-thing) -- _We’re constantly stepping over the thing that
    we think we’re seeking in the act of seeking it._ ... _You can’t actually
    become happy. You can only be happy._
    -   Related: [WHV #247 Take a picture with your mind](/2022/11/01/weekly-head-voices-247-precious-moments/#take-a-picture-with-your-mind) -- Your narrating self, the
        one that needs to take all of those photos, can also take you out of the
        thing.
-   [WHV #239 Embarrassing finitude](/2022/03/01/weekly-head-voices-239-embarrassing-finitude/#the-rickety-raft-of-life-directions-and-priorities) -- I'm going to summarise that post section
    here with "pick your battles", or for the more poetically inclined readers
    "choose your f\*cks". Our time is extremely limited - it is best to make
    extremely deliberate and economical choices about the things that we spend
    our time and energy on at any point.
-   [WHV #242 Multiplicity of me](/2022/05/23/weekly-head-voices-242-multiplicity-of-me/) -- If you skip everything else, read this
    one. It's like "happiness for dummies, in 24 hours".
-   [WHV #243 Part-time role model](/2022/06/23/weekly-head-voices-243-part-time-role-model/#part-time--role--model) -- Some motivation to never stop trying to be the
    best you, also when, inevitably, you'll only have occasional success.
-   [WHV #246 Call up your friends](/2022/09/25/weekly-head-voices-246-call-up-your-friends/#call-up-your-friends) -- Do call up that friend you're thinking
    up. Write thank-you notes. Send birthday messages. Make the connection!
-   [WHV #249 Self-discipline](/2022/11/20/weekly-head-voices-249-self-discipline/#self-discipline) -- Take care of this personal engine and it will
    take you places.
-   [WHV #250 Durable, blissful contentment](/2022/12/06/weekly-head-voices-250-durable-blissful-contentment/#happiness-is-a-joke)


### Quo vadis 2023 {#quo-vadis-2023}

Writing on this here blog, and specifically the WHVs, is important to me for
the following reasons:

-   They enable learning, through retro- and introspection.
-   Each successful post is an exercise in applied and externalised self-discipline.
-   I enjoy practising the dying art of writing.
-   They help to form a connection with other humans, both friends and strangers.

The reason for this retro-retrospection here, is that I am evaluating the
(smouldering) results and implications of the tension between post regularity
on the one hand, and self-perceived post substance on the other, over the past
year.

I've erred on the side of post substance, when regularity might have been the
better option.

It's not that I was able to control it that deftly; what we have here is merely
the result of trying to publish posts of a reasonable quality at a reasonable
cadence.

My current feeling is that I would like to increase regularity, in spite of
past performance.

To make this happen, I have to learn to be satisfied with somewhat less, and
more importantly, I have to come up with improvements to my blogging workflow
that enable a more predictable flow of material.

A new year won't be a true new year without overly ambitious resolutions, now
will it?


## Running {#running}

This year, I averaged 20km of running per week for a total of 1044km (118 runs,
just under 99 hours) over the whole year.

Last year I did 25km per week, which is what I would have liked for this year
as well, but this is fine. _Any_ kilometres are better than no kilometres!

{{< figure src="images/Tasks/2022-12-31_16-17-19_screenshot.png" caption="<span class=\"figure-number\">Figure 2: </span>Random drop-outs in graph below. At least finished strong in last week of year." >}}

I did three quick spot checks in my daily journals to see if I could determine
any specific reasons for the low / no-exercise weeks, but nothing jumped out.

I'm going to have to blame work for this one too.

Anyways, what I _can_ say, without any hesitation, is that running made a massive
positive contribution to my physical and mental well-being this year.

The effects can generally be immediately felt (that beautiful bit when it feels
like all one's limbs are finally working together, rhythmically even, is
exhilarating), and usually signal another start of a cascade of positive
physiological and life-style factors.

Running resolutions for 2023: 0) Much enjoy. 1) Don't get injured. 2) Try _again_ for the 25km/w average.


## Reading {#reading}

I really enjoyed the following books:


### Fiction {#fiction}

-   [Project Hail Mary by Andy Weir](https://www.goodreads.com/book/show/54906250-project-hail-mary) - feel good edge of seat stranded in space but
    have to save the earth human-alien-buddy movie -book. Great for engineers who
    know how to suspend disbelief.
    -   I could not remember that I had ever bought this book, but enjoyed the
        living daylights out of it. Only later discovered that it was GOU #1 (who
        shares my Kindle account)! 🥰 we enjoyed the same book!
-   [Termination Shock by Neal Stephenson](https://www.goodreads.com/book/show/57357418-termination-shock) - this is such a disciplined, detailed,
    diligent piece of science fiction by someone who clearly has _practised_ this
    art and honed their craft to perfection. I enjoyed the story (it does require
    some reader stamina) and appreciated the massive skills of the artist.
-   [Permutation City by Greg Egan](/2022/03/21/weekly-head-voices-240-i-am-just-a-copy-of-a-copy-of-a-copy/#permutation-city) - click on the link to the left to go to my
    mini-review in WHV #240.


### Non-fiction {#non-fiction}

-   [Projections: A Story of Human Emotions by Karl Deisseroth](/2022/07/24/weekly-head-voices-244-biyamiti-bat-fan/#projections) - click on the link
    to the left to go to my mini-review in WHV #244.
-   [The Unseen
    Body: A Doctor's Journey Through the Hidden Wonders of Human Anatomy by
    Jonathan Reisman](https://www.goodreads.com/book/show/59516276-the-unseen-body) - Join the doctor on a fascinating journey through each
    and every organ in the human body, robustly spiced by his stories of travels
    to some of the most remote corners of the globe, and of his experience
    various medical emergencies.


### Resolutions {#resolutions}

Somewhere in the second half of 2022, I somehow lost my [reading-before-sleep
habit](/2022/01/23/the-2021-to-2022-transition-post/#reading).

I plan to reinstate this habit, and to install the new habit of reading more
books on my phone (vs being limited to my Kindle, which is not always with me).

Armed with these two life-hacks, I hope to finish reading 20 books in 2023.

Please send me your recommendations in the comments below!


## Systems and tools for running this human {#systems-and-tools-for-running-this-human}

As per tradition, I quote from previous transition posts my explanation of "The
System":

> The System is Emacs, and orgmode, and multi-scalar note-taking everywhere, and
> sketching, and daily habits, and a whole bag of tricks to try and keep this
> creaky old frame moving in the right direction.

Similar to [last year](/2022/01/23/the-2021-to-2022-transition-post/#systems-and-tools-for-running-this-human--pkm-baby), Emacs, Orgmode and Org-roam are still going very strong,
and constitute the lion's share of my personal knowledge management system.

In fact, with the imminent Emacs 29 release, a recent build of which I'm typing
this draft into (English is hard folks...), Emacs has only become _more_
compelling.

Amongst [many other improvements](https://blog.phundrak.com/emacs-29-what-can-we-expect), tree-sitter, eglot and use-package are now all
part of core.


### Byeeeeee Dropbox! {#byeeeeee-dropbox}

However...

The time has finally come for me to drop (again) Dropbox.

Although I have been a paying customer for many years (see [WHV #15](/2010/02/28/weekly-head-voices-15-auto-tune-my-cloud/) from
February of 2010 for a report close to the start of our commercial
relationship), in the end it was their intransigence and inscrutability around
the Dropbox Paper 2020 migration that broke the camel's back.

They have been promising since before 2020 that they would migrate all existing
users to the new 2020 edition of Dropbox Paper.

However, now all you can find about this are frustrated forum posts from
long-time customers. My direct support request to be migrated was promptly
answered, and then closed with the following message:

> As much as I would like to help, currently, the latest version of Paper release
> is available to new users only.
>
> Our team is currently in the process of working on this new feature in order to
> build the best Paper experience for all our users.

I still really love that tool (winner of the WHV Award for the Most
Unexpectedly Useful Software Tool of the Year 2021!), but the interaction above
only served as a reminder of the pitfalls of a relationship like this.

During the writing of my yet-to-appear 202x note-taking approach blog post, it
bugged me that I had to come up with a good explanation for why I allowed
Dropbox Paper to break my rule of everything-needs-to-be-a-file-I-could-sync.

Although my yearly Dropbox Paper subscription is only up for renewal in June of
'23, I decided to bite the bullet and [migrate everything out to an extremely
frightening mix of OneDrive, syncthing and unison](/2022/11/11/weekly-head-voices-248-oh-snap/#hell-freezes-over--again).

As I write this, it's been just over two months with nary a hiccup.

In June, I'll let that Dropbox subscription lapse.

Dropbox Paper, RIP.

(With [1writer](https://1writerapp.com/) and also [Plain Org](https://plainorg.com/) on the iPhone, and [syncthing](https://syncthing.net/) on my main desktop
at home, plus Apple Notes for the truly ephemeral stuff, I have a pretty
capable mobile response to Paper.)


### Resolutions {#resolutions}

1.  I would really like to publish a blog post titled _Note-taking approach
    2023_. Ideally, it should be full of information about my current PKM system.
2.  Write more notes, including both journals and [Zettelkasten-style](/tags/zettelkasten/) notes.
3.  Stretch goal: Maybe get another useful patch into Emacs.


## Work {#work}

2022 was my first year back in employment, after [eight years of freelancing](/2013/03/09/dear-academia-i-hope-we-can-still-be-friends/).

In this year, I have only become more deeply involved and invested in the
current [Stone Three](https://stonethree.com/) adventure.

As I mentioned previously, I have the privilege of working closely together
with extremely capable folks, in a high-trust setting.

Many of my colleagues are smarter than I am in their respective fields. Due to
that, and the fact that we are both growing and innovating, I am constantly
learning.

My personal responsibilities span the spectrum from programming, through
mentor- and leadership to management and org-level technical decisions. On the
other dimension, I am exposed to everything from software plumbing to data
science, engineering and visualization. (This is what's known as a
PiM-situation. PiM = pig in mud)

The work is hard, but it's varied, it's challenging, it's together with a group
of humans I like, and it feels meaningful.

I have written all these words to try and explain that although it's clear from
this post that Work(tm) took up significantly more time and space this year, it
has contributed substantially to my well-being.

Freelancing was less stressful -- I could focus on the engineering tasks at
hand and usually deliver. Now I have more responsibility, which brings
substantially more stress but also more satisfaction.

Furthermore, in terms of maintaining the plasticity of my neural network,
something I do have to pay more and more attention to thanks to the advancing
years, the variation and challenges of my current work setting are great.

That being said, I definitely have to get better at controlling stress.


## Things I would like to work on in 2023 {#things-i-would-like-to-work-on-in-2023}

In addition to the blogging, running, reading and systems resolutions mentioned
above, I would like to work on the following bigger themes in 2023:

1.  Work(tm).
2.  Self-discipline, [as featured in WHV #249](/2022/11/20/weekly-head-voices-249-self-discipline/#self-discipline). I will implement this by writing
    really stern messages to me in my diary.
3.  Creating, restoring and maintaining good habits that [compound](/tags/compounding/): Reading,
    writing, running, mindfulness practice.

... and then finally, my central theme for 2023 will be:


### 4. Expansiveness {#4-dot-expansiveness}

Sometimes, most probably when you're out in nature, you experience your senses
really opening up.

It is as if the usually clearly defined borders between you and your
surroundings start to fade away.

I've talked about this phenomenon before, in [WHV #217's The Strange Continuum
of Consciousness](/2021/03/22/weekly-head-voices-217-consciousness-continuum/#the-strange-continuum-of-consciousness) and in other places.

It's a great feeling, and it usually happens when you are fully present in that
moment.

For a while, you can get pleasantly lost in the infinite and fractal detail in
the moment and its participants.

For a while, you can truly appreciate the beauty of your surroundings, of the food
and drink you might be enjoying, and of the humans in your company.

In 2023, let us be expansive!
