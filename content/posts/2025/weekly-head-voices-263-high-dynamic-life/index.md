---
title: "Weekly Head Voices #263: High Dynamic Life"
slug: weekly-head-voices-263-high-dynamic-life
author: "Charl P. Botha"
date: 2025-12-25T14:41:00+02:00
draft: false
tags:
  - avif
  - bliss
  - boox
  - contentment
  - hdr
  - hugo
  - iPhone
  - life partner
  - table mountain
  - ultra hdr
  - webp
categories: ["weekly head voices"]
type: "post"
# EXCEPTION: keep ogimage as jpg, og.html will convert this to webp when resizing
# DO NOT use .webp here, then you'll git the golang / hugo webp decoding bug
# for the rest of the post, use webp, but keep a same-named jpg/png ok?
ogimage: "rooi_els_anniversary_hike_5996.jpg"
---

Well will you look at that date... Merry Christmas everyone!

I would also like to welcome you to the 263d edition of the Weekly Head Voices, a surprise even to me that it managed to get this far!

{{< figure_orig link="rooi_els_anniversary_hike_5996.jpg" src="rooi_els_anniversary_hike_5996_1280.jpg" caption="26th wedding anniversary hike, this time a forbidden route starting from Rooi Els" >}}

I was partially inspired by Martin Fowler's ["writing fragments"](https://martinfowler.com/articles/writing-fragments.html) to just get this post out there. In his post, he makes the case that social media comes and goes, something I've seen happen more than once during the 25 year existence of this blog, and so he just plonks together a bunch of things that he found interesting and publishes that as a blog post.

Plonking together a bunch of things and calling it a post sounds like a robust approach to me, and so I'm adopting it as of now.

I also thought that it would feel good publishing one more normal WHV for 2025 before the [traditional year transition post](/tags/transition/) which will hopefully also happen on time(ish).

## Boox Go 6 e-ink reader micro review

My fourth Kindle e-reader, a 2018 Paperwhite, has this irritating issue where it will hard crash after some amount of reading, at which point one has to hard reboot, a process that takes some number of minutes.

This is of course not great when you're reading in bed, in the dark, before going to sleep. I tried all of the recommended remedies, including the factor reset, all to no avail. (see [my Amazon review](https://www.amazon.com/review/RRA4LVNPHE0TE/ref=cm_cr_srp_d_rdp_perm?ie=UTF8))

It's too late to return this unit, and so I decided to invest in the Boox Go 6 e-ink reader, a more generic Android device that is able to run the official Android apps of all the retailers, including Kindle, Kobo and more.

I've now been using this for about four months (it arrived on August 21) and I can say that it's a keeper.

Here are some observations, but please let me know in the comments if you would like to know anything else:

- I bought my unit through [DynamicCom](https://www.dynamiccom.co.za/products/boox-go-6-e-ink-reader/1123586000024646701), the local distributor, who were super helpful and send regular emails to inform me of shipment progress. Down here the unit is slightly more expensive than the equivalent Kindle. I also bought the Boox magnetic cover, highly recommended!
- By default, the power setting on this device does a full shutdown after 15 minutes! This was super irritating, because I had to wait for it to boot up every time. Fortunately, by changing `settings -> power -> power-off timeout` from 15 minutes to 2 days, I now have instant on, returning to the page I was reading.
- It is indeed great that I can now buy and read books from Kobo as well. I'm currently binging [Adrian Tchaikovsy](https://adriantchaikovsky.com/), and the two most recent books I bought were substantially cheaper on Kobo than on Amazon.
- The Kobo app's maximum font size is not big enough so that I can read without my spectacles at night. This is only an issue if you are >50 (welcome to the club!) or have other vision challenges. I have submitted a support request with Kobo. In the meantime, I am reading the DRM-free epubs that Kobo supplied with my purchase in the Boox's built-in e-reader.
- Battery life, even with my 2 day power off timeout, is practically a week or more. The unit charges with USB-C which is great.
- As far as I can see, the Boox uses the Carta 1300 e-ink screen. It is a pleasure to read from. The backlight brightness and colour temperature can be adjusted to your liking.

## Hugo 0.153 with libwebp via wasm

You might remember from [WHV #257](/2024/12/08/weekly-head-voices-257-untitled49-ipynb/#webp-ftw) about the long-standing Golang bug that darkens webp images, which I worked around by using an auxiliary non-webp image as the source.

Thanks to github notifications on [the relevant Hugo bug](https://github.com/gohugoio/hugo/issues/8879), I saw that bep (Bjørn Erik Pedersen, the amazing creator of Hugo) had just merged a [PR switching to libwebp via WASM](https://github.com/gohugoio/hugo/pull/14234) (!!) instead of the built-in Go libraries.

This update uses libwebp, a C-library, compiled to wasm via the wazero.io pure-go runtime.

Based on what I read, in the [relevant github issue](https://github.com/gohugoio/hugo/issues/12843) and elsewhere, this is a really neat trick for Hugo to have pure Go builds that can use native libraries because they've been compiled to wasm! In this specific case, it means that in hugo 0.153, I can webp all the things without the work-around I am using at the moment.

I was really excited by this update, and thus also reloading the [hugo 0.153 release milestone](https://github.com/gohugoio/hugo/milestone/349) multiple times per day, until the release of 0.153 and 0.153.1 shortly after on December 20.

The Hugo release was the additional fuel needed to get this post off the ground, but alas, my enthusiasm for WebP was just about snuffed out when I discovered that it has 0 (zero) support for HDR...

## The surprising trickiness of HDR photos on this blog

As I was putting this post together, I selected a number of candidate photos, as I usually do.

However, this time I could not help but notice the HDR (high dynamic range) adding some extra brightness to the highlights: In this particular case, brighter parts in sunny photos, and night lights in night photos.  

As is often the case with my brain, multiple multi-hour research sessions ensued, some of the notes of which you can see [at my TiL site](https://charlbotha.com/til/Convert-iPhone-HDR-.heic-photos-to-web-compatible-HDR-images).

Long story short, many iPhones and Androids can add HDR information to their photos when the scene requires it. Apple does it in their .HEIC images (mostly extra HDR gainmap, but could also be in a single image), and Google adds the HDR gainmap as part of the JPG metadata, a format dubbed [Ultra HDR](https://github.com/google/libultrahdr).

You can see some [examples of web-compatible HDR photos](https://gregbenzphotography.com/hdr-gain-map-gallery/) at Greg Benz's site. (If you dig into this, you'll run into Greg Benz in many places -- he has been working hard campaigning for web-compatible gainmap-based HDR image support in various places.)

Currently most of the main browsers support _subsets of_ Ultra HDR (you have to know which subset!), and hopefully in the slightly further future, we'll be able to use [AVIF](https://caniuse.com/?search=avif) for HDR and also all other web-facing images.

_Note: WebP has no support for HDR. My new hope for the future is AVIF._

In my case, I had to figure out how to convert my iPhone's .HEIC images into UltraHDR JPGs. After more hours of failed experiments (no, none of Gimp, ImageMagick, libvips, Affinity Photo, GraphicConverter 12 do this correctly), I landed on a rather obscure bit of macOS / Swift open-source called [toGainMapHDR](https://github.com/chemharuka/toGainMapHDR) which is able to convert HDR .HEIC files to Ultra HDR with the particular Apple gainmap format (`-g`) currently supported by Edge and Chrome on macOS.

Alernatively, Graphic Converter 12 can convert from HDR .HEIC images to single image HDR AVIF, which are substantially smaller than the corresponding Ultra HDR JPG files. The problem is that these AVIFs have no built-in fallback to standard SDR like Ultra HDR has by design. Soon there will be more support for HDR AVIF via included gainmap, which will have similar fallback behaviour to Ultra HDR.

So after all that, the Ultra HDR photos in this post should show up with HDR highlights if your display system and browser (Chrome, Edge, Safari do, Firefox not yet) support it, and gracefully fall back to the non HDR versions if they do not!

Because neither Hugo or Golang support processing the HDR metadata in these images correctly, I have to manually resize them, instead of using [my otherwise convenient srcsets figure shortcode](/2020/05/02/drop-in-replacement-for-hugo-figure-shortcode-with-responsive-img-srcset/) that automatically creates all the scaled versions.

### P.S. A taste of the AVIF future

Below I have embedded the same photo as the Ultra HDR (JPG) shown in the next section, but here as a high(er)-bitdepth single image HDR AVIF.

{{< figure_orig src="cape_town_from_overseers_5775_640.avif" link="cape_town_from_overseers_5775.avif" >}}

You should see the AVIF image above these words, and your browser should show the full resolution version if you click on the image. If you don't, please let me know in the comments below, or via any other means, along with details of your web-browser.

For interest's sake, here are the file sizes:

- original .heic 4032x2268: 1 MB
- Ultra HDR JPG 85% quality: 2 MB
- HDR AVIF 12-bit depth 85% quality: 422 kB

## Significant life events

My SO completed a significant but undisclosed number of orbits around the sun. We celebrated with friends by spending the night at the Overseers Cottage on top of Table Mountain, which felt like a pretty spectacular way to celebrate this special birthday. The party fully lived up to this standard (and then some).

{{< figure_orig link="cape_town_from_overseers_5775.jpg" src="cape_town_from_overseers_5775_1280.jpg" caption="Cape Town at night as seen from the overseers cottage on top of Table Mountain" >}}

Somewhat later, we celebrated my mom's 80th at home, with a great group of her close friends. It was such a beautiful day to celebrate such a beautiful human's vitality. In addition to being in great shape in spite of her limits and to being mentally sharp (did your 80 year old figure out Apple Pay by herself?!), my mom is an example to us all of how to celebrate life, and how to celebrate one's people.

(Hi Mom!)

Somewhat later than that, above-mentioned SO and I celebrated our 26th year of marriage with our traditional anniversary hike, this time on a forbidden route (no jokes) starting from Rooi Els.

The hike was absolutely brilliant, even although we both had more than one near-faceplant coming back down the mountain on loose rocks. This is what happens when you get a bit tired, and you need to work extra hard to focus on the footwork. In Rooi Els, there were some ice-cold Stellas waiting, after which we had an early celebratory dinner with the family.

There's a lot more that I'm not going to talk about here, but I do need to mention that these past few weeks I've really been experiencing those moments of [durable, blissful contentment](/2022/12/06/weekly-head-voices-250-durable-blissful-contentment/#happiness-is-a-joke) with my family and my friends, and it's brilliant.

Thank you for reading this fellow human! I hope to see you soon, either here, or on the road somewhere...

> There is no way to happiness, happiness is the way. There is no way to peace, peace is the way. There is no way to enlightenment, enlightenment is the way.
>
> -- Thich Nhat Hanh
