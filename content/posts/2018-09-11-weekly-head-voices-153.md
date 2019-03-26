---
title: 'Weekly Head Voices #153: pH < 7 dreams.'
author: cpbotha
type: post
date: 2018-09-11T20:17:27+00:00
url: /2018/09/11/weekly-head-voices-153/
categories:
  - weekly head voices
tags:
  - apfs
  - aphex twin
  - benchmarks
  - brave
  - browsers
  - equation
  - formula
  - healthfit
  - runalyze
  - running
  - spectrogram

---
<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/SqayDnQ2wmw?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

Looking back at the week from Monday September 3 to Sunday September 9, I present to you the following memories and after-effects.

# Aphex Twin never left us

I serendipitously ran into T69 Collapse, the brand new track and video by Aphex Twin.

In the grand tradition of WHV intro art, I have embedded the video above.

Whether you&#8217;re a fan or not, I think it&#8217;s worth sitting through this one, preferably with the headphones and the video in full screen.

Pro-tip: This is not one of those tracks where the whole thing can be more or less predicted by viewing the first minute. There&#8217;s a thing at 1:55 and a second thing at 3:14.

I had to wonder whether the [3:14][1] was intentional. We&#8217;re not much into our biblical references over here as you might know, but you have to recall that Aphex Twin is the guy who, already back in 1999, hid his face in the spectrogram of a music track called:


  
\[\Delta M_i^{-1} = -\alpha \sum\limits_{n=1}^N D_i [n] \left[\sum\limits_{j \in C[i]} F_{ji} [n-1] + Fext_i [n^{-1}]\right]\]

That&#8217;s the actual name of the track (#2 on the famous [Windowlicker EP][2]), although most people (plebs!) refer  to it as just _Function_ or _Equation_. I got sucked down that rabbit hole last night, but no-one on the internet seems to know the true meaning of the equation. Please ask RDJ if you ever run into him.

Anyways, I have embedded \(\Delta M_i^{-1} = -\alpha \sum\limits_{n=1}^N D_i [n] \left[\sum\limits_{j \in C[i]} F_{ji} [n-1] + Fext_i [n^{-1}]\right]\) below for your listening and viewing pleasure. Aphex Twin&#8217;s face appears at 5:30.

<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/M9xMuPWAZW8?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

# APFS encryption vs Samsung hardware encryption effective SSD speed

I ran benchmarks on my external Samsung T3 SSD comparing the speed of encrypted APFS to unencrypted APFS with Samsung&#8217;s hardware-based full disk encryption.

I used [AmorphousDiskMark][3], [BlackMagic Disk Speed Test][4] and plain old iostat whilst copying 30GB of files to and from the disk.

There will probably soon be a detailed blog post over on vxlabs.com about this, but I&#8217;ll give you the skinny here:

  * It&#8217;s hard to get benchmarks right. BlackMagic gave wildly varying results depending on how many times I let it run its benchmark for example.
  * APFS&#8217;s software encryption looks like it causes a performance hit ranging from 5 to about 10%, with outliers in both directions.
  * Emacs can calculate over columns of data, for example from iostat&#8217;s standard out, using a simple `M-x calc-grab-from-rectangle` and `M-x calc-vector-mean`.

# Brave browser and the Basic Attention Token (BAT): This could be big. Or not. It&#8217;s at least interesting.

[Brave][5] is a new(ish) browser also based on the Chrome engine.

I knew they were doing something with cryptocurrency, and paying or getting paid for the consumption of content and/or advertising, but I was, as you can see, quite vague on the details.

What I learned last week taking it for a quick spin is the following:

Brave out of the box is massively privacy-focused. Without installing any plugins, it blocks every single advertisement and tracking cookie known to humankind. It also automatically switches to secure SSL wherever that&#8217;s possible.

More interestingly, in Brave you can opt in to &#8220;[Brave Payments][6]&#8220;, which looks like it might soon be renamed to Brave Rewards, but don&#8217;t quote me on that.

One part of this system, is that you as a user contribute a set amount of BAT tokens (these are tokens on the ethereum chain) per month. At the end of each month, Brave will pay out your tokens to the websites that you visited, based on the amount of time you spend on each site.

In this way, publishers can get recompensed for their content in hard cash, without having to resort to advertising. (It does look like Brave also supports the model where advertisers can pay, in BAT tokens of course, for your eyeball time.)

Brave already has 4 million monthly active users (MAU).

If they&#8217;re able to grow this user base, and get a significant portion to participate in the payment system, this could be a game changer. Imagine being able to pay your favourite content creators in this seamless way, and being able to switch off ads in  the process!

# RunAlyze where have you been all my life?

I publish my runs to Strava, as I have a bunch of friends there, and I like the idea of a social network where you have pay with a bucket of sweat before you&#8217;re allowed to say _anything_.

However, I was also relying on Strava to keep track of my shoe mileage. Recently, it started losing the miles I put on my Xero Genesis sandals (the most unforgiving shoes in the universe), and I was not able to coax the system into correctly tracking those terrible, terrible kilometres.

Because I use HealthFit to push my data to Strava, I took a look at some of its other endpoints and then, again extremely serendipitously, ran into:

[RUNALYZE][7]

It&#8217;s a site made by two running nerds (and it **really** shows) from Germany.

It keeps track of my shoes (the goal of this&#8230; _exercise_, bad pun, sorry) but the authors have also implemented a bunch of metrics from academic papers, some metrics of their own, and they show tables of your data sliced and diced in many different ways ON ALL FOUR WALLS of their website.

<Dr Evil voice>It&#8217;s breathtaking.</Dr Evil voice>

Anyways, if you&#8217;re a running nerd too, you should probably take a peek.

# Fin

See you soon brothers and sisters. I am grateful for our time together.

&nbsp;

 [1]: https://en.wikipedia.org/wiki/Matthew_3:14
 [2]: https://en.wikipedia.org/wiki/Windowlicker
 [3]: http://www.katsurashareware.com/pgs/adm.html
 [4]: https://itunes.apple.com/us/app/blackmagic-disk-speed-test/id425264550?mt=12
 [5]: https://brave.com
 [6]: https://brave.com/publishers/
 [7]: https://blog.runalyze.com
