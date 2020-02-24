---
title: "Weekly Head Voices #189: All systems green."
slug: "weekly-head-voices-189-all-systems-green"
date: 2020-02-23T21:57:00+02:00
tags:
  - backyard philosophy
  - gou
  - hetzner
  - medicine
  - quantum mechanics
  - science
  - sean carroll
  - webfaction
categories:
  - weekly head voices
type: "post"
ogimage: "bettys_jock_fishing.jpg"
---

<figure>
{{< img src="bettys_jock_fishing.jpg" link="true" >}}
</figure>

The first Weekly Head Voices of 2020 is almost two months late.

When there's any sort of significant WHV hiatus, you can bet your lucrative
blogging career that there's something important afoot in the life of the
person owning the head that mostly contains the eponymous voices featuring at
the core of this blog's business.

If you prefer that I misuse a pet-related metaphor instead, WHV breaks are
almost like dry noses in dog world.

Indeed, I chose the start of this year to deal with a long-standing health
issue which I had been avoiding and/or postponing for a few years now, thanks
to irrational anxiety. (The irony of this does not escape me.)

I am *quite* happy to report that, in an utterly unsurprising non-turn of
events, science and modern medicine prevailed. Hard.

Please don't get the wrong impression.

I am utterly grateful for the predictability, and for the science, and for
modern medicine and its precise practitioners.

As I sit here, my internal sensors report all systems greener than they have
been in quite a while.

At this moment, life is truly brilliant.

## GOU #1 is now a high-schooler.

At the end of last year, [I wrote about GOU #1 finishing primary
school](/2019/12/08/weekly-head-voices-185-starship-gou-1/#starship-gou-1-taxiing-on-the-runway).

In the meantime, the pace of development seems to have picked up even more.

GOU #1 is now getting on the bus at Super Early O' Clock every morning to go to
her new high school, which sometimes reminds me of a sort of Hogwarts for young
power women.

It feels like she is growing more independent by the day, regularly surprising
us with new skills and capabilities.

Perhaps more importantly, she seems to be handling all of these changes, both
external and internal, with grace and a gratifying helping of reason.

## The whole cpbotha.net-hive has been migrated to a small Hetzner server.

For the past days I've been quite busy migrating this website, along with a
number of others ([vxlabs.com](https://vxlabs.com/),
[medvis.org](https://medvis.org/) and about 10 more), away from WebFaction
(RIP) to a new Hetzner server in Nuremberg.

GoDaddy acquired WebFaction, and they have made clear that they will at some
unknown time in the nearish future pull the plug on the whole WebFaction
setup.

For the 12 years that I was a customer, it was the perfect hoster: The ideal
combination of managed and unmanaged hosting for a very reasonable price.

Although this migration led to quite a bit of work, I am happy that all of the
ported sites are running slightly leaner on the new VPS.

Also, I made use of the opportunity to outfit each ported site with a Let's
Encrypt certificate, meaning we now have 100% SSL.

I would like to note the following possibly helpful learnings:

- [Duplicator](https://wordpress.org/plugins/duplicator/), a wordpress plugin,
  is the perfect solution for transporting a wordpress site from one corner of
  the planet to another.
- You can use [supervisor to run non-php fastcgi processes behind
  nginx](https://vxlabs.com/2020/02/22/supervisor-fastcgi-nginx/).
- After the first wordpress migration, I had a checklist in Emacs Orgmode with
  which I could migrate the other 7 in my sleep, and almost did. See below for
  a Real World Example&trade;.

``` org
** DONE vxuni.com [8/8] [2020-02-22 Sat 15:06]
CLOSED: [2020-02-22 Sat 15:43]

- [X] duplicator the site on the source end
  - disable jetpack image caching, any other caching, as many plugins as you can
  - ensure theme is supported on php 7.x
- [X] setup nginx for new wordpress site
- [X] rewrite your laptop's hosts files so you can access the new site
- [X] create database and user
- [X] install duplicate on destination
- [X] redo the DNS
- [X] certbot
- [X] activate jetpack protect / jetpack -> settings -> security -> brute force
  attack protection.

#+begin_src sql
create database wordpress_blabla;
GRANT ALL PRIVILEGES ON wordpress_blabla.* TO "u_blabla"@"localhost" identified by "difficult password";
flush privileges;
exit
#+end_src

#+begin_src shell
certbot certonly -d vxuni.com,www.vxuni.com --nginx --dry-run
#+end_src
```

## Would you like to split the universe? There's an app for that.

I'm currently reading [*Something Deeply Hidden: Quantum Worlds and the
Emergence of Spacetime* by Sean
Carroll](https://www.npr.org/2019/09/13/760545897/in-something-deeply-hidden-sean-carroll-argues-there-are-infinite-copies-of-you).

Somewhere in there, Carroll mentions the iPhone app [*Universe
Splitter*](https://apps.apple.com/us/app/universe-splitter/id329233299), which
you can use to split the whole universe into copies of itself.

It starts more mundanely, when you have to make a difficult decision between
two options.

Fear no more, because now you can just start up that app, and use quantum
mechanics to make the decision.

As a side effect, you end up splitting the universe.

When you submit your choice, a message is sent to a lab in Switzerland, where a
photon is sent toward a beam splitter.

According to Schrödinger's equation, the splitter turns the photon's wave
function into two components going left *and* right, each of which ends up at a
different detector.

When either detector picks up the photon, it produces a readout that becomes
entangled with its environment (whoops!), quickly leading to decoherence and a
branching of the wave function into two universes.

Now there are two copies of you.

One copy of you will see choice A, and the other will see choice B.

## It's what future you would want, quote edition.

All the way back in March of '19, [I wrote about the suggestion to try to
predict which tasks the completion of which would satisfy future you the most
at the end of the
day](/2019/03/09/weekly-head-voices-164-its-what-future-you-would-want/#thinking-of-future-you).

Well, the other day as I was aimlessly browsing twitter, something which was
decidedly NOT a task that future me would have approved of, or a task anyone
could conceivably ever complete, I came across [this jewel tweeted by John
Arundel](https://twitter.com/bitfield/status/1219309618813337601):

> If we are ever in doubt about what to do, it is a good rule to ask ourselves
> what we shall wish on the morrow that we had done.  -- John Lubbock

Although the message is the same, I find Lubbock's formulation more elegant.

Folks, have a great week, full of satisfied future yous, in all of the
universes that you are about to inhabit!
