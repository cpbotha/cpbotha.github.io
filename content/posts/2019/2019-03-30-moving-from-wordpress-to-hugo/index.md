---
title: "Moving 18 years of this personal blog from Wordpress to Hugo"
slug: wordpress-to-hugo
author: cpbotha
date: 2019-03-30T16:30:23+02:00
draft: true
tags:
  - hugo
  - wordpress
  - gutenberg
categories:
  - howto
type: "post"
---

pretty straight-forward, but I have a thing for posts titled "Moving M years
of K from Y to Z"

As readers of this blog will know by now, I am really not happy with the new post
editor in Wordpress 5, Gutenberg.

I attempted to get used to it, but it feels like it gets in my way 9 out of 10
times as I'm just trying to write a straight-forward long form blog post, like
this one.

For the past 15 years or so, Wordpres
 s was just about perfect for my use case
of writing and publishing blog posts.

not an easy decision

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

# Bonus level: Automatic resizing of images
