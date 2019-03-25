---
title: Getting the FRIKKING euro key working on a Dvorak keyboard layout in Ubuntu 5.04
author: cpbotha
type: post
date: 2005-09-22T14:16:16+00:00
url: /2005/09/22/getting-the-frikking-euro-key-working-on-a-dvorak-keyboard-layout-in-ubuntu-504/
categories:
  - Uncategorized

---
I&#8217;ve lost at least 5 hours of my life to the frikking euro key on my Microsoft Natural (old-style) keyboard. It seems that Gnome 2.10 on Ubuntu 5.04, otherwise a great combination, enjoys torturing its Dvorak keyboard layout users with the euro-symbol on the &#8216;5&#8217; key. It simply doesn&#8217;t work, no matter what you try.

After sacrificing the prerequisite 5 hours to the Linux gods of Ultimate Non-Usability, I came up with the following solution. Make the following change to your /etc/X11/xkb/symbols/pc/dvorak file:
  
`<br />
--- dvorak.ORIG 2005-09-22 11:28:18.704428504 +0200<br />
+++ dvorak      2005-09-22 11:45:14.296035112 +0200<br />
@@ -16,7 +16,7 @@<br />
     key <ae02> { [         2,  at              ]       };<br />
     key <ae03> { [         3,  numbersign      ]       };<br />
     key <ae04> { [         4,  dollar          ]       };<br />
-    key <ae05> { [         5,  percent         ]       };<br />
+    key <ae05> { [         5,  percent, EuroSign, EuroSign ] };<br />
     key <ae06> { [         6,  asciicircum, dead_circumflex, dead_circumflex ]};<br />
     key <ae07> { [         7,  ampersand       ]       };<br />
     key <ae08> { [         8,  asterisk        ]       };<br />
` 

Now make sure that your right-ALT generates ISO\_Level3\_Shift (also known as AltGr) by using xev. If your font and roughly 8000 other little settings support it, pressing right-alt-5 should make a pretty euro symbol.