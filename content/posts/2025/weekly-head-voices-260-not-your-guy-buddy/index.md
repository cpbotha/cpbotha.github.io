---
title: "Weekly Head Voices #260: I'm not your guy, buddy"
slug: weekly-head-voices-260-not-your-guy-buddy
author: "Charl P. Botha"
date: 2025-04-22T09:00:00+02:00
draft: false
tags:
  - Guy Kawasaki
  - Steve Jobs
  - docker
  - emacs
  - gou-3
  - hetzner
  - netcup
  - orgmode
  - pomodoro
  - productivity
  - obsidian
categories: ["weekly head voices"]
type: "post"
# EXCEPTION: keep ogimage as jpg, og.html will convert this to webp when resizing
# DO NOT use .webp here, then you'll git the golang / hugo webp decoding bug
# for the rest of the post, use webp, but keep a same-named jpg/png ok?
ogimage: "20250322_palmiet_hike.jpg"
---

This wildly-non-weekly 260th edition of the Weekly Head Voices covers the period of my life, exceptionally patchily, from Wednesday, March 12 to Monday, April 21, 2025.

{{< figure src="20250322_palmiet_hike.webp" link="20250322_palmiet_hike.webp" >}}

The photo above is from a little family hike down to the Palmiet river mouth, next to Betty's Bay. [GOU #3](/about/weekly-head-voices-abbreviations/) (now 9), seemed to enjoy the first bit, but then suddenly did not, which usually leads to quite a bit of complaining.  It was really great to see her perk up again when I returned with the car to pick them up more quickly than she expected. (All of that running exercise has a purpose you know.)

A week or two later, GOU #3 recovered by being an absolute trooper through the whole of the slightly more substantial and absolutely brilliant 6.5km family hike all around the little [Sea Farm private reserve's peninsula](https://maps.app.goo.gl/rreQJ7uyT1SFSKfJ7). I tell myself, and others, that this is partially due to involving her in the progress of the event, by showing her at regular intervals on Google Maps exactly where we found ourselves, and how we were making progress around the peninsula.

Maybe one day, we will both have better answers to the question:

> Why am I in such a rush to get through life when I want so much to enjoy it?
>
> -- Jan Chozen Bays

(With that in mind, you might also find [WHV #237](/2022/02/03/weekly-head-voices-237-dont-step-over-the-thing/#i-don-t-want-to-step-over-the-thing) interesting!)

## The whole cpbotha.net-hive migrates again

Slightly more than five years after [the previous migration of the whole so-called cpbotha.net-hive from WebFaction (RIP) to Hetzner](/2020/02/23/weekly-head-voices-189-all-systems-green/#the-whole-cpbothanet-hive-has-been-migrated-to-a-small-hetzner-server), I got an offer I could not refuse, [on Bluesky (!)](https://bsky.app/profile/mackuba.eu/post/3ll7dgrep7c25), for a [netcup VPS](https://www.netcup.com/en/server/vps/vps-1000-g11-12m-iv) with double the number of vCPUs, double the RAM and 5x the storage, all for about 25% cheaper every month.

On the weekend of March 28 I managed to port the six websites in question across (3 easy static ones, including this blog, and 3 slightly more tricky wordpress ones).

I am most grateful that as part of this porting effort I have now finally been able to dockerize the binaries I built years ago of the super obscure [WlzIIPSrv fork of the C++ IIP image slice server](https://github.com/ma-tech/WlzIIPSrv) and will in future be able to migrate much more easily if I ever need to do so again. WlzIIPSrv is the software that serves the pannable and zoomable histology slices when you browse a [visible-orbit.org (wordpress site also hosted on this new server) stack like this one](https://visible-orbit.org/slices/dk2904l-registered/).

Although this migration is a significant and positive technical event for me, most of you will probably not even notice that this site responds a tad (or three) more snappily than it used to.

Whatever the case may be, I am celebrating that this is officially the first blog post coming to you from this shiny new server!

## Productivity (d)evolution

### Just get it done with Kanban

Someone once called using Trello for task management "the time management connoisseur equivalent of lying in the gutter with a cheap bottle of wine in a brown paper bag".

(So, by the way, that someone was me! See [the previous admission on this blog, in WHV #86 from 2014](/2014/11/27/weekly-head-voices-86-beardy/#note-taking-and-todo-system-chaos-nerd-warning), original source of my statement is [this comment on Noeska's blog](https://noeskasmit.com/comparison-of-task-managers-rtm-astrid-wunderlist-todoist/#comment-71).)

I mention this now, because my current system, the one which has to act as replacement for [my almighty Emacs Org-mode](/2025/03/11/weekly-head-voices-259-backbone/#a-bientôt-monsieur-org), is a monthly Kanban board with columns for "todo", "today / next", "doing" and "done", and task cards that I can move, quite satisfyingly, from column to column, which is essentially a less full-featured but fully local version of my old Trello-based system.

While the 2014-org-mode-me mind really cannot comprehend this, the current system, based on the plugins [obsidian-kanban](https://github.com/mgmeyers/obsidian-kanban) and [obsidian-tasks](https://publish.obsidian.md/tasks/Introduction), is working just fine for the moment.

### pomodori made from 100% xbar

You might recall from the previous WHV that I was still [using Emacs as an over-powered pomodoro timer](/2025/03/11/weekly-head-voices-259-backbone/#productivity-hack-of-the-year).

Well, even that started itching a bit too much, and now I've just re-implemented the whole thing, along with the productivity boosting auto-DnD setting, by [modifying an existing self-contained macOS xbar script](https://charlbotha.com/til/xbar-pomodoro-timer-with-DnD-for-macOS) which you can use if you too wish to work harder.

### Loggin' time

Together with the pomodoro timing, I was also using org-mode to maintain detailed time logs for work, using the built-in org-clock functionality.

Because of above-mentioned itch, I now have a semi-usable replacement which I put together as an [Obsidian Dataview custom view](https://blacksmithgu.github.io/obsidian-dataview/api/code-reference/#dvviewpath-input), in other words, a bunch of javascript that piggy-backs on the dataview parser and groups bullet items with start and end timestamps under their parent tasks and container headings, as projects, in order to spit out daily and monthly timelog breakdowns.

I've only been testing this since the start of April. Although it's giving me all of the data that I need, the UX is just barely over the threshold of usable-by-me.

Perhaps in the coming weeks I'll find some time to write more about this tool to hear what others think.

## The Bozo explosion

My great friend Dave told me about this phenomenon, of which I then had to go find the source.

It turns out the originator is none other than Steve Jobs, with the idea being injected into the internet hive-mind by [Guy Kawasaki](https://en.wikipedia.org/wiki/Guy_Kawasaki), a Guy who worked for Jobs at Apple (I see what I'm doing here) from 1983 until about 1986.

There's a short but great post by Guy Kawasaki titled [What I Learned From Steve Jobs](https://guykawasaki.com/what-i-learned-from-steve-jobs/) which is definitely worth a few minutes of your time.

Here I want to focus on point 9, namely "A players hire A+ players".

I've personally seen this a number of times with the smartest and best leaders I've ever had the privilege of interacting with. They, the A players, actively seek and appoint colleagues who are smarter or better than they are, the A+ players. They absolutely revel in the opportunity of being challenged by the best people they can find. This turns into a positive feedback loop, with more and more similarly capable people seeking out their peers.

The opposite of this happens when you start with B players. B players easily feel threatened by more capable folks, and so they tend to recruit C players so that they can maintain the pecking order. Those C players will accordingly recruit D players and so on. This process of course leads to what Jobs coined as "the Bozo explosion", which sounds frighteningly similar to what is currently happening in some parts of the world today.

Next time when you're evaluating a new opportunity, do make some time to ensure that the folks involved have the A player mentality.

## Conclusion

For future me, here's a list of other notable events from the period under review:

- Two 50th celebrations.
- Various very special eating and drinking occasions with treasured friends, some from afar, and family.
- Three family hikes.
- 1 Sting concert (with my life partner) which exceeded all my expectations.
- My first running race (Spookhill challenge).
- Visits with Parisian friends and family to the breathtaking [Zeitz Museum of Contemporary Art Africa (MOCAA)](https://en.wikipedia.org/wiki/Zeitz_Museum_of_Contemporary_Art_Africa) and the Two Oceans aquarium.
- Far too many marshmallow eggs.

... and with that, I would like to leave you with this:

> The trick is to learn how to want the things you already have.
>
> -- William B. Irvine

{{< figure src="zeitz_mocaa_ocular.webp" link="zeitz_mocaa_ocular.webp" caption="Top floor of Zeitz MOCAA, looking at the Ocular restaurant" >}}

<!-- "not your guy, buddy" from the South Park episode "Canada on strike" https://www.imdb.com/title/tt1211261/characters/nm0005295/ -->