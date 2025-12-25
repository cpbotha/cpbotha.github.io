+++
title = "Daily Head Voices for week 4 of 2024"
date = 2024-01-28T21:27:00+02:00
lastmod = 2024-01-28T21:27:48+02:00
slug = "daily-head-voices-2024-01-22_28"
tags = ["lifelog", "gou", "gou-1", "gou-2", "gou-3", "mindfulness", "streamlit", "react", "marimo", "til", "running", "tailscale", "cloudflare", "productivity", "betty's bay", "beer", "llm", "macbook pro"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

## Monday 2024-01-22 {#monday-2024-01-22}

-   As GOU#1 and GOU#2 were busy leaving for school, #3 came in to #2 for a hug but #2 was a bit too focused on getting all of her things ready to go in the car. Good Charl, in his only appearance of the day, spontaneously interjected with: "When you're in a hug, for that moment, you put your full attention into that hug. For that moment, nothing else exists but the hug.". I could really see the message hitting home with #2, and she vocalised as much. Monday: BIG SUCCESS!
-   At work, managed to spill black coffee all over meself as I was just doing step 1 of living the one cable dream (read: attaching usb-c cable to my macbook). Clumsy Charl clearly at the wheel...
-   Short but really nice [streamlit](https://streamlit.io/) demo during a work meeting. I knew about streamlit, but I've never actually played with it.
-   Spent the rest of the day fighting trying, without success, to update the webcola d3 adapter to the latest version of d3.
    -   In bed that night, had light-bulb that React was probably a better solution for this visualization in any case...
    -   ... and then realised that few years back I built something similar for work, and had a similar evolution of ideas which ended up with react + webcola.


## Tuesday 2024-01-23 {#tuesday-2024-01-23}

-   At the office nice and early (7:30).
-   Chatted with colleague about the abovementioned React + webcola thing we worked on together, at which point he pointed me at [react-flow](https://reactflow.dev/) and comfyui
    -   react-flow looks like it could work pretty well for this new project. Also: SO SHINY!
-   streamlit app life cycle: script re-runs every time user interacts, see <https://docs.streamlit.io/get-started/fundamentals/summary>
    -   it does have caching mechanisms to make this go faster
    -   marimo, although much newer, approaches this issue with its reactive cell pattern
-   Idea: We should write focused technical memos at work. This is now howto, but rather "things I learned" formulated to teach not just to document.
-   Upgaded phone to iOS 17.3 and MacBook to macOS 14.3. Apparently there's a [zero day vulnerability](https://www.tomsguide.com/news/apple-issues-urgent-security-updates-to-fix-zero-day-flaw-update-your-iphone-and-mac-right-now) in previous versions that can be exploited via malicious websites.


## Wednesday 2024-01-24 {#wednesday-2024-01-24}

-   8km run at just after 7 AM before it really got hot
-   dip in the pool (friend LM says we must but pool is probably not cold enough due to +30℃ temps), then started to work
-   right after dip in pool, partially pulled back muscle. Partial, because two warning spasms, but not complete lock like many previous times. PHEW!
    -   Remember kids: Our spine's vertical operation is a major evolutionary hack job and a mechanical disaster just waiting to happen. My advice: Spend more time horizontally.
    -   This is also the reason why I'm still searching for a long enough reclining chair.
-   Lovely working lunch with friend S at [No Way José](https://www.facebook.com/NoWayJoseSomerset)
-   Some random ideas that popped into my head as I was trying to work:
    -   idea: make github so that people can `pipx install marimo-turbo` to get install with pandas, altair, matplotlib, and so on.
    -   idea: figure out way to publish marimo dashboard to HTTPS url somewhere, for really really cheap
        -   sounds like AWS API gateway + lambdas can do something complicated to host streamlit, which also uses websockets
        -   in the end, probably better to do this on my own VPS
            -   ... or even better, on my own machine behind tailscale funnel! This was straight-forward and seems to work well. See <https://emacs.ch/@cpbotha/111811547009420844> (post is also embedded below)
    -   idea: (which has been active for a bit longer) A reliable pattern to lazy start upstream processes only when the first request comes in, and to stop them when no-one is connected. Client -&gt; nginx -&gt; supervisord -&gt; tornado
        -   systemd can partially do something like this using socket activation: <https://serverfault.com/questions/1121584/start-apache-on-demand-using-systemd-socket-activation>
        -   I would prefer to use supervisord for this
        -   This will remain on the todo list for now, unless one of you knows a trick?
-   ran into dude who built kubernetes thing for Hetzner using Crystal, a programming language of which I remembered that it just had a release, so quickly lost some more time on "crystal vs nim-lang" googling
    -   blog post: <https://vitobotta.com/2023/01/07/kubernetes-on-hetzner-cloud-the-easiest-way/>
    -   the kubernetes thing: <https://github.com/vitobotta/hetzner-k3s>

<iframe src="https://emacs.ch/@cpbotha/111811547009420844/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe><script src="https://emacs.ch/embed.js" async="async"></script>


### TIL: mastodon embeds are not as durable as twitter embeds {#til-mastodon-embeds-are-not-as-durable-as-twitter-embeds}

As I pasted the above embed, I saw to my disappointment that it's just pulling in the mastodon post URL via `iframe`.

With twitter, you get more self-contained HTML which will render even when twitter or just the original tweet don't exist anymore.

This is probably just another reason to figure out how I can get more low-friction microblogging going on my own websites so that the embedding implementations of other microblogging sites become irrelevant.


## Thursday 2024-01-25 {#thursday-2024-01-25}

-   Took a look at [cloudflare tunnels](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/) to expose marimo and other dashboards to the internet
    -   great that I can use my existing domains for this, and I can route between multiple domains to multiple locally running services
    -   some more steps to setup, but it did not take more than about 5 minutes, and gives me even more options than tailscale funnels. OPTIONS MAN!
-   At work, quickly got react-flow... flowing. SHINY!
-   In the evening, found <https://www.macstories.net/stories/generating-markdown-links-to-mail-messages-with-shortcuts-and-applescript/> which is the new Shortcuts based way, based on the old AppleScript way, of getting a `message://` link onto the clipboard.
    -   You [might recall from this blog](/2023/04/11/note-taking-strategy-2023/#email-linking) that `message://` are the most durable and cross-platform way to link to emails from your notes (or anywhere else)


## Friday 2024-01-26 {#friday-2024-01-26}

-   Woke up to cool, overcast weather, a big change from a series of 30℃ + days. Really had to resist going out for a run (normal run day + that amazing coolness), because of Wednesday's partially pulled back muscle not being 100% yet.
-   Worked on mystery visualization project (react-flow)
-   Lovely and energising lunch with previous colleague and friend. Happy that I reached out on Thursday although they have a packed schedule because only in country for limited time. I guess this is quite related to [calling up your friends](/2022/09/25/weekly-head-voices-246-call-up-your-friends/#call-up-your-friends), with a ping of serendipity salt.
-   I was shocked by how well and fast [ollama](https://ollama.ai/) worked on my MacBook. See embedded tweet below.
-   Almost at the end of the afternoon, friend S and I went to some more friends for the first Weiss-off, that is, a Weiss beer tasting contest. It was huge fun blind-tasting 10 different Weiss beers, ranking them, trying to identify them (so much harder than I thought!), and then having them revealed at the end.
    -   Between the experts there (read: us), Stangen Weiss Bier came out on top, followed by Weisbier No5 and Jack Black Atlantic Weiss. The fourth place was shared by Erdinger and CBC Amber Weiss.
    -   My favourite, Stellenbrau Jonkersweiss, is glaringly absent from the top. I'll live, probably consoled by just such a Jonkersweiss. Super happy that Amber Weiss and Atlantic are both present!
    -   There was a trophy (for the taster who could blind-identify the most beers in the Weiss-off), which we have christened the _David Weisselhoff wisseltrofee_.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">With <a href="https://twitter.com/MistralAI?ref_src=twsrc%5Etfw">@MistralAI</a>&#39;s Mistral 7B at Q4_0 on this MacBook M1 Pro 10C / 16C, <a href="https://twitter.com/ollama?ref_src=twsrc%5Etfw">@ollama</a> looks like it&#39;s easily 3 times faster than the new MLX 0.0.11 (with GGUF support).<br><br>It&#39;s subjectively (visually) faster, and the tokens/s measurements confirm this. <a href="https://t.co/9vyluimLKK">pic.twitter.com/9vyluimLKK</a></p>&mdash; @cpbotha@emacs.ch (@cvoxel) <a href="https://twitter.com/cvoxel/status/1750824125419942036?ref_src=twsrc%5Etfw">January 26, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## Saturday 2024-01-27 {#saturday-2024-01-27}

-   Yesterday's Wonderful Weiss-off also had some, thankfully quite minor, effect the next morning, but I went out for a careful weekday distance run, which fortunately went without a hitch. Just very hot thanks.
-   Went to Buco and then to [Apple Tool and Gas](https://appletoolandgas.com/) to find the rest of the screws I needed to repair the shower door. Friendly gentleman at Apple even sawed some of my screws to size! Shower door back in operation.
-   Updated my "old" M1 MBA to macOS 14.3 and then reset to transfer to GOU#1's iCloud. Say what you want about Apple, but that part of their stuff works _really_ well.
-   Left for Betty's Bay at about 16:00 with GOUs #1 and #2. The rest of the family already there.


## Sunday 2024-01-28 {#sunday-2024-01-28}

-   Woke up in Betty's Bay after a longer than normal night of sleep, but Garmin body battery was still not completely happy.
-   In spite of having run yesterday and still feeling a bit tired (see body battery above), I had the best run of the month so far in Betty's. Go figure.
-   Spent some time with Canva -- what a great resource for doing nice designs, even flow charts -- but not sure where I could use this.
-   Background thought through the past weeks, and mentioned on Tuesday: I would really like to do (and promite) more TIL-style writing at work and at home. See [Simon Willison's amazing TIL collection](https://til.simonwillison.net/) for inspiration.
-   Ran into <https://github.com/outlines-dev/outlines> a Python library that can guarantee structured text generation from many LLMs, e.g. 100% valid JSON according to a specified schema. What makes it different from similar libraries? "Unlike other libraries, regex-guided generation in Outlines is almost as fast as non-guided generation."
-   I already had [AutoGen](https://github.com/microsoft/autogen) on my list for experimenting with multi-agent LLM applications, but now it has been joined by [crewAI](https://github.com/joaomdmoura/crewAI) which I have also just ran into (thanks reddit!) and which seems to have significant support online.
