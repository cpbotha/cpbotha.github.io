---
title: 'Android vs iPhone performance: A quick note.'
author: cpbotha
type: post
date: 2017-02-12T13:40:28+00:00
url: /2017/02/12/android-vs-iphone-performance-a-quick-note/
categories:
  - tech
tags:
  - android
  - benchmarks
  - iphone
  - multi-core
  - qualcomm
  - single core
  - snapdragon

---
I've been spending some time doing research on the relative (perceived) performance of flagship Android phones compared to iPhones. I will probably not write the extended post I was planning to, as it seems that it's hard to answer this question scientifically, and, perhaps more importantly, it makes people Very Very Angry.

I would still like to leave you with some interesting reading material. Hence this quick note.

From [this discussion post][1] (December 2016) by CodingHorror, aka Jeff Atwood, one of the two founders of the whole StackOverflow empire, where he measures the relative performance of his discourse web-app, the following choice quote:

> Some Android users report up to about 29 score on very new late 2016 Android
> devices, depending on the vagaries of the browser used. Still below the 2013
> iPhone 5s which can be purchased used for about $150 these days.

That's pretty amazing: Based on the [browserbench speedtest][2], which is supposed to reflect quite realistically real-world web-browsing performance, **the 2013 iPhone 5s outperforms 2016 Android flagships**. Ouch.<figure id="attachment_2808" aria-describedby="caption-attachment-2808" style="width: 300px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench.png" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2808" data-permalink="https://cpbotha.net/2017/02/12/android-vs-iphone-performance-a-quick-note/snapdragon808-browserbench/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench.png" data-orig-size="1440,1158" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="snapdragon808-browserbench" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench-300x241.png" data-large-file="https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench-1024x823.png" class="wp-image-2808 size-medium" src="https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench-300x241.png" width="300" height="241" srcset="https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench-300x241.png 300w, https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench-768x618.png 768w, https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench-1024x823.png 1024w, https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench-1200x965.png 1200w, https://cpbotha.net/wp-content/uploads/2017/02/snapdragon808-browserbench.png 1440w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-2808" class="wp-caption-text">My Snapdragon 808 does a measly 14.7 on browserbench. The iPhone 5s which is a year or two older does more than double that.</figcaption></figure> 

There are more sites where this discussion / flamewar is being continued. Google is your friend.

The core argument is that Apple long ago made the call that fewer, more high performance CPU cores would give the best **subjective** performance. In other words, to a user the phone would feel more responsive.

This does make sense: As a user, when I tap a button, I would like to see an instantaneous response. A single really fast core is going to help more with this than a higher number of slower cores.

Furthermore, programming single-threaded apps is significantly easier than programming robust and efficient multi-threaded apps. You can guess what the apps in the various stores look like in this regard.

The iPhone 6s had only two cores, whereas most mid- to high-range Androids had 6 or more cores when the 6s was released.

The iPhone 7 A10 chip has finally made the jump to 4 cores, two of which are lower power cores. Still, it turns out this chip again [crushes all of its Android (read: Qualcomm) competition][3].

Here's another <a href="https://youtu.be/k_PK_6F_Bhk" data-rel="lightbox-video-0">relevant demo on YouTube </a>where the same set of apps are started up in the same sequence, which is repeated, on both the iPhone 7 and the Samsung S7. All in all, the iPhone manages to get through the exercise more than twice as fast as the S7. This is definitely some indication of how users will perceive the responsivity of these devices.

The argument that multi-core was not a good choice for Android is weakened to an extent by [this recent AnandTech analysis][4] showing that these phones are actually pretty good at utilising all of their cores:

> In the end what we should take away from this analysis is that Android
> devices can make much better use of multi-threading than initially
> expected. There's very solid evidence that not only are 4.4 big.LITTLE
> designs validated, but we also find practical benefits of using 8-core
> "little" designs over similar single-cluster 4-core SoCs.

My personal experience with the Snapdragon 808 (6 core big.LITTLE) in my [BlackBerry PRIV][5] (late 2015 flagship) has been less than stellar. I love the phone for its screen, physical keyboard and other little idiosyncrasies, but the fact that I often have to wait more than a second after tapping an icon or a button before it responds, combined with [the terrible Android security story][6] (where the PRIV paradoxically does quite well), makes me wonder about the future smartphone landscape for Android enthusiasts.

 [1]: https://discuss.emberjs.com/t/why-is-ember-3x-5x-slower-on-android/6577/60
 [2]: http://browserbench.org/Speedometer/
 [3]: http://bgr.com/2016/10/21/iphone-7-specs-a10-fusion-processor/
 [4]: http://www.anandtech.com/show/9518/the-mobile-cpu-corecount-debate
 [5]: http://www.gsmarena.com/blackberry_priv-7587.php
 [6]: /2016/11/27/android-security-in-2016-is-a-mess/
