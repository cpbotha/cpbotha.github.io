---
title: Fix the unusable window resize border in Gnome Flashback Metacity on Ubuntu
author: cpbotha
type: post
date: 2016-01-22T09:04:25+00:00
url: /2016/01/22/fix-the-unusable-window-resize-border-in-gnome-flashback-metacity-on-ubuntu/
categories:
  - howto
tags:
  - gnome flashback
  - metacity
  - nerd
  - thin
  - ubuntu
  - window border

---
On Ubuntu I mostly use [Gnome Flashback with Metacity][1], along with the brilliant [Synapse app starter / file finder][2]. I do this in spite of having a beefy NVIDIA GPU in this Core i7 workstation, because the OpenGL compositing on this 2560×1440 display makes video conferencing really slow, and because I do OpenGL development and need to have maximum performance for the app I’m working on.

However, it irritated me to no end that the window borders were so thin that I was not able to grab them for a resize. Adding insult to injury, there were only the four standard themes in Settings | Appearance, namely Adwaita, Ambiance, Radiance and High Contrast, none of which has usable borders.

The solution is to use the Gnome Tweak Tool (package gnome-tweak-tool) to change the Window theme to something with better borders. I used _Watercolor_ (from the metacity-themes package), and set the rest up as follows on the appearance tab:

<img alt="tweak-tool-theme" class="alignnone size-full wp-image-2342" data-attachment-id="2342" data-comments-opened="1" data-image-description="" data-image-meta='{"aperture":"0","credit":"","camera":"","caption":"","created_timestamp":"0","copyright":"","focal_length":"0","iso":"0","shutter_speed":"0","title":"","orientation":"0"}' data-image-title="tweak-tool-theme" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/tweak-tool-theme.png" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/tweak-tool-theme-300x116.png" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/tweak-tool-theme.png" data-orig-size="732,283" data-permalink="https://cpbotha.net/2016/01/22/fix-the-unusable-window-resize-border-in-gnome-flashback-metacity-on-ubuntu/tweak-tool-theme/" height="283" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 984px) 61vw, (max-width: 1362px) 45vw, 600px" src="https://cpbotha.net/wp-content/uploads/2016/01/tweak-tool-theme.png" srcset="https://cpbotha.net/wp-content/uploads/2016/01/tweak-tool-theme.png 732w, https://cpbotha.net/wp-content/uploads/2016/01/tweak-tool-theme-300x116.png 300w" width="732"/>

Once this is done, your window borders should look like this:

<img alt="watercolor-window-borders" class="alignnone size-full wp-image-2344" data-attachment-id="2344" data-comments-opened="1" data-image-description="" data-image-meta='{"aperture":"0","credit":"","camera":"","caption":"","created_timestamp":"0","copyright":"","focal_length":"0","iso":"0","shutter_speed":"0","title":"","orientation":"0"}' data-image-title="watercolor-window-borders" data-large-file="https://cpbotha.net/wp-content/uploads/2016/01/watercolor-window-borders.png" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/01/watercolor-window-borders-300x205.png" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/01/watercolor-window-borders.png" data-orig-size="400,273" data-permalink="https://cpbotha.net/2016/01/22/fix-the-unusable-window-resize-border-in-gnome-flashback-metacity-on-ubuntu/watercolor-window-borders/" height="273" sizes="(max-width: 400px) 85vw, 400px" src="https://cpbotha.net/wp-content/uploads/2016/01/watercolor-window-borders.png" srcset="https://cpbotha.net/wp-content/uploads/2016/01/watercolor-window-borders.png 400w, https://cpbotha.net/wp-content/uploads/2016/01/watercolor-window-borders-300x205.png 300w" width="400"/>

Now you can resize your windows again, AND you can enjoy the snappiness of Gnome Flashback with Metacity!

 [1]: http://www.webupd8.org/2014/04/how-to-install-and-tweak-gnome.html
 [2]: http://lifehacker.com/5704221/synapse-is-a-super-fast-tightly-integrated-application-launcher-for-linux
