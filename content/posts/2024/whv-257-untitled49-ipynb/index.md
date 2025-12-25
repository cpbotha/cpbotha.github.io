---
title: "Weekly Head Voices #257: Untitled49.ipynb"
slug: weekly-head-voices-257-untitled49-ipynb
author: "Charl P. Botha"
date: 2024-12-08T17:57:35+02:00
draft: false
tags: 
  - advent of code
  - emacs
  - haskell
  - hugo
  - orgmode
  - webp
  - stellenbosch
  - haskell
categories: ["weekly head voices"]
type: "post"
# EXCEPTION: keep ogimage as jpg, og.html will convert this to webp when resizing
# DO NOT use .webp here, then you'll git the golang / hugo webp decoding bug
# for the rest of the post, use webp, but keep a same-named jpg/png ok?
ogimage: "stellenbosch_reserve_view_from_table.jpg"
---

This, the 257th edition of the WHV, covers the period of time from Monday November 25 to Sunday December 8, 2024.  

{{<figure caption="The view right from our lunch table at Stellenbosch Reserve, Haskell Vineyard" src="stellenbosch_reserve_view_from_table.webp" link="stellenbosch_reserve_view_from_table.webp" >}}

Haskell vineyard has made previous appearances on this blog in [WHV #99 in 2015](/2015/08/23/weekly-head-voices-99-no-lands/), in [WHV #181 in 2019](/2019/10/17/weekly-head-voices-181-the-slow-ones/) and perhaps in other posts. I strongly suspect that some of the good friends mentioned there were the same good friends we were so fortunate to spend this Sunday lunch with!

## Why I'm definitely not taking part in Advent of Code 2024

I tried to [explain The Advent of Code in WHV #211](/2020/12/12/weekly-head-voices-211-table-mountain-run-ish/#advent-of-code-2020), back in December of 2020 when I took part for the first time.

An extract from that explanation pertinent to this discussion is:

> To my non-programmer friends: Solving puzzles is like concentrated cat nip to programmers. In the case of AoC, you get unadulterated puzzle solving, and none of the other complications of writing production software.

The dark side of that property is that as the puzzles get more difficult and take up increasing amounts of time, the cat nip enjoyer can get locked in and have great difficulty even noticing that they are spending hours every day writing computer programmes when at first other people are working and later, down here, they are outside enjoying their summer vacation.

In 2020, I think it was on day 21 that I noticed after more than four hours on that day's puzzle that it was probably time to put down the keyboard.

Since then I have been carefully enjoying the first few days of each year's AoC, taking care to walk away when the cat nip becomes too strong.

This year I had resolved not to take part at all, as there are a number of important work projects and personal obligations to take care of.

However, my resolve broke on the first day when I thought "What could be the harm in just taking a little peek?". That little peek led to a little solution, and then another, and then another day, and so on.

Anyways, as you can see from my [#AdventOfCode tagged posts on Bluesky](https://bsky.app/hashtag/AdventOfCode?author=charlbotha.com), I am not officially taking part, I'm just submitting solutions every day.

On a more serious note: I am happy not to miss out on the AoC loads of fun, especially the banter and comparisons and learning on various chat groups, but I am really trying to keep a critical eye on the daily time expense. If it gets out of hand, I will walk away from the programmer cat nip.

P.S. Today was particularly fun, precisely because I managed to squeeze the puzzle in between more important activities. The little rush when I submitted part 2's solution minutes before we had to leave for lunch was exquisite.

<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:oy5vmr2vnff6yxs65hwgk5xq/app.bsky.feed.post/3lcsengeop22r" data-bluesky-cid="bafyreic3sip7ko7ice6gssjd5e57i7l7mbzkghwzp6dy24bee3m2texiza"><p lang="en">Today I was planning on extra vigorously NOT taking part in AoC because it&#x27;s Sunday: planning a long run followed by lunch with some of our best friends.

Plans all happened, but in between I completed &quot;Resonant Collinearity&quot; - Day 8 - Advent of Code 2024 #AdventOfCode adventofcode.com/2024/day/8<br><br><a href="https://bsky.app/profile/did:plc:oy5vmr2vnff6yxs65hwgk5xq/post/3lcsengeop22r?ref_src=embed">[image or embed]</a></p>&mdash; Charl P. Botha | code, data-*, Emacs, running, humans (<a href="https://bsky.app/profile/did:plc:oy5vmr2vnff6yxs65hwgk5xq?ref_src=embed">@charlbotha.com</a>) <a href="https://bsky.app/profile/did:plc:oy5vmr2vnff6yxs65hwgk5xq/post/3lcsengeop22r?ref_src=embed">December 8, 2024 at 3:59 PM</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>

## WebP FTW

Back in 2020, friend [Stéfan](https://mentat.za.net/) and I [hacked and slashed together a Hugo shortcode to render srcset images](/2020/05/02/drop-in-replacement-for-hugo-figure-shortcode-with-responsive-img-srcset/).

In short, this adds multiple resolutions of each image in such a way that users download only what makes sense on their displays, often leading to faster page loading.

Fast forward 4 years as I try out [WebP](https://en.wikipedia.org/wiki/WebP) format images on this website (always for faster loading!) and run into a disappointingly long-standing bug in the Go standard library...

Another long story short, our [figure shortcode can now work around this bug](https://gist.github.com/cpbotha/deb310eed14308fe26f7b7d0fabeb34d?permalink_comment_id=5299293) by displaying webp, but using png/jpg behind the scenes for all conversions, meaning most images should load faster for you.

The photo at the top of this post should have the WebP format, and thanks to srcset it should download lower resolution versions if you are on a smaller display.

## Why I'm starting to write these more regularly in Hugo vs Orgmode

This is just a quick note to me, and perhaps others who occupy this same nanoscopic technical niche.

For the past few years, [since May of 2020](/2020/05/03/weekly-head-voices-193-covid-19-part-3/#fantastic-blogging-tools-and-where-to-find-them), I've been writing most of the WHV posts, and posts for my other blogs, in Emacs Orgmode, exporting them with the wonderful ox-hugo tool.

It made a great deal of sense to me (and it still does!) that my WHV entries were just entries in my monthly orgmode file.

However, sometimes when I go back to update a post from a few years back, some evolution in my orgmode configuration over the years complicates the orgmode to Hugo markdown process, and I'm relegated to debugging the issue before I can get down to the actual update.

A year or two back, to lessen the impact of this problem, I started creating standalone org files for the WHVs. Whilst this certainly reduces the error surface, it's not as robust as editing the markdown directly, which I'm doing right now.

Thanks for coming to my TED talk.

## On waiting

> There's no such thing as waiting -- only unexpected extra time to practice being present. -- [Jan Chozen Bays](https://en.wikipedia.org/wiki/Jan_Chozen_Bays)

P.S. In American English, practice is used both as verb and as noun, unlike British English which uses practice as a noun, and practise as the verb. Dr Bays is American, so I'm keeping the spelling.
