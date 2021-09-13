---
title: 'Weekly Head Voices #130-2: Direct experience dopamine.'
author: cpbotha
type: post
date: 2018-02-04T18:43:17+00:00
url: /2018/02/04/weekly-head-voices-130-2-direct-experience-dopamine/
categories:
  - weekly head voices
tags:
  - direct experience network
  - dopamine
  - mindfulness
  - narrative network
  - python
  - type hinting

---
{{< figure src="/wp-content/uploads/2018/02/IMG_3174-1-1024x576.jpg" link="/wp-content/uploads/2018/02/IMG_3174-1.jpg" caption="Photogenic and non-camera-shy dragonfly I met in Paarl over the weekend.">}} 

As I went through my notes to extract material for this week’s post, I noticed a small discrepancy between the task description for the previous post and the published version: #129 in my notes versus [#130 in the published post][1]!

It’s too late now to rename #130, so in this reality I’m just going to have to deal with the fact that WHV #129 will never exist. I have decided to name this edition #130-2 so that eventually (well, in about a week), we will be back to uninflated post numbers. Nobody likes inflation. Except perhaps tyres. And balloons.

# Your brain at work part 2: Dopamine and more mindfulness

Ironically, the incorrectly numbered post #130 dealt with [the many ways in which our brains fail us every day][2]. (Now that I’ve finally gotten around to installing the [WP Anchor Header plugin][3], we can link directly down to any heading in any post, as demonstrated in the previous sentence.)

At least some clouds do seem to have a silver lining.

Your Brain at Work, [the book I mentioned last week][2], has turned out to be a veritable treasure trove of practical human neuroscience, and I still have about 30% to go. My attempt at meteorological humour above was inspired by part of the book’s treatment of the important role of dopamine in your daily life.

For optimal results, one is supposed to remain mildly optimistic about expected future rewards, but not too much, which will result in a sharp dopamine drop when those rewards don’t crystallise, and a greater increase when they do. For optimal results, one should try to remain in a perpetual state of mildly optimistic expectations, but also in a state of being continually pleasantly surprised when those expectations are slightly exceeded.

More generally, the book deals really well with the intricacies of trying to keep one’s various neural subsystems happy and in balance. Too much stress, and the [limbic system][4] starts taking over (you want to run away, more or less), blocking your ability to think and make new connections, which in this modern life could very well be your only ticket out of Stress Town.

To my pleasant surprise (argh, I’ll stop), [mindfulness][5] made its appearance at about 40% into the book, shortly after I had published last week’s WHV.  In my favourite mindfulness book, [Mindfulness: A Practical Guide to Peace in a Frantic World][6] by [Mark Williams][7] and Danny Penman, two of the major brain states are called _doing,_ the planning and execution mode we find ourselves in most of the time, also in the middle of the night when we’re worrying about things we can do nothing about at that point, and _being_, the mode of pure, unjudgemental observation the activation and cultivation of which is practised in mindfulness.

In David Rock’s book, these two states are described as being actual brain networks, and they have different but complementary names: The _narrative network_ corresponds to the doing mode, and the _direct experience network_ corresponds to the being mode.

The narrative network processes all incoming sensory information through various filters, moulding it to fit into one’s existing mental model of the world. David Rock describes it in the book and in [this HuffPost piece][8] as follows:

> When you experience the world using this narrative network, you take in information from the outside world, process it through a filter of what everything means, and add your interpretations. Sitting on the dock with your narrative circuit active, a cool breeze isn’t a cool breeze, it’s a sign than summer will be over soon, which starts you thinking about where to go skiing, and whether your ski suit needs a dry clean.

This is certainly useful most of the time, but it can get tiring and increase stress when you least need it.

The much-more attractively named _direct experience network_ is active when you feel all of your senses opening up to the outside world to give you that full HD IMAX(tm) surround sound VR experience. No judging, no mental modelling, just sensory bliss and inner calm. [Rock sez][8]:

> When this direct experience network is activated, you are not thinking intently about the past or future, other people, or yourself, or considering much at all. Rather, you are experiencing information coming into your senses in real time. Sitting on the jetty, your attention is on the warmth of the sun on your skin, the cool breeze in your hair, and the cold beer in your hand.

Again, these two systems are on opposite sides of a neurophysiological see-saw. When you are worrying and planning, no zen for you! On the other hand, when you’re feeling the breeze flowing and and through each individual hair on your arms and the sun rays seemingly feeding energy directly into your cells, your stress is soon forgotten.

Fortunately, mindfulness gives us practical tools to distinguish more easily when we’re on which path, and, more importantly, to switch mental modes at will.

I hope you don’t mind me concluding this piece by recursively quoting David Rock quoting John Teasdale, one of the three academic founders of [Mindfulness Based Cognitive Therapy (MBCT)][9]:

> Mindfulness is a habit, it’s something the more one does, the more likely one is to be in that mode with less and less effort… it’s a skill that can be learned. It’s accessing something we already have. Mindfulness isn’t difficult. What’s difficult is to remember to be mindful.

(If the book has any more interesting surprises, I’ll be sure to report on them in future WHV editions.)

# Miscellany at the end of week 5 of 2018

  * The rather dire water situation has not changed much, except that due to more citizens putting their backs into the water saving efforts, day zero (when municipal water is to be cut off) has been postponed by 4 days to April 16. We are now officially limited to 50 litres per person per day, for everything. Practically, this means even more buckets of grey water are being carried around in my house every day in order to be re-used.
  * I ran 95km in January, which is nicely on target for my modest 2018 goal. Although January was a long month, and Winter Is Coming (And Then We Run Much Less Often), I am mildly optimistic that I might be able to keep it up.
  * [Python type hinting][10] is brilliant. I have started using it much more often, but I only recently discovered how to specify a type which can have a value or None, an often-occurring pattern:


<pre class="src src-python"><span style="color: #0000ff;">from</span> typing <span style="color: #0000ff;">import</span> Optional, Tuple
<span style="color: #0000ff;">def</span> <span style="color: #006699;">get_preview_filename</span><span style="color: #707183;">(</span>attachment: Attachment<span style="color: #707183;">)</span> -&gt; Tuple<span style="color: #707183;">[</span>Optional<span style="color: #7388d6;">[</span><span style="color: #006fe0;">str</span><span style="color: #7388d6;">]</span>, Optional<span style="color: #7388d6;">[</span><span style="color: #006fe0;">str</span><span style="color: #7388d6;">]</span><span style="color: #707183;">]</span>:
    <span style="color: #0000ff;">pass</span>
</pre>

  * On Wednesday, January 31, GOU #3 had her first real (play) school day, that is, without any of us present at least for a while. We’re taking it as gradually as possible, but it must be pretty intense when you’re that young (but old enough to talk, more or less) and all of a sudden you notice that you’re all alone with all those other little human beings, none of which are the family members you’re usually surrounded with.

# The End

Thank you dear reader for coming to visit me over here, I really do enjoy it when you do!

I hope to see you next again next week, same time, same place.

 

 [1]: /2018/01/28/weekly-head-voices-130-ttaggg/
 [2]: /2018/01/28/weekly-head-voices-130-ttaggg/#your-brain-not-at-work
 [3]: https://wordpress.org/plugins/wp-anchor-header/
 [4]: http://www.brainbasics.org/home/limbic-system
 [5]: /tag/mindfulness/
 [6]: https://books.google.co.za/books?id=rxddAgAAQBAJ&source=gbs_similarbooks
 [7]: https://www.neuroscience.ox.ac.uk/research-directory/mark-williams
 [8]: https://www.huffingtonpost.com/david-rock/the-neuroscience-of-mindf_b_2908665.html
 [9]: https://en.wikipedia.org/wiki/Mindfulness-based_cognitive_therapy
 [10]: https://www.python.org/dev/peps/pep-0484/
