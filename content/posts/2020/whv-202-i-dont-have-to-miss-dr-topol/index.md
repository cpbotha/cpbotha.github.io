+++
title = "Weekly Head Voices #202: I don't even have to miss Dr Topol!"
date = 2020-08-10T22:16:00+02:00
lastmod = 2020-08-11T08:52:37+02:00
slug = "weekly-head-voices-201-i-dont-have-to-miss-dr-topol"
tags = ["adam grant", "agi", "eric topol", "inoreader", "lex fridman", "social media", "twifraf", "twitter"]
categories = ["weekly head voices"]
draft = false
ogimage = "closeup_prot.jpg"
+++

Welcome everyone to this, the two hundred and second edition of the Weekly Head
Voices, looking back at the two weeks from Monday July 27 to Sunday August 9 of
the year of our simulation-running overlords 2020.

{{< figure src="closeup_prot.jpg" caption="Figure 1: Photo of multiple instances of an important local flower, taken by GOU #1." link="closeup_prot.jpg" >}}


## Shape Up: Stop Running in Circles and Ship Work that Matters {#shape-up-stop-running-in-circles-and-ship-work-that-matters}

After it having spent a few quality months in my to-do list, I finally got
around to reading [the Shape Up book by Ryan Singer](https://basecamp.com/shapeup).

(You can too, by clicking on that link, it's free!)

This book documents the development methodology that the folks over at
37signals, also the original makers of [Ruby on Rails](https://rubyonrails.org/), [Basecamp](https://basecamp.com/), and most
recently the new email re-imagining [HEY](https://hey.com/), have evolved over the years.

I'm not currently using any of those artifacts, but RoR has made (and is
probably still making) a significant impact on the technology landscape, and
the other products are truly impressive in their own right.

My point is, the 37signals company ships high-impact products like it's
nobody's business, so one should probably pay attention if they are willing to
explain to the rest of us how they are able to perform this feat so
consistently.

If you're involved in software development, or are interested, then this
compact book is worth your time.

However, until you can get around to it, I present to you the book's own
bullet-list summary (you'll find it in the conclusions chapter), where I've
embellished each bullet with my from-memory explanation.

Shaped versus unshaped work
: In Shape Up, each project is a user-visible
    feature that can be done in 6 weeks or less. Senior devs in the company
    _shape_ the work, which means that they derisk and write down enough to
    delineate the work, to specify the parameters, but not so much that it has
    been pinned down. The team that gets the project assigned is given free reign
    as to _how_ exactly they fill in the space delineated by the shaping.

Setting appetites instead of estimates
: Instead of specifying a feature,
    and then estimating how much time it will take (feature first, number
    second), Shape Up suggests rather determining at management level how much
    appetite / motivation there is for a feature, up to a maximum of 6 weeks,
    knowing that the feature will be _hammered_ down to fit into the appetite for
    it (number first, feature second).

Designing at the right level of abstraction
: As mentioned above, the
    shaping process has to reach the Goldilocks level somewhere between abstract
    and concrete. Enough detail so there are no surprises that could risk the
    success of the project, but little enough so that the team has the freedom to
    construct a solution independently and in a more data-driven fashion.

Concepting with breadboards and fat marker sketches
: These are practical
    tricks to keep the detail level under control. For example, during shaping, a
    **fat marker** is used to draw UI ideas to prevent the shapers from inking in
    too much detail.

Making bets with a capped downside (the circuit breaker) and honoring uninterrupted time
: This
    is pretty hardcore. If a project runs over its time (e.g. 6 weeks), it is
    cancelled, that is, moth-balled. End of story. As a corollary, teams are not
    to be interrupted during their project cycle.

Choosing the right cycle length (six weeks)
: Six weeks is the maximum time
    a team will get to finish a feature. This seems to be the sweet spot for
    features that are significant enough to be interesting, but don't get too big
    to manage.

A cool-down period between cycles
: After every six week cycle, all teams
    get two weeks of cool-down time. This is to be used for fixing bugs, writing
    tests, doing spikes, and just generally recovering from the feature
    development cycle.

Breaking projects apart into scopes
: As a team works on a certain feature,
    the sub-tasks that they formulate as they work, can be naturally grouped into
    thematic scopes. It's important that these emergent groupings are closely
    monitored and updated. They are useful for understanding the feature, and for
    reporting on progress.

Downhill versus uphill work and communicating about unknowns
: The team
    gives _asynchronous_ feedback on project progress by plotting each scope on a
    [hill chart](https://basecamp.com/features/hill-charts). To me this is yet another interesting and useful concept from the
    book. If a scope is somewhere on the uphill part, there are still unknowns
    that have to be investigated. Once the team thinks there are no more
    unknowns, a scope can be moved past the top and somewhere onto the downhill
    section.

Scope hammering to separate must-haves from nice-to-haves
: In this case,
    scope is used in the more traditional software development sense, and scope
    hammering refers to the action of whittling down features until a project
    fits into the time allotted to it.

At work, we are currently experimenting with elements of this methodology for a
new product we're working on. I'm curious to see how much of this will work in
our setup. It sure looks good on paper!

(The book impressed me further with its chapter containing practical advice on
how to implement various levels of Shape Up in organizations of various types
and sizes. Super pragmatic!)


## The Pygmalion Effect {#the-pygmalion-effect}

I'm currently reading the organizational psychologist Adam Grant's book [Give
and Take](https://www.adamgrant.net/give-and-take).

In this book he describes the classic study led by Harvard psychologist Robert
Rosenthal, where he told the teachers of 18 different classrooms that 20
percent of their children had scored high on a Harvard aptitude test, when in
fact they had been randomly chosen.

In spite of being _randomly chosen_, those children showed consistently higher
performance than their peers, even when they were measured years later.

From Grant's book:

> The Harvard test was discerning: when the students took the cognitive ability
> test a year later, the bloomers [the randomly selected kids, ed.] improved more
> than the rest of the students. The bloomers gained an average of twelve IQ
> points, compared with average gains of only eight points for their
> classmates. The bloomers outgained their peers by roughly fifteen IQ points in
> first grade and ten IQ points in second grade. Two years later, the bloomers
> were still outgaining their classmates. The intelligence test was successful in
> identifying high-potential students: the bloomers got smarter -- and at a faster
> rate than their classmates

and then a paragraph or two later:

> Teachers' beliefs created self-fulfilling prophecies. When teachers believed
> their students were bloomers, they set high expectations for their success. As
> a result, the teachers engaged in more supportive behaviors that boosted the
> students' confidence and enhanced their learning and development. Teachers
> communicated more warmly to the bloomers, gave them more challenging
> assignments, called on them more often, and provided them with more
> feedback. Many experiments have replicated these effects, showing that teacher
> expectations are especially important for improving the grades and intelligence
> test scores of low-achieving students and members of stigmatized minority
> groups.

Just to reiterate: These kids were randomly selected, but just because their
teachers _thought_ that they had scored higher on an aptitude test and hence
treated them differently, they started and then kept out-performing their peers
for years.

Grant writes that similar experiments have been successfully performed in different
learning contexts, and the results were always the same.

This really blows my mind folks. I hope I can keep this knowledge close.


## Yet another social media fast because you have to keep on doing them {#yet-another-social-media-fast-because-you-have-to-keep-on-doing-them}

[The Great Social Media Fast of 2019](/2019/09/09/weekly-head-voices-177-streakers/#the-great-social-media-fast-of-2019) really was great when it started, but it
unfortunately fizzled out a few months later, probably when the end-of-the-year
vacation started.

When COVID-19 hit, I had such a need for up-to-the-minute news that my phone
soon had twitter almost permanently on position #1 of the app suggestions you
get when you swipe down.

Fast-forward another few months, and I was again stuck in TwiFRaF-Yo like it
was nobody's business.

Anyways, this weekend I had some serious discussions with myself, during which
I _again_ had to convince myself that the select few jewels of Twitter (Dr
Topol, I salute you) and the rest of TwiFRaF-Yo did not even come close to
justifying the amount of mental cycles I was spending.

Fortunately I won that debate, and so now I'm again officially on a social
media fast, during which I have resolved to read more books, blogs and other
long-form content, and to write more notes and blogs.

My brain already feels substantially more roomy and relaxed than it did a mere
day ago.

I would be remiss if I didn't mention one of my favourite College Humor skits
in this context:

<iframe width="560" height="315"
src="https://www.youtube-nocookie.com/embed/md4kM9AKjHs" frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen></iframe>


### A not quite satisfactory solution for not having to miss Dr Topol {#a-not-quite-satisfactory-solution-for-not-having-to-miss-dr-topol}

Dr Topol did briefly complicate my temporary exit.

How was I going to keep up to date with his twitter stream without using the
twitter app and getting sucked in?

Unfortunately, my inoreader "supporter" subscription does not include its
social media subscription function that does exactly what I need, and the
upgrade is $50 per year instead of my current $20.

While I think about this, I've activated [the IFTTT twitter to email thingy](https://ifttt.com/applets/xcHFiVvR-get-an-email-when-there-s-a-new-tweet-from-a-specific-username).

This sends me an email for _each_ tweet, which constitutes a whole new problem
in itself.


### Inoreader satisfaction with a side of retail therapy {#inoreader-satisfaction-with-a-side-of-retail-therapy}

_... 8 hours pass after this post was published ..._

Narrator: _It became a whole new problem in itself._

Dr Topol can't stop tweeting admittedly truly interesting health- and
covid-related research, but the format of one email per tweet is indeed not
going to cut it.

I have deactivated that IFTTT thingy, and upgraded my inoreader subscription to
pro.

This is where I read all my blog subscriptions when I make time for that, so
having Dr Topol's feed there as well makes a great deal more sense.


## An AI to fall in love (with) {#an-ai-to-fall-in-love--with}

[Lex Fridman](https://lexfridman.com/) is another of the internet's jewels, who is fortunately accessible
via long-form podcast.

In [episode #106](https://lexfridman.com/matt-botvinick/), he talks with [Prof. Matt Botvinick](https://hai.stanford.edu/people/matthew-botvinick), a brilliant
neuro-scientist who also employs AI in his research, and clearly likes to think
deeply about deep questions.

One of the things I (and apparently many of his interviewees) love about Dr
Fridman, is the left-field questions he often poses.

He does this with Botvinick:

> But let me ask the over-romanticized question: Do you think we'll ever engineer
> an AGI system that we humans would be able to love and that would love us back?
> So have that level and depth of connection?

Goodness, so many layers.

What do you think?
