---
title: alt.gil.die.die.die
author: cpbotha
type: post
date: 2005-06-15T01:22:49+00:00
url: /2005/06/15/altgildiediedie/
categories:
  - Uncategorized

---
Anyone who knows me even moderately well knows that I adore Python. However, once again it seems that nothing’s perfect. Python uses a global interpreter lock, or GIL, to ensure that multiple threads don’t mess up interpreter state too badly. This means that only the thread that holds the GIL can run the interpreter at any specific moment.

In investigating possibilities for the next generation of [DeVIDE][1], I was considering threadifying the whole deal in order to enable the user to steer processing pipelines whilst they’re processing and in order to detach the GUI completely from the processing backend. However, after constructing [this example][2], that seems to be impossible with the GIL currently used by CPython. Running the example, you’ll note that the VTK pipelines execute sequentially instead of in parallel. Unless I’ve misunderstood something somewhere, I have the GIL to blame for this.

ARGH!

Now I’ll have to look at far more hare-brained schemes to detach everything from everything. I was hoping that the threading thing would work out, as I need to chuck hundreds of megabytes of data around at interactive speeds.

Oh yeah, a pre-emptive little something to the asynchronous-programming-it’s-all-a-state-machine-fanboys: I was implementing state-machines on hardware when you were still dirtying your nappies. Now bite me.

 [1]: http://cpbotha.net/DeVIDE
 [2]: http://visualisation.tudelft.nl/~cpbotha/thingies/PythonGIL_Bad.py
