---
title: Two PowerPoint 2007 tricks that could save your life
author: cpbotha
type: post
date: 2009-10-31T13:27:13+00:00
url: /2009/10/31/two-powerpoint-2007-tricks-that-could-save-your-life/
categories:
  - tech
  - work
tags:
  - avi
  - black box
  - embedded movie
  - powerpoint
  - slow transition

---
On Wednesday evening I was putting the finishing touches on probably the most important presentation I’ve given in the past few years.  As I was testing everything on my trusty little netbook just before bed-time, two scary problems reared their ugly heads: 1) An embedded MS-MPEG4 encoded AVI simply showed a black box when played and, perhaps even more disheartening, 2) the last and most important slide took between 4 and 6 seconds to appear.
{{< figure src="/wp-content/uploads/2009/10/ms.jpg" link="/wp-content/uploads/2009/10/ms.jpg" caption="The people that brought you PowerPoint.">}} 

Some of you might remember that I posted about a [strange PowerPoint 2003 bug and its work-around][1] back in 2005.  In short, hyperlinking to an MS-MPEG4 encoded AVI would result in a completely unnecessary warning dialogue.  Renaming the AVI to MPG made this problem go away.

Guess how I worked around the **movie clip black box problem in PowerPoint 2007**?  Yes, children, **changing the file extension from AVI to MPG and re-embedding** the movie-clip resulted in a perfectly-playing embedded AVI.  You can thank the clever guys and girls at Microsoft for keeping life interesting with these pleasant little surprises.

Problem #2 took slightly longer to solve, but Uncle Google soon had me on the [right track][2].  The last slide in my presentation, the one that took 4 to 6 seconds to appear, was quite image-heavy.  It turns out that PowerPoint saves embedded images in a relatively inefficient non-compressed form.  This does, contrary to what we expect from MS, make sense, as one would like to retain all image information.  However, when one is doing a slide-show, the processing that has to take place scaling and displaying all images takes an inordinate amount of time.  Having an upwards of 4 second delay before the next slide appears is simply not acceptable.

The solution is **saving a copy of your presentation, but with image compression activated**.  Do “Save As” and on the bottom-left of the dialogue that appears, select the “Tools” menu button, then “Compress Pictures”, then “Options” and finally “Screen (150ppi)”.  Now “Ok” twice, then finally select a new filename and click on “Save”.  In my case, the presentation file was reduced from 10MB to 2MB, and the load time for that crucial last slide from 4 seconds (minimum) to slightly less than 1.

That concludes the second installment in my exciting life as a PowerPoint flunky!

 [1]: http://cpbotha.net/2005/03/06/hyperlinked-avis-and-powerpoint-2003/ "Link to previous PowerPoint 2003 bug"
 [2]: http://www.tech-recipes.com/rx/1423/powerpoint_compress_and_optimize_presentations_ppt_to_decrease_size/ "tech-recipes site with more information concerning compression of ppts"
