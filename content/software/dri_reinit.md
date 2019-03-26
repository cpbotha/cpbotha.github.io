---
title: dri_reinit
author: cpbotha
type: page
date: 2007-04-10T15:56:32+00:00

---
**This work evolved into the [dri_resume][1] code and was subsequently absorbed into the XFree86 code-base. This page is here for reference purposes.**

This used to be the home of my driReInitKludge. However, Michel Dänzer made a far better patch based on my work and has since started a new branch in DRI CVS for the development of this functionality.

So, I&#8217;m now using this page to distribute binaries of this XFree86 DRI reinit-0-0-1-branch. What makes these drivers different from the normal DRI Radeon drivers is that they re-initialise DRI across each VT switch, meaning that you can do all kinds of neat tricks with X, including (but not limited to) suspending to disc and resuming whilst running DRI (i.e. 3D-accelerated X). There is only one caveat and that is that you should NOT suspend if X is running a 3D application at the time. This is very easy to check for.

Before these changes, DRI XFree86 would break if you attempted suspend/resume, with no exceptions.

In order for suspending/resuming to work, you will have to modify your agpgart driver as well. [agpgart-i845-resume.patch][2]{.external} shows how to do this for the i845 chipset. You&#8217;ll have to do something similar for your own chipset. This makes sure that your AGP chipset is in a somewhat sane state when you resume. You might be able to get away without patching your agpgart by adjusting your suspend script so that it removes the radeon and agpgart modules just before suspending (i.e. after chvt&#8217;ing away from X) and re-inserts them when resuming, before chvt&#8217;ing back to X.

Get the binary drivers [here][3] and install it over an existing XFree86 4.2.0 installation with the included install.sh shell script.

Once you have the patch installed, check the use-count of the radeon module with lsmod. In X it should be 1, switched away to a VT it should be 0.

Once you are running with the modified binaries, change your suspend script so that it checks for the use count of the radeon module and does not suspend if it&#8217;s more than 0. This would mean that X could not release the DRM because some 3D app was running at the time. Example:

<pre>OLDCON=`fgconsole`
# make sure we are on a text VT
chvt 1
# we can't go to sleep if the radeon DRM is still in use
RADEON_USECOUNT=`lsmod | grep radeon | awk {'print $3'}`
if [ $RADEON_USECOUNT -gt 0 ]; then
beep; beep; beep
echo "Radeon DRM in use, not going to suspend!"
chvt $OLDCON
exit 1
fi
# continue with suspend

# do this if you did NOT patch your agpgart (untested)
#rmmod radeon
#rmmod agpgart
.
.
.
# then the RESUME

# do this if you did NOT patch your agpgart (untested)
#modprobe agpgart
#modprobe radeon

chvt $OLDCON</pre>

If you&#8217;re interested in the source, perhaps for historical reasons, you could browse the [download directory][4].

 [1]: /software/dri_resume
 [2]: /files/dri_reinit/agpgart-i845-resume.patch
 [3]: /files/dre_reinit/radeon-reinit-20020804-linux.i386.tar.bz2
 [4]: /files/dri_reinit/ "dri_reinit download dir"