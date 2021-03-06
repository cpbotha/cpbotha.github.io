---
title: 'Weekly Head Voices #123: A semblance of a cadence.'
author: cpbotha
type: post
date: 2017-06-28T19:29:59+00:00
url: /2017/06/28/weekly-head-voices-123-a-semblance-of-a-cadence/
categories:
  - weekly head voices
tags:
  - asp.net core
  - backyard philosophy
  - c++
  - emacs
  - gtd
  - habits
  - org2blog
  - orgmode

---
{{< figure src="/wp-content/uploads/2017/06/IMG_0321-PANO-1024x598.jpg" link="/wp-content/uploads/2017/06/IMG_0321-PANO.jpg" caption="Yes, we ended up in the mountains again.">}} 

In the period from Monday June 12 to Sunday June 25 we were mostly trying to get through the winter, fighting off a virus or three (the kind that invades biological organisms you nerd) and generally nerding out.

One more of my [org2blog pull requests][1] was merged in: You can now configure the thumbnail sizes your blog will automatically show of your uploaded images. Getting my own itch scratches merged merged into open source projects never fails to makes me happy, even although in this case there can’t be more than 5 other people who will ever use this particular functionality.

Anyways.

# ASP.NET Core SURPRISE!

For a work project I was _encouraged_ to explore Microsoft’s brand new [ASP.NET Core][2]. While on the one hand I remain wary of Microsoft (IE6 anyone?), I am an absolute sucker for new technology on the other.

You may colour me impressed.

If I had to describe it in one sentence, I would have to describe ASP.NET Core as Django done in C#. You can develop and deploy this on Windows, Mac or Linux. You model and query your data using Entity Framework Core and LINQ for example, or Dapper if you prefer performance and don’t mind the SQL (I don’t), or both. You write controller classes and view templates using the Razor templating language.

C# 7.0 looks like it could be a high development velocity language. It has modern features such as lambdas with what looks like real closures (unlike C++ variable capturing), as well as the [null coalescing operator (??)][3] and the [null conditional operator (?.)][4], the latter of which looks superbly useful. Between Visual Studio on Windows and the Mac, or the new Intellij Rider IDE (all platforms) or Visual Studio Code (all platforms), the tooling is top notch.

Time will have to tell how it compares to Python with respect to development velocity, a competition that Python traditionally fares extremely well at.

Where ASP.NET Core wins hands down is in the memory usage department: By default you deploy using the Kestrel web server, which runs your C# code using _multiple_ libuv (yeah, of lightning fast node.js event loop fame) event loops, all in threads.

With Django I usually deploy as many processes as I can behind uwsgi, itself behind nginx. The problem is that with Python’s garbage collector, these processes end up sharing very little memory, and so one has to take into account memory limits as well as CPU count on servers when considering concurrency.

The long and the short of this is that one will probably be able to process many more requests in parallel with ASP.NET Core than with Django. With uwsgi and Django I have experimented with gevent in uwsgi and monkey patching, but this does not work as well as it does in ASP.NET Core, which has been designed with this concurrency model in mind from the get go. My first memory usage and performance experiments have shown compelling results.

Hopefully more later!

# A cadence of accountability

Lately my [Deep Work habits][5] have taken a bit of a hit. At first I could not understand how to address this, until I remembered mention of a _cadence of accountability_ in [The Book][6]_._

Taking a quick look at [that post][5], I understood what I had forgotten to integrate with my habits. Besides just doing the deep work, it’s important to “keep a compelling scoreboard” and to “create a cadence of accountability”.

Although I was tracking my deep work time using the [orgmode clocking commands][7] (when I start “deep working” on anything, I make an orgmode heading for it in my journal and clock in; when I’m done I clock out; orgmode remembers all durations) I was not regularly reviewing my performance.

With orgmode’s `org-clock-report` command (`C-c C-x C-r`), I can easily create or update a little table, embedded in my monthly journal orgfile, with all of my deep work clocked time tallied by day. This “compelling scoreboard” gives me instant insight into my weekly and monthly performance, and gives me either a mental kick in the behind or pat on the shoulder, depending on how many deep work hours I’ve been able to squeeze in that day and the days before it.

The moment I started doing this at regular intervals, “creating a cadence of accountability” in other words, I was able to swat distractions out of the way and get my zone back.

This is an interesting similarity with [GTD][8] (which I don’t do so much anymore because focus is far more important to me than taking care of sometimes arbitrary and fragmentary tasks) in that GTD has the [regular review][9] as a core principle.

Us humans being so dependent on habits to make real progress in life leads me to the conclusion that this is a clever trick to acquire behaviour that is not habitual: Work on an auxiliary behaviour that is habitual, e.g. the regular review, that encourages / reinforces behaviour that is perhaps not habitual, e.g. taking care of randomly scheduled heterogeneous tasks (GTD) or fitting in randomly scheduled focus periods (Deep Work of the journalistic variant).

As an aside, cadence in this context is just a really elegant synonym for habit. I suggest we use it more, especially at cocktail parties.

 

 [1]: https://github.com/org2blog/org2blog/pull/226
 [2]: https://docs.microsoft.com/en-us/aspnet/core/
 [3]: https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/null-conditional-operator
 [4]: http://geekswithblogs.net/BlackRabbitCoder/archive/2015/06/05/c.net-little-wonders-null-conditional-operator-in-c-6.aspx
 [5]: /2017/01/09/deep-work-a-welcome-kick-in-the-butt/
 [6]: http://calnewport.com/books/deep-work/
 [7]: http://orgmode.org/manual/Clocking-commands.html
 [8]: /tag/gtd/
 [9]: https://zenhabits.net/weekly-review-key-to-gtd-and-achieving/
