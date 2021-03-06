---
title: 'Weekly Head Voices #146: You too can learn Kung Fu.'
author: cpbotha
type: post
date: 2018-06-18T21:24:40+00:00
url: /2018/06/18/weekly-head-voices-146-you-too-can-learn-kung-fu/
categories:
  - weekly head voices
tags:
  - AI
  - barefoot
  - common lisp
  - cryptocurrency
  - emacs
  - ether
  - ethereum
  - harald eia
  - kung fu
  - lisp
  - running
  - social democracy
  - socialism
  - tedx
  - the matrix

---
_This post covers the period Monday June 11 to Sunday June 17. Read it to become rich, yawn at Lisp and Emacs, yearn to run free on the wide open plains and to learn Kung Fu. Not ambitious at all._
{{< figure src="/wp-content/uploads/2018/06/IMG_2004-768x1024.jpg" link="/wp-content/uploads/2018/06/IMG_2004.jpg" caption="Front door nearby De Waal Park, in Cape Town. Photo taken on Sunday by GOU#1, age 12.">}} 

# Social Democracy FTW

It turns out that your chances of becoming rich are the greatest if you had the good fortune to have been born in one of the Nordic social democracies, such as Norway, Sweden or Denmark.

The US trails these countries, at position 13, in terms of per capita individuals with net worth over $30 million.

<div class="jetpack-video-wrapper">
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="473" src="https://www.youtube.com/embed/A9UmdY0E8hU?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="840"></iframe></span>
</div>

Being a proponent of social democracy as the most humane form of currently practical human government, and often infuriating conservatives   by pointing out that many crucial aspects of social democracies can be described as socialistic, I really enjoyed the linked TEDx talk by Norwegian [Harald Eia][1].

This material will serve me well as the source of future mischief.

# Paradigms of AI Programming in Common Lisp

I am currently working my way through [“Paradigms of Artificial Intelligence Programming: Case Studies in Common Lisp”][2], Peter Norvig’s famous 1992 book an artificial intelligence. Although modern AI has been transformed almost unrecognisably since then (THANKS DEEP LEARNING! [Norvig’s PAIP retrospective][3]) the way in which Norvig uses Lisp to model and solve real-world problems is inspiring and quite foundational.

It’s not only that though.

My inconvenient but uncontrollable infatuation with Common Lisp also seems to be pulling the strings. I should study a real language which is not 60 years old, like Rust or something.

What attracts me about Common Lisp is the liberated and pragmatic way in which it enables one to mix functional, object-oriented and procedural programming, and, perhaps most importantly, how it was designed from the ground up for iterative and interactive programming.

Tweak the defun, eval the defun, watch the system adapt. This is what I always imagined programming would be like. Except for the Lisps, it really turned out perhaps a bit more boring than it really needs to be.

## interleave-mode for working through PDF books

For the fellow Emacs users, I also wanted to mention the utility of [interleave-mode][4] for working through such a programming book, if you can find it in PDF format.

In my Emacs I have the PDF on the left, and my interleave-mode-linked orgfile on the right. On any page of the PDF I hit the i-button to add a note in the orgfile, where I can of course insert and execute live code snippets.

The sections in the orgfile remain linked to the correct pages of the PDF.

For programming books this is an amazing combination. For studying other books, having your orgfile notes linked will probably also be quite useful.

On the topic of note-taking: This past week, on Friday June 15 (I made a note of that), I was able to help a colleague solve a technical problem by searching for and retrieving an org-file note, including detailed configuration settings, that I made on May 13, 2014.

# Ether as currency

Although I acquired a small amount of the Ether cryptocurrency for the first time in July of 2016, I’ve never had the opportunity to actually transact with it.

Up to now, it has functioned solely as a pretty volatile store of value.

On Saturday, I used some ether for the first time to straight-up buy something on the internet, which was a pretty exciting but in practice an uneventful procedure, fortunately.

The vendor used a payment processor which presented me with an address and corresponding QR code. I scanned the QR code with the relevant mobile app (Luno in this case), paid the requested amount, and waited for a few minutes for it to be multiply confirmed by the blockchain. The sending fee was about 0.04% of the transaction.

# Barefoot-style running update

On Sunday I went for a long(ish) run, bringing my total on the Luna sandals to just over 200km.

My feet, ankles and calves are much stronger than they used to be, but the barefoot conversion is clearly still has some ways to go. I have to take at the very least two rest days (instead of one) between runs to give my feet some extra time to recover.

What I have recently started doing, is that instead of trying to micro-manage my form (put your foot down like this, bend your ankle like that, let your achilles tendon shoot back like this, and so on), I am following the advice of some _new_ random person on [reddit/r/BarefootRunning][5] who gave the advice, often echoed elsewhere by barefoot-runners, to try and maintain a cadence (steps-per-minute) of at least 180.

That sounds pretty high for a normal person like me, but it turns out that when I do that, and I try at the same time to run as silently as possible (I often just APPEAR right beside someone, hehe), my legs and feet figure out their elastic bio-kinematics all by themselves.

As yet another random reddit expert (I wish I could find the post) quipped:

> You can’t overthink proprioception.

(that’s a running nerd joke)

# I know Kung Fu

Do you remember this scene from The Matrix (1999)?

<div class="jetpack-video-wrapper">
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="473" src="https://www.youtube.com/embed/V8ZdGmgj0PQ?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="840"></iframe></span>
</div>

The other day at the [Old People Reunion][6], friend T. Monster, a highly capable pragmatist but also backyard theoretician, talked about how often it happened these days that you had to deal with some DIY issue, tapped or spoke the question into youtube, watched a video or two, and then fixed the issue like a pro.

This, along with my recent pseudo-expert repair of a number of stripped cabinet hinge screw holes with tooth picks and cold glue (this works, I kid you not), made me think that, although The Matrix version was perhaps far more spectacular, we in fact now find ourselves in a _real, shared reality_ where a large subset of skills can be acquired _a la carte_.

Some may take longer than a few minutes, but it still is pretty amazing how far YouTube has managed to democratise so many different forms of modern Kung Fu.

 

 

 [1]: https://en.wikipedia.org/wiki/Harald_Eia
 [2]: https://github.com/norvig/paip-lisp
 [3]: http://norvig.com/Lisp-retro.html
 [4]: https://github.com/rudolfochrist/interleave
 [5]: https://www.reddit.com/r/BarefootRunning/
 [6]: /2018/06/03/weekly-head-voices-144-eternal-learner/#reunion
