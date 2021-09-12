---
title: An Even More Ultimate Boot Disk!
author: cpbotha
type: post
date: 2010-05-24T14:29:09+00:00
url: /2010/05/24/an-even-more-ultimate-boot-disk/
categories:
  - howto
  - nerd
  - tech
tags:
  - boot
  - flash
  - knoppix
  - linux
  - ubcd
  - ubuntu
  - ultimatebootcd
  - usb

---
In this short howto, I show you how to combine the Ultimate Boot CD (UBCD) with both Knoppix 6.2.1 and Ubuntu 10.04 onto a single USB stick to create An Even More Ultimate Boot Disk (EMUBD)!

<p style="text-align: center;">
<a data-rel="lightbox-image-0" data-rl_caption="" data-rl_title="" href="http://cpbotha.net/wp-content/uploads/2010/05/emubd_logo_400.jpg" title=""><img alt="" class="aligncenter size-full wp-image-910" data-attachment-id="910" data-comments-opened="1" data-image-description="" data-image-meta='{"aperture":"0","credit":"","camera":"","caption":"","created_timestamp":"0","copyright":"","focal_length":"0","iso":"0","shutter_speed":"0","title":""}' data-image-title="emubd_logo_400" data-large-file="https://cpbotha.net/wp-content/uploads/2010/05/emubd_logo_400.jpg" data-medium-file="https://cpbotha.net/wp-content/uploads/2010/05/emubd_logo_400-300x135.jpg" data-orig-file="https://cpbotha.net/wp-content/uploads/2010/05/emubd_logo_400.jpg" data-orig-size="400,181" data-permalink="https://cpbotha.net/2010/05/24/an-even-more-ultimate-boot-disk/emubd_logo_400/" height="181" sizes="(max-width: 400px) 85vw, 400px" src="http://cpbotha.net/wp-content/uploads/2010/05/emubd_logo_400.jpg" srcset="https://cpbotha.net/wp-content/uploads/2010/05/emubd_logo_400.jpg 400w, https://cpbotha.net/wp-content/uploads/2010/05/emubd_logo_400-300x135.jpg 300w" style="border: none;" title="emubd_logo_400" width="400"/></a>
</p>

[UBCD][1] is a bootable CD image that’s fantastic if you’re trying to save grandma’s PC from a certain death, as it contains a number of different bootable utilities for testing memory, testing and low-level repair of hard drives, partition repair, antivirus and so forth. It even contains Parted Magic, a compact linux distribution for fixing partitions, amongst others.

[Knoppix][2] is the swiss knife of live linux distributions, and [Ubuntu][3] 10.04 is probably the slickest distribution out there at the moment. Both of these can be ran live from your USB disc, so they don’t have to touch your hard drive.  However, both of them are also able to install to your hard disc if you so choose.

To me it seemed logical to combine **all three of these elements onto the single USB flash drive** that I carry on my keychain, as I know of many grandmas with broken PCs…

Let’s go!

  1. make sure the single FAT32 partition on your USB stick is bootable (use command ‘a’ in linux fdisk) and large enough (you’ll need just a bit less than 2G).
  2. mount your flash drive on a directory, henceforth referred to as FLASH_MNT.
  3. copy all files from the ubcd5 iso into a directory, henceforth referred to as CUSTOM_UBCD5.
  4. mount the ubuntu 10.04 i386 iso on a directory, henceforth referred to as LUCID_MNT
  5. mount the knoppix iso on a directory, henceforth referred to as KNOPPIX_MNT.
  6. copy necessary boot files from the ubuntu ISO to UBCD: <pre class="brush: bash; title: ; notranslate" title="">mkdir CUSTOM_UBCD5/ubcd/custom/lucid
cp LUCID_MNT/casper/vmlinuz LUCID_MNT/casper/initrd.lz CUSTOM_UBCD5/ubcd/custom/lucid
</pre>

  7. copy ubuntu-10.04-desktop-i386.iso to your flash disk: <pre class="brush: bash; title: ; notranslate" title="">mkdir /FLASH_MNT/isos
cp ubuntu-10.04-desktop-386.iso /FLASH_MNT/isos/
</pre>

  8. Knoppix can’t be booted directly from its iso like Ubuntu, so we have to copy the actual contents of the ISO to your flash: <pre class="brush: bash; title: ; notranslate" title="">cp -r KNOPPIX_MNT/KNOPPIX to FLASH_MNT/
cp -r KNOPPIX_MNT/boot/isolinux to FLASH_MNT/KNOPPIX/isolinux
</pre>

  9. replace FLASH_MNT/KNOPPIX/isolinux/isolinux.cfg with the isolinux.cfg at the bottom of this post. (It’s the same file, except that “KERNEL linux” is replaced with “KERNEL /KNOPPIX/isolinux/linux”, “initrd=minirt.gz” with “initrd=/KNOPPIX/isolinux/minirt.gz”, F1, F2, F3 and DISPLAY paths all fixed, e.g. “F2 f2” becomes “F2 /KNOPPIX/f2” and finally all instances of “quiet” removed)
 10. Now replace CUSTOM_UBCD5/ubcd/custom/custom.cfg with the custom.cfg at the bottom of this post.
 11. copy all files from CUSTOM_UBCD5 to your usb flash disk: <pre class="brush: bash; title: ; notranslate" title="">cp -r CUSTOM_UBCD5/* FLASH_MNT/
</pre>

 12. Finally, make the whole thing bootable with the following invocation. It’s really important that you replace /dev/sdX1 with the correct device for your flash disk. To see what this is, type “mount” and see the device associated with your FLASH_MNT. <pre class="brush: bash; title: ; notranslate" title="">cd FLASH_MNT
sudo ./ubcd/tools/linux/ubcd2usb/syslinux -s -d /boot/syslinux /dev/sdX1
</pre>

You’re done. You should now be able to boot with your EMUBD! Knoppix and Ubuntu can be found under “User defined”.

Here are those files that you’ll need. First **FLASH_MNT/KNOPPIX/isolinux/isolinux.cfg**:

<pre class="brush: bash; title: ; notranslate" title="">DEFAULT knoppix
APPEND ramdisk_size=100000 lang=en vt.default_utf8=0 apm=power-off vga=0x311 initrd=/KNOPPIX/isolinux/minirt.gz nomce loglevel=0 tz=localtime
TIMEOUT 50
# TOTALTIMEOUT 20
# KBDMAP german.kbd
PROMPT 1
F1 /KNOPPIX/isolinux/boot.msg
F2 /KNOPPIX/isolinux/f2
F3 /KNOPPIX/isolinux/f3
DISPLAY /KNOPPIX/isolinux/boot.msg
LABEL adriane
KERNEL /KNOPPIX/isolinux/linux
APPEND ramdisk_size=100000 lang=en vt.default_utf8=0 apm=power-off vga=0x311 initrd=/KNOPPIX/isolinux/minirt.gz nomce loglevel=0 tz=localtime adriane
LABEL knoppix
KERNEL /KNOPPIX/isolinux/linux
APPEND ramdisk_size=100000 lang=en vt.default_utf8=0 apm=power-off vga=791 initrd=/KNOPPIX/isolinux/minirt.gz nomce loglevel=0 tz=localtime
LABEL fb1024x768
KERNEL /KNOPPIX/isolinux/linux
APPEND ramdisk_size=100000 lang=en vt.default_utf8=0 apm=power-off vga=791 xmodule=fbdev initrd=/KNOPPIX/isolinux/minirt.gz nomce loglevel=0 tz=localtime
LABEL fb1280x1024
KERNEL /KNOPPIX/isolinux/linux
APPEND ramdisk_size=100000 lang=en vt.default_utf8=0 apm=power-off vga=794 xmodule=fbdev initrd=/KNOPPIX/isolinux/minirt.gz nomce loglevel=0 tz=localtime
LABEL fb800x600
KERNEL /KNOPPIX/isolinux/linux
APPEND ramdisk_size=100000 lang=en vt.default_utf8=0 apm=power-off vga=788 xmodule=fbdev initrd=/KNOPPIX/isolinux/minirt.gz nomce loglevel=0 tz=localtime
LABEL memtest
KERNEL memtest
APPEND foo
LABEL dos
KERNEL memdisk
APPEND initrd=balder.img
LABEL failsafe
KERNEL /KNOPPIX/isolinux/linux
APPEND ramdisk_size=100000 lang=en vt.default_utf8=0 vga=normal atapicd nosound noapic nolapic noacpi pnpbios=off acpi=off nofstab noscsi nodma noapm nousb nopcmcia nofirewire noagp nomce nonetwork nodhcp xmodule=vesa initrd=/KNOPPIX/isolinux/minirt.gz
</pre>

… and then **CUSTOM_UBCD5/ubcd/custom/custom.cfg**:

<pre class="brush: bash; title: ; notranslate" title="">MENU INCLUDE /ubcd/menus/syslinux/defaults.cfg
UI /boot/syslinux/menu.c32

# option to be able to go back to the main menu
LABEL -
MENU LABEL ..
COM32 /boot/syslinux/menu.c32
APPEND /ubcd/menus/syslinux/main.cfg

# this clause will boot directly from the ubuntu iso
LABEL ubuntulive
MENU LABEL Ubuntu 10.04 i386 Desktop LIVE
LINUX /ubcd/custom/lucid/vmlinuz
INITRD /ubcd/custom/lucid/initrd.lz
APPEND boot=casper iso-scan/filename=/isos/ubuntu-10.04-desktop-i386.iso --

# and this one will chain into the knoppix boot setup
LABEL knoppix
MENU LABEL Knoppix 6.2.1 LIVE
CONFIG /KNOPPIX/isolinux/isolinux.cfg
</pre>

**Post scriptum**

  * The instructions in this post are derived from the UBCD linux documentation and various forum posts.  Credits to their authors!
  * If you _don’t want Knoppix_ on your bootable USB and you have a Windows computer, you could also use [MultiBootISOS][4] to add multiple ISOs to a USB boot disk.

 [1]: http://ultimatebootcd.com/ "Ultimate Boot CD website"
 [2]: http://www.knoppix.net/ "Knoppix website"
 [3]: http://www.ubuntu.com/ "Ubuntu website"
 [4]: http://www.pendrivelinux.com/boot-multiple-iso-from-usb-multiboot-usb/ "Link to post explaining MultiBootISOs"
