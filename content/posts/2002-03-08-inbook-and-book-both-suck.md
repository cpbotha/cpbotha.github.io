---
title: InBook and Book both suck.
author: cpbotha
type: post
date: 2002-03-08T17:18:00+00:00
url: /2002/03/08/inbook-and-book-both-suck/
categories:
  - Uncategorized

---
I just updated the script that generates our [publications listings][1] so that it doesn’t list the cross references separately anymore. It creates full citations for each and every publication instead. In this change, I ran into the old problem of @InBook and @Book not allowing author and editor, which is strange… think about when you’ve written a chapter in a book for instance. In anycase, my advice is to ditch these and use @Proceedings and @InProceedings instead. Doh.

 [1]: http://visualisation.tudelft.nl/publications.html
