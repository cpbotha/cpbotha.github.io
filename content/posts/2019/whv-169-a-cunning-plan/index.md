---
title: "Weekly Head Voices #169: A cunning plan."
# we specify slug also, because hugo keeps the # in there, breaking routing
slug: "weekly-head-voices-169-a-cunning-plan"
author: cpbotha
# REMEMBER TO CHANGE BEFORE PUBLISHING!
date: 2019-04-15T22:12:00+02:00
tags:
  - fsharp
  - nim-lang
  - jbop
  - vo2max
  - vaccination
  - the matrix
  - 
categories:
  - weekly head voices
type: "post"
---

<figure>
<a href="pretty_clouds_above_home.jpg">
{{< img src="pretty_clouds_above_home.jpg" alt="pretty evening clouds above my home" >}}
</a>
<figcaption>
Beautiful evening skies above my house.
</figcaption>
</figure>

I just went through my notes. 

As far as I can see now, the week from Monday April 8 to Sunday April 14 2019,
although otherwise quite solid in terms of productivity and of The Important
Stuff(tm), did not fare too well on the blog-worthiness scale.

About the exact implications of this discrepancy, [I am also not entirely
sure](https://en.wikipedia.org/wiki/If_a_tree_falls_in_a_forest).

Nonetheless, my mission at this moment is to try and give you something
entertaining and/or educational, and for this [I have a cunning
plan...](http://blackadderquotes.com/i-have-a-cunning-plan)

# nimfatuation is now OVER.

```common-lisp
;; consider reading this section if this line of code is clear to you
(if (not (are-nerd you)) (skip-this-section))
```

Last week, [I had happily started diving into the nim language and its
ecosystem](/2019/04/08/weekly-head-voices-168-postcards-from-the-edge/#nim-surprise).

I was quite happy to hear that in addition to the enjoyment it had given me,
the spark had jumped over to at least one other peep (O HAI THERE S!) via
these writings.

However, after getting deeper into [jester's multi-threading
intricacies](https://github.com/dom96/jester/issues/194) and discovering that
I could not get run-time confirmation that my requests were being handled by
separate threads, I returned to my initial target language for this experiment of
rewriting, namely f\#!

nim is really a great little experiment: It consists of higher level
abstractions that compile down to C, and it's quite amazing to see what this
enables one to do.

However, I require something richer and more functional for my language
learning slot.

As I have written previously, [f# hits all six of my 2018
PL-requirements](/2018/07/17/weekly-head-voices-148-data-stylist/#f).

In addition to the qualities of the language itself, [dotnet core 3, currently
at preview
3](https://devblogs.microsoft.com/dotnet/announcing-net-core-3-preview-3/), is
showing great progress, also in terms of memory efficiency and raw
performance.

I spent some time during the past week to re-re-implement my
nim-re-implementation of parts of isso, again purely for learning purposes.

(As an aside, it's interesting how close such a real-world example enables one
to get to using a tool or language *in anger*.)

Here's a fragment from my learning experiment, because if you're like me
you'll want to see what f\# looks like:

```fsharp
let getCommentsHandler : HttpHandler =
    fun (next : HttpFunc) (ctx : HttpContext) ->
        task {
            // going from normal str -> Result to str -> Task<Result>,
            // so unfortunately no railway OP here.
            match ctx.GetQueryStringValue "uri" with
            | Error _ -> return! setStatusCode 404 next ctx
            | Ok uri ->
                match! getThreadForUriAsync uri with
                | Ok thread ->
                    match! getCommentsForThreadId thread.id with
                    | Ok comments -> return! json comments next ctx
                    | Error msg -> return! (setStatusCode 404 >=> text msg) next ctx
                | Error msg -> return! (setStatusCode 404 >=> text msg) next ctx
        }
```

This is a [Giraffe](https://github.com/giraffe-fsharp/Giraffe) handler that
handles a request with a `uri` query parameter. First it looks up the comment
thread in the isso database. If it finds a thread, it looks up the comments
and returns the whole list as JSON.

As you can see, there is error handling at every level.

F\# code is expressive, but it is also fully typed. In this case it is
executed asynchronously (that's what the `task {}` and the `!`s are for), with
the asynchronous tasks distributed over threads.

In other words, we have a compiled functional language with Python-level
expressivity with really strong (and easy!) concurrency support.

If there had been no need for asynchrony, the code above could have been
rewritten following the [railway-oriented
programming](https://swlaschin.gitbooks.io/fsharpforfunandprofit/content/posts/recipe-part2.html)
idea (from memory, not tested, as one does!):

```fsharp
// create chain of input -> Result calls using the railway operator
// an Error anywhere will exit from the chain and can be handled by caller
let getCommentsForRequest (ctx: HttpContext) =
    ctx.GetQueryStringValue "uri"
    >>= getThreadIdForUri
    >>= getCommentsForThreadId    

fun (next : HttpFunc) (ctx : HttpContext) ->
    match getCommentsForRequest ctx with
    | Ok comments -> return! json comments next ctx
    | Error msg -> return! (setStatusCode 404 >=> text msg) next ctx
```

During this exercise, I found F\# Interactive (the built-in repl) super useful
to select and execute blocks of code from my source, Lisp-style, in order to
get my database support up and running.

In terms of the learning journey, I have not even left my own village
yet. However, F\# seems to be triggering all of the right receptors.

# Someone is right on the internet.

*My* week might not have been the most blog-worthy, but, my goodness, the
Wonderful World of Science has not been sitting still!

You see, in desperation I went rummaging through the recent additions to
[JBOP](/2019/03/21/weekly-head-voices-165-get-in-my-pocket/#replacing-pocket-with-just-a-bunch-of-pdfs-jbop),
aka my growing collection of Really Interesting PDFs, and I hand-picked a few
tidbits worthy of casually mentioning during the undoubtedly erudite
discussion at your next cocktail party!

## Each millilitre of VO<sub>2</sub> max reduces your risk of dying by 2.8%.

If we've run (I see what I did there) into each other more than once, [I've
probably
mentioned](/2018/10/23/weekly-head-voices-156-karma-chameleon/#grab-bag-of-thought-and-or-debate-provoking-pieces)
last year's publication of the Cleveland treadmill study where they put 122000
people on a treadmill (the study took 20 years) to show that being unfit on a
treadmill is at least as risky (in terms of you dying) as being a smoker.

Well, last week the result of an even larger Swedish study, with 316137
participants, [were reported at EuroPrevent
2019](https://www.eurekalert.org/pub_releases/2019-04/esoc-mmt040819.php).

With each additional millilitre of oxygen per kilogram of body mass per minute
([VO<sub>2</sub> max, a cardiorespiratory fitness
measure](https://en.wikipedia.org/wiki/VO2_max)), the risk of all-cause
mortality fell by 2.8%, and the risk of cardiovascular events fell by 3.2%.

According to at least [one
source](https://www.topendsports.com/testing/norms/vo2max.htm), the range
between poor and excellent VO<sub>2</sub> max in most age segments for men and
women is 20 millilitres or more.

At 2.8% per millilitre, that certainly makes one think!

## HPV vaccine linked to dramatic drop in cervical disease.

Almost exactly 10 years ago, I wrote [a post on this blog titled "You must
vaccinate"](/2009/05/21/you-must-vaccinate/) because friends and acquaintances
were asking questions which I found surprising on the one hand and quite
alarming on the other.

At that point I thought that even the slowest among us would have caught up to
the fact that there are an extremely large number of good reasons to
vaccinate, and almost none not to.

It seems that I over-estimated the capabilities and size of the slow group...

It is now 10 years later, and the anti-vaxxers have managed to [bring measles
(and some friends) back from
extinction](https://www.who.int/news-room/detail/29-11-2018-measles-cases-spike-globally-due-to-gaps-in-vaccination-coverage).

Fortunately, there is also much to celebrate on the vaccination front.

Scotland started with their human papilomavirus vaccination programme 10 years
ago, administering the vaccine to girls when they are at around 12 years of
age.

Researchers now say that since then the HPV vaccine has ["nearly wiped out
cases of cervical pre-cancer in young
women"](https://www.bbc.com/news/uk-scotland-47803975).

What's also heartening is that unvaccinated women also showed a reduction in
disease, implying that the immunisation programme is protecting even more
humans from the disease due to the herd effect.

(GOU#1 had her HPV shot at school last year. There were parents who
complained. I don't know if there were any refusers.)

I am still hopeful that one day all of these victories will contribute to the
attrition of the irresponsibly dangerous anti-vaxx movement.

## How The Matrix Built A Bullet-Proof Legacy.

Surprise! This one is not from science, but it was such an amazing read that I
have to share.

If, like me, you saw The Matrix more times than you can count, you will also
enjoy this write-up of how the whole project came together:

Extract from the book *How 1999 blew up the Big Screen* by Brian Raftery: [HOW
THE MATRIX BUILT A BULLET-PROOF
LEGACY](https://www.wired.com/story/the-matrix-legacy-book-excerpt/)


# You never write.

At Tuesday's edition of the Helderberg Software Developers and Entrepreneurs
meetup, organised by [Wogan May](https://wogan.blog/) (pssst, he has a
personal blog with mostly weekly updates!) and myself, [Johan
Beyers](http://johan.beyers.co.za/) talked about the personal resolution of
doing a given amount of (personal) writing every day.

I try to do it once weekly with the WHV, and I mostly manage to make a few
bullet points detailing my exploits every day, but the idea of additionally
writing a few more prose-like paragraphs of thoughts every day really
resonates with me.

Derek Sivers (he was a famous startup-person even before the whole startup
boom, thanks [Gerwin de Haan](https://twitter.com/gerwindehaan) for that book
so many years ago!) [makes a good case for writing a few diary-like sentences
every evening](https://sivers.org/dj).

What's even more intriguing, is his suggestion to maintain separate "Thoughts
On" journals for various topics that you think about often. In my case, these
could be for example "Thoughts on Programming Languages", or "Thoughts on
mindfulness for children", or "Thoughts on the WHV rules for a contented
life", and so on.

I think it would be a cunning plan to give both of these additional writing
practices a good go.

Let me know in the comments what you think!

<figure>
<a href="strand_running_clouds_on_mountains.jpg">
{{< img src="strand_running_clouds_on_mountains.jpg" alt="photo taken at postcard cafe" >}}
</a>
<figcaption> 
You've seen photos like these before, but on this very day, I really liked how the clouds
were creating patterns of light and dark created on the mountains in the distance.
</figcaption>
</figure>
