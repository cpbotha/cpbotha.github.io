---
title: Python-enabled VTK 5.1 and ITK 3.2 Windows binaries
author: cpbotha
type: post
date: 2007-08-02T13:47:17+00:00
url: /2007/08/02/python-enabled-vtk-51-and-itk-32-windows-binaries/
categories:
  - tech

---
_You can always check my [Latest VTK Windows binaries page][1] to make sure you have the latest blog posting and hence the latest VTK binaries._

Get your Python 2.4-enabled VTK 5.1 (Paraview-3-0 branch as of 20070801) and ITK 3.2 Windows binaries by clicking on the following link: [http://visualisation.tudelft.nl/~cpbotha/files/vtk_itk/][2]

**IMPORTANT**: you HAVE TO to install the MS VS2005 [vcredist_x86][3] package (free!) if you want to use these DLLs (thanks Jelle for pointing this out). In future, I might include the relevant assemblies in the downloads, I’ll let you know.

I’ve built these with Visual Studio 2005 (8.0) SP1 for Python 2.4.x (NOT 2.5) on Windows XP SP2. ITK has been built with the brilliant built-in WrapITK support. VTK has been modified with my [python-exception-patches][4] (I hope to commit these to VTK CVS soon). I’ve also rebased all DLL and PYD files so they don’t have to be relocated at run-time, saving you time and memory.

I’m making these available as they might _coincidentally_ scratch someone else’s itch. I have no time to build binaries with your specific configuration requests, so please don’t ask. :)

That being said, **please leave a comment on this blog posting if you use these**. It’s almost like postcard-ware, but with blog comments. Please also link to this page and not directly to the download location, thanks!

To use this from Python, you need to add the following to your PATH:

  * d:\opt\VTK\bin
  * d:\opt\ITK\bin
  * d:\opt\ITK\lib\InsightToolkit\WrapITK\lib

You also need to add **all of the above** to PYTHONPATH, as well as the following:

  * d:\opt\ITK\lib\InsightToolkit\WrapITK\Python
  * d:\opt\VTK\lib\site-packages

… where d:\opt is the drive and directory where you unpacked the two ZIP files.
  
Once you’ve done this and logged out and in again, “import vtk” and “import itk” should work at the Python prompt. Shameless plug: you can use my free [envedit][5] software to do the environment editing. It beats the default XP editing thingy.

**UPDATES**

  * **20071015 M5:** VTK now has Parallel kit built as well.
  * **20070909 M4**: Changed available types in ITK build. It now has: complex float, float, signed short, unsigned long and vector float, for 2 and 3D.
  * **20070905 M3**: Includes fix for extremely obscure progress-event-cancels-VTK-error-exception bug. It’s obscure (as in it was incredibly hard to find) but it could still bite you.
  * **20070829 M2**: I’ve put up new VTK binaries (see the M2 in the filename) that include [my shader fixes][6] and also an updated version of the wxVTKRenderWindowInteractor (from current CVS head) with more fixes to deal with the new VTK/Python exception support.

 [1]: http://cpbotha.net/software/latest-vtk-windows-binaries/ "Latest VTK Windows binaries page."
 [2]: http://visualisation.tudelft.nl/~cpbotha/files/vtk_itk/ "Download link for VTK and ITK binaries."
 [3]: http://www.microsoft.com/downloads/details.aspx?familyid=32BC1BEE-A3F9-4C13-9C99-220B62A191EE&displaylang=en "link to vcredist_x86.exe"
 [4]: http://public.kitware.com/pipermail/vtk-developers/2006-August/004260.html "link to mail concerning python exception patch"
 [5]: http://cpbotha.net/software/envedit "envedit homepage"
 [6]: http://public.kitware.com/pipermail/vtkusers/2007-August/092345.html "link to mail explaining my shader fixes"
