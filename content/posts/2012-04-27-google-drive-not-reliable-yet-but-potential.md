---
title: 'Google Drive: Not reliable yet, but potential.'
author: cpbotha
type: post
date: 2012-04-27T20:47:56+00:00
url: /2012/04/27/google-drive-not-reliable-yet-but-potential/
topsy_short_url:
  - http://is.gd/d4miO1
categories:
  - review
tags:
  - dropbox
  - google drive
  - review
  - screenshots
  - undelete
  - unstable
  - vim

---
I’ve been a Dropbox Pro (50G) user for [more than two years now][1], and in this time it has never let me down, not even by a little bit. Still, when Google [announced its new Google Drive syncing service][2], I had to take it for a spin.

For those of you with short attention spans, my conclusion is: _Google Drive has great promise due to its price-point, Google’s great infrastructure and the integration with Google Docs, but you shouldn’t yet trust this service with your critical files._

To summarise: Google Drive is Google’s answer to Dropbox (and 50 other inferior syncing services). You install a small app on your Windows or Mac (no Linux yet, although [it has been promised][3]), and then it’ll keep a folder of your choosing in sync with Google Drive in the cloud. You can access your files via the website [drive.google.com][4] (google docs, but slightly updated), any computer with the Google Drive software, or via the Google Drive mobile apps.  You can also share files through authorizing the relevant google accounts, or via URL. Google Drive has a number of built-in viewers, meaning that users will not have to install PowerPoint to view your PowerPoint presentation for example.

Things start to deviate from Dropbox when we look at the storage plans and prices the big G is offering:

<a data-rel="lightbox-image-0" data-rl_caption="" data-rl_title="" href="http://cpbotha.net/wp-content/uploads/2012/04/gdrive_storage_plans.jpg" title=""><img alt="" class="aligncenter size-medium wp-image-1654" data-attachment-id="1654" data-comments-opened="1" data-image-description="" data-image-meta='{"aperture":"0","credit":"","camera":"","caption":"","created_timestamp":"0","copyright":"","focal_length":"0","iso":"0","shutter_speed":"0","title":""}' data-image-title="gdrive_storage_plans" data-large-file="https://cpbotha.net/wp-content/uploads/2012/04/gdrive_storage_plans.jpg" data-medium-file="https://cpbotha.net/wp-content/uploads/2012/04/gdrive_storage_plans-300x86.jpg" data-orig-file="https://cpbotha.net/wp-content/uploads/2012/04/gdrive_storage_plans.jpg" data-orig-size="744,215" data-permalink="https://cpbotha.net/2012/04/27/google-drive-not-reliable-yet-but-potential/gdrive_storage_plans/" height="86" sizes="(max-width: 300px) 85vw, 300px" src="http://cpbotha.net/wp-content/uploads/2012/04/gdrive_storage_plans-300x86.jpg" srcset="https://cpbotha.net/wp-content/uploads/2012/04/gdrive_storage_plans-300x86.jpg 300w, https://cpbotha.net/wp-content/uploads/2012/04/gdrive_storage_plans.jpg 744w" title="gdrive_storage_plans" width="300"/></a>

You get 5G for free. For a measly $2.49 per month, you get 25G of storage, and 30G of GMail storage as a bonus, and for $5 per month you get 100G! Compare this with the $10 / month Dropbox wants for 50G. This, together with the fact that you _could_ go up to 16 TERABYTES if you would want to, makes you at least think for a bit.

I installed the client on this Windows laptop. For you screenshot-freaks, here’s the context menu for the systray icon:
{{< figure src="/wp-content/uploads/2012/04/gdrive_systray_menu.jpg" link="/wp-content/uploads/2012/04/gdrive_systray_menu.jpg" caption="Google Drive systray context menu.">}} 

Note that because I pay a measly $5 / year for 25G of extra GMail space, I’ve been _grandfathered_ into 25G of Google Drive space. Heh, I also only just learnt the term grandfathered. It means I could get this because of my previous price plan that doesn’t exist anymore.

Here’s the preferences dialog, nothing special really, unless you have a screenshot fetish:
{{< figure src="/wp-content/uploads/2012/04/gdrive_prefs.jpg" link="/wp-content/uploads/2012/04/gdrive_prefs.jpg" caption="Google Drive preferences dialog.">}} 

For me also an important functionality: You can easily recover deleted files. If you delete a file on your client computer, it gets synced to the trash folder on the google drive website, from where undeletion is an easy click on the “Recover” button away. Under the File | Manage Revisions you can retrieve file versions up to 30 days ago, or 100 revisions, whichever comes earlier.

Another important difference is that Google Drive, as far as I could find out, does not do something similar to Dropbox’s LAN sync, a pretty cool function that will grab files from the computers on the local LAN if they’re available, instead of from the cloud.

So I set out to do some tests. Before I could really get started, I ran into the first problems. I created a text file in my Google Drive folder with Vim (yes, I use Vim. deal.), as I wanted to test the file revisions. As you know, when Vim saves a file, it first writes to a temporary file, then deletes the original file and finally renames the new file to the original file. This confused Google Drive to no end. For each save, Google Drive created a new file with exactly the same name in the web interface, whilst on the client side, there was only one file.

I then proceeded to delete the text file on the client, leaving me with the following situation, even after Google Drive was done syncing:
{{< figure src="/wp-content/uploads/2012/04/gdrive_sync_huh.jpg" link="/wp-content/uploads/2012/04/gdrive_sync_huh.jpg" caption="Huh?! You call this syncing?">}} 

As you can see, on the server is my text file, on the client nothing. I expect of a syncing solution to actually, uhm, synchronise my files. I did notice a sync error message in the systray context menu. After clicking, I got this dialog:
{{< figure src="/wp-content/uploads/2012/04/gdrive_sync_error.jpg" link="/wp-content/uploads/2012/04/gdrive_sync_error.jpg" caption="Informative error message. NOT.">}} 

Yes, thank you Google Drive, you have an unknown issue. That’s just great.

So, in spite of the really attractive offering, this type of wonkiness (multiple files due to stupid create-new-rename saves, sync errors soon after), even after a few minutes of playing around, does not instil confidence or trust. If there’s one thing a good sync service should do, it’s instil confidence and trust. Dropbox has never failed me, and I’ve thrown some pretty strange things at it. Until Google Drive is able to do the same, I’ll continue coughing up 10 bucks a month for Dropbox.

 [1]: /2010/03/29/weekly-head-voices-19-the-time-travellers-bbq/ "me gets a dropbox pro account"
 [2]: http://googleblog.blogspot.com/2012/04/introducing-google-drive-yes-really.html "google drive announcement"
 [3]: http://www.pcworld.com/businesscenter/article/254488/google_drive_for_linux_is_on_the_way.html "Google Drive for Linux should come"
 [4]: http://drive.google.com/ "google drive website"
