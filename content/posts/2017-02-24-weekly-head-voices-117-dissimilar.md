---
title: 'Weekly Head Voices #117: Dissimilar.'
author: cpbotha
type: post
date: 2017-02-24T20:14:15+00:00
url: /2017/02/24/weekly-head-voices-117-dissimilar/
categories:
  - weekly head voices
tags:
  - dissimilarity representation
  - emacs
  - ipython
  - jupyter
  - machine learning
  - todoist

---
The week of Monday February 13 to Sunday February 19, 2017 might have _appeared_ to be really pretty boring to any inter-dimensional and also more mundane onlookers.

(I mention both groups, because I&#8217;m almost sure I would have detected the second group watching, whereas the first group, being interdimensional, would probably have been able to escape detection. _As far as I know_, nobody watched.)

I just went through [my orgmode journals][1]. They are filled with a mix of notes on the following mostly very nerdy and quite boring topics.

_**Warning:** If you&#8217;re not an emacs, python or machine learning nerd, there is a high probability that you might not enjoy this post. Please feel free to skip to the pretty mountain at the end!_

# Advanced Emacs configuration

I finally migrated my whole configuration away from [Emacs Prelude][2].

Prelude is a fantastic Emacs &#8220;distribution&#8221; (it&#8217;s a simple git clone away!) that truly upgrades one&#8217;s Emacs experience in terms of look and feel, and functionality. It played a central role in my return to the Emacs fold after a decade long hiatus spent with JED, VIM (there was more really weird stuff going on during that time&#8230;) and Sublime.

However, it&#8217;s a sort of rite of passage constructing one&#8217;s own Emacs configuration from scratch, and my time had come.

In parallel with Day Job, I extricated Prelude from my configuration, and filled up the gaps it left with my own constructs. There is something quite addictive using emacs-lisp to weave together whatever you need in your computing environment.

To celebrate, I decided that it was also **time to move my todo system away from [todoist][3]** (a really great ecosystem) and into Emacs orgmode.<figure id="attachment_2833" aria-describedby="caption-attachment-2833" style="width: 678px" class="wp-caption alignnone">

[<img data-attachment-id="2833" data-permalink="https://cpbotha.net/2017/02/24/weekly-head-voices-117-dissimilar/todoist-interview-screenshot_1-678x554/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/02/Todoist-interview-screenshot_1-678x554.jpg" data-orig-size="678,554" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="Todoist-interview-screenshot_1-678&#215;554" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/02/Todoist-interview-screenshot_1-678x554-300x245.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2017/02/Todoist-interview-screenshot_1-678x554.jpg" class="size-full wp-image-2833" src="https://cpbotha.net/wp-content/uploads/2017/02/Todoist-interview-screenshot_1-678x554.jpg" alt="" width="678" height="554" srcset="https://cpbotha.net/wp-content/uploads/2017/02/Todoist-interview-screenshot_1-678x554.jpg 678w, https://cpbotha.net/wp-content/uploads/2017/02/Todoist-interview-screenshot_1-678x554-300x245.jpg 300w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 984px) 61vw, (max-width: 1362px) 45vw, 600px" />][4]<figcaption id="caption-attachment-2833" class="wp-caption-text">From this&#8230; (beautiful multi-platform graphical app)</figcaption></figure> <figure id="attachment_2834" aria-describedby="caption-attachment-2834" style="width: 620px" class="wp-caption alignnone">[<img data-attachment-id="2834" data-permalink="https://cpbotha.net/2017/02/24/weekly-head-voices-117-dissimilar/wpid-example-agenda/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/02/wpid-example-agenda.png" data-orig-size="620,592" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="wpid-example-agenda" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/02/wpid-example-agenda-300x286.png" data-large-file="https://cpbotha.net/wp-content/uploads/2017/02/wpid-example-agenda.png" class="size-full wp-image-2834" src="https://cpbotha.net/wp-content/uploads/2017/02/wpid-example-agenda.png" alt="" width="620" height="592" srcset="https://cpbotha.net/wp-content/uploads/2017/02/wpid-example-agenda.png 620w, https://cpbotha.net/wp-content/uploads/2017/02/wpid-example-agenda-300x286.png 300w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 984px) 61vw, (max-width: 1362px) 45vw, 600px" />][5]<figcaption id="caption-attachment-2834" class="wp-caption-text">&#8230; to this!! (YOUR LIFE IN PLAINTEXT. DUN DUN DUUUUUN!)</figcaption></figure> 

I had sort of settled with todoist for the past few years. However, my yearly subscription is about to end on March 5, and I&#8217;ve realised that with the above-mentioned Emacs-lisp weaving and orgmode, there is almost unlimited flexibility also in managing my todo list.

Anyways,  I have it setup so that tasks are extracted right from their context in various orgfiles, including my current monthly journal, and shown in a special view. I can add arbitrary metadata, such as attachments and just plain text, and more esoteric tidbits such as live queries into my email database.

The advantage of having the bulk of the tasks in my month journal, means I am forced to review all of the remaining tasks at the end of the month before transferring them to the new month&#8217;s journal.

We&#8217;ll see how this goes!

# Jupyter Notebook usage

Due to an interesting machine learning project at work, I had a great excuse to spend some quality time with the [Jupyter Notebook][6] (formerly known as IPython Notebook) and the scipy family of packages.

Because Far Too Much Muscle-Memory, I tried interfacing to my notebook server using [Emacs IPython Notebook (EIN)][7], which looked like this:

<a href="https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img data-attachment-id="2827" data-permalink="https://cpbotha.net/2017/02/24/weekly-head-voices-117-dissimilar/ipython-notebook-in-emacs-with-ein/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein.png" data-orig-size="716,709" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="ipython-notebook-in-emacs-with-ein" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein-300x297.png" data-large-file="https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein.png" class="alignnone size-medium wp-image-2827" src="https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein-300x297.png" alt="" width="300" height="297" srcset="https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein-300x297.png 300w, https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein-150x150.png 150w, https://cpbotha.net/wp-content/uploads/2017/02/ipython-notebook-in-emacs-with-ein.png 716w" sizes="(max-width: 300px) 85vw, 300px" /></a>

However, the initial exhilaration quickly fizzled out as EIN exhibits some flakiness (primarily broken indentation in cells which makes this hard to interact with), and I had no time to try to fix or work-around, because day job deadlines. (When I have a little more time, I will have to get back to the EIN! Apparently they were planning to call this new fork Zwei. Now that would have been awesome.)

So it was back to the Jupyter Notebook. This time I made an effort to learn all of the new hotkeys. (Things have gone modal since I last used this intensively.)

The Notebook is an awe-inspiringly useful tool.

However, the cell-based execution model definitely has its drawbacks. I often wish to re-execute a single line or a few lines after changing something. With the notebook, I have to split the cell at the very least once to do this, resulting in multiple cells that I now have to manage.

In certain other languages, which I cannot mention anymore because I have utterly exhausted my monthly quota, you can easily re-execute any sub-expression interactively, which makes for a more effective interactive coding experience.

The notebook is a good and practical way to document one&#8217;s analytical path. However, I sometimes wonder if there are less linear (graph-oriented?) ways of representing the often branching routes one follows during an analysis session.

# Dissimilarity representation

Some years ago, I attended a talk where [Prof. Robert P.W. Duin][8] gave a fantastic talk about the history and future of pattern recognition.

In this talk, he introduced the idea of dissimilarity representation.

In much of pattern recognition, it was pretty much the norm that you had to reduce your training samples (and later unseen samples) to feature vectors. The core idea of building a classifier, is constructing hyper-surfaces that divide the high-dimensional feature space into classes. An unseen sample can then be positioned in feature space, and its class simply determined by checking on which side of the hypersurface(s) it finds itself.

However, for many types of (heterogenous) data, determining these feature vectors can be prohibitively difficult.

With the dissimilarity representation, one only has to determine a suitable function that can be used to calculate the dissimilarity between any two samples in the population. Especially for heterogenous data, or data such as geometric shapes for example, this is a much more tractable exercise.

More importantly, it&#8217;s often easier to discuss with domain experts about similarity than it is to talk about feature spaces.

Due to the machine learning project mentioned above, I had to work with categorical data that will probably later also prove to be of heterogeneous modality. This was of course the best (THE BEST) excuse to get out the old dissimilarity toolbox (in my case, that&#8217;s [SciPy and friends][9]), and to read a bunch of dissimilarity papers that were still on my list.

Besides the fact that much fun was had by all (me), I am cautiously optimistic, based on first experiments, that this approach might be a good one. I was _especially_ impressed by how much I could put together in a relatively short time with the SciPy ecosystem.

Machine learning peeps in the audience, what is your experience with the dissimilarity representation?

# A mountain at the end

By the end of a week filled with nerdery, it was high time to walk up a mountain(ish), and so I did, in the sun and the wind, up a piece of the Kogelberg in Betty&#8217;s Bay.

At the top, I made you this panoroma of the view:<figure id="attachment_2826" aria-describedby="caption-attachment-2826" style="width: 840px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2017/02/IMG\_20170219\_1434219-panorama.jpg" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title="">

<img data-attachment-id="2826" data-permalink="https://cpbotha.net/2017/02/24/weekly-head-voices-117-dissimilar/img_20170219_1434219-panorama/" data-orig-file="https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama.jpg" data-orig-size="7738,2067" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;STV100-4&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1487514864&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="IMG_20170219_1434219-panorama" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama-300x80.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama-1024x274.jpg" class="size-large wp-image-2826" src="https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama-1024x274.jpg" alt="" width="840" height="225" srcset="https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama-1024x274.jpg 1024w, https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama-300x80.jpg 300w, https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama-768x205.jpg 768w, https://cpbotha.net/wp-content/uploads/2017/02/IMG_20170219_1434219-panorama-1200x321.jpg 1200w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" /></a><figcaption id="caption-attachment-2826" class="wp-caption-text">Click for the 7738 x 2067 full resolution panorama!</figcaption></figure> 

At that point, the wind was doing its best to blow me off the mountain, which served as a visceral reminder of my mortality, and thus also kept the big M (for mindfulness) dial turned up to 11.

I was really only planning to go up and down in brisk hike mode due to a whiny knee, but I could not help turning parts of the up and the largest part of the down into an exhilarating lope.

When I grow up, I&#8217;m going to be a trail runner.

Have fun (nerdy) kids, I hope to see you soon!

 [1]: /2016/01/05/note-taking-strategy-early-2016/
 [2]: https://github.com/bbatsov/prelude
 [3]: http://todoist.com/
 [4]: https://blog.todoist.com/user-stories/how-skinny-laminx-uses-todoist-for-creativity/
 [5]: http://pragmaticemacs.com/emacs/org-mode-basics-vii-a-todo-list-with-schedules-and-deadlines/
 [6]: http://jupyter.org/
 [7]: https://github.com/millejoh/emacs-ipython-notebook
 [8]: http://rduin.nl/
 [9]: https://www.scipy.org