---
title: My PalmOS-based GTD setup
author: cpbotha
type: post
date: 2007-10-07T14:28:08+00:00
url: /2007/10/07/my-palmos-based-gtd-setup/
categories:
  - life

---
HI THERE GANG! If you don&#8217;t like long-winded introductions, skip to the bit starting with &#8220;THE NITTY GRITTY&#8221;.

Getting Things Done (GTD, see [here][1] for the book, [here][2] and [here][3] for introductory information, and [here][4] for a cool workflow diagram) by David Allen is a master-piece. Having read it, most of it kind of fits. It&#8217;s almost as if, if one had had the time to sit down and think for long enough, one would have come up with the same brilliant tips. But one hadn&#8217;t, so one didn&#8217;t. The Delete-Do-Delegate-Defer monster, contextual todo-lists (Work-Computer, Home, Calls, Errands, etc.), the Weekly Review(tm) and _actionable_ next actions are some of the most valuable things I picked up when I read this book about a year and a half ago.

As all GTD converts do, I initially set out to design the perfect GTD implementation (Allen leaves one to one&#8217;s own devices), and as is always the case, it was far from. Based on the use of a Palm Tungsten C, my system was lacking a direct link between projects and next actions which eventually resulted in things falling through the cracks. Things Falling Through Cracks are of course highly undesirable, and can even be acutely embarrassing.

So recently, because my system erroneously reported that I had absolutely nothing to do (and because I have one of the biggest deadlines of my life looming, of course), I spent my completely imaginary free time improving my GTD implementation. It seems to be going swimmingly, so I&#8217;ve documented it here:

**The Nitty Gritty
  
** 
  
_Electronic:_
  
Everything is coordinated on my Palm Tungsten C with Datebk6 (Datebk5 should also do the trick). Everything else (mail, physical files) is ancillary, the Tungsten is canonical. If it&#8217;s not in there, it won&#8217;t get done. So:

  * each project gets a memofile, first line is &#8220;0project_code &#8211; project name&#8221;, e.g. &#8220;0VCBM08 &#8211; organize VCBM 2008 congress in Delft&#8221;, second line is the outcome, i.e. what should happen for me to consider the project successful. The rest of the memo file contains unstructured metadata related to the congress. All these memofiles are in the category &#8220;@ Projects&#8221;
  * right after having created the project memofile, I create all actionable tasks as normal Palm ToDos in DateBk6. Each task name is built up as follows: &#8220;0project_code:: task description&#8221;, for example &#8220;0VCBM08:: Call TU congress facilities to get a quote.&#8221;
  * all tasks, except for the next actions are put in the category &#8220;99Dormant&#8221;. The next actions are put in the categories corresponding to their correct contexts, for example &#8220;@ Work-Comp&#8221;.
  * you can see where this is going: in DateBk6, one can very easily change which categories of todos are shown (I use shortcut stroke-2), depending on one&#8217;s context. &#8220;99Dormant&#8221; is last in the list, so I keep these tasks invisible. When a task is completed, it is ticked off, and the next task&#8217;s category is toggled from &#8220;99Dormant&#8221; to its correct context, meaning it won&#8217;t be invisible / inactive anymore and will appear in the correct context.
  * to get an overview of all next tasks, I activate all ToDo categories, including &#8220;99Dormant&#8221;. I have the ToDo views sorted alphabetically, so all tasks belonging to a project automatically clump together, thus giving me a nice project-oriented overview. Because all project codes start with &#8220;0&#8221;, they clump together at the beginning.
  * tasks can optionally have a due date. I&#8217;ve set up ToDos in DateBk6 to show always, no matter their due date In general, I only date next actions if they very clearly constitute the last required step for a deadline to be met.
  * I have an optional project code &#8220;YYDead::&#8221; just for deadlines. These are not actionable items, they are merely reminders.
  * I also have project code &#8220;ZZ::&#8221; for project-less next actions.
  * Completed project memofiles are moved to the category &#8220;@ Completed&#8221; for documentation purposes. There is also a &#8220;@ Someday / Maybe&#8221; category for project memofiles that can be simply activated later.

In this way, I have a very explicit link from project to constituent actions, and also to next actions. In contrast to [PigPog][5]&#8216;ing, I also get the endorphin rush when I check off an action as done, and I&#8217;ve setup DateBk6 to make a note in my daily journal (automatically) documenting when it was completed. I haven&#8217;t tried this yet because I don&#8217;t really need it, but with a tool such as PsLink and the appropriate project codes it should be possible to link back from any task to its parent project.

_Physical:_
  
I have two sets of transparent file thingies: one in my laptop bag (always with me), and one at home, each set consisting of 3 labeled classes: @ Read / Review, @ Waiting For and @ Actions. This is for carrying around paper work that relates to these contexts. However, each piece of paper work is covered by an entry in my PDA.

That should cover it! If I&#8217;ve missed anything, or something is not clear, please let me know in the comments so I can amend this posting.

 [1]: http://www.amazon.co.uk/Getting-Things-Done-Stress-Free-Productivity/dp/0142000280/ref=pd_bbs_sr_2/026-1822804-9222826?ie=UTF8&s=books&qid=1191746337&sr=8-2 "Link to Allen's GTD on amazon.co.uk."
 [2]: http://www.43folders.com/2004/09/08/getting-started-with-getting-things-done "43folders introduction to GTD."
 [3]: http://gtd.marvelz.com/blog/2007/07/10/gtd-gems-part-1/ "More intro info on GTD."
 [4]: http://www.scribd.com/doc/249379/Getting-Things-Done-advanced-work-flow-diagram "GTD advanced workflow diagram"
 [5]: http://pigpog.com/node/1031 "GTD PigPog method"