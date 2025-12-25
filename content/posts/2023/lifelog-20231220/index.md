+++
title = "Daily Head Voices on Wednesday 2023-12-20"
date = 2023-12-22T12:13:00+02:00
lastmod = 2023-12-22T12:14:48+02:00
tags = ["lifelog", "apple", "apple tv 4", "llm", "ai", "applescript", "orgmode"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

-   Morning run on the gravel road along the Serpentine river in Wilderness, probably one of my favourite routes ever.
-   On a new wifi network with Apple TV, but forgot remote at home. Moved TV and Apple TV closer to AP to plug in via ethernet, which allowed the iPhone remote to connect, BUT Apple decided to be infuriating again: _If your Apple TV has an Ethernet port, make sure your Apple TV isn't connected to an Ethernet cable. If you're using an Ethernet cable, you won't see the option to connect to Wi-Fi._ see <https://support.apple.com/en-za/102346> -- this is of course a great big catch 22 for us at the moment.
    -   They do plenty of things right, but man, they make some really stupid mistakes.
    -   On a related note, it seems that before iOS 17, the Remote app on the iPhone was able to control the Apple TV even when they weren't on the same WiFi network, see <https://www.reddit.com/r/appletv/comments/16mo99d/apple_tv_remote_app_requires_a_wifi_connection_as/>
-   On the other hand: Based on the following two recent publications, it really looks like Apple is cooking up something really interesting with large language models (LLMs):
    -   Apple announces ProTIP: Progressive Tool Retrieval Improves Planning -- so they are working on much improved ways of hooking up LLMs to tools, perhaps even on their devices? via <https://twitter.com/_akhaliq/status/1736982938942677421>
    -   New Arxiv paper by Apple titled "LLM in a flash: Efficient Large Language Model Inference with Limited Memory" -- from the abstract: "These methods collectively enable running models up to twice the size of the available DRAM, with a 4-5x and 20-25x increase in inference speed compared to naive loading approaches in CPU and GPU, respectively. Our integration of sparsity awareness, context-adaptive loading, and a hardware-oriented design paves the way for effective inference of LLMs on devices with limited memory." via <https://www.threads.net/@sung.kim.mw/post/C1Dwx7Iypg4/>
-   Spent some time digging into AppleScript (again) and how I could make a better orgmode to apple notes workflow
    -   Previous attempt is here: <https://vxlabs.com/2018/10/29/importing-orgmode-notes-into-apple-notes/#bonus-round-convert-orgmode-buffer-to-apple-note-using-applescript>
    -   The new flow should merge more cleverly with an existing folder in Notes, instead of re-importing the whole database each time
