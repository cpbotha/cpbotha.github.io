---
title: 'Weekly Head Voices #118: Accelerando.'
author: cpbotha
type: post
date: 2017-03-10T21:14:38+00:00
url: /2017/03/10/weekly-head-voices-118-accelerando/
categories:
  - weekly head voices
tags:
  - deep learning
  - emacs
  - google
  - gpu
  - nimbix
  - nvpy

---
Too much nerdery took place from Monday February 20 to Sunday March 5. Fortunately, be the end of that period, we found ourselves here:<figure id="attachment_2844" aria-describedby="caption-attachment-2844" style="width: 840px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip.jpg" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2844" data-permalink="https://cpbotha.net/2017/03/10/weekly-head-voices-118-accelerando/looking_at_hangklip/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip.jpg" data-orig-size="4618,2436" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;2.2&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;PRIV&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1488735201&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;4.75&quot;,&quot;iso&quot;:&quot;50&quot;,&quot;shutter_speed&quot;:&quot;0.00091491308325709&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="looking_at_hangklip" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip-300x158.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip-1024x540.jpg" class="wp-image-2844 size-large" src="https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip-1024x540.jpg" alt="" width="840" height="443" srcset="https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip-1024x540.jpg 1024w, https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip-300x158.jpg 300w, https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip-768x405.jpg 768w, https://cpbotha.net/wp-content/uploads/2017/03/looking_at_hangklip-1200x633.jpg 1200w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" /></a><figcaption id="caption-attachment-2844" class="wp-caption-text">The view from the shark lookout all the way to Hangklip.</figcaption></figure> 

# bibtex references in orgmode

For a technical report, I thought it would be handy going from Emacs orgmode (where all my lab notes live in any case) to PDF via LaTeX.

This transformation is more or less built-in, but getting the whole machinery to work with citations from a local BibTeX export from my main Zotero database does not work out of the box.

I wrote [a post on my other even-more-nerdy blog][1] showing the extra steps needed to turn this into an easy-peasy 38-shortcut-key-combo affair.

# Google GCE K80 CPUs available, cheap(ish)!

I&#8217;ve been using a cloud-hosted NVIDIA Tesla from Nimbix for my small-scale deep learning experiments with TensorFlow. This has also helped me to resist the temptation of buying an expensive new GPU for my workstation.

However, Google [Compute Engine has finally shipped (in beta) their cloud-based GPU product][2]. Using [their pricing calculator][3], it turns out I can get a virtual machine with 8 CPU cores, 30G of RAM, 375GB of local SSD and a whole NVIDIA Tesla K80 GPU (12GB of memory) in their EU data centre for a paltry $1.32 / hour.

This is significantly less than half of what I paid Nimbix!

(That resistance is going to crumble, the question is just when. Having your stuff run locally and interactively for small experiments still beats the 150ms latency from this here tip of the African continent to the EU.)

# nvpy leaves the nest :\`(

My most successful open source project to date is probably [nvpy][4], the cross-platform (Linux, macOS, Windows) Simplenote client. 600+ stars on github is not A-list, but it&#8217;s definitely also nothing to sneeze at.<figure id="attachment_2848" aria-describedby="caption-attachment-2848" style="width: 300px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer.png" data-rel="lightbox-image-1" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2848" data-permalink="https://cpbotha.net/2017/03/10/weekly-head-voices-118-accelerando/20170304-nvpy-github-stats-before-xfer/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer.png" data-orig-size="1021,449" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="20170304-nvpy-github-stats-before-xfer" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer-300x132.png" data-large-file="https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer.png" class="wp-image-2848 size-medium" src="https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer-300x132.png" alt="" width="300" height="132" srcset="https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer-300x132.png 300w, https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer-768x338.png 768w, https://cpbotha.net/wp-content/uploads/2017/03/20170304-nvpy-github-stats-before-xfer.png 1021w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-2848" class="wp-caption-text">nvpy stats right before the hand-over</figcaption></figure> 

Anyways, I wrote nvpy in 2012 when I was still a heavy Simplenote user and there was no good client for Linux.

In the meantime, Emacs had started taking over my note-taking life and so in October of 2014, I made the decision to [start looking for a new maintainer][5] for my open-source baby nvpy.

That attempt was not successful.

By the end of 2015 / early 2016 I had a bit of a Simplenote / nvpy revival, as [I was using the official client on my phone, and hence nvpy on the desktop][6].

Emacs put a stop to that revival also by magically becoming available on my phone as well. I have to add that the Android Simplenote client also seems to have become quite sluggish.

I really was not using nvpy anymore, but I had to make plans for the users who did.

On Saturday March 4, I approached github user [yuuki0xff][7], who had prepared a pretty impressive background-syncing PR for nvpy, about the possibility of becoming the new owner and maintainer of nvpy.

To my pleasant surprise, he was happy to do so!

It is a strange new world that we live in where you create a useful artifact from scratch, make it available for free to anyone that would like to use it, and continue working on improving that artifact for a few years, only to hand the whole thing over to someone else for caretaking.

The handing-over brought with it mixed feelings, but overall I am super happy that my little creation is now in capable and more active hands.

# Navel Gaze

Fortunately, there&#8217;s a _handy_ twitter account reminding us regularly how much of 2017 we have already put behind us (thanks [G-J van Rooyen][8] for the tip):

<blockquote class="twitter-tweet" data-width="550">
  <p lang="und" dir="ltr">
    ▓▓▓░░░░░░░░░░░░ 17%
  </p>
  
  <p>
    &mdash; Year Progress (@year_progress) <a href="https://twitter.com/year_progress/status/837845049257902080">March 4, 2017</a>
  </p>
</blockquote>



That slowly advancing progress bar seems to be very effective at getting me to take stock of the year so far.

Am I spending time on the right things? Am I spending just the right amount of effort on prioritising without this cogitation eating into the very resource it&#8217;s supposed to be optimising? Are my hobbies optimal?

I think the answer is: One deliberate step after the other is best.

 [1]: https://vxlabs.com/2017/02/20/from-org-file-with-local-bibtex-to-latex-and-pdf/
 [2]: https://cloud.google.com/compute/docs/gpus/
 [3]: https://cloud.google.com/products/calculator/
 [4]: https://github.com/cpbotha/nvpy
 [5]: https://groups.google.com/forum/#!msg/nvpy/_GuWNfnxY9E/S0Vel4i4MEgJ
 [6]: /2016/01/05/note-taking-strategy-early-2016/
 [7]: https://github.com/yuuki0xff
 [8]: https://twitter.com/gvrooyen
