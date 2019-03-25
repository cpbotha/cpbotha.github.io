---
title: Closure expressions in Swift
author: cpbotha
type: post
date: 2016-01-07T20:01:00+00:00
url: /2016/01/07/closure-expressions-in-swift/
categories:
  - howto
tags:
  - anonymous functions
  - apple
  - closure expressions
  - lambda
  - python
  - swift

---
[Swift][1] is a new high-performance compiled language designed by Apple. I&#8217;ve had some experience using it for an IOS development project, but the language is open source and is already available for Linux. 

Some of you are probably able to appreciate the irony of me writing a blog post about Apple&#8217;s new programming language Swift, but here we are. :) I am, grudgingly, really impressed by Apple&#8217;s good work. 

In this post I&#8217;m going to chat about _closure expression syntax_, in the process showing you IBM&#8217;s Swift Sandbox, an online tool for experimenting with Swift. 

Let&#8217;s start with a simple example (slightly modified from [Apple&#8217;s documentation on Swift closures][2]) for sorting a list of strings in reverse alphabetical order: 

<div class="org-src-container">
  <pre class="src src-swift"><span style="color: #7F9F7F;">// names will be constaint, so we use let and not var</span>
<span style="color: #F0DFAF; font-weight: bold;">let</span> <span style="color: #DFAF8F;">names </span>= [<span style="color: #CC9393;">"Chris"</span>, <span style="color: #CC9393;">"Alex"</span>, <span style="color: #CC9393;">"Ewa"</span>, <span style="color: #CC9393;">"Barry"</span>, <span style="color: #CC9393;">"Daniella"</span>]

<span style="color: #7F9F7F;">// function taking two parameters and returning boolean</span>
<span style="color: #F0DFAF; font-weight: bold;">func</span> <span style="color: #93E0E3;">backwards</span>(s1: <span style="color: #7CB8BB;">String</span>, <span style="color: #F0DFAF; font-weight: bold;">_</span> s2: <span style="color: #7CB8BB;">String</span>) -&gt; <span style="color: #7CB8BB;">Bool</span> {
    <span style="color: #F0DFAF; font-weight: bold;">return</span> s1 &gt; s2
}

<span style="color: #F0DFAF; font-weight: bold;">let</span> <span style="color: #DFAF8F;">reversed </span>= names.sort(backwards)

print(<span style="color: #CC9393;">"Reversed alpha:"</span>, reversed)
</pre>
</div>

That&#8217;s a complete compilable program in Swift, which you can run directly in your browser by clicking [here][3]. 

We use `let` to define a list of strings. Swift is strongly-typed, but in this case it simply infers the type of the `names` variable from the value that&#8217;s assigned to it. MAGIC! 

If we were planning to change the value of the `names` list at some point, we would have had to use `var` (mutable) instead of `let` (immutable). 

We then define a function called `backwards` that takes two strings, and returns the true value if the first is larger than the second. In the final let statement, we call the `sort()` method on the names list, but we pass it the `backwards()` function, which it will use to compare elements during sorting. Because we have flipped the `s1` and `s2` variables, we get our list back in reverse alphabetical order. 

`sort()` can be seen as a higher order function that takes the `backwards()` function as one of its inputs, and uses it to do its work. 

Since we&#8217;re only using the `backwards()` function once, it would have been pretty convenient if there were some way to define it more compactly and in-place. 

This is exactly what Swift&#8217;s `closure expression syntax` is for. Here&#8217;s the above code, with the `backwards()` function written as a closure expression: 

<div class="org-src-container">
  <pre class="src src-swift"><span style="color: #F0DFAF; font-weight: bold;">let</span> <span style="color: #DFAF8F;">names </span>= [<span style="color: #CC9393;">"Chris"</span>, <span style="color: #CC9393;">"Alex"</span>, <span style="color: #CC9393;">"Ewa"</span>, <span style="color: #CC9393;">"Barry"</span>, <span style="color: #CC9393;">"Daniella"</span>]

<span style="color: #7F9F7F;">// closure expression syntax for inline anonymous function:</span>
<span style="color: #7F9F7F;">// { (args) -&gt; returnType in statements }</span>
<span style="color: #F0DFAF; font-weight: bold;">var</span> <span style="color: #DFAF8F;">reversed </span>= names.sort({ (s1: <span style="color: #7CB8BB;">String</span>, s2: <span style="color: #7CB8BB;">String</span>) -&gt; <span style="color: #7CB8BB;">Bool</span> <span style="color: #F0DFAF; font-weight: bold;">in</span> <span style="color: #F0DFAF; font-weight: bold;">return</span> s1 &gt; s2})

print(<span style="color: #CC9393;">"Reversed:"</span>, reversed)
</pre>
</div>

(You can run this Swift code in your browser by clicking [here][4].) 

Instead of having to define and name a separate function, we can specify a function in the exact spot where it&#8217;s needed, using _closure expression syntax_ i.e.: `{ (parameters) -> returnType in statements }`. 

For you Python-heads out there (MY PEOPLE!), the above code can be written in Python as follows: 

<div class="org-src-container">
  <pre class="src src-python"><span style="color: #DFAF8F;">names</span> = [<span style="color: #CC9393;">"Chris"</span>, <span style="color: #CC9393;">"Alex"</span>, <span style="color: #CC9393;">"Ewa"</span>, <span style="color: #CC9393;">"Barry"</span>, <span style="color: #CC9393;">"Daniella"</span>]

<span style="color: #DCDCCC; font-weight: bold;">reversed</span> = <span style="color: #DCDCCC; font-weight: bold;">sorted</span>(
<span style="color: #DCDCCC; background-color: #4F4F4F;"> </span>   names,
<span style="color: #DCDCCC; background-color: #4F4F4F;"> </span>   <span style="color: #DCDCCC; font-weight: bold;">cmp</span>=<span style="color: #F0DFAF; font-weight: bold;">lambda</span> s1, s2: 0 <span style="color: #F0DFAF; font-weight: bold;">if</span> s1 == s2 <span style="color: #F0DFAF; font-weight: bold;">else</span> (-1 <span style="color: #F0DFAF; font-weight: bold;">if</span> s1 &gt; s2 <span style="color: #F0DFAF; font-weight: bold;">else</span> 1))

<span style="color: #F0DFAF; font-weight: bold;">print</span>(<span style="color: #DCDCCC; font-weight: bold;">reversed</span>)
</pre>
</div>

In Python, `lambda` is used to specify anonymous function objects (our closure expression syntax, in other words). The compare function is defined differently, which is why it&#8217;s somewhat more complicated, but the principle is the same. 

Whilst typing this blog, I downloaded Swift 2.2 from the [open source download site][5] and installed it on my Ubuntu 14.04 laptop (the internet is so slow over here, we have to multi-task to stay sane). After compiling both the examples using `swiftc whatever.swift`, the resulting binaries are about 21 Kbytes each (they are dynamically linked to a number of system libraries, and the 5M `libswiftCore.so`). 

<div class="figure">
  <p>
    <a href="https://cpbotha.net/wp-content/uploads/2016/01/swift-sort-binaries.png" data-rel="lightbox-image-0" data-rl_title="" data-rl_caption="" title=""><img src="https://cpbotha.net/wp-content/uploads/2016/01/swift-sort-binaries-300x82.png" alt="swift-sort-binaries.png" /></a>
  </p></p>
</div>

The Swift language is open source, is already available for Linux, has a number of really compelling modern language features of which closure expressions are just one example (other interesting examples include optional types and protocol extensions), is statically typed with good type inference, and has a good compiler. For these reasons, it should be strongly considered for a permanent spot in your compiled language toolbox! 

P.S. Yes, I do know that C++ has `lambda` and `auto`. I like them too!

 [1]: https://swift.org/
 [2]: https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-ID95
 [3]: http://swiftlang.ng.bluemix.net/#/repl/6ab18271be682adc2a39c45988978ee92826c41faf70ed4420664fce1cd42bc8
 [4]: http://swiftlang.ng.bluemix.net/#/repl/0dbcdef74dfef00da5c7f21878cb5ed42739796116a6fd232ab20f05d6040a81
 [5]: https://swift.org/download/#latest-development-snapshots