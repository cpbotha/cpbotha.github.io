---
title: On DivX 4.0 and OpenDivX
author: cpbotha
type: post
date: 2002-03-13T20:28:00+00:00
url: /2002/03/13/on-divx-40-and-opendivx/
categories:
  - Uncategorized

---
I&#8217;ve just done a quick subjective comparison between the same film compressed with [DivX Networks&#8217;][1] [DivX 4.0 codec][2] (as performed with my own [im2avi][3] linked with [avifile][4]) and [Project Mayo&#8217;s][5] OpenDivX (also mpeg4) codec, as implemented independently by [ffmpeg][6].

Now, ffmpeg encodes the whole movie in a fraction of the time. This is no surprise, as ffmpeg has spent some time on optimising their code for real-time streaming. This is still impressive.

Keep in mind that, at least according to what I read, DivX 4.0 was developed starting from the open source OpenDivX by more or less the same group of people. Well, subjectively speaking, even when encoding OpenDivX at DOUBLE the bitrate, the DivX 4.0 movie still looks _far_ better. I would have liked to make a version of im2avi for ffmpeg exclusively: ffmpeg has just about zero dependencies and a carrot could compile it. Building avifile correctly (with support for all the codecs) is somewhat more involved. However, the quality of divx4 is hard to beat with open source. If I get VERY bored, I&#8217;ll do some quantitative tests.

 [1]: http://www.divxnetworks.com/
 [2]: http://www.divx.com/
 [3]: http://cpbotha.net/im2avi.html
 [4]: http://avifile.sf.net/
 [5]: http://www.projectmayo.com/
 [6]: http://ffmpeg.sf.net/