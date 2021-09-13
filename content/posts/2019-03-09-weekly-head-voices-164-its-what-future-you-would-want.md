---
title: 'Weekly Head Voices #164: It’s what future you would want.'
author: cpbotha
type: post
date: 2019-03-09T14:53:44+00:00
url: /2019/03/09/weekly-head-voices-164-its-what-future-you-would-want/
featured_image: https://cpbotha.net/wp-content/uploads/2019/02/strand_running_route_2-1200x900.jpg
categories:
  - weekly head voices
tags:
  - dirvish
  - dropbox
  - electricity
  - goodwe
  - google drive
  - gou
  - productivity
  - rclone
  - solar
  - sunk cost
  - time machine

---
{{< figure src="/wp-content/uploads/2019/02/strand_running_route_2-1024x768.jpg" link="/wp-content/uploads/2019/02/strand_running_route_2.jpg" caption="Pre-work not-too-shabby running route.">}} 

Welcome back friends! This WHV looks back at the two weeks from Monday February 18 to Sunday March 3, 2019. I was planning to release the edition of the WHV on time, but my need for a break was greater.

Because I’ve given up on ever mastering the art of the bullet-list form of the weekly(ish) status update, I am going to double-down on the old-fashioned sectioned prose form that you see before you.

Also, this post has again evolved into a long ramble. (It’s now Saturday March 9, time to start working on the next edition. I’m curious what form it will take.)

## GOU#1 is #2

It feels like through these posts you’ve pretty much seen [GOU#1 grow up before your eyes][1], so I’ve given myself permission to mention this moment of parental pride, hopefully quite briefly though (I write this blog not only for you, but also for me in 20 years time!):

GOU #1 has been elected as [deputy head girl][2] of her 1600+ pupil primary school!

She was really mature, also before the time, about this possible outcome of taking the #2 position. She seems to have made up her mind before the time that this would in fact be, for her, the best configuration.

This thoughtfulness of hers might have made me even more proud than the achievement itself.

## Dreams of clean solar electricity wafting ineffectually against the greasy gears of government.

Way back in December of last year [I mentioned][3] that we were working on getting the house upgraded with a photovoltaic solar power system.

Some of you have asked me via various communication pathways how it was going.

Thanks to legislation, or rather the lack of communication around this legislation, the amount of physical progress we have made so far is close to zero. Oh, just make that zero.

My shopping list now looks as follows:

  * Unchanged: 3.6kW GoodWe EM hybrid inverter: Although a larger inverter would have been preferable, uncertainty caused by above-mentioned lack of communication motivates me to play it safe with this unit which is in the 2017 column of the approved list.
  * Unchanged: 2 x PylonTech US3000b lithium ion batteries.
  * CHANGED: 16 x Canadian Solar CS3U 350Wp or 355Wp solar panels.

It used to be common knowledge that monocrystalline panel power output suffered less due to high temperature than that of the cheaper polycrystalline panels. This is quite relevant, because just sitting there on your roof the whole day, these things can get really hot!

Well, I finally went and looked up the temperature coefficient of these current generation Canadian Solar panels, namely the CS3U range, [which is -0.37% Pmax / ℃][4]. This is in fact slightly better than the -0.39% of the monocrystalline panels I had on my list.

I am currently on the lookout for what is going to be my fourth candidate solar installer, although at this stage I would be quite happy with a talented electrician who is not afraid of heights.

(My second installer had difficulty keeping up with all of their work (probably thanks to load-shedding and also to the substantial price increases expected from our embattled electricity monopoly) and my third installer has decided to focus on commercial installations.)

## My big and stupid misstep into Google Drive.

Somewhere during the past two weeks, I lost, forever and ever, at least three evenings.

Tipped off by a colleague at work, encouraged by my family’s mobile photos investment in Google Photos, and further tempted by the significant price difference and the family storage sharing option, I convinced myself that it was time to migrate my little empire of useless files (dropbox reports that I currently have just over 500000 (five hundred thousand) of them) out of Dropbox and into Google Drive.

This is how it looked on paper, i.e. in my head and in my Emacs notes:

  * I have about 70GB of photos taken with various family cameras of kids growing up, vacations everywhere and so on. These photos are currently not easily accessible by said family. If they were on Google Drive, they could be automatically exposed to Google Photos, which my family is already using!
  * My 237G of Google Drive space, sufficient for everything, costs R39 / month (that’s about $2.75), whereas my Dropbox subscription costs $10 / month.
  * The cheap subscription of Drive already enables one to do content searches. E.g. I could find scans of documents instantly by typing OCR’d words that occur in the documents. If you want the same with Dropbox, you have to go Pro (not Plus), and pay double, that is $19.99 per month.
  * Drive has a built-in facility to backup folders outside of the main sync folder.
  * There’s a great tool called [rclone][5] with which nerds can sync files to Google Drive from the command-line!

### Four lessons learned uploading 500k files to Google Drive

  1. Google has servers down here in South Africa: With larger files, the upload could easily max out my 50Mbit/s upload. 
  2. However, in spite of allocating and configuring my own [`client_id`][6], I could not upload faster than about 3 files per second. Based on various threads on the rclone forums, this is a known issue.
  3. Google Drive’s selective sync functionality does NOT (easily) allow you to maintain a local version of an excluded directory in the same way that Dropbox does. This is _especially_ annoying for those already quite annoying `node_modules` folders.
  4. Google Drive and its API support identically named files and directories, located in the same parent directory.

### How did the wheels fall off then?

I was alternating between the official Google Backup & Sync client and `rclone sync`. I did this to check if rclone with a private `client_id` would be able to upload faster (it couldn’t) and because rclone showed sync progress more clearly with an estimated time of completion (all of this turned out to be wildly incorrect and variable due to all of those small files).

My logic was that as long as the two tools were not running in parallel, sync logic and checksums should prevail right?!

Well, that turned out to be a very sad assumption…

rclone, which I still believe is a great tool for bulk uploads and downloads, should probably not be used for syncing in situations like this.

Unbeknownst to me, it had created hundreds of identically-named directories everywhere. (See lesson #4 above.)

At about halfway through this multi-day upload project, I switched back to the official Google tool, which finally, FINALLY managed to sync everything after about 5 days I would guess.

I was briefly _quite_ happy with Google’s arrow-in-cloud you-are-fully-synced icon in the menubar.

However, because happiness is so inherently fleeting anyways, I decided that it was time for the next phase of the project: Add the first Linux workstation to the little sync family.

Google Drive does NOT have a native client for Linux, although they’ve promised this since the start, and so I decided to try [Insync][7], which seems to be one of the best of the third party clients.

I pre-seeded the sync directory on said Linux machine using rsync and then started the insync client. This is a use case which was often enough mentioned on the forums as being supported.

Initially, everything seemed to be going swimmingly!

However, soon I saw whole directory hierarchies with thousands of files disappearing simultaneously from both my local disc and google drive.

STAAAAAAAAHP!!! JUST STAHP.

A second, stubborn attempt, after having recovered files and synced everything up with Google’s tool, yielded similarly frustrating results.

Granted, the duplicate folders on Google Drive are a far from ideal test case, but deleting directories like that on both client and server is not defensible.

Defeated, I retreated to the expensive, but safe, embrace of Dropbox.

### More lessons learned:

  * The lack of an official Google Drive client on Linux is debilitating to my workflow.
  * Handle the third-party Insync client with extreme caution.
  * The [sunk cost fallacy][8] is a real danger in cases like these.
  * The hours I lost are probably worth at least a year or two of Dropbox.
  * Having reliable incremental backups outside of your cloud syncing service remains important.

On that last point: Juggling my 500k files between Dropbox, Google Drive, then going live on Google Drive with real work before jumping into the shady world of badly implemented sync clients made me realise (again) the importance of a separate set of incremental backups.

Before my macOS phase (which started on May 6, 2015 when my employer bought me my first MacBook Pro and I wrote in my diary: “Bought 13.3 retina MacBook Pro early 2015, 128 GB SSD. I am doomed.”) I used to maintain a [dirvish][9] backup. 

(Dirvish is an amazing tool by the way.)

The truly stupid and frustrating adventure I write about here, did at least lead to some learning, and to me hooking up a [Seagate 4TB external drive][10] to my desk at work. Now when I connect my MacBook, Time Machine performs incremental backups the whole day long.

The next time I have one of these moments of irrationality again, I will at least have the possibility of returning my files to sanity as soon as I do.

## Thinking of future you.

There was one more learning I wanted to share.

I have mentioned before [on this blog][11] the well-known productivity trick of writing down, during your morning planning, the two to three really important tasks for the day.

In [the Sam Harris podcast where he interviews Derren Brown][12], they briefly mention a really interesting take or perspective on the tip above.

_When writing those tasks down, try to predict the two to three tasks the completion of which will satisfy future you the most at the end of the day._

It sounds like a small tweak, but this is a great way to encourage deeper (almost meta-)consideration of tasks that will really matter.

Additionally and more straight-forward than that, with this exercise you increase the chances that you end the day with that great feeling of closure that comes with getting important stuff done.

 [1]: /2010/07/26/island-style-weekly-head-voices-27/
 [2]: https://en.wikipedia.org/wiki/Head_girl_and_head_boy
 [3]: /2018/12/19/weekly-head-voices-159-extreme/#extreme-solar
 [4]: https://www.canadiansolar.com/upload/521adedf1d5fecb9/e5ba81805bf70380.pdf
 [5]: https://rclone.org/
 [6]: https://rclone.org/drive/#making-your-own-client-id
 [7]: https://www.insynchq.com
 [8]: https://www.behavioraleconomics.com/resources/mini-encyclopedia-of-be/sunk-cost-fallacy/
 [9]: http://dirvish.org
 [10]: https://www.storagereview.com/seagate_4tb_backup_plus_portable_drive_review
 [11]: https://cpbotha.net/2011/02/19/on-the-importance-of-taking-notes-weekly-head-voices-38/#three
 [12]: https://samharris.org/podcasts/143-keys-mind/
