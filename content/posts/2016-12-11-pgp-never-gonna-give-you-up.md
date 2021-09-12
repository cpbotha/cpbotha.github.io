---
title: PGP Never Gonna Give You Up
author: cpbotha
type: post
date: 2016-12-11T15:34:26+00:00
url: /2016/12/11/pgp-never-gonna-give-you-up/
categories:
  - howto
tags:
  - android
  - encryption
  - openpgp
  - pgp
  - privacy
  - security

---

_(Summary: Cryptographically signing messages with my long-term PGP keys is
too important to give up. Doing this on my Android telephone is easier than I
thought. You should strengthen your secret key encryption if you're also
going to do this.)_

Recently, Filippo Valsorda, cryptography expert and TLS guy at Cloudflare,
[wrote that he was giving up on PGP, or at least on long term PGP keys][1].

I agree with many of his points, especially the complexity of managing those
keys, lack of forward secrecy (if someone were to steal my keys, they could
decrypt all past conversations, unlike for example Signal) and accessibility
(how do you verify a message with a baby on your left arm and your telephone
in your right?). More generally, it makes a great deal of sense to make your
security a moving target, [as one of the Ars Technica commenters
astutely summarised Filippo's ideas][2].

## Cryptographic signatures FTW

However, in spite of these factors, I am not yet ready to give up my PGP long-term keys.

Why is that?

_Well, one of the most important uses of my long-term PGP keys is to
cryptographically sign messages that can be verified by people in my network
as having come from my hands._

For example, when I change my phone or re-flash its firmware (this has
happened 3 or 4 times over the past two months because Android), I send
PGP-signed messages to my main Signal correspondents with our new safety
numbers.

With all of these correspondents I have in the past either done some sort of
in-person formal PGP signing procedure, or I make use of the web of trust, or
I rely on <a href="https://keybase.io/">keybase</a>. My business cards even
have my key fingerprint on them (yes, I'm one of those nerds).

At their ends, the recipients of my messages are able to determine with an
extremely high degree of confidence that _I_ wrote the exact message they
opened.

## Accessible PGP on your smartphone with OpenKeychain

In terms of accessibility, the post did make me curious enough to experiment
with a mobile PGP solution, as I also did have to agree that I've in the
past often had to wait until I was behind one of my own laptops or
workstations to PGP-verify a message.

As my one friend explained on Signal:

It's tricky to verify a message with a baby in your left hand and a telephone in your right!
    
<a href="https://www.openkeychain.org/">OpenKeychain</a> to the rescue!

### Strengthen your secret key encryption

Seeing that I was planning on carrying my long-term private keys around on my
telephone (BlackBerry PRIV, FDE encryption active FWIW), I had to double-check
the security of the secret key encryption.

It turns out that PGP encrypts each of your secret keys with a hash of the
passphrase you supply. My passphrase is significantly longer than the average,
and consists of random characters (uppercase, lowercase, numbers,
symbols). Passphrase length and complexity is by far the most important factor
determining the safety of your encrypted secret key.

However, I had the default SHA-1 hash (ouch) with only 64k
iterations. Iterating the hash is called <a
href="https://en.wikipedia.org/wiki/Key_stretching">key stretching</a>: the
passphrase is hashed, that result is hashed, and so on, for very many times,
so that the testing of each passphrase takes more time, complicating
brute-force cracking approaches.

Inspired by <a href="http://nullprogram.com/blog/2012/06/24/">the writings of
Chris Wellons</a> who keeps his encrypted secret keys on a public website
(!!!), I reconfigured my private key encryption to use 1 million iterations of
the SHA-512 hash, and to use AES-256 for the encryption itself:

```shell
gpg --s2k-cipher-algo AES256 --s2k-digest-algo SHA512 --s2k-mode 3 --s2k-count 1000000 --edit-key 384435C7E77A4564
```

After typing that command, enter <code>passwd</code> at the prompt, then
follow the prompts. You will have to enter your passphrase, and then enter
your new passphrase twice.


You can then check that this operation is successful by using the command <code>gpg --list-packets secring.gpg</code>. My output looks as follows. Most important is that algo is 9 (AES-256), hash is 10 (SHA-512) and protect count in my case is just over 1 million.

    :secret key packet:
    version 4, algo 1, created 1376407300, expires 0
    skey[0]: [4096 bits]
    skey[1]: [17 bits]
    iter+salt S2K, algo: 9, SHA1 protection, hash: 10, salt: blabla
    protect count: 1015808 (
    protect IV:
    encrypted stuff follows
    keyid: 384435C7E77A4564
      

SHA-512 is the slowest hash which PGP offers (see <a
href="http://thepasswordproject.com/oclhashcat_benchmarking">these oclHashcat
benchmarks for example</a>), which means that each iteration of a brute-force
password cracking attempt will take a bit longer / eat more GPU watts, which
is exactly what we want. You can increase the protect count for as long as the
delay on your smartphone is still tolerable.

However, remember that a stronger and longer passphrase is much better! (so we
do both)


Other than that, remember that <a
href="/2016/11/27/android-security-in-2016-is-a-mess/">Android security is far
from good</a>, so do as much as you can to keep your phone safe (keep up with
OS updates, stay away from unofficial app markets, and so on).


### Use your keys with OpenKeychain

I was pleasantly surprised to learn that I could directly import both my
<code>secring.pgp</code> and <code>pubring.gpg</code> files from my
<code>~/.gnupg</code> directory. Right after selecting secring.pgp for import,
the UI looked like this:

<p>
<a href="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007.png" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2665" data-permalink="https://cpbotha.net/2016/12/11/pgp-never-gonna-give-you-up/screenshot_20161209-075007/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007.png" data-orig-size="1440,2560" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screenshot_20161209-075007" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007-169x300.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007-576x1024.png" class="alignnone size-medium wp-image-2665" src="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007-169x300.png" alt="" width="169" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007-169x300.png 169w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007-768x1365.png 768w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007-576x1024.png 576w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007-1200x2133.png 1200w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161209-075007.png 1440w" sizes="(max-width: 169px) 85vw, 169px" /></a>
</p>
    
You can see the old 1024 bit key I made in 2000 to use for my Debian
activities, and the 4096 bit key I currently use.

After importing your secret and public keyring, you are able to encrypt,
decrypt, sign and verify any files or clipboard contents on your Android
phone:

<p>
<a href="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851.png" data-rel="lightbox-image-1" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2666" data-permalink="https://cpbotha.net/2016/12/11/pgp-never-gonna-give-you-up/screenshot_20161211-170851/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851.png" data-orig-size="1440,2560" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screenshot_20161211-170851" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851-169x300.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851-576x1024.png" class="alignnone size-medium wp-image-2666" src="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851-169x300.png" alt="" width="169" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851-169x300.png 169w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851-768x1365.png 768w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851-576x1024.png 576w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851-1200x2133.png 1200w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-170851.png 1440w" sizes="(max-width: 169px) 85vw, 169px" /></a>
</p>
    
So if I receive something like this via Signal:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512
    
    Never gonna give you up, never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry, never gonna say goodbye
    Never gonna tell a lie and hurt you
    -----BEGIN PGP SIGNATURE-----
    
    iQFEBAEBCgAuJxxTdGVmYW4gdmFuIGRlciBXYWx0IDxzdGVmYW5Ac3VuLmFjLnph
    PgUCWE2aUQAKCRDl/rykoDTdZZgvB/9Yi76C9o7xIgQ/d85WbnKDjNosp5uXzgHm
    A2y+cxZDLVNLTMrlCTXOMRulaJMvb3Ocsvi+/gQVUF49fT74EXlZpZvvdTzhQfa2
    VvQPjZmf/9PNzB3pgUtEDBwyLC21C6dqU+y7mPk91Aw1m8cKBQUSHmQxa7F/dCFc
    DCuWOcXjNt5vLQ2Q8mQBMpHaG9J5+4/0k/GEHAVcm55fzb7o2hJyEVb3EoYy8Pls
    khIwJpZVdwyY4FPoLXW3iJYanC5qoOoS81YLCyLEyin0jH56ve05uHbF0XcaNY4h
    NupkN2D+Dt4X2m2FXieM27eG/Ty9hVx7n7B3pT4P9KqeFDX8hQ/q
    =c7j9
    -----END PGP SIGNATURE-----

I long-press, copy the message and then select &#8220;read from
clipboard&#8221; from OpenKeychain's Encrypt/Decrypt screen, which, if
everything checks out, shows me the following message:
    
<p>
<a href="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817.png" data-rel="lightbox-image-2" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2673" data-permalink="https://cpbotha.net/2016/12/11/pgp-never-gonna-give-you-up/screenshot_20161211-202817/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817.png" data-orig-size="1440,2560" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screenshot_20161211-202817" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817-169x300.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817-576x1024.png" class="alignnone wp-image-2673 size-medium" src="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817-169x300.png" width="169" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817-169x300.png 169w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817-768x1365.png 768w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817-576x1024.png 576w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817-1200x2133.png 1200w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-202817.png 1440w" sizes="(max-width: 169px) 85vw, 169px" /></a>
</p>
    
I can now rest assured that <a href="http://mentat.za.net/">this
specific buddy of mine</a> is never gonna give me up and is never gonna let me
down.
    
Cryptographically signing a message is equally easy, except that you'll
have to enter that long passphrase of yours. OpenKeychain will then make the
signed and optionally encrypted text text available for sharing to any app, or
for copying and pasting:

    
<p>
<a href="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458.png" data-rel="lightbox-image-3" data-rl_title="" data-rl_caption="" title=""><img data-attachment-id="2670" data-permalink="https://cpbotha.net/2016/12/11/pgp-never-gonna-give-you-up/screenshot_20161211-174458/" data-orig-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458.png" data-orig-size="1440,2560" data-comments-opened="1" data-image-meta="{&quot;aperture&quot;:&quot;0&quot;,&quot;credit&quot;:&quot;&quot;,&quot;camera&quot;:&quot;&quot;,&quot;caption&quot;:&quot;&quot;,&quot;created_timestamp&quot;:&quot;0&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;focal_length&quot;:&quot;0&quot;,&quot;iso&quot;:&quot;0&quot;,&quot;shutter_speed&quot;:&quot;0&quot;,&quot;title&quot;:&quot;&quot;,&quot;orientation&quot;:&quot;0&quot;}" data-image-title="Screenshot_20161211-174458" data-image-description="" data-medium-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458-169x300.png" data-large-file="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458-576x1024.png" class="alignnone size-medium wp-image-2670" src="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458-169x300.png" alt="" width="169" height="300" srcset="https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458-169x300.png 169w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458-768x1365.png 768w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458-576x1024.png 576w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458-1200x2133.png 1200w, https://cpbotha.net/wp-content/uploads/2016/12/Screenshot_20161211-174458.png 1440w" sizes="(max-width: 169px) 85vw, 169px" /></a>
</p>
    
Easy peasy, and tested under all sorts of usually-PGP-unfriendly conditions!
    
## Conclusion

Maintaining PGP long-term keys certainly has its issues, but the possibility
of cryptographically signing any message so that recipients can establish with
high confidence that it originated from you is too important to give up.

With an app like OpenKeychain and sufficiently strong passphrase hashing and
secret key encryption, you are able to use your keys with ease from your
telephone.

Granted, you are trading in some security for this convenience. However, given
the choice between discarding my PGP keys completely, vs. taking these steps,
I'll hold on to my keys for a little while longer.

In order to mitigate the potential damage of one of my long-term keys being
compromised, I have resolved to generate and start using a new private key as
soon as I run through my current batch of business cards, and to continue
rotating like this in the future.

Let me know in the comments what you think. Do you know of a better
alternative for remotely verifying the identity and messages of your
correspondents?

 [1]: https://blog.filippo.io/giving-up-on-long-term-pgp/
 [2]: https://twitter.com/FiloSottile/status/807612248223051776
