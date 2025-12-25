+++
title = "Daily Head Voices on Tuesday 2024-01-02: Culture of doubt"
date = 2024-01-03T21:50:00+02:00
lastmod = 2024-01-03T21:50:50+02:00
slug = "daily-head-voices-on-tuesday-2024-01-02"
tags = ["lifelog", "betty's bay", "backyard philosophy", "richard feynman", "telegram", "zapier"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

> Religion is a culture of faith; science is a culture of doubt. -- Richard Feynman

-   Went to the beach at just after 11:00. Brilliant weather which for Betty's is quite special, so the place was absolutely packed.
-   Finally created `org-capture-template` to do the Daily Head Voices post setup more easily and more consistently, see below for the relevant element.
-   Thought a bit about writing and then self-hosting the tool that scans the cpbotha.net RSS feed and then performs actions, e.g. sending to Telegram, when new posts appear
    -   Initial thought was Go, because small and self-contained (like my discord scihub bot and my eureka-alert RSS feed generator), but Python means much higher development velocity. Because it's a script that will run every few minutes and then stop, RAM is less of an issue, and the official docker images <https://hub.docker.com/_/python/> mean I don't yet have to upgrade the ancient Ubuntu 18.04 on my VPS.
    -   Next thought was rather to spend this time writing. Zapier free tier is working fine for now, will get back to self-hosting it later.
-   `org-roam-node-find` calls `org-roam-node-read` calls `org-roam-node-read--completions` calls `org-roam-node-list`, which always reads the full list of nodes from the sqlite database. Whyyyyy? When I do a semantic search using `org-roam-similarity`, I already have the small list of IDs. I only want to offer the user this small list, I **don't** want to read the full list every time, and then remove everything except the list I already have -- so much wasted effort. I'm really hoping d12frosted's [vulpea](https://github.com/d12frosted/vulpea) has something better...


## org-capture-template to create DHV after prompting for date {#org-capture-template-to-create-dhv-after-prompting-for-date}

```emacs-lisp
;; select region around your private day notes, then C-c c l
("l" "Lifelog" entry (file+olp+datetree lifelog-org)
 "* TODO Daily Head Voices on %<%A> %<%Y-%m-%d>
:PROPERTIES:
:EXPORT_FILE_NAME: index.md
:EXPORT_HUGO_BUNDLE: lifelog-%<%Y%m%d>
:EXPORT_HUGO_TAGS: lifelog
:END:
:LOGBOOK:
- Created \"TODO\" %U
:END:

%i
"
 ;; - with org 9.6.6 :time-prompt is only honoured when target is
 ;;   "file+olp+datetree"
 ;; - I would have preferred just target "file" for this, but need
 ;;   time-prompt as I often only create post after the day
 :empty-lines 1 :jump-to-captured 't :time-prompt 't :tree-type 'month)
```
