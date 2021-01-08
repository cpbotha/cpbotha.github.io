---
title: Recording screencasts on Windows with free software
author: cpbotha
type: post
date: 2008-05-10T20:23:09+00:00
url: /2008/05/10/recording-screencasts-on-windows-with-free-software/
topsy_short_url:
  - http://is.gd/6SAJwy
categories:
  - tech
tags:
  - camstudio
  - capture
  - devide
  - howto
  - screencast
  - video
  - youtube

---

_(This post was first written in May of 2008, but I've been updating it
periodically. See also the updates right at the end.)_

## What are screencasts?

[Screencasts][1] refer to video recordings of screen activity, often with
narration. These can be used to demonstrate software or to serve as a kind of
visual HOWTO. We often make screencasts of software we design in the [Medical
Visualisation group][2] at the TU Delft to use in presentations at conferences
or to distribute online.

## Windows software for making screen recodings

On Windows, Camtasia Studio ($300) or Camtasia SnagIt ($40) are probably the
best options your money can buy. Most of the free alternatives suck quite
badly: This includes the Windows Media Encoder, thank you very much. In fact,
the Windows Media 9 Screen Capture Codec has been fine-tuned to create the
worst possible quality movies you can imagine. Another problem with the free
options is that they often can't sustain writing the video stream to disk,
hence resulting in dropped frames and unusable screencasts. When they are able
to sustain writing, it probably means that the compression is completely
killing video quality.

### CamStudio: Free and open source, just be careful from where you download

Fortunately, it turns out that there is a free option which offers comparable
performance to the Camtasia products, and for good reason. It's called
[CamStudio][3], and it's even open source! It's terribly important that you
also install the [lossless CamStudio Screen Capture codec][4], it's this that
makes all the difference.

This codec compresses all frames with the fast LZO lossless compression
algorithm, so you get the highest possible quality without dropping frames due
relatively slow disc writing.

It is important that you stick to the sourceforge links I've posted above. It is
quite unfortunate that some of the CamStudio installers have a sordid history
with adware and malware, but these SourceForge versions seem to be fine.

Using CamStudio, I made a 3.5 minute screencast, with live audio recording,
show-casing some of the new DICOM browsing functionality in the next DeVIDE
release. After capture, I transcoded the CamStudio screen capture codec AVI to
XVID using [MediaCoder][5], and then uploaded to YouTube (play at your own
risk!):

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/iLfu6JXkWP4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Update on 2010-02-21

I've made <a title="Link to DRE screencast #1"
href="http://www.youtube.com/watch?v=xEbYw73y3pM"
data-rel="lightbox-video-0">two</a> <a title="Link to DRE screencast #2"
href="http://www.youtube.com/watch?v=7FwPw9qlsms"
data-rel="lightbox-video-1">more</a> screencasts and learnt some time-expensive
lessons:

- DON'T encode with H.264, in spite of YouTube's recommendation. This screws up
  captured text elements extremely badly. I had much more success with XVID at
  1500 kbit/s and MP3 audio using MediaCoder, and **THE MOST SUCCESS OF ALL
  just directly uploading the lossless codec screencast to YouTube, without any
  transcoding**.
- DO capture at 640x480 or at 1280x720 (HD).  For example 800x600 is NOT worth
  it, it gets downscaled by YouTube. By capturing at 640x480 or 1280x720 you
  have much more control over what finally appears on YouTube.
- If you get audio / video sync problems (I experienced them with a 10 minute
  screencast), try activating "Use MCI Recording" in the CamStudio "Audio
  Option for Microphone".

## Update on 2011-10-22

With CamStudio 2.6 r294 getting the codec working on Windows 7 64bit is not straight-forward. You first install the codec in the normal way (with the exe installer), then you have to do TWO things. First copy camcodec.dll from Windows\System32 to Windows\SysWOW64. Second, create a reg file with the following contents:

<pre class="brush: plain; title: ; notranslate" title="">
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\drivers.desc]
"camcodec.dll"="CamStudio lossless codec [CSCD]"
[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32]
"VIDC.CSCD"="camcodec.dll"
</pre>

Install it by double-clicking the reg file, or doing right-click and then selecting Merge. After this, you should be able to select the camstudio codec from Options | Video Options | Compressor.

Furthermore, you can upload camstudio-encoded movies directly to Google Picasa, it Just Works(tm)!

## Update on 2013-02-13

If CamStudio 2.7 complains about MSVCR100.dll being missing, you should install
the <a title="MS Visual C++ redistributable 32bit"
href="http://www.microsoft.com/en-us/download/details.aspx?id=5555">MS Visual
C++ redistributable</a> (32bit, because CamStudio is 32bit).

## Update on 2020-06-25

It is the year 2020.

We have flying cars and sentient androids ... and camstudio is still working
fine on the latest Windows 10 2004 release.

I've just installed `CamStudio_Setup_2-7_r316` and `CamStudioCodec_1.5_Setup`
from the sourceforge links in the third paragraph of this post, and everything
still works like a charm: Lossless recording using the camstudio codec, and
then transcoding to mp4 using [HandBrake](https://handbrake.fr/).

 [1]: http://en.wikipedia.org/wiki/Screencast "Screencast entry on Wikipedia"
 [2]: http://visualisation.tudelft.nl/MedVis "MedVis at the TU Delft"
 [3]: https://sourceforge.net/projects/camstudio/files/stable/ "Link to CamStudio sourceforge"
 [4]: http://sourceforge.net/projects/camstudio/files/legacy/CamStudioCodec_1.5_Setup.exe/download "CamStudio screen capture codec link"
 [5]: http://www.mediacoderhq.com/ "MediaCoder website"
