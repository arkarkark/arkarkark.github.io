---
layout: post
title: Migrating to github pages
date: 2014-12-14
comments: false
---

# {{ page.title }}

I started getting used to writing
[github markdown](https://guides.github.com/features/mastering-markdown/)
and wanted to use it to write blog posts here. Mostly because quoting
code is just so pretty. [Github pages](https://pages.github.com/) to
the rescue. I don't need to host anything (security!) and it's git
based so I'm stoked about that. It uses
[Jekyll](http://jekyllrb.com/docs/quickstart/) to create all the
pages.

Welcome to my first blog post written in markdown! (using [github-markdown-server](https://github.com/arkarkark/github-markdown-server)!)

My old blog was on blogger, and I found this tool called import.rb
from [here](https://gist.github.com/ngauthier/1506614) that sucked
over all my posts from the blogger xml export format (from Settings -> Other -> Export blog). Nice.

Of course the xml format doesn't have everything you need:

   * no idea what url the post was published to
   * no indication of what labels a post has (this is called tags in Jekyll speak)

## Keeping Published Urls consistent

Jekyll defaults to year/month/day/post-title.html permalink format,
but of course that's no good for me, it wasn't how blogger did it. A
quick addition to _config.yaml fixed that:

```yaml
permalink: /:year/:month/:title.html
```

But not all posts were fixed with this.

Since the xml doesn't include the url that the blog post lives at on my server, old posts like this one [/2008/11/new-server.php](http://blog.wtwf.com/2008/11/new-server.php) were living at a path called /2008/11/a-new-server.html

Note how the old stuff used to end in .php and also I had published this post, then changed the title (added an 'a') and blogger kept the old url so I wouldn't break anyone linking to my blog.

Fixing this was non-trivial. Jekyll doesn't support mod-rewrite (as [danvk noted](http://www.danvk.org/2014/10/23/fully-migrated-to-github-pages.html)).

First get a list of all the pages on your blogger blog. I leveraged the little posts' archive blogger widget to get them all like this.

```shell
for yr in $(seq 2005 2014); do \
  for mo in $(seq -w 1 12); do  \
    sleep 1; \
    wget -q -O - "http://blog.wtwf.com/?action=getTitles&widgetId=BlogArchive1&widgetType=BlogArchive&responseType=js&path=http%3A%2F%2Fblog.wtwf.com%2F${yr}_${mo}_01_archive.html" \
    | egrep -o "http://blog.wtwf.com[^']*"; \
  done; done | tee all.txt
```

At first I was going to fix this by hand. To see how big the problem was I ran this in the _posts directory.
Things starting with a 2 were o.k. everything else was wrong.

```shell
(cat ../all.txt | fgrep -v _archive.html ; \ls -d * | \
perl -p -e 's!^(\d+)-(\d+)-\d+-(.*)$!http://blog.wtwf.com/$1/$2/$3!g') \
| sort | uniq -c | sort -r -n >../diffs.txt
```

Pretty much everything was wrong.

So I wrote a small python script [fix_posts.py](https://github.com/arkarkark/arkarkark.github.io/blob/master/bin/fix_posts.py) (I really should start doing these in Ruby I guess). It uses the all.txt I made above and adds a permalink section to the yaml at the top of each post.
I get the feeling I'll be using this to do other stuff to so I almost wrote it with some qwality.

After that, there were only a couple of posts that manually needed to be edited (because I changed the first few characters of a title).

## RSS

The rss in the standard set of pages is at a fixed url, I wanted my pages to point elsewhere (for feedburner)
so I added this line to my _config.yaml

```yaml
rss: "http://wtwf.com/scripts/atom.xml"
```

and updated this line in _includes/head.html

```html
  <link rel="alternate" type="application/atom+xml" title="{{ site.title }}" href="{% if site.rss %}{{ site.rss }}{% else %}{{"/feed.xml" | prepend: site.baseurl }}{% endif %}" >
```

and index.html

```html
  <p class="rss-subscribe">subscribe <a href="{% if site.rss %}{{ site.rss }}{% else %}{{"/feed.xml" | prepend: site.baseurl }}{% endif %}">via RSS</a></p>
```

## What's next...

**Next up** labels/tags.
[This post](http://www.minddust.com/post/tags-and-categories-on-github-pages/) is going to be helpful!
