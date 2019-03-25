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
<a href="https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title=""><img data-attachment-id="3007" data-permalink="https://cpbotha.net/2018/01/21/weekly-head-voices-128-water-water-everywhere-but-not-a-drop-to-drink/bbay-pano-20180121/" data-orig-file="https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121.jpg" data-orig-size="7086,2258" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;2.2&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;iPhone 6s&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1516548081&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;4.15&quot;,&quot;iso&quot;:&quot;25&quot;,&quot;shutter_speed&quot;:&quot;0.00042900042900043&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;1&quot;}" data-image-title="bbay-pano-20180121" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121-300x96.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121-1024x326.jpg" class="alignnone size-large wp-image-3007" src="https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121-1024x326.jpg" alt="" width="840" height="267" srcset="https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121-1024x326.jpg 1024w, https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121-300x96.jpg 300w, https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121-768x245.jpg 768w, https://cpbotha.net/wp-content/uploads/2018/01/bbay-pano-20180121-1200x382.jpg 1200w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" /></a>

Hey friends, welcome back!

We have to talk about the water situation, seeing that Cape Town is now in the international news as [being on track to be the first major city EVAR to run out of water][1].

In short, if it doesn&#8217;t rain in substantial amounts during the coming three months (which history and projections say it won&#8217;t), [the municipal water supply will be shut off on April 21][2], a date festively referred to as _Day Zero_.

This means when we try to open any tap, no water will come out. This situation might continue for quite a while, which is pretty intense.

On that day, we will be celebrating by dressing up as Kevin Costner and running around barefoot shouting &#8220;NOTHING&#8217;S FREE IN WATERWORLD!&#8221;. Those who are not big fans of Kevin are allowed to dress up as [Imperator Furiosa][3].

At my house, we stopped watering our garden with municipal water months ago. We installed a grey water recovery system: Shower and bath water ends up in the only remaining green corner of the garden.

We also installed a rain water recovery system three months ago, which has fortunately enabled us to collect a few thousand litres of rain water via the rerouted gutters and pipework from the roof. This water we will probably use after Day Zero to be able to wash and to flush a toilet now and then.

(Flushing frequency has necessarily decreased significantly. Around these parts we now have the saying: &#8220;If it&#8217;s yellow, let it mellow. If it&#8217;s br\***, flush it down.&#8221; Please excuse the mental graphics.)

We have been managing to keep our use of municipal water under the requested 87 litres per person per day. Starting on February 1, we will have to stay consistently under 50 litres per person per day, including drinking, cooking and washing. I guess 2 minute showers were wasting too much of my time in any case.

I have to do more research and corroboration (fingers are being pointed in all directions), but it seems the fundamental issue is not so much the current drought alone, but to a large extent mismanagement by _both_ local and national government. It&#8217;s complicated, and politics is involved, so read at least [this][4] (otherwise good piece, but author is a DA / local government apologist), [this][5] (DA / local government IS to blame) and [this][6] (a longer, more balanced piece) to start with.

That being said, I _am_ happy that a large part of the populace has become much more water efficient. If we get through this, in spite of &#8220;this&#8221; being called &#8220;the new normal&#8221;, I hope that we retain our mad Dune-grade water saving skills.

With that out of the way, it would be sort of anti-climactic for me to talk extensively about what-I-did-last-week, so I&#8217;m going to limit it to a REAL bullet list (ping me in the comments if something interests you):

  * [pipenv][7] is the bee&#8217;s knees, I have switched my non-miniconda projects.
  * convincingly but fortunately only temporarily locked myself out of my one laptop due to TCG-Opal hardware encryption, UEFI32, UEFI64 and legacy boot incompatibilities. I&#8217;m getting old, I used to NOT lock me out of my laptop in my sleep.
  * A compulsive twitch made me fix years of old-style broken youtube shortcodes using the [wordpress regex plugin][8]. The regexp you are looking for is `/\[youtube\](.*)\[\/youtube\]/` which you can replace with `\1`.
  * [People dislike really smart leaders][9]. See water crisis above for one possible reason why this is a bad thing.
  * In spite of having invested a significant amount of time in deciding on the [Office UI Fabric React components][10] for my most major side-project (#38465 if you&#8217;ll recall), I switched to [Semantic UI React][11] (which was also in the running, together with [Palantir&#8217;s blueprint][12], [HP&#8217;s grommet][13], [Alibaba&#8217;s Ant Design of React][14] and more) at the last minute. I am happier now.

That&#8217;s it from me for now. Have fun this week kids, I hope to see you soon!

&nbsp;

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