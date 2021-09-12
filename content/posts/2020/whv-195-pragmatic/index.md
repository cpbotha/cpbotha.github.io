+++
title = "Weekly Head Voices #195: Pragmatic"
date = 2020-05-20T23:06:00+02:00
lastmod = 2021-06-26T12:57:05+02:00
slug = "weekly-head-voices-195-pragmatic"
tags = ["book", "exocortex", "keyboards", "wsl", "xrdp", "context", "backyard-philosophy"]
categories = ["weekly head voices"]
draft = false
ogimage = "nbh_mountain_walk_pano.jpg"
org = true
+++

{{< figure src="nbh_mountain_walk_pano.jpg" caption="Figure 1: Photo from a walk with the fam jam up the mountain a little while out from our backyard, all within the sanctioned exercise hours between 6 and 9 in the mornings." link="nbh_mountain_walk_pano.jpg" >}}

This edition of the Weekly Head Voices looks back at the week from Monday May
11 to Sunday May 17, 2020.

The rest of this post consists of a part about keyboards, a part chock full of
ways to waste your time with WSL and f#, a part about why you might be wasting
your time with aforementioned, and then finally a part about a really
interesting book.

If you don't like keyboards, and you're wondering in a non-curious way what a
WSL is, I would strongly recommend that you jump to the part, at the end of the
post, about the really interesting book.


## Ergonomic keyboard one-way street {#ergonomic-keyboard-one-way-street}

As you will recall from [the thrilling events of episode #193](/2020/05/03/weekly-head-voices-193-covid-19-part-3/#microsoft-sculpt-ergonomic-desktop-at-4-years-rip), one of my two
(home-office and office-office) Microsoft Sculpt Ergonomic keyboards gave up
the ghost.

After far too many keyboard reviews and a fruitless search for a worthy
alternative, I indeed gave up and tried to make peace with the fact that over
the coming years I'll be slowly buying up the rest of the world's Sculpt
supply.

My secret campaign got off to a pretty unspectacular start as I was able to
find exactly one (1) online retailer that was able to supply at this moment.

I mundanely ordered the thing, and it was pretty mundanely delivered to my
house a few days later.

After some breaking in, I am happy to report that a brand-new Sculpt indeed
feels a great deal more amazing than a 4-year-old Sculpt.

As backups for any additional future apocalyptic situations, I also bought two
much cheaper "normal" keyboards, namely [the Microsoft Wired Keyboard 600](https://www.microsoft.com/accessories/en-us/products/keyboards/wired-keyboard-600/anb-00001).

I tried typing on one just to see what it was like, but more specifically to
develop some sort of intuition for if I would ever be able to return to
straight boards.

To be quite frank, my first impressions were pretty horrible.

Wrists having to bend outwards like that is positively uncomfortable, while the
keys on that unit make for a solid 14 on the 10-point mushiness scale.

One could perhaps get used to the mushiness, or preferably just invest in a
more expensive (mechanical) keyboard, but that ulnar deviation is a total deal
breaker.

My dreams of joining the clickety-clackety cliques of the mechanical keyboard
digerati had been shattered, fortunately quite cheaply.

Instead, I shall be redoubling my Sculpt stockpiling efforts.


## Interlude of even more nerdy miscellany. {#interlude-of-even-more-nerdy-miscellany-dot}

On Friday evening I was sucked into Windows and WSL2 again.

I stayed up a bit too late because I discovered that instead of displaying to
X410 on Windows, which is slightly painful with WSL2 due to port redirects
and/or firewalling and/or the connection dying every time the Windows host
suspends, one can also start xrdp on WSL2, and then connect to that with
Windows remote desktop.

For WSL2, this is much more robust than X11, and for some use-cases it offers a
better experience. (I'm writing this on Tuesday, and [MSBuild has just made a
number of super relevant announcements with regard to native WSL2 Linux GUI
support](https://devblogs.microsoft.com/commandline/the-windows-subsystem-for-linux-build-2020-summary/). For the demo of WSL2 Linux GUI apps, they were displaying to Wayland
on WSL2 and connecting to that using RDP.)

On Saturday, I wrestled with and was solidly trounced by .net core 5 preview 3
and the preview of F# 5.

My goal was to try out the [new `r# nuget` package references](https://devblogs.microsoft.com/dotnet/announcing-f-5-preview-1/), and specifically
to try this out with the PowerShell type provider in [FSharp.Management](https://github.com/fsprojects/FSharp.Management).

At this point, I also can't tell you exactly why.

I now believe that this was just an instance of the eternal and far broader
learn-something-completely-new vs. work-on-some-compounding-activity conundrum.

(I would later learn that Fsharp.Management has not been updated in a while,
and the packages are not compatible with netcore or netstandard.)

Probably more importantly, I learned that when you're an utter F# noob like me
you should probably just avoid the bleeding edge altogether.

It's called the _bleeding_ edge for good reason.


### The story behind this story: One context to rule them all! {#the-story-behind-this-story-one-context-to-rule-them-all}

When I bought my ex-MacBook Pro 2017 in 2017 on my birthday, you might remember
[how I justified it then](/2017/09/05/weekly-head-voices-125/#new-laptop):

> Up to then, I had been working on all of three different machines:
> Linux-running i7 desktop (acquired in Feb of 2015), early 2015 13″ retina
> MacBook Pro (acquired in June of 2015) and my trusty old klunky i7 Acer
> Linux-running laptop (acquired around March 2013).
>
> Data is kept in sync, but context switching between different projects with
> different development environments on different machines at home and at work
> does seem to take up more time than I would care to admit.
>
> Having everything on a single powerful-enough laptop would indeed make the most
> sense from a time-efficiency perspective.

That part of the MacBook Pro experiment worked out quite well: The hardware and
software was good enough for _everything_ that I needed to do, so I hardly ever
needed to context switch out of the laptop.

Although [the new ThinkPad](/2019/04/27/new-laptop-2019/) is more powerful, the fact that I reboot multiple
times per day in and out of Windows and two different Linux configurations on
the laptop is almost like having three different machines, which of course
kills the whole single context dream.

(spoiler alert: In the book-review section after this, context-switching is one
of the main villains!)

Anyways, the reason I keep on returning to WSL2 and then wasting time trying to
make it work more like native Linux and to integrate better with my workflow on
Windows is because I would really like to get rid of this specific context
switch.


## Pragmatic Thinking and Learning {#pragmatic-thinking-and-learning}

This past weekend I finished reading [Pragmatic Thinking & Learning - Refactor
Your Wetware (ed: ahem) by Andy Hunt](https://www.goodreads.com/book/show/3063393-pragmatic-thinking-and-learning).

The book is chock full of valuable guidelines for trying to improve the way in
which I apply the limited mental energy I have at my disposal.

(Quite ironically, it felt like the weekend was pretty much me flying right in
the face of just about every piece of advice in the book.)

Here is a selection of the notes I made, slightly massaged for your
consumption. Bon appetit!

-   Make room for the creative part of your brain to fly. First pour in some
    reading and structured thinking, and then take a walk, stare out into space,
    shower (again), take a nap, make a drawing upside-down. Do whatever's
    required to shut logical Spock voice up for a while. When the ideas start
    flying in, and they do, switch logical Spock voice back on to structure and
    process them.
-   Build and start using an exocortex. (The reason I bought this book, is
    because it was pointed out to me as a good reference for the context and term
    _exocortex_. I'm planning to write more about it [here](https://cpbotha.net/2020/05/03/weekly-head-voices-193-covid-19-part-3/#the-amazing-niklas-luhmann-and-his-zettelkasten) and [elsewhere](https://orgmode-exocortex.com/).)
-   Science says that happiness enhances cognition. In other words, when you're
    happier, you're really smarter.
-   **Write drunk, revise sober.**
-   Get in the habit of collecting snippets of your writing. That's what the
    exocortex is for. You might be surprised at what you're able to construct
    with all of the snippets you collect over time. In the book, this is called
    the Fieldstone method, but it sounds suspiciously similar to slips of paper
    in a slipbox, aka Zettelkasten.
-   Formulate SMART goals, that is Specific, Measurable, Achivable, Relevant and
    Time-boxed. If you read this blog, you're probably "smart" enough (dad joke,
    sorry) to figure out why this is good.
-   Manage your mind along three axes:
    1.  Increase focus and attention, e.g. by training focus and attention also
        through practising meditation and by sometimes just doing nothing. [Daniel
        Dennett's _multiple drafts_ model of consciousness](https://en.wikipedia.org/wiki/Multiple%5Fdrafts%5Fmodel) is discussed here,
        super interesting stuff.
        -   On that note, your whole brain and all of its high-level capabilities
            are squarely in the use-it-or-lose-it camp.
    2.  Manage your knowledge. You guessed it: Exocortex.
    3.  Optimise your current context. Keep in your view only what is required to
        work on the current thing. Minimise context switching. Avoid distractions
        and manage interruptions.

Well, that was basically my exocortex flexing for you.

ANYWAYS

After all of that, my favourite part of the book was this:

{{< figure src="pragmatic_screenshot.png" link="pragmatic_screenshot.png" >}}

For those of you viewing this blog in its 100% text-only form, the screenshot
above is of the part of the text explaining that not every day is going to be a
productive one.

I highlighted that, and added the comment:

> Some days gonna be crap.

As life goes on, I have come to the realisation that no matter how hard you
work and how much you practise, the days when everything seems to go right
according to plan are truly scarce and should be celebrated.

It's probably best to make peace with that fact, and simply to never stop
trying.

Also remember that it is quite possible to bend time just a little bit so as to
create a little more space around the small victories and pleasures that one
experiences even on _those_ days.

See you around friends!
