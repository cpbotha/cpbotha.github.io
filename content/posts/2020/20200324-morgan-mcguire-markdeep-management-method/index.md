---
title: "The Morgan McGuire Markdeep project Management Method: MMMMM."
slug: "the-morgan-mcguire-markdeep-project-management-method-mmmmm"
date: 2020-03-24T21:37:00+02:00
tags:
  - graphics
  - markdeep
  - markdown
  - morgan mcguire
  - orgmode
  - project management
categories:
  - howto
type: "post"
ogimage: "mmmmm_example_journal.jpg"
---

This weekend, Morgan McGuire, graphics and game programming god, [tweeted a
thread about his text journal based method of software development project
management](https://twitter.com/CasualEffects/status/1241329539902570498).

Here I single out three of the tweets, but you should really read the whole
thread:

> When coding, I always maintain a journal in the repo (I happen to use Markdeep
> for this now) with a TODO list.
>
> Tasks are at the level of one hour for "today" stuff, one day for next week,
> and then week- or longer level tasks.
>
> I expand the details for the next week on Friday.

Tweet 3:

> When I start working on the top, ~1-hour item, on the list, I immediately
> expand it recursively until the subtasks are completely braindead to
> implement.
>
> I do all of the hard part of programming here, in the TODO list, figuring out
> the library calls, designing the APIs, etc.

Tweet 4:

> When I get into the actual source code, I'm just working from my own
> walk-through on the TODO list, and I only need to think about syntax and code
> cleanup. I can focus on programming legibly in the small instead of worrying
> about the big picture.

He shows the following screenshot as an example:

{{< img src="mmmmm_example_journal.jpg" link="true" >}}

This is such a brilliant way of doing the highest level "programming" in an
outlining tool, and then working one's way down until it's eventually time to
jump into the code.

I can also immediately see how well this would work in a team context.

During the planning session, the outline could be collaboratively fleshed
out. Furthermore, as McGuire states, it can be fleshed out differently
depending on the experience level of the team member.

This makes me wonder how much we as engineers *really* need the Jiras and the
YouTracks and the DevOpses of the world?

(Just joking folks, I know we need it, but perhaps we could do with a little
more MMMMM in our lives?)

## Markdeep.

Almost in passing McGuire mentions markdeep, the system he designed for
extremely agile technical documentation.

A friend from work introduced me to this years ago (thanks HB!), but then I
somehow missed its genius.

One of the core ideas that makes markdeep so interesting and useful, is that
the markdeep plaintext markup (it's like supercharged markdown) is embedded in
an extremely thin layer of HTML which invokes the markdeep.js renderer on
itself.

In other words, you edit the self-contained `.md.html` file with your favourite
text editor, but when you open this file in your browser, a single line of HTML
at the end pulls in `markdeep.min.js` from a CDN or from your local disc, and
renders the beautifully typeset version of the document.

As if that was not enough, markdeep has extensive support for the SVG rendering
of ascii art.

See the following pages for more information:

- [The Markdeep website](https://casual-effects.com/markdeep/).
- [The extensive Markdeep demo
  document](https://casual-effects.com/markdeep/features.md.html) - especially
  the [diagram
  examples](https://casual-effects.com/markdeep/features.md.html#diagramexamples)
  are impressive!

For my own notes I am sticking to [Orgmode](https://orgmode.org/) (if you're an
emacs user, it's more powerful), but there will surely be situations where the
self-contained Markdeep makes more sense.

## The Graphics Codex.

Markdeep has been used to author a number of books, but [The Graphics
Codex](http://graphicscodex.com/) must be one of the more amazing examples, in
terms of its interactivity and just general prettiness.

The iPhone app version looks like this:

<a href="http://graphicscodex.com/">
{{< img src="iphone5-large.png" >}}
</a>

I bought the web version not because I currently need a graphics reference, but
rather because it is a thing of beauty, and because I wanted to be able to see
better how it all works.
