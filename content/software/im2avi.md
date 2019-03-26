---
title: im2avi
author: cpbotha
type: page
date: 2007-02-19T14:37:22+00:00

---
NOTE: All the linux machines that I work with are still running Debian Stable (aka Woody aka Linux 1958) and im2avi happily works on these machines. Some users have reported getting it to run on newer machines, some users have reported not being able to. At some stage, I&#8217;ll spend some time on a newer Linux distribution and update everything to run out of the box on such machines. Until then, you are primarily on your own.

im2avi is a small program for making AVIs from sequences of images. It makes use of [avifile][1] for encoding video streams, so im2avi has access to all the codecs that avifile supports, including e.g. DivX ;) or Cinepak. It uses the [ImageMagick++ library][2] to load the images, so it supports a wide range of formats. im2avi was developed on linux, but should run on most OSen that support avifile, ImageMagick and fltk.

My primary use for im2avi is to make &#8220;screen movies&#8221; for presentations and such-like. To capture the actual frames, I use [xvidcap][3]. I write the frames to the default xwd-format (which im2avi can easily read) and then make msmpeg4 AVIs. For an examples of the output, see the movies on my [ShellSplatting page][4].

NOTE: It seems xvidcap now has its own built-in encoding support, so you might want to try that first!

im2avi adds value in offering an easy to use UI frontend to avifile and ImageMagick++. im2avi is distributed under the GPL v2 or later.

You can download version 0.4 (released 20030620) by clicking [here][5]. Please read the included README file. The changelog is also available [here][6].

To see a screenshot, click <a href="http://visualisation.tudelft.nl/~cpbotha/screenshots/im2avi-0.2.jpg" title="" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="">here</a>.

 [1]: http://avifile.sourceforge.net/ "link to avifile website"
 [2]: http://www.imagemagick.org/www/Magick++/ "ImageMagick++ website"
 [3]: http://xvidcap.sourceforge.net/ "xvidcap website"
 [4]: http://visualisation.tudelft.nl/publications/botha2003/ "ShellSplatting webpage"
 [5]: http://visualisation.tudelft.nl/~cpbotha/files/im2avi/im2avi-0.4.tar.gz "im2avi download link"
 [6]: http://visualisation.tudelft.nl/~cpbotha/thingies/changelog.im2avi "im2avi changelog"