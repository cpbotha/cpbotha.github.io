---
title: 'User interface boo-boo #1: Disabled controls without explanations!'
author: cpbotha
type: post
date: 2016-01-06T20:24:38+00:00
url: /2016/01/06/user-interface-boo-boo-1-disabled-controls/
categories:
  - tech
tags:
  - discoverability
  - qt creator
  - rant
  - UI
  - user interface
  - UX

---
Today as I was configuring some build settings in [Qt Creator][1], an otherwise really great product, I was faced with this extremely frustrating situation:

{{< figure src="/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM.png" link="/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM.png" >}}

I absolutely, definitely needed to configure the debugger. However, the controls required to do so were disabled, as can be seen by their greyed out visual state. Although it was easy to find the controls for configuring the debugger (good discoverability), it was impossible to find out exactly _why_ the software would not allow me to do so.

What made this even more frustrating, is that it would have been straight-forward for the software to have shown me an informative tooltip or dialog box when I hovered over or clicked on the disabled controls. This message could have explained shortly why the control was disabled, and what exactly I needed to do to resolve the problem.

If you have or you were planning to use disabled controls in your next project without an easily discoverable (read: right on the disabled control itself) explanation of the reason (and fix) for having disabled them, I would like to say this:


<img alt="JUST... JUST STOP." class="alignnone wp-image-2317 size-full" data-attachment-id="2317" data-comments-opened="1" data-image-description="" data-image-meta='{"aperture":"0","credit":"Picasa","camera":"","caption":"","created_timestamp":"1339193494","copyright":"","focal_length":"0","iso":"0","shutter_speed":"0","title":"","orientation":"1"}' data-image-title="stop-just-stop" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop-300x300.jpg" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg" data-orig-size="358,358" data-permalink="https://cpbotha.net/2016/01/06/user-interface-boo-boo-1-disabled-controls/stop-just-stop/" height="358" sizes="(max-width: 358px) 85vw, 358px" src="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg" srcset="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg 358w, https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop-150x150.jpg 150w, https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop-300x300.jpg 300w" width="358"/>

I’ve singled out Qt Creator due to my experience today, but there are too many examples of this in modern user interfaces. **Hooking up discoverable explanations to disabled controls** is a small effort on the part of the programmer which multiplies to a significant time-saving and thus **value-add for your users**.

 [1]: http://www.qt.io/ide/
