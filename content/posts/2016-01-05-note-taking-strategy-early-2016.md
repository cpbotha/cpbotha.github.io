---
title: Note-taking strategy early 2016
author: cpbotha
type: post
date: 2016-01-05T20:23:48+00:00
url: /2016/01/05/note-taking-strategy-early-2016/
categories:
  - tech
tags:
  - emacs
  - keep
  - lab journal
  - note-taking
  - nvpy
  - simplenote
  - tabletops

---
I’m probably what one might call an obsessive note-taker.

I’ve [talked in the past about the importance of keeping a lab journal.][1] Initially I produced a stack of books filled with hand-scribbled notes. Although this is my favourite authoring modality, the fact that such notes can’t be easily indexed and queried (maybe one day?!) soon leads one to try electronic solutions. Over the years I’ve [experimented with a number of different tools][2] (see under “Nerd News”) to do this.

This post summarises my current selection of tools.

For making notes with a visual aspect, for example photos of beers that I’ve tasted, and sometimes screenshots of websites, I use [Google Keep][3]. This has a really great Android app with which you can easily save a website, including screenshot, using the Android “share with” functionality. On the desktop, this has a web-app that looks like this:

{{< figure src="/wp-content/uploads/2016/01/keep_screenie-790x1024.jpg" link="/wp-content/uploads/2016/01/keep_screenie.jpg" >}}

One of the neat features of Keep is that you can easily have it extract and OCR text from images, for example if you’ve taken a photo of a business card. Unfortunately, the web-app is quite sluggish (this could be because I live in a bandwidth-constrained world here at the southern tip of Africa), and there’s no web clipper with which I can easily save web pages whilst on the desktop. Furthermore, I find the layout to be quite chaotic, and therefore I treat it more like my similarly chaotic digital cork board.

After a two year hiatus, I’ve returned to the [SimpleNote universe][4] as my **core mobile and desktop note-taking tool**. They have great apps on IOS, Android, Mac and Web. I use the super sleek, some might say austere, [SimpleNote Android app][5] (recently rewritten when [Automattic][6], makers of WordPress, bought Simperium, makers of SimpleNote) and on the desktop I mostly use [nvpy, my open source SimpleNote client][7]. The latest greatest version (0.10.0, soon to be released) looks like this:

{{< figure src="/wp-content/uploads/2016/01/nvpy_screenie.png" link="/wp-content/uploads/2016/01/nvpy_screenie.png" >}}

Because SimpleNote is text-only, and it’s a fully synced offline-capable tool, it’s nice and fast. This is the tool you want to use to store those small but useful factoids, quotes and code snippets.

For more in-depth and technical lab journals, I use GNU Emacs with [Org mode][8]. This enables me to write documents with beautifully typeset math, syntax-highlighted and in some cases even live-evaluated code blocks, and good document structure, all in plain text. Here’s a sample of my November 2015 lab journal where I started reading about and experimenting with a bit of D language:

{{< figure src="/wp-content/uploads/2016/01/emacs_orgmode_screenie.png" link="/wp-content/uploads/2016/01/emacs_orgmode_screenie.png" >}}

Parts of these journals [can be sent directly to your WordPress blog from within Emacs][9], and you can generate high quality PDFs at the press of a typical simple 12 key Emacs shortcut combo. This being Emacs, the experience can be easily customised to emulate SimpleNote in terms of interactivity, but this will not easily compete with SimpleNote proper in terms of transparent syncing between all devices and in terms of accessibility on mobile.

Using these three tools together currently takes good care of my note-taking requirements. However, I think that there might be room for a fourth type of tool that is more visual, supports rich and graphical linking between data items and even between sub-components of such items and, perhaps most importantly, enables us to build note landscapes that are natively as non-linear as our thoughts.

 [1]: https://cpbotha.net/2011/02/19/on-the-importance-of-taking-notes-weekly-head-voices-38/
 [2]: https://cpbotha.net/2011/07/02/the-monthly-weekly-head-voices-50/
 [3]: https://www.google.com/keep/
 [4]: http://simplenote.com/
 [5]: https://play.google.com/store/apps/details?id=com.automattic.simplenote
 [6]: https://automattic.com/
 [7]: https://github.com/cpbotha/nvpy
 [8]: http://orgmode.org/
 [9]: https://vxlabs.com/2014/05/25/emacs-24-with-prelude-org2blog-and-wordpress/
