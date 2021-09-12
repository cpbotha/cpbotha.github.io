---
title: Processing + NyARToolkit + multiple marker tracking
author: cpbotha
type: post
date: 2010-06-05T22:59:24+00:00
url: /2010/06/05/processing-nyartoolkit-multiple-marker-tracking/
topsy_short_url:
  - http://is.gd/cE3Hb
categories:
  - howto
  - nerd
  - tech
tags:
  - augmented reality
  - nyartoolkit
  - processing

---
For various reasons, I need to do multiple marker tracking in [processing][1] with [NyARToolkit][2].  However, with the default [NyAR4psg][3] layer between these two, multiple marker tracking is downright hard, and when you get it working, it’s not quite what you expect. After a few days of Java hacking, during which I was very pleasantly surprised with eclipse, I am now pleased to present to you my modifications to the NyAR4psg that makes multiple marker tracking easy! See here:
{{< figure src="/wp-content/uploads/2010/06/nyarmultiboard_ss.jpg" link="/wp-content/uploads/2010/06/nyarmultiboard_ss.jpg" caption="Standard hiro and kanji markers tracked simultaneously with augmented reality sphere and cube. In the background some artwork by my daughter!">}} 

I’ve called it NyARMultiBoard, and you can use it instead of the default NyARBoard if you want to track multiple markers.

Download a ZIP file containing everything (source code, jar files) from [this directory][4].  If you unpack this into your processing sketchbook/libraries directory, it should work out of the box.  It’s a drop-in replacement for NyAR4psg, so you don’t need to have that installed as well. There is an example to get you started in NyAR2/example/NyARMultiTest.  Note: This uses the GSVideo capturing stack as I explain [here][5], you should easily be able to change it back to processing defaults (just change GSCapture to Capture).

_Please let me know in the comments if this works (or doesn’t) for you!_

I made this screencast to demonstrate the multiple marker tracking, assisted by [TNR][6]:

<div class="jetpack-video-wrapper">
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="473" src="https://www.youtube.com/embed/a9nXZqtkrsk?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="840"></iframe></span>
</div>

I also made this really bad screencast (old webcam + night time lighting + transcoding):

<div class="jetpack-video-wrapper">
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="473" src="https://www.youtube.com/embed/5qAMUM7Z1_4?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="840"></iframe></span>
</div>

**If you’re really into the details**

I’ve just added two new classes NyARMultiBoard and NyARMultiBoardMarker to the default NyAR4psg distribution. Very importantly, NyARToolkit itself needs to be patched with one extra method in NyARDetectMarker, see the NyARMultiBoard comments.

**Update on 20110304**

I’ve fixed the problematic frame bug in gsvideo that many of you have been running into. See [this post][7].

**Update on 20110305**

I’ve updated NyAR2 so it works with the P3D renderer as well, which is often faster for blitting the webcam image onto the display. The updated zip file is named NyAR2-20110305.zip, and it can be downloaded from the [usual directory][8]. My changes are based on NyAR4psg 0.3.0 and NyARToolkit 2.5.2.

 [1]: http://processing.org/ "processing website"
 [2]: http://nyatla.jp/nyartoolkit/wiki/index.php?FrontPage.en "NyARToolkit website"
 [3]: http://nyatla.jp/nyartoolkit/wiki/index.php?NyAR4psg.en "Link to NyAR4psg page"
 [4]: http://cpbotha.net/files/nyar4psg_multimarker/ "Link to NyARMultiBoard archive"
 [5]: http://cpbotha.net/2010/03/04/processing-gsvideo-nyartoolkit-on-linux-x86_64/ "howto getting gsvideo going on x76_64"
 [6]: http://cpbotha.net/2009/09/20/weekly-head-voices-4-the-new-roomie-medvis-at-mevis-fairy-tale-beach/ "The New Roomie blog"
 [7]: http://cpbotha.net/2011/03/04/i-crushed-the-gsvideo-problematic-frame-error/ "post with gsvideo problematic frame error fix"
 [8]: http://cpbotha.net/files/nyar4psg_multimarker/ "NyAR2 multimarker download directory."
