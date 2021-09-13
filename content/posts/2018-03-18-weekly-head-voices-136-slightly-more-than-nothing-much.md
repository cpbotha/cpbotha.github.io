---
title: 'Weekly Head Voices #136: Slightly more than nothing much.'
author: cpbotha
type: post
date: 2018-03-18T20:53:28+00:00
url: /2018/03/18/weekly-head-voices-136-slightly-more-than-nothing-much/
categories:
  - weekly head voices
tags:
  - arduino
  - arm
  - bodega
  - cortex
  - darling brew
  - dornier
  - itead
  - japan
  - robotdyn
  - wa
  - warlord
  - xbee

---
{{< figure src="/wp-content/uploads/2018/03/IMG_3359-1024x768.jpg" link="/wp-content/uploads/2018/03/IMG_3359.jpg" caption="The majestic view from Bodega onto the Dornier cellar and the Hottentots-Holland mountain behind it.">}} 

Welcome back peeps! Make yourselves at home.

It seemed that nothing much happened during most of the week, but I started writing anyway. It turns out there was slightly more than nothing much. Writing stuff down does have its perks.

# vimium

Pro-tip of the week: Install [vimium][1]. It’s a chrome extension which enables you to SURF THE INFORMATION HIGHWAY with just a bunch of keyboard shortcuts.

I avoided this for the longest time because it has the word “vim” in its name, but I was wrong.

I can now waste time on reddit, twitch and youtube 73% more efficiently, every day.

# nerd works

As far as I can remember, my work week was pretty straight-forward.

I started implementing PDF reports again, but for a different application. [wkhtmltopdf][2] is now magically broken in different ways from [the previous time][3]. Compared to bundling and maintaining a stripped-down [TeXLive][4], or paying the $995 license for [pdftk][5] with which PDF forms can be programmatically filled in, this is the best choice at the moment.

Remember, [there are no answers, only choices][6], even when baking PDFs.

For Most Major Sideproject (MMS) I unfortunately had to do some front-end programming. I say unfortunately, because the back-end is all machine learning and cleverness, and then I smash my little programming clown car into the idiot brick wall that is web frontends. At least react makes the crash slightly less painful, and this time [react-router][7] helped me to get my URLs synchronised with app state fairly easily.

Ok maybe it’s not _that_ bad.

My new [Robotdyn Arduino SAMD21 M0][8] boards arrived! This is arduino, but with a 32bit ARM Cortex M0+ instead of the Atmel 328p on the UNO boards. After some more hours of struggling to get Arduinos talking to each other via XBEE radios, I now know much more about programming these gadgets than I ever wanted to.

Mostly due to the very-badly-documented-and-seemingly-unsupported [itead arduino-xbee interface boards][9] I’m using, I am closer but have not yet received any cigars. (pro-tip: That extra top 3.3V jumper does more than just control level shifting. It also connects A0, RTS and DIN together. If you think you’re going to use A0 for RTS, your xbee will mysteriously hardware reset every 5 seconds. However, if you disconnect the jumper, your board will hardware reset every 5 seconds no matter what you do. Pro-tip: Don’t buy itead.)

# new beer warlord

On Wednesday I tasted a new craft beer (this does not happen very often anymore, as I’ve had almost all of them) during a Top Secret Business Meeting. It’s the War Lord IPA by Darling Brew:

{{< figure src="/wp-content/uploads/2018/03/warlord_beer_cutout-441x1024.png" link="/wp-content/uploads/2018/03/warlord_beer_cutout.png" >}}

This might even be more metal than their [Bone Crusher][10] \<INSERT HEAVY METAL GUITAR RIFF HERE\>, which is extremely high praise. As IPAs go, I will definitely make this choice again, perhaps  even in the very near future.

# part of the weekend never dies

On Saturday and Sunday morning (overnight parties are the BEST parties) we had long-time friends over for a dinner party.

Something like 25 years ago we did the [Magoebaskloof hiking trail][11] together. There’s nothing like sharing meals of dried soya (just add water, INDISTINGUISHABLE from meat the packet said), dried mash (“smash” I believe) and dried vegetables during days of hiking through the forest for getting to know each other better.

Besides the hiking, and many student parties, there was also the little matter of me meeting my life partner through this connection. Not unimportant.

Anyways, craft beer ([King’s Blockhouse IPA][12], nice and strong), great local wine (a Chardonnay-Pinot Noir blend which more or less satisfies my “expensive Chardonnay” criterion) and brilliant food (chicken, extremely slow over the fire) acted as the culinary backdrop for naturally flowing and energising conversation.

Thank you long-time friends!

Late morning Sunday we left for a family lunch at Bodega, restaurant at Dornier vineyard. This restaurant has made previous appearances in [WHV #76 (July 1, 2014)][13] and [WHV #102 (January 20, 2016)][14].

Again I can do nothing other than award it the WHV three thumbs up award! Wine-food-scenery-climate combinations really are amazing.

(I just noticed that the wine which was paired with my Mauritian (no, no Martian fish yet) seabass, and blew me away, also blew me away in 2014. It’s the Donatus White, Semillon-Chenin Blanc blend. External memories FTW.)

# let us ponder: wa

Westerners are often very individualistic.

We are brought up with the mission to “be yourself”.

In Japan, there is “wa” (和) which [wikipedia describes as][15]: _… harmony. It implies a peaceful unity and conformity within a social group, in which members prefer the continuation of a harmonious community **over their personal interests**_. (emphasis mine)

I understand that this has a different set of downsides to our individualism, but group harmony sure sounds nice. Perhaps in the future society we are going to start building soon, we could somehow combine “wa” with a deep respect for the scientific method, and in this way finally transform into the Star Trek Federation that we were promised.

# bises

Have a productive but especially harmonious week kids! I hope to see you again soon.

 

 [1]: https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en
 [2]: https://wkhtmltopdf.org/
 [3]: /2015/06/21/weekly-head-voices-92-the-cake-is-a-lie/
 [4]: https://www.tug.org/texlive/
 [5]: https://www.pdflabs.com/tools/pdftk-server/
 [6]: /2016/02/02/weekly-head-voices-103-chips/#inspiring-quotes-that-you-can-repost-if-you-want
 [7]: https://github.com/ReactTraining/react-router
 [8]: https://robotdyn.com/samd21-m0.html
 [9]: https://www.itead.cc/wiki/XBee_Shield
 [10]: /2014/04/21/weekly-head-voices-68-harsh-autumn-weekends/
 [11]: https://www.sa-venues.com/things-to-do/limpopo/magoebaskloof-hiking-trail/
 [12]: https://www.devilspeakbrewing.co.za/kings-blockhouse-ipa/
 [13]: /2014/07/01/weekly-head-voices-76-someone-is-wrong-on-the-internet/
 [14]: /2016/01/20/weekly-head-voices-102-high-on-life/
 [15]: https://en.wikipedia.org/wiki/Wa_(Japanese_culture)
