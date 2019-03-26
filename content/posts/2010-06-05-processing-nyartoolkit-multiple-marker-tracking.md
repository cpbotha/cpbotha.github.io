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
For various reasons, I need to do multiple marker tracking in [processing][1] with [NyARToolkit][2].  However, with the default [NyAR4psg][3] layer between these two, multiple marker tracking is downright hard, and when you get it working, it&#8217;s not quite what you expect. After a few days of Java hacking, during which I was very pleasantly surprised with eclipse, I am now pleased to present to you my modifications to the NyAR4psg that makes multiple marker tracking easy! See here:<figure id="attachment_944" aria-describedby="caption-attachment-944" style="width: 300px" class="wp-caption aligncenter"><a href="http://cpbotha.net/wp-content/uploads/2010/06/nyarmultiboard_ss.jpg" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="944" data-permalink="https://cpbotha.net/2010/06/05/processing-nyartoolkit-multiple-marker-tracking/nyarmultiboard_ss/" data-orig-file="https://cpbotha.net/wp-content/uploads/2010/06/nyarmultiboard_ss.jpg" data-orig-size="719,576" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;}" data-image-title="nyarmultiboard_ss" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2010/06/nyarmultiboard_ss-300x240.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2010/06/nyarmultiboard_ss.jpg" class="size-medium wp-image-944" title="nyarmultiboard_ss" src="http://cpbotha.net/wp-content/uploads/2010/06/nyarmultiboard_ss-300x240.jpg" alt="" width="300" height="240" srcset="https://cpbotha.net/wp-content/uploads/2010/06/nyarmultiboard_ss-300x240.jpg 300w, https://cpbotha.net/wp-content/uploads/2010/06/nyarmultiboard_ss.jpg 719w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-944" class="wp-caption-text">Standard hiro and kanji markers tracked simultaneously with augmented reality sphere and cube. In the background some artwork by my daughter!</figcaption></figure> 

I&#8217;ve called it NyARMultiBoard, and you can use it instead of the default NyARBoard if you want to track multiple markers.

Download a ZIP file containing everything (source code, jar files) from [this directory][4].  If you unpack this into your processing sketchbook/libraries directory, it should work out of the box.  It&#8217;s a drop-in replacement for NyAR4psg, so you don&#8217;t need to have that installed as well. There is an example to get you started in NyAR2/example/NyARMultiTest.  Note: This uses the GSVideo capturing stack as I explain [here][5], you should easily be able to change it back to processing defaults (just change GSCapture to Capture).

_Please let me know in the comments if this works (or doesn&#8217;t) for you!_

I made this screencast to demonstrate the multiple marker tracking, assisted by [TNR][6]:

<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/a9nXZqtkrsk?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

I also made this really bad screencast (old webcam + night time lighting + transcoding):

<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/5qAMUM7Z1_4?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

**If you&#8217;re really into the details**

I&#8217;ve just added two new classes NyARMultiBoard and NyARMultiBoardMarker to the default NyAR4psg distribution. Very importantly, NyARToolkit itself needs to be patched with one extra method in NyARDetectMarker, see the NyARMultiBoard comments.

**Update on 20110304**

I&#8217;ve fixed the problematic frame bug in gsvideo that many of you have been running into. See [this post][7].

**Update on 20110305**

I&#8217;ve updated NyAR2 so it works with the P3D renderer as well, which is often faster for blitting the webcam image onto the display. The updated zip file is named NyAR2-20110305.zip, and it can be downloaded from the [usual directory][8]. My changes are based on NyAR4psg 0.3.0 and NyARToolkit 2.5.2.

 [1]: http://processing.org/ "processing website"
 [2]: http://nyatla.jp/nyartoolkit/wiki/index.php?FrontPage.en "NyARToolkit website"
 [3]: http://nyatla.jp/nyartoolkit/wiki/index.php?NyAR4psg.en "Link to NyAR4psg page"
 [4]: http://cpbotha.net/files/nyar4psg_multimarker/ "Link to NyARMultiBoard archive"
 [5]: http://cpbotha.net/2010/03/04/processing-gsvideo-nyartoolkit-on-linux-x86_64/ "howto getting gsvideo going on x76_64"
 [6]: http://cpbotha.net/2009/09/20/weekly-head-voices-4-the-new-roomie-medvis-at-mevis-fairy-tale-beach/ "The New Roomie blog"
 [7]: http://cpbotha.net/2011/03/04/i-crushed-the-gsvideo-problematic-frame-error/ "post with gsvideo problematic frame error fix"
 [8]: http://cpbotha.net/files/nyar4psg_multimarker/ "NyAR2 multimarker download directory."
