---
title: 'Weekly Head Voices #71: Vote for the future.'
author: cpbotha
type: post
date: 2014-05-24T20:27:40+00:00
url: /2014/05/24/weekly-head-voices-71-vote-for-the-future/
categories:
  - weekly head voices
tags:
  - emacs
  - email
  - mu4e
  - star trek

---
On Wednesday May 7, together with just over 18 million other South Africans, I voted. Afterwards, my thumb looked like this:<figure id="attachment_1873" aria-describedby="caption-attachment-1873" style="width: 300px" class="wp-caption aligncenter"><a href="http://cpbotha.net/wp-content/uploads/2014/05/voting\_thumb.jpg" data-rel="lightbox-image-0" data-rl\_title="" data-rl_caption="" title="">

<img data-attachment-id="1873" data-permalink="https://cpbotha.net/2014/05/24/weekly-head-voices-71-vote-for-the-future/voting_thumb/" data-orig-file="https://cpbotha.net/wp-content/uploads/2014/05/voting_thumb.jpg" data-orig-size="1024,838" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;2.65&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;Nexus 4&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;1399484141&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;4.6&quot;,&quot;iso&quot;:&quot;100&quot;,&quot;shutter_speed&quot;:&quot;0.016666666666667&quot;,&quot;title&quot;:&quot;&quot;}" data-image-title="voting_thumb" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2014/05/voting_thumb-300x245.jpg" data-large-file="https://cpbotha.net/wp-content/uploads/2014/05/voting_thumb.jpg" class="size-medium wp-image-1873" src="http://cpbotha.net/wp-content/uploads/2014/05/voting_thumb-300x245.jpg" alt="POWER THUMB!" width="300" height="245" srcset="https://cpbotha.net/wp-content/uploads/2014/05/voting_thumb-300x245.jpg 300w, https://cpbotha.net/wp-content/uploads/2014/05/voting_thumb-535x437.jpg 535w, https://cpbotha.net/wp-content/uploads/2014/05/voting_thumb.jpg 1024w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-1873" class="wp-caption-text">POWER THUMB!</figcaption></figure> 

&#8230; and the rest of me felt **like a million bucks**!

Some complained about the outcome. I think we&#8217;re moving, albeit slowly, in the direction of a healthy democracy. Here are [this year&#8217;s results][1], and here are [2009&#8217;s results][2]. The opposition has been growing (slowly) at a national level. Interestingly, in Gauteng, smallest province with all of the money and power, the opposition is making similar progress.

Late to the party as per usual, I discovered [Vagrant][3], a fantastic command-line tool to create, use and destroy virtual machines AT A WHIM. I was so happy with this that I created <a title="vagrant screencast" href="http://youtu.be/sY0wNgTpEOg" data-rel="lightbox-video-0">this screencast</a>, which has the added advantage of being an effective component of insomnia treatment. (Yes, I do know about and have even played with Docker. For what I&#8217;m doing now (deploying multiple self-contained servers on on-premises servers without direct access), vagrant+virtualbox fits better.)

On the topic of nerdy software, let&#8217;s turn the dial to 11. I&#8217;ve started using emacs 24 with [mu4e][4] as my main email client now. It looks like this:<figure id="attachment_1875" aria-describedby="caption-attachment-1875" style="width: 300px" class="wp-caption aligncenter"><a href="http://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl\_caption="" title="">

<img data-attachment-id="1875" data-permalink="https://cpbotha.net/2014/05/24/weekly-head-voices-71-vote-for-the-future/cpbotha-mu4e-screenie/" data-orig-file="https://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie.png" data-orig-size="848,732" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;}" data-image-title="cpbotha-mu4e-screenie" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie-300x258.png" data-large-file="https://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie.png" class="size-medium wp-image-1875" src="http://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie-300x258.png" alt="mu4e screenshot with nvpy search active" width="300" height="258" srcset="https://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie-300x258.png 300w, https://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie-535x461.png 535w, https://cpbotha.net/wp-content/uploads/2014/05/cpbotha-mu4e-screenie.png 848w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-1875" class="wp-caption-text">mu4e screenshot with nvpy search active</figcaption></figure> 

After leaving GMail, I made do for a while with Thunderbird, but wasn&#8217;t really happy with it. (It&#8217;s really an awesome email client, but my inner nerd wanted more.) I can honestly say that I&#8217;m in email heaven at the moment. My 68 thousand email archive is locally mirrored with [offlineimap 0.6.5][5]. mu4e in Emacs is able to perform search requests through the whole archive in milliseconds. It makes GMail seem positively snail-like in comparison. In addition, I can use my crappy elisp-fu to make it do the most silly things with the user interface and my email. Oh yes, and [zenburn][6]. Gaaaaaaaaaaah&#8230;

Completely accidentally, I saw Star Trek Into Darkness on Netflix the other night (no, we don&#8217;t have Netflix over here, really) and was completely BLOWN AWAY. Benedict Cumberbatch as Khan was an awe-inspiring movie villain. According to [the Wikipedia page on Khan Noonien Singh][7] (recurring villain in the Star Trek universe), Jonathan Romney of The Independent had the following to say about Cumberbatch&#8217;s voice:

> [It was] so sepulchrally resonant that it could have been synthesised from the combined timbres of Ian McKellen, Patrick Stewart and Alan Rickman holding an elocution contest down a well.

Dang. If you&#8217;ve seen the movie, you&#8217;ll know what he&#8217;s talking about.

Just in case you thought that we didn&#8217;t live in the future, have a look at this live video stream of the Earth, taken by the cameras of the International Space Station, which is only floating 422km above the Earth&#8217;s surface:

<iframe style="border: 0px none transparent;" src="http://www.ustream.tv/embed/17074538?v=3&wmode=direct" width="480" height="302" frameborder="0" scrolling="no"></iframe>

(read more [here][8])

 [1]: http://www.news24.com/Elections/results
 [2]: http://www.news24.com/Elections/results#year=2009
 [3]: http://vagrantup.com/
 [4]: http://www.djcbsoftware.nl/code/mu/mu4e.html
 [5]: http://offlineimap.org/
 [6]: http://slinky.imukuppi.org/zenburnpage/
 [7]: http://en.wikipedia.org/wiki/Khan_Noonien_Singh
 [8]: http://www.ustream.tv/channel/iss-hdev-payload