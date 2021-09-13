---
title: 'Weekly Head Voices #158: Charlie and the Chocolate Factory.'
author: cpbotha
type: post
date: 2018-11-22T20:20:39+00:00
url: /2018/11/22/weekly-head-voices-158-charlie-and-the-chocolate-factory/
categories:
  - weekly head voices
tags:
  - backyard philosophy
  - deep learning
  - luna
  - nvidia
  - posterior tibial tendon
  - pytorch
  - running
  - telegram

---
_(Note that there’s now a [Telegram group][1] that you can join to be kept up to date with these posts. I’m never going to make the A-List, but at least I haz the gimmicks!)_

This edition of the weekly (haha) head voices attempts to reflect on the period of time from Monday November 5 to Sunday November 18, 2018.

The following action scene happened exactly halfway through:
{{< figure src="/wp-content/uploads/2018/11/paarl-running-20181111-1024x642.jpg" link="/wp-content/uploads/2018/11/paarl-running-20181111.jpg" caption="Pre-requisite running photo, this one taken in Paarl. It was already quite hot. Getting really hot really early in the morning is Paarl’s thing.">}} 

# Running aka Irony update

Seeing that you’ve made me talk about running again, have a look at this photo of one Luna Mono 2.0 after about 700 km of (mostly road) running in about seven months, and one brand new Luna Mono 2.0:

{{< figure src="/wp-content/uploads/2018/11/old-vs-new-lunas-1024x768.jpg" link="/wp-content/uploads/2018/11/old-vs-new-lunas.jpg" >}}

At around about the same time as the new shoes arrived, shortly after South African customs charged me a painful amount before letting the new babies through, both my ankles, from around the posterior tibial tendon area, let me know in no uncertain terms that they were now _demanding_ a break.

After repeated explanations by my life partner (she counts being a rheumatologist amongst her many talents), and by a foot surgeon friend, that my flat feet mean that my posterior tibial tendons have to work even harder than they would usually have done had I been anatomically speaking more normal, I had to start facing the music:

_I was going to have to wear normal person running shoes again._

(If I have to be honest I would have to say that the music was in fact more about having to take a running break. I had sneakily been pushing up my weekly distance, trying to run through ankle discomfort, and this was probably the true core of the problem.

All of that being said, I am choosing to interpret matters a bit differently. Running breaks are really hard yo.)

I’ve now done two runs in my pre-Mono Kinvara 8s, and it does indeed feel (of course it does) like my ankles might slowly be recovering. I am hopeful that the trend continues, and that I can eventually rotate in my Lunas again.

# Nerd toys update: RTX 2070 in da house.

After weeks of deliberating, I broke down and bought an [NVIDIA RTX 2070][2] for deep learning.

This in turn led to a flurry of experimentation and to be quite honest a slight case of deep learning binging.

At least I have the following new blog posts to show for it:

  * [PyTorch 1.0 preview (Nov 10, 2018) packages with full CUDA 10 support for your Ubuntu 18.04 x86_64 systems][3] – In order to use the shiny new TensorCores on the RTX for more efficient deep learning, you need a CUDA 10 build of PyTorch. YOUR WISH IS MY COMMAND.
  * [Configuring Emacs, lsp-mode and Microsoft’s Visual Studio Code Python language server][4] – When you prefer using Emacs inside of a tmux in a mosh or ssh session to your Linux desktop with the RTX 2070 to develop PyTorch and fastai scripts (no Jupyter in sight, what a relief!), you need the best code-intelligence you can get. Visual Studio Code’s Python Language Server McGuyvered right into Emacs will do nicely thanks!
  * [A Simple Ansible script to convert a clean Ubuntu 18.04 to a CUDA 10, PyTorch 1.0rc, fastai, miniconda3 deep learning machine][5] – When you need MOAR firepower to train your networks with larger batch sizes, or just to see how much memory your network would have taken in fp32 mode instead of mixed-precision, this ansible script will reproducibly convert a clean Ubuntu 18.04 GPU instance, such as that supplied by PaperSpace or Google Compute Engine, into a CUDA 10, PyTorch, fastai, miniconda3 deep learning playground, all in about 10 minutes.

(I know that some of these occurred outside of the two week timespan covered by this post.)

## On the memory saving of mixed-precision training.

In my tests with ResNet50, a serious convolutional neural network for image classification, the exact same network with the exact same training settings required 14159 MiB in fp32 mode but only 7641 MiB in mixed precision mode.

This means that in some cases, this new RTX 2070 can go toe-to-toe with many far more expensive cards.

Furthermore, I informally measured a training speed boost of about 20% with the smaller ResNet34.

It’s no wonder that the [RTX 2070 gets the Tim Dettmers stamp of approval for the most cost-effective training][6].

# Your message, to take home.

I came across this backyard philosophy jewel [on reddit the other day][7] and loved it. It’s about the 1971 movie W_illy Wonka & the Chocolate Factory_, a stellar adaptation of Roald Dahl’s book [Charlie and the Chocolate Factory][8].

> … in test screenings, Willy Wonka had a scene with a hiker seeking a guru, asking him the meaning of life. The guru requests a Wonka Bar. Finding no golden ticket, he says, “Life is a disappointment.” The director loved it, but few laughed. A psychologist told him that the message was too real.

Just remember the [Buddhist Twist][9] my friends:

> … and finally passing through the gate of wishlessness (apranihita) – realizing that nirvana is the state of not even wishing for nirvana.

 [1]: https://t.me/headvoices
 [2]: https://www.nvidia.com/en-us/geforce/graphics-cards/rtx-2070/
 [3]: https://vxlabs.com/2018/11/04/pytorch-1-0-preview-nov-4-2018-packages-with-full-cuda-10-support-for-your-ubuntu-18-04-x86_64-systems/
 [4]: https://vxlabs.com/2018/11/19/configuring-emacs-lsp-mode-and-microsofts-visual-studio-code-python-language-server/
 [5]: https://vxlabs.com/2018/11/21/a-simple-ansible-script-to-convert-a-clean-ubuntu-18-04-to-a-cuda-10-pytorch-1-0rc-fastai-miniconda3-deep-learning-machine/
 [6]: http://timdettmers.com/2018/11/05/which-gpu-for-deep-learning/
 [7]: https://www.reddit.com/r/todayilearned/comments/9ozu4e/til_in_test_screenings_willy_wonka_had_a_scene/
 [8]: https://en.wikipedia.org/wiki/Charlie_and_the_Chocolate_Factory
 [9]: /2018/06/03/weekly-head-voices-144-eternal-learner/#the-buddhist-twist
