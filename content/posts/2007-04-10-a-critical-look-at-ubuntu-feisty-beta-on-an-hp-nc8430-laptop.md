---
title: a critical look at ubuntu feisty beta on an hp nc8430 laptop
author: cpbotha
type: post
date: 2007-04-10T14:37:41+00:00
url: /2007/04/10/a-critical-look-at-ubuntu-feisty-beta-on-an-hp-nc8430-laptop/
topsy_short_url:
  - http://is.gd/f5oNp
categories:
  - nerd
  - review
  - tech
tags:
  - 7.04
  - laptop
  - linux
  - nc8430
  - radeon
  - review
  - ubuntu

---
I&#8217;ve been running Linux since 1993 (kernel 0.99-pl13 if I remember correctly) on most of my workstations and servers. I&#8217;ve had my idiot-zealot phase (&#8220;nothing but Linux is good enough&#8221;), but fortunately have left that far behind me. Now I like teasing idiot-zealots with comments about that shareware Loonix thing.

So for the past few laptops, I&#8217;ve been running Windows XP, mostly because this Just Works(tm) on modern laptop hardware. Linux really didn&#8217;t cut it when compared to XP: yes, you could install it without too much trouble, but getting 100% out of your laptop (suspend/resume, **good** power management, full support for modern GPUs, etc) is a different story.

Because XP is getting more scary by the day (WGA things, licensing issues) and Vista promises to be even more scary (binding itself to your motherboard) and because I&#8217;ve been hearing many good things about Ubuntu Feisty (the soon-to-be-released 7.04), I decided to give this a shot on my HP NC8430 laptop (Core Duo 2GHz, ATI X1600, 2G RAM, etc.). Initially I was determined to do this like a &#8220;normal&#8221; user, i.e. no tweaking config files and especially no script writing. I wanted to see how far your average user could get with a state of the art Linux installation on a laptop.

**Installation**

This was quite impressive: I defragmented my NTFS filesystem, booted from the Ubuntu Feisty live CD and did the install. Without getting all cocky about it, the installer resized my NTFS partition, created a new EXT3 partition and installed itself. Colour me impressed.

**General configuration**

After the first boot, I was greeted with a VESA-driven x.org and an incorrect resolution. My laptop screen supports 1680 x 1050. The Gnome Preferences | Screen Resolution applet couldn&#8217;t go higher than 1280 x 1024. I had to break my first rule and edit the x.org configuration file to add the higher resolution. Why is this still necessary? A novice user shouldn&#8217;t need to have to do this!

I also installed the Ubuntu packaged fglrx ATI drivers with the Synaptic package management software, as I depend on good 3D graphics support for my work. The new Restricted Driver Manager helps one to complete this configuration in a user-friendly fashion.

By running &#8220;aticonfig &#8211;set-powerstate 1&#8221;, the GPU can be set to a lower-power mode, leading to a cooler-running laptop, meaning the fans don&#8217;t spin up as often. This command can be added to the gnome startup by adding it to System | Preferences | Sessions. With &#8220;aticonfig &#8211;lsp&#8221; one can query the available powerstates. One can only change the powerstate if a single display is active.

I removed &#8220;quiet&#8221; (but left &#8220;splash&#8221;) from the GRUB config for the default kernel in order to be able to see boot-up messages. These are helpful, especially when things take longer than they should.

**Wireless networking support**

This is the part that really impressed me: With Ubuntu 6.10 (Edgy Eft), I had to jump through all kinds of very user-unfriendly hoops to connect to my WPA wireless network. Feisty Beta simply popped up a pretty dialog box showing me the detected wireless networks and prompted me for the network key when I selected my WPA access point. I was online&#8230; colour me even more impressed!

**Power management**

This is when my jaw dropped ever so slightly (I&#8217;ll get to the &#8220;critical&#8221; part of this look a bit later): I selected suspend to RAM, which the laptop promptly did. When I pressed the power button to resume, I expected the typical black-screen-crashed-laptop syndrome. Instead, my desktop came back and I could continue working. This is a quantum leap in user-friendly Linux!

However, I soon saw that at every third resume (on average) all my _keyboards would be dead_.

It turns out something similar to [this bug][1] applies to my laptop. By adding the necessary suspend/resume hooks as documented in the bug report (so that the i8042 module is removed before suspend and re-installed after resume), the problem seems to have been solved.

Often after resume, my laptop gets stuck in the text console. I have to switch manually to X with Alt-F7. Another suspend/resume glitch is that the CPU Frequency Scaling Monitor gnome applet is stuck on 2GHz for my second core, although the core is running at half that most of the time. In general, things get a bit flaky after resume; often I need to restart X to get back to normal. I could potentially deal with this.

Another disappointing issue is the terrible battery life under Ubuntu Feisty. On Windows, I get more than 4 hours of battery life with average use (wireless network, web browsing, text editing). With Feisty, even after enabling LAPTOP_MODE in /etc/default/acpi-support and putting the GPU in low-power mode as explained above, I get only 2 hours and 40 minutes. This is almost a show stopper.

Out of the box ACPI monitoring support is well-done. With just a few clicks, I could various temperatures and fan speeds on my panel. See the panel at the top of the screen in the screenshot below:

&nbsp;

<p style="text-align: center;">
  <a href="http://picasaweb.google.com/cpbotha/Screenshots/photo#5051808151758926946"><img src="http://lh6.google.com/image/cpbotha/Rhugv5cDdGI/AAAAAAAAAc0/mT09SLVTKkA/s288/cpb_ubuntu_feisty_beta_20070408.jpg" alt="" /></a>
</p>

This also shows the Deskbar applet in action.

**Dynamic multi-monitor support SUCKS**

My laptop has a docking station with an external LCD monitor, resolution 1280 x 1024. The laptop is 1680 x 1050, as I&#8217;ve mentioned. With Windows, (hot) docking / undocking always Just Works. It automatically activates the correct resolution without me having to configure anything. So whenever I resume, I have a working display.

Feisty does not quite get this yet. In fact, Feisty needs some serious clue-bat-based attention&#8230; When I dock or undock and then resume, I have no display, and no way of getting my display back, besides power-cycling the laptop at every dock / undock. I ended up writing [this Python script][2] and binding it to Alt-F5 (for example) so that I would always have a way of activating the _next_ display in the list of connected displays. Oh jeez, even assigning an arbitrary shell command to a global hot key in Gnome is not straight-forward. You have to use gconf as explained on [this page][3]. You can query connected and enabled displays with &#8220;aticonfig &#8211;query-monitor&#8221; and activate any subset with &#8220;aticonfig &#8211;enable-monitor=name1,name2,&#8230;,nameN&#8221;.

**Desktop effects with XGL and Beryl**

Wobbly Windows, you know, these are immensely useful and result in a more productive computing experience. NOT!

They are really very nice though. Most of the desktop effects are more nice to look at than actually useful, except for one: The ExposÃ©-like functionality, called &#8220;Scale&#8221; by Beryl, scales and fits all windows on the current screen so that one can select the window that one wants to select easily.

Because fglrx doesn&#8217;t support the XComposite extension, I could not install AIGLX (Ubuntu default) and had to go for XGL and Beryl. After following [this guide][4] and making sure to use the external Beryl package repository as explained [here][5] (the Ubuntu packages won&#8217;t work in this case, they don&#8217;t have XGL support), I got the whole shebang to work. MAN this is pretty! Check out the screenshot below for Scale in action (there are non-desktop-effect ways of doing this, e.g. kompose or skippy, but none of them are as slick as the desktop effects version):

&nbsp;

<p style="text-align: center;">
  <a href="http://picasaweb.google.com/cpbotha/Screenshots/photo#5051808151758926962"><img src="http://lh6.google.com/image/cpbotha/Rhugv5cDdHI/AAAAAAAAAc8/DMNDclhbAyk/s288/cpb_ubuntu_feisty_beta_scale_20070410b.jpg" alt="" /></a>
</p>

As with most other things in Ubuntu, this functionality is not without its caveats. This is even more flaky with suspending and resuming: after resuming, logging out and in will give you a garbled display. I have to restart X at the GDM login screen to get XGL to work again. There are also some focus issues, especially with the Gnome Deskbar (very useful utility, by the way): pressing the hotkey activates the deskbar, but you can&#8217;t begin to type, as the current window still has the focus. I managed to fix this by setting the Beryl &#8220;Level of Focus Stealing Prevention&#8221; (under general settings) to None. Changing to a higher resolution with the &#8220;Display Resolution&#8221; applet whilst running XGL+Beryl, results in only part of the screen being usable.

**Miscellaneous issues**

  * Palm Pilot synchronisation seems to work out of the box with my Tungsten C, but hangs forever on ToDo synchronisation. Seems it&#8217;s due to [this bug][6].
  * The built-in Texas Instruments SD card reader works out of the box, but does not automount like other removable media. This is either due to the fact that it&#8217;s not seen as removable, or that the driver forgets to assign its parent bus. See [this mail thread][7]. I ended up applying [this workaround][8], involving adding rules to the udev system to pmount the SD card.
  * Gimp doesn&#8217;t understand SMB: URIs, whereas the Gnome Image Viewer does, and gthumb pretends to but doesn&#8217;t.

**Conclusion**

All in all, I&#8217;m positive but not quite convinced yet. The Ubuntu people have done a marvellous job, but Feisty Beta (up to date as of 2007-04-10) doesn&#8217;t quite Just Work(tm) on the HP NC8430. I had to break my rule of editing config files or writing scripts more than once to get it to work to my satisfaction, and still there are problems that would make it difficult to work in Ubuntu full-time: the miserable battery life, the flaky suspend/resume and the really bad dynamic multi-monitor support. That being said, things like the user-friendly WPA support and the flawless install on an NTFS partition are going in the right direction.

**Updates**

  * This post has been linked by OSNews! You can also follow some of the discussion [over there][9].
  * It&#8217;s also on digg (should I say that it&#8217;s been dugg?).Â  See [here][10].
  * Fixed aticonfig lsp/lsb typo, thanks lampshade!
  * My domain has been migrated to a more stable server, some comments may have been lost in the process. If your comment has not appeared yet, _please_ re-submit it.

**PS**

Please comment away, but keep it civilised. I&#8217;ll update the post as we go along, and give credit where credit&#8217;s due.

 [1]: https://launchpad.net/ubuntu/+source/linux-source-2.6.20/+bug/23497 "link to ubuntu feisty bug where keyboard is dead after resume"
 [2]: http://graphics.tudelft.nl/~cpbotha/thingies/aticonfig_switch.py "Python script to switch to NEXT display with aticonfig"
 [3]: http://www.captain.at/howto-gnome-custom-hotkey-keyboard-shortcut.php "binding arbitrary shell commands to global hotkeys in Gnome"
 [4]: http://lhansen.blogspot.com/2006/10/3d-desktop-beryl-and-xgl-on-ubuntu-edgy.html "beryl + xgl on ubuntu and fglrx"
 [5]: http://ubuntuforums.org/showthread.php?t=393678 "More tips on beryl + xgl"
 [6]: https://bugs.launchpad.net/ubuntu/+source/gnome-pilot-conduits/+bug/81170 "feisty pilot todo syncing bug"
 [7]: http://www.nabble.com/SD-card-automounting-t2870318.html "mail thread wrt SD card not automounting"
 [8]: http://www.dau-sicher.de/pmwiki/Main/CardreaderWithUdev "workaround for SD card thingy"
 [9]: http://osnews.com/comment.php?news_id=17663 "Link to this post at OSNews.com."
 [10]: http://digg.com/linux_unix/A_critical_look_at_Ubuntu_Feisty_beta "digg dugg"