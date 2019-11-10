---
title: "We now have self-hosted isso comments"
date: 2019-11-10T16:28:00+02:00
tags:
  - blog
  - comments
  - disqus
  - isso
categories:
  - howto
type: "post"
---

As one is prone to do on a Saturday, I decided yesterday to migrate all 2500+
of the comments on this site to isso, an open-source self-hosted commenting
system.

TL;DR: Comments on this blog are now managed by self-hosted, open-source isso
that I control. Commenting should be much faster and more fun, so have at it!

## Why I recommend strongly against Disqus.

You might recall, or you could just check [the relevant blog
post](/2019/03/31/wordpress-to-hugo/#transfer-comments-to-disqus), that I
ported all comments from wordpress to disqus (grrr...) in March of this year,
when I upgraded to the Hugo static site generator.

At that point, I had already poured quite some time into the Hugo migration,
and so I thought that trying out Disqus for a while, on a personal site without
any ads whatsoever, couldn't hurt.

I could always at a later stage simply export my comments from there, right?

Wrong.

I triggered the built-in export-functionality in the Disqus admin interface.

The site then shows a message that it will email you when the export is ready.

Well, it's now 24 hours later and that email never came...

(I retried at least 3 times. I even [tweeted at
them](https://twitter.com/cvoxel/status/1193181451002482690), because there's
no other way to contact support.)

When you read the fineprint on [the relevant help
page](https://help.disqus.com/en/articles/1717199-importing-exporting#exporting-from-disqus),
you see the following (emphasis mine):

> Please note: exports **may not be available for all sites**, particularly
> those of a large size. If you've requested an export file more than twice and
> still have not received a download link from us, it's likely that an export
> for your site is **currently unavailable**.

So that's pretty reassuring! You *might* get an export. It depends... Whatever
the case may be, you *won't* get any sort of feedback however.

I guess this is an issue with any hosted solution.

However, one would expect from any such service that advertises the possibility
to export one's *own data*, even on the free tier, that one is in fact
*allowed* to export one's own data.

NOT IN DISQUS WORLD!

Anyways, I was not going to let this highly disappointing performance stop my
migration efforts.

## Enter isso!

After discovering that the open-source self-hosted [commento
software](https://gitlab.com/commento/commento) requires at least Postgres 9.5
but webfaction (my webhoster for years and years now, unfortunately our ways
will probably have to part thanks to the godaddy acquisition) is stuck at
Postgres 9.4, I decided to configure isso, the same [commenting system I have
running on vxlabs](https://vxlabs.com/2019/04/06/isso-on-webfaction/).

### New feature: Auto-approve previously approved authors.

However, to make it a little more interesting, I decided to implement an
auto-moderation feature in isso that I used to use in all my wordpress
installations:

*Auto-approve authors who have had comments approved in the past N months*.

Long story short, you can find my work in [this github fork of
isso](https://github.com/cpbotha/isso/commits/cpbotha-auto-moderate-known-authors).

I will soon create a PR into the main repo. It might or might not get accepted.

Simply edit the `moderation` section of your `isso.cfg` to look something like
the following:

``` ini
[moderation]
enabled = true
activate-if-email-previously-approved = true
```

When someone leaves a comment, and their email address has had a comment
approved within the last 6 months, the new comment will be automatically
activated.

The advantage of this feature is that comment-conversations can happen much
more fluidly, without me having to approve each and every comment that comes
in.

### Migrating comments in spite of Disqus.

In NormalWorld, I would have exported an XML from Disqus, and just imported
that into isso using the built-in functionality.

However, in DisqusWorld, the user has to suffer.

Fortunately I could import the bulk of the old comments (up to March of this
year) using the old Wordpress site export and isso's great import function.

For the remaining 25 comments, I manually copied each and every one of them,
along with author name, email (if I knew it) and exact date, and then inserted
them manually into the isso sqlite database, using the amazing
[sqlitebrowser](https://sqlitebrowser.org/).

I discovered three possibly useful facts:

- If the `parent` column in a `comment` record is not set explicitly to `NULL`
  in the case of no parent, the comment does not show up.
- Isso supports only one level of nesting in the database. This means the
  `parent` column has to point to a root, i.e. parent-less, comment.
- Isso stores timestamps as seconds since epoch. You can use the following SQL
  to convert a timestring to seconds since epoch:
  
``` sql
select strftime("%s", "2019-08-22 14:11");
```

I was up until 01:00 getting all of this running smoothly.

That is how much I love this blog and its people. :D

## Conclusions.

I am happy that all of your comments are now self-hosted on this server using
open-source software that I have a good grasp of.

I am happy that your valuable thoughts are backed up each and every night.

You should also notice that pages load much faster (disqus is quite slow).

(Also: MARKDOWN!)

Ok folks, I hope this further diminishes any barriers that there might have
been to you leaving us a message now and then!
