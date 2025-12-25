+++
title = "Daily Head Voices on Friday 2023-12-22"
date = 2023-12-25T18:46:00+02:00
lastmod = 2024-01-01T13:00:02+02:00
tags = ["lifelog", "apple", "applescript", "pandoc", "copilot", "github", "emacs"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

-   Throughout the day, probably spent far too much time fighting with AppleScript to figure out attachments (learned stuff, also that Apple Notes AppleScript is quite broken), and then also some time on ox-pandoc export, as it can embed image attachments as base64, which is what should in theory work for Apple notes (haha...)
-   I used a mix of perplexity (free), bing chat in gpt4 mode and even a bit of you.com to help me, but AppleScript and specifically its application in notes is pretty obscure, with ox-pandoc not very far behind.
-   Did get <https://github.com/zerolfx/copilot.el> working in Emacs -- this has turned out really useful for my most recent emacs-lisp adventures! My config is below in case you find it useful.

<!--listend-->

```emacs-lisp
(use-package copilot
  :ensure t
  :vc (:fetcher "https://github.com/zerolfx/copilot.el.git")
  :config
  ;; only copilot in insert mode
  ;; https://www.irfanhabib.com/2022-04-26-setting-up-github-copilot-in-emacs/
  (customize-set-variable 'copilot-enable-predicates '(evil-insert-state-p))
  ;; binds inspired by https://code.visualstudio.com/docs/editor/github-copilot
  (define-key copilot-completion-map (kbd "<tab>") 'copilot-accept-completion)
  (define-key copilot-completion-map (kbd "TAB") 'copilot-accept-completion)
  (define-key copilot-completion-map (kbd "M-]") 'copilot-next-completion)
  ;; command-right on macOS, windows-right on Linux / Windows
  (define-key copilot-completion-map (kbd "s-<right>") 'copilot-accept-completion-by-word))
```
