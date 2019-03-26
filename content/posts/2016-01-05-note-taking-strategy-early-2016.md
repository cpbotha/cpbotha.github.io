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
I&#8217;m probably what one might call an obsessive note-taker.

I&#8217;ve [talked in the past about the importance of keeping a lab journal.][1] Initially I produced a stack of books filled with hand-scribbled notes. Although this is my favourite authoring modality, the fact that such notes can&#8217;t be easily indexed and queried (maybe one day?!) soon leads one to try electronic solutions. Over the years I&#8217;ve [experimented with a number of different tools][2] (see under &#8220;Nerd News&#8221;) to do this.

This post summarises my current selection of tools.

For making notes with a visual aspect, for example photos of beers that I&#8217;ve tasted, and sometimes screenshots of websites, I use [Google Keep][3]. This has a really great Android app with which you can easily save a website, including screenshot, using the Android &#8220;share with&#8221; functionality. On the desktop, this has a web-app that looks like this:

<a href="https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie.jpg" rel="attachment wp-att-2307" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2307" data-permalink="https://cpbotha.net/2016/01/05/note-taking-strategy-early-2016/keep_screenie/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie.jpg" data-orig-size="835,1083" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="keep_screenie" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie-231x300.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie-790x1024.jpg" class="alignnone size-medium wp-image-2307" src="https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie-231x300.jpg" alt="keep_screenie" width="231" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie-231x300.jpg 231w, https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie-768x996.jpg 768w, https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie-790x1024.jpg 790w, https://cpbotha.net/wp-content/uploads/2016/01/keep_screenie.jpg 835w" sizes="(max-width: 231px) 85vw, 231px" /></a>

One of the neat features of Keep is that you can easily have it extract and OCR text from images, for example if you&#8217;ve taken a photo of a business card. Unfortunately, the web-app is quite sluggish (this could be because I live in a bandwidth-constrained world here at the southern tip of Africa), and there&#8217;s no web clipper with which I can easily save web pages whilst on the desktop. Furthermore, I find the layout to be quite chaotic, and therefore I treat it more like my similarly chaotic digital cork board.

After a two year hiatus, I&#8217;ve returned to the [SimpleNote universe][4] as my **core mobile and desktop note-taking tool**. They have great apps on IOS, Android, Mac and Web. I use the super sleek, some might say austere, [SimpleNote Android app][5] (recently rewritten when [Automattic][6], makers of WordPress, bought Simperium, makers of SimpleNote) and on the desktop I mostly use [nvpy, my open source SimpleNote client][7]. The latest greatest version (0.10.0, soon to be released) looks like this:

<a href="https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie.png" rel="attachment wp-att-2308" data-rel="lightbox-image-1" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2308" data-permalink="https://cpbotha.net/2016/01/05/note-taking-strategy-early-2016/nvpy_screenie/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie.png" data-orig-size="1008,679" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="nvpy_screenie" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie-300x202.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie.png" class="alignnone size-medium wp-image-2308" src="https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie-300x202.png" alt="nvpy_screenie" width="300" height="202" srcset="https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie-300x202.png 300w, https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie-768x517.png 768w, https://cpbotha.net/wp-content/uploads/2016/01/nvpy_screenie.png 1008w" sizes="(max-width: 300px) 85vw, 300px" /></a>

Because SimpleNote is text-only, and it&#8217;s a fully synced offline-capable tool, it&#8217;s nice and fast. This is the tool you want to use to store those small but useful factoids, quotes and code snippets.

For more in-depth and technical lab journals, I use GNU Emacs with [Org mode][8]. This enables me to write documents with beautifully typeset math, syntax-highlighted and in some cases even live-evaluated code blocks, and good document structure, all in plain text. Here&#8217;s a sample of my November 2015 lab journal where I started reading about and experimenting with a bit of D language:

<a href="https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie.png" rel="attachment wp-att-2309" data-rel="lightbox-image-2" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2309" data-permalink="https://cpbotha.net/2016/01/05/note-taking-strategy-early-2016/emacs_orgmode_screenie/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie.png" data-orig-size="896,997" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="emacs_orgmode_screenie" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie-270x300.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie.png" class="alignnone size-medium wp-image-2309" src="https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie-270x300.png" alt="emacs_orgmode_screenie" width="270" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie-270x300.png 270w, https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie-768x855.png 768w, https://cpbotha.net/wp-content/uploads/2016/01/emacs_orgmode_screenie.png 896w" sizes="(max-width: 270px) 85vw, 270px" /></a>

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
