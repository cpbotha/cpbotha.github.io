---
title: My PalmOS-based GTD setup
author: cpbotha
type: post
date: 2007-10-07T14:28:08+00:00
url: /2007/10/07/my-palmos-based-gtd-setup/
categories:
  - life
tags:
  - gtd
  - productivity

---
HI THERE GANG! If you don't like long-winded introductions, skip to the bit
starting with "THE NITTY GRITTY".

Getting Things Done (GTD, see [here][1] for the book, [here][2] and [here][3]
for introductory information, and [here][4] for a cool workflow diagram) by
David Allen is a master-piece. Having read it, most of it kind of fits. It's
almost as if, if one had had the time to sit down and think for long enough,
one would have come up with the same brilliant tips. But one hadn't, so one
didn't. The Delete-Do-Delegate-Defer monster, contextual todo-lists
(Work-Computer, Home, Calls, Errands, etc.), the Weekly Review(tm) and
_actionable_ next actions are some of the most valuable things I picked up when
I read this book about a year and a half ago.

As all GTD converts do, I initially set out to design the perfect GTD
implementation (Allen leaves one to one's own devices), and as is always the
case, it was far from. Based on the use of a Palm Tungsten C, my system was
lacking a direct link between projects and next actions which eventually
resulted in things falling through the cracks. Things Falling Through Cracks
are of course highly undesirable, and can even be acutely embarrassing.

So recently, because my system erroneously reported that I had absolutely
nothing to do (and because I have one of the biggest deadlines of my life
looming, of course), I spent my completely imaginary free time improving my GTD
implementation. It seems to be going swimmingly, so I've documented it here:

# The Nitty Gritty
  
## Electronic
  
Everything is coordinated on my Palm Tungsten C with Datebk6 (Datebk5 should
also do the trick). Everything else (mail, physical files) is ancillary, the
Tungsten is canonical. If it's not in there, it won't get done. So:

- each project gets a memofile, first line is "0project_code - project name",
  e.g. "0VCBM08 - organize VCBM 2008 congress in Delft", second line is the
  outcome, i.e. what should happen for me to consider the project
  successful. The rest of the memo file contains unstructured metadata related
  to the congress. All these memofiles are in the category "@ Projects"
- right after having created the project memofile, I create all actionable
  tasks as normal Palm ToDos in DateBk6. Each task name is built up as follows:
  "0project_code:: task description", for example "0VCBM08:: Call TU congress
  facilities to get a quote."
- all tasks, except for the next actions are put in the category
  "99Dormant". The next actions are put in the categories corresponding to
  their correct contexts, for example "@ Work-Comp".
- you can see where this is going: in DateBk6, one can very easily change which
  categories of todos are shown (I use shortcut stroke-2), depending on one's
  context. "99Dormant" is last in the list, so I keep these tasks
  invisible. When a task is completed, it is ticked off, and the next task's
  category is toggled from "99Dormant" to its correct context, meaning it won't
  be invisible / inactive anymore and will appear in the correct context.
- to get an overview of all next tasks, I activate all ToDo categories,
  including "99Dormant". I have the ToDo views sorted alphabetically, so all
  tasks belonging to a project automatically clump together, thus giving me a
  nice project-oriented overview. Because all project codes start with "0",
  they clump together at the beginning.
- tasks can optionally have a due date. I've set up ToDos in DateBk6 to show
  always, no matter their due date In general, I only date next actions if they
  very clearly constitute the last required step for a deadline to be met.
- I have an optional project code "YYDead::" just for deadlines. These are not
  actionable items, they are merely reminders.
- I also have project code "ZZ::" for project-less next actions.
- Completed project memofiles are moved to the category "@ Completed" for
  documentation purposes. There is also a "@ Someday / Maybe" category for
  project memofiles that can be simply activated later.

In this way, I have a very explicit link from project to constituent actions,
and also to next actions. In contrast to [PigPog][5]'ing, I also get the
endorphin rush when I check off an action as done, and I've setup DateBk6 to
make a note in my daily journal (automatically) documenting when it was
completed. I haven't tried this yet because I don't really need it, but with a
tool such as PsLink and the appropriate project codes it should be possible to
link back from any task to its parent project.

## Physical
  
I have two sets of transparent file thingies: one in my laptop bag (always with
me), and one at home, each set consisting of 3 labeled classes: @ Read /
Review, @ Waiting For and @ Actions. This is for carrying around paper work
that relates to these contexts. However, each piece of paper work is covered by
an entry in my PDA.

That should cover it! If I've missed anything, or something is not clear,
please let me know in the comments so I can amend this posting.

 [1]: http://www.amazon.co.uk/Getting-Things-Done-Stress-Free-Productivity/dp/0142000280/ref=pd_bbs_sr_2/026-1822804-9222826?ie=UTF8&s=books&qid=1191746337&sr=8-2 "Link to Allen's GTD on amazon.co.uk."
 [2]: http://www.43folders.com/2004/09/08/getting-started-with-getting-things-done "43folders introduction to GTD."
 [3]: http://gtd.marvelz.com/blog/2007/07/10/gtd-gems-part-1/ "More intro info on GTD."
 [4]: http://www.scribd.com/doc/249379/Getting-Things-Done-advanced-work-flow-diagram "GTD advanced workflow diagram"
 [5]: http://pigpog.com/node/1031 "GTD PigPog method"
