---
title: 'Weekly Head Voices #110: Satoshi.'
author: cpbotha
type: post
date: 2016-07-25T21:27:17+00:00
url: /2016/07/25/weekly-head-voices-110-satoshi/
categories:
  - weekly head voices
tags:
  - asymmetric
  - bitcoin
  - cryptography
  - hash
  - public key
  - spock

---
This update contains carefully selected thought bubbles from the time span between Earth date Wednesday July 20 and Sunday July 24, 2016.

Actually, the majority of this post is taken up by my Poor Man&#8217;s Bitcoin Explanation. If you&#8217;re not a nerd and/or you don&#8217;t have any interest in fabulous new virtual currencies that manage to _work around_ a whole constellation of systems and rules put in place by governments the world over (STICK IT TO THE MAN BY THE POWER OF MATH!!), just skip over the next section.

# Bitcoin in 10 minutes

I finally got around to studying the math behind bitcoin.

If you more or less know what a **hash** is (the hash is as a short string, e.g. 32 characters, than can be calculated from a file of arbitrary size; if even one byte in the file changes, the hash will be completely different; [read more on wikipedia][1], or ask me in the comments) and you more or less know how the **public and private keys** in asymmetric cryptography work (you can encrypt (encode) something with the public key, ONLY its matching secret private key can decode it; you can SIGN any file with a secret private key, the authenticity of that signature can be proven by anyone with matching public key; [read more on wikipedia][2], or ask in the comments!) you can more or less understand bitcoin in particular and cryptocurrency in particular.

Let&#8217;s say you were to generate a completely random private key, you can then use a well-known procedure to derive its matching public key. By applying two successive hash functions to that public key, you have a **bitcoin address**!

If I were to owe you money, you could then give me that bitcoin address.

I could then pay you back by writing a specially crafted message called a **bitcoin transaction**, in which I describe that I am transferring some bitcoins TO the address that you gave me FROM another bitcoin address (henceforth the source address), of which I have the matching secret private key.

In that message, I cryptographically _sign_ the input part, a modified version of the whole transaction, including source and destination address, with the (secret) private key matching that source address. The signature mathematically proves that I own the bitcoins I am about to transfer, and it mathematically locks in the whole transaction, so that the destination addresses also can&#8217;t be changed. I generally also allocate a very small amount (by leaving money unaccounted for) as a transaction fee. We&#8217;ll see why in a minute.

I broadcast the signed transaction to the bitcoin network, where it eventually gets picked up by one or more of the **bitcoin miners**. Miners batch together a number of transactions into a block, together with a hash of the last successfully mined block, and a **piece of random data called the nonce**. They then proceed to continuously hash the block, changing the nonce every time so that the hash changes, until the first few digits of the hash are zeroes.

Based on the nature of cryptographic hashes, this will statistically take a very long time. One could get lucky and get the correct hash early, but generally it requires a whole lot of number crunching, which means kilowatts, which means actual money. The special hash resulting from this number crunching is called the **proof of work**.

When a miner has hit the jackpot, they broadcast the block to the network, which recognises that it&#8217;s the next valid block by checking the hash, and then, in a peer to peer fashion, irreversibly records this as the next block in the globally shared **block chain**. The successful miner receives 12.5 bitcoins (currently worth about 7500 EURO; thank you Wayne Kitching for the correction in the comments! &#8212; on July 9 of this year, this reward was halved, for the previous period it was 25 BTC per block) as well as all of the included per-transaction fees.

Now you probably understand why so many people are mining so enthusiastically. (No, you can&#8217;t really participate anymore with your home PC like you could in the early days; you have to acquire a large room full of **bitcoin mining ASICs**, circuitry that has been purpose-designed for one thing: bitcoin mining, to make any kind of impact. On the other hand, if you play the lottery, you might as well fire up your PC.)

You could now go and print out your private key (or its QR code) and the matching bitcoin address (actually you only need the private key, the public key and address can be derived from it) and then destroy all of your computers. Whenever you need to send that bitcoin somewhere, you simply type in the private key or rather scan the QR code, and then repeat the process of creating a bitcoin transaction, using your private key.

The money is never actually stored anywhere, only transactions encoding the movement of money from one random virtual address to another are. The block-chain is mathematically unbreakable and unforgeable.

I find the relative simplicity of the whole thing utter genius: A usable and versatile currency backed by hard math. YEAH!

## Further reading

The two sources that helped me the most were [Bitcoin transactions, metaphorically (Part 1)][3] and [Bitcoin transactions, technically (Part 2)][4], both on the [What does the quant say?][5] blog.

Hmmm, that blog title unfortunately reminds me of this:

<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/jofNR_WkoCE?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

# The end of the internet

Last night I realised why it feels like there&#8217;s so much less happening on the internet these days. I seem to be able to go bed with the feeling that I&#8217;ve finished reading the internet. In other words, my usual hard-to-break cycle of reddit-inoreader-google+(yes I still use it!)-hackernews-twitter-facebook-reddit-argh-go-to-bed-reddit-reddit/r/emacs-reddit/r/strange-new-programming-language-ARGH-ARGH ARGH twitter ends at a more or less normal time, because the potentially dopamine-inducing-but-mostly-not-because-disappointing items stop flooding in.

In any case, I had completely forgotten that the Northern Hemisphere (hi there everyone! enjoy your vacation! **WINTER IS COMING.**) is currently on vacation, whilst down South we&#8217;re all wondering if the internet is broken again.

# Gruffalo

A few mornings ago I had that wonderful guess-what&#8217;s-the-most-dangerous-animal-on-the-planet conversation with my six year old (Genetic Offspring Unit #2). It started with her explaining how afraid she was of certain insects (not all of &#8217;em interestingly enough), at which point I, enthusiastically assisted by GOU #1 (with whom I had a similar conversation some years ago), started the guessing game with her.

It was fabulous seeing her widening eyes when, after guessing tigers, and elephants, and sharks, and whales, we guided her to the correct answer.

Perspective shift.

I did (and do) my best to contextualise as well as possible the fact that we humans are the most scary beings on the planet.

# LLAP

Spock, from the original Star Trek TV series which fortunately also aired in South Africa (must have been late 70s to early 80s), made a huge impact on me as a young boy, probably at role model level.

So when I saw the trailer of &#8220;For the Love of Spock&#8221;, a forthcoming documentary about Leonard Nimoy, the actor who really _was_ Spock for almost 50 years, and who very unfortunately died in 2015, I was not able to remain completely tearless.

Live long and prosper!

<div class="jetpack-video-wrapper">
  <span class="embed-youtube" style="text-align:center; display: block;"><iframe class='youtube-player' type='text/html' width='840' height='473' src='https://www.youtube.com/embed/sZcIWWjLVZ8?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' allowfullscreen='true' style='border:0;'></iframe></span>
</div>

 [1]: https://en.wikipedia.org/wiki/Cryptographic_hash_function
 [2]: https://en.wikipedia.org/wiki/Public-key_cryptography
 [3]: http://whatdoesthequantsay.com/2014/03/29/bitcoin-transactions-metaphorically/
 [4]: http://whatdoesthequantsay.com/2014/05/04/bitcoin-transactions-technically-part-2/
 [5]: http://whatdoesthequantsay.com/
