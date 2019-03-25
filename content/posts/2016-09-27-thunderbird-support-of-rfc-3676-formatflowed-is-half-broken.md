---
title: ThunderBird support of RFC 3676 format=flowed is half-broken
author: cpbotha
type: post
date: 2016-09-27T07:00:25+00:00
url: /2016/09/27/thunderbird-support-of-rfc-3676-formatflowed-is-half-broken/
categories:
  - tech
tags:
  - format=flowed
  - hard line break
  - plaintext
  - reflow
  - RFC 2646
  - rfc 3676
  - soft line break
  - thunderbird

---
Summary: [RFC 3676][1] format=flowed is an elegant and backwards-compatible method to have plaintext emails reflowed on (mobile) devices that support this feature. Although this standard has been around for more than 10 years, and Thunderbird 45.3.0 reports supporting it, it only does so on non-quoted text. Most unfortunately, it wraps quoted text incorrectly, disabling reflowing on receiving devices, resulting in embarrassingly ugly email rendering.

# What is RFC 3676 format=flowed?

Half of the people on the internet are of less than average intelligence. This is especially evident in discussions around format=flowed. To exacerbate matters, participants in most cases have not taken the time to actually read through [RFC 3676][1] (go on, click the link!) and instead prefer to argue on the basis of their very strong emotions and opinions around text wrapping.

I would like to try and summarise very compactly what exactly format=flowed is and how it works.

Believe it or not, email can still be sent as plain text, i.e. not as HTML. Furthermore, this text is usually wrapped, i.e. newlines are inserted at a comfortable column width, e.g. 72 characters. This used to work wonderfully, until mobile devices came along. Because their screens often aren&#8217;t able to show the full 72 character width, the devices would be forced to wrap the text, resulting in a really ugly comb effect:

<pre>Someone sent me this really interesting
email. Unfortunately
it was wrapped so badly that I had difficulty
reading it. Even worse,
it made me like the sender of the email less.</pre>

To solve this problem, RFC 2646 was proposed (later to be superseded by its successor [RFC 3676][1]). All that had to happen, was that the sender could add a &#8220;format=flowed&#8221; to the outgoing email&#8217;s content-type, and wrap the email with both **soft** and **hard** line breaks (a line break in this case is a carriage return followed by a line feed, or CRLF). **Soft line breaks**, consisting of a space followed by CRLF, are used at the end of intra-paragraph lines, i.e. lines that could potentially be reflowed / joined. **Hard line breaks**, consisting of just the CRLF directly following the last character of the line, are used at the end of lines that should not be reflowed.

This meant that we could continue sending plaintext mails as we always did, with CRLFs exactly where we always had them. However, with format=flowed and a few extra spaces at strategic points, receiving devices that supported this format had the _option_ of reflowing. Older devices would display the email exactly as they always had.

# What is Thunderbird doing wrong?

In Thunderbird 45.3.0, format=flowed can be activated in _Preferences | Advanced | Config Editor_ by setting _mailnews.send\_plaintext\_flowed_ to _true_.

If you now start sending an email in plaintext mode, you&#8217;ll notice that Thunderbird is visually wrapping your text, i.e. it&#8217;s not inserting any hard line breaks. However, when you actually send the email, Thunderbird will replace all the visual line breaks with _format=flowed_ **soft** line breaks. Your manually entered hard line breaks are maintained.

This is really great! Your emails render perfectly, even on smaller devices.

Unfortunately, when you reply to a correctly formatted format=flowed email, the quoted text is hard wrapped.

Viewing the message source with Emacs, we can see line breaks as $ characters. In the non-quoted part, the pink blocks are the expected spaces before each line break, meaning they will be treated as reflowable. However, in the quoted reply, there are no spaces before the line breaks, meaning they will be treated as unreflowable hard line breaks:<figure id="attachment_2522" aria-describedby="caption-attachment-2522" style="width: 761px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/09/2016-09-27-091622\_761x286\_scrot.png" data-rel="lightbox-image-0" data-rl\_title="" data-rl\_caption="" title="">

<img data-attachment-id="2522" data-permalink="https://cpbotha.net/2016/09/27/thunderbird-support-of-rfc-3676-formatflowed-is-half-broken/2016-09-27-091622_761x286_scrot/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/09/2016-09-27-091622_761x286_scrot.png" data-orig-size="761,286" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="2016-09-27-091622_761x286_scrot" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/09/2016-09-27-091622_761x286_scrot-300x113.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/09/2016-09-27-091622_761x286_scrot.png" class="wp-image-2522 size-full" src="https://cpbotha.net/wp-content/uploads/2016/09/2016-09-27-091622_761x286_scrot.png" alt="TB 45.3.0 hard wraps a quoted reply in format=flowed mode. Naughty Thunderbird!" width="761" height="286" srcset="https://cpbotha.net/wp-content/uploads/2016/09/2016-09-27-091622_761x286_scrot.png 761w, https://cpbotha.net/wp-content/uploads/2016/09/2016-09-27-091622_761x286_scrot-300x113.png 300w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 984px) 61vw, (max-width: 1362px) 45vw, 600px" /></a><figcaption id="caption-attachment-2522" class="wp-caption-text">TB 45.3.0 hard wraps a quoted reply in format=flowed mode. Naughty Thunderbird!</figcaption></figure> 

This is really very sad, and also quite unnecessary. When the email arrives on a mobile device, the quoted reply can&#8217;t be reflowed, and it looks like this:<figure id="attachment_2518" aria-describedby="caption-attachment-2518" style="width: 840px" class="wp-caption alignnone"><a href="https://cpbotha.net/wp-content/uploads/2016/09/Screenshot\_2016-09-27-08-24-55.png" data-rel="lightbox-image-1" data-rl\_title="" data-rl_caption="" title="">

<img data-attachment-id="2518" data-permalink="https://cpbotha.net/2016/09/27/thunderbird-support-of-rfc-3676-formatflowed-is-half-broken/screenshot_2016-09-27-08-24-55/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55.png" data-orig-size="1440,1034" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="screenshot_2016-09-27-08-24-55" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55-300x215.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55-1024x735.png" class="size-large wp-image-2518" src="https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55-1024x735.png" alt="Incorrectly soft-wrapped quoted reply can't be reflowed on my mobile device." width="840" height="603" srcset="https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55-1024x735.png 1024w, https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55-300x215.png 300w, https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55-768x551.png 768w, https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55-1200x862.png 1200w, https://cpbotha.net/wp-content/uploads/2016/09/Screenshot_2016-09-27-08-24-55.png 1440w" sizes="(max-width: 709px) 85vw, (max-width: 909px) 67vw, (max-width: 1362px) 62vw, 840px" /></a><figcaption id="caption-attachment-2518" class="wp-caption-text">Incorrectly soft-wrapped quoted reply can&#8217;t be reflowed on my mobile device.</figcaption></figure> 

How embarrassing.

# How ever will we be able to survive this catastrophe?

I have not been able to convince Thunderbird to soft-wrap quoted replies, even going so far as to insert the extra spaces myself. Thunderbird helpfully (not!) removes those spaces before sending the email, resulting in really embarrassing email rendering on receiving mobile devices that fully support format=flowed.

_Edit | Rewrap_ in the compose window simply hard wraps everything, so it will only make things worse in the context of format=flowed.

I have also experimented with sending the quoted bits as really long lines (Emacs and the [TB External Editor addon][2] FTW). This displays nicely on modern mobile devices, but will result in infuriatingly long lines on MUAs that do not support flowed text.

Ideally, someone working on Thunderbird will realise that the current implementation desperately needs fixing, and will just do the job. Alternatively, someone will point me at a Thunderbird addon and source code I could modify to fix this behaviour. (If you&#8217;ve seen the multi-year arguments about text wrapping on the Thunderbird bug tracker, you&#8217;ll understand why I think an addon is a better bet than an externally suggested code change / pull request.)

I fear that I may be one of the last people still sending plaintext emails, so it might be that nothing will come of this desperate call for help. :)

&nbsp;

 [1]: http://www.ietf.org/rfc/rfc3676.txt
 [2]: http://globs.org/download.php?lng=en