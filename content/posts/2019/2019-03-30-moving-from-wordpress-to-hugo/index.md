---
title: "Moving 18 years of this personal blog from Wordpress to Hugo"
slug: wordpress-to-hugo
author: cpbotha
date: 2019-03-31T00:10:00+02:00
tags:
  - hugo
  - wordpress
  - gutenberg
  - ox-hugo
categories:
  - howto
type: "post"
---

It sounds a bit more involved than it turned out to be, but I have a thing for
posts titled "Moving M years of K from Y to Z".

As can be seen in the [history page](/about/history/) or rather the [first
weblog entry dated 2001-02-27](/2001/02/27/1469/), this blog has been around
for more than 18 years.

It started as some CGI script, then spent some time as a LiveJournal, then,
thanks to meeting [Professor Biella
Coleman](https://en.wikipedia.org/wiki/Gabriella_Coleman) who was at that
point still a grad student, went through a Movable Type phase and then, at
some point, converted to Wordpress.

I don't know when exactly the Wordpress stage started, but it's probably not
too long after Wordpress was born in 2003 somewhere.

Anyways, after many happy years together, our ways are parting.

The new block-based editor in Wordpress 5, [Gutenberg](/tags/gutenberg/),
caters more for Wordpress as a CMS, and far less for Wordpress as a platform
for long-form blogging.

Personally I have noticed that the new editor gets in my way most of the time,
where the pre-Gutenberg editor worked just perfectly, for my use case.

Because life is short, and many more blog posts have to written, I made the
decision, not easily, to move this blog away from Wordpress, to a different
and hopefully more suitable platform.

I ended up choosing Hugo because its native mode of operation involves me
writing posts in some form of text editor, which is my preferred modality in
any case, but primarily because of all the static generators, it was the only
one with a prominent [Emacs Orgmode plugin](https://ox-hugo.scripter.co).

(Based on what I now know about Hugo, it looks like once again Emacs Orgmode
helped me make the best decision.)

In the rest of this post I describe the process of migrating the blog you see
before you from Wordpress to Hugo.

# Export data from Wordpress.

I used [SchumacherFM's
wordpress-to-hugo-exporter](https://github.com/SchumacherFM/wordpress-to-hugo-exporter)
to export my whole wordpress site to a Hugo-compatible project.

Following(ish) [the
instructions](https://github.com/SchumacherFM/wordpress-to-hugo-exporter#usage-with-a-self-hosted-wordpress-installation),
I git cloned the `wordpress-to-hugo-exporter` into the `wp-content/plugins`
folder of the relevant wordpress installation, and then I invoked the export
script with `php hugo-export-cli.php`.

The end-result was a 600MB `/tmp/wp-hugo.zip` which I SCP'd down to my laptop
and then unzipped into a directory called `hugo-export`.

# Install hugo get site up and running.

The main goal here was to get Hugo running with the exported wordpress data.

After installing hugo with `brew install hugo`, I continued with Hugo's [quick
start instructions](https://gohugo.io/getting-started/quick-start/).

Create the new Hugo site:

```
hugo new site cpbotha.net
```

Copy the exported contents into the Hugo site:

```
mv hugo-export/* cpbotha.net/content/
```

I chose [the minos theme](https://themes.gohugo.io/hugo-theme-minos/) from the
great [Hugo Themes repository](https://themes.gohugo.io) and installed it into
the new site like this:

```
cd cpbotha.net/themes
git clone https://github.com/carsonip/hugo-theme-minos.git
```

Before starting up the new site for the first time, I edited the top-level
`config.toml` so it looked like the following:

```toml
baseURL = "https://cpbotha.net/"
languageCode = "en-us"
title = "voices in my head"
theme = "hugo-theme-minos"
# required for disqus comments, see next section
disqusShortname = "cpbotha"

[permalinks]
  # mimic wordpress permalink configuration for future posts
  # exported wordpress posts have `url` correctly set which overrides everything
  posts = "/:year/:month/:day/:slug/"
```

Note: The theme that you currently see on this site is a modified version of
minos, implemented using Hugo's [Theme
Components](https://gohugo.io/themes/theme-components/) mechanism.

## Fire up Hugo in development mode!

To see your site in all of its new static glory, you can start Hugo in
development mode from the project's top-level directory:

```
cd cpbotha.net/
hugo serve -D
```

By pointing your browser at `http://localhost:1313`, you'll be able to see a
dynamic version of your site that automatically refreshes whenever you make
changes to any of the underlying files.

# Transfer comments to Disqus.

This blog's small but amazing group of commenters, and the comments they have
written over the years, are super valuable to me. It was important to transfer
them and their work over to the new blog without a hitch.

## Motivation.
I considered self-hosting comments using something like
[Commento](https://github.com/adtac/commento), but the fact that I was able to
get ad-free Disqus for free, as this site does not do advertising, and the
fact that the conversion from Wordpress to Disqus is well-documented, won me
over.

Furthermore, going from Wordpress to Commento often involves a quick stop at
Disqus in any case. In other words, the option of self-hosting remains.

## Procedure.

The Disqus plugin for Wordpress has an automatic "import comments" mode which
promises to transfer all of your wordpress comments to Disqus.

In my case, this worked for most posts, except those with more than 60 or 70
comments, in thich no comments were transferred.

I ended up following the "manual import" procedure [documented in the Disqus
help](https://help.disqus.com/import-export-and-syncing/importing-comments-from-wordpress).

In short, you export your whole wordpress site as XML / WXR, download the
file, and then import that using the upload functionality of [the Disqus
import site](https://import.disqus.com/).

This seemed to have transferred all of my comments.

In spite of multiple attempts at automatic import, followed by the manual
import, Disqus was clever enough not to duplicate any comments.

### Export domain name should be same as display domain name.

It is important when you export your Wordpress comments, that the domain-name
you export from is the same as the domain-name where you'll end up displaying
the Disqus comments.

If this is not the case, you will have to edit the exported XML files to
search and replaced all of the instances of export domain name to display
domain name.

# Build and upload the new static hotness.

My workflow now looks like this:

1. Write new post in Emacs with `hugo serve -D` running. The browser window
   adjacent to Emacs updates in real-time showing my changes. (I will eventually look into
   [ox-hugo](https://ox-hugo.scripter.co) so I can write posts in orgmode.)
2. When I'm happy with the post, I build the site with `hugo -d ~/Downloads/cpbotha.net`
   and sync it up to my web host using `rsync`
   
You can build the site by just invoking `hugo` in the top-level directory, in
which case the output of the build will end up in a sub-directory named
`public`.

However, I keep the source to this blog in a git repository in my Dropbox, and
I would prefer not syncing the expendable 600MB+ output directory, instead
building it and syncing it from `~/Downloads`.

The little bash script I used to perform step 2 in one go looks like this:

```sh
#!/bin/bash
hugo -d ~/Downloads/cpbotha.net
# sync contents of public dir into static_cpbothanet/
rsync -av --progress ~/Downloads/cpbotha.net/ \
cpbotha@my.webhost.com:~/webapps/static_cpbothanet
```

# Bonus level: Bundling and automatic resizing of images.

As each edition of [the WHV](categories/weekly-head-voices/) usually contains
at least an image or two, an important piece of the puzzle was how to keep
images together with the markdown post source, instead of in a separate static
directory.

In addition, Wordpress has this great feature where it automatically resizes
images on upload, enabling posts to inline lower resolution versions that can
be clicked on to see the full resolution.

I had resigned myself to the reality that this would probably be a manual
process for Hugo.

Thanks to a [super useful and detailed post by Laura
Kalbag](https://laurakalbag.com/processing-responsive-images-with-hugo/), I
learned that the image-bundling problem had already been addressed by Hugo,
and that Laura Kalbag had developed a Hugo shortcode which solved the second
problem using Hugo's built-in image processing and a relatively new browser
feature called [srcsets](https://ericportis.com/posts/2014/srcset-sizes/).

With her `img` shortcode, high-resolution images are automatically resized
into multiple lower resolution versions at build time, all of which will be
offered to the client, which will then decide which to download based on the
client-side display parameters.

With regard to the image bundling, this is simply a matter of creating a
directory containing the relevant images and the post contents in a file
called `index.md`.

In my case, I would create a post by invoking the following command in the
top-level directory:

```sh
hugo new content/posts/2019/some-post-slug/index.md
```

Based on the `permalinks` setting in the `config.toml`, this post will be
available at `/year/month/day/slug-in-frontmatter/`. The `index.md` can refer
to images that are in the same directory using just their relative filenames.

# Mailing lists.

In addition to The Commenters mentioned above, I also treasure The Readers. :)

On the Wordpress blog, I had already started making use of
[Mailchimp](https://mailchimp.com/) a while back for the daily and the weekly
post emails, in addition to Wordpress.com's own email subscription which
services the largest group of readers.

I briefly looked into [tinyletter](https://tinyletter.com/), but then decided
that it made the most sense to migrate the Wordpress.com email subscribers
over to the Mailchimp daily email list.

It was relatively straight-forward to export a CSV with subscriber address
from Wordpress.com and then to import that into the Mailchimp list.

# Wrapping up.

Converting this blog from Wordpress to Hugo went significantly more smoothly
than I expected. In fact, the first Hugo version was online after a single
evening of work.

Other than that, Hugo has already impressed me a number of times with its
speed, and features that have clearly been thought through. Besides the
built-in image processing and the theme composition, there are smaller but
still super useful features such as [the
archetypes](https://gohugo.io/content-management/archetypes/) which I have
configured to help me start a blog post more easily.

Let me know in the comments if you have any other questions.

Here's to at least 18 more years of blog posts!
