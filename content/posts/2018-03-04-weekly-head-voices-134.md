---
title: 'Weekly Head Voices #134: SCARF.'
author: cpbotha
type: post
date: 2018-03-04T20:47:46+00:00
url: /2018/03/04/weekly-head-voices-134/
categories:
  - weekly head voices
tags:
  - arduino
  - backyard psychology
  - c++
  - david rock
  - gou
  - running
  - saucony

---
{{< figure src="/wp-content/uploads/2018/03/untitled_by_sylvia_20180304-1024x492.png" link="/wp-content/uploads/2018/03/untitled_by_sylvia_20180304.png" caption="Untitled artwork by GOU#2 (age 7), who is also known as My Most Favourite Middle Child.">}} 

I somehow forgot to take photos this past week. At the very last moment, GOU#2 delivered, as if commissioned, the piece shown above.

The WHV visual element lives to fight another day!

The rest of this post is divided into three parts: One for the programming nerds, one for the running nerds and one for the arm-chair psychologists. Feel free to pick and choose!

# C++ quo vadis?

This week, we spent more than a day chasing an elusive memory-related access violation (big words for “crash”) in the software we recently released.

In the end, the bug was only really reproducible on Windows 7 (not on Linux, not on macOS, and only with great difficulty and infinite patience on Windows 10). It turned out to be hidden deep in a well-tested, industry-backed open source C++ library.

This and the specific nature of this bug again demonstrated to me that C++, although I love it dearly, simply has too many well-disguised flaws (let’s call them foot-guns) which will eventually lead to even the most experienced and sharp programmer making mistakes.

In spite of the recent language renaissance (C++11, 14, 17 with 20 imminent) and a slew of improvements, it’s still too easy to write unsafe code.

With contenders like rust ([rustlang][1] AJ, rustlang!) which enable programmers to write programmes which have C++-level performance but are by default safe, could C++’s days be counted?

# Run

It was time to retire my trusty pair of Asics Cumulus 18 shoes.

They had clocked just over 900km, which is perhaps a little too much. By the end, I could feel the bones in my big toe’s main joint (apparently also known as the big-toe’s MTP or metatarsophalangeal joint) crunching down with each strike.

Normally not prone to these types of visits, I had no choice but to pop out to the [Run Specialist Store][2] in Edward street on Thursday to get a new pair of activity-proof foot covers.

They let me run on a treadmill (whoohooo running!) with a high-speed video camera. In the footage, we could see that indeed my conversion to forefoot running had been successful (which was good to hear, because it had cost me about 100km of pain), but that I tended to land on the outsides of my forefeet.

The minimal shoes I had had in mind were not (yet) to be.

Instead the run doctor prescribed a pair of [Saucony Kinvara 8s][3], which make my old Asics look like previous generation gardening shoes. I’ve since taken these out on two runs. They are super light, and super springy (everun FTW?), but I have to say that I have my doubts about the durability of the outsole. I’ll report back.

In February, I’m pretty happy that I managed to squeeze in just over 110km of running, which is not too shabby (by my standards, as always!) for the short month.

# SCARF

Yes, winter is coming, but this, although also quite useful, is not that type of SCARF.

I am still reading [David Rock’s book Your Brain at Work][4], and SCARF is his mnemonic for Status, Certainty, Autonomy, Relatedness and Fairness.

These are five social needs, the threat or confirmation of which can have profound effects on humans.

If you feel that you are being unfairly treated, for example, this triggers a low-level threat response which fundamentally complicates dealing rationally with a situation.

Conversely, if for example an interaction grants you more certainty or even better autonomy, you are magically able to contribute significantly more cognitive capacity and creativity to that interaction.

Both the fundamental threat and reward responses go for all five of these qualities. Once you know what to look for, it’s easy to go through some of your memories and to see where one or more of the SCARF needs played a role.

Although one (hopefully) mostly intuitively integrates this in one’s daily dealings, I think it’s super useful being able to enumerate the SCARF social needs like this. It helps when managing oneself in any situation (especially when your prefrontal cortex is exhausted, which is just about always), and it certainly helps when you might find yourself in position where you are able to contribute to another human’s well-being.

# The end

Have a great week friends, I hope to see you again soon!

P.S. if there are any arduino uno -> hardware serial -> xbee experts in the audience, I would like to have a word. ([sparkfun shield][5]. with software serial can talk to xbee. with hardware serial, and sparkfun switch in the right position, xbee won’t respond. [uno is a robotdyn clone][6].)

 [1]: https://www.rust-lang.org/en-US/
 [2]: https://www.runspecialiststore.com/
 [3]: https://www.solereview.com/saucony-kinvara-8-review/
 [4]: https://your-brain-at-work.com/
 [5]: https://www.sparkfun.com/products/12847
 [6]: https://medium.com/@phurl/robotdyn-uno-vs-arduino-genuino-uno-a9ac3b17a96f
