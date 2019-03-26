---
title: vtkFlRenderWindowInteractor
author: cpbotha
type: page
date: 2007-03-03T21:36:31+00:00

---
vtkFlRenderWindowInteractor is a VTK class (actually FLTK too, but it helps to think of it as VTK) that enables VTK to render to and interact with your FLTK application. It is based on code by David Pont (the code was then called FlvtkInteractorWindow) which in its turn was partly based on the wxVTK code by David D. Marshall and Brian Todd. I reworked the code extensively to be simpler, more robust and bug-free(tm). It should always be available from [http://cpbotha.net/vtkFlRenderWindowInteractor.html][1] .

The main idea behind this class is to be as simple and robust as possible. It fulfils one purpose and that&#8217;s to enable you to write applications with FLTK and VTK. It is possible to have multiple VTK renderings (all active) in your FLTK application, each with its own independent working VTK interactorstyle. You can also add custom interactorstyles, just like with any standard VTK interactor. Picking also works fine, thank you.

This code has been successfully tested on Linux, Irix, Windows and many of the other platforms supported by ITK, as the vtkFlRWI is extensively used in the InsightApplications component of ITK.

**Downloads**

The current version is 1.02. You can download a source and example tarball by clicking [here][2]{.external}. Read the [<span class="external">changelog</span>][3] for a detailed description of changes.

The vtkFlRenderWindowInteractor project development is hosted by Google Code.  Go to [our project page][4] to checkout the latest development source or to file a bug!

 [1]: http://cpbotha.net/software/vtkFlRenderWindowInteractor "vtkFlRenderWindowInteractor home page"
 [2]: http://cpbotha.net/files/vtkFlRenderWindowInteractor/vtkFlRenderWindowInteractor-1.02.tar.gz
 [3]: http://code.google.com/p/vtkflrenderwindowinteractor/source/browse/trunk/changelog?r=78 "Changelog for release 1.02"
 [4]: http://code.google.com/p/vtkflrenderwindowinteractor/ "Google Code project page"