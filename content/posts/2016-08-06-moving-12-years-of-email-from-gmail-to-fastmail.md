---
title: Moving 12 years of email from GMail to FastMail
author: cpbotha
type: post
date: 2016-08-06T20:22:04+00:00
url: /2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/
featured_image: https://cpbotha.net/wp-content/uploads/2016/08/fastmail_vs_gmail_671x200.png
categories:
  - review
tags:
  - carddav
  - fastmail
  - gmail
  - IMAP
  - jmap
  - todoist
  - webmail

---
In 2013, when it became clear, primarily through Edward Snowden&#8217;s heroic actions, that the level of snooping by the US and other governments was far greater than any of us would have thought, I moved all of my data out of the US and of course [blogged about it][1] (that blog post has been read almost 70000 times; I think for many people this is an important issue).

This included migrating 60000 emails away from my beloved GMail (I got my GMail invite from [The Vogon Poet][2] on August 24, 2004. At that time, you could only get GMail by invitation. It was pretty exciting! (I have emails from before 2004, back to &#8217;93 or &#8217;94, but those are in a backup archive somewhere.)) to the little [Synology DS213j][3] standing next to my desk at the time.  This was all well and good behind the stable Dutch 100 Mbit/s _down_ / 10 Mbit/s _up_ cable connection I had, but when we decided to move back to South Africa, where home internet is a few years behind The Netherlands, I ended up having to pay for a virtual private server in Cape Town (to keep latency between me and my mail server manageable) and having to admin my own dovecot IMAP and postfix SMTP server.

Initially this was workable, until the Nth time that I had to interrupt my real job (which has nothing to do with mail servers) to apply a security patch or get the VPS booting again after a botched kernel upgrade. Besides that, I had to deal with keeping my server out of over-enthusiastic spam blacklists and whatnot. Also, inspite of [mu4e][4], I did end up missing the fast graphical GMail web interface.

So, it was with a great deal of tail between my legs that on June 10, 2015 ([I have a lab journal, remember][5]) I went right back back to GMail. My mail setup, although pleasingly decentralised, was costing me too much time and hence actual money.

Fast forward to July 15, 2016 (there&#8217;s that lab journal again&#8230;) when, after receiving an email from Google asking me to indicate how exactly I would like them to use my data to customise adverts around the web, and after thinking for a bit about what kind of machine learning tricks I would be able to pull on you with 12 years of your email, I decided that I really had to make alternative plans for my little email empire.

Somehow FastMail came up and in one of those impulsive LET&#8217;S WASTE SOME TIME manoeuvres, I pressed the big red MIGRATE button!

The rest of this post is my mini-review of the FastMail service after almost 3 weeks of intensive use.

# Importing mail from GMail<figure id="attachment_2458" aria-describedby="caption-attachment-2458" style="width: 300px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM.png" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2458" data-permalink="https://cpbotha.net/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/screen-shot-2016-08-06-at-10-50-45-am/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM.png" data-orig-size="1456,844" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screen Shot 2016-08-06 at 10.50.45 AM" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM-300x174.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM-1024x594.png" class="wp-image-2458 size-medium" src="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM-300x174.png" alt="The main import & export window" width="300" height="174" srcset="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM-300x174.png 300w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM-768x445.png 768w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM-1024x594.png 1024w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM-1200x696.png 1200w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-10.50.45-AM.png 1456w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-2458" class="wp-caption-text">The main import & export window</figcaption></figure> <figure id="attachment_2461" aria-describedby="caption-attachment-2461" style="width: 300px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM.png" data-rel="lightbox-image-1" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2461" data-permalink="https://cpbotha.net/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/screen-shot-2016-08-06-at-11-01-46-am/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM.png" data-orig-size="850,670" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screen Shot 2016-08-06 at 11.01.46 AM" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM-300x236.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM.png" class="wp-image-2461 size-medium" src="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM-300x236.png" alt="IMAP migration configuration dialog" width="300" height="236" srcset="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM-300x236.png 300w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM-768x605.png 768w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.01.46-AM.png 850w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-2461" class="wp-caption-text">IMAP migration configuration dialog</figcaption></figure> 

The **Settings | Import & Export** option in FastMail was easy to setup. It knows how to authenticate with GMail, even when you make use of two-factor authentication, like I do and you probably should.

The import takes place via the GMail IMAP interface. It&#8217;s important to remember that via the IMAP client, an email tagged in GMail with both _important_ and _info_ will appear in two different folders. Because of this, I did check the **no duplicates** checkbox, but still I noticed that my 15 GB FastMail evaluation mailbox was filling up more quickly than I would have expected.

After a support request which was responded to within minutes (bonus), I discovered the **Quota Usage** screen and could see that the duplicate detection did indeed not seem to work correctly during the import. Based on more tips from the support tech, I made use of the **Mass delete or remove duplicates** module (Settings | Folders | Scroll all the way to the bottom of the page) to delete thousands of duplicate emails during the import. This was indeed because of emails appearing in multiple IMAP folders due to their GMail tags. _**Note:** Friend and reader [stefanvdwalt][6] reported the exact same mail duplication during import issue which in his case did go over quota, so do keep an eye on this!_

After a day or so (during which I could email more or less normally) I received an import report from FastMail claiming that the import had been successful, except for this error:

<pre>Log: Fri Jul 15 17:49:17 2016; cpbotha/imap.gmail.com; Migrating folder Inbox -&gt; Inbox
Log: Fri Jul 15 17:49:17 2016; cpbotha/imap.gmail.com; Creating local folder Inbox
Log: Fri Jul 15 17:49:17 2016; cpbotha/imap.gmail.com; Error migrating remote folder Inbox: Failed to create Inbox. IMAP Command : 'create' failed. Response was : no - Mailbox already exists</pre>

The import had managed to figure out that GMail Sent should map to FastMail Sent for example, but Inbox was probably too special to map in the same way. I fixed this by firing up my trusty Thunderbird, and using IMAP to drag and drop emails from my GMail Inbox to my shiny new FastMail Inbox.

In retrospect, I should have selected **Create under new sub-folder** in the IMAP migration configuration instead of **Merge into existing folders**. I discovered later that **moving thousands of emails to a different folder is near instantaneous** in the FastMail web-app.

# What I like

## Webmail speed

I live more or less at the southern tip of the African continent. My lowest latency connection with the rest of the internet is via undersea optic cable to Europe (about 140ms ping).

The FastMail web servers are in the USA, which is, as the ping flies, much further away. I was not expecting much from the webmail, but colour me surprised when I discovered that this felt subjectively _faster_ than GMail (who have servers everywhere, even down here). Things remained snappy, even with all 50000 of my conversations imported.

As far as I can figure out, it seems that much of this is due to FastMail&#8217;s self-designed but open source IMAP-replacement called [JMAP][7]. JMAP has been designed for low latency, and for improved battery life. What it does differently, is batch requests together, and it also has optimisations specifically for interactive webmail.

The web-app has full support for keyboard shortcuts, which increases the subjective perception of speed.

## Webmail search

For my purposes, search in FastMail is on par with that of GMail. I can dig up any of my emails, back up to 2004, in seconds.<figure id="attachment_2463" aria-describedby="caption-attachment-2463" style="width: 259px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM.png" data-rel="lightbox-image-2" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2463" data-permalink="https://cpbotha.net/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/screen-shot-2016-08-06-at-11-18-06-am/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM.png" data-orig-size="866,1002" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screen Shot 2016-08-06 at 11.18.06 AM" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM-259x300.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM.png" class="wp-image-2463 size-medium" src="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM-259x300.png" alt="FastMail advanced search interface" width="259" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM-259x300.png 259w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM-768x889.png 768w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-11.18.06-AM.png 866w" sizes="(max-width: 259px) 85vw, 259px" /></a><figcaption id="caption-attachment-2463" class="wp-caption-text">FastMail advanced search interface</figcaption></figure> 

What&#8217;s also very useful, is that you can turn any search into a virtual folder.

## Tech support

This is one area where Google really can&#8217;t hold a candle to FastMail. If something goes wrong with your gmail account (this hardly ever happens, but it&#8217;s possible) it&#8217;s almost impossible to get hold of any kind of official tech support. Here&#8217;s [a recent story][8] where a GMail user&#8217;s account was summarily terminated. There _was_ probably some kind of ToS infringment, but the user has no idea what or why, and has lost all access to their emails and contacts database.

So far I&#8217;ve contacted FastMail tech support twice: Once during my email migration, and once to confirm the absence of the &#8220;quote selected text in reply&#8221; feature (discussed below). In both cases, I was helped by real humans who responded very quickly and courteously to my support requests.

# Email and contacts (and calendar) out of Google&#8217;s view

I&#8217;m still of the opinion that Google makes fantastic and valuable products. However, with all of their data mining know-how and resources, one has to decide how much of one&#8217;s personal information one is willing to trade in for the use of these fantastic products.

With FastMail, I have been able to extricate my significant email archive (2004 to 2016, 50000 conversations) as well as my contacts database. I&#8217;m still making use of Google Calendar, because of bunches of sharing going on with family members, but I have the option of moving that out also.

By the way, the FastMail Calendar web interface is more than capable (and pretty enough) to replace Google&#8217;s version.

# What I don&#8217;t like

## Missing integrations: Todoist

GMail, being as popular as it is, has tonnes of integrations with other apps. In my case, I will really miss the [Todoist for Gmail extension][9]. With this, I had a mini-todoist window inside my GMail, and I could turn any email into a task at the click of a button (or the press of a shortcut).

Because FastMail email URLs seem to be persistent, I use the [Todoist Chrome extension&#8217;s][10] &#8220;Add to Todoist&#8221; context menu action to add the URL and email subject as a task. This not as nice as the gmail-specific extension (the task goes immediately into the todoist inbox, without the possibility to edit metadata such as due date and tags).

## Missing feature: Quote selection in reply

In Gmail and in Thunderbird, if you select text in an incoming email and then reply, that selected text is quoted in the reply email. Unfortunately, this feature is not available in the FastMail web-app, and they have no plans to implement it.

I use both the FastMail web-interface as well as Thunderbird, because of its great PGP email encryption and signature support (hey, [find me on keybase][11], send me encrypted email!), so this issue is somewhat ameliorated. Still, it would have been nice.

## Android app lag

I do have [FastMail&#8217;s Android app][12] on my telephone. The app is a Cordova / PhoneGap / CrossWalk style unit with real-time email push and notification via Google Cloud Messaging (this is a relatively energy-efficient way for android phones to get push notification and is natively supported by FastMail).

However, there is a few second lag when I open the inbox, so I prefer using the pro version of [AquaMail, a great Android IMAP mail client][13]. I have this set to 15 minute polling for new email, as IMAP IDLE (push, in other words) is not as battery efficient as GCM or Apple&#8217;s email push. Opening any folder or email in AquaMail is of course instantaneous, as the emails live on the phone.

That being said, I use the FastMail app for searching, which is just as fast and as effective as the web-app.

THAT being said, FastMail really needs to implement some sort of caching in the Android app for lightning _fast_ folder and email access. (The FastMail app is quite attractive, I would prefer using it more.)<figure id="attachment_2477" aria-describedby="caption-attachment-2477" style="width: 300px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play.png" data-rel="lightbox-image-3" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2477" data-permalink="https://cpbotha.net/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/fastmail_calendar_google_play/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play.png" data-orig-size="1280,725" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="fastmail_calendar_google_play" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play-300x170.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play-1024x580.png" class="size-medium wp-image-2477" src="https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play-300x170.png" alt="FastMail Android app Calendar screen, from the Google Play page." width="300" height="170" srcset="https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play-300x170.png 300w, https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play-768x435.png 768w, https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play-1024x580.png 1024w, https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play-1200x680.png 1200w, https://cpbotha.net/wp-content/uploads/2016/08/fastmail_calendar_google_play.png 1280w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-2477" class="wp-caption-text">FastMail Android app Calendar screen, from the Google Play page.</figcaption></figure> 

## Niggle: Creating an email alias / incoming route automatically creates a new sending identity

FastMail can manage the DNS for any of the custom domains that you assign to it, which is super useful if you don&#8217;t already have a DNS service.

I already make use of webfaction&#8217;s DNS for all of my domains, so I chose to add DNS records to designate fastmail as the official MX for those domains. (All of this is explained clearly in the FastMail help.)

When you do this, you have to create an email alias for each incoming address you would like to receive mail for (you can also create a catchall, but this could result in more spam arriving in your inbox). For each and every alias, [FastMail automatically creates an outgoing (from address) identity][14]. While this is usually quite convenient, I have quite a number of incoming addresses, but I only ever send from a subset of these addresses, so the drop-down list with sending identities became quite unwieldy.

I deleted all of the unnecessary identities. What would help, would be if FastMail were to implement most-used-at-the-top sorting for that drop-down.

# Other noteworthy points

## Domain setup

For my most important domains, I have set FastMail to be the MX. I have also performed the necessary [SPF and DKIM][15] setup: FastMail gives super useful feedback in its configuration screens to help you with this. For these domains, I send mail directly via the FastMail SMTP servers, and mail is delivered directly to FastMail servers. Nice and simple.<figure id="attachment_2470" aria-describedby="caption-attachment-2470" style="width: 300px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM.png" data-rel="lightbox-image-4" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2470" data-permalink="https://cpbotha.net/2016/08/06/moving-12-years-of-email-from-gmail-to-fastmail/screen-shot-2016-08-06-at-9-46-01-pm/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM.png" data-orig-size="1634,994" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screen Shot 2016-08-06 at 9.46.01 PM" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM-300x182.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM-1024x623.png" class="size-medium wp-image-2470" src="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM-300x182.png" alt="Domain setup feedback screen." width="300" height="182" srcset="https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM-300x182.png 300w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM-768x467.png 768w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM-1024x623.png 1024w, https://cpbotha.net/wp-content/uploads/2016/08/Screen-Shot-2016-08-06-at-9.46.01-PM-1200x730.png 1200w" sizes="(max-width: 300px) 85vw, 300px" /></a><figcaption id="caption-attachment-2470" class="wp-caption-text">Domain setup feedback screen.</figcaption></figure> 

For some other email accounts I have with clients, FastMail supports POP fetch from and SMTP send via foreign servers.

## iOS Push support

If you use any Apple iOS devices to read your mail, you&#8217;ll be pleased to know that FastMail, with help from the big A, [fully supports iOS push][16]. This means battery efficient real-time incoming emails to make it even more difficult for you to focus on That One Really Important Thing.

## Android contact syncing with CardDAV

With google contacts, syncing on Android just works, and it works really well. To sync my contacts with FastMail&#8217;s Address Book instead, I bought the pro version of the [CardDAV android app][17] for 24 South African Ront (that&#8217;s about EUR 1.5). This works as a sync provider, so once setup, the process is also pretty much transparent.

# Final thoughts

So there you have it: A hopefully helpful story, with included mini-review, about my move from GMail to the FastMail service.

So far, my conclusion is that this is a service that is technically more than capable of replacing GMail, even for power users. Furthermore, FastMail&#8217;s primary (and in fact only) business model is to charge you money for making sure that you can keep on emailing like a boss. Together, this makes for an offer that I could not refuse.

_P.S. Let me know in the comments if you would like me to add anything else to this post._

_P.P.S. You can also join the lively [Hacker News discussion of this post][18]!_

 [1]: /2013/09/15/dear-usa-my-data-has-left-your-building/
 [2]: https://twitter.com/vogonpoet
 [3]: https://www.engadget.com/products/synology/ds213j/
 [4]: https://vxlabs.com/2014/06/06/configuring-emacs-mu4e-with-nullmailer-offlineimap-and-multiple-identities/
 [5]: /2016/01/05/note-taking-strategy-early-2016/
 [6]: https://twitter.com/stefanvdwalt
 [7]: http://jmap.io/
 [8]: https://medium.com/@xdvl/stop-using-gmail-com-for-things-you-care-about-14af40e43a88#.h5ljyewg7
 [9]: https://chrome.google.com/webstore/detail/todoist-for-gmail/clgenfnodoocmhnlnpknojdbjjnmecff
 [10]: https://chrome.google.com/webstore/detail/todoist-to-do-list-and-ta/jldhpllghnbhlbpcmnajkpdmadaolakh
 [11]: https://keybase.io/cpbotha
 [12]: https://play.google.com/store/apps/details?id=com.fastmail.app
 [13]: https://play.google.com/store/apps/details?id=org.kman.AquaMail
 [14]: https://www.fastmail.com/help/receive/alias-catchall.html
 [15]: https://blog.fastmail.com/2014/12/09/email-authentication/
 [16]: https://blog.fastmail.com/2015/07/17/push-email-now-available-in-ios-mail/
 [17]: https://play.google.com/store/apps/details?id=org.dmfs.carddav.Sync
 [18]: https://news.ycombinator.com/item?id=12247401
