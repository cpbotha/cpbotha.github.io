+++
title = "Daily Head Voices on Thursday 2024-01-04"
date = 2024-01-07T17:33:00+02:00
lastmod = 2024-01-07T17:33:44+02:00
slug = "daily-head-voices-2024-01-04"
tags = ["lifelog"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

-   Pushed through to completion finally, [the 2024 edition of the traditional yearly year transition blog post](/2024/01/04/the-2023-to-2024-transition-post/)!
-   Added an [about page for the Daily Head Voices / lifelog](/about/daily-head-voices/) (an edition of which you are reading now)
    -   How can I add this as a standard but discrete part of every DHV? Should I?
-   Noticed that I can upgrade my super humble Hetzner VPS + its extra storage for visible-orbit.org to a newer Hetzner VPS with 4 x ARM64 cores instead of 2 x AMD64 (according to benchmarks in total a small step up), double the RAM and enough storage for current needs for only a few cents extra per month. Benefit: Microscopically faster websites. Cost: Some time to modernize the configuration from ubuntu 18.04 to 22.04, perhaps even dockerizing everything in the process.
    -   In the process of sniffing around, noticed that someone was bruteforcing the `xmlrpc.php` on medvis.org (thanks htop and puny VPS CPUs!), and so added a [fail2ban](https://github.com/fail2ban/fail2ban) configuration to iptables them into oblivion.
    -   After that, took a deeper dive into the porting and modernization work. Biggest blocker looks like the super obscure wlziipsrv code I would have to rebuild for arm64 for the [visible-orbit high-res slice viewer](https://visible-orbit.org/the-collection/high-res-section-stacks/).
