---
title: Python 2.6 enabled VTK 5.4 Windows binaries
author: cpbotha
type: post
date: 2009-08-13T21:37:32+00:00
url: /2009/08/13/python-2-6-enabled-vtk-5-4-windows-binaries/
categories:
  - nerd
  - tech
tags:
  - nerd
  - python
  - vtk
  - windows

---
[<img class="alignnone" style="border: 0pt none;" src="http://vtk.org/opensourcelogos/vtk100.png" border="0" alt="" width="456" height="100" />][1]

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  <em>You can always check my <a style="color: #0060ff; text-decoration: underline; padding: 0px; margin: 0px;" title="Latest VTK Windows binaries page." href="http://cpbotha.net/software/latest-vtk-windows-binaries/">Latest VTK Windows binaries page</a> to make sure you have the latest blog posting and hence the latest binaries.  It also links to the &#8220;old&#8221; Python 2.5 VTK 5.4.1 binaries.</em>
</p>

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  I’ve made available my home-baked VTK 5.4.2 Windows binaries.  These have the <a title="Link to new and improved Python exceptions patch." href="http://code.google.com/p/devide/source/detail?spec=svn3800&r=3732">new-and-improved version of my python-exception-patches</a> integrated (more about this in a future post; a serious dead-lock has been fixed and as a side-effect, you can now run multiple VTK pipelines in different threads!) and have been built with Visual Studio 2008 (9.0) SP1 on Windows XP SP3 with full Python 2.6 support.  Get the binaries (or my patched source) from the two links below.  You want the binaries if you want to use VTK from Python.
</p>

  * Binaries: [VTK-5-4-2-Py26-VS9sp1-win32-cpbotha.net.zip][2]
  * Source: [VTK-5-4-2-source-cpbotha.net.zip][3]

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  <strong>IMPORTANT</strong>: you might have to install the MS VS2008 SP1 <a title="Link to MS VS2008 SP redistributable" href="http://www.microsoft.com/downloads/details.aspx?familyid=A5C84275-3B97-4AB7-A40D-3802B2AF5FC2&displaylang=en">vcredist_x86</a> package (free!) if you want to use these DLLs (thanks Jelle for pointing this out).  This might not be necessary if you already have one or more of the MS development environments installed.
</p>

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  <strong>P</strong><strong>lease leave a comment on this blog posting if you use these or just hate them</strong>. It’s almost like postcard-ware, but with blog comments. Please also link to this page and not directly to the download location, thanks!
</p>

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  To use this from Python, you need to add the following to your PATH:
</p>

<ul style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 40px; list-style-type: square; padding: 0px;">
  <li style="margin-top: 0px; margin-right: 0px; margin-bottom: 0.5em; margin-left: 0px; padding: 0px;">
    d:\opt\VTK\bin
  </li>
</ul>

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  You also need to add <strong>all of the above</strong> to PYTHONPATH, as well as the following:
</p>

<ul style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 40px; list-style-type: square; padding: 0px;">
  <li style="margin-top: 0px; margin-right: 0px; margin-bottom: 0.5em; margin-left: 0px; padding: 0px;">
    d:\opt\VTK\lib\site-packages
  </li>
</ul>

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  … where d:\opt is the drive and directory where you unpacked the ZIP file.
</p>

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">
  Once you’ve done this and logged out and in again, “import vtk” should work at the Python prompt. Shameless plug: you can use my free <a style="color: #0060ff; text-decoration: underline; padding: 0px; margin: 0px;" title="envedit homepage" href="../software/envedit">envedit</a> software to do the environment editing. It beats the default XP editing thingy.
</p>

<p style="margin-top: 0px; margin-right: 0px; margin-bottom: 1.5em; margin-left: 0px; padding: 0px;">

 [1]: http://www.vtk.org/
 [2]: http://visualisation.tudelft.nl/~cpbotha/files/vtk_itk/vtk-5.4/VTK-5-4-2-Py26-VS9sp1-win32-cpbotha.net.zip "Link to vtk 5.4.2 python 2.6 win32 binaries"
 [3]: http://visualisation.tudelft.nl/~cpbotha/files/vtk_itk/vtk-5.4/VTK-5-4-2-source-cpbotha.net.zip "Link to patched VTK 5.4.2 source I used to bulid this."
