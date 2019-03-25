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
_(This post was first written in May of 2008, but I&#8217;ve been updating it periodically. See also the updates right at the end.)_

[Screencasts][1] refer to video recordings of screen activity, often with narration. These can be used to demonstrate software or to serve as a kind of visual HOWTO. We often make screencasts of software we design in the [Medical Visualisation group][2] at the TU Delft to use in presentations at conferences or to distribute online.

On Windows, Camtasia Studio ($300) or Camtasia SnagIt ($40) are probably the best options your money can buy. Most of the free alternatives suck quite badly: This includes the Windows Media Encoder, thank you very much. In fact, the Windows Media 9 Screen Capture Codec has been fine-tuned to create the worst possible quality movies you can imagine. Another problem with the free options is that they often can&#8217;t sustain writing the video stream to disk, hence resulting in dropped frames and unusable screencasts. When they are able to sustain writing, it probably means that the compression is completely killing video quality.

Fortunately, it turns out that there is a free option which offers comparable performance to the Camtasia products, and for good reason. It&#8217;s called [CamStudio][3], and it&#8217;s even open source! It&#8217;s terribly important that you also install the [lossless CamStudio Screen Capture codec][4], it&#8217;s this that makes all the difference. This codec compresses all frames with the fast LZO lossless compression algorithm, so you get the highest possible quality without dropping frames due relatively slow disc writing.

Using CamStudio, I made a 3.5 minute screencast, with live audio recording, show-casing some of the new DICOM browsing functionality in the next DeVIDE release. After capture, I transcoded the CamStudio screen capture codec AVI to XVID using [MediaCoder][5], and then uploaded to YouTube (play at your own risk!):

<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/iLfu6JXkWP4?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

**Update on 2010-02-21:**

I&#8217;ve made <a title="Link to DRE screencast #1" href="http://www.youtube.com/watch?v=xEbYw73y3pM" data-rel="lightbox-video-0">two</a> <a title="Link to DRE screencast #2" href="http://www.youtube.com/watch?v=7FwPw9qlsms" data-rel="lightbox-video-1">more</a> screencasts and learnt some time-expensive lessons:

  * DON&#8217;T encode with H.264, in spite of YouTube&#8217;s recommendation. This screws up captured text elements extremely badly. I had much more success with XVID at 1500 kbit/s and MP3 audio using MediaCoder, and **THE MOST SUCCESS OF ALL just directly uploading the lossless codec screencast to YouTube, without any transcoding**.
  * DO capture at 640&#215;480 or at 1280&#215;720 (HD).  For example 800&#215;600 is NOT worth it, it gets downscaled by YouTube. By capturing at 640&#215;480 or 1280&#215;720 you have much more control over what finally appears on YouTube.
  * If you get audio / video sync problems (I experienced them with a 10 minute screencast), try activating &#8220;Use MCI Recording&#8221; in the CamStudio &#8220;Audio Option for Microphone&#8221;.

<div>
  <strong>Update on 2011-10-22:</strong>
</div>

<div>
  <p>
    With CamStudio 2.6 r294 getting the codec working on Windows 7 64bit is not straight-forward. You first install the codec in the normal way (with the exe installer), then you have to do TWO things. First copy camcodec.dll from Windows\System32 to Windows\SysWOW64. Second, create a reg file with the following contents:
  </p>
  
  <pre class="brush: plain; title: ; notranslate" title="">
Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\drivers.desc]
"camcodec.dll"="CamStudio lossless codec [CSCD]"
[HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32]
"VIDC.CSCD"="camcodec.dll"
</pre>
  
  <p>
    Install it by double-clicking the reg file, or doing right-click and then selecting Merge. After this, you should be able to select the camstudio codec from Options | Video Options | Compressor.
  </p>
  
  <p>
    Furthermore, you can upload camstudio-encoded movies directly to Google Picasa, it Just Works(tm)!
  </p>
  
  <div>
    <strong>Update on 2013-02-13:</strong>
  </div>
  
  <div>
  </div>
  
  <div>
    If CamStudio 2.7 complains about MSVCR100.dll being missing, you should install the <a title="MS Visual C++ redistributable 32bit" href="http://www.microsoft.com/en-us/download/details.aspx?id=5555">MS Visual C++ redistributable</a> (32bit, because CamStudio is 32bit).
  </div>
</div>

 [1]: http://en.wikipedia.org/wiki/Screencast "Screencast entry on Wikipedia"
 [2]: http://visualisation.tudelft.nl/MedVis "MedVis at the TU Delft"
 [3]: http://camstudio.org/ "Link to CamStudio website"
 [4]: http://sourceforge.net/projects/camstudio/files/legacy/CamStudioCodec_1.5_Setup.exe/download "CamStudio screen capture codec link"
 [5]: http://www.mediacoderhq.com/ "MediaCoder website"