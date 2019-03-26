---
title: dri_resume
author: cpbotha
type: page
date: 2007-04-10T15:57:43+00:00

---
**IMPORTANT NOTE**: My patches have finally found their way into the XFree86 CVS (post 4.3) as well as DRI CVS. The version in DRI CVS has been greatly cleaned-up by Michel Daenzer and will probably propagate its way back into XFree86. What all of this means is that all current releases of XFree86 and X.org include the Radeon suspend/resume functionality, and as is the case with software, most users won&#8217;t even know it&#8217;s there.

In short: **This page is only here for reference purposes. The work documented here has been absorbed into the relevant repositories.**

Below follows the original text of this webpage:

* * *

With the software available at this page, you can suspend from / resume to DRI-capable (i.e. hardware 3D-accelerated) XFree86 for the Radeon, even with 3D apps running.

Suspending / resuming DRI-capable XFree86 used to be impossible, until I made the infamous [dri_reinit][1] kludge which allowed this if no 3D apps were running at the time. However, what you find on this page is a new solution and the best solution at the moment if all you&#8217;re interested in is suspending/resuming DRI-capable XFree86. It most definitely allows suspending / resuming even with running 3D applications.

In order to make this code work, you first have to make changes to your agpgart similar to those in the [agpgart-i845-resume.patch][2]{.external}. If you have an Intel 845 chipset, you&#8217;re in luck as you can just use this patch. If not, have a look at what it does (simply makes sure that the resume hook calls the configure hook) and do the same for your chipset. IMPORTANT: This patch (and code similar to it) has been making its way into kernels everywhere. 2.4.20 will have it integrated, Florent&#8217;s v14 swsusp patch has something similar already included for all intel chipsets, 2.5.xx has it integrated AFAIK. The bottom-line is: check your source before blindly making changes. If this is confusing you, you can ask me for help.

Thomas Grossmann has contributed an agpgart patch for via chipsets. You can download it by clicking [here][3]{.external}.

Once you&#8217;ve done this, you can either download my modified binary Radeon drivers or you can patch and build your own XFree86. In the binary case, you have three versions to choose from: one for 4.2 XFree86 and two for 4.3 or later XFree86.

## Binaries {#head-803192bb2f51215eb848dcddd9706905dfa5677e}

If you&#8217;re running a 4.2.x series XFree86, get [this package][4]{.external} (patched 20021012 DRI CVS snapshot, equivalent to v5; v6 or later CAN&#8217;T be installed over an existing 4.2.x installation) and install it over an existing XFree86 4.2.x installation with the included install.sh shell script.

If you&#8217;re running a 4.3 (or later) XFree86, I have two different sets of binary drivers on offer.

  * The first set (my preferred) is built from DRI CVS (20030405). Download the tarball [here][5]{.external}. This fixes a number of bugs that still exist in stock 4.3.0.
  * The second set is built from stock XFree86 version 4.3.0. Get it [here][6]{.external}.

## Important notes {#head-e6884c23c0b7b7976cc439bc754c85a21eaf48ef}

**NOTE1:** You have to switch VTs away from X (with e.g. chvt) at suspend time and switch back at resume time for this to work.

**NOTE2:** Unlike the driReinit patch, you do NOT have to check for the use-count on the radeon module before suspending, just go ahead.

**NOTE3:** It seems that the swsusp code doesn&#8217;t correctly restore all MTRRs: in your suspend/resume script, do something similar to what I do at the end of my script. Replace the addresses and sizes with what you see when you do a &#8220;cat /proc/mtrr&#8221; on your system. This is not crucial and you should only do it if you see a 2D slow down during full screen repainting (at virtual desktop switches for instance). It also seems (from the changelog) that swsusp v17 is restoring MTRRs now. I haven&#8217;t been able to test this yet.

**NOTE4:** I am using this code along with kernel 2.4.21-pre3, swsuspv16 and ACPI20030109.

## Source {#head-a80ddf968c653a435811e74a11ec657c0fe521de}

If you prefer patching the source yourself, or you have a 8500 (r200 &#8211; the patch will work for this as well, but my binaries don&#8217;t include it), download and apply [xfree86-dri-resume-v8.patch][7] to your XFree86 source before building. It should work on both XFree86 and DRI source trees.

My modifications have been submitted to XFree86: they should be merged any day now&#8230;

  * Changes in v8: Nothing, just applies cleanly to XFree86 4.3.0 RC 1
  * Changes in v7: Merged with XFree86 CVS main tree.
  * Changes in v6: Merged with post XFree86 4.2.99 merge DRI tree.
  * Changes in v5: Adapted IOCTL changes in DRI tree.
  * Changes in v4: Suspending/resuming XVideo is now supported.

 [1]: http://cpbotha.net/software/dri_reinit/ "dri_reinit page"
 [2]: /files/dri_reinit/agpgart-i845-resume.patch
 [3]: /files/dri_resume/contrib/agpgart-via-resume.patch
 [4]: /files/dri_resume/radeon-cpbotha-20021012-linux.i386.tar.bz2
 [5]: /files/dri_resume/radeon-cpbotha-20030405-linux.DRI.i386.tar.bz2
 [6]: /files/dri_resume/radeon-cpbotha-20030302-linux.xfree86-4.3.0.i386.tar.bz2
 [7]: /files/dri_resume/xfree86-dri-resume-v8.patch