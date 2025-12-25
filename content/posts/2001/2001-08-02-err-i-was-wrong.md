---
title: Err, I was wrong.
author: cpbotha
type: post
date: 2001-08-02T18:38:00+00:00
url: /2001/08/02/err-i-was-wrong/
categories:
  - Uncategorized

---
So the ram is fine if we can trust memtest86. Why am I still getting oopses?! I sent a mail to the reiserfs mailing list and got the typical reiserfs answer: your hardware is borked, it _can’t_ be our code. Hmmmm… right. I’m sure the reiserfs code is well-tested, but it’s still not a good approach to blame the hardware _immediately_, especially if tests indicate elsewhere. What the hell, I’m going to try and reproduce this. At the moment the oopses are so sporadic (sometimes days apart) that finding the problem is going to take weeks. If I can reproduce the oops however, that’s going to make things much easier.
