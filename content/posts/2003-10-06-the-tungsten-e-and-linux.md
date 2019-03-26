---
title: The Tungsten E and Linux
author: cpbotha
type: post
date: 2003-10-06T14:57:51+00:00
url: /2003/10/06/the-tungsten-e-and-linux/
categories:
  - Uncategorized

---
There are a few things you have to remember when trying to keep your pilot synchronised with your Linux workstation. Most of these caveats are due to general Gnome 2.2 shittiness. My opinion that many open source programmers should rather go back to school has just been enforced by this opinion. :)
  
<!--more-->


  
**Testing kernel setup with pilot-xfer**

Make sure your kernel has full support for usb and that you&#8217;ve built usbserial and visor modules as well. Make sure the visor module is installed. Connect your visor with the supplied mini-usb cable, switch it on and tap the sync thingy (that little star in the corner). Now type the following:
  
`<br />
pilot-xfer -p usb:/dev/ttyUSB1 --list<br />
` 
  
You should see a list of all the databases on your palm. If you&#8217;ve gotten this far, you&#8217;ve done well! Make sure you have the latest pilot-link package.

**Backing up with pilot-xfer**
  
If you now try a backup with:
  
`<br />
pilot-xfer -p usb:/dev/ttyUSB1 -s /home/yourname/your/backupdir/<br />
` 
  
You&#8217;ll see your USB stack crash reproducibly when synching ImgFile-Foto or Jpeg-Foto. It will do this with uhci and usb-uhci. This is frustrating.

To get around this, create a file called something like &#8220;excludeList&#8221; and add the following lines:
  
`<br />
ImgFile-Foto<br />
Jpeg-Foto<br />
` 
  
Now try your backup with:
  
`<br />
pilot-xfer -p usb:/dev/ttyUSB1 -e /path/to/excludeList -s /home/yourname/your/backupdir/<br />
` 

**Evolution and gnome-pilot**
  
Now that we have a backup going, step 2 is synching with evolution via gnome-pilot. What a stinking piece of software. Note that, if you don&#8217;t have /proc/bus/usb mounted, gpilotd will crash inexplicably (and without any kind of meanigful hint as to why) every time you try to configure it to use /dev/ttyUSB1 as a usb port. Go GNOME! Idiots. Moral of the story: _make sure your /proc/bus/usb/ is mounted_.

Configure your gpilotd (via the capplet) to use /dev/ttyUSB1 (or whatever the devfs equivalent is) and make sure that the type is set to &#8220;USB&#8221;. Synching should now work in evolution, unless you&#8217;ve been so stupid as to expect the backup conduit to work! Those databases that we&#8217;ve excluded above are screwing us over again&#8230;

Now it seems that gpilotd can be configured to exclude certain databases as well, but this option is nowhere to be found in the GUI. Probably part of Gnome&#8217;s policy of making the best GUI for stupid idiots, i.e. so simple as to be useless. If you go scratching in $HOME/.gnome2/gnome-pilot.d/backup-conduit, you&#8217;ll notice an &#8220;exclude_files&#8221; option. Mostly due to the glaring lack of documentation, I was unable to modify this option and get gpilotd to heed my changes. &#8220;ImgFile-Foto,Jpeg-Foto&#8221; for instance does not work.

So, bye-bye backup conduit. I never liked you anyway.

**The End**
  
Currently I sync my Calendar, Tasks and Contacts with evolution. For backups, I use my own leet [Palm rotating backup Python script][1]. Feel free to abuse it!

 [1]: http://cpbotha.net/files/leet_scripts/palmBackup.tar.gz
