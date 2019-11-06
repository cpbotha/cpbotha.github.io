---
title: "Forming and maintaining habits using Orgmode."
slug: "forming-and-maintaining-habits-using-orgmode"
date: 2019-11-02T16:48:00+02:00
tags:
  - compounding
  - habits
  - habit tracking
  - orgmode
  - streaking
categories:
  - howto
type: "post"
---

In this post, I explain how to get up and running with Emacs Orgmode habits.

Even if you're not planning to use Emacs for this, it might be interesting
context for the development of other ideas for habit tracking tricks and tools.

## The importance of habits.

If you have some experience being, you know, alive, and perhaps even trying to
get just that little bit better at it every day, you will have realised by now
that being able to form and maintain good habits is almost a super power.

(Other real-life super powers: Kindness. Peace. Focus. I digress... haha.)

All of those promises we make to ourselves to read more, to eat better, to
exercise more, to meditate regularly, and so on: The key to making all of these
happen is forming and then maintaining habits.

First the habit has to be created out of nothing, and once it's up and running,
the idea is to keep going at it for as long as possible.

[Streaking](/2019/09/09/weekly-head-voices-177-streakers/#life-optimisation-tip-73-streak-more),
that is trying to continue for as long as possible without any interruption, is
a fun and effective trick to keep at it.

However, it is just as important being able to restart a new streak once the
previous one has been broken for whatever reason.

## What the Orgmode habit tracker does.

Up to now, I mostly used [daily checklists to keep track of healthy
habits](/2019/09/21/note-taking-strategy-2019/#monthly-journal-files), but for
some habits, especially ones with a non-daily frequency, this does not work so
well.

A significant step up from daily checklists, the [Emacs Orgmode habits
function](https://orgmode.org/manual/Tracking-your-habits.html) enables you:

- to specify any number of habits, each with different, sometimes less regular
  frequencies;
- to track when you perform a habit and when you should next perform it and finally
- to visualize if you are performing according to the specifications you have
  set.
  
For example: I would like to run at least three times a week. There should be
at least one rest day after a running day (I'm not a spring chicken
anymore). There should be a maximum of three rest days allowed (this usually
happens after a longer weekend run).

Although I enjoy running enough to keep this habit up by myself, I chose it as
a first test of the Orgmode habits function.

So far I have setup two other simpler examples:

- A core exercise which I call "The Wheel" (of pain). This has to happen every
  second day, usually in between running days.
- "Deep reading", which is meant to describe a session of focused reading of
  long-form, i.e. mostly books. This has to happen every day.
  
Before starting tracking of these latter two habits slightly more than a week
ago, I somehow kept on letting them slip.

This morning, my org-agenda looked like this:

<figure>
<a href="org-habits-screenshot.png">
{{< img src="org-habits-screenshot.png" >}}
</a>
</figure>

In the figure you can see that today, represented by the exclamation mark `!`,
I will have to schedule in a session of deep reading (indicated by the yellow
colouring), and a session of "the wheel".

The running habit graph  is showing that I still have three days, including
today, on which I do not have to run.

By default it would not have displayed today, because I ran yesterday, as shown
by the asterisk `*`, and I specified that minimum of one rest day. However, I
temporarily configured it to show today for the sake of this exposition.

To summarise: These habit graphs show up as part of your org-agenda view and
show you at a glance when you should perform which habits, and, quite
importantly, how long you have been streaking a particular habit.

## How to setup Orgmode habits.

### Global configuration.

Firstly, ensure that the `org-habit` Orgmode extension is activated by adding
the following to your `init.el`:

``` elisp
(add-to-list 'org-modules 'org-habit t)
```

Whilst your in your `init.el`, add something like the following to activate
state logging for the task `DONE` state:

``` elisp
;; each state with ! is recorded as state change
;; in this case I'm logging TODO and DONE states
(setq org-todo-keywords
      '((sequence "TODO(t!)" "NEXT(n)" "SOMD(s)" "WAFO(w)" "|" "DONE(d!)" "CANC(c!)")))
;; I prefer to log TODO creation also
(setq org-treat-insert-todo-heading-as-state-change t)
;; log into LOGBOOK drawer
(setq org-log-into-drawer t)
```

### Per-habit configuration.

Then, start creating the special habit nodes as explained in the following:

Below is what the "running" habit currently looks like in my [current monthly
journal file](/2019/09/21/note-taking-strategy-2019/#monthly-journal-files):

<!-- I used M-x htmlize-region-save-screenshot to get this HTML representation of a real org file onto the clipboard. -->
<pre style="color: #DCDCCC; background-color: #3F3F3F;">
<span style="color: #BFEBBF; background-color: #3F3F3F;">** </span><span style="color: #CC9393; font-weight: bold;">TODO</span><span style="color: #BFEBBF; background-color: #3F3F3F;"> Running</span>
<span style="color: #7F9F7F;">SCHEDULED:</span> <span style="color: #8CD0D3; text-decoration: underline;">&lt;2019-11-03 Sun .+2d/4d&gt;</span>
<span style="color: #7F9F7F;">:PROPERTIES:</span>
<span style="color: #7F9F7F;">:STYLE:</span>    habit
<span style="color: #7F9F7F;">:LAST_REPEAT:</span> <span style="color: #8CD0D3; text-decoration: underline;">[2019-11-01 Wed 16:00]</span>
<span style="color: #7F9F7F;">:END:</span>
<span style="color: #7F9F7F;">:LOGBOOK:</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-11-01 Wed 16:00]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-30 Wed 15:41]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-26 Sat 14:14]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-24 Thu 19:11]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-22 Tue 16:00]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-20 Sun 10:00]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-18 Fri 16:00]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-18 Fri 16:00]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-16 Wed 08:13]</span>
- State "DONE"       from "TODO"       <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-13 Sun 10:00]</span>
- Created "TODO" <span style="color: #8CD0D3; text-decoration: underline;">[2019-10-23 Wed 09:53]</span>
<span style="color: #7F9F7F;">:END:</span>
</pre>

The [orgmode habits
documentation](https://orgmode.org/manual/Tracking-your-habits.html) explains
that a habit is a special sort of `TODO` node with the following additional
properties, which can all be seen in the above example:

- The node has a `:STYLE:` property of `habit`. Configure with =M-x
  org-set-property=.
- The node has a `SCHEDULED` date in the future on the next date when this
  habit should take place, along with a frequency / time constraint
  specification, in this case `.+2d/4d`, meaning that at the most every second
  day, and at the least every fourth day.

Furthermore, with `DONE` state logging configured as explained above, you'll
get the `LOGBOOK` with the required state changes used by the habit graphs.

### In use.

Whenever you've completed a habit, fire up Emacs (I'm joking of course: Emacs
is always running) and then toggle the state of the habit to `DONE`.

You'll see that it briefly toggles to `DONE`, and then automatically switches
back to `TODO`.

(There's some philosophical lesson to be learned from that...)

When this happens, the `:LAST_REPEAT:` timestamp will be automatically updated
to the current time, and, more importantly, the `SCHEDULED` date will be
automatically updated to the next earliest date when this habit should be
exercised.

In the case of the running example above, that will be tomorrow, as today is a
rest day.

Whenever you activate org-agenda, you'll see the habit graphs right at the top,
by default only on the days when they are actually scheduled. In the running
example, that habit will not appear on rest days. (This can naturally be
configured, see `M-x describe-variable RET org-habit-show-all-today`).

## Conclusion.

- Being able to forming and maintain habits can form an important component of
  better living.
- *Habit streaking* is a fun psychological trick to keep you going.
- However, don't be disheartened by a broken streak. Get back on that horse and
  try again.
- Emacs Orgmode habit tracking is a great tool for Emacs users to help form and
  maintain habits, especially non-daily ones.
