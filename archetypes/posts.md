---
title: "{{ replace .TranslationBaseName "-" " " | title }}"
author: cpbotha
date: {{ .Date }}
draft: true
tags: []
categories: []
type: "post"
---

Post text

<a href="kalbag-sample.png">
<figure>
  {{< img src="kalbag-sample.png" alt="alt text" >}}
  <figcaption>
  This is a fairly long caption, I need to see where it goes. Why can't it be
  nicely typeset? Let's make it a bit longer.
  </figcaption>
</figure>
</a>

and here we continue with the main text.
