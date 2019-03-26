---
title: Second day of IEEE Visualization 2007
author: cpbotha
type: post
date: 2007-10-29T23:21:54+00:00
url: /2007/10/29/second-day-of-ieee-visualization-2007/
categories:
  - tech

---
What an imaginative title!

Today (actually yesterday, but I&#8217;m acting as if I wrote this up yesterday, when yesterday was still today, okay?) I had the typical IEEE Vis problem of Too Many Very Cool Things All at the Same Time(TM). I chose to start with the Illustrative Visualization tutorial. One of the highlights of this was [Stefan Bruckner&#8217;s][1] presentation of his [Style Transfer Functions][2]. Stefan is a brilliant presenter, and this deceptively simple idea makes it possible to render, in real-time, illustrative volume renderings with all kinds of cool lighting possibilities. See the figure below:

<a href="http://www.cg.tuwien.ac.at/research/publications/2007/bruckner-2007-STF/image-orig.jpg" title="" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption=""><img src="http://www.cg.tuwien.ac.at/research/publications/2007/bruckner-2007-STF/image-300.jpg" title="Thumbnail of STF volume rendering" alt="Thumbnail of STF volume rendering" height="300" width="247" /></a>

In the Advanced Visual Medicine tutorial, Felix Ritter gave an impressive demo of the [MeVisLab software][3]. I have been playing with this software, what impressed me during the tutorial was the speed and ease with one could build custom-designed user interfaces around one&#8217;s network&#8217;s in order to deploy one&#8217;s work for clinical use. This is definitely something I should think of doing for [DeVIDE][4] as well. As a side note, this presentation has also led me to come to the conclusion that **I should open source DeVIDE**, after adding some critical functionality such as the planned hybrid scheduling (part deterministic, part demand-driven streaming, all goodness!) and pyparallel integration. More on this later&#8230; You can download the MeVisLab example networks Felix used during the tutorial from [http://mevislab.de/vis2007][5].

Bernhard Preim gave a very interesting talk on the use of visualisation in the radiological workflow. The take-home message here is that 3D is hardly ever used, mostly for extremely deviant pathologies. This is a good lesson: don&#8217;t make the mistake of thinking that 3D vis is by definition better for everything, it really isn&#8217;t. In clinical practice MIP, oblique MPR and slab rendering (especially for detecting lung nodules) are still king.

Karel Zuiderveld, medical visualisation pioneer and currently technology strategist (read: head scientist) at [Vital Images][6], the premier provider of 3D volume rendering workstations for the radiological practice, gave an insightful view from his perspective. The take home message here was that radiologists need to get through an exam as quickly as possible (they get paid per exam); the more you can do to help them with this, the better. Think step-by-step assistance with an exam protocol, canned transfer functions and viewing settings, and so forth. There&#8217;s a large schism between what&#8217;s produced in cutting edge medvis research and what&#8217;s accepted in radiological practice. Karel emphasised the 3D-is-not-necessarily-better point by stating that we should start thinking in terms of &#8220;advanced visualisation&#8221; and not necessarily 3D.

So, it&#8217;s looking more and more certain that we will be organizing a new workshop in Delft next year called Visual Computing for Biomedicine. The Eurographics powers-that-be have discussed this issue during Vis, and it&#8217;s looking quite positive. I&#8217;ve put up a website just in case: [http://vcbm.org/][7] Put that in your aggregator to keep up to date. Submission deadline will be around June 22, the conference will be in the first week of October. It&#8217;s going to rock, I guarantee it.

See you tomorrow!

 [1]: http://www.cg.tuwien.ac.at/staff/StefanBruckner.html "Stefan Bruckner's homepage"
 [2]: http://www.cg.tuwien.ac.at/research/publications/2007/bruckner-2007-STF/ "Style Transfer Functions home page."
 [3]: http://mevislab.de/ "mevislab homepage"
 [4]: http://visualisation.tudelft.nl/Projects/DeVIDE "DeVIDE website."
 [5]: http://mevislab.de/vis2007 "link to mevislab vis2007 materials"
 [6]: http://vitalimages.com/ "Vital Images website"
 [7]: http://vcbm.org/ "VCBM website"
