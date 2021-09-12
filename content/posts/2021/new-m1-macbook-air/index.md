+++
title = "New Emacs-capable hardware: M1 MacBook Air"
date = 2021-03-21T21:49:00+02:00
lastmod = 2021-04-15T08:29:29+02:00
tags = ["apple", "context", "emacs", "m1", "macbook", "new computer"]
categories = ["nerd"]
draft = false
author = "Charl P. Botha"
ogimage = "m1-macbook-air-about.png"
org = true
+++

You know the drill here at the WHV: If there's a new computer in the family, I
usually write a little something about it.

These mentions and posts go back to at least 2002, and now I've back-tagged
most of them so that you can see them all in this convenient ["new computer" tag
list](/tags/new-computer/)!


## Fast, cheap and energy efficient: Choose three {#fast-cheap-and-energy-efficient-choose-three}

This time, I, or rather my employer, had difficulty resisting the siren song of
the new [Apple M1 chip](https://en.wikipedia.org/wiki/Apple%5FM1) and especially of the entry-level M1 MacBook Air: Great
performance and power efficiency in a truly cool and quiet package.

{{< figure src="m1-macbook-air-about.png" link="m1-macbook-air-about.png" >}}

I'm still _quite_ happy with the [ThinkPad X1 Extreme Gen1](/2019/04/27/new-laptop-2019/) as my main
workstation, but although classed as thin-and-light it _is_ still a
workstation.

Specifically, due to the fact that it takes at least a minute or two to resume
from sleep, and the fact that its performance on battery is substantially
slower than on AC, it's not the sort of machine that you can flip open to work
on when inspiration strikes.

As if that was not enough, it's a really effective lap warmer, and so gets
uncomfortable _quite_ quickly.

In sharp contrast, the performance of this MacBook Air is the same, namely
"super snappy", whether it's on AC or on battery, the laptop resumes from
standby faster that I'm able to open the lid, and it hardly ever gets warm.

In short, I can bust this out of my bag and be typing on my lap in under 3
seconds, and this is something that has already started paying off in terms of
my writing.


## This might be the best Emacs-host I've ever used {#this-might-be-the-best-emacs-host-i-ve-ever-used}

This very post is currently being typed on `GNU Emacs 27.1.91 (build 1,
arm-apple-darwin20.3.0, Carbon Version 164 AppKit 2022.3) of 2021-03-15` on the
device in question.

Have I mentioned "super snappy"?

By the way, if you build Emacs like this on the M1:

```shell
brew tap railwaycat/emacsmacport
brew install --formula emacs-mac --HEAD
```

... you should be good to go.


### Update on 2021-04-15 {#update-on-2021-04-15}

A few days ago, I started seeing the following error during homebrew Emacs update:

```text
./temacs --batch  -l loadup --temacs=pbootstrap
make[1]: *** [bootstrap-emacs.pdmp] Killed: 9
make: *** [src] Error 2
```

This looks similar to [this github issue on emacs-plus](https://github.com/d12frosted/homebrew-emacs-plus/issues/292), which was fixed on emacs
master.

It was easiest for me to switch to emacs-plus, which went like this:

```shell
brew uninstall emacs-mac
brew tap d12frosted/emacs-plus
brew install emacs-plus@28 --with-no-titlebar
```


## Quo vadis, one device to rule them all? {#quo-vadis-one-device-to-rule-them-all}

It's a pity that the ThinkPad, although powerful enough to satisfy [my single
computing device / single context requirement](/2020/05/20/weekly-head-voices-195-pragmatic/#the-story-behind-this-story-one-context-to-rule-them-all), and with [WSL2 becoming
increasingly useful](/2020/09/16/weekly-head-voices-204-what-is-your-purpose/#wsl2-and-nativecomp-emacs-workflow-update) and hence addressing the dual-boot issue, does not satisfy
the _instantly available_ requirement.

Fortunately the two devices cater for complementary contexts.

The Air is for instant-on writing, communication, admin and maybe a tiny bit of
development, whilst the ThinkPad is for all of the heavy lifting, but who knows
how these lines are going to be blurred in the coming months?
