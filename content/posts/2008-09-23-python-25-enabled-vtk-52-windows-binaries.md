---
title: Python 2.5 enabled VTK 5.2 Windows binaries
author: cpbotha
type: post
date: 2008-09-23T18:28:42+00:00
url: /2008/09/23/python-25-enabled-vtk-52-windows-binaries/
categories:
  - Uncategorized

---
_You can always check my [Latest VTK Windows binaries page][1] to make sure you have the latest blog posting and hence the latest binaries._

I&#8217;ve made available my home-baked VTK 5.2 Windows binaries.  These have my special [python-exception-patches][2] integrated and have been built with Visual Studio 2005 (8.0) SP1 on Windows XP2 with full Python 2.5 support.  Get the binaries (or my patched source) by going [here][3].  You want the binaries if you want to use VTK from Python.

**IMPORTANT**: you might have to install the MS VS2005 [vcredist_x86][4] package (free!) if you want to use these DLLs (thanks Jelle for pointing this out).  This might not be necessary if you already have one or more of the MS development environments installed.

**P****lease leave a comment on this blog posting if you use these or just hate them**. It’s almost like postcard-ware, but with blog comments. Please also link to this page and not directly to the download location, thanks!

To use this from Python, you need to add the following to your PATH:

  * d:\opt\VTK\bin

You also need to add **all of the above** to PYTHONPATH, as well as the following:

  * d:\opt\VTK\lib\site-packages

… where d:\opt is the drive and directory where you unpacked the ZIP file.
  
Once you’ve done this and logged out and in again, “import vtk” should work at the Python prompt. Shameless plug: you can use my free [envedit][5] software to do the environment editing. It beats the default XP editing thingy.

 [1]: http://cpbotha.net/software/latest-vtk-windows-binaries/ "Latest VTK Windows binaries page."
 [2]: http://public.kitware.com/pipermail/vtk-developers/2006-August/004260.html "Mailing list mail with my python exception patch work."
 [3]: http://visualisation.tudelft.nl/~cpbotha/files/vtk_itk/vtk-5.2/ "Link to VTK 5.2 windows binaries download"
 [4]: http://www.microsoft.com/downloads/details.aspx?familyid=32BC1BEE-A3F9-4C13-9C99-220B62A191EE&displaylang=en "link to vcredist_x86.exe"
 [5]: ../software/envedit "envedit homepage"