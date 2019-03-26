---
title: Processing + GSVideo + NyARToolkit on Linux x86_64
author: cpbotha
type: post
date: 2010-03-04T22:41:48+00:00
url: /2010/03/04/processing-gsvideo-nyartoolkit-on-linux-x86_64/
topsy_short_url:
  - http://is.gd/cC3JS
categories:
  - nerd
tags:
  - artoolkit
  - gstreamer
  - gsvideo
  - java
  - jdk
  - nyartoolkit
  - processing
  - x86_64

---
Every now and then, I blast out the cruft from my nerd gland&#8217;s exit duct by writing a terribly nerdy post.  This is just such a post, so if you don&#8217;t speak Nerd, i&#8217;d highly recommend that you go have some fun [elsewhere][1], at least until my next Weekly Head Voices of course!

As mentioned around these parts, I&#8217;m currently playing with [Processing][2], a beautiful programming stack for making interactive visual, err, thingies. To be more specific, I&#8217;d like to use processing together with something like ARToolkit to do real-time 3D tracking of markers in live video, for augmented reality fun.  To see what this could look like, see this YouTube video:

<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/uoncHfnYWHM?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

Today&#8217;s challenge is getting whole stack, including processing, the GSVideo video capture library for processing and the NyARToolkit augmented reality for processing going on Linux x86_64 (64bit).  On Linux x86 (32bit) this is much more straight-forward, but I wouldn&#8217;t write a blog post about straight-forward, now would I?

Here is the recipe:

  1. Make sure you have the native 64bit Sun JDK installed for your system.  On this Ubuntu 9.10 machine it&#8217;s ﻿﻿﻿sun-java6-jdk 6-15-1, on Ubuntu 10.04 (also tested) it&#8217;s ﻿6.20dlj-1ubuntu3.
  2. Also install the jogl libraries, on this machine called libjogl-java.
  3. Make sure you have the whole of gstreamer installed. On ubuntu, all packages containing &#8220;gstreamer&#8221;.
  4. Get and unpack the processing for Linux tarball (I&#8217;ve tested this whole procedure with processing 1.0.9, 1.1 and 1.2.1) from the processing [download site][3].
  5. In the unpacked processing directory, remove the whole java subdirectory. Now make a symlink pointing to your system java directory (the one containing bin, ext, jre, lib, etc.).  On my system, that was: <pre class="brush: bash; title: ; notranslate" title="">cd processing
rm -rf java
ln -s /usr/lib/jvm/java-6-sun-1.6.0.15﻿ java
</pre>

  6. In processing/libraries/opengl/library remove the 3 libjogl*.so files and libgluegen-rt.so. Symlink their replacements from /usr/lib/jni with for example: <pre class="brush: bash; title: ; notranslate" title="">cd processing/libraries/opengl/library
rm lib*.so
ln -s /usr/lib/jni/libgluegen-rt.so
ln -s /usr/lib/jni/libjogl_awt.so
ln -s /usr/lib/jni/libjogl.so
</pre>

  7. [Download][4] and unpack gsvideo into processing/libraries.  You should be able to run the examples in processing/libraries/gsvideo/examples/Capture with the PDE (Processing Development Environment).
  8. [Download][5] and unpack the NyARToolkit for Processing library into processing/libraries.

You should now be able to run the NyARToolkit examples by changing replacing the import call as follows:

<pre class="brush: java; title: ; notranslate" title="">// replace this call:
// import processing.video.*;
// by this call:
import codeanticode.gsvideo.*;
</pre>

and changing the Capture class (twice) to GSCapture and perhaps also the capture resolution, depending on your camera. The relevant conversions are:

<pre class="brush: java; title: ; notranslate" title="">// Capture cam;
// becomes:
GSCapture cam;

// later, in setup():
// cam=new Capture(this,width,height);
// becomes:
cam=new GSCapture(this,width,height);
</pre>

The major trick in all of this is converting your Processing installation to use your system 64bit JDK instead of its own built-in 32bit JDK.

Let me know in the comments if this worked (or didn&#8217;t) for you!

 [1]: http://chatroulette.com/ "fun random webcam site"
 [2]: http://processing.org/ "Processing website"
 [3]: http://processing.org/download/ "processing download site"
 [4]: http://users.design.ucla.edu/~acolubri/processing/gsvideo/home/ "GSVideo website"
 [5]: http://nyatla.jp/nyartoolkit/wiki/index.php?NyAR4psg.en "NyARToolkit for Processing website"
