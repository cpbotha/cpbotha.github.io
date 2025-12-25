---
title: Days 3 and 4 of IEEE Visualization
author: cpbotha
type: post
date: 2007-10-31T22:26:08+00:00
url: /2007/10/31/days-3-and-4-of-ieee-visualization/
categories:
  - tech

---
On **Day 3 (Tuesday)** the actual Visualization conference kicked off with awards and a keynote by Rick Stevens of the Argonne National Laboratory and the University of Chicago. Prof. Jarke van Wijk won the Visualization Technical Achievement award and gave the coolest acceptance speech I have ever had the privilege of experiencing. Spending quite some time on the origins of his (to our Anglophile colleagues) extraordinary name and succeeding in making all of the almost 800 attendees laugh several times, he managed to bring all of this back to the flow visualization research for which he earned this award, and then put it all in context by explaining what his daughter thought of his world-famous inventions: “That’s the stupidest thing I’ve ever heard”. :)

This was followed by Rick Stevens’ keynote “Visualization Challenges at the intersection of petascale computing and biology”. It was definitely impressive, but was somewhat lacking in focus. I guess that’s one of the problems of giving a keynote: one would like to give a broad overview that does one’s field justice, but that goes at the cost of zooming into the core and explaining some of the issues with more depth. One of the take-home messages was that the challenge of linking genotypes to phenotypes involves a Whole Lot Of Data(TM).

Some of the highlights of the Tuesday were the presentations by Stefan Bruckner (the guy must be brilliant) on real-time halos for emphasising depth in real-time illustrative visualisation, and on [Semantic Layers for Illustrative Volume Rendering][1] Peter Rautek. The latter uses an interesting combination of fuzzy logic to enable the very high-level specification of visual features in volume renderings.

My **day 4 (Wednesday)** started with an early morning (7:30) secret meeting concerning the upcoming [VCBM conference][2], followed by paper sessions. Papers that stood out on Wednesday include Peter Kohlmann’s [_LiveSync: Deformed Viewing Spheres for Knowledge-Based Navigation_][3]_,_ a straight-forward yet effective way of picking a good viewing direction in a direct volume rendering given a clicked-on position in an MPR view. [Carlos Scheidegger’s][4] (from the group of Claudio Silvia) paper on querying and creating visualizations by analogy with VisTrails was really cool. These guys have managed to elevate boxes and lines visual programming (data-flow) to a higher level, by thinking about the math that one can do with functional networks and their metadata. This also won the Vis best paper award!

In the afternoon I joined the panel on “All Visualization Software is the same, right?”. This was more of a discussion on research software vs. commercial software. It was quite interesting, but did lack a bit of focus. Again, Karel Zuiderveld shone with his “10 reasons why I hate open source software”. Bottom-line of this discussion: there’s a huge difference between academic and commercial software (doh), and don’t let any of those open source fanboys tell you different. :)

After the poster session, where I had a few interesting chats concerning [Peter Krekel’s][5] shoulder replacement validation poster, I went to the Kitware BOF. More demos of the cool new InfoVis functionality in VTK by Brian Wylie and Jeff Baumes, also the ominously named ThreatView, built on top of this. More impressive VisTrails demos were shown as well. At the very end, I got to give a presentation on DeVIDE, thus making the session run out by almost half an hour. Thanks for not killing me guys!

Afterwards, Florian Link of MeVis showed me some of the to-be-released functionality in MeVisLab. My opinion of this comes down to “WOW”. Much better Python, Javascript and MeVisLab interpreter user interface niceties.

Stick around for my next posting on the last day of Vis, and some final extremely profound and earth-shattering thoughts. I’m swamped at the moment, so it might take a few days. :)

 [1]: http://www.cg.tuwien.ac.at/research/publications/2007/Rautek-2007-SLI/ "TU Wien page on Semantic Layers for Illustrative Volume Rendering"
 [2]: http://vcbm.org/ "VCBM conference site"
 [3]: http://www.cg.tuwien.ac.at/research/publications/2007/kohlmann-2007-livesync/ "Link to deformed viewing spheres"
 [4]: http://www.sci.utah.edu/~cscheid/ "Homepage of Carlos, with link to Vis 2007 paper and presentation"
 [5]: http://krekel.tk/ "Peter Krekel's website"
