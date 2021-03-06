---
title: 'Weekly Head Voices #132: Potato deadline.'
author: cpbotha
type: post
date: 2018-02-18T20:45:08+00:00
url: /2018/02/18/weekly-head-voices-132/
categories:
  - weekly head voices
tags:
  - day zero
  - django
  - emacs
  - gou
  - note-taking
  - optic fibre
  - ramaphosa
  - south africa
  - speech recognition
  - water

---
{{< figure src="/wp-content/uploads/2018/02/IMG_3247-1024x930.jpg" link="/wp-content/uploads/2018/02/IMG_3247.jpg" caption="Fragment of potato skin, taken with phone camera through GOU#2’s microscope at 100x.">}} 

We have a serious deadline coming up on Tuesday, so I’m going to make these few WHV minutes count.

BULLET LIST TO THE RESCUE!

  * Day zero has again been [postponed, this time to June 4][1]. We continue with our water saving efforts.
  * That [unexpected side-project I mentioned in last week’s post][2] did end up going live that very night. Armed with the Django Rest Framework and plenty of battle scars, it took about 17 hours from idea to fully deployed REST API, a large part of which was debugging the paper’s math and spreadsheets. 
      * Django might be a slow runner relative to some of the other kids on the block (go with any of its web frameworks, nginx with openresty (lua right in your web server!), even apistar with uvicorn), but the completeness and maturity of Django and its ginormous ecosystem are hard to beat when it comes to development velocity.
  * There’s a [whole blog on the nature of note-taking][3]. I arrived there via [interleave][4] and [org-noter][5], both emacs packages for keeping text (orgmode) notes synchronised with PDFs, both found via [irreal][6], a great Emacs blog.
  * In the extra lessons I have with GOU#1, we studied electrical current from basic (atomic) principles. As I was getting all excited about the outer electrons being passed on from copper atom to copper atom (Khan Academy and I tag team these lessons), GOU#1 had to laugh at the goose flesh on my arms. 
      * The Khan Academy lecture seemed to imply that Benjamin Franklin started us down the not-quite-correct path of conventional current (from positive to negative), whereas the electrons being passed on imply current flow from negative to positive, aka electron current. However, [this physics StackOverflow answer][7] more completely explains that current is defined as _the flow of electric charge_, with electron flow being one example, and hence both directions are correct.
  * To be honest, I became ever so slightly irritated with an episode of one of my favourite podcasts, CPPCast, as the guest said “like” so often that I had trouble following what he was _actually_ like trying to say. This like led me to using Google’s machine-learning-based speech to text API one night to like transcribe the audio of the podcast to speech so that I could like count the number of like utterances. There were not as many as I thought, but still a whole lot. If you’re curious as to the stats, I wrote everything up in [this nerdy vxlabs blog post][8]. 
      * On the topic of note-taking: Because I make lab notes of everything in my Emacs, including late night speech recognition experiments, publishing a blog post is a question of some copy pasting, and then telling Emacs to publish to the blog.
  * On Thursday, some dudes came to my house and, after somehow switching seamlessly from pick-axe to optic fibre splicer and back several times, left me with this (and more):
  {{< figure src="/wp-content/uploads/2018/02/IMG_3241-1024x819.jpg" link="/wp-content/uploads/2018/02/IMG_3241.jpg" caption="Two fibre strands into my house. They tell me one is for backup.">}} 

  * These are strange Gibson-esque times when there’s now permanently a laser transmitting all of these packets to you via the network of glass strands encircling the Earth, whilst many of us are still struggling to grasp the difference between fact and fiction. 
      * “The future is already here — it’s just not very evenly distributed”, William Gibson, probably ’93.
  * We have a new president: President [Cyril Ramaphosa!][9] He was Mandela’s choice to become president of this country, but it was Thabo’s turn, and then things went pear-shaped with Zuma. Years later, the situation is quite dire, but so far there are many indications that Ramaphosa has the makings of a great leader (I have become convinced that we humans, all of us, need great leaders to advance as humanity; I hope to write a post about that some day). After Friday’s state of the nation (SONA) address by present Ramaphosa, I, along with many fellow South Africans, are hopeful for our future.

Ok peeps, have a wonderful week! I’ll see you NEXT TIME!

 [1]: https://mg.co.za/article/2018-02-13-day-zero-pushed-back-to-june-as-drought-declared-a-national-disaster/
 [2]: /2018/02/11/weekly-head-voices-131-function-over-form/#tool-belts-for-humanity
 [3]: http://takingnotenow.blogspot.co.za/
 [4]: https://github.com/rudolfochrist/interleave
 [5]: https://github.com/weirdNox/org-noter
 [6]: http://irreal.org/blog/?p=6954
 [7]: https://physics.stackexchange.com/a/17131
 [8]: https://vxlabs.com/2018/02/15/use-the-google-cloud-speech-api-to-transcribe-a-podcast/
 [9]: https://en.wikipedia.org/wiki/Cyril_Ramaphosa
