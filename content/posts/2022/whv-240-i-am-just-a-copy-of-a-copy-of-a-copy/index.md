+++
title = "Weekly Head Voices #240: I am just a copy of a copy of a copy"
date = 2022-03-21T21:06:00+02:00
lastmod = 2022-04-18T14:05:14+02:00
slug = "weekly-head-voices-240-i-am-just-a-copy-of-a-copy-of-a-copy"
tags = ["flowers", "greg egan", "mind uploading", "work", "backyard philosophy", "facebook", "emacs", "orgmode", "meetup"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
ogimage = "blood-flowers.jpg"
org = true
+++

Welcome back to another tri-weekly edition of the weekly head voices, looking
back at the period of time from Monday February 28 to Sunday March 20.

I've been so busy at work that I was unable to create a sufficient amount of
the right sort of headspace to sit down and write a WHV, hence the gap of three
weeks instead of one.

I did spend a number of mental cycles (for the Nth time) thinking about
alternative and more compact post formats that would in theory be more
resilient to lack of time and headspace, but ironically there was not enough
time and headspace to come to any sort of conclusion.

(Some more famous bloggers that I follow manage to put out a paragraph or two
every single day. It would be interesting to try an experiment like that.)

Anyways, switching out of meta mode back to the mishmash of on-topics for edition
240:


## Blood flowers {#blood-flowers}

During a recent karma-restoring family beach walk, we came across the following
pretty striking flowers:

{{< figure src="blood-flowers.jpg" caption="<span class=\"figure-number\">Figure 1: </span>Blood flowers in Betty's Bay. See text for (much) more details." link="blood-flowers.jpg" >}}

The [PlantZAfrica website tells us](http://pza.sanbi.org/haemanthus-coccineus) that these are examples of _Haemanthus
coccineus_, also known as "March flower" (no idea why) or "blood flower", the
latter which is more in line with the meaning of its Greek genus (haima =
blood, anthos = flower), and its Latin species.

We are not the first or only people to find it quite striking:

> It was probably the first flower to be collected from Table Mountain and,
> probably also the first illustration of a South African flower to appearin a
> European publication. The illustration was by the Flemish botanis de L'Obel
> in 1605. -- PlantZAfrica

Furthermore, as if the name "Blood Flower" is not metal enough, it turns out
_Haemanthus coccineus_ lives fully underground in the form of a large bulb for
the dry summer months, only revealing its brilliant red flower when the rainy
season is about to start.


## Fantastic karma and how to destroy it {#fantastic-karma-and-how-to-destroy-it}

Picture this:

It's Friday evening. We've just had a brilliant edition of our Friday evening
family braai tradition, and everyone starts retiring to their various
individual relaxation activities.

I decide that it's a great idea to forge ahead with the [react-vega](https://github.com/vega/react-vega/tree/master/packages/react-vega) and [RTK
Query](https://redux-toolkit.js.org/rtk-query/overview) visualization functionality I had ended my work week with.

I'd successfully worked with a previous version of the former, and my
confidence in RTKQ's quality was trending upwards due to recent experience in
one of our products.

I had already made a start with this new instance, and surely my first fully
backend-data-driven visualization was only an hour or two away, giving me a
final Friday evening boost.

Well friends, in hindsight I should have stopped right there and then.

Sure, it was the sort of gamble that had often paid off in the past -- who does
not like to start their weekend with the dopamine rush that comes with the
solving of a little technical puzzle, especially one that results in pretty
pictures?! -- but in this case it was doomed to failure.

The later it got, the less able I was to debug the issue, and the less
emotional control I was able to exert over my growing frustration.

(I am still less than happy with the new react-vega's limited documentation,
error handling and examples.)

I went to bed far later than normal, frustrated, and with no solution in sight.

All of this continued to affect my Saturday (grumpy with capital G... no wait,
all capitals...), until I finally made the conscious decision to disconnect
from the technical problem completely.

Anyways, I'm writing this down as a reminder to me to be really, really careful
with the work-to-weekend transition.


## Techno interlude #1: Make my home smart, but do it really slowly {#techno-interlude-1-make-my-home-smart-but-do-it-really-slowly}

I finally got around to hooking up one (1) of the [Shelly 1 smart relays](https://shelly.cloud/products/shelly-1-smart-home-automation-relay/) I
bought at the end of 2020.

My whole family is now able to open the main yard gate using... THEIR PHONES.

Noteworthy here is how easily the Shelly switches can be flashed, over the air
(OTA) no less, with the third party [shelly-homekit firmware](https://github.com/mongoose-os-apps/shelly-homekit) to make them
natively Apple homekit compatible.

You can read about the how and the what in [this vxlabs post](https://vxlabs.com/2022/03/05/connecting-the-shelly-1-to-an-et-systems-gate-motor-for-apple-homekit-control/).

Shortly after that post appeared, we held a ["home automation"-themed Helderberg
Software Developers and Entrepreneurs meetup](https://fb.me/e/30MWR7Rq3). Thanks to current interest in the
topic, and the three absolutely brilliant speakers who were willing to take us
along on their HA adventure, it was the biggest and most active we've had in
years, by far!

In another probably surprising move, we are currently moving the meetup group
away from meetup.com and onto facebook as a [group](https://www.facebook.com/groups/helderberg.swdev.entrep.meetups/) (join if you're on fb!) from
where we can easily setup events.

Since 2019, meetup.com has been charging a pretty ridiculous $50 / 6-months fee
for a 100% free meetup with 0 commercial intent. In return for that, they
handle attendance (ish, we ofen had &gt;50% no-shows) and supply a bit of
discoverability.

Whatever the case may be, we now fortunately also have a snazzy website at
<https://helderberg.dev/> where you'll always be able to find the meetup, no
matter the events platform _du jour_.


## Techno interlude #2: Make Emacs More Prettier {#techno-interlude-2-make-emacs-more-prettier}

In spite of general business, I did have to make time for some `init.el`
wrangling, as is the privilege and sworn duty of every Emacs user.

This time, I refined my font and specifically `variable-pitch` setup.

I settled on the [Inter font](https://www.figma.com/blog/the-birth-of-inter/) because I liked the look of [obsidian.md](https://obsidian.md/), where it's
the default. Then I discovered that it was designed (based on the Roboto font)
by Figma designer Rasmus Andersson as "a font meant to make it easier to read
text on computer screens" (hey, that's exactly what I need!), and is now also
the default on github, mozilla, and notion. Pretty good typographic company
right there.

The other small change I made which was much more satisfying than I expected,
was setting the default font size based on the estimated pixel density of the
current screen.

This means that my Emacs will render its default fonts at sizes that make sense
on whichever display I'm using it.

Yes, I know that we should have been able to specify [resolution invariant font
sizes by now](https://github.com/kickingvegas/12pt-should-be-the-same-everywhere/blob/master/absoluteMeasurementDPI.md), but until that future arrives, my Emacs config will just have to
compensate.

The screenshot below shows an example of variable-pitch rendering on the left
(org-roam entry at the bottom, automatic topic backlinks at the top) and in the
centre (a slightly earlier draft of this post) and fixed-pitch on the right,
the relevant parts of my `init.el` showing the font and ([humanoid](https://github.com/humanoid-colors/emacs-humanoid-themes)) theme setup.

{{< figure src="images/2022/2022-03-21_20-07-58_screenshot.png" caption="<span class=\"figure-number\">Figure 2: </span>Emacs screenshot. No, [I don't like dark themes](/2021/08/20/weekly-head-voices-230-follow-your-blisters/#why-i-don-t-like-dark-mode-anymore)." link="images/2022/2022-03-21_20-07-58_screenshot.png" >}}


## Permutation City {#permutation-city}

When I saw a recommendation for [Permutation City, a 1994 sci-fi novel by the
Australian author Greg Egan](https://www.goodreads.com/book/show/156784.Permutation_City), I was hesitant.

Would a novel, written more than 25 years ago, about uploading digital copies
of humans to virtual reality (I wrote a bit about that in [WHV #199](/2020/07/01/weekly-head-voices-199-a-bit-stubborn/#a-totally-unexpected-ramble-on-cycles-patterns-and-teleportation) back in
2020), still be up to date with the latest ideas on the topic, seeing that
several adjacent fields of research have been advancing at a break-neck pace in
recent decades?

Weeeeell....

It turns out great sci-fi has no problem reaching ahead through a quarter
century of modern technological development and then blowing my mind several
times.

With Permutation City, Egan has written the book I would have wanted to write,
in my wildest fantasies of course, about humans, and copies of humans, and the
philosophically indistinguishable self-awareness and consciousness of the
copies, and of their copies, and so on, literally ad infinitum.

Fortunately this is my first Egan novel, and even more fortunately it turns out
that he has produced a [considerable collection of stories](https://www.goodreads.com/author/show/32699.Greg_Egan) which I now have the
privilege to proceed to assimilate!