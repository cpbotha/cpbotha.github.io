---
title: Where should that dang button go?
author: cpbotha
type: post
date: 2003-05-04T14:59:54+00:00
url: /2003/05/04/where-should-that-dang-button-go/
categories:
  - howto
tags:
  - design guidelines
  - gui
  - microsoft
  - UI
  - UX
  - windows

---
So, here we have the [Aqua Human Interface Guidelines][1] (i.e. the MacOS-X user interface guidelines), the [GNOME Human Interface Guidelines][2], the [KDE User Interface Guidelines][3] and of course the [Microsoft Windows Official Guidelines for User Interface Developers and Designers][4] (I came back in January of 2018 to fix this link &#8212; also interesting is the [section on margins and spacing][5]).

Apple [says][6] that &#8220;The default button for dismissing a dialog should go in the lower-right corner. If there’s a Cancel button, it should be to the left of the default button.&#8221;. Gnome [seems to imply][7] that the default button should be on the bottom right, with other buttons to its left, which is more or less consistent with the Apple guidelines.

Microsoft [says][8]: &#8220;Lay out the major command buttons either stacked along the upper right border of the dialog box or lined up across the bottom of the dialog box. Position the most important button — typically the default command — as the first button in the set.&#8221; The KDE User Interface Guidelines don&#8217;t seem to set specific constraints on this kind of button placement, but judging by many of the standard KDE 3.1 applications, the dialogs seem to follow the Windows convention.
  
<!--more-->


  
So, amongst these major user interfaces, it seems there are two camps: the &#8220;default-button-first-in-the-group&#8221; camp and the &#8220;default-button-in-the-bottom-right-corner&#8221; camp, which leaves us with a major headache if we&#8217;re trying to develop cross-platform software. No matter what convention you choose for, there are going to be clashes between the dialog boxes you&#8217;ve designed for your application and the OS-specific common dialogs (e.g. colour selection, font selection, etc.) that you&#8217;re bound to use.

I&#8217;m afraid that I&#8217;m going to have to opt for the Windows/KDE convention. Linux users have learnt to live with the inconsistency (KDE vs Gnome conventions in this case) and will probably not notice. Windows users on the other hand, are quite used to the relative position of their buttons. I confirmed this by conducting a survey amongst a large group consisting of one novice Windows user. How&#8217;s that for solid research?

Seriously though, the application in question will mostly be used by two kinds of users: Doctors or non-geek professionals using Windows and Super-Geeks Using Linux. The former group will probably be significantly larger than the latter group.

What do you think?

 [1]: http://developer.apple.com/techpubs/macosx/Essentials/AquaHIGuidelines/index.html
 [2]: http://developer.gnome.org/projects/gup/hig/
 [3]: http://developer.kde.org/documentation/standards/kde/style/basics/index.html
 [4]: https://msdn.microsoft.com/en-us/library/windows/desktop/dn688964(v=vs.85).aspx
 [5]: https://msdn.microsoft.com/en-us/library/windows/desktop/dn742486(v=vs.85).aspx
 [6]: http://developer.apple.com/techpubs/macosx/Essentials/AquaHIGuidelines/AHIGLayout/chapter_8_section_2.html
 [7]: http://developer.gnome.org/projects/gup/hig/1.0/windows.html#alert-button-order
 [8]: http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnwue/html/ch09d.asp
