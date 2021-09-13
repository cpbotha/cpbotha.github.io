---
title: 'Weekly Head Voices #128: Water water everywhere, but not a drop to drink.'
author: cpbotha
type: post
date: 2018-01-21T15:39:35+00:00
url: /2018/01/21/weekly-head-voices-128-water-water-everywhere-but-not-a-drop-to-drink/
categories:
  - weekly head voices
tags:
  - day zero
  - pipenv
  - python
  - react
  - semantic ui
  - water

---
{{< figure src="/wp-content/uploads/2018/01/bbay-pano-20180121-1024x326.jpg" link="/wp-content/uploads/2018/01/bbay-pano-20180121.jpg" >}}

Hey friends, welcome back!

We have to talk about the water situation, seeing that Cape Town is now in the international news as [being on track to be the first major city EVAR to run out of water][1].

In short, if it doesn’t rain in substantial amounts during the coming three months (which history and projections say it won’t), [the municipal water supply will be shut off on April 21][2], a date festively referred to as _Day Zero_.

This means when we try to open any tap, no water will come out. This situation might continue for quite a while, which is pretty intense.

On that day, we will be celebrating by dressing up as Kevin Costner and running around barefoot shouting “NOTHING’S FREE IN WATERWORLD!”. Those who are not big fans of Kevin are allowed to dress up as [Imperator Furiosa][3].

At my house, we stopped watering our garden with municipal water months ago. We installed a grey water recovery system: Shower and bath water ends up in the only remaining green corner of the garden.

We also installed a rain water recovery system three months ago, which has fortunately enabled us to collect a few thousand litres of rain water via the rerouted gutters and pipework from the roof. This water we will probably use after Day Zero to be able to wash and to flush a toilet now and then.

(Flushing frequency has necessarily decreased significantly. Around these parts we now have the saying: “If it’s yellow, let it mellow. If it’s br\***, flush it down.” Please excuse the mental graphics.)

We have been managing to keep our use of municipal water under the requested 87 litres per person per day. Starting on February 1, we will have to stay consistently under 50 litres per person per day, including drinking, cooking and washing. I guess 2 minute showers were wasting too much of my time in any case.

I have to do more research and corroboration (fingers are being pointed in all directions), but it seems the fundamental issue is not so much the current drought alone, but to a large extent mismanagement by _both_ local and national government. It’s complicated, and politics is involved, so read at least [this][4] (otherwise good piece, but author is a DA / local government apologist), [this][5] (DA / local government IS to blame) and [this][6] (a longer, more balanced piece) to start with.

That being said, I _am_ happy that a large part of the populace has become much more water efficient. If we get through this, in spite of “this” being called “the new normal”, I hope that we retain our mad Dune-grade water saving skills.

With that out of the way, it would be sort of anti-climactic for me to talk extensively about what-I-did-last-week, so I’m going to limit it to a REAL bullet list (ping me in the comments if something interests you):

  * [pipenv][7] is the bee’s knees, I have switched my non-miniconda projects.
  * convincingly but fortunately only temporarily locked myself out of my one laptop due to TCG-Opal hardware encryption, UEFI32, UEFI64 and legacy boot incompatibilities. I’m getting old, I used to NOT lock me out of my laptop in my sleep.
  * A compulsive twitch made me fix years of old-style broken youtube shortcodes using the [wordpress regex plugin][8]. The regexp you are looking for is `/\[youtube\](.*)\[\/youtube\]/` which you can replace with `\1`.
  * [People dislike really smart leaders][9]. See water crisis above for one possible reason why this is a bad thing.
  * In spite of having invested a significant amount of time in deciding on the [Office UI Fabric React components][10] for my most major side-project (#38465 if you’ll recall), I switched to [Semantic UI React][11] (which was also in the running, together with [Palantir’s blueprint][12], [HP’s grommet][13], [Alibaba’s Ant Design of React][14] and more) at the last minute. I am happier now.

That’s it from me for now. Have fun this week kids, I hope to see you soon!

 

 [1]: http://time.com/5103259/cape-town-water-crisis/
 [2]: http://untoldafrica.com/calling-all-capetonians-its-time-to-prepare-for-day-zero/
 [3]: https://en.wikipedia.org/wiki/Imperator_Furiosa
 [4]: https://theconversation.com/cape-towns-water-crisis-driven-by-politics-more-than-drought-88191
 [5]: https://www.dailymaverick.co.za/article/2018-01-22-op-ed-cape-town-a-city-drowning-in-incompetence/
 [6]: https://www.dailymaverick.co.za/article/2018-01-22-analysis-a-drought-of-nature-compounded-by-a-drought-in-leadership/
 [7]: https://github.com/pypa/pipenv
 [8]: https://wordpress.org/plugins/search-regex/
 [9]: https://www.scientificamerican.com/article/why-people-dislike-really-smart-leaders/
 [10]: https://github.com/OfficeDev/office-ui-fabric-react
 [11]: https://react.semantic-ui.com/introduction
 [12]: http://blueprintjs.com/
 [13]: http://grommet.io/
 [14]: https://ant.design/docs/react/introduce
