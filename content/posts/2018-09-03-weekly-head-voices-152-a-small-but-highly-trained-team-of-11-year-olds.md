---
title: 'Weekly Head Voices #152: A small but highly trained team of 11 year olds.'
author: cpbotha
type: post
date: 2018-09-03T21:07:10+00:00
url: /2018/09/03/weekly-head-voices-152-a-small-but-highly-trained-team-of-11-year-olds/
categories:
  - weekly head voices
tags:
  - apple music
  - birthday
  - bitbar
  - hammerspoon
  - netherlands
  - side-projects
  - spotify
  - spotify2applemusic
  - typescript

---
{{< figure src="/wp-content/uploads/2018/09/sylvia_henna-1024x719.jpg" link="/wp-content/uploads/2018/09/sylvia_henna.jpg" caption="GOU#2, age 8, made this for the blog, super special.">}} 

This edition of the Weekly Head Voices covers the period from Monday August 6 to Sunday September 2.

Somewhere during this period, I experienced my 44th birthday.

More than once since then, my partner has had to endure my brand-new joke / half-truth that I’m now as clever as a team of four smart 11-year olds. (Hey, it took a team of four smart 11-year olds to come up with that joke!)

On the big (for me) day, I cooked for a super tiny group of friends. I experienced the ritual of preparing dinner for friends to be an honest one, and filled with human warmth. 12/10 – Would do again.

The next morning, ever-so-slightly in recovery mode, I was surprised by my little brother and my little sister (in-law). MY FAMILY HAD CONSPIRED AGAINST ME WITH SUCH SUCCESS!

Somewhere during this period, I also had the fantastic privilege of going back to my other home (the one with the cheese, and the clogs, and the social democracy FTW) and spending time with my family there.

So much celebration. So much warmth.

(There is also some bitter-sweetness, but that’s the price one has to pay for having roots in different hemispheres.)

I would have liked to say more, but this is one of those WHAMPSAMP* situations.

(As part of a deal I made at AfrikaBurn with a brother, I went fully vegetarian from the Friday to the Monday. It was actually really good!)

(* WHAMPSAMP = What Happens At Mysterious Place Stays At Mysterious Place.)

# Music (nerd) and/or plain nerd section.

Somewhere during that period, Evil Charl went ahead and implemented that [Spotify2AppleMusic chrome plugin][1] that Responsible Charl mentioned in a [previous edition of the WHV][2] with the explicit purpose of getting it out of our system.

It’s out there now, and it’s free, so you might as well try it the next time that you need to convert any public (or private in your account) Spotify playlist to the corresponding Apple Music playlist.

I wrote this one in TypeScript where the type interfaces were a fantastic help in writing correct code for the parsing of the various APIs that this plugin has to inter-operate with.

# Nerd section: BitBar with Lua, Hammerspoon, nerd motivations.

Also somewhere during that period, but in a slightly more surprising twist, I [added lua support to the open-source macOS utility called bitbar][3], purely because I wanted to write a network bandwidth plugin that consumed less memory and was faster than the built in shell + awk versions.

That means I’m now also an [official bitbar plugin author][4], which I find strangely satisfying.

Well, maybe it’s not so strange. I do have a thing with producing artifacts that other people (might) use in some way. There’s even more vagueness on this topic at the bottom of this post.

(BTW, the Python version of the same plugin consumed 8 times as much memory as the lua version, which itself consumed about 30% less memory than the shell+awk version.)

(BTW, if you’re on a Mac, and you know a little bit of lua, [Hammerspoon][5] is an amazing tool for automating your desktop via its lua bindings to the mac desktop API. In a few lines of code, I was able to throw out [Spectacle][6], which itself is a great app, but Hammerspoon, the successor of Mjolnir, scores highly on the nerd street-cred scale and has MOAR FUNCTION.)

# Au revoir

I am grateful that you are here reading this, thank you!

I have recently acquired a new side-project (Evil Charl: “HELL YEAH!” BRRRAAAAAAAAMMMM <— crashes straight through office wall to the great outdoors on big motorbike. Responsible Charl: “sigh.”) which is currently sucking up a great deal of my creative output.

We all know what usually happens to side-projects. I guess the high probability of failure may even add to their attractiveness.

In either case, high or low probability outcome, I’ll eventually spill the beans over here. Suffice to say that I do seem to have a thing for [setting things up and then calling them universities][7], and in this case it’s even allowing me to produce reasonably sized packets of usefulness that might just magically add up to a valuable whole.

I am ever-so-slightly excited.

 [1]: https://chrome.google.com/webstore/detail/spotify2applemusic/gehbfaolompeeapflihekomijnhgccbk
 [2]: /2018/08/08/weekly-head-voices-151-we-are-pleased-to-meet-you/#chrome-or-firefox-plugin-to-convert-spotify-playlists-to-apple-music-using-the-new-musickit-js-api
 [3]: https://github.com/matryer/bitbar-plugins/pull/1084
 [4]: https://getbitbar.com/contributors/cpbotha
 [5]: https://www.hammerspoon.org
 [6]: https://www.spectacleapp.com
 [7]: /2018/05/09/weekly-head-voices-141-albert-was-burning-really-hard/
