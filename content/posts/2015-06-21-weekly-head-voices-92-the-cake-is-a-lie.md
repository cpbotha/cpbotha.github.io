---
title: 'Weekly Head Voices #92: The cake is a lie.'
author: cpbotha
type: post
date: 2015-06-21T20:33:00+00:00
url: /2015/06/21/weekly-head-voices-92-the-cake-is-a-lie/
categories:
  - weekly head voices
tags:
  - backyard philosophy
  - backyard psychology
  - experience
  - gpu
  - materialism
  - possession
  - wkhtmltopdf

---

{{< figure src="/wp-content/uploads/2015/06/wpid-del_vera_view.jpg" link="/wp-content/uploads/2015/06/wpid-del_vera_view.jpg" caption="A random winter’s day view from Del Vera, where father’s day was celebrated." >}}

The week of Monday June 15 to Sunday June 21 in bullets: 

<ul class="org-ul">
<li>
    Ran around organizing all kinds of things for the new house. The various institutions have been cooperating <i>very</i> nicely.
  </li>
<li>
    Spent days trying first to fix an implementation of a <a href="http://www.chrisoat.com/papers/Oat-Tatarchuk-Isidoro-Layered_Car_Paint_Shader_Print.pdf">GPU algorithm to simulate car paint</a>, and then to implement an alternative algorithm by the clever boys and girls at NVIDIA. A team-mate finally got everything working by realising that the float16 texture coordinates (long story) we were using to sample a noise texture needed to be float32. Lesson learnt: If you’re seeing splotches when you’re supposed to be seeing snow, check your float precision!
  </li>
<li>
    Spent the rest of the week fighting with <a href="http://wkhtmltopdf.org/">wkhtmltopdf</a>, a tool that converts HTML into PDF. Unfortunately the tool is 50% webkit, and 50% black magic. Lesson learnt: wkhtmltopdf 0.12.2.1 renders internally at 74.8dpi. Accept it, calculate with it, and move on. The upshot of this is that the <a href="http://www.patinformatics.com/blog/next-generation-ng-ip-and-rd-dashboard-a-joint-development-by-evalueserve-and-treparel/">IP Dashboard</a> is now 37% better at exporting charts.
  </li>
<li>
    For some time now, when I have to make decisions, I actively optimise for experiences and not for possessions. At some point in the past I read in the blogosphere that experiences make people happier than possessions, and since then I’ve been paying more attention to this. IT REALLY WORKS!(tm) Tonight I wanted to look up the sources of this idea for you (and for me). Here are the two academic papers causing most of that online discussion, and a summarising blog post:: <ul class="org-ul">
<li>
<a href="http://cornellpsych.org/people/travis/materials/Carter-Gilovich-Relative%20Relativity-JPSP-2010.pdf"><i>The Relative Relativity of Material and Experiential Purchases</i></a> (2010), Travis J. Carter and Thomas Gilovich.
      </li>
<li>
<a href="http://cornellpsych.org/people/travis/materials/Carter-Gilovich-Material%20Experiential%20Identity-JPSP-2012.pdf"><i>I Am What I Do, Not What I Have: The Differential Centrality of Experiential and Material Purchases to the Self</i></a> (2012), Travis J. Carter and Thomas Gilovich.
      </li>
<li>
<a href="http://phys.org/news/2010-03-study-shows-experiences-are-better.html">Study shows experiences are better than possessions</a> -- summarising post on phys.org. Carter and Gilovich’s research (based on on a number of tests and questionnaires they did with a sample of Cornell students) demonstrated that experiences were more satisfying than possessions. Their results also support at least one explanatory mechanism: Experiences are more closely connected to the self. This makes sense: Anybody else can buy the same thing you bought, but, by definition, your experience of some event or adventure is quite unique to you. To my mind, the idea of focusing on the experience rather than the cake at the end is pleasingly complementary to the adage that <i>Life is a journey, not a destination</i>, which I have just learned is due to <a href="https://www.goodreads.com/quotes/24142-life-is-a-journey-not-a-destination">Ralph Waldo Emerson</a>.
    
</li>
</ul>
</li>
<li>
    I’m still terrible at bullets, I know.
  </li>
</ul>

Dear reader(s), have a beautiful and experience-filled week!

 [1]: http://cpbotha.net/wp-content/uploads/2015/06/wpid-del_vera_view-300x129.jpg
