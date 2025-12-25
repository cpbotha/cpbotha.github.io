+++
title = "Daily Head Voices on Thursday 2023-12-28"
date = 2023-12-31T11:52:00+02:00
lastmod = 2023-12-31T12:21:51+02:00
tags = ["lifelog", "org-roam", "embedding", "similarity", "life systems", "openai", "audio books"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

-   Longer run brought my year target back in reach, at the cost of some hip niggle. 4km in, I decided that this was not the time and place for a fasted run and bought me a powerade. I bought another on the way back from the Vergelegen-to-Reservoir Road section of my route. I have no regrets.
-   Before the run, thought about Values vs Vision vs Sinek's Why. This was brought on by a twitter thread (which I did not bookmark argh) by a person who identified the root cause of a previously resolved mental health challenge to be the fact that at that point they had ill-defined personal values, and that addressing that was a large part of the resolution. I think my previously-mentioned ["life systems"](https://cpbotha.net/2021/01/10/the-2020-to-2021-transition-post/#life-systems-2021) are indeed closely related, but it can't do harm to spend some more mental cycles on listing my values, and then maybe to see how exactly these related to my life systems.
-   Before and during the run, half-designed in my head a software tool for narrating books using OpenAI's text-to-speech API.
-   After the run, took care of some errands:
    -   Had car battery replaced
    -   Installed new diaphragm for the Zodiac pool cleaner, the current one has a hole in it and did not work at all
    -   New brush for the pool pole
-   After errands, built and then published the afore-thought-about prototype <https://github.com/cpbotha/audio-my-book> -- warning, it's still super rough, but it works nicely chopping up your book text into semantic chunks and then text-to-speeching each chunk into mp3 (the openai tts API has a 4096 character limit, hence the chunking)
-   In the evening, worked on <https://github.com/cpbotha/org-roam-similarity> fixing bugs, and also showing similarity scores in the `*org-roam*` buffer.
