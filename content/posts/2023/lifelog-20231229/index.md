+++
title = "Daily Head Voices on Friday 2023-12-29"
date = 2023-12-31T12:18:00+02:00
lastmod = 2023-12-31T17:29:04+02:00
tags = ["lifelog", "clarence drive", "sivers", "vim", "evil-mode", "emacs"]
categories = ["lifelog"]
draft = false
author = "Charl P. Botha"
org = true
+++

-   First time back on the [Clarence Drive coastal route](https://www.mountainpassessouthafrica.co.za/find-a-pass/western-cape/item/95-clarence-drive,-gordons-bay.html) after the floods. As beautiful as ever.
-   Derek Sivers's walk and talk: 100km through Northern Thailand over 7 days with interesting folks. See <https://sive.rs/wt>
-   According to my notes, it was 2023-09-23 when I had started giving [evil-mode](https://github.com/emacs-evil/evil) a solid bash again. Last time was... &lt;checks notes&gt;... 2017-09-18. Strange that it was also in September! (My previous vim-proper era probably around 2007, but I'm guessing). Anyways, it now feels like it was the right choice to try again now. My emacs agility is almost back to what it was before the switch, and with some of the vim interactions now trained into muscle-memory, there are many more places where that's turning out to be useful, which was a large part of the motivation for this experiment.


## My evil-mode config {#my-evil-mode-config}

As per special request by Keegan below, here is my mostly by-the-book `evil-mode` config, part of my vanilla-Emacs _ball-of-config_:

```emacs-lisp
(use-package evil
  :ensure t
  ;;:disabled t
  :init
  ;; evil-collection wants this set to nil
  (setq evil-want-keybinding nil)
  ;; on 2023-10-22 trying out visual-line-mode in orgmode
  ;; this setting means j/k e.g. will navigate displayed lines not true lines
  (setq evil-respect-visual-line-mode t)
  :config
  ;; use 'visual instead of 'relative to ignore collapsed / hidden org-mode drawers
  ;; on 2023-11-20: However, I would like to count visual wrapped lines as a single line, but I need 'visual
  ;; here else it incorrectly handles collapsed drawers, just like some of the folks below:
  ;; https://www.reddit.com/r/emacs/comments/nwwlx0/displaying_relative_line_numbers_over_folds_in/
  ;; and so I'm forced to evil-respect-visual-line-mode
  (setq display-line-numbers-type 'visual) ;; 'relative, 'visual, 't, nil
  (setq display-line-numbers-grow-only t)

  (defun display-line-numbers--turn-on ()
    "Turn on line numbers except for certain major modes. "
    (unless (or (minibufferp)
                (member major-mode '(pdf-view-mode)))
      (display-line-numbers-mode)))

  (global-display-line-numbers-mode)


  (global-display-line-numbers-mode 1)
  (evil-set-undo-system 'undo-tree)
  ;; set leader key in normal state
  (evil-set-leader 'normal ",")
  ;; what's default in the vim world? looks like leader-leader these days
  (evil-define-key 'normal 'global (kbd "<leader>l") 'evil-avy-goto-line)
  (evil-mode 1)

  (use-package evil-org
    :ensure t
    :after org
    :hook (org-mode . (lambda () (evil-org-mode)))
    :config
    (evil-org-set-key-theme '(navigation insert textobjects additional calendar))
    (require 'evil-org-agenda)
    (evil-org-agenda-set-keys))

  ;; ys<textobj><surround-delim>
  ;; ysiw~ = surround inner-word with ~
  ;; in visual state, do: S<surround-delim>
  ;; https://github.com/emacs-evil/evil-surround#examples
  (use-package evil-surround
    :ensure t
    :config
    (global-evil-surround-mode 1))

  ;; not yet working for me -- I need more practise with the "normal" commands
  ;; (use-package evil-easymotion
  ;;   :ensure t
  ;;   :config
  ;;   (evilem-default-keybindings "SPC"))

  )

(use-package evil-collection
  :ensure t
  :after evil
  :config
  ;; this should take care of corfu completion popups, as it's part of evil-collection
  ;; however, I still saw wonkiness in completion of [[title]] links in org-roam
  ;; https://github.com/emacs-evil/evil-collection/commit/ceac1a9681cb47de35aa37d63532b1b92cd58b72
  (evil-collection-init)

  (with-eval-after-load 'dired-quick-sort
    (evil-collection-define-key 'normal 'dired-mode-map "S" 'hydra-dired-quick-sort/body)))

;; For the motions g; g, and for the last-change-register ".". goto-chg supplies goto-last-change
(use-package goto-chg
  :vc (:fetcher "https://github.com/emacs-evil/goto-chg"))
```
