---
title: I crushed the GSVideo problematic frame error!
author: cpbotha
type: post
date: 2011-03-04T20:44:27+00:00
url: /2011/03/04/i-crushed-the-gsvideo-problematic-frame-error/
topsy_short_url:
  - http://is.gd/NMIKU8
categories:
  - nerd
  - tech
tags:
  - gsvideo
  - processing

---
_Nerd warning: This post really belongs on my nerd blog [VXLabs.com][1], but as this blog has a rich tradition of popular [processing posts][2], I’m posting it here._

[<img alt="Debugging" height="180" src="http://farm3.static.flickr.com/2676/4047355843_0fd2fa0036_m.jpg" width="240"/>][3]

[GSVideo][4] is a brilliant library that you can use in [processing][5] to capture live video, on Windows, Linux and OSX, and it’s a huge improvement over the built-in capturing support. Unfortunately, a number of us (including some of the 123 students we got to build augmented reality music instruments this September) have been running into a problematic frame error crash that meant captures didn’t last for very long before unceremoniously crashing the application. Error info and stack trace look something like the following (edited for brevity):

<pre class="brush: plain; title: ; notranslate" title=""># A fatal error has been detected by the Java Runtime Environment:
#
#  EXCEPTION_ACCESS_VIOLATION (0xc0000005) at pc=0x7c342eee, pid=1564, tid=2052
#
# JRE version: 6.0_20-b02
# Java VM: Java HotSpot(TM) Client VM (16.3-b01 mixed mode windows-x86 )
# Problematic frame:
# C  [msvcr71.dll+0x2eee]
#
---------------  T H R E A D  ---------------

Current thread (0x18db7000):  JavaThread "Animation Thread" [_thread_in_native, id=2052, stack(0x1bfd0000,0x1c020000)]

Stack: [0x1bfd0000,0x1c020000],  sp=0x1c01f8a0,  free space=13e1c01f384k
Native frames: (J=compiled Java code, j=interpreted, Vv=VM code, C=native code)
C  [msvcr71.dll+0x2eee]
C  [java.dll+0x728d]
J  java.nio.Bits.copyToByteArray(JLjava/lang/Object;JJ)V
j  java.nio.DirectIntBufferU.get([III)Ljava/nio/IntBuffer;+126
j  java.nio.IntBuffer.get([I)Ljava/nio/IntBuffer;+5
j  codeanticode.gsvideo.GSCapture.read()V+24
j  CathetAR.draw()V+22
</pre>

Read more about it on this [forum thread][6].

In any case, today I spent some hours I don’t really have and finally managed to crush it. Turns out, and some of you will probably not be surprised, that it was a threading problem. The capture event handler invokeEvent() and the read() call were being interleaved, and the buffer they were using is also not thread-safe. Doh. Some synchronization here and there, and an extra capture buffer, now I can’t get it to crash anymore.

Get the [patch here][7], and a [patched GSVideo.jar][8] here. Both of these are for the GSVideo 20110203 test version. If you can’t patch and build it yourself, just copy my GSVideo.jar over the GSVideo.jar in your unpacked GSVideo 20110203 plugin directory (sub-directory library). **Update: See below, GSVideo 0.8 has been released and now contains my patch. Rather get the 0.8 download!**

Leave me a comment if this helps!

### Update on 2011-03-06

Andres Colubri, author of GSVideo, has refined and [integrated][9] my patch. The next GSVideo release (0.8 and newer) should have this fix.

### Update on 2011-03-15

Andres has just released GSVideo 0.8, which integrates my fix and many other improvements. Go read his [0.8 release post][10]!

 [1]: http://vxlabs.com/ "VXLabs.com, my favourite nerd blog!"
 [2]: /tag/processing/ "All posts on this site tagged with "processing"."
 [3]: http://www.flickr.com/photos/28208534@N07/4047355843/ "Debugging by mikemol, on Flickr"
 [4]: http://gsvideo.sourceforge.net/ "GSVideo website"
 [5]: http://processing.org/ "processing website"
 [6]: http://forum.processing.org/topic/gsvideo-0-6-crash-problem "forum thread 1 concerning the problematic frame crash"
 [7]: http://cpbotha.net/files/gsvideo-20110203-patch-20110304/gsvideo-20110203-problematic-frame-fix-cpbotha.diff "gsvideo problematic frame fix"
 [8]: http://cpbotha.net/files/gsvideo-20110203-patch-20110304/GSVideo.jar "patched and built GSVideo.jar"
 [9]: http://gsvideo.svn.sourceforge.net/viewvc/gsvideo/trunk/src/codeanticode/gsvideo/GSCapture.java?r1=152&r2=151&pathrev=152 "gsvideo changeset integrating crash fix"
 [10]: http://codeanticode.wordpress.com/2011/03/15/gsvideo-0-8/ "gsvideo 0.8 release post"
