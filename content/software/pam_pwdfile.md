---
title: pam_pwdfile
author: cpbotha
type: page
date: 2007-04-10T22:13:40+00:00

---
Timo Weingärtner has graciously offered to take over the maintenance of pam_pwdfile. Its development will henceforth be hosted at [https://github.com/tiwe-de/libpam-pwdfile][1].

# Old page contents follows

PAM, or pluggable authentication modules, is a very effective method by which applications can abstract the way that they authenticate and authorize users. Using PAM for example, a whole system can be switched from normal /etc/passwd to shadow passwords without recompiling a single binary, as was the case with older *ix systems. Linux being my OS of choice, I have had most contact with Linux-PAM, as maintained by Andrew Morgan. Please see the Linux PAM pages at <http://www.us.kernel.org/pub/linux/libs/pam/>.

We required a Linux PAM module for authenticating using arbitrary password files containing username:crypted\_password pairs, and this was not yet available for Linux PAM. As is the way with nicely open operating systems, I was able to put one together quickly, and you can get the source here. Since then, patches for extending functionality have also been contributed and integrated with pam\_pwdfile. You can use this module to have different sets of passwords for each of the PAM-based services on your systems.

This module is available as part of Debian, where it is known as [libpam-pwdfile][2]{.external}. It also exists in the FreeBSD ports collection.

Warwick Duncan has written a very useful utility (command-line and CGI) to manage password files that can be used by pam_pwdfile. You can read all about chpwdfile and download it from the [chpwdfile homepage][3]{.external}! (Hmmm, it seems that the chpwdfile site has dropped off the edge of the internet. I&#8217;ve mirrored the source tarball of chpwdfile [here][4]{.external}. Remember that you can also use the apache htpasswd utility to manage your password files from the command line.)

 [1]: https://github.com/tiwe-de/libpam-pwdfile "pam-pwdfile github"
 [2]: http://packages.debian.org/unstable/admin/libpam-pwdfile.html
 [3]: http://eclipse.che.uct.ac.za/chpwdfile/
 [4]: http://cpbotha.net/files/mirror/chpwdfile-0.24.tar.gz