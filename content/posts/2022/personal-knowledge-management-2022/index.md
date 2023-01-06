+++
title = "Personal knowledge management strategy 2022"
date = 2022-02-27T21:50:00+02:00
lastmod = 2022-06-05T15:52:18+02:00
slug = "personal-knowledge-management-2022"
tags = ["note-taking"]
categories = ["tech"]
draft = true
author = "Charl P. Botha"
org = true
+++

I wrote about my note-taking approach for [the first time in 2016](/2016/01/05/note-taking-strategy-early-2016/) (read for
fun), and [then pretty expansively about its evolved version  in 2019](/2019/09/21/note-taking-strategy-2019/).

In spite of the title of that post, already in 2019 it had become more a system
for _personal knowledge management_ than just for note-taking.

It is now again three years later, and the system has continued on its path of
steady evolution.

The purpose of this post is to document the _current_ state of the system.

TODO: talk about this post being self-contained.


## Highest level overview {#highest-level-overview}

The system has to satisfy the following functional requirements:

1.  Fast capture of any information, including free-form notes and media.
2.  Tracking of projects and metadata such as due dates and schedules.
3.  Fast and accurate retrieval of any information relevant to the current
    situation.
4.  Potentially serendipitous surfacing of assets that might be relevant to the
    main search focus, for example through linking or through search.

The system should have the following two characteristics:

1.  There should be a single search interface that can in theory find everything
    that was ever stored in the system. This is to prevent the situation where
    you urgently need some document and can't remember into _which_ notes app you
    stored it so many years ago. (True story)
2.  As far as possible, everything should live on local drives where that's
    possible, and be synchronized with a tool like Dropbox. In this way, the
    system is robust to the whims of a note-taking SaaS. Even Dropbox could be
    replaced, although in my case that would not be painless.

At the highest level, my system, which satisfies the requirements and
characteristics above, consists of the following components:

Emacs with Org-mode and Org-roam
: This is the nexus of the whole thing. It
    tracks projects, tasks and notes, spread out over hundreds of files, all
    linked together.

PDF'd web-pages and articles (JBOP)
: Locally stored PDF versions of
    reference-worthy web-pages and articles can be annotated, linked and shared,
    and they remain usable long after the source website has disappeared.

Academic articles managed with Zotero
: Zotero is one of the best ways to
    manage all of your academic literature and metadata. As if that's not enough,
    it's fully open source.

Mobile device for capturing and access
: In my case that's an iPhone with
    the following apps: Dropbox and Dropbox Paper, [Plain Org](https://plainorg.com/), [Print Friendly &amp;
    PDF bookmarklet](https://www.printfriendly.com/extensions/safari)

Dropbox for synchronization and searching
: This infrastructural component
    is critical. It ensures that all of the files are synced and available on all
    devices that I use, and, quite importantly, it indexes everything so that I
    can interactively search through the contents of hundreds of thousands of
    files. There are some work-arounds and caveats which I will get into further
    down.


## The components in more detail {#the-components-in-more-detail}


### Emacs with Org-mode and Org-roam {#emacs-with-org-mode-and-org-roam}

The heart of my knowledge management system, let's call it \`pkb4000\`, is [Emacs
Org mode](<https://orgmode.org/>). Org mode, or "Your life in plaintext", is a
powerful text-file-based system for managing notes, task lists, projects and
even authoring documents.

Once you get used to the programmable flexibility it offers, you will find it
hard to go back to any conventional system.

On [February 26, 2020, a commenter on the 2019 post asked if I'd taken a look at
org-roam](/2019/09/21/note-taking-strategy-2019/#isso-2654), a question to which my answer at that point was that I had looked but
not really gotten into it yet.

I just checked my notes (an `org-roam` buffer with backlinks, which sort of gives
away the story), and it turns out that a week later on March 3 of 2020 I indeed
got `org-roam` configured and running.

From that point on, it pretty much took over the [core notes database](/2019/09/21/note-taking-strategy-2019/#core-notes-database) function
of my PKM.

Fortunately `org-roam`, and even more so `org-roam v2`, relies as much as possible
on standard Org-mode functionality while adding all of the instantaneous note
searching, creation and linking that has succeeded in drastically upgrading my
Org-mode implementation to a increasingly densely linked, tagged and far more
useful exocortex.


#### Monthly journal files {#monthly-journal-files}

In my main Org mode directory, I have a subdirectory named `journals`, which
contains a directory for each year.

Each of these year directories contains an `.org` file for each month, so we
would have for example `journals/2022/2022-06-Jun.org`.

Each month file follows the structure showed in the following redacted version
of my current journal file:


<pre style="color: #232629; background-color: #f8f8f2;">
<span style="bg0: #fefef8;">#+TITLE:</span><span style="bg0: #fefef8;"> </span><span style="color: #fb6107; bg0: #fefef8; font-size: 140%; font-weight: bold; text-decoration: underline;">2022-06 June month journal
</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">
</span><span style="color: #6b7566; bg0: #e9f0e5;"># HUGO options here so I can export any heading to a blog post</span><span style="bg0: #e9f0e5;">

</span><span style="color: #2376ad; bg0: #e9f0e5; font-size: 130%; font-weight: bold;">* Vitals
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">*</span><span style="color: #2595ab; bg0: #e9f0e5; font-size: 120%; font-weight: bold;">* Systems 2022 edition
</span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">   </span><span style="bg0: #e9f0e5;">Here I keep daily reminders of principles that I find important.

</span><span style="bg0: #e9f0e5;">   </span><span style="bg0: #e9f0e5;">If you're interested, it's written up in a number of posts on my blog, but the
</span><span style="bg0: #e9f0e5;">   </span><span style="bg0: #e9f0e5;">most relevant ones currently are:

</span><span style="bg0: #e9f0e5;">   - </span><span style="bg0: #e9f0e5; text-decoration: underline;"><a href="/2021/01/10/the-2020-to-2021-transition-post/#life-systems-2021">Life Systems 2021</a></span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">   - </span><span style="bg0: #e9f0e5; text-decoration: underline;"><a href="/2022/05/23/weekly-head-voices-242-multiplicity-of-me/">Weekly Head Voices #242: Multiplicity of me</a></span><span style="bg0: #e9f0e5;">

</span><span style="color: #f8f8f2; bg0: #e9f0e5;">*</span><span style="color: #2595ab; bg0: #e9f0e5; font-size: 120%; font-weight: bold;">* Side-projects
</span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">   </span><span style="bg0: #e9f0e5;">A reminder list of my current side-projects.

</span><span style="color: #f8f8f2; bg0: #e9f0e5;">*</span><span style="color: #2595ab; bg0: #e9f0e5; font-size: 120%; font-weight: bold;">* Planning / overview / major done list </span><span style="color: #22a54e; bg0: #e9f0e5; font-size: 120%; font-weight: bold;">[1/1]</span><span style="color: #2595ab; bg0: #e9f0e5; font-size: 120%; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">   - </span><span style="bg0: #e9f0e5; font-weight: bold;">[X]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">A manual checklist of more significant projects that I've completed.

</span><span style="color: #2376ad; bg0: #e9f0e5; font-size: 130%; font-weight: bold;">* Goals
</span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">  </span><span style="bg0: #e9f0e5;">See </span><span style="bg0: #e9f0e5; text-decoration: underline;"><a href="id:dd2bc341-0801-4703-b0dd-ed202b94b2fa">Goals for 2022</a></span><span style="bg0: #e9f0e5;">

</span><span style="color: #2376ad; bg0: #e9f0e5; font-size: 130%; font-weight: bold;">* Tasks
</span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">  </span><span style="bg0: #e9f0e5;">Mostly personal Org-mode </span><span style="bg0: #e9f0e5;">TODO</span><span style="bg0: #e9f0e5;"> items that don't belong in project files.

</span><span style="color: #2376ad; bg0: #e9f0e5; font-size: 130%; font-weight: bold;">* 2022
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">*</span><span style="color: #2595ab; bg0: #e9f0e5; font-size: 120%; font-weight: bold;">* 2022-W22
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">**</span><span style="color: #27a89e; bg0: #e9f0e5; font-size: 110%; font-weight: bold;">* Week planning for 2022-W22 </span><span style="color: #ff3d00; bg0: #e9f0e5; font-size: 110%; font-weight: bold;">[1/3]</span><span style="color: #27a89e; bg0: #e9f0e5; font-size: 110%; font-weight: bold;"> </span><span style="bg0: #e9f0e5;">&lt;2022-05-30 Mon 08:31&gt;</span><span style="color: #27a89e; bg0: #e9f0e5; font-size: 110%; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">    </span><span style="bg0: #e9f0e5;">At the start of the week, I select around three important tasks / goals for the week.

</span><span style="color: #f8f8f2; bg0: #e9f0e5;">**</span><span style="color: #27a89e; bg0: #e9f0e5; font-size: 110%; font-weight: bold;">* 2022-05-30 Monday
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">***</span><span style="color: #29a466; bg0: #e9f0e5; font-weight: bold;">* Day planning </span><span style="bg0: #e9f0e5;">&lt;2022-05-30 Mon 08:31&gt;</span><span style="color: #29a466; bg0: #e9f0e5; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">****</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">* Done list / thoughts / diary
</span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">      </span><span style="bg0: #e9f0e5;">General journal-style writing during the day. What happened, what I
</span><span style="bg0: #e9f0e5;">      </span><span style="bg0: #e9f0e5;">thought, what I think now.

</span><span style="color: #f8f8f2; bg0: #e9f0e5;">****</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">* One Main Thing and Task(s) that will satisfy end-of-day Charl </span><span style="color: #22a54e; bg0: #e9f0e5; font-weight: bold;">[0/0]</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">****</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">* Tasks for today </span><span style="color: #22a54e; bg0: #e9f0e5; font-weight: bold;">[0/0]</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">****</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">* Stretch tasks for today </span><span style="color: #22a54e; bg0: #e9f0e5; font-weight: bold;">[0/0]</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">
</span><span style="color: #f8f8f2; bg0: #e9f0e5;">****</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">* Review </span><span style="color: #ff3d00; bg0: #e9f0e5; font-weight: bold;">[0/9]</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5; text-decoration: underline;"><a href="*Vitals">Month vitals</a></span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">Org tasks, projects and goals -- review, but also groom and triage
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">Week planning
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5; text-decoration: underline;"><a href="id:dd2bc341-0801-4703-b0dd-ed202b94b2fa">Goals for 2022</a></span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">Scheduled for today / calfw
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">Calendar
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5; text-decoration: underline;"><a href="id:D500BC12-4EC8-49DD-861B-7CE4590FFF37">inbox mobile 2022</a></span><span style="bg0: #e9f0e5;">
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">Signal Note to Self
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5; text-decoration: underline;"><a href="elisp:org-roam-node-random">M-x org-roam-node-random</a></span><span style="bg0: #e9f0e5;">

</span><span style="color: #f8f8f2; bg0: #e9f0e5;">****</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">* Habits / important </span><span style="color: #ff3d00; bg0: #e9f0e5; font-weight: bold;">[0/2]</span><span style="color: #519f2a; bg0: #e9f0e5; font-weight: bold;">
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">7.5 hrs sleep last night
</span><span style="bg0: #e9f0e5;">      - </span><span style="bg0: #e9f0e5; font-weight: bold;">[ ]</span><span style="bg0: #e9f0e5;"> </span><span style="bg0: #e9f0e5;">block focus time in calendar
</span></pre>


#### Org-agenda {#org-agenda}


#### Core notes database {#core-notes-database}


## Changes since 2019 {#changes-since-2019}


## Org-mode is now augmented by Org-roam {#org-mode-is-now-augmented-by-org-roam}

On [February 26, 2020, a commenter on the 2019 post asked if I'd taken a look at
org-roam](/2019/09/21/note-taking-strategy-2019/#isso-2654), a question to which my answer at that point was that I had looked but
not really gotten into it yet.

I just checked my notes (an `org-roam` buffer with backlinks, which sort of gives
away the story), and it turns out that a week later on March 3 of 2020 I indeed
got `org-roam` configured and running.

From that point on, it pretty much took over the [core notes database](/2019/09/21/note-taking-strategy-2019/#core-notes-database) function
of my PKM.

Fortunately `org-roam`, and even more so `org-roam v2`, relies as much as possible
on standard Org-mode functionality while adding all of the instantaneous note
searching, creation and linking that has succeeded in drastically upgrading my
Org-mode implementation to a increasingly densely linked, tagged and far more
useful exocortex.

{{< figure src="images/Personal_knowledge_management_strategy_2022/2022-02-26_22-16-07_screenshot.png" >}}

-   notes and subset of that that function as nodes


### Variable-pitch-mode and poet-theme {#variable-pitch-mode-and-poet-theme}

<https://explog.in/notes/poet.html>

python find first element


## The mobile story has converged slightly {#the-mobile-story-has-converged-slightly}


## The role of Dropbox and DOCX {#the-role-of-dropbox-and-docx}


## Appendix {#appendix}