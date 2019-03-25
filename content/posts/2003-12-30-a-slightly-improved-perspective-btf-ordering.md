---
title: A slightly improved perspective BTF ordering
author: cpbotha
type: post
date: 2003-12-30T18:26:18+00:00
url: /2003/12/30/a-slightly-improved-perspective-btf-ordering/
categories:
  - Uncategorized

---
Finding a single BTF (back-to-front) ordering for perspectively rendered volumes without sorting is more difficult than it sounds. See what happens when we make use of a traditional BTF (Frieder et al., 1985): <a href="http://visualisation.tudelft.nl/~cpbotha/thingies/perspectiveBTF.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">it breaks badly.</a>

Ed Swan came up with a super-elegant constructive proof for a perspective BTF ordering that works (Swan, 1998). However, his &#8220;PBTF&#8221; rendering and its proof assume that voxels are infinitesimally small. As is very often the case, voxels can have significant size, and volume resolution is often lower than screen resolution, which results in disturbing rendering artefacts. Ed&#8217;s algorithm is still a great improvement: <a href="http://visualisation.tudelft.nl/~cpbotha/thingies/perspectivePBTF.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title="">see here, but note the artefact.</a>

This problem has been cooking in the back of my head for quite a while now. I think I might&#8217;ve solved it: <a href="http://visualisation.tudelft.nl/~cpbotha/thingies/perspectiveIPPBTF.png" data-rel="lightbox-image-2" data-rl\_title="" data-rl\_caption="" title="">click here</a>.

ADDENDUM:
  
Some more samples: <a href="http://visualisation.tudelft.nl/~cpbotha/thingies/faceonPBTF.png" data-rel="lightbox-image-3" data-rl\_title="" data-rl\_caption="" title="">before</a> and <a href="http://visualisation.tudelft.nl/~cpbotha/thingies/faceonIPPBTF.png" data-rel="lightbox-image-4" data-rl\_title="" data-rl\_caption="" title="">after</a>.