---
title: nvpy 1.0.0 has been released!
author: cpbotha
type: post
date: 2016-12-02T10:19:40+00:00
url: /2016/12/02/nvpy-1-0-0-has-been-released/
categories:
  - news
tags:
  - note-taking
  - nvpy
  - simplenote

---
Oh happy day!

Last night [I released version 1.0.0][1] of [nvpy][2], a cross-platform (linux, mac, windows) simplenote-syncing note-taking app. nvpy is also my most popular open source baby, at least by github stars and forks.<figure id="attachment_2649" aria-describedby="caption-attachment-2649" style="width: 840px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot.png" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2649" data-permalink="https://cpbotha.net/2016/12/02/nvpy-1-0-0-has-been-released/2016-12-02-115217_1032x679_scrot/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot.png" data-orig-size="1032,679" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="2016-12-02-115217_1032x679_scrot" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot-300x197.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot-1024x674.png" class="size-large wp-image-2649" src="https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot-1024x674.png" alt="Screenshot of nvpy 1.0.0 with a demo database of notes." width="840" height="553" srcset="https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot-1024x674.png 1024w, https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot-300x197.png 300w, https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot-768x505.png 768w, https://cpbotha.net/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot.png 1032w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" /></a><figcaption id="caption-attachment-2649" class="wp-caption-text">Screenshot of nvpy 1.0.0 with a demo database of notes.</figcaption></figure> 

Since I first released nvpy in 2012, [automattic][3] have released their own official open source desktop app for simplenote. Although the official app is prettier (it is electron-based), nvpy is faster and uses a fraction of the RAM (70MB RSS vs 1000MB+ RSS). Furthermore, nvpy&#8217;s syncing is more deterministic: You can see exactly when and how it syncs.

Personally, I use nvpy on my Linux and Mac workstations and laptops, and the official simplenote apps on my Android devices for the text-only notes [I always need to be with me][4].

I am currently planning to write a new sqlite-based storage backend for nvpy, which should greatly speed up its interactive note-searching.

 [1]: https://groups.google.com/forum/#!topic/nvpy/9r3ED7w3axs
 [2]: https://github.com/cpbotha/nvpy
 [3]: https://automattic.com/
 [4]: /2016/01/05/note-taking-strategy-early-2016/
