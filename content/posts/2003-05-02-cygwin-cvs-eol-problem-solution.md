---
title: Cygwin CVS EOL problem solution
author: cpbotha
type: post
date: 2003-05-02T00:22:53+00:00
url: /2003/05/02/cygwin-cvs-eol-problem-solution/
categories:
  - howto
tags:
  - cvs
  - cygwin
  - version control

---
At this very moment, you might be wondering why, if [CVS][1] is such a wonderful piece of version control software that even offers to soothe your cross-platform end of line woes (\*ix: eol = lf, macos: eol = cr, windows: eol = crlf), it&#8217;s suddenly breaking the end of line checkouts on the \*ix side since you&#8217;ve been committing your ports on the windows side with CVS from [Cygwin][2].

The answer is fortunately far shorter and simpler that the previous sentence. Cygwin also has to deal with the ugly text file / binary file distinction on Windows, and therein lies the problem. Make sure that any filesystem from whence you will be committing with Cygwin CVS is mounted with the textmode option (and not binmode). Running &#8220;mount&#8221; will tell you if this is the case or not.

If it isn&#8217;t, a simple &#8220;mount -f -t -s d: /cygwin/mount/point&#8221; should do the trick. See [here][3] for more detail.

 [1]: https://en.wikipedia.org/wiki/Concurrent_Versions_System
 [2]: http://www.cygwin.org/
 [3]: https://chess.eecs.berkeley.edu/softdevel/faq/5.html
