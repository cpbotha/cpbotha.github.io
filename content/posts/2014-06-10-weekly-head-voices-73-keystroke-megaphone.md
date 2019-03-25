---
title: 'Weekly Head Voices #73: Keystroke megaphone!'
author: cpbotha
type: post
date: 2014-06-10T18:42:00+00:00
url: /2014/06/10/weekly-head-voices-73-keystroke-megaphone/
categories:
  - weekly head voices
tags:
  - deft
  - emacs
  - Jeff Atwood
  - Jon Udell
  - mu4e
  - org2blog
  - Scott Hanselman

---
In week 23 of 2014 I nerded out by writing two Emacs-related blog posts over at the vxlabs, and hacking org2blog to support WordPress image thumbnails: 

<ul class="org-ul">
  <li>
    <a href="http://vxlabs.com/2014/06/04/modify-emacs-deft-for-recursive-directory-search/">Modify Emacs Deft for recursive directory search</a> &#8211; this shows you how you can modify Emacs Deft mode, a Notational Velocity clone, to handle nested directories.
  </li>
  <li>
    <a href="http://vxlabs.com/2014/06/06/configuring-emacs-mu4e-with-nullmailer-offlineimap-and-multiple-identities/">Configuring Emacs mu4e with nullmailer, offlineimap and multiple identities</a> &#8211; this post documents my complete Emacs-based mail client setup.
  </li>
  <li>
    <a href="https://github.com/cpbotha/org2blog">org2blog image-thumbnail fork</a> on github &#8211; this is my first significant Emacs package hack! Using this, you can configure org2blog to make use of the image thumbnails automatically created by WordPress on image upload. By default, it will insert the 300px thumbnail into your post and link to the full size image, instead of just inserting the full size version.
  </li>
</ul>

<div id="outline-container-sec-1" class="outline-2">
  <h2 id="sec-1">
    Conserving keystrokes
  </h2>
  
  <div class="outline-text-2" id="text-1">
    <p>
      Besides the general Emacs frenzy I&#8217;m going through at the moment, there is some method to my madness, especially the org2blog part. Through <a href="http://vxlabs.com/2014/05/25/emacs-24-with-prelude-org2blog-and-wordpress/">Emacs and org2blog</a>, it has become significantly easier for me to publish a blog post. I&#8217;m in Emacs the whole day in any case (email and text notes database), so turning any piece of existing text into a blog post now takes no more than a minute or two.
    </p>
    
    <p>
      Why is that interesting?
    </p>
    
    <p>
      Well, in 2007, Jon Udell (we&#8217;ll forget for a while that he works for the enemy, because the man talks sense) wrote <a href="http://blog.jonudell.net/2007/04/10/too-busy-to-blog-count-your-keystrokes/">a blog post</a> urging his readers to count their keystrokes. Here are three selected paragraphs:
    </p>
    
    <blockquote>
      <p>
        When people tell me they’re too busy to blog, I ask them to count up their output of keystrokes. How many of those keystrokes flow into email messages? Most. How many people receive those email messages? Few. How many people could usefully benefit from those messages, now or later? More than a few, maybe a lot more.
      </p>
      
      <p>
        From this perspective, blogging is a communication pattern that optimizes for the amount of awareness and influence that each keystroke can possibly yield. Some topics, of course, are necessarily private and interpersonal. But a surprising amount of business communication is potentially broader in scope. If your choice is to invest keystrokes in an email to three people, or in a blog entry that could be read by those same three people plus more — maybe many more — why not choose the latter? Why not make each keystroke work as hard as it can?
      </p>
      
      <p>
        [converting an email to a blog post] can have powerful network effects. To exploit them, you have to realize that the delivery of a message, and the notification of delivery, do not necessarily coincide. Most of the time, in email, they do. The message is both notification and payload. But a message can also notify and point to a payload which is available to the recipient but also to other people and processes in other contexts. That arrangement costs hardly any extra keystrokes, and hardly any extra time. But it’s an optimization that can radically expand influence and awareness.
      </p>
    </blockquote>
    
    <p>
      I&#8217;ve reproduced the same paragraphs that Jeff Atwood (co-creator of Stack Overflow, together with Joel Spolsky, I&#8217;M NOT WORTHY) extracted in <a href="http://blog.codinghorror.com/maximizing-the-value-of-your-keystrokes/">his blog post on the matter</a>, where he exhorted us with the question:
    </p>
    
    <blockquote>
      <p>
        The next time you find yourself typing more than a few sentences on your keyboard, stop and ask: are you maximizing the value of your keystrokes?
      </p>
    </blockquote>
    
    <p>
      (Scott Hanselman, like Udell also with the enemy but again a source of internet wisdom (hey, what&#8217;s up with that?!), is a strong proponent of this idea, see for example <a href="http://www.hanselman.com/blog/DoTheyDeserveTheGiftOfYourKeystrokes.aspx">his 2010 post on the matter</a>.)
    </p>
  </div>
</div>

<div id="outline-container-sec-2" class="outline-2">
  <h2 id="sec-2">
    Normal human stuff
  </h2>
  
  <div class="outline-text-2" id="text-2">
    <p>
      I haven&#8217;t felt this cold in a long long time. Because winter here is usually short and/or mild and the summers are long and, err, <i>summery</i>, houses are not really well geared for the cold season. At night, the temperature inside my house approaches that of outside.
    </p>
    
    <p>
      That&#8217;s why I&#8217;m counting down the days until June 21 (sorry Northern Hemisphere friends). It might be the middle of winter over here, but it&#8217;s also the point after which the days starting getting slowly longer and warmer.
    </p>
    
    <p>
      While me wait, there are sunsets like this one on Friday, at the Stone Three company braai:
    </p><figure style="width: 300px" class="wp-caption alignnone"><a href="http://cpbotha.net/wp-content/uploads/2014/06/wpid-strand_sunset.jpg" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">
    
    <img src="http://cpbotha.net/wp-content/uploads/2014/06/wpid-strand_sunset-300x225.jpg" /></a><figcaption class="wp-caption-text">Sunset, seen from the Strand Yacht Club on Friday June 6, 2014.</figcaption></figure> 
    
    <p>
      &#x2026; and lovely beers like this one:
    </p><figure style="width: 300px" class="wp-caption alignnone"><a href="http://cpbotha.net/wp-content/uploads/2014/06/wpid-johnny_gold.jpg" data-rel="lightbox-image-1" data-rl_title="" data-rl_caption="" title="">
    
    <img src="http://cpbotha.net/wp-content/uploads/2014/06/wpid-johnny_gold-300x225.jpg" /></a><figcaption class="wp-caption-text">Look how the sun sets ever so artfully on my Johnny Gold!</figcaption></figure> 
    
    <p>
      &#x2026; to keep me busy.
    </p>
    
    <p>
      Have a great week kids!
    </p>
  </div>
</div>