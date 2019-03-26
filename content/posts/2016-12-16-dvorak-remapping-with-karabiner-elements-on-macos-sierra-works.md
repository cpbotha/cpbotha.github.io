---
title: Dvorak remapping with Karabiner-Elements on macOS Sierra works!
author: cpbotha
type: post
date: 2016-12-16T09:46:38+00:00
url: /2016/12/16/dvorak-remapping-with-karabiner-elements-on-macos-sierra-works/
categories:
  - howto
tags:
  - dvorak
  - karabiner
  - mac
  - osx
  - sierra

---
<figure id="attachment_2680" aria-describedby="caption-attachment-2680" style="width: 840px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM.png" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2680" data-permalink="https://cpbotha.net/2016/12/16/dvorak-remapping-with-karabiner-elements-on-macos-sierra-works/screen-shot-2016-12-16-at-11-09-32-am/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM.png" data-orig-size="1798,1134" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screen Shot 2016-12-16 at 11.09.32 AM" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-300x189.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-1024x646.png" class="wp-image-2680 size-large" src="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-1024x646.png" width="840" height="530" srcset="https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-1024x646.png 1024w, https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-300x189.png 300w, https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-768x484.png 768w, https://cpbotha.net/wp-content/uploads/2016/12/Screen-Shot-2016-12-16-at-11.09.32-AM-1200x757.png 1200w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" /></a><figcaption id="caption-attachment-2680" class="wp-caption-text">With some config file elbow grease, Karabiner-Elements works wonderfully on macOS Sierra to remap your keyboard to Dvorak.</figcaption></figure> 

I have been using [Karabiner][1] for a while now to remap my keyboard to Dvorak, as the OSX system Dvorak keyboard mapping exposes [a bug in many Java apps][2], including all of the JetBrains development environment tools I use intensively, whereby the keyboard is in fact Dvorak, but all shortcut keys are Qwerty, which is of course tremendously confusing. You can read more about the issue in [this StackOverflow answer][3].

I was postponing the upgrade to macOS Sierra, because Karabiner, fantastic keyboard remapping tool, is unable to function on the new OS due to changed APIs and whatnot.

Fortunately [Takayama Fumihiko][4], awesome hacker behind Karabiner, has been re-implementing his work in a new tool called [Karabiner-Elements][5]. The GUI is not up to pre-Sierra level yet, but the tool works perfectly to solve my Dvorak-remapping (and other) issues!

After upgrading to Sierra, install from the dmg file, start Karabiner-Elements, then copy [`qwerty_to_dvorak.json` from the examples][6] into your `~/.karabiner.d/configuration/` directory and name it `karabiner.json`. It will be immediately picked up, so you&#8217;re typing in Dvorak.

Personally I have also added the relevant lines from the `change_caps_lock_to_left_control.json` and `change_section_key_to_accent_key.json` examples to the `simple_modifications` clause of my `karabiner.json` file. Using caps-lock as control is essential for efficient Emacs use, and that section key at the top-left of the MBP 2015 keyboards should have been backtick / tilde to start with.

 [1]: https://pqrs.org/osx/karabiner/
 [2]: https://bugs.openjdk.java.net/browse/JDK-8022079
 [3]: http://stackoverflow.com/a/31119280/532513
 [4]: https://github.com/tekezo
 [5]: https://github.com/tekezo/Karabiner-Elements
 [6]: https://github.com/tekezo/Karabiner-Elements/blob/master/examples/qwerty_to_dvorak.json
