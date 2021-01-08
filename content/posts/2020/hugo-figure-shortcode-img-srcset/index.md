+++
title = "Drop-in replacement for Hugo figure shortcode with responsive img srcset"
date = 2020-05-02T11:42:00+02:00
lastmod = 2020-05-02T11:42:57+02:00
categories = ["howto"]
tags = ["hugo", "srcset", "responsive"]
draft = false
author = "Charl P. Botha"
+++

When [I moved this blog over to
Hugo](/2019/03/31/wordpress-to-hugo/#bonus-level-bundling-and-automatic-resizing-of-images)
slightly more than a year ago, I started using [Laura Kalbag's special `img`
shortcode](https://laurakalbag.com/processing-responsive-images-with-hugo/)
with [img srcset
support](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia%5Fand%5Fembedding/Responsive%5Fimages).

To make a long and interesting story short, `srcset` enables us to tell the
browser that we have for example 5 different resolutions of an image available,
and that it should choose the best one based on the user's device.

Pretty neat actually!

Anyways, I tweaked the code a bit over time, and most recently I combined it
with the stock Hugo `figure` shortcode.

What this means, is that you can now use just the straight [Hugo `figure`
shortcode as per the
documentation](https://gohugo.io/content-management/shortcodes/#figure), and my
modified shortcode will do all of image processing and srcset specification
fully automatically.

In other words, you only have to refer to your fullest resolution image in the
figure shortcode, and hugo will take care of creating a number of downscaled
versions, and offer them to modern browsers in a way that gives the user the
best experience.

## Install and use {#install-and-use}

To install, simply download [the figure.html
gist](https://gist.github.com/cpbotha/deb310eed14308fe26f7b7d0fabeb34d)
(embedded below) into the `layouts/shortcodes` directory in your hugo blog and
then rebuild your blog.

**NOTE:** It's **very** important that images have to be in [the page
bundle](https://gohugo.io/content-management/page-bundles/) if you want
automatic resizing and srcset. The shortcode will fall back to stock Hugo
behaviour otherwise.

{{< gist cpbotha deb310eed14308fe26f7b7d0fabeb34d >}}

## Example result {#example-result}

I've posted the image below so you can see the shortcode in action.

It started as `{{</* figure src="20200324_stillbaai_beach.jpg"
link="20200324_stillbaai_beach.jpg" caption="..." */>}}` and ended up as the
image below.

If you right click, and then inspect, you'll see the `srcset`
specification. Even better if you switch to the network panel in devtools, then
reload, and note that your browser downloads a lower resolution image if you've
narrowed your viewport, or switched devtools to mobile emulation.

{{< figure src="20200324_stillbaai_beach.jpg" link="20200324_stillbaai_beach.jpg" caption="Figure 1: A photo taken on the beach in Stilbaai on March 24, 2020." >}}

## Updates

- On 2020-05-10 I updated the shortcode to fall back to stock Hugo behaviour
  instead of just breaking when the image was not part of the page
  bundle. However, if you want resizing and srcset (the whole point of this
  post), your images should be in the page bundle. :)

