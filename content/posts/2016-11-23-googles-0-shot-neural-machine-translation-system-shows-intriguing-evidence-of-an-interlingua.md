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

[<img data-attachment-id="2596" data-permalink="https://cpbotha.net/2016/11/23/googles-0-shot-neural-machine-translation-system-shows-intriguing-evidence-of-an-interlingua/interlingua_tsne/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/11/interlingua_tsne.png" data-orig-size="1024,548" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="interlingua_tsne" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/11/interlingua_tsne-300x161.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/11/interlingua_tsne-1024x548.png" class="alignnone wp-image-2596 size-large" src="https://cpbotha.net/wp-content/uploads/2016/11/interlingua_tsne-1024x548.png" width="840" height="450" srcset="https://cpbotha.net/wp-content/uploads/2016/11/interlingua_tsne.png 1024w, https://cpbotha.net/wp-content/uploads/2016/11/interlingua_tsne-300x161.png 300w, https://cpbotha.net/wp-content/uploads/2016/11/interlingua_tsne-768x411.png 768w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" />][1]

What I also found interesting about this work (and related to the above finding), is that they&#8217;re able to perform translations between language pairs that the system has never trained on.

A further pleasant surprise was seeing how they used the [t-SNE visualization][3] technique to embed the high-dimensionally represented sentences in 2D, in order to study the interlingua phenomenon.

 [1]: https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html
 [2]: https://arxiv.org/abs/1611.04558
 [3]: https://lvdmaaten.github.io/tsne/
