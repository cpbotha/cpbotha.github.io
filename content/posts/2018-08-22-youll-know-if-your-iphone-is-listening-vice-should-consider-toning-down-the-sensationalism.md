---
title: You’ll know if your iPhone is listening. Vice should consider toning down the sensationalism.
author: cpbotha
type: post
date: 2018-08-22T20:34:14+00:00
url: /2018/08/22/youll-know-if-your-iphone-is-listening-vice-should-consider-toning-down-the-sensationalism/
categories:
  - privacy
tags:
  - advertising
  - android
  - background audio
  - background recording
  - facebook
  - ios
  - permissions
  - vice

---
A Vice article titled [Your Phone Is Listening and it’s Not Paranoia][1] has been doing the rounds. In it, the author explains how they did an “experiment” demonstrating that topics they discussed verbally were later reflected in Facebook ads.

Whilst it’s prudent to be careful with modern technology around one’s privacy, Vice is being a tad sensationalist. This blog post, which will optimistically be read by three to four people, tries to fill some of the holes they left.

We already know that we can’t trust Facebook in any way, so we are dependent on the telephone’s operating system to take our privacy seriously: That’s usually Android or iOS.

Android does in theory _enable_ background recording up to and including Android O, but [starting from Android P][2] it will disable this. Unfortunately, it shouldn’t be more than about 10 years before all phones are on Android P or later.

([I have previously indicated that I’m not the biggest fan of Android’s security story][3]. I am happy to see that they are making such progress, but the tardiness or even worse refusal of OEMs in upgrading their devices diminishes most of that.)

In iOS on the other hand, there are at least three mechanisms that protect users against this background recording abuse:

  1. The app has to ask the user explicitly for microphone permission, which the user can easily revoke at any time (Settings | App’s name | Microphone; see screenshot below for an example).
  2. The developer has to indicate explicitly and statically in their app that they intend to use background audio. Apple’s review process is quite strict and will reject outright an app that does not have a legitimate reason to make use of this function.
  3. Even when an app has been able to convince Apple’s review process that it should be allowed to record audio in the background, there are two more privacy mechanisms in place: 
      1. An app can only record in the background, if it started to record audio whilst on the foreground. When the recording stops, [the app will be suspended][4].
      2. When any app is recording, the system will display a big red bar at the top of the iOS display, much like the blue bar which displays when a location-based app such as Google Maps or Waze is active in the background. [This red bar can’t be hidden][5].

To see this in action (another “experiment” !!), download an app like [Awesome Voice Recorder][6] which advertises background recording, start a recording, and then switch anywhere else. The red bar looks like this (I’ve switched the app permissions screen in iOS settings, so you can also see where to disable the microphone permissions):
{{< figure src="/wp-content/uploads/2018/08/IMG_EBA399A01B16-1.jpeg" link="/wp-content/uploads/2018/08/IMG_EBA399A01B16-1.jpeg" caption="AVR is recording in the background, so iOS shows this red bar at the top. If you tap on the red bar, it will switch to the app which is recording. This is related to the blue bar for location, and the green bar for ongoing phone calls.">}} 

With the above measures in place, it would be fairly tricky for an iOS app to perform background recording without your knowledge.

For some extra peace of mind, you can disable the app’s (a totally random example being Facebook) microphone permissions. If the app ever really needs to record, iOS will have to ask your permission again.

P.S. In iOS, under Settings | Privacy | Microphone you can find a handy list of all apps that have successfully requested microphone permissions. From here, you can also easily remove any of these permissions.

# Updates

  * 2018-08-23: It seems [Androids phone home much more often than iPhones][7].

 [1]: https://www.vice.com/en_uk/article/wjbzzy/your-phone-is-listening-and-its-not-paranoia
 [2]: https://www.theverge.com/platform/amp/2018/3/7/17091104/android-p-prevents-apps-using-mic-camera-idle-background
 [3]: /2016/11/27/android-security-in-2016-is-a-mess/
 [4]: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html#//apple_ref/doc/uid/TP40007072-CH4-SW26
 [5]: https://stackoverflow.com/a/39963079/532513
 [6]: https://itunes.apple.com/us/app/awesome-voice-recorder/id892208399?mt=8
 [7]: https://www.zdnet.com/article/want-google-to-track-you-less-get-an-iphone-ditch-the-android/
