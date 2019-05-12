---
title: "Weekly Head Voices #170: Yeet."
slug: "weekly-head-voices-170-yeet"
author: cpbotha
date: 2019-05-07T22:02:00+02:00
tags:
  - devide
  - emacs
  - emoji
  - GOUs
  - laptop
  - gen z
  - endgame
  - sleep
  - matthew walker
  - yuval harari
  - homo deus
  - peter attia
  - yeet
categories:
  - weekly head voices
type: "post"
---

Hello there friends!

This edition of the WHV, number 170, is how I choose look back at the three
weeks from Monday April 15 to Sunday May 5, 2019.

This period was host to whooshing-by-deadline-induced stress, one amazing and
thought-provoking wedding, the birthdays of two of my GOUs, and, a bit
strangely part of this list, the acquisition of a new computing device.

At least we were able to pause everything for a sublime afternoon at a
favourite vineyard close to my backyard:

<figure>
<a href="lourensford_cellar_skies.jpg">
{{< img src="lourensford_cellar_skies.jpg" >}}
</a>
<figcaption>
I ended the three week WHV-hiatus in this place, together with my
fam jam<sup>*</sup>. It was lit.
</figcaption>
</figure>

# A brief but educational interlude: HOW TO SPEAK GEN Z.

I too did not know what "fam jam" meant until I viewed the educational video
below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/YtrxVWf91Jo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

I feel like I understand my budding teenager (GOU#1) a little better now.

On a related note: GOU#1 and I went to watch End Game together, on her 13th
birthday.

This is the first time I've been in a cinema since forever, as I usually find
it hard to justify the time expense.

In this case however, the film, but far more importantly my company and the
special occasion, made it doubly worth it.

P.S. Dumbledore doesn't make it. 😢

P.P.S. That emoji comes straight from my Emacs! (It comes as a bit of a
surprise to me that I am quite excited by how our systems of written
communication are evolving.)

P.P.P.S. If you too want your Emacs to do this, add the following to your `init.el`:

```emacs-lisp
;; 💪💪💪
(use-package emojify
  :ensure t
  :config
  (emojify-set-emoji-styles '(unicode))
  (global-emojify-mode)
  (global-set-key (kbd "C-x 8 e") 'emojify-insert-emoji))
```

# The other blog posts I did get around to writing.

Perhaps unbeknownst to you, I was not completely quiet on the blogging front.

I produced the following four posts, the latter three of which will have to
live on the nerdy sister blog:

- [meepx1e: I haz new laptop!](/2019/04/27/new-laptop-2019/) - The traditional
  welcome-new-computer-to-my-household post on this blog.
- [Using the new dotnet fsi from .NET Core 3 Preview 3 in Visual Studio
  Code](https://vxlabs.com/2019/04/16/dotnet-fsi-in-vscode/) - A modest trick
  for an improved F# repl.
- [PyCharm and Docker Compose for Django and TypeScript development on Windows
  10](https://vxlabs.com/2019/04/19/django-typescript-docker-compose-windows/) -
  You can run your Linux inside of Microsoft-supported Docker containers on
  your Windows laptop. How times have changed...
- [Link directly to emails from Emacs Orgmode using Thunderbird and
  Thunderlink](https://vxlabs.com/2019/04/20/link-thunderbird-emails-from-emacs-orgmode/) -
  This is a core part of my task management workflows. On macOS it worked more
  or less out of the box, on Windows and Linux you have to get your hands
  dirty.

# The easiest but most high impact measure you can take to not die too soon: Go to bed on time.

[I've mentioned Matthew Walker, the increasingly world-renowned Professor of
Sleep Science, on this blog
before](/2017/12/29/the-2017-to-2018-transition-post/).

I'm currently working through a three-part podcast between [Dr Peter Attia
MD](https://peterattiamd.com), life optimisation expert with the
hyper-analytical accent(tm), and Prof. Walker, and it is absolutely
*fascinating*.

Several times now, points discussed by the two gentleman have made me go
"OH. MY. GOODNESS." in the car between home, the daily school-run and work.

The long and the short of it is that although we so easily trade away sleep for
an extra hour of work, or even worse to assuage pangs of guilt at not working
enough during the day, that sleep is one of the most crucial components of
one's health.

Looking at it from a different angle, and one which Walker is not scared to
take, probably because it is so critical, lack of sleep has terrifyingly
deleterious effects on human health.

Anyways, if you're looking for a thought-provoking conversation, you could
easily do worse than this.

- Part 1: https://peterattiamd.com/matthewwalker1/
- Part 2: https://peterattiamd.com/matthewwalker2/
- Part 3: https://peterattiamd.com/matthewwalker3/

If you don't have the opportunity to listen to the podcast, perhaps because you
need to catch up on your sleep, [this 2017 article in The
Guardian](https://www.theguardian.com/lifeandstyle/2017/sep/24/why-lack-of-sleep-health-worst-enemy-matthew-walker-why-we-sleep)
is a great summary.

# The Edge of Humanity.

(Not interested in hearing about sleep? How about existential risks that
threaten the continued existence of our species? Here at the WHV we like to
keep the issues light and light-hearted!)

_Homo Deus_ by Yuval Harari is one of those books I really think _everyone_
should read. This is such a fantastic and broad treatise on where we came from,
and where we might be going.

I am happy that we have the privilege of Harari as the superbly articulate
thinker that he is.

This discussion between Yuval Harari and Sam Harris, available as [podcast #138
on Sam Harris's website](https://samharris.org/podcasts/138-edge-humanity/), is
both valuable and highly entertaining.

Besides the moment at about 32 minutes in when Harari made the case that all of
the large scale media manipulation and user data mining demonstrate that the
human mind is now indeed hackable (!!), I wanted to mention the
thought-provoking topic of how comically out of their depth our political
leaders are.

They don't seem to be able to do much more than _react_ to short-term fears and
impulses (which they also play to), and as if that was not bad enough, they do
so with an horizon of not much more than about four years.

How many of our leaders would be able to field convincingly the question of
what their plans were, what their _vision_ is for humanity, for the coming 40
years?

What *is* our 40 year grand plan for energy, for the environment, for poverty,
and for preventing another world war?

Please give your answers in the comments.

# A strange thing happened this weekend.

During my time at the TU Delft, I made and maintained a software tool called
DeVIDE, or the *Delft Visualisation and Image Processing Development
Environment*, or *Not Responding* as it was called by *some* of its users.

Development started in 2002, the first open source release was in 2007 and the
last release was in 2012.

(You can still download working binaries of the 2012 release from the
[downloads page](https://github.com/cpbotha/devide/wiki/Downloads). It was
pretty strong on loading chaotic collections of DICOM images, and it was pretty
strong on enabling users to talk to almost any part of it in Python, at
runtime. Frits Post and I published a [paper in 2008 which nicely summarised
the interesting parts of the
software](https://www.semanticscholar.org/paper/Hybrid-Scheduling-in-the-DeVIDE-Dataflow-Botha-Post/a96cc2530609d46d9a39f5884d8a9f8192991114).)

When [I left the TU and
academia](/2013/03/09/dear-academia-i-hope-we-can-still-be-friends/), my work
positively careened off in a different direction and it became more or less
impossible for me to justify continuing to maintain DeVIDE.

Fast forward a few years, and due to Project Z I'm again all up in the
[DICOMs](https://www.dicomlibrary.com/dicom/).

More acutely however, I feel the need for creatively implemented projective
geometry.

Well, my weekend brain got behind the steering wheel, and before I knew it I
was staring at the DeVIDE UI, all prettied up with Python 3 and VTK 8.2:

<figure>
<a href="devide2019-screenshot-20190505.png">
{{< img src="devide2019-screenshot-20190505.png" >}}
</a>
</figure>

At this moment it's only a limping shadow of its previous self, but it still
managed to bring back so many warm memories.

With a few hours more of work, it could start becoming useful again.

I'm not entirely sure where weekend-brain wanted to go with this. We'll have to
wait until he gets back to see.

# 🙏🙏🙏

Friends, thank you for connecting with me here in these words and symbols.

I am already looking forward to the next time that we meet!
