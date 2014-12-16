---
layout: post
title: Migrating to github pages
date: 2014-12-16
comments: false
tags: [github]
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

```bash
for yr in $(seq 2005 2014); do \
  for mo in $(seq -w 1 12); do  \
    sleep 1; \
    wget -q -O - "http://blog.wtwf.com/?action=getTitles&widgetId=BlogArchive1&widgetType=BlogArchive&responseType=js&path=http%3A%2F%2Fblog.wtwf.com%2F${yr}_${mo}_01_archive.html" \
    | egrep -o "http://blog.wtwf.com[^']*"; \
  done; done | tee all.txt
```

At first I was going to fix this by hand. To see how big the problem was I ran this in the _posts directory.
Things starting with a 2 were o.k. everything else was wrong.

```bash
(cat ../all.txt | fgrep -v _archive.html ; \ls -d * | \
perl -p -e 's!^(\d+)-(\d+)-\d+-(.*)$!http://blog.wtwf.com/$1/$2/$3!g') \
| sort | uniq -c | sort -r -n >../diffs.txt
```

Pretty much everything was wrong.

So I wrote a small python script [fix_posts.py](https://github.com/arkarkark/arkarkark.github.io/blob/master/bin/fix_posts.py) --permalinks (I really should start doing these in Ruby I guess). It uses the all.txt I made above and adds a permalink section to the yaml at the top of each post.
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

Because the guid in the feed for each post is different than the one blogger uses I only wanted the rss feed to include new posts. Otherwise feed readers (all 16 of you!) would see the last 10 posts duplicated in their feed reader, that annoys me when it happens to me.

Now liquid annoys me.... Here's the only way I could find to do it: in feed.xml I added this.

{% raw %}
```xml
    ...
    <generator>Jekyll v{{ jekyll.version }}</generator>
    {% for post in site.posts limit:10 %}
      {% capture threshold %}{{'2014-12-16' | date: '%s'}}{% endcapture %}
      {% capture post_date_unix %}{{post.date | date: '%s'}}{% endcapture %}
      {% if post_date_unix > threshold %}
        <item>
          <title>{{ post.title | xml_escape }}</title>
          ...
```
{% endraw %}

## Syntax highlighting

I like code fences with the language specified after the triple ticks. to get that to work I had to change the markdown config to `redcarpet`.

To get it working when I served files locally with jekyll I had to

```bash
sudo pip install Pygments
gem install redcarpet
gem install pygments.rb
```

## Refreshing automatically when running locally

Adding this into [_includes/head.html](https://github.com/arkarkark/arkarkark.github.io/blob/master/_includes/head.html) loads [live.js](http://livejs.com/) when you're running a local server. When you save, a few seconds later your page will refresh.

```html
  <script>
    if (window.location.port == 4000) {
      el = document.createElement('script');
      el.src = '/js/live.js';
      document.head.appendChild(el);
    }
  </script>
```

## Labels / Tags

I had labels on my blogger posts, but of course that info also isn't in the exported xml. It wasn't fetched by the page via xmlrpc either so I went to my blogger console and looked at the requests sent there. Oh look a request to `https://draft.blogger.com/blogger_rpc?blogID=10...44` sends back JSON (not JSONP) with useful information in it. I likely could have used this for my published urls consisten thing above, oh well, that ship sailed...

[fix_posts.py](https://github.com/arkarkark/arkarkark.github.io/blob/master/bin/fix_posts.py) --import_labels to the rescue, It loads the JSON that you saved from above and adds a tags section to each post.

I then followed the instructions from [This post](http://www.minddust.com/post/tags-and-categories-on-github-pages/) to make a /search/label/ directory filled with the data I wanted. fix_posts.py will make sure you have a label file for each label you have in your posts. Run it before you commit with a pre-commit hook?

## What's next...


   * <input type="checkbox"> archive files?
   * <input type="checkbox"> sidebar (maybe [lanyon](https://github.com/poole/lanyon)?)
      * <input type="checkbox"> favorite posts
      * <input type="checkbox"> email me
      * <input type="checkbox"> search this blog
      * <input type="checkbox"> labels
      * <input type="checkbox"> all posts?
      * <input type="checkbox"> subscribe via email
