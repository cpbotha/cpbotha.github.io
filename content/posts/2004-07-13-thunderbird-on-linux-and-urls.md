---
title: Thunderbird on Linux and URLs
author: cpbotha
type: post
date: 2004-07-13T11:17:49+00:00
url: /2004/07/13/thunderbird-on-linux-and-urls/
categories:
  - Uncategorized

---
It seems Mozilla Thunderbird (GREAT mail client, BTW) seems to download and open the downloaded HTML file when you click on a URL in an email. This is usually not what I want&#8230; so:

1. Exit Thunderbird if it&#8217;s running.
  
2. Edit your prefs.js (usually in ~/.mozilla-thunderbird/default/random_characters/prefs.js
  
3. Add this line: user_pref(&#8220;network.protocol-handler.app.http&#8221;, &#8220;/usr/bin/mozilla-firefox&#8221;);
  
4. Save (DOH)

Obviously, if you don&#8217;t have an intelligent mozilla-firefox script in /usr/bin that is able to make use of a running instance of firefox, you might have to use the mozilla-firefox-xremote-client or somesuch. Perhaps you even prefer to use another browser&#8230; heaven forbid!

For more details, see here: http://www.mozilla.org/projects/thunderbird/linuxurls.html