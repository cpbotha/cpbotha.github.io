+++
title = "Weekly Head Voices #250: Durable, blissful contentment"
date = 2022-12-06T22:29:00+02:00
publishDate = 2022-12-06T00:00:00+02:00
lastmod = 2022-12-10T14:27:22+02:00
slug = "weekly-head-voices-250-durable-blissful-contentment"
tags = ["contentment", "happiness", "machine learning", "sam harris"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
org = true
ogimage = "bettys-sunset-colours.jpg"
+++

This, the quarter-thousandth edition of the Weekly Head Voices, covers two
weeks from Monday November 21 to Sunday December 4, 2022.

{{< figure src="bettys-sunset-colours.jpg" caption="<span class=\"figure-number\">Figure 1: </span>The sunset colours in Betty's were beautiful that day." link="bettys-sunset-colours.jpg" >}}

I am happy that my ever-evolving life philosophy (as well as my approach to
health and wellness) includes a growing section on the importance of hard and
challenging work with great colleagues, because these past few weeks have
really been delivering in that respect.

The rest of this post consists of two main parts: The first is a nerdy bit
about the ease of doing state-of-the-art multi-lingual speech-to-text
transcription on your own computer, and the second is about not being happy.


## An applied machine learning prelude {#an-applied-machine-learning-prelude}

A few months ago, I listened to a podcast with Sam Harris and Morgan Housel,
titled, quite uncharacteristically for Harris podcasts, "Wealth Matters".

Hidden between all of the money- and economics-related information, they
started to talk about human well-being, and specifically about happiness vs
contentment.

As I was driving, a few specific words by Sam Harris dealing with the modest
but robust bliss in everyday contentment really hit home for me.

I made a mental note to find the spot in question later, and then to transcribe
it for this blog.

It went the way of many of my mental notes made while driving and listening to
podcasts... floating peacefully and oblivious somewhere in my brain.

... until last week, when the mental note surfaced (!!).

First I graduated the mental note into my Emacs Org mode notes. A few days
later I tracked down the interview in question (man, that Waking Up app has
great content, but it's usability has much room for improvement (low hanging
fruit include 1. automatically continuing current listening and 2. better
search)) and made another note, which on its part led to me sitting down a bit
later with my phone, trying to find the correct spot in the 2 hour podcast.

Fortunately, two attempts got me to the desired segment at 48m55s.

At that point, I could have just manually transcribed the speech in question,
but it turned out to be a longer segment than expected, and then a little voice
(haha) reminded me of [the recent release of OpenAI's multi-lingual
text-to-speech neural network model called Whisper](https://openai.com/blog/whisper/).

In spite of XKCD's extremely valuable [lessons on when you should or shouldn't
automate a thing](https://xkcd.com/1205/), I decided that there was a learning opportunity here and so
I git cloned (nerd for "downloaded") the [Whisper source code](https://github.com/openai/whisper).

It took me the most of the time to get the required GPU-capable packages on
Windows, where my RTX 2070 lives (I had to revert to miniforge and conda, see
`environment.yml` below), and then to record the 6.5 minute audio segment from my
phone using the external microphone on my PC with Audacity (this was the only
way to get the audio out of the app).

Once that was done, Whisper took about a minute (64 seconds to be exact) to
transcribe the 6.5 minutes into absolutely _flawless_, timestamped English text.

I was quite flabbergasted.

It is now possible to download a pretty compact neural network to your own PC,
and then to use that model to transcribe automatically any number of spoken
languages, optionally also translating in the process.


### environment.yml for mamba {#environment-dot-yml-for-mamba}

```yaml
# mamba env update
# conda activate whisper
# whisper --language English name_of_your.mp3
name: whisper

channels:
  - pytorch
  - nvidia
dependencies:
  - python=3.10
  - pip
  - pytorch
  - torchvision
  - torchaudio
  - pytorch-cuda=11.7
  - pip:
    - git+https://github.com/openai/whisper.git
```


## Happiness is a joke {#happiness-is-a-joke}

The section that really hit home for me is the one in response to this
statement by Morgan Housel, the interview guest:

> That difference between happiness and satisfaction is really key and easy to
> overlook.  Happiness, like I said earlier, is a very fleeting emotion.
>
> I use the example of, like, if I told you the funniest joke in the world,
> you've never heard a funniest joke, you would laugh for 30 seconds, and then
> you'd be over it.
>
> And if I told you that joke every day, you'd get sick of it, even if it was the
> best joke in the world.
>
> Happiness is like that as well, and therefore I think the most that we can aim
> for, the best we can aim for, is contentment.
>
> ...
>
> But when people chase happiness, I think that's when people are setting
> themselves up for disappointment, because no matter how funny the joke is, so
> to speak, it's a fleeting emotion that sticks around for just very brief
> moments before you revert to something else.

I'm not a fan of analogies, because they have the tendency to distract folks
from the core of the discussion at hand. In the worst case, people think they
understand the issue because they understand the analogy.

However, here we can say that the world's funniest joke would indeed probably
be as fleeting as that feeling of happiness.

I have heard people joke about Sam Harris, saying he is one of the few humans
who is able to "speak in full paragraphs".

His off-the-cuff response, the transcription of which is shown below with my
emphasis, indeed seems to demonstrate that quality.

> Yeah, I'm a big fan of thinking of well-being in terms of a kind of a **larger
> footprint of contentment and equanimity and peace**, you know, non-conflict, as
> opposed to the more transitory, hotter experiences of joy and happiness.
>
> I mean, joy is a fleeting emotion.
>
> It's not to say it's not important, and we don't love it.  But there's a kind
> of a background context of just not having a problem, which is certainly
> underrated.
>
> It's not something people tend to, when they think of living their best
> possible life, people tend to think about joy and fun and even, you know,
> ecstasy, and they get bored with words like contentment or peace or equanimity.
>
> And yet, really, when you just look at it, when you study the nature of your
> own psychological suffering, really, **the thing that is durable, the thing that
> is achievable and, you know, truly enviable**, if you don't have it, **is
> contentment**, and it can **deepen to the point where, you know, there's a blissful
> component to it**, and it's born of **not craving things that are not here in this
> moment**, right?

I've [mentioned at least once before my preference for contentment over
happiness](/2017/07/30/weekly-head-voices-124-ceci-nest-pas-dennui/), although I then also cited opinions to the effect that even
contentment was not possible, but I really like the way Sam so eloquently
combines the achievability, the robustness, and _especially_ the bliss that can
be obtained through contentment, which itself can be cultivated through the
active practice of filling the current moment with your full and deliberate
presence.


## P.S. about A.I. {#p-dot-s-dot-about-a-dot-i-dot}

With the current excitement over all of the applied Large Language Models
(LLMS), especially around the meteoric rise of [ChatGPT](https://openai.com/blog/chatgpt/), I have resolved to
maintain this blog as a shining example of 100% ad-free and human (namely
me)-generated content.

I have nothing against applying ML, but personally I prefer my blogs as
personal as possible.

It is quite poetic that after making that resolution, I did enlist the help of
an ML model to transcribe the speech in the previous section.

Thinking about this some more, who knows how I might use ML in the future to
help me answer questions, whilst still experiencing that it is truly _me_ who
ends up writing these words.

These distinctions are already quite blurry.

With the technology and its context evolving so rapidly, there's no telling
where this journey will take us.
