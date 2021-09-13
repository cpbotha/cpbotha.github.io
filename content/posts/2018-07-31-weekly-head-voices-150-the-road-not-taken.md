---
title: 'Weekly Head Voices #150: The Road not Taken.'
author: cpbotha
type: post
date: 2018-07-31T20:40:21+00:00
url: /2018/07/31/weekly-head-voices-150-the-road-not-taken/
categories:
  - weekly head voices
tags:
  - deep learning
  - dired
  - emacs
  - luna
  - poetry
  - robert frost
  - running
  - wisdom tooth
  - xero

---
{{< figure src="/wp-content/uploads/2018/07/IMG_2740-768x1024.jpg" link="/wp-content/uploads/2018/07/IMG_2740.jpg" caption="Photo of a cotula lineariloba flower, taken by GOU#1, age 12.">}} 

This edition of the WHV covers the week from Monday, July 23 up to and including Sunday, July 29.

# Running update

Strava says I’ve just passed the 300km threshold in my [Luna Mono 2 sandals][1].

It also says I’ve done 27km in my [Xero Genesis sandals][2], or as I have begun to call them, _Xero Tolerance_.

You make one mistake, and something will break. You do get to keep all the bloody pieces.

In any case, when I started on this barefoot-style / natural running adventure, I had subconsciously set myself the limit of 200km before evaluating the success of the experiment.

At 200km, the experiment was still unsuccessful (different parts of feet and ankles were taking turns complaining) so I moved the threshold to 300km, with the plan to move it to 400km if required.

I call this The Stubborn Scientific Method(tm): You keep _running_ the experiment (harr harr) until it says what you want it to say.

To be fair, in this specific case an injury would have (and still can), stop the experiment. Most fortunately the muscles, bones and tendons in my feet, ankles and calves, although complaining quite audibly, have held up.

This past Sunday I did a long(ish) run where it felt for the first time like my feet and ankles had finally toughened up enough (and perhaps my form had also improved slightly) to just keep on propelling me forward quietly and efficiently.

Together with the brilliant sunny winter morning conditions, this conspired to reconfigure my face machine into a rather long-lasting grin.

I am carefully optimistic that I might be able to make this specific adventure a more permanent one, and that makes me really happy.

# The Emacs Section

_NERD-ALERT. SKIP TO THE NEXT SECTION IF YOU ARE NOT INTO TEXT EDITORS!_

A friend from work sent me a ZIP file with research data.

I was super surprised that I could easily decompress the ZIP file using Emacs Dired (Dired is of course the file-manager built into Emacs, doh), but that there was no easy way to mark and extract specific files from the archive.

I found [an SO answer with a piece of Emacs Lisp code][3] that someone had put together and integrated it with my Emacs.

It worked, but it didn’t default to the opposite Dired file-list pane as all commander-style tools should do, and by default it re-created relative paths, which is the opposite of the default in most two-pane commanders I know.

As is the wont of Emacs users, I reshaped the code ever so slightly to work like I thought it should.

Shaping Emacs Lisp code has a pleasant fluid feeling to it. Code is data, code is configuration, data flows through code.

I’m telling you this story, because it was a nice little reminder of one of the reasons I like this software so much.

You can find [my modified version of archive-extract-to-file.el as a github gist][4].

# The Odd Bits of Interesting News Section

{{< figure src="/wp-content/uploads/2018/07/Screen-Shot-2018-07-31-at-22.22.59-1024x509.png" link="/wp-content/uploads/2018/07/Screen-Shot-2018-07-31-at-22.22.59.png" >}}

  * [Differentiable Image Parameterizations][5], a beautiful machine learning article on Distill that surveys and showcases different techniques for generating beautiful images with deep learning. These networks sort of learn to see in order to solve specific tasks, but you can tickle them in different ways to get them to show you the insides of their visual circuitry, and it’s quite beautiful.
  * [The Prophylactic Extraction of Third Molars: A Public Health Hazard][6] is an article which was published all the way back in 2007. It makes the claim that at least two thirds of wisdom tooth extraction are unnecessary. One could say that their only function is to… _extract_ your money. BA DUM TSSSSS! To that I would like to add: WHY DENTISTRY WHY? HAVE YOU NOT HURT US ENOUGH?!
  * A colleague at work emailed [this TechCrunch post about a 3D printed neural network][7] that diffracts light going through in order to do its trained inference work on incoming images. Although it’s a retro-futuro-mind-bending idea to do it with a whole neural network, and it smacks of hell-yeah-this-is-what-scifi-promised-me-that-AI-would-look-like, I could not help but recall a certain Very Flat Cat telling us about this sort of passive light-based computation almost 20 years ago.

# The Poetry Section

GOU#1 had to select an English poem to recite for class.

From the depths of my memory bubbled up [The Road not Taken by Robert Frost][8].

I had forgotten how much subtlety and recognisable human complexity this poem was able to pack into such a petite little frame. If you have the time, read the analysis linked above after spending some time with the poem itself.

> Two roads diverged in a yellow wood,
  
> And sorry I could not travel both
  
> And be one traveler, long I stood
  
> And looked down one as far as I could
  
> To where it bent in the undergrowth;
> 
> Then took the other, as just as fair,
  
> And having perhaps the better claim,
  
> Because it was grassy and wanted wear;
  
> Though as for that the passing there
  
> Had worn them really about the same,
> 
> And both that morning equally lay
  
> In leaves no step had trodden black.
  
> Oh, I kept the first for another day!
  
> Yet knowing how way leads on to way,
  
> I doubted if I should ever come back.
> 
> I shall be telling this with a sigh
  
> Somewhere ages and ages hence:
  
> Two roads diverged in a wood, and I—
  
> I took the one less traveled by,
  
> And that has made all the difference.

Friends, no matter which paths you take this week, I hope that we may meet again.

 [1]: /2018/04/08/weekly-head-voices-139-luna/
 [2]: /2018/07/17/weekly-head-voices-148-data-stylist/#weekend-running-update
 [3]: https://emacs.stackexchange.com/a/3843/8743
 [4]: https://gist.github.com/cpbotha/05e07dee7fd8243ba73339be186c0b88
 [5]: https://distill.pub/2018/differentiable-parameterizations/
 [6]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1963310/#__ffn_sectitle
 [7]: https://techcrunch.com/2018/07/26/this-3d-printed-ai-construct-analyzes-by-bending-light/
 [8]: https://www.poetryfoundation.org/poems/44272/the-road-not-taken
