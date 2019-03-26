---
title: envedit
author: cpbotha
type: page
date: 2007-02-19T14:29:00+00:00

---
envedit is a Windows Environment Editor. Use it to edit / set all your user and system environment variables, such as the PATH. I made this tool as the built-in Windows editor (Start | Control Panel | System | Advanced | Environment Variables) is definitely one of the worst user interface examples ever created.

envedit is different from other environment editor tools in that it offers two free-form edit windows. Changes to the complete text will be parsed and applied to the Windows environment keys in the registry. See the screenshot below:

<img title="envedit screenshot" src="/files/envedit/envedit-6.3.20-screenshot.png" alt="envedit screenshot" width="512" height="478" align="middle" />

### Quickstart

Download the binary installer (setup) and run it to install the tool. You should now have an envedit icon on your desktop.

Before you begin, always make a backup of your user and system environments by using _File | Save to file [Ctrl-S]_ for both the user and system environments.

The selected environment (USER or SYSTEM) is shown with a blue background. All actions will be performed on the selected environment. After making changes, go to preview mode (_Environment | Preview [F7]_) and check your changes before selecting _Environment | Apply [F8]_. To undo changes (you can only do this if you haven&#8217;t applied yet), use _Environment | Synchronise [F5]_.

You can also try _Tools | Path Edit current variable [F3]_ to bring up the path editor, which will allow you to edit the ;-separated paths line by line, and to make use of the directory and file selection dialogs to replace or insert directory and file paths. When invoking this function, your cursor has to be on a non-empty line in the user or system text edit box.

###  ****Download

The latest release of envedit is 6.3.20. See the [changelog][1] if you&#8217;re interested in the changes since previous versions.

You can download a binary installer (setup exe, this is the easiest), a zip file containing the binaries, or the source code.

  * Binary installer: [envedit-6.3.20-setup.exe][2] (if you don&#8217;t know what to download, just get this one)
  * ZIPped binaries: [envedit-6.3.20.zip][3]
  * Source code: [envedit-6.3.20-source.zip][4] (Python 2.3 or 2.4, Tkinter)

The source code is released under a BSD open-source license, which also means that the binaries are freeware.

### Dependencies

The binary installer includes all its dependencies and should run on a clean Windows installation, i.e. you don&#8217;t have to install any other frameworks whatsoever.

### Development

We have a [Google Code Project Site][5] where you can SVN the latest source or file any bugs that you may come across.

 [1]: http://cpbotha.net/files/envedit/changelog.txt "envedit changelog"
 [2]: http://cpbotha.net/files/envedit/envedit-6.3.20-setup.exe "binary installer"
 [3]: http://cpbotha.net/files/envedit/envedit-6.3.20.zip "zipped binaries"
 [4]: http://cpbotha.net/files/envedit/envedit-6.3.20-source.zip "source code"
 [5]: http://envedit.googlecode.com/ "Google Code projecct site for envedit"
