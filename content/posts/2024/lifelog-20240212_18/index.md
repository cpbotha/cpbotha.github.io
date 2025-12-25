+++
title = "Daily Head Voices for week 7 of 2024: Rest For Success"
date = 2024-02-18T17:42:00+02:00
lastmod = 2024-02-18T21:08:24+02:00
slug = "daily-head-voices-week-7-2024"
tags = ["lifelog", "emacs", "running", "gou-1", "gou-3", "productivity", "marimo", "observable"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

> Most people in high-stress, decision-making industries are always operating at this kind of simmering six, as opposed to the undulation between just deep relaxation and being at a 10. Being at a 10 is millions of times better than being at a 6. It’s just in a different universe. -- Josh Waitzkin (see Sunday below)


## Monday 2024-02-12 {#monday-2024-02-12}

-   I really enjoyed this [Rolling Stone article about Nine Inch Nails' Head Like a Hole](https://www.rollingstone.com/music/music-features/nine-inch-nails-head-like-a-hole-anthem-900750/)
    -   Yes, that's also a subtle jab at those of you who read last week's title and did not get the reference. :P
-   Extreme almost asymptotic anger moment at Outlook PWA: Spent time crafting a detailed meeting description. Unrelated meeting notification came in, meeting edit dialog disappears, all of those beautiful words gone. Forever.
-   Accidentally upgraded Emacs to 29.2 (`brew upgrade` if you must now, and there it went building emacs along with installing all the other smaller dependencies, the ones I actually had in mind)
-   Added ad-hoc similar node search for [org-roam-similarity](https://github.com/cpbotha/org-roam-similarity?tab=readme-ov-file#key-bind-the-ad-hoc-similarity-search) (that links to the new function's documentation)
    -   This means you can also select any text, or just use the whole current buffer as your input, and then get a completing read list of similar nodes to open
-   The area of my forehead around the scar feels like it has substantial nerve drop-out. I can't feel much there, and I also can't actuate much. The reconstructive surgeon warned before the time that this might be the case. Thanks again cancer. I'm crossing my fingers that there's still some recovery that needs to happen and this is not my forehead's final form.
-   bitbar is now xbar. It looks like xbar can eat RAM <https://github.com/matryer/xbar/issues/725>
    -   I looked this up, because during [my previous macOS phase](/2017/09/05/weekly-head-voices-125/#new-laptop) I contributed code to bitbar to support Lua plugins. That work is now gone. Oh well.
-   What a craptastically unproductive day. I had all of the time, and in that time I utterly failed at my selected task. I did some other interesting and possibly valuable stuff, but the majority of the time was wasted.
    -   Old lesson on this blog: [some days gonna be crap](/2020/05/20/weekly-head-voices-195-pragmatic/#pragmatic-thinking-and-learning)
    -   However, responded to this by reviving my old FocusApp licence (see pro-tip #2 in [WHV #126](/2018/01/07/weekly-head-voices-126-fleur-de-lis/)) and installed on my machine


## Tuesday 2024-02-13 {#tuesday-2024-02-13}

-   First day back at the office. Lots of conversations due to the giant scar criss-crossing over half my forehead.
-   Implemented the new (but very very old) "avoid all social media during work hours except a little bit on your phone during real breaks" rule.
-   Using terminal Emacs for some remote work, because reasons
    -   Bothersome delay when pressing escape to get out of insert mode into normal mode. IT WAS TMUX. <https://unix.stackexchange.com/a/25638/32868>
    -   Noticed how much I rely on the cursor shape to know in what mode (insert, normal, emacs) I am. Fortunately found <https://github.com/7696122/evil-terminal-cursor-changer> and it's a ... game changer.
-   Today was much fun at the office. Also much higher productivity due to above-mentioned no-social-media-goofing-off-rule.


## Wednesday 2024-02-14 {#wednesday-2024-02-14}

-   Happy Valentine's day everyone!
-   Utterly crazy this morning because load-shedding, but due to GOU#3 being so very on time we left at 7:05 and could avoid most of that chaos.
-   6.5km short run just to get back into it, after 1.5 weeks out thanks to surgery and recovery. Garmin not happy with my fitness, but man it felt good.
-   Went to doctor's rooms to have stitches removed. Kind and professional nurse left the stitches in the middle, because skin there still needed some time to relax into the new situation. Feels really good to have the others out. Will go back on Friday for the rest.
-   Pro-tip: it was a bit of a change management challenge, but I've converted my household to the new shopping list support in Apple Reminders. If you're an Apple family, this woks much better than a WhatsApp group named "Shopping". True story.
    -   Thanks to said app, remembered to get flowers.
-   FocusApp really did its work today.
-   I'm a tiny little bit bummed that no-one picked up on the Head like a Hole reference from last week's Daily Head Voices. Or maybe someone did, but they just have not contacted me about it.
    -   Hopefully this week's title does better.
-   SUCH A GOOD DAY today thank you!


## Thursday 2024-02-15 {#thursday-2024-02-15}

-   Pretty busy day with meetings (Thursday is secondary meeting day at work after all), good conversations with colleagues, and an internal product playbook workshop.


## Friday 2024-02-16 {#friday-2024-02-16}

-   Sublime run in Land &amp; Zeezicht (school district) right after dropping off GOU#3, which also helped to avoid most of the traffic back home, again utterly crazy due to the 6 - 8:30 AM load-shedding slot disabling some critical (for us) traffic lights.
-   Best afternoon ever: Father and daughter picnic with GOU#1 (school event, so many other fathers and daughters) at Zorgvliet Wine Estate
-   In the evening, got my work inbox unread email count to just under 4000. Thank you for coming to my TED talk.
-   Spent a bit more time reading about the new and open source [Observable Framework](https://observablehq.com/framework/)
    -   I've always liked the ObservableJS notebooks, but this new development which supports working locally and self-hosting is really exciting!
    -   marimo is very nice for experimentation, but big advantage of OF is that it builds a static site as output. marimo needs Python to be running on the server.
    -   Again that idea: How automatically could I push a completely new OF built dashboard to a newly allocated CloudFlare pages site?
    -   Tried it out on Sunday evening (IN THE FUTURE): Was really quick to get the intro dashboard going in my case with `pnpm`, but a big challenge at this moment is the developer experience: There is very little coding assistance of any kind as you work on the javascript code blocks in the markdown pages. Hopefully they will be able to improve this with a vscode extension and/or a web-based editing experience, like marimo.
-   Tried out Thunderbird 115.7 on the macbook.
    -   Much better than the TB 115 experience I had just after its release on Windows, where its currently selected mail logic handled it very badly when I archived a mail.
    -   I am trying out TB, because I miss the today, yesterday, last week date grouping.


## Saturday 2024-02-17 {#saturday-2024-02-17}

-   Woke up with low body battery (Garmin). Somewhat surprised, because only two beers last night. Perhaps the stress of the arguments, and probably still the alcohol because I'm old now.
-   Wrote some Mojo to see if I could create a Pandas DataFrame and write to disc as Parquet.
    -   I love parquet.
    -   Although Mojo is still missing some data structures, it was not too involved to use the imported numpy and pandas libraries to do this job.
-   Smoked snoek braai (so good! 🤤) at friend LM's place with more friends.


## Sunday 2024-02-18 {#sunday-2024-02-18}

-   Super enjoyable 13km run. Not too hot, just a little bit of wind, and enough energy to finish strong.
-   George Mack makes the statement: "There’s no such thing as working too hard. There’s just being under rested."
    -   This might indeed be a controversial statement, but  I really like that his advice is to focus on the quality and purity of one's rest (a very mindful idea), leading to much more energy for intensity 10 work.
    -   See [his tweet](https://twitter.com/george__mack/status/1759122352036577546) (also embedded below, but please do click on "show more") for a bunch of interesting examples.
-   Figured out that it's pretty easy to setup "Smart Mailboxes" on Apple Mail for today, yesterday, last week and so on.
-   Truly sublime lunch with family at [Stables on Vergelegen wine estate](https://vergelegen.co.za/restaurants/stables-at-vergelegen/).

<blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Semi-controversial opinion: There’s no such thing as working too hard. There’s just being under rested.<br><br>1. Winston Churchill used to work 16 hours per day in his old age during the war — but he also worked in bed every day until 11am. He had a nap after lunch, and a 2 hour nap… <a href="https://t.co/kyiAuTEwjA">pic.twitter.com/kyiAuTEwjA</a></p>&mdash; George Mack (@george__mack) <a href="https://twitter.com/george__mack/status/1759122352036577546?ref_src=twsrc%5Etfw">February 18, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
