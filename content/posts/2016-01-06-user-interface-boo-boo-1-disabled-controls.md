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

<a href="https://cpbotha.net/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM.png" rel="attachment wp-att-2314" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img data-attachment-id="2314" data-permalink="https://cpbotha.net/2016/01/06/user-interface-boo-boo-1-disabled-controls/screen-shot-2016-01-06-at-4-27-00-pm/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM.png" data-orig-size="760,104" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screen Shot 2016-01-06 at 4.27.00 PM" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM-300x41.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM.png" class="alignnone wp-image-2314 size-full" src="https://cpbotha.net/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM.png" alt="Screen Shot 2016-01-06 at 4.27.00 PM" width="760" height="104" srcset="https://cpbotha.net/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM.png 760w, https://cpbotha.net/wp-content/uploads/2016/01/Screen-Shot-2016-01-06-at-4.27.00-PM-300x41.png 300w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 984px) 61vw, (max-width: 1362px) 45vw, 600px" /></a>

I absolutely, definitely needed to configure the debugger. However, the controls required to do so were disabled, as can be seen by their greyed out visual state. Although it was easy to find the controls for configuring the debugger (good discoverability), it was impossible to find out exactly _why_ the software would not allow me to do so.

What made this even more frustrating, is that it would have been straight-forward for the software to have shown me an informative tooltip or dialog box when I hovered over or clicked on the disabled controls. This message could have explained shortly why the control was disabled, and what exactly I needed to do to resolve the problem.

If you have or you were planning to use disabled controls in your next project without an easily discoverable (read: right on the disabled control itself) explanation of the reason (and fix) for having disabled them, I would like to say this:

<img data-attachment-id="2317" data-permalink="https://cpbotha.net/2016/01/06/user-interface-boo-boo-1-disabled-controls/stop-just-stop/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg" data-orig-size="358,358" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;Picasa&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1339193494&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="stop-just-stop" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop-300x300.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg" class="alignnone wp-image-2317 size-full" src="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg" alt="JUST... JUST STOP." width="358" height="358" srcset="https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop.jpg 358w, https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop-150x150.jpg 150w, https://cpbotha.net/wp-content/uploads/2016/01/stop-just-stop-300x300.jpg 300w" sizes="(max-width: 358px) 85vw, 358px" />

I&#8217;ve singled out Qt Creator due to my experience today, but there are too many examples of this in modern user interfaces. **Hooking up discoverable explanations to disabled controls** is a small effort on the part of the programmer which multiplies to a significant time-saving and thus **value-add for your users**.

 [1]: http://www.qt.io/ide/