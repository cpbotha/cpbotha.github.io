---
title: Dear USA, my data has left your building.
author: cpbotha
type: post
date: 2013-09-15T18:02:00+00:00
url: /2013/09/15/dear-usa-my-data-has-left-your-building/
categories:
  - nerd
  - tech
tags:
  - dropbox
  - gchq
  - gmail
  - nsa
  - pgp
  - prism
  - prismbreak
  - privacy
  - security
  - snowden
  - synology

---
NSA, GCHQ, Prism, FISA, Project Bullrun, Sigint.

After [Edward Snowden][1], former CIA and NSA employee, started revealing how massively, intensely and _easily_ we are all being spied upon by the intelligence agencies of various governments, the terms above have suddenly been spending a great deal more time in the media.
{{< figure src="/wp-content/uploads/2013/09/tumblr_mp3xgwYLsi1qz82gvo1_1280.jpg" link="/wp-content/uploads/2013/09/tumblr_mp3xgwYLsi1qz82gvo1_1280.jpg" caption="Image by BLOGGING via TYPEWRITER">}} 

It turns out that government agencies are allowed to extract, at a whim, your and my data from service providers, such as Google, Microsoft and Yahoo. There is no real legal process (unless you can call a secret judge in a secret court giving a secret order a real legal process), _especially_ if you’re not a US citizen, and the providers that have been forced to give up your data in this way are not allowed to notify you about your digital self being violated. So even if they _say_ that you shouldn’t worry, _you can never be entirely sure_.

Furthermore, it has also been revealed that the NSA has for years being acquiring encryption keys via legal (secretly forcing companies to give them the keys) and extra-legal (simply hacking into company servers) means. Even worse, they have for years been deliberately introducing security weaknesses into software products and encryption software in order to be able to crack open your data even more easily.

You can read more about this state of affairs in [The Guardian’s NSA files][3]. The Guardian has been doing a sterling job of analysing and bringing to light the depths to which our governments have sunk. There’s a whole lot of information, and most of it is quite upsetting.

For me the final straw was when secure email service [lavabit][4] voluntarily shut itself down, when faced with the prospect of being forced to leak user information to the US government without being allowed to tell anyone. The message on the site is quite chilling, and concludes with the following:

> This experience has taught me one very important lesson: without congressional action or a strong judicial precedent, I would _strongly_ recommend against anyone trusting their private data to a company with physical ties to the United States.

At this point, I was a super happy and pretty heavy user of a number of US-based services, including GMail (all my email, about 40000 conversations consisting of 60000 mails, that’s excluding my work email which I also hosted on GMail), Google+ Photos (all my photos, about 21000 of ’em), Google Drive, Dropbox (50G of data spread out over 120000 files). _In all cases, I still consider these to be best of class services._ In putting my money where my mouth is, I was paying both Google and Dropbox for extra storage.

I also had no problem with Google filtering through my email to show me targeted advertising. This is the deal I had with them. I also had no problem with the possibility of someone getting my data after due legal process. However, the idea that some NSA or other government agency flunky could quite easily stick their grubby paws into my data, and that I would never know about this, was too much.

There’s probably nothing much of interest in my data. However, it has become a matter of principle; Privacy is a basic human right. [Here’s an old essay by Bruce Schneier][5] if you need to read more about why privacy is so important.

In short: **It was time to extricate all of my lovely data from probably well-meaning US companies, thanks to the ridiculously powerful and secretive NSA, and thanks to all of its shadowy counterparts around the world.**

Here’s how I did it:

  * Considered building another low-cost Linux server, or even a Raspberry Pi. Decided against this due to time required for configuration and acquired a Synology DS213j NAS, which is at this moment standing on the desk about 1 metre to my left. My recommendation: Just get this, you won’t be sorry.
  * Downloaded 60000 emails to Synology using Thunderbird mail client. Deleted everything from GMail. Google engineers assure me that after a few months, data will _really_ be gone.
  * My webhoster ([WebFaction][6]) receives mail for all my domains. My Synology retrieves mail every 5 minutes via POP (you can set this up via Roundcube on the Synology) and deletes it from WebFaction.
  * Outgoing mail is relayed by the Synology via the WebFaction SMTP server. I don’t have to worry too much about blacklisting and whatnot, my hoster does this.
  * I’m back to interacting with my mail using Thunderbird and IMAP SSL. The loss of GMail conversation view was initially really REALLY painful. People have forgotten the ancient art of quoting. However, I’ve configured Thunderbird to archive all mail to year-stamped archive folders, and to put my sent mail there. Poor-man’s Conversation View! (the [conversations plugin][7] is wonky. it’s shocking how much the availability of GMail, which works really well, has stunted the development of alternative email clients) Importantly, I am now able to use [OpenPGP][8] again for the strong encryption and cryptographic signing of my emails.
  * On my Android telephone (whoops…) I am using [the Kaiten IMAP client][9].
  * All the data I had in Dropbox is now being synced between the Synology, two laptops and a workstation using [BitTorrent Sync][10]. This peer-to-peer syncing system is still a little rough around the edges, but falls squarely in the category of “Best Things Since Sliced Bread”, and it’s _FAST_. CloudStation, Synology’s dropbox-inspired solution, was just far too slow on my Synology model.
  * My photos (21000 of them) have been downloaded from Google+ Photos (thank you [Google Takeout][11]) and are now being served from the Synology using PhotoStation.
  * My music (5400+ tracks) is downloading from Google Music as we speak, and will be served from the Synology using AudioStation.
  * I make incremental backups of everything to an encrypted external USB drive, using [dirvish][12]. I will probably add an extra external drive to the mix and try to keep that off site.

It’s been an interesting process moving my stuff out, and getting used to these alternative systems is sometimes slightly uncomfortable, but I am quite happy with the end result. I hope that more people will take this step, and I really hope that more and easier-to-use alternatives for secure email (such as [mailpile][13]) and for ubiquitous private data will become available.

# Addendum 2013-09-16

My [submission of this post][14] spent some time on the Hacker News front page, and from there was [picked up by reddit][15] as well. This brought many comments, a number of which were positive and thoughtful, and a number of which that were far less so. It’s amazing how anonymity and comment sections can bring out the worst in people. (if you have to know, the Hacker News community is generally MILES more polite than reddit)

In any case, I wanted to clarify an issue or two: After moving my data away from GMail and Dropbox, I am not under any impression that my data is now secure. I can still be hacked. My hardware and software could be full of backdoors. My email will still be read as it jumps from server to server, probably ending up in someone else’s GMail. :) However, if more people were to move their data out to their own premises, it becomes more complicated and costly for government agencies to monitor us all. At the moment, the NSA cuts deals with a few large email and other cloud service providers, and with that they’re able to monitor large swathes of users. However, if more of those users were to move away, many more deals have to be cut and servers hacked, costing more time and more money. Add to that increased used of OpenPGP (which I do use, and mention in my post), and it becomes even more difficult. I know that I’m just a drop in a bucket, but hey, at least I am a drop in a bucket!

My goal with posting this was to show that it’s relatively easy to move much of your data away. I have the feeling that many of the most impolite anonymous commenters still store their data with cloud providers, and would really prefer to believe that there are no worthwhile alternatives, hence all the ad hominem attacks.

Fortunately, each polite and humane comment makes up for a whole pile of bad ones. :)

 [1]: http://en.wikipedia.org/wiki/Edward_Snowden "Edward Snowden wikipedia page"
 [2]: http://inothernews.tumblr.com/image/54099907452
 [3]: http://www.theguardian.com/world/the-nsa-files "The Guardian NSA files"
 [4]: http://lavabit.com/ "lavabit website with close-down message"
 [5]: http://www.wired.com/politics/security/commentary/securitymatters/2006/05/70886 "value of privacy by Bruce Schneier"
 [6]: https://www.webfaction.com/
 [7]: https://addons.mozilla.org/en-us/thunderbird/addon/gmail-conversation-view/
 [8]: http://www.openpgp.org/
 [9]: https://play.google.com/store/apps/details?id=com.kaitenmail&hl=en "Kaiten email on the Google Play store"
 [10]: http://labs.bittorrent.com/experiments/sync.html "bittorrent sync"
 [11]: https://www.google.com/takeout/ "Google Takeout"
 [12]: http://www.dirvish.org/ "dirvish website"
 [13]: http://www.mailpile.is/ "mailpile website"
 [14]: https://news.ycombinator.com/item?id=6392322
 [15]: http://www.reddit.com/r/technology/comments/1mhpqj/dear_usa_my_data_has_left_your_building/
