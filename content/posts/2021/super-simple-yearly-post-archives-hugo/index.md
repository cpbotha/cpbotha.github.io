+++
title = "Super simple yearly post archives for Hugo"
date = 2021-01-10T15:48:00+02:00
lastmod = 2021-01-10T15:49:45+02:00
slug = "super-simple-yearly-post-archives-hugo"
tags = ["hugo"]
categories = ["howto"]
draft = false
org = true
+++

I was looking for the most simple way to get automatic yearly archives of all
blog posts for the [Hugo](https://gohugo.io/) setup responsible for cpbotha.net (this blog).

Fortunately I ran into [Rohan Verma's template-based solution](https://rohanverma.net/blog/2019/11/15/archive-pages-group-by-year-hugo/) which I could then
simplify into the even more straight-forward shortcode-based solution presented
in this post.

For an example of the output, see [the post archives here](/archive/).

To make this happen on your Hugo setup is a two step process.


## Step 1: Install shortcode {#step-1-install-shortcode}

Save the following snippet as `layouts/shortcodes/archive.html`.

Note that you might have to change `"posts"` in the code below to whatever Hugo
section contains your blog posts.

```go-html-template
{{/*

simple shortcode to display all posts in yearly sections on your archive page
by Charl P. Botha

this is a much simplified version of the yearly post archiving template at:
https://rohanverma.net/blog/2019/11/15/archive-pages-group-by-year-hugo/

*/}}

{{ $prev := 3000}}
{{range where .Site.RegularPages "Section" "posts"}}
{{if .Date}}
{{if gt $prev (.Date.Format "2006")}}
## {{ .Date.Format "2006" }}
{{end}}
{{.Date.Format "02 Jan"}} -- [{{.Title}}]({{.Permalink}})
{{ $prev = .Date.Format "2006"}}
{{end}}
{{end}}
```


## Step 2: Use shortcode {#step-2-use-shortcode}

Use the shortcode on any page as `{{%/* archive */%}}`, as shown in the example below.

Note here that we're using [the shortcode syntax for markdown shortcodes](https://gohugo.io/content-management/shortcodes/#shortcodes-with-markdown),
i.e. `%` instead of the `<` you might be more used to for HTML shortcodes.

```markdown
---
title: "Posts Archive"
slug: "archive"
date: 2021-01-09T16:17:00+02:00
type: "page"
---

Some text that will appear before the archive.



{{%/* archive */%}}
```
