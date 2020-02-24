---
title: "Note-taking strategy 2019."
slug: "note-taking-strategy-2019"
date: 2019-09-21T16:19:00+02:00
tags:
  - dropbox
  - emacs
  - evernote
  - lab journal
  - note-taking
  - orgmode
  - personal knowledge management
  - pkb4000
categories:
  - tech
type: "post"
---

At the start of 2016, I published an [overview of my note-taking strategy
then](/2016/01/05/note-taking-strategy-early-2016/).

In the intervening three and a half years, my note-taking has further evolved
to adapt to my changing environment, and the underlying "system" has co-evolved
to support this.

Although note-taking is at the core of the system, a more accurate description
of its current purpose would be [*personal knowledge
management*](https://en.wikipedia.org/wiki/Personal_knowledge_management).

What you'll also find in this post, is the culmination of many years of lessons
learned trying to ["keep a lab
journal"](/2011/02/19/on-the-importance-of-taking-notes-weekly-head-voices-38/#three).

## Highest level overview of note-taking system.

My approach consists of four main components:

At the core of everything is [**1. Emacs Org mode**](https://orgmode.org/).

As you might know, Org mode is infinitely flexible. This is where all of my
projects and tasks are tracked. This is also where I keep my daily personal and
work journals.

I describe the specific directory structure and orgfile setup in the sections
below.

I continually and actively search for and find interesting **2. Web-pages and
Articles**, both academic and less so, which I convert to PDF and store in a
year-stamped directory inside of my
[JBOP](https://cpbotha.net/2019/03/21/weekly-head-voices-165-get-in-my-pocket/#replacing-pocket-with-just-a-bunch-of-pdfs-jbop).

**3. Academic articles** that I plan to refer to in my own writings graduate into my
Zotero bibliographic database, which is synced together with everything else.

On **4. Mobile** (phone and watch, oh my!), I use the Dropbox app for capturing
and for limited access to my notes database via a small subset of markdown
files, PDFs and exported HTML, and I use the new WatchOS 6 voice notes if I'm
not able to use my phone.

### Other noteworthy characteristics.

Everything mentioned above lives on local drives, synced with Dropbox and also
automatically and continuously backed-up to a removable disk at my office.

The Org mode part of the system has been in use since 2014. I have also
imported a few years of Simplenote text notes into Org mode, so its memory
stretches a bit further back still.

The longer the system lasts, the more valuable it gets.

It has now happened more than once that I could help someone with the same
advice I helped someone else with 4 years ago, simply because the real-time
text search found the relevant snippet of code or attachment in my Org mode
database.

Even if I were ever to change tools, the current single source of truth is a
collection of plaintext org files and PDF files which can easily be further
processed and imported into some new system.

## The components in slightly more detail.

In the following sections, I explain each of the four components in more detail
than in the overview above.

### Emacs Org mode.

The heart of my knowledge management system, let's call it `pkb4000`, is [Emacs
Org mode](https://orgmode.org/). Org mode, or "Your life in plaintext", is a
powerful text-file-based system for managing notes, task lists, projects and
even authoring documents.

Once you get used to the programmable flexibility it offers, you will find it
hard to go back to any conventional system.

#### Monthly journal files.

In my main Org mode directory, I have a subdirectory named `journals`, which
contains a directory for each year.

Each of these year directories contains an `.org` file for each month, so we would have for example
 `journals/2019/2019-09-Sep.org`.

Each month file follows the structure showed in the following redacted version
of my current journal file:

<!-- I used M-x htmlize-region-save-screenshot to get this HTML representation of a real org file onto the clipboard. -->
<pre style="color: #DCDCCC; background-color: #3F3F3F;">
<span style="color: #b3b3b3;">#+TITLE:</span> <span style="color: #8CD0D3; background-color: #3F3F3F; font-weight: bold;">2019-09 September month journal
</span>
<span style="color: #DFAF8F; background-color: #3F3F3F;">* Vitals</span>
<span style="color: #3F3F3F;">*</span><span style="color: #BFEBBF; background-color: #3F3F3F;">* Focus items</span>
Topics and reminders I would like to spend a few minutes on during every
morning review: High value time, always be compounding, always be in a focus
block, etc.
<span style="color: #3F3F3F;">*</span><span style="color: #BFEBBF; background-color: #3F3F3F;">* Tired list</span>
A general list of valuable activities for when I have some time, but brain too
tired to come up with anything.
<span style="color: #3F3F3F;">*</span><span style="color: #BFEBBF; background-color: #3F3F3F;">* Planning / overview / major done list</span>
Check lists with books, courses, etc.
<span style="color: #DFAF8F; background-color: #3F3F3F;">* Projects</span>
A list of current major projects, with links to each project's dedicated org
file.
<span style="color: #DFAF8F; background-color: #3F3F3F;">* Tasks</span>
A list of Org mode tasks that are not associated with specific projects. This
list is reviewed at the start of every month, as I have to manually copy across
those tasks that are still relevant and important.
<span style="color: #DFAF8F; background-color: #3F3F3F;">* 2019</span>
<span style="color: #3F3F3F;">*</span><span style="color: #BFEBBF; background-color: #3F3F3F;">* 2019-09 September</span>
<span style="color: #3F3F3F;">**</span><span style="color: #7CB8BB; background-color: #3F3F3F;">* 2019-09-19 Thursday (example day)</span>
<span style="color: #3F3F3F;">***</span><span style="color: #D0BF8F; background-color: #3F3F3F;">* Day planning </span><span style="color: #8CD0D3; text-decoration: underline;">[2019-09-19 Thu 09:17]</span>
<span style="color: #3F3F3F;">****</span><span style="color: #93E0E3; background-color: #3F3F3F;">* Done list / thoughts / diary</span>
<span style="color: #3F3F3F;">****</span><span style="color: #93E0E3; background-color: #3F3F3F;">* Tasks for today </span><span style="color: #CC9393; font-weight: bold;">[/]</span>
<span style="color: #3F3F3F;">****</span><span style="color: #93E0E3; background-color: #3F3F3F;">* Tasks that will satisfy end-of-the-day Charl </span><span style="color: #CC9393; font-weight: bold;">[/]</span>
<span style="color: #3F3F3F;">****</span><span style="color: #93E0E3; background-color: #3F3F3F;">* Focus blocks</span>
<span style="color: #3F3F3F;">****</span><span style="color: #93E0E3; background-color: #3F3F3F;">* Sleep</span>
<span style="color: #3F3F3F;">****</span><span style="color: #93E0E3; background-color: #3F3F3F;">* Review </span><span style="color: #CC9393; font-weight: bold;">[3/8]</span>
      - <span style="color: #FFFFEF; background-color: #5F5F5F;">[X]</span> <span style="color: #D0BF8F; text-decoration: underline;"><a href="*Vitals">Month vitals</a></span>
      - <span style="color: #FFFFEF; background-color: #5F5F5F;">[X]</span> Calendar
      - <span style="color: #FFFFEF; background-color: #5F5F5F;">[ ]</span> Org tasks
      - <span style="color: #FFFFEF; background-color: #5F5F5F;">[ ]</span> <span style="color: #D0BF8F; text-decoration: underline;"><a href="file:~/Dropbox/notes/mobile/inbox/">dropbox mobile inbox</a></span>
      - ...

<span style="color: #3F3F3F;">****</span><span style="color: #93E0E3; background-color: #3F3F3F;">* Habits / important </span><span style="color: #CC9393; font-weight: bold;">[7/12]</span>
      - <span style="color: #FFFFEF; background-color: #5F5F5F;">[X]</span> 7.5 hrs sleep last night
      - <span style="color: #FFFFEF; background-color: #5F5F5F;">[ ]</span> are you satisfied with number of pomodori? = 0 (v R)
      - <span style="color: #FFFFEF; background-color: #5F5F5F;">[X]</span> did you write stuff down?
      - ...
<span style="color: #3F3F3F;">***</span><span style="color: #D0BF8F; background-color: #3F3F3F;">* is dropbox better than evernote for mobile capturing? </span><span style="color: #8CD0D3; text-decoration: underline;">&lt;2019-09-19 Thu 22:16&gt;</span>

     in ios, with any page in safari, I can do "save to dropbox" and get a PDF
     version of the page for the <span style="color: #b3b3b3;">=notes/mobile/inbox=</span>.
</pre>

As you can see from the example above, the monthly journal file is the main
index to my current high-level goals and focus items, my currently running work
and personal projects, miscellaneous tasks, and my detailed daily journalling
and habit tracking.

##### Daily review.

When I start the day, I instantiate a new org-capture "day planning" template
by pressing `C-c c p`.

This creates the `Day planning` subsection with all of its subsections and
checklists. As you will see, this guides me through the morning review, which
in turn has me check each of those additional sources of incoming information
and tasks.

New bits of information are filed into their correct place, whilst the task
review shows me a list of tasks, extracted from the month file and the list of
current project files, so that I can decide which ones should be taken on.

I list tasks which should preferably be taken care of today under `Tasks for
today`, whilst any really high-value high-satisfaction tasks go under `Tasks
that will satisfy end-of-the-day Charl`.

##### During the day.

During the rest of the day, I'll write short diary-like notes under `Done list
/ thoughts / diary` and log pomodori (focus blocks) under, you guessed it,
`Focus blocks`, either using the `org-pomodoro` package, or plain Org mode
clocking in and out functions.

I use additional custom org-capture templates, via keyboard shortcuts, to
create more extensive timestamped journal entries (see the `is dropbox better
...` example) and to create new timestamped and logged Org mode `TODO` entries.

##### Kill your darlings (during the monthly review).

I've mentioned this before, but it's just an important aspect of my "system"
that I would like to mention it again.

When I still used primitive task management systems such as *everything else*
that's not Org mode, the collection of more mature tasks would soon grow out of
control.

However, because I create a new Org mode file for every month, I have to copy
across manually any tasks that have not been completed yet.

"WHY IS THAT NOT AUTOMATED YET?!" you are probably thinking.

Well, the advantage of having to copy each task over manually is that it is the
ideal opportunity to evaluate the task and ask some hard questions as to its
continued relevance...

When a task gets too old, I will often make the decision to change its status
to `CANC` (for cancelled), sometimes with the reason for the cancellation
explained in the task body, and then just leave it there in the old month file.

With most of these task systems, regular reviews are of crucial importance. The
monthly start-over is a great, almost enforced, opportunity for review, as is
the morning routine when I instantiate the day planner template.

##### What about email?!

An important part of knowledge and task management is one's emails.

Although I currently prefer processing my email using
[`mu4e`](/2019/07/17/weekly-head-voices-173-i-know/#would-you-like-some-more-emacs-with-that-email),
an email client which lives inside of Emacs, I have used other tools in the
past, and will probably use new tools in the future.

Also, even at this moment I alternate between `mu4e` and the
[FastMail](/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/)
web-interface.

Long story short, I have it setup so that I can easily convert any email in
`mu4e` into a universal `message://message-id` link to be integrated with a
new task or note entry.

When I later open that link using a shortcut, I have programmed it so that
`mu4e` will open the relevant email if it is active, or the `FastMail` webmail
when it is not. From here I can either review the email to see what the
associated task requires, or respond to it, if the task has been completed.

Some of these `message://` links were created using macOS mail and they still
work. In future, if I add a new mail client to the mix, I will still be able to
jump to specific old emails, no matter where they find themselves inside of my
FastMail mailboxes.

#### Core notes database.

With `database` I of course refer to hundreds of org and markdown files, most
of which find themselves in the top-level `pkb4000` directory, one level up
from the `journals` directory containing all of the monthly journal files.

There are files on various `rsync` or `ffmpeg` invocations, files on
programming languages, software tools, note-taking strategies, personal
information on each of my kids, and much more.

Org mode enables me to combine document structure, math, vector and bitmap
images and executable source code in many different languages.

I have configured my Emacs (where by "configured" I mean "coded up the emacs
lisp for") to invoke ripgrep on different subsets of my notes database, and to
proffer up the results in different ways.

I can usually find anything that went in to this database at any point.

What I really like, is also being able to tell you on which day, and during
which hour, I learned this or that, or experimented with something or the
other.

#### Project files.

Work and personal projects each get their own Org file. Some projects even get
a whole directory to themselves, in cases where the project will have many more
files than just the main Org file.

In all cases, the project org file will live somewhere below a year-stamped
directory, e.g. `work/projects/2019/project-name/`.

Some projects go over year boundaries, but their files and directories remain
in the year that they started in. The project org also has `Tasks` and a
datetree section, similar to the month journal.

All current project files, along with my the current month file, are configured
to be part of the `org-agenda-files` variable.

This means that when I activate the `org-agenda` view, I see a unified list of
all tasks as extracted from all current project files and the current monthly
journal file.

When a project is completed, it is of course removed from `org-agenda-files`.

### Web-pages and articles.

As mentioned in the short system overview, I store all web-pages and articles I
come across as date-stamped PDF files in a set of year-stamped directories.

For more detail, please refer to the
[JBOP](/2019/03/21/weekly-head-voices-165-get-in-my-pocket/#replacing-pocket-with-just-a-bunch-of-pdfs-jbop)
section of WHV#165 on this blog.

In short, I use good ad-blocking and *mostly* the [printfriendly browser
extension](https://www.printfriendly.com/) in Brave or Chromium to convert any
interesting web-pages to PDF. PDF articles from journals and other reputable
sources obviously don't have to be converted.

I name and save these PDFs into my `refs` hierarchy, for example
`Dropbox/refs/2019/20190518 Measles and Immune Amnesia - asm.pdf`.

Usually, to win any argument, I can find the pertinent reference on my phone or
my laptop in 30 seconds or less.

(I used to be a paying Pocket subscriber. However, as you will read in WHV#165
cited above, I was disappointed by the super important search function. The
advantages of having Just a Bunch of PDFs on your (synced) disc are many.)

### Zotero.

The `refs` directory hierarchy described above is great for quickly storing an
article in the right place with a suitable name, ready for search-based
retrieval later.

However, in cases where one needs to cite any academics works, having these
articles in a good reference manager is important.

Zotero is in my view one of the best reference managers out there, and it's open
source!

The reasons I prefer zotero are:

- You can make use of their synchronisation service, or you can do it
  yourself. I have about 2.3GB of additional articles in zotero, so this is
  great.
- Zotero uses your browser to retrieve fulltexts automatically when you import
  any web-page with bibliographic information using the browser extension. This
  is great when you have access via your institution. Competing cloud services
  would historically use *their* servers to retrieve the fulltext, which would
  often not work.
- Zotero is open source. To me this is important, [because on more than one
  occasion](https://vxlabs.com/tags/zotero/) I have been able to make small
  modifications to make it perform peculiar tricks I needed at that point.

### Mobile.

This has always been the weakest part of my whole knowledge management system.

Ideally, I would have easy access to my complete org database and any related
files. Ideally, it would be possible to store any interesting tidbits I come
across whilst browsing using my phone.

So far I have invested time in the following apps and ecosystems:

- iCloud Notes: This was great, until [I sold my
  MacBook](/2019/04/27/new-laptop-2019/#so-tell-me-why-did-your-somewhat-stylish-macbook-phase-have-to-come-to-an-end). iCloud
  Notes web-access is terribly slow and more or less unusable. Whatever I have
  on mobile, needs to interoperate smoothly with desktop.
- Google Keep: This worked pretty well on mobile and via the web, but it's a
  closed off ecosystem. You can
  ["takeout"](https://takeout.google.com/settings/takeout) your data, but you
  end up with ginormous HTML files (images are base64-encoded and included)
  that are not straight-forward to work with.
- OneNote: This has SO MUCH potential (free-form note-taking, drawing with
  Apple Pencil, apps for so many platforms, great organization, etc. etc.) but
  is just so frustratingly unusable due to syncing issues everywhere, even on
  my true-blue Windows 10 laptop with the true-blue official gold star
  Microsoft OneNote application. Microsoft is doing fantastic work in some
  domains (Visual Studio Code, .net core, WSL, etc. etc.) but in some others
  not so much it seems.
- Evernote: I recently just gave up and bought a premium subscription for the
  year, because Evernote is the industry standard and it had Apple Watch voice
  notes even before WatchOS 6 was released. In any case, although initially
  promising, Evernote is unfortunately quite slow at unpredictable moments
  (sharing web-page with evernote mobile app for storage can sometimes take 20
  second or more...) so I've had to ditch it. Again.
  
During all of this experimentation, I started storing mobile discoveries in a
new section called "inbox" in the relevant note-taking app's organizational
structure. During morning review, I go through the relevant inbox, and
re-convert the relevant page into PDF for my more permanent archive.

It dawned on me that this approach could also be applied with just the Dropbox
app! It would be klunky, but at least not disappointing.

So, when I want to store something from the phone, I either print to PDF or
make use of the "Save to Dropbox" app extension, and then store the resultant
PDF in `Dropbox/notes/inbox`. During morning review, PDFs in this directory are
re-converted if required, and then stored in their more permanent home.

Using the Dropbox app, I can also create markdown text files in the `inbox`
directory.

If I have something a little more extensive, I have the option of using the
"Voice Memos" app, either on the phone, or even via the Apple Watch.

In `Dropbox/notes/mobile` I keep items I often need to access from the phone:
Think loyalty cards, markdown files with IP numbers and configuration of my
home network, and so on. This directory is marked as "available offline", so I
can access its contents even when there's no data connection.

Other than that, I do an export of my whole org database to HTML now and then,
following a procedure similar to the one I used [to use for exporting Org mode
to iCloud
Notes](https://vxlabs.com/2018/10/29/importing-orgmode-notes-into-apple-notes/). The
HTML versions are searchable on the phone.

What would be better, is if the Dropbox iOS app would start recognising .org
files as plaintext files, much like what it already does for markdown .md
files. As it stands, I keep a small subset of my notes as markdown, instead of
the superior org, for mobile editing.

#### Drawing with Apple Pencil on the iPad using Notability.

Sometimes one does need to sketch.

This could be a rough UI, an architecture diagram, a data flow chart, or just
doodling.

Since about the end of 2018, I've been using the [Notability
app](https://apps.apple.com/za/app/notability/id360593530) along with an iPad
6th gen (2018 entry-level, the first non-Pro to support the Pencil) to doodle
electronically.

Notability automatically syncs all of these drawings as fully vectorised PDFs
to my Dropbox. All handwritten text is quite smartly OCRd, and the OCRd version
is stored as correctly positioned metadata behind my ugly scribbles.

I would have liked Notability even more if it supported arbitrary canvas sizes
(as it stands, only standard paper size in protrait mode), and had an always
visible overview minimap.

#### Signal messaging app's brilliant "Note to Self" contact.

The [Signal messaging app](https://signal.org/), which you should all be using,
has a built-in contact called "Note to Self".

As of late (since about December 2019) this has become my main *capturing tool*
when I'm on the phone.

You can share links, media, photos, voice notes or a plain old text message,
all of which will be securely stored, neatly timestampted to boot, in your
conversation with this silent but very useful "Note to Self" character.

During the morning review, I go through each of the shared items, processing
them, and then add the message "DONE =====>" to indicate that they have been
completed.

## Limitations and points for improvement.

The current system is great for capturing and search-based retrieval of
personal knowledge.

However, I miss functionality for making some of the higher-level patterns and
networks more *discoverable*.

For example, as I create a new orgmode entry, the system could show me related,
older nodes (that is something I could implement...).

Furthermore, it would have been great to see some form of visual representation
of the associations between nodes, and of how they fit into higher-level
concepts. This bit is slightly far-fetched.

Interestingly, I just ran into the following paragraph at the end of [my 2016
note-taking post](/2016/01/05/note-taking-strategy-early-2016/):

> However, I think that there might be room for a fourth type of tool that is
> more visual, supports rich and graphical linking between data items and even
> between sub-components of such items and, perhaps most importantly, enables
> us to build note landscapes that are natively as non-linear as our thoughts.

Let's see what happens over the next few years!

## Appendix

### Redacted Emacs Orgmode capture template

``` emacs-lisp
;; normally I construct current-journal-filename using mix of expand-file-name and concat
(setq current-journal-filename "/full/path/to/current/month-journal/")
;; %i = selected text, %a org-store-link, %U created timestamp, %? place cursor here
(setq org-capture-templates
      '(("t" "Todo" entry (file+headline current-journal-filename "Tasks")
         "* TODO %?\n:LOGBOOK:\n- Created \"TODO\" %U\n:END:\n%i\n%a\n\n" 
         :empty-lines 1)
        ("j" "Journal" entry (file+olp+datetree current-journal-filename)
         "* %? %T\n"
         :empty-lines 1)
        ("p" "Day planning" entry (file+olp+datetree current-journal-filename)
         "* Day planning %U

** Done list / thoughts / diary

- %?

** Tasks for today [/]

** Experiment: Articulate your directions / systems.

** Tasks that will satisfy end-of-the-day Charl [/]

** Focus blocks

** Review [/]
- [ ] [[*Vitals][Month vitals]]
- [ ] Org sub-projects
- [ ] Calendar
- [ ] ...

** Habits / important [/]
- [ ] 7.5 hrs sleep last night
- [ ] are you satisfied with number of pomodori? = 0 (v R)
- [ ] did you write stuff down?
- [ ] ...

"
         :empty-lines 1)))
```

## Updates

### Sunday 2020-01-12

- Add [example of orgmode capture template
  configuration](#redacted-emacs-orgmode-capture-template) in appendix.
- Add [section about iPad, Notability and Apple
  Pencil](#drawing-with-apple-pencil-on-the-ipad-using-notability).
- Add [section about Signal's Note to Self
  contact](#signal-messaging-apps-brilliant-note-to-self-contact).

