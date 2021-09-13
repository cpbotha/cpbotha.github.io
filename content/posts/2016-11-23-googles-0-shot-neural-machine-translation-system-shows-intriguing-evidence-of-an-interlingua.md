---
title: Google’s 0-shot neural machine translation system shows intriguing evidence of an interlingua
author: cpbotha
type: post
date: 2016-11-23T06:16:06+00:00
url: /2016/11/23/googles-0-shot-neural-machine-translation-system-shows-intriguing-evidence-of-an-interlingua/
categories:
  - microblog
tags:
  - google
  - google brain
  - interlingua
  - neural network
  - tsne
  - visualization
format: aside

---
In [recent research][1] ([full paper also available][2]), researchers from the Google Brain and Google Translate teams have shown intriguing evidence of a so-called _interlingua,_ that is, a language-agnostic common representation of sentences with the same meaning from different languages.

{{< figure src="/wp-content/uploads/2016/11/interlingua_tsne.png" link="https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html" >}}

What I also found interesting about this work (and related to the above finding), is that they’re able to perform translations between language pairs that the system has never trained on.

A further pleasant surprise was seeing how they used the [t-SNE visualization][3] technique to embed the high-dimensionally represented sentences in 2D, in order to study the interlingua phenomenon.

 [1]: https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html
 [2]: https://arxiv.org/abs/1611.04558
 [3]: https://lvdmaaten.github.io/tsne/
