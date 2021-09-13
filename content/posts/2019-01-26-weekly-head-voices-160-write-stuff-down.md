---
title: 'Weekly Head Voices #160: Write stuff down.'
author: cpbotha
type: post
date: 2019-01-26T17:10:31+00:00
url: /2019/01/26/weekly-head-voices-160-write-stuff-down/
categories:
  - weekly head voices
tags:
  - 101 mind-tricks
  - avocado tree
  - gutenberg
  - ios
  - ipad
  - org2blog
  - potjie
  - prefrontal cortex
  - solar
  - telesensi
  - textastic
  - tips

---
{{< figure src="/wp-content/uploads/2019/01/chicken_potjie_no2-1024x768.jpg" link="/wp-content/uploads/2019/01/chicken_potjie_no2.jpg" caption="In the foreground, the mortar and pestle I used to mash together garlic, ginger, a serenade chilli, green cardamom pods, a whole cinnamon quill, one bay leaf, some curry powder for even more oomf, turmeric, coriander, salt and a few cloves. This paste ended up in that blurry red cast iron pot on the coals to result, a few hours later, in a delectable chicken curry potjie.">}} 

Welcome to the first WHV of the year 2019 folks!

In what is hopefully just a minor incident and not a portent of calamitous events to come, we have already skipped the first two weeks of the year, which means this WHV looks back at the three weeks from Monday January 7 to Saturday January 26.

I guess this would not be the WHV if we did not start off with some sort of awkwardness or miscellaneous embarrassment, so: CHECK!

Because you are probably thirsty for your WHV now, I tried to write you a long and rambly edition, with pictures! (Because it’s so long and rambly, and because markdown, I have liberally sprinkled with headings and sub-headings, so that those of you with lives outside of blog reading can hop, skip and jump through like the professionals you are.)

## The future is here: Long-form blog posts on the iPad.

This also would not be the WHV if we did not have some little digital trick to reveal: Today’s attempt is that this post is being written, for the largest part, on a 2018 iPad (the cheapest one) with an old (also very cheap) bluetooth keyboard.

Because I really don’t like the new block-based WordPress 5.0 editor, named in an entirely non-hubristic fashion “Gutenberg”, but it does fortunately support importing markdown formatted blog posts (just make sure you don’t hard-wrap anything), and because I like trying new things, I am typing this on the iPad using the iOS version of [Textastic][1].

A few hours ago, it looked like this:
{{< figure src="/wp-content/uploads/2019/01/img_0005-1024x768.png" link="/wp-content/uploads/2019/01/img_0005.png" >}} 

In contrast to the direct [orgmode to wordpress Emacs workflow][2] I normally use, this workflow enables me to copy and paste sections of markdown text into WordPress. Each pasted section is automatically imported as WordPress blocks, based on the markdown structure.

This means I can position and edit images using the WordPress interface, but author the text using Markdown. With [org2blog][3] the whole post, including images, has to go through life as an orgmode file, which is brilliant for my more technical posts, but not so much for prose-heavy blog posts such as this one.

### BTW 1: Why I don’t (yet) like the new WordPress editor.

The old WordPress editor enabled me to focus on the content and just write.

The new [Gutenberg editor][4] now wants me to create a bunch of blocks, e.g. paragraph, image, paragraph, bullet list, etc., and then work with those blocks.

That’s really great if you’re building a site, but not so much when you would just like to get down and write that blog post.

Although this is now the standard editor in WordPress, there are still bugs, such as the fact that my cursor keeps on jumping to the start of the block while I’m typing, which is not irritating at all, and the not unimportant observation that none of the mobile apps support Gutenberg yet.

WordPress-using readers, what do you think?

(P.S. Another just-discovered issue: In Gutenberg, your biggest heading is H2. H1 is not available in the UI normally. When pasting in markdown, H1s do display, but do not show in the type-UI as anything. Here is [a confusing Gutenberg bug report][5].)

### BTW 2: Why Textastic? (AKA At least it will syntax highlight your Orgmode.)

The main reason I found and purchased Textastic, was that I ran into [Jez Cope’s github repo][6] with a TextMate Bundle (that’s an editor configuration) that was made for Textastic to support editing Emacs orgmode files.

As is the age-old open source way, there were a few small bugs which I [fixed in my fork][7], which you should definitely get if you are in the same I-want-to-edit-Orgmode-on-my-iOS boat as I am. It’s not a very large boat, but it’s super fun!

(There is no Emacs on iOS. This is in my view the greatest downside of iOS. It turns out that Apple generally does not allow apps with embedded interpreters on the app store. However, I am still trying to find out why there are no iOS-capable Emacs source code forks available.)

### BTW 3: The iPad with keyboard is a shockingly good laptop replacement.

I recently recommended to a privacy-conscious reader who was searching for an affordable Linux-running laptop in South Africa, that she instead consider buying an iPad with bluetooth keyboard.

Down here a brand new 2018 iPad costs R5999. A cheap keyboard cover (e.g. Body Glove) can be had for about R860.

If you compare this to any new laptop of R6900 (about EUR 444) which will probably be sold with Windows included, you get a computing device with a fantastic quality multi-touch screen, great battery life, best-in-class security, almost no maintenance, and a fantastic app ecosystem. To seal the deal, the iPad’s resale value is proportionally probably also much better than that entry-level laptop.

_After_ I sent that email, I started with this iPad + cheap bluetooth keyboard experiment to try it for myself. I have to say that the experience has been way better than I expected.

For a large subset of laptop users, and for a large subset of workflows and tasks, this is a really great solution.

Please don’t worry (too much) yet, I am not planning one of those “I switched to an iPad as my main computing device” blog posts. I would not be able to survive without my development tools, and I would especially not be able to survive without my Emacs.

## PV Solar installation progress

As I excitedly [announced in WHV #159][8] (slightly more than a month ago), we had decided that it was time to get a photovoltaic solar power system installed at the house.

I found a local installer with the required PVGreenCard accreditation and started the consultation process.

Unfortunately, the installer did not seem to be prepared for a customer that would not stop asking questions. The customer even went so far as to pose questions that challenged the installer’s brand loyalty!

I really do understand that I’m probably not the easiest end-user, but I don’t think that an expert’s brand loyalty should get in the way of reason, and far more importantly in the way of basic physics.

To make a long story short, I ended up getting fired by the installer.

This was probably for the better: He can now continue doing well-practised installs for other clients who don’t ask (so many) questions, and I suddenly had the opportunity to find a new, more engineer-friendly installer, and to continue learning.

Following are two noteworthy learnings:

### Learning 1: You should almost always try to oversize the photovoltaic array

If the equipment states for example 4600kVA, then you are usually quite safe installing from 25% up to 30% more kWp of solar panels.

Oversizing will mean that on very sunny days you’ll get peaks higher than the maximum rated PV, which can be handled for short periods by the solar equipment, but more importantly, you’ll be able to generate more electricity when there is less sun, which is most of the time.

In other words, you increase the area under the curve of kW generated per hour.

By the way, I emailed GoodWe (they make the hybrid inverters I have my eye on) who confirmed that their EM range supports 27.8% oversizing. The ES range advertise 30% PV oversizing on the box.

It is of course an interesting question what exactly is meant by oversizing. Do they support pumping 30% more power into the inverter for 5 minutes, or for 2 hours?

### Learning 2: powerforum.co.za is a great source of information.

[This forum][9] has a surprisingly high signal to noise ratio.

There are a number of experts hanging around, including one of Victron’s super helpful and knowledgeable R&D engineers, and the archive posts are invaluable as you try to navigate [the quagmire][10] of often conflicting information.

## Avocado baby progress: Very much touch and go.

The baby avocado tree, in spite of being being watered almost every day (thank you rainwater harvest!) does not seem to be doing too well.

Because the summer sun down here can be quite vicious, the tree has its own little pink umbrella.

The current plan is to feed it more compost, and, if that fails, to try to transplant it out of the big, wild garden and into a pot with softer, kinder earth.

## How to explain complicated topics

The international and yearly [Machine Learning Summer School took place in Stellenbosch this year][11], from Monday, January 7 to Friday, January 18.

As you can see from the programme, there were a bunch of heavy hitting speakers present both physically and virtually, including the super resourceful (failed super resolution pun, su(p)e(r) me) Dr Stefan van der Walt, who gave a talk on good scientific software.

Anyways, because I am currently in a more commercial configuration, I could not justify taking two weeks out, and instead opted for a day visit at the start of the congress.

It is a testament to the current prominence of the field that the list of international sponsors included Microsoft, Apple, SAP, Uber _and_ Amazon.

It was gratifying to experience a sampling of such a well-organized international gathering here in my neck of the woods.

On the first day, we had a high throughput introduction to causality, probabilistic thinking, and variational inference. All the presenters were clearly good speakers, but they weren’t all equally experienced in teaching such complex material.

(At one point one of the statisticians I was chatting to in break admitted having difficulty keeping up with the math. I did not feel **that** stupid anymore.)

“What is the difference between being a good speaker and an experienced teacher?”, you might now ask.

Great question, I would then say, grateful for the opportunity to explain.

What I was missing in the one specific case I do not want to be too specific about, was that the presenter did a great job of talking about each of a long list of concepts relevant to his topic, but somehow forgot that one of the most important parts of teaching is communicating the conceptual framework into which all of those concepts fit.

Conceptual frameworks are also one of those multi-scalar things: Each group of factoids can be gratifyingly embedded into a slightly higher level component, groups of which can be slotted into the overarching “big idea”, or another level of compnonent. (It’s turtles all the way down.)

As great lecturers talk, they keep on bringing their narrative back up to the higher-level embedding construct.

It looks something like this:
{{< figure src="/wp-content/uploads/2019/01/teach_complicated_things-1024x576.png" link="/wp-content/uploads/2019/01/teach_complicated_things.png" caption="Yes, I did make this especially for this post, especially for you. No, I am not sure exactly why.">}} 

By repeatedly diving deeper into the details, and then following the conceptual link back up to the higher-level constructs and especially your big idea, your listeners will start to see the beautiful fractal of understanding that you are guiding them through.

## What will I be working on this year?

At this moment, 2019 is shaping up to be pretty exciting work-wise.

We just heard that we will be able to continue for some months more working on the X-Ray based surgical planning project we worked on last year.

Partly thanks to the great deep learning work of two summer interns (note: Southern Hemisphere means summer interns over December and January, which might be weird if you’re from the Northern Hemisphere) we are in great shape for all of the deep neural network-based image understanding plans we need to execute on.

This year I will also be spending more time on [TeleSensi, our FDA-certified tele-auscultation product][12]. This is less rocket-sciencey than the surgical planning project, but super interesting to work on, as it has many more users on the open market.

(That being said, we do have plans to increase the level of rocket science significantly. I am not called the science officer for nothing… (well, that and also the fact that I got to choose my own title, and so I chose the same as Spock on the USS Enterprise).)

## Do you write stuff down?

You might remember from WHV #155 [my trick of starting the day with a checklist][13].

A part of that checklist is a checklist of habits which I try to form and maintain, called The HabitFormer(tm). Every item that I sufficiently address gets a super satisfying little `[X]` mark, which feels a whole lot better than the sadly empty `[ ]` construct.

Here is the current list:

  * did you write stuff down?
  * are you satisfied with number of pomodori?
  * 7.5 hrs sleep last night
  * meditate <– (WHV _hidden_ pro-tip: Get the [Waking Up][14] app by Sam Harris. Thanks LM for the fantastic recommendation.)
  * stand at desk
  * do valuable things
  * fruit & veg
  * reading
  * thinking
  * running or other exercise

Ironically enough, the first item is brand new on the list.

I somehow forgot my habit of writing, during the day, a little done list / random thoughts lists. After bringing this habit back I noticed what difference it made.

At regular intervals during the day, I will spend a minute or three writing down what I had completed, or what I was thinking. This moment of introspection would either result in a pleasant bit of satisfaction with some small task taken care of, or, more often, it would reel me back in from a spot of less than deliberate action and enable me to bring back my attention to the point of focus.

I’m filing this under “101 tricks to get your [rider back on your elephant][15]“.

Alright friends, thank you very much for joining me on this part of my journey. I am looking forward to our next interaction!

 [1]: https://www.textasticapp.com/
 [2]: https://vxlabs.com/2014/05/25/emacs-24-with-prelude-org2blog-and-wordpress/
 [3]: https://github.com/org2blog/org2blog
 [4]: https://wordpress.org/gutenberg/
 [5]: https://github.com/WordPress/gutenberg/issues/4234
 [6]: https://github.com/jezcope/Org.tmbundle
 [7]: https://github.com/jezcope/Org.tmbundle/pull/5
 [8]: /2018/12/19/weekly-head-voices-159-extreme/#extreme-solar
 [9]: https://powerforum.co.za/
 [10]: https://powerforum.co.za/topic/2791-experience-getting-city-of-cape-town-to-sign-off-a-zero-feed-in-system-with-inverter-maximum-output-greater-than-35kva/
 [11]: https://mlssafrica.com
 [12]: https://www.telesensi.com
 [13]: https://cpbotha.net/2018/10/12/weekly-head-voices-155-lush/#productivity-pro-tip-fool-yourself-into-doing-a-good-daily-review
 [14]: https://wakingup.com/
 [15]: https://cpbotha.net/2018/05/20/weekly-head-voices-143-the-rider-and-the-elephant/
