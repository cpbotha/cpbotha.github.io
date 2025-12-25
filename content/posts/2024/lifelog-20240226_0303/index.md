+++
title = "Daily Head Voices for week 9 of 2024"
date = 2024-03-10T18:50:00+02:00
lastmod = 2024-03-10T18:52:34+02:00
slug = "daily-head-voices-2024-week-9"
tags = ["lifelog", "gou-3", "emacs", "org-roam", "mindfulness", "marimo", "orgmode"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

## Monday 2024-02-26 {#monday-2024-02-26}

-   started the morning (and the work week!) with stupid indecision: Had all my work gear in the car, but chose to drive back home after dropping of GOU#3 for a logistical task which one of my other clan members would gladly have taken care of.
    -   Indecision irrelevant against the backdrop: We had such a good time in the car first being on time (GOU#3 loves that), then listening to Skrillex together, then talking, and then performing our morning ritual of verbally attesting our super-infinite love for each other as I drop her off at school.
-   During highly technical demo outside of my domains, used perplexity in real-time to lookup various details as the demo was going on, and thus could focus on the really interesting questions for the presenter.
-   Between meetings, struggled a bit to focus in the focusy bits, but managed to do quite a bit of work eventually (with focusapp and some deep house) and even got milestones done.


## Tuesday 2024-02-27 {#tuesday-2024-02-27}

-   Super frustrated during the morning rush, because could not find running shoes at the critical moment when we had to leave for school
    -   Reverted to backup shoes (old ones, with too many kilometres on them)
    -   Good run in L&amp;Z, but it took so  long to disconnect from my shoe moment, in spite of really putting my mind to it. Succeeded a little bit at the end, shocked at the mental cost of something this trivial.
    -   BTW, it was almost a textbook "not inside it's on top!" situation.


## Wednesday 2024-02-28 {#wednesday-2024-02-28}

-   For once some [Waking Up](https://www.wakingup.com/) in the morning! (I once had a streak of more than a year. Currently happy if I do just one!)
-   Started the day in pensive mood (before and after the meditation) thinking about what I would like from the future
    -   Naturally I wanted to write a note, so then I tapped out a topic in the daily list so that I could use `org-roam-node-find-similar` to surface similar notes from the past. I did find the correct historic note which I would not have otherwise, but then I got sucked into emacs config...
        -   why has my `org-roam-node-find-*` never done live preview like other consult commands? -- solved by installing <https://github.com/jgru/consult-org-roam/tree/main> and then tooting about it: <https://emacs.ch/@cpbotha/112008312753264000>
            -   During the day I was surprised at the amount of traction that toot got. It seems there are more people who missed this. It seems it can sometimes really help to share the minutiae.
        -   realised that `org-roam-node-find-similar` did not sort the similar nodes by similarity, so fixed that: <https://github.com/cpbotha/org-roam-similarity/commit/d940c12e70468adfbc1e41ef997c5f797540ebf7>
    -   After extricating myself back out of Emacs config yak shaving, I did spend some quality time writing up my thoughts, helping to clarify them.
        -   I don't know the answer yet, but the direction I'm moving in feels good.
-   Lunch with inner circle friend and mentor DMW at No Way Jose was great thank you!


## Thursday 2024-02-29 {#thursday-2024-02-29}

-   Run at shortly after 7. Legs did not really want to cooperate.
-   Got distracted by meetings day at work, so almost no writing in the daily. Now, <span class="timestamp-wrapper"><span class="timestamp">[2024-03-10 Sun 18:35]</span></span>, I'm really sorry.


## Friday 2024-03-01 {#friday-2024-03-01}

-   Pool repair at my house. They are able to pump out all water, repair floor of pool, then pump all water back all in a few hours.
-   I have two ideas for the weekend
    -   Build and publish a QRCode contact card generator using marimo and wasm
    -   build a telegram bot to manipulate my org-mode database, e.g. adding tasks, searching for existing tasks and notes.
        -   I don't like this second idea, but it keeps on coming back to me.


## Saturday 2024-03-02 {#saturday-2024-03-02}

-   12km run with tired legs, so tired that I decided to stop the fast and get Powerade for the last 5km, which felt like it really helped.
-   Super happy that I could get the promised marimo-wasm-qrcode generator online: <https://vxlabs.com/2024/03/02/contact-qrcode-generator-with-marimo-and-wasm/>


## Sunday 2024-03-03 {#sunday-2024-03-03}

-   After sunday morning coffee and scrolling, dug into marimo to see if there's some way to create the WASM locally. There does not seem to be.
-   Scanned through <https://core.telegram.org/bots> to see (again...) what might be possible.
-   Actually, now I'm thinking about the idea of making a telegram bot that sends me random tasks from my org-mode every day. I already have a proof of concept in Python that uses emacsclient to expose org-roam nodes via API (see <https://github.com/cpbotha/org-roam-canvas> ) so I would probably follow a similar path, probably with something like org-ql. Does anyone know if something like this exists somewhere?
    -   Apple's Journal app, that suggests a new journalling possibility now and then, made me think that this could help.
-   In iTerm2, press the Option-Cmd keys together to make a rectangular selection.
-   Sublime lunch at Millhouse Kitchen with inner circle family
-   Back home, tried to get MobileOrg going again; looked promising, but then after successful sync ran into [this bug with empty outlines in the app when synced via iCloud](https://github.com/MobileOrg/mobileorg/issues/292). 😥
-   Configured perplexity via gptel in my Emacs; I am especially interested in using perplexity's [`sonar-online` internet-capable models](https://www.perplexity.ai/hub/blog/introducing-pplx-online-llms).
