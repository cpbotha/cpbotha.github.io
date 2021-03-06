---
title: 'Weekly Head Voices #151: We are pleased to meet you.'
author: cpbotha
type: post
date: 2018-08-08T06:34:27+00:00
url: /2018/08/08/weekly-head-voices-151-we-are-pleased-to-meet-you/
categories:
  - weekly head voices
tags:
  - apple music
  - backyard philosophy
  - dan luu
  - data science
  - deep learning
  - emacs
  - fibre
  - google colab
  - head voices review
  - jupyter notebook
  - microbiome
  - pytorch
  - rescuetime
  - review
  - side-projects
  - spotify
  - webextension

---
The Weekly Head Voices number 151 are trying to tell you something about the week from Monday July 30 to Sunday August 5.

Prepare yourself for a slightly stranger than usual post. I have: two short programming ideas, a bad review of an outdoor security passive infrared sensor, using Jupyter Notebook for (GPU-accelerated) numerical computation when you only have a browser, computing device input latency, and an utterly unexpected bit of backyard philosophy from the gut.

# Two random micro side-project ideas

I would like to start with two hobby / maker ideas that popped up in my head this week. There’s a high probability I will not get around to them, but perhaps they help you to spawn a new set of hopefully more worthwhile ideas.

## Chrome or Firefox plugin to convert Spotify playlists to Apple Music using the new MusicKit JS API

I seem to see many more Spotify playlists shared than Apple Music playlists. For example, at this moment I’m listening to the official Lowlands 2018 playlist.

This is not ideal, as I am an Apple Music subscriber, but not a Spotify subscriber.

It turns out there are paid apps to convert Spotify playlists to Apple music playlists.

However, it also turns out that Apple has a new thing (still in beta) called [MusicKit JS][1].

I briefly dissected the Spotify Playlist website.

It would be straight-forward for a Chrome or Firefox plugin (WebExtension, so same code. I’ve done this before) to go through this playlist, search for each track using the MusicKit JS API, and then recreate the playlist in the user’s Apple Music account.

This solution would be much cleaner and simpler than the current app-based ones.

## An Emacs package for displaying your RescueTime productivity metric right on the mode line

I scanned the [RescueTime API documentation][2].

I was just about to start working on it, when I came up with the bright idea to name the package ironic.el, and so I stopped.

On that topic: The struggle for practically sustainable focus is real, and it never seems to stop.

# The Head Voices REVIEW(tm) the Optex HX-80 outdoor passive infrared security detector: AVOID AT ALL COSTS

From the [Optex HX-80 outdoor passive infrared security detector’s web-page][3] we have the following:

> **The most important element in reliable outdoor detector is accuracy to distinguish a human from a small animal**. … In addition, the HX-80N’s dual PIR’s and 20 detection zones utilize the ‘AND’ detection pattern technology … **This technology helps to prevent false alarms caused by a pet or small animal.**

Well, I had two of these installed by trained professionals.

(There are of course interesting discussions to be had about the necessity of devices such as the HX-80, or its mythical actually working counterpart, down here.)

I can confirm that they excel at one fairly specific function: Triggering the alarm, and thus automatically calling my security company, at the most ungodly hours of the night, whenever a certain small grey cat, looking exceptionally unlike a human, decides to take a stroll outside of our house.

<div class="jetpack-video-wrapper">
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="473" src="https://www.youtube.com/embed/8ZXAmMroePI?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="840"></iframe></span>
</div>

Oh yes, the cat is not even ours, but belongs to our neighbour.

The installation and subsequent repeated fine-tuning of our Optex HX-80 have only had the result of me having to punch in an additional key-sequence every evening to bypass the two ‘AND’-detection-pattern-technology-equipped HX-80 devices.

You will understand that the only reasonable Head Voices REVIEW(tm) of the Optex HX-80 is:

  * 100% NON-FUNCTIONING THROUGH INFERIOR DESIGN.
  * AVOID AT ALL COSTS.
  * DON’T TRUST THE MARKETING.
  * THE TRUTH IS OUT THERE.
  * JUST DON’T.

![Image result for just don't meme][4]

# Some more odd but perhaps useful bits

## Google Colaboratory for Numerical Computation when all you have is a browser.

I’m late to the party (again), but [Google Colab][5] is really great if you need a Jupyter Notebook with some GPU power behind it.

It comes with tensorflow pre-installed (being Google and all), but getting the GPU-accelerated PyTorch 0.4.1 (latest version of the most amazing deep learning tool at the time of writing) going was a cinch.

{{< figure src="/wp-content/uploads/2018/08/google_colab_torch_0.4.1.png" link="/wp-content/uploads/2018/08/google_colab_torch_0.4.1.png" >}}

To repeat this experiment, create new notebook with File | New Python 3 Notebook, then change Edit | Notebook Settings | Hardware accelerator to GPU.

You can then install the correct version of PyTorch by executing

<pre>!pip install http://download.pytorch.org/whl/cu80/torch-0.4.1-cp36-cp36m-linux_x86_64.whl</pre>

in a notebook cell.

What a time to be alive!

P.S. Remember, [under normal (non-Colab) circumstances][6] we keep our Notebooks as empty as possible. Prefer as much as possible of your code in Python modules. The notebooks are only there to act as glue, for visualization and sometimes for long-running jobs.

## Dan Luu’s computer and mobile device input latency research

[This most amazing work][7] was recently brought to my attention by WHV reader [Matthew Brecher][8] in the comments under my [2017 Android vs iPhone performance post][9].

In it, Dan Luu measured the input latency of various devices, using the 240fps camera on his iPhone SE, or with the 1000 fps  Sony RX100 V camera if the device was too fast.

For the computers in his study, input latency was defined as the time between keypress and character appearing on the display. For the mobile devices, it was defined as the time between finger movement and display scrolling starting.

If you have any interest in this sort of technology and also in-depth technology journalism, [the full article][7] is definitely worth your time.

I wanted to mention two interesting points:

  1. The 1983 Apple 2e, with a CPU running at 1MHz, had significantly lower input latency (30ms between button press and character display) than any modern multi-GHz system. The comparison is of course not completely fair, but it’s still nice to see.
  2. Amongst the mobile devices, Apple dominates the fast / low latency end of the spectrum. Their devices, in terms of input lag, are ALL faster than all of the Android devices tested, including for example the 2017 Google Pixel 2XL. 
      * Yes, this is me eating my hat, and some more of that yummy humble pie.
      * Android 9, code-name Pie, has just been (will soon be… err) released and has an [amazing list of features][10]. I still hope they manage they also manage to catch up with regards to some of the basics like input latency.

## Yet another reason to eat more fibre

There are an [estimated 100 trillion (10 to the power of 14; 100 with 12 zeroes) bacterial cells][11] housed in each of our bodies.

Each adult human consists of on average only 37 trillion human cells, meaning there are on average almost 3 alien cells for every 1 of your own cells.

I find this a beautiful realisation: All aspects of our lives depend on this multitude of foreign visitors.

They help us digest our food, and, as it has been turning out more recently, they play a crucial role in our mood,  our behaviour and our thinking.

We (or at least the clever people) now talk about the [microbiome-gut-brain axis][12], further underlining the importance that our bacterial visitors play in our lives.

Taking a few more steps back, thinking about the relationship between the 37 trillion human cells, and the 100 trillion visiting cells,  I ask the question:

Who am I really? Who exactly is thinking this?

I, or perhaps rather “we”, find this truly fascinating.

What I was initially planning to mention before going off on this tangent, was a recent paper accepted for publication in the Journal of Physiology, with the title Short-Chain Fatty Acids: [Microbial Metabolites That Alleviate Stress-induced Brain-Gut Axis Alterations (click for PDF fulltext)][13].

The Physiological Society press release is more digestibly (I had to) titled “[Eat high fibre foods to reduce effects of stress on gut and behaviour][14]“.

In short, fibre stimulates gut bacteria to produce short-chain fatty acids (SCFA), which, besides being the main source of nutrition for cells in this region of the body, also decrease levels of stress and anxiety, at the very least in mice.

# The end

Thank you for sticking around friends!

I hope that you found something of value, even if not directly from this post.

I’ll see you next time! Until then, remember to eat your vegetables.

 [1]: https://developer.apple.com/documentation/musickitjs
 [2]: https://www.rescuetime.com/apidoc
 [3]: https://www.optexamerica.com/security-products/hx-80n
 [4]: data:image/jpeg;base64,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
 [5]: https://colab.research.google.com/notebooks/welcome.ipynb
 [6]: /2018/07/17/weekly-head-voices-148-data-stylist/#development-environment-pycharm
 [7]: https://danluu.com/input-lag/
 [8]: https://matthewbrecher.com/
 [9]: /2017/02/12/android-vs-iphone-performance-a-quick-note/
 [10]: https://www.theguardian.com/technology/2018/aug/07/android-9-pie-google-new-mobile-os-everything-you-need-to-know
 [11]: https://en.wikipedia.org/wiki/Human_microbiota
 [12]: https://en.wikipedia.org/wiki/Gut%E2%80%93brain_axis
 [13]: https://physoc.onlinelibrary.wiley.com/doi/epdf/10.1113/JP276431
 [14]: http://www.physoc.org/press-release/2018/eat-high-fibre-foods-reduce-effects-stress-gut-and-behaviour
