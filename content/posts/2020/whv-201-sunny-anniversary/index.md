+++
title = "Weekly Head Voices #201: Sunny anniversary"
date = 2020-07-29T10:12:00+02:00
lastmod = 2020-07-29T11:26:35+02:00
slug = "weekly-head-voices-201-sunny-anniversary"
tags = ["microsoft", "paul graham", "solar", "telesensi"]
categories = ["weekly head voices"]
draft = false
ogimage = "la_mountain_pano.jpg"
+++

{{< figure src="la_mountain_pano.jpg" link="la_mountain_pano.jpg" >}}

I could feel this one almost slipping through to the two week group, but then I
thought to myself: It feels like I have nothing to write about, but future me
will probably still want to know what _sort_ of nothing exactly happened in
that week.

The 201st edition of the Weekly Head Voices looks back at the week from Moday
July 20 to Sunday July 26, 2020, which since last week I'm calling
Cray-cray 20.


## Solar Power Birthday {#solar-power-birthday}

You might recall that we [solar powered our house at the end of June last year](/2019/06/30/weekly-head-voices-172-abc/#solar-powerrrrrrrr),
but that there were still some teething problems (read: almost bricked the
inverter) which [we had solved by July 25](/2019/07/25/weekly-head-voices-174-i-row-row-row-your-boat/#bullet-list-of-miscellany-blom), almost exactly a year ago!

That means...

_HAPPY BIRTHDAY DEAR SOLAR POWER AT MY HOUSE HAPPY BIRTHDAY TO YOU WE LOVE YOU!_

{{< figure src="goodwe_sems_sample_20200728.png" caption="Figure 1: Solar production today (2020-07-18, a sunny winter's day) was 24.4kWh and total production since commissioning just under 8MWh. Cost saving is an estimate." width="300" link="goodwe_sems_sample_20200728.png" >}}

The app reports that since commissioning we have generated and used almost 8
MWh of solar power, which makes me happy.

What makes me even happier, is that the whole system has been essentially
maintenance free this whole time.

The only action I perform, is to switch the inverter to back-up mode when we're
in load-shedding season, which means that it prioritises keeping the lithium
ion batteries full.

When we're not load-shedding seasion, it's in normal mode, meaning it
prioritises using as little grid power as possible, which in the summer months
is quite close to nothing.

P.S. For our viewing pleasure, I just looked up the monthly generation for the
past 12 months, in order to be able to see the seasonal variation. It looks
like this:

{{< figure src="goodwe_monthly_generation_202007.png" link="goodwe_monthly_generation_202007.png" >}}

While July has been **really** good sun-wise (thanks Cape winter, you're a
star!), we will probably be entering the 600kWh+/month zone soon.

That dip last December is probably because we were away from home for a
while. The February dip is of course because it's a few days shorter than most
months, which in February can easily amount to 30kWh per day.


## Nerdy posts over on vxlabs {#nerdy-posts-over-on-vxlabs}

Whilst working with the brand new Microsoft Pylance Python language server for
Visual Studio Code, I figured out how to make some red squiggly lines yellow
and wrote a whole blog post about it: [Set severity override of Visual Studio
Code Pylance type mismatches for better visual distinction](https://vxlabs.com/2020/07/23/vscode-pylance-type-mismatch-warning/)

Besides the subject of the post, it was interesting to check how low the
barrier between my internal notes and publishing a blog post had become since I
started using ox-hugo.

The screenshots in the post meant I had to do some manual `attachment:`
link-wrangling, and so I wrote an Emacs function to fix that.

In a slightly meta fashion, I then pushed my notes about that new function to
another blog post titled: [An Emacs Lisp function to convert attachment: links
to file: links for ox-hugo exports](https://vxlabs.com/2020/07/25/emacs-lisp-function-convert-attachment-to-file/)

Ironically, that blog post itself did not contain a single screenshot.

Somewhere in-between I tweaked the fonts on [vxlabs.com](https://vxlabs.com/).

-   It surprised me what a difference such a small change can make.
-   With the new [Hugo pipes](https://gohugo.io/hugo-pipes/) it has become straight-forward to modify source SCSS
    (for example) and then have the hugo build server automatically rebuild the
    resultant CSS while you work. Kudos to the authors!


## Microsoft helps to break NVIDIA's stranglehold on deep learning hardware {#microsoft-helps-to-break-nvidia-s-stranglehold-on-deep-learning-hardware}

What I realised only the other day, is that Microsoft's recent work on [porting
TensorFlow to run on their DirectML stack](https://devblogs.microsoft.com/directx/directx-heart-linux/) has magically enabled AMD and even
Intel GPUs to be used to accelerate deep learning training and inference.

If you look at this [DirectML github issue](https://github.com/microsoft/DirectML/issues/21), you'll see that it's still early
days as performance is not what it should be, but peeps are almost routinely
accelerating their deep learning workloads using AMD GPUs, something which up
to now has been almost impossibly impractical.

To reiterate: Microsoft has made it straight-forward for any GPU manufacturer
to support deep learning, by simply implementing DirectML support. NVIDIA on
the other hand was really happy with their fully proprietary CUDA platform and
its dominance in the deep learning world.

What a strange world we live in.

The Microsoft of 2020 has built up a track record over the past years of doing
truly positive stuff.

I approve.


## Living in the future {#living-in-the-future}

Thanks to the internet, I was just able to find the source of a remembered adage.

The source is [Paul Graham's essay How to Get Startup Ideas](http://paulgraham.com/startupideas.html), and the adage is:

> Live in the future, then build what's missing.

It's going quite well with the company. We have products, we have (slowly)
growing traction in the market, and we have a great team.

However, just like any other company, we have to work hard at getting more traction.

There are direct ways to increase traction (SELL MORE WIDGETS!), but as an
engineer I also tend to look at the product side.

We have started work on a really exciting new feature, which is a natural
extension of what [TeleSensi](https://www.telesensi.com/) already does and which there is already a market
for, that in my mind also falls squarely into the class of things that people
in the future (5 year horizon) are going to need a whole lot more of.

That's my inner engineer talking.

My inner scientist has pointedly asked to "show him the data".

How does one solve this conundrum?

To build a truly successful product, it seems you have to take a chance on an
idea that's going to be huge in the future.

By definition, we can't measure there.

You can only measure now, then lick and hold up your finger to determine the
current wind direction, and finally muster up all of your cognitive biases to
make that call.

And then...

_You've got to ask yourself one question: "Do I feel lucky?"_

_Well, do you, punk?_
