+++
title = "Weekly Head Voices #210: MiniBurn 2020"
date = 2020-11-29T09:50:00+02:00
lastmod = 2020-12-06T15:55:51+02:00
slug = "weekly-head-voices-210-miniburn-2020"
tags = ["afrikaburn", "ai", "emacs", "gu43", "helm", "ivy", "joris voorn", "nim-lang"]
categories = ["weekly head voices"]
draft = false
ogimage = "dirt_road_to_stanford.jpg"
org = true
+++

{{< figure src="dirt_road_to_stanford.jpg" link="dirt_road_to_stanford.jpg" >}}

Welcome back to the WHV blogging clubhouse, gang!

Somewhat inspired by Descartes, I can say with a fair amount of confidence that
you are now reading these words, and for that I am grateful.

This post covers the weeks from Monday, November 9 to Sunday, November 22 of
the year 2020.


## papercite\_static: put some bibtex into your Hugo {#papercite-static-put-some-bibtex-into-your-hugo}

After languishing for almost a year on my todo list, I finally got around to
cleaning up and making available my Python script for embedding your BiBTeX
bibliographies in your markdown files.

The script is called [papercite\_static](https://github.com/cpbotha/papercite%5Fstatic), because it was inspired by [the papercite
Wordpress plugin](https://wordpress.org/plugins/papercite/) that I previously used, but it was built for use in static
websites.

Catchy right?

This is pretty useful when you are academically inclined, or just really like
managing BiBTeX files.

If you're one of those people, you can go check it out at [the papercite\_static
github page](https://github.com/cpbotha/papercite%5Fstatic).


## save\_image\_from\_clipboard {#save-image-from-clipboard}

From the Department of Catchy Names, the same one that brought you the script
above, comes [save\_image\_from\_clipboard](https://github.com/cpbotha/save%5Fimage%5Ffrom%5Fclipboard)!

I wrote this to scratch my own extremely niche itch (scranitch-ware!), but it
could be useful in other slightly less niche contexts.

My Emacs is configured with the org-download package so that I can use any
system tool to screenshot an arbitrary region of my screen to the clipboard,
and then tell Emacs to attach whatever is in the clipboard to the current
Orgmode heading.

This is something I use really often during daily note-taking and task
management.

The org-download package expects a PNG image to be available on the
clipboard. When this is not the case, because the screenshotting or other image
copying workflow instead copied a JPG or a BMP (long story, starts with a W,
ends with SL...), I get a blank attachment which makes me sad, and costs me
more time.

On macOS, I used [pngpaste](https://github.com/jcsalterego/pngpaste) for this, a tool that ensures that whatever image
format is in the clipboard gets converted to PNG.

Well, [save\_image\_from\_clipboard](https://github.com/cpbotha/save%5Fimage%5Ffrom%5Fclipboard) does exactly this, and a little more by simply
converting whatever's on the clipboard to the format that you specify.

This has already saved me countless SECONDS of time, and a substantial amount
of frustration.

P.S. I've again been spending more hobby time with [nim](https://nim-lang.org/), which would have
resulted in a much smaller and faster binary in this case, but the Python
version wrote itself fairly quickly, with both of my hands behind my back.

P.P.S. nim is _so_ hard to resist, in spite of what [I wrote about nimfatuation
being over, back in WHV #169](/2019/04/15/weekly-head-voices-169-a-cunning-plan/#nimfatuation-is-now-over). It combines much of the expressiveness and some
of the batteries-included of Python, paired with the generation of tiny
self-contained binaries.


## My Emacs is now all-in on Ivy {#my-emacs-is-now-all-in-on-ivy}

As you will _most probably_ remember from [WHV #171](/2019/05/22/weekly-head-voices-171-icemirb/#you-can-easily-dired-jump-to-the-currently-ivy-readd-file-in-emacs), my Emacs configuration used
a mishmash of [Helm](https://github.com/emacs-helm/helm) and [Ivy](https://github.com/abo-abo/swiper).

Helm and Ivy are two great, but different, examples of Emacs completion /
selection frameworks, something that is really important to any disciple of
this amazing religion.

In something that is probably some sort of reflection of my character, I was
happily using both of them simultaneously for quite a while.

However, waking up one morning with the realisation that this was yet another
small context switch that was costing me time and focus, in one of my highest
ROI tool workflows to boot, I decided that it was time to excise Helm from my
configuration.

Fast-forward a few hours of Lisp-driven terraforming, and I was all-in on my
Ivy.

During this terraforming I ran into some undesired behaviour in ivy-rich, which
resulted first in me writing [a blog post documenting the work-around](https://vxlabs.com/2020/11/15/fix-ivy-rich-switch-buffer-directories-display-in-emacs/), then
noticing that ivy-rich's astute author had subsequently integrated part of my
fix, and finally authoring a [github pull request (PR)](https://github.com/Yevgnen/ivy-rich/pull/92), merged shortly after to
fix the remaining issues.

P.S. I sometimes wonder whether people outside of the open source world
understand how much github contributed to the software world by streamlining
the process whereby random developers are able to contribute lines of source
code into open source projects like this.

WELL DO YA?!


## mynoise.net is an amazing soundscape generator {#mynoise-dot-net-is-an-amazing-soundscape-generator}

In the past few weeks, Lazar Focus has rescued my days so often.

What usually happens is that I get distracted... no wait, I fall down a
rabbit-hole... no wait, I actually get violently pulled into a rabbit
**singularity** from whence no productivity can escape.

The best I can do at that point, is to pour all will power into my puny arm and
click on that FOCUS button in Lazar Focus, at which point it instantly kills
everything that's sapping my attention, and then I again have a chance to save
the day.

Thanks to a recommendation by Noeska which ended up languishing in my
sub-conscious but then fortunately managed to bubble to the top, I found myself
on a wonderful site called [myNoise](https://mynoise.net/).

This is the creation of [Dr. Ir. Stéphane Pigeon](https://stephanepigeon.com/), a research engineer & sound
designer from Belgium, who has combined noise generation as well as a library
of the highest quality recording of samples from the world over with a system
for composing these into the most amazing sound-scapes.

Why is this interesting, you might ask?

Well, in one's quest to block distractions of all kinds, finding the perfect
aural stimulus that is pleasant, but does not soak up attention itself, and is
also able to mask both external and internal (tinnitus, e.g.) sounds, myNoise
is exactly what the doctor ordered!

To give you a taste of Dr Pigeon's attention to detail, see for example the
[singing bowls generator](https://mynoise.net/NoiseMachines/singingBowlsDroneGenerator.php), and then the [Free-falling with vocalist Enlia
soundscape](https://mynoise.net/NoiseMachines/enliaVocalSoundscape.php).

Notice that in both cases you are able to customise different elements of each
soundscape with the sliders, or even press `A` to have them animate randomly
over time, morphing the landscape as you work.

What I only recently learned, is that Dr Pigeon designed the soundscapes to
work also simultaneously. In other words, keep the two soundscapes above open
in two browser tabs, and note how wonderfully they mesh.

It really feels like my brain is starting to associate high attention mode with
the mynoise soundscapes.

Between that and LF, we might be going places!

P.S. Narrator: _Yes, he did make a small donation to mynoise, and based on the
value he has derived since, will probably make another._


## What does it mean for humanity when the AI can derive your talking face from your voice alone? {#what-does-it-mean-for-humanity-when-the-ai-can-derive-your-talking-face-from-your-voice-alone}

You might have read about [NVIDIA's new AI-based video conferencing bag of
tricks, called Maxine](https://www.theverge.com/2020/10/5/21502003/nvidia-ai-videoconferencing-maxine-platform-face-gaze-alignment-gans-compression-resolution).

An interesting part of this is that they use a technique, similar to deepfakes,
to send only the pose of your face over the internet, and then reconstruct a
high quality version of it on the other side.

From the article:

> "Instead of streaming the entire screen of pixels, the AI software analyzes the
> key facial points of each person on a call and then intelligently re-animates
> the face in the video on the other side," said the company in a blog
> post. "This makes it possible to stream video with far less data flowing back
> and forth across the internet."

This made me think:

Soon the AI will be good enough that it can reconstruct your face from just the
audio, or maybe even text that you type.

This idea started as a half-serious joke, but it does raise really interesting
questions around the implications of this technology. (BTW, it is technically
entirely possible.)

If you're having a conversation with someone, and both of your faces are
indistinguishable _simulations_ of the real thing, and hence help the quality
of the conversation, what does that mean for the conversation that's happening?

In other words, imagine for a second that you're having an intense (emotional)
conversation with someone, but the faces that both of you are seeing, are 100%
synthesised.

They reflect almost exactly how your faces would have looked had you had a
video link, but they are estimated by the AI.

Did you really have that intense conversation?


## MiniBurn 2020 {#miniburn-2020}

As you might remember from [WHV #191](/2020/03/24/weekly-head-voices-191-covid-19-part-1/#sht-gets-real-in-mzansi), AfrikaBurn 2020 was one of the first group
events down here that was cancelled by the pandemic.

Months after that, and with stats looking almost reasonable, the local subset
of our camp (THE BURNIVERSITY) decided to celebrate life together, as
responsibly as possible (which mostly comes down to: stay outside, keep your
distance), by gathering at some secret but beautiful location for the weekend.

(You might have deduced by now that this is one of those Burny situations where
I have no choice but to keep things as vague as they are. I still wanted to
write **something** as a beacon for future me. Future me, when you read this:
Read our private notes man. I left you something there.)

We sort of modeled the weekend like a whole Burn: Friday is arrival, setup, and
first small celebrations. Saturday represents the body of the week: Running,
workshops, celebration. Sunday is, just like it is for the full Burn, the
slightly depressing but already nostalgic clean-up, pack-up and leave the
desert stage. It's surprising how well this whole sequencing worked.

Thanks to the awe-inspiring talents of specific camp members, the cuisine was
divine and the music beautiful. Combined with the personalities and shared
memories of our small ensemble, the resultant experience was nothing short of
magic.

P.S. Ironically, [GU43 **is** turning into the 2020 soundtrack that I wanted](/2020/11/12/weekly-head-voices-208-blogging-like-its-2009/#thank-you-joris).
