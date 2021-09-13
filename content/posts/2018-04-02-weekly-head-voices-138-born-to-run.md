---
title: 'Weekly Head Voices #138: Born to run.'
author: cpbotha
type: post
date: 2018-04-02T08:13:12+00:00
url: /2018/04/02/weekly-head-voices-138-born-to-run/
categories:
  - weekly head voices
tags:
  - barefoot
  - born to run
  - caballo blanco
  - emacs
  - helm
  - spotlight
  - tracker

---
{{< figure src="/wp-content/uploads/2018/04/mystery_place-1024x575.jpg" link="/wp-content/uploads/2018/04/mystery_place.jpg" >}}

I am currently in a place with no to extremely little internet. Just getting the photo above uploaded was an adventure.

I briefly debated breaking my current WHV posting streak due to exceptional circumstances, but decided against it, at least for now.

Anyways, I might have no internet, but the scenery here is phenomenal.

(It later turned out that just getting this blog post uploaded on Sunday evening was not going to happen.)

# Sometimes focus falls and slips into Emacs

During the past week I had a fairly difficult technical puzzle to deal with. It’s one of those puzzles that can only be solved with multiple days of research and concerted focus.

It’s funny how my mind manages to sort of slip away when faced with these sorts of puzzles where the solution, if it even exists (this is probably the main reason for the continual slippage), seems to be weeks away, instead of a few hours or days.

It’s like a usually sharp(ish) knife which simply refuses to bite into the thing that I so desperately want to cut with it.

In my specific case, especially later in the afternoons when prefrontal cortex is long-gone, mindlessly drinking its beer while staring into space somewhere, or even later in the evenings when everyone else is also drinking beer while staring into space, I wake up to find myself working on some obscure Emacs hack.

This week, primary thought slippage resulted in:

  * Hooking up my emacs, via [helm-for-files][1] with mdfind (the command-line interface to spotlight) on macOS and the tracker file indexer on Linux. This means that with a simple press of the `C-x c o` keys, I can instantly open any file in Emacs which is already open somewhere, which I’ve recently worked on, whose filename faintly resembles what I’m typing, whose contents (or tags) faintly resembles what I’m typing, no matter where that file is hiding in the hundreds of gigabytes on my SSD.
  * My efforts getting the above working for Linux are [now part of helm][2], via the wonderful system of github pull requests.
  * Setting up [Emacs dired][3] to do rsync-based network copying in the background, which culminated in [a github contribution][4] which will hopefully also find its way into the main repository soon. (I do most of my **serious** file management in Emacs dired. You should try it.)

# The Running People

I finally bought [Born to Run by Christopher McDougall][5].

In between travelling and other activities, I was not able put this book down.

As I was reading the final pages on Sunday morning, I had trouble keeping my eyes dry. I had connected with the story and all of its nested stories on so many levels.

One strand of the story makes the case that humans, or more specifically homo sapiens, had evolved to run its prey down on the savannah.

We are able to cool ourselves down during running thanks to being mostly hairless and sweaty, whereas an antelope is not able to pant while galloping, and has no choice but to stop.

So the trick is simple: We can run fast enough to keep a galloping antelope in sight. Eventually it will lose the battle, overheat and collapse.

This is what homo sapiens did for millions of years for food. [_Homo neanderthalensis_][6], our intelligent and stronger competition who used to dominate during colder times, had no chance.

McDougall connects with a number of scientists and sports trainers to flesh out this part of the story. Below is an interesting (and related) video about Prof Daniel Liebermann and his work on the evolutionary biology and biomechanics of barefoot running:

<div class="jetpack-video-wrapper">
<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="473" src="https://www.youtube.com/embed/7jrnj-7YKZE?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="840"></iframe></span>
</div>

(Being internet-deprived, I’m not currently able to find one of the cited Nature papers discussing other elements of our biology underlining our running heritage. Remind me in the comments so I can update this later.)

Another strand of the story is about the [Tarahumara of Mexico, also
  
known as Rarámuri][7], or The Running People, a legendary tribe of natural super athletes who are masters of avoiding other humans (due to past persecution and other shenanigans) and of running 30 miles in the mountains, in sandals.

_Even more intriguing than their home-made sandals, is that they run throughout their healthy lives with joy and exuberance._

The final strand I want to mention here, is McDougall’s personal journey from injury-prone runner all the way to finally taking part in the very first edition of a gruelling 50 mile trail race (the centre-piece of the story I would argue), together with the world’s best ultra marathoners and the Taramuhara in the Copper Canyons of Mexico.

For a large part of this journey, he and a number of other key actors are propelled along by [Caballo Blanco][8], the White Horse, a supernaturally gifted runner who lived off the land in the Copper Canyons, and one of the few foreigners who seemed to be completely accepted by the Taramuhara.

Caballo is the one who managed to bring together, for the first time, the Taramuhara and the best ultra-marathoners in the small town of Urque for this humanity-affirming 50 mile trail run. He did so from his stone hut in the middle of nowhere, from where he would have to run for 30 miles to the closest settlement that had a telephone line that he could use.

Often that line was down.

Caballo passed away in 2012, shortly after the first Copper Canyon race. Shortly after, the race was officially dubbed the [Ultramaraton Caballo Blanco.][9]

Right after I put the book down, I put on my shoes and went for a run
  
up the mountain-side and in the valley over here. On the balls of my feet as they landed right under me, really small steps, straight back, trying my best to float over the earth, just like the running people in the book.

I could not help but smile for most of the way.

 

 [1]: http://pragmaticemacs.com/emacs/find-and-open-files-from-anywhere-with-helm-for-files/
 [2]: https://github.com/emacs-helm/helm/pull/2005
 [3]: https://www.gnu.org/software/emacs/manual/html_node/emacs/Dired.html
 [4]: https://github.com/tmtxt/tmtxt-dired-async/pull/6
 [5]: http://www.chrismcdougall.com/born-to-run/
 [6]: https://en.wikipedia.org/wiki/Neanderthal
 [7]: https://en.wikipedia.org/wiki/Rar%C3%A1muri
 [8]: https://en.wikipedia.org/wiki/Micah_True
 [9]: https://en.wikipedia.org/wiki/Ultramaraton_Caballo_Blanco
