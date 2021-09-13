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

Last night [I released version 1.0.0][1] of [nvpy][2], a cross-platform (linux, mac, windows) simplenote-syncing note-taking app. nvpy is also my most popular open source baby, at least by github stars and forks.
{{< figure src="/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot-1024x674.png" link="/wp-content/uploads/2016/12/2016-12-02-115217_1032x679_scrot.png" caption="Screenshot of nvpy 1.0.0 with a demo database of notes.">}} 

Since I first released nvpy in 2012, [automattic][3] have released their own official open source desktop app for simplenote. Although the official app is prettier (it is electron-based), nvpy is faster and uses a fraction of the RAM (70MB RSS vs 1000MB+ RSS). Furthermore, nvpy’s syncing is more deterministic: You can see exactly when and how it syncs.

Personally, I use nvpy on my Linux and Mac workstations and laptops, and the official simplenote apps on my Android devices for the text-only notes [I always need to be with me][4].

I am currently planning to write a new sqlite-based storage backend for nvpy, which should greatly speed up its interactive note-searching.

 [1]: https://groups.google.com/forum/#!topic/nvpy/9r3ED7w3axs
 [2]: https://github.com/cpbotha/nvpy
 [3]: https://automattic.com/
 [4]: /2016/01/05/note-taking-strategy-early-2016/
