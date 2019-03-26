---
title: phpBugTracker
author: cpbotha
type: post
date: 2004-11-27T20:17:51+00:00
url: /2004/11/27/phpbugtracker/
categories:
  - Uncategorized

---
This weekend I decided that it was time to install web-based bug-tracking software to allow the users of [DeVIDE][1] (all 2 of them) to be able to report bugs and to allow me to be able to keep track of all the reports.

Because of my experience with the [phpBugTracker][2] installation used by [Kitware][3] for [VTK][4], [ITK][5] and a bunch of their other products, I decided to go with this software.

However, after installing and configuring this, I got the following error message when trying to login for the first time:
  
`<br />
Fatal error: session_start(): Failed to initialize storage module: user (path: /tmp) in /home/bothac/public_html/bugs/include.php on line 169<br />
` 

ARGH! After some searching around, this turns out to be a some generic PHP problem, solved by making the following changes before the session_start() call in include.php:
  
`<br />
if (!defined('NO_AUTH')) {<br />
  // change by cpbotha<br />
  ini_set('session.save_handler', 'files');<br />
  // end of change by cpbotha<br />
  session_start();<br />
` 

So, after fixing this, attempting to commit any change in the bug-tracking system lead to an apparently famous &#8220;headers already sent&#8221; error message. It turns out that you should not have any spaces or empty lines after the last &#8220;?>&#8221; in your config.php!

I mention this in the hope of saving somebody else all the trouble. This is otherwise a very useful system.

 [1]: http://cpbotha.net/DeVIDE
 [2]: http://phpbt.sf.net/
 [3]: http://www.kitware.com/
 [4]: http://www.vtk.org/
 [5]: http://www.itk.org/
