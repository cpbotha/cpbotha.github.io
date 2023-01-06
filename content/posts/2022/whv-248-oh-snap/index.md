+++
title = "Weekly Head Voices #248: Oh snap"
date = 2022-11-11T17:11:00+02:00
lastmod = 2022-11-13T18:34:28+02:00
slug = "weekly-head-voices-248-oh-snap"
tags = ["dropbox", "keyboards", "math", "onedrive", "physics"]
categories = ["weekly head voices"]
draft = false
author = "Charl P. Botha"
katex = true
org = true
ogimage = "watsonia.jpg"
+++

Welcome back everyone to this completely normal and _of course_ utterly on-time
edition of the WHV which spans (checks notes...) the one (1) week from Monday
October 31 to Sunday November 6, 2022.

{{< figure src="watsonia.jpg" caption="<span class=\"figure-number\">Figure 1: </span>Watsonia posing in front of mountain. Photo by partner." link="watsonia.jpg" >}}

(Yes, I am a little bit excited that for once this post is technically on time
enough to cover only that one week. Of course what's in the post does not
necessarily have to do anything with the events that transpired in that week,
but we won't let that keep us from this little punctuality celebration.)

On to the post: We have keyboards, file synchronization approaches and some
surprising mathematical terminology!


## Keyboard never-endgame {#keyboard-never-endgame}

It has been ...9 (nine)... months since I last talked about [keyboards on this
blog](/tags/keyboards/).

At that point, [I had just replaced the tactile brown switches in my Womier with
linear reds](/2022/02/09/weekly-head-voices-238-live-deep-and-suck-out-all-the-marrow-of-life/#womier-k87-keyboard-customization-unlocked), and discovered to my surprise that I do in fact prefer linears.

Since then, I have again replaced the switches on that board, but this time
with Kailh Speed Silvers.

My plan was to get as close as possible to the effortlessly smooth feel of my
Varmilo VA87m (with Cherry MX Speed Silvers) at work.

While that board was certainly inching closer, it was still missing a little
something...

... perhaps, perhaps it was just missing a completely new little new keyboard!

When respected YouTube reviewers call a keyboard with factory-lubed switches,
luxury double-shot PBT OSA-profile keycaps and this particular sound the ["The
Keychron V1 **Bargain**"](https://youtu.be/HVphB6RYBaY), and other reviewers remark that the only issue with this
board is that you'll be hard-pressed to find one in stock due to its level of
bang-for-buck, you could probably predict that I would find it quite hard to
resist.

I had to pull some (Aramex) strings to get the keyboard delivered here, but
wow, it was so worth it!

Although I was hoping for something close to my Varmilo in terms of feel, this
V1 with its red switches is at least the Varmilo's equal, if not a little more.


## Hell freezes over (again) {#hell-freezes-over--again}

Readers of this blog know that I've been [using (and paying for) Dropbox](/tags/dropbox/) for
quite a number of years.

We've been together for long enough that we even got to do a [break-up-make-up
cycle back in 2013](/2013/09/15/dear-usa-my-data-has-left-your-building/), and in 2019 I tried and [failed spectacularly to migrate to
a cheaper competitor whose name starts with a G](/2019/03/09/weekly-head-voices-164-its-what-future-you-would-want/#my-big-and-stupid-misstep-into-google-drive).

One would have thought that I learned my lesson in 2019 (that post even
explicitly lists the lessons learned...), but apparently not.

After I recently discovered how to get the fantastic [unison bi-directional
syncing tool to sync between WSL and the Windows host](https://vxlabs.com/2022/10/22/unison-file-synchronization-directly-via-the-wsl-bridge/), I decided that it was
again time to attempt _something_ stupid, this time migrating my whole digital
life to OneDrive, the cloud file synchronization tool made by Microsoft, our
erstwhile sworn enemy who later turned out to be pretty cool after all.

My main reason this time was again cost, and reducing the number of
subscriptions and cloud systems we use. (we already have OneDrive as part of
the incredibly reasonably priced Microsoft 365 family)

About two weeks ago I managed to copy all of my files (more than 500 thousand
files totalling over 200GB) from Dropbox to OneDrive over a few days, using the
amazing rclone tool, via my Hetzner VPS in Germany.

After some initial hiccups as the various OneDrive clients had to catch up to
the deluge of new files that were coming in, this setup has been working pretty
well!

On each of my Windows development machines (2 active, 1 semi-active) I have
unison running in watch mode under tmux syncing only the subset of the folders
that I need to be on WSL2, namely source code and my pkb4000 notes
database. (the same notes database containing the month file that houses this
blog post draft -- every time I hit `C-x C-s`, the Emacs hotkey for save, this
file is synced from WSL to the host drive by Unison, and then from there to the
OneDrive cloud)

I also have the OneDrive client on my M1 MBA where it uses more ram than
Dropbox, but where its RAM for some reason gets compressed much more readily
than the Dropbox client.

While the syncing is not as fast as dropbox (in terms of picking up changes and
zapping them to the cloud and to other machines), it's entirely
serviceable. unison is blindingly fast for its part of the job.

As an added bonus, this enabled me to exclude `node_modules` FOREVER in the
default unison profile that I use.

Note that you can configure OneDrive to exclude files BY WILDCARD (see [this
superuser.com answer](https://superuser.com/a/1662761/130835)), something that even the great Dropbox has no way of
doing.


### Yes, you CAN keep your checked-out source code in Dropbox or OneDrive! {#yes-you-can-keep-your-checked-out-source-code-in-dropbox-or-onedrive}

Finally, hereby I also officially announce that: Why yes, I do keep _all_ of my
checked out source code projects in OneDrive. Previously, I did the same for
years and years in Dropbox.

I have very good reasons for doing this.

My tweet below and the blog post that I link explain some of these reasons:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Every time someone asks about storing git repos in <a href="https://twitter.com/Dropbox?ref_src=twsrc%5Etfw">@Dropbox</a> / <a href="https://twitter.com/onedrive?ref_src=twsrc%5Etfw">@onedrive</a> someone asks &quot;why?! because git already does that!&quot; - well no, it doesn&#39;t instantaneously sync all your work so that you can change workstations on a whim! <a href="https://twitter.com/Lexisomes?ref_src=twsrc%5Etfw">@Lexisomes</a> explains: <a href="https://t.co/UCiNcAGCal">https://t.co/UCiNcAGCal</a></p>&mdash; charlbotha dot com dot net dot org (@cvoxel) <a href="https://twitter.com/cvoxel/status/1582682819037626368?ref_src=twsrc%5Etfw">October 19, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

... and here I recently came out about this issue on reddit:

> I have been hosting all of my source code in dropbox AND pushing to various git
> repos for years and years now, with nary a hitch. For the past few weeks, I
> have been trying OneDrive, and so far it's been going well.
>
> I've been trying to explain to people over the years that there are good
> reasons for doing so, in my case primarily the fact that I work on the same
> projects on various machines and laptops, and I prefer NOT abusing git commits
> for manual syncing
>
> Furthermore, I'm often working on a number of repos, and having to commit all
> of them just to switch ot my laptop does not make any sense.

The next time someone claims that this is what git is for, please send them to
me, because it's not.


## From the Departments of Physics and Breakfast {#from-the-departments-of-physics-and-breakfast}

I recently learned about the official names of the third to sixth derivates of
position, from [Twitter of all places](https://twitter.com/JimPfaendtner/status/1588987738426314752).

(Over the years, I've actually learned quite a lot from there, but who knows
how we'll look back at it in a few years time.)

[Wikipedia confirms](https://en.wikipedia.org/wiki/Fourth,_fifth,_and_sixth_derivatives_of_position) that indeed after the pretty unsurprisingly named first and
second derivatives, namely _velocity_ and _acceleration_, things started getting just a
little bit weird, but understandable, with _jerk_ for the third, and _snap_ or _jounce_ for the
fourth, but then the clown gloves came off with **_snap_**, **_crackle_** and **_pop_** for the
fourth to the sixth derivatives!

Isn't that just marvelous?!

I really wanted to reproduce the list here using the built-in \\(\KaTeX\\) support
in this blog, and so I fell down a small rabbit-hole because \\(\KaTeX\\), while
amazing and fast, does not have `eqnarray`, and its `aligned` environment needs
some help with vertical spacing (`\\[1.5ex]` at the end of every line to give it
a bit of an extra nudge).

Secondly, I had to update my modification of the [hugo-minos theme](https://github.com/carsonip/hugo-theme-minos) so that it
uses the latest version of \\(\KaTeX\\), and so that I could add that very `aligned`
environment to its default list of [delimiters via the optional `options`
argument to `renderMathInElement()`](https://katex.org/docs/autorender.html#api).

Finally, while Org-mode and the brilliant ox-hugo usually automatically pass
[\\(\LaTeX\\) fragments](https://orgmode.org/manual/LaTeX-fragments.html) through to Hugo, in this case I had to wrap it in an `HTML`
export block and manually specify the correct number (four) of slashes, as it was
automatically transforming `\\[1.5ex]` into `\\\[1.5ex]` (note the three slashes
instead of four, whilst without the `[...]` it correctly generates four).

Anyways, after all that, you get these nicely rendered equations:

\begin{aligned}
\bm{r} &= \operatorname{position}\\\\[1.5ex]
\frac{d\bm{r}}{dt} &= \operatorname{velocity}\\\\[1.5ex]
\frac{d^2\bm{r}}{dt^2} &= \operatorname{acceleration}\\\\[1.5ex]
\frac{d^3\bm{r}}{dt^3} &= \operatorname{jerk}\\\\[1.5ex]
\frac{d^4\bm{r}}{dt^4} &= \operatorname{snap}\\\\[1.5ex]
\frac{d^5\bm{r}}{dt^5} &= \operatorname{crackle}\\\\[1.5ex]
\frac{d^6\bm{r}}{dt^6} &= \operatorname{pop}
\end{aligned}

Wow, blogging with Org-mode and Hugo sure is easy! :)

P.S. You might remember that it was also a [Physics paper that helped
main-streaming the word _embiggen_](https://blogs.scientificamerican.com/news-blog/how-a-fake-word-from-the-simpsons-e/) from The Simpsons right into our
dictionaries.
