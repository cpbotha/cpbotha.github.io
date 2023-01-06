+++
title = "Weekly Head Voices #245: This too shall pass"
date = 2022-08-09T20:18:00+02:00
lastmod = 2022-08-10T19:38:35+02:00
slug = "weekly-head-voices-245-this-too-shall-pass"
tags = ["docker", "goodwe", "pi-hole", "practice", "solar", "rancher desktop", "wikipedia"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
ogimage = "vergelegen-peekaboo.jpg"
org = true
+++

WELL HELLO EVERYONE and welcome back to the Weekly Head Voices, edition #245 to
be specific, looking back at the period of time from Monday July 25 to Sunday
Aug 7, 2022.

{{< figure src="vergelegen-peekaboo.jpg" caption="<span class=\"figure-number\">Figure 1: </span>Scene from a walk after a delicious family Sunday lunch." link="vergelegen-peekaboo.jpg" >}}

In the spirit of full disclosure, I do seem to be going through a patch of
mostly pretty "meh" WHV attempts.

However, as they say, a badly written but _published_ blog post is miles better
than an unpublished blog post of _any_ quality.

Also, one day when I finally reach [the A-list](/2017/06/11/weekly-head-voices-122/) you'll be able to say that you
were already reading my stuff before it was cool.

More seriously though, the whole of [life is continuous practice](/2018/02/25/weekly-head-voices-133-onder-in-my-whiskeyglas/#life-is-continuous-practice), which can
include long stretches of rolling hills of meh.

(see also [WHV #144's section on Mastery](/2018/06/03/weekly-head-voices-144-eternal-learner/#mastery))


## Nerdy bits {#nerdy-bits}


### Postel's law and ISO 8601 date and time formatting {#postel-s-law-and-iso-8601-date-and-time-formatting}

This movie is based on a true story that happened at work.

I published a short org-roam note to my nerd blog. You can read it here:
[Conservative rendering and liberal parsing of ISO 8601 timestamps in Python](https://vxlabs.com/2022/08/05/conservative-rendering-and-liberal-parsing-of-iso-8601-timestamps-in-python/)


### Replacing DDW with RD on Windows for (WSL) devcontainers {#replacing-ddw-with-rd-on-windows-for--wsl--devcontainers}

I have replaced Docker Desktop for Windows with [Rancher Desktop](https://rancherdesktop.io/), with the
dockerd runtime, on two of my Windows development machines.

Although you have to create some WSL symlinks manually, configure RD's
`docker-credential-wincred.exe` (if you're using private container registries)
and manually install zsh completions, the end-result is a great and
fully-functional replacement for my use-case of [devcontainers](https://containers.dev/) everywhere.

Please let me know if you need more detail about the RD config.

P.S. It might come as a shock to some readers, not to mention me of 10 years
ago, that I have not only one, but two Windows workstations. My excuse is:
"adaptation".

P.P.S. There will soon be three of them.


### Notes on locally upgrading the firmware of the GW5048D-ES inverter {#notes-on-locally-upgrading-the-firmware-of-the-gw5048d-es-inverter}

There is a Goodwe GW5048D-ES 4.6 kVA inverter at the heart of the solar system powering my house.

I love it, because it's reliable, and just does the work 99.7% of the time.

However, because that 0.3% manifested recently (settings were partially
scrambled, resulting in a few minutes of darkness during a load shedding
session; could have been the Home Assistant Goodwe integration; more acutely,
its wifi access point, needed for configuration, recently disappeared) and the
OTA firmware I requested via Goodwe support failed, probably due to firmware
being a bit old already, I had to attempt a local firmware upgrade, with a USB
cable, like [I last did three years ago](/2019/07/17/weekly-head-voices-173-i-know/#bullet-list-of-miscellany-blom) (rocky road then).

Well, although my inverter is now sporting firmware version 2424G, the upgrade
definitety went on roads of the more rocky variety.

Here are some tips to help you if you're in the same boat:

-   Follow the instructions to the letter:
    -   Remove all power sources except for a single DC source. I disconnected grid
        and solar panels, keeping only the batteries connected which were close to
        full.
    -   Remove the wifi module: 4 screws, and then carefully remove the plastic
        connector.
-   Get a straight USB-A male to USB-A male cable. None of my USB-C to USB-A
    cables, or my various Frankensteined extensions, could connect (as reported
    by EzFlash.

In my case, the EzFlash upgrade worked (two bin files), but then right after
that the DataSend failed.

I retried DataSend multiple times, but finally lost connection to the
inverter's USB port.

After I put everything back together (having resolved to contact support to
help troubleshoot), the inverter's access point magically appeared, at which
point I could connect to see that everything was functioning, and inverter
reported firmware version as 2424G.

I did contact Goodwe to ask about the implications of DataSend
failing. Although I'm happy with their service, I would have appreciated a bit
more detail.

I've summarised our email thread below:

> I asked: "When I did the upgrade, the DataSend file did not go through at
> all. Could you help me understand how the upgrade is OK if I only did the
> EzFlash stage, and NOT the DataSend phase?"
>
> They answered: "Do note that the datasend file is only for use when updating
> the Armware. When updating firmware its only the EZflash and master bin file
> that is use."
>
> Then I asked: "What is the Armware for then? Why is it not necessary to upgrade
> it, although the upgrade manual gives instructions to upgrade it?"
>
> Upon which they replied: "You ARM is already updated that is why i advised not
> to worry about it. There isn't anything technical that i can share on this. The
> arm as we know normally works with communication with the batteries."


## School's anti-wikipedia stance leads to lessons and Pi-hole {#school-s-anti-wikipedia-stance-leads-to-lessons-and-pi-hole}

Last week, GOU #2 tried to print a pretty nasty, infinite-scroll, ad-infested
site with stolen wikipedia content because her school has a far too simplistic
and strict rule _against_ using wikipedia for school work.

I then proceeded to:

1.  have a long talk with her about computers not doing what you intend, but
    rather exactly what you tell them to,
2.  Do some research and realise to my shock that this anti-wikipedia stance
    seems to be a world-wide teacher thing;
3.  Write a long but friendly email to the teacher explaining that it's a lot
    more nuanced, and could I please help them to understand the nuances so that
    our kids get better at filtering information rather than just blindly
    avoiding wikipedia and
4.  At long last get around to installing [Pi-hole](https://pi-hole.net/) on this old linux laptop (via
    docker-compose) and sending all DNS requests its way (via my main router's
    DHCP service), all-in-all quite a painless process!

What this means is that all devices in my household (and there's quite a number
of them) get all of their ads blocked automatically.

{{< figure src="images/2022/2022-08-09_14-53-44_screenshot.png" caption="<span class=\"figure-number\">Figure 2: </span>The Pi-hole dashboard a few moments ago. The percentage of blocked queries remains around 10%." width="480" link="images/2022/2022-08-09_14-53-44_screenshot.png" >}}

I should have done this much earlier. There's really no chance I can install
ublock origin or equivalent on each of the growing cloud of devices and
accounts at home. Pi-hole makes 10x more sense.


## This too shall pass {#this-too-shall-pass}

On Saturday July 30, the date of the final interschools clash between Paarl
Boys' High School (my alma mater) and its arch-opponent Paarl Gimnasium, I had
the privilege of attending the 30th (!!) anniversary of my matriculation year,
along with about 50 class mates.

As a bit of context, back then I operated probably at the lowest end of the
popularity scale, mostly because of my personality. Not that it's that
important anymore, but I think that I would probably have irritated myself (in
both ways) to quite an extent.

As if that was not enough, I had even _less_ ball sense then than I do now.

In spite of all that, the reunion was a sublime and deeply enjoyable affair.

It was so great connecting again with the human journeyers I had in many cases
last seen right before we would all set off on the start of adulthood.

Back then, we were all bright-eyed, hot-headed, full of plans and with heads
full of luscious hair.

Now there was substantially less hair, many hard lessons learned, but wisdom,
and sometimes peace, in the eyes.

To me it really felt as if everyone there had this collective, positive
realisation of:

> You know what?
>
> Everything's OK.
>
> We know better what's truly important, and it's not what we believed back then.
>
> All of this? Let us enjoy it without complication.
>
> Like everything before it, this too shall pass.

Perhaps I am over-projecting.

Whatever the case may be, the enjoyment was as real as could be.

Thank you Boys High' Class of '92!