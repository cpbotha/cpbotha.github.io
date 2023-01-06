+++
title = "Weekly Head Voices #249: Self-discipline"
date = 2022-11-20T17:39:00+02:00
lastmod = 2022-11-20T19:42:58+02:00
slug = "weekly-head-voices-249-self-discipline"
tags = ["backyard-psychology", "emacs", "jupyter", "mastodon", "quarto", "self-discipline"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
org = true
ogimage = "watsonias-effects.jpg"
+++

Welcome to WHV #249, covering the two weeks from Monday November 7 to Sunday
November 20, 2022.

{{< figure src="watsonias_pano_thanks_stella.jpg" caption="<span class=\"figure-number\">Figure 1: </span>Photo of many Watsonias (up from last week!), taken by partner on a hike." link="watsonias_pano_thanks_stella.jpg" >}}


## Emacs Mastodon server was irresistible {#emacs-mastodon-server-was-irresistible}

A week or two ago, I was still chatting with friends about how to respond to
the currently in-progress Twitter Muskification.

At that point, largely due to all of the great connections and positive
experience I've been enjoying on twitter (howto: follow only kind humans who
are involved in your fields of interest; in my case visualization, machine
learning, data, mobility), I commented that I had no plans yet and preferred
waiting for a bit to see how it would pan out.

The topic of [Mastodon](https://joinmastodon.org/) did come up, but the feeling in that tech-savvy group was
that it was perhaps a bit complicated.

In the days since then, the developments at Twitter seemed to have accelerated,
but it's still extremely tricky to predict where all of this will end up.

Also in the days since then, a Swiss gentleman named [Louis](https://emacs.ch/@louis) had the nerve ;) to
setup a Mastodon server called [emacs.ch](https://emacs.ch), catering to Emacs enthusiasts...

CURSES!

I see Emacs, I move.

My account was created a few minutes later, and suddenly Mastodon was not
complicated at all y'all!

Things that I really like so far:

-   Anyone can setup an independent yet connected server that caters to a
    specific interest group, such as Emacs users.
-   Much more engagement and connectedness with other users, thanks to the server
    focus.
-   Early internet feelings: Optimism, grassroots, people.
-   Fantastic Emacs support. I can [read and post directly from Emacs, using the
    amazing `mastodon.el`](https://emacs.ch/@cpbotha/109337719793270417).
-   No algorithm that re-arranges the posts that you see. What you see is what
    your timeline posted, when they posted it.
-   No ads!
-   Yes, here you **can** edit your posts after you've posted them. IT'S TRUE.
-   NO ADS!

I've been having fun tracking down friends and colleagues on their various
mastodon servers, and re-making connections.

If you're also interested, my advice would be to start by [searching for a
server](https://joinmastodon.org/servers) (or more than one!) that really suits you.

Then, if you like, you can find _me_ at [@cpbotha@emacs.ch](https://emacs.ch/@cpbotha) !


## Quarto .qmd looks like the answer to my .ipynb prayers {#quarto-dot-qmd-looks-like-the-answer-to-my-dot-ipynb-prayers}

Back in 2018 I talked about [my complicated feelings for Jupyter Notebooks](/2018/07/17/weekly-head-voices-148-data-stylist/#vacation-based-thinking-driven-tool-sharpening-aka-the-wvv-2018-data-science-toolboxtm).

To elaborate a bit, I still do think notebooks are amazing, but they are so
amazing that their design limitations can get in the way.

Most recently, the .ipynb format, which is standard .json representing the
various input cells (code and markdown mainly) and also their outputs (yikes!),
caused issues at work.

Although it's convenient from a notebook user standpoint that you can open up
an ipynb and see the last rendered version of the notebook, it really
complicates source control (diffs), and opening the .ipynb up in a normal
editor to debug issues is not fun at all.

Well, recently, spurred on by the below provocative tweet by Chelsea
Parlett-Pelleriti (who is now also on Mastodon as
[@chelseaparlett@nerdculture.de](https://nerdculture.de/@chelseaparlett)):

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Friendship ended with .rmd<br><br>now .qmd is my best friend <a href="https://t.co/7ETH4o2KUH">pic.twitter.com/7ETH4o2KUH</a></p>&mdash; Chelsea @chelseaparlett@nerdculture.de (@ChelseaParlett) <a href="https://twitter.com/ChelseaParlett/status/1591505992805543936?ref_src=twsrc%5Etfw">November 12, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

... I decided to take a deeper look at Quarto and especially .qmd.

In short, .qmd is markdown with executable code-cells!

If you take a look at the VSCode-based [Get Started guide](https://quarto.org/docs/get-started/hello/vscode.html), you'll see that can
type up .qmd files in any text editor, and then have the quarto cli tool show
you a continuous preview of your work.

The examples they show look _really_ attractive folks!

One of the fundamental improvements here, is that by design outputs are not
stored inside the .qmd file format.

An addition, the top-to-bottom execution of one's notebook is the primary mode
of operation, although cell-based execution is also possible. This is the
opposite of normal notebooks, where the default interactive cell-based
execution often results in the top-to-bottom not being tested, and hence often
being broken.

For my current analytics applications, it looks like we'll be able to use .qmd
as a drop-in replacement for .ipynb.

Although Org mode and org-babel have been doing this (plaintext file with
executable code cells) for a long time now, I am really excited that there's
now a more accessible solution that will hopefully become very popular.

P.S. After all of that, I was additionally thrilled to discover that Dr Carlos
Scheidegger, a brilliant and friendly colleague from the the data visualization
world, was on the core developer team. Here he is [announcing, on Mastodon, the
just-released v1.2 of Quarto](https://emacs.ch/@scheidegger@mastodon.social/109343921680547594)!


## Self-discipline {#self-discipline}

Picture this:

You wake up in the morning, refreshed and ready to take on the day.

With your mind as clear as it'll ever be, you make a list of the things that
you know that you should work on today: Let's call them Things A, B, C and H.

You're really passionate about A, but you realise that B and C are at least as
important to your and your family's well-being.

H is just something urgent that you've postponed for too long and now really
has to be taken care of, or perhaps the H stands for Harbinger.

"Harbinger of what?" I hear you think...

Shortly after this moment of clarity, the day (on some days aka "all Hell")
breaks loose and you suddenly have to deal with all of the vagaries of modern
work and life.

It's starting to feel like the crystalline clarity of a few moments ago might
be just a little too brittle to resist the deluge of chaos.

On your _better_ days, you will be able to keep your eye on Thing A, in spite of
all of the obstacles that stand in your path. Your passion for A helps you to
power through.

On your _best_ days, you will find that quiet determination inside, that modest
but diamond-hard resolve that will enable you to tend to Things B and C in
addition to A, with deliberateness and diligence.

In my view, being able to focus on your passions in spite of challenges on your
path sounds like **_grit_**:

> ... grit is a positive, non-cognitive trait based on an individual's
> perseverance of effort combined with the passion for a particular long-term
> goal or end state (a powerful motivation to achieve an objective). This
> perseverance of effort promotes the overcoming of obstacles or challenges that
> lie on the path to accomplishment and serves as a driving force in achievement
> realization. Distinct but commonly associated concepts within the field of
> psychology include "perseverance", "hardiness", "resilience", "ambition", "need
> for achievement" and "conscientiousness". These constructs can be
> conceptualized as individual differences related to the accomplishment of work
> rather than talent or ability. -- [Wikipedia on "grit"](https://en.wikipedia.org/wiki/Grit_(personality_trait))

Whereas I would label the characteristic of being able to continue paying
attention to things that are important but not necessarily your areas of
passion **_self-discipline_**:

> Resolute adherence to a regimen or course of action in order to achieve one's
> goals. -- [definition #2 from the APA Dictionary of Psychology](https://dictionary.apa.org/self-discipline)

(Definition #1 on that page is _self-control_, which seems to be the passive
counterpart (or component) of _self-discipline_, based on what I can find
online. Unfortunately, what I can find online are mostly second- and third-hand
observations, see e.g. [quote by Dr. Julia-Marie O'Brien #1 without citation](https://fredericksburg.com/self-control-and-self-discipline-arent-the-same/article_9e91991c-81e8-5a8f-bca0-972e025fbe24.html),
[same quote #2](https://matthogan.blog/self-discipline-vs-self-control/), [same quote #3](https://selfctrl.com/3-lessons-learned-on-building-self-control/) or [quora, sorry!](https://www.quora.com/Whats-the-difference-between-self-control-and-self-discipline) -- "Self-control says no, or
stop. Self-discipline says go, and keep it going." -- Although I would like to
find better discussion about this, the distinction does make sense.)

Self-discipline is one of those skills that can be practised.

By applying it more often, and especially so when it feels like the going has
gotten tough, you'll be able to apply it more reliably and more consistently in
the future.

Self-discipline is the reliable bridge linking you and your goals, at your
absolute best, with you at all other points.

It can be difficult to keep on practising, but when you can look back on one of
_those_ days, and see how you even managed to take care of Things B and C, in
addition to A, in spite of the adversities on your path, you will experience
quiet satisfaction.

Savour the moment.
