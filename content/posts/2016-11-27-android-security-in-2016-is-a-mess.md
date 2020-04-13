---
title: Android security in 2016 is a mess.
author: cpbotha
type: post
date: 2016-11-27T11:41:36+00:00
url: /2016/11/27/android-security-in-2016-is-a-mess/
categories:
  - tech
tags:
  - android
  - blu
  - google
  - ios
  - mediatek
  - nexus
  - nougat
  - pixel
  - privacy
  - security

---
# Summary

Your phone probably contains banking, payment and personal information that can be remotely stolen via numerous known and unknown bugs in the Android software. This is attractive to criminals.

Vendors (LG, Samsung, Xiaomi, etc.), after selling you their phone, have no incentive to keep your phone's software up to date with Google's fixes. Your Android phone is probably out of date and therefore a gaping security hole through which attackers can steal your stuff from the safety of their own laptops.

Read on for more.<figure id="attachment_2621" aria-describedby="caption-attachment-2621" style="width: 750px" class="wp-caption alignnone">

[<img data-attachment-id="2621" data-permalink="https://cpbotha.net/2016/11/27/android-security-in-2016-is-a-mess/google_android_active_base/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/11/google_android_active_base.png" data-orig-size="750,482" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="google_android_active_base" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/11/google_android_active_base-300x193.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/11/google_android_active_base.png" class="size-full wp-image-2621" src="https://cpbotha.net/wp-content/uploads/2016/11/google_android_active_base.png" alt="Between 1.3 and 1.4 billion Google Android phones in March of 2016. Click image for source." width="750" height="482" srcset="https://cpbotha.net/wp-content/uploads/2016/11/google_android_active_base.png 750w, https://cpbotha.net/wp-content/uploads/2016/11/google_android_active_base-300x193.png 300w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 984px) 61vw, (max-width: 1362px) 45vw, 600px" />][1]<figcaption id="caption-attachment-2621" class="wp-caption-text">Between 1.3 and 1.4 billion Google Android phones in March of 2016. Click image for source.</figcaption></figure> 

# An illustration: MediaTek / BLU phones are uploading your data.

You might recently have read about [the incident with the popular BLU phones sold by Amazon in the US][2] (interestingly, the author deleted their article from both hackernoon.com and from medium; I now link to the Wayback Machine's stored copy). It turned out that these phones were regularly sending bunches of personal information to servers in China: text messages, call logs, contact lists and so forth. After more investigation, it came to light that this was happening via a low-level piece of software called ADUPS.

When Google had previously updated its systems to check for ADUPS, MediaTek (they make the chipset in millions of low-end phones) simply modified their system software to evade Google's checks. Nice one MediaTek!

This is a painful example of the fact that the software on your phone, although based on Google's software, is customised by the phone vendor. The further frustrating effect of this is that when Google releases security patches to Android ([which they do regularly][3]), there is very little incentive for the phone vendor to spend money on updating phones they have already sold.

# What about A-list phone makers?

I bought my LG G3 in 2014 here in South Africa. It was LG's flagship in that year, and sold extremely well. LG is a well-known smartphone OEM.

However, only because I took steps to flash the official KDZ image (V30a-ZAF-XX), which consumers would normally not do, am I now running Android 6. However, my security patch level is 2016-03, meaning there are 6 months of security updates I don't have. (You can check your **Android security patch level** by going to _Settings | General | About Phone | Software info_.)

Before you think six months lag is not too bad, here's a nice example vulnerability from [the November 1 Android security bulletin][4]:

> The most severe of these issues is a Critical security vulnerability that could enable remote code execution on an affected device through multiple methods such as email, web browsing, and MMS when processing media files.

In short, your phone could be hacked wide open from afar through a single innocent-looking email, MMS or web-page.

My friend's South African LG G3 is still stuck on Android 5.0 (V20n-ZAF-XX). Most probably this is being blocked due to his carrier (MTN). In any case, 5.0 does not even show the security patch level, so we have no idea how many months of security fixes this phone is missing.

([LG seems to be tracking Google's security updates quite well][5], but somehow these updates are not reaching phones.)

## A scary little aside

I just tried Check Point Labs' [QuadRooter Scanner app][6] on my &#8220;updated&#8221; LG G3, and this is what I saw:<figure id="attachment_2641" aria-describedby="caption-attachment-2641" style="width: 169px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12.png" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title="">

<img data-attachment-id="2641" data-permalink="https://cpbotha.net/2016/11/27/android-security-in-2016-is-a-mess/screenshot_2016-11-27-20-55-12/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12.png" data-orig-size="1440,2560" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="screenshot_2016-11-27-20-55-12" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12-169x300.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12-576x1024.png" class="size-medium wp-image-2641" src="https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12-169x300.png" alt="LG G3 with Marshmallow and Android security patch level 2016-03 is vulnerable to QuadRooter." width="169" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12-169x300.png 169w, https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12-768x1365.png 768w, https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12-576x1024.png 576w, https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12-1200x2133.png 1200w, https://cpbotha.net/wp-content/uploads/2016/11/Screenshot_2016-11-27-20-55-12.png 1440w" sizes="(max-width: 169px) 85vw, 169px" /></a><figcaption id="caption-attachment-2641" class="wp-caption-text">LG G3 with Marshmallow and Android security patch level 2016-03 is vulnerable to QuadRooter.</figcaption></figure> 

So my manually updated LG G3 is still very much vulnerable to QuadRooter. In theory, my phone could be (or already has been) [rooted and pillaged by any old innocent-looking app][7], although I keep mostly to the official Play Market, so the risk is slightly mitigated.

At this stage, even as a relatively knowledgeable user, there's not much I can do to patch my phone against this vulnerability.

# Google's leniency cuts both ways: More than a billion Android users, but most of them vulnerable.

It's fantastic that Google's openness and leniency with Android has helped to make smartphone technology accessible to more than a billion users (probably closer to 2 billion taking into account Chinese Android phones not connected to Google services, see [Ben Evans's post][1]). However, this same leniency allows manufacturers to be irresponsible about keeping their customers safe.

The fundamental problem here is that there are a great deal of Android phone vendors who make phones from absolute entry-level to top-of-the-line flagships, who have very little incentive to spend money on post-sale security updates.

Once you've paid for the phone, you're not important enough anymore to have a secure(ish) telephone.

# What can we do?

## Buy an iPhone. No really.

I've been using Android since the HTC Desire Z. I love Android, because I love Linux which I have been using since 1993.

However, if money is no object, my only sound advice can be to **buy an iPhone**. Apple is still shipping security updates, albeit on iOS 9, for the iPhone 4s which was released in 2011 (5 years ago). The iPhone 5 is still being kept up to date with iOS 10.

Furthermore, in terms of phone encryption, [iOS 4, released 6 years ago, was already more advanced than than Android 7 Nougat][8], released in August of this year. In short, already then Apple made better choices in how exactly different files are encrypted, whilst Android implemented full disk encryption, which for the smartphone usecase is not the right choice. In Nougat, Android has finally also changed to file-based, but they're missing important parts of the puzzle. [The phone encryption blog post][8] I link to is insightful, please take a look.

## Stick with Android Pixel or Nexus.

If you prefer sticking with Android, the best choice is getting an official Google device, which means either a Nexus or a new Pixel. [Google's policy for Pixel and Nexus security][9] states that they will ship security updates either for three years after device introduction, or for 1.5 years after the device was last officially sold from the Google Store, whichever is longer.

Unfortunately, iPhones are really expensive, and Google's new Pixel devices are also aiming for the higher-end market. The previous generation Nexus phones offer a more mid-range but very temporary reprieve.

In other words, most normal consumers on a budget, i.e. the largest part of the Android user base, actually of the smartphone-using world, are stuck with insecure, vulnerable phones. This is not cool.

## Consider installing a custom ROM.

Installing a custom ROM such as Cyanogenmod brings with it another set of issues with regard to the phone being rooted, and with regard to driver-level support of proprietary hardware. In any case, this is not something your average consumer will have access to, but Android gurus can certainly apply.

Efforts like [CopperheadOS][10] (hardened Android) are certainly promising, but it will be quite a while before they are accessible to the largest group of Android users.

**Update:** David Metcalfe pointed out in the comments that you can buy a secure Android phone from Copperhead.  If you are in the US or Canada, and you have some budget, you could buy the [LG Nexus 5x or the Huawei Nexus 6P with CopperheadOS pre-installed][11]. It's great that this is available, but due to price and geography not really accessible to most Android users.

## Keep manufacturers honest.

Ideally, Google starts taking a much harder line with manufacturers who put Android on their phones. They could for example maintain and publish a list of phone models that are kept up to date with the latest security fixes, and a list of those that aren't.

I was happy to see that at least [Huawei has a pretty good record][12] in terms of keeping their Android phones up to date (although the results were probably skewed as they counted the Huawei-produced Nexus 6P phones, and these formed the majority of the test set, doh). This factor will play a role in the next smartphone that I buy.

Do you know of any (other) manufacturers of more affordable Android phones who are committed to keeping their users safe? Please let me know in the comments!

# Addendum: Android phones with acceptable security update records

## Blackberry PRIV, DTEK50 and DTEK60

lobste.rs user jabberwock [tipped me off to the fact that Blackberry's Android phones get monthly security updates][13]. Read more at [CrackBerry][14] and here in the [BlackBerry Android security bulletin for November][15]: It looks like these phones receive monthly updates (**when not blocked by the carrier, _sigh_**)** **and have already received the November 2016 update.

Here is [the original blog post where BlackBerry explained their security patching policies for the PRIV][16].

# Updates.

## Wednesday 2020-02-26.

I wanted to post some relevant updates, so here goes (okay just one):

- [Android Security is a Hot Mess (yet Again)](https://securityboulevard.com/2019/03/android-security-is-a-hot-mess-yet-again/), March 15, 2019.


 [1]: http://ben-evans.com/benedictevans/2016/7/25/platform-wars-final-score
 [2]: https://web.archive.org/web/20161117073724/https://hackernoon.com/no-one-cares-about-the-security-of-your-unlocked-android-phone-cd8ad4aae4c5?gi=e0e2979fddb
 [3]: https://source.android.com/security/bulletin/index.html
 [4]: https://source.android.com/security/bulletin/2016-11-01.html
 [5]: https://lgsecurity.lge.com/security_updates.html
 [6]: https://www.checkpoint.com/resources/quadrooter-vulnerability-consumer/
 [7]: http://www.techradar.com/news/phone-and-communications/mobile-phones/android-quadrooter-vulnerability-should-you-be-worried-1326286
 [8]: https://blog.cryptographyengineering.com/2016/11/24/android-n-encryption/
 [9]: https://support.google.com/pixelphone/answer/4457705#pixel_phones&nexus_devices
 [10]: https://copperhead.co/android/
 [11]: https://copperhead.co/android/buy
 [12]: http://news.softpedia.com/news/huawei-is-the-best-oem-at-applying-android-security-updates-505767.shtml
 [13]: https://lobste.rs/s/8g2nkz/android_security_2016_is_mess/comments/4p7rwr#c_4p7rwr
 [14]: http://crackberry.com/blackberry-priv-dtek50-and-dtek60-november-updates-now-available
 [15]: http://support.blackberry.com/kb/articleDetail?articleNumber=000038666
 [16]: http://blogs.blackberry.com/2015/11/managing-android-security-patching-for-priv/
