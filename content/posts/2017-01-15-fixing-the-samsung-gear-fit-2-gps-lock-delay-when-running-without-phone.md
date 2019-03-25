---
title: Fixing the Samsung Gear Fit 2 GPS lock delay when running without phone
author: cpbotha
type: post
date: 2017-01-15T08:37:51+00:00
url: /2017/01/15/fixing-the-samsung-gear-fit-2-gps-lock-delay-when-running-without-phone/
categories:
  - howto
tags:
  - gadgets
  - gps
  - running
  - samsung
  - samsung gear fit 2

---
For the past few runs, I noticed that my Gear Fit 2 would only lock onto GPS after more than 0.5 km. By &#8220;noticed&#8221;, I of course mean &#8220;got super frustrated with and considered briefly throwing the gadget onto the ground and arranging for its utter disintegration through repeated jumping on it&#8221;.

Besides losing the first 0.5 km of my run data, the pacing information, delivered via synthesised voice, would be wildly inaccurate for the rest of my run.

Judging by [this 22 page thread on the Samsung community forums][1], there are other users who were also less than happy that the Gear Fit 2 built-in GPS does not seem to work as advertised. Understandably, people bought the gadget in order to be able to go running without having to lug their smartphones along.

Fortunately, it turns out the explanation is quite logical, although Samsung really has to do better to communicate this to their users.

# Why does my Gear Fit 2 take so long to acquire a GPS lock?

In short, at the start of my run, my smartphone was lying on my desk one floor up. At that point the Gear Fit 2 still had a bluetooth connection to the phone, and it was planning to use the phone GPS instead of its built-in unit. As far as I know, the gadget&#8217;s use of the phone&#8217;s GPS is not well known.

As the distance between me and the office building increased, the Gear Fit 2 obviously lost the bluetooth connection to the smartphone. With the current firmware (R360XXU1BPL1 at the time of writing), it takes the Gear Fit 2 about 0.5 km to realise that the connection is really lost, and that it should switch to its built-in GPS.

This as all pretty logical, but highly frustrating when you don&#8217;t know what&#8217;s going on. Samsung clearly has to do better.

# The Fix

Knowing what the issue is makes the fix pretty straight-forward.

Before starting your run, disable bluetooth on your smartphone, and wait for the Gear Fit 2 to register loss of the connection. It should vibrate on your wrist, and then show a little rectangle at the top right of the display, like this:<figure id="attachment_2749" aria-describedby="caption-attachment-2749" style="width: 184px" class="wp-caption alignnone">

<img data-attachment-id="2749" data-permalink="https://cpbotha.net/2017/01/15/fixing-the-samsung-gear-fit-2-gps-lock-delay-when-running-without-phone/img_20170115_0925427/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427.jpg" data-orig-size="2250,3678" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;2.2&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;PRIV&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1484472342&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;4.75&quot;,&quot;iso&quot;:&quot;676&quot;,&quot;shutter_speed&quot;:&quot;0.033333333333333&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="IMG_20170115_0925427" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427-184x300.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427-626x1024.jpg" class="size-medium wp-image-2749" src="https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427-184x300.jpg" alt="" width="184" height="300" srcset="https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427-184x300.jpg 184w, https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427-768x1255.jpg 768w, https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427-626x1024.jpg 626w, https://cpbotha.net/wp-content/uploads/2017/01/IMG_20170115_0925427-1200x1962.jpg 1200w" sizes="(max-width: 184px) 85vw, 184px" /><figcaption id="caption-attachment-2749" class="wp-caption-text">Samsung Gear Fit 2 should recognise that it has lost connection with the phone, as shown by the rectangle at the top right.</figcaption></figure> 

You can now start the exercise app and then start your run.

This morning, my Gear Fit 2 acquired a GPS lock almost instantly. You can see this by **the location icon which briefly flashes and then stays on** (it&#8217;s very important that you ensure that it stays on before running off), and by the fact that the on-screen distance gauge (you only see the distance gauge if you have set a distance target) starts climbing immediately.

(Update: I&#8217;ve had more runs since. Sometimes the GPS struggles for half a minute or more to get a lock, with the location icon remaining in the flashing state. In these cases, I sometimes stop the run, and start over, until that damned flashing location icon goes stable. Frustrating.)

# Samsung Gear Fit 2: Even casual runners should think twice.

For the price, the Samsung Gear Fit 2 packs a lot of features.

However, between this undocumented (as far as I can see) and sometimes plain frustrating GPS behaviour, the voice guidance which breaks easily and mysteriously (see [another post of mine on that issue and how to fix it][2]), and the battery life (a 40 minute run with music and GPS can use up 30% to 40% of the battery), slightly more serious casual runners (strange category, I know) might want to consider carefully their alternatives.

 [1]: https://us.community.samsung.com/t5/forums/v3_1/forumtopicpage/board-id/wearabletech/thread-id/464/page/1
 [2]: /2017/01/21/samsung-gear-fit-2-voice-guide-at-intervals-not-working-at-all-the-fix/