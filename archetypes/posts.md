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


<figure>
    <a href="kalbag-sample.png">
    <!-- uncomment, move < to be adjacent to double brace -->
    <!-- {{ < img src="blabla.jpg" alt="trolo" > }} -->
    </a>
    <figcaption>
    This is a fairly long caption, I need to see where it goes. Why can't it be
    nicely typeset? Let's make it a bit longer.
    </figcaption>
</figure>


and here we continue with the main text.
