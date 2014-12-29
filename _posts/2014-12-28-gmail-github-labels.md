---
layout: post
title: gmail-github-labels
date: 2014-12-28
comments: false
tags: [github, gmail, apps script, labels]
---

When I'm reading about an issue in gmail, it's hard to tell if that
issue is assigned to me or I just got mentioned in it. I'd also like
to know if an issue is Critical or Major and considered a Bug. Those
are all specific labels we have come up with at our company.

This script fetches all the issues that have been modified since
yesterday, and also all the email about github issues and adds/removes
labels on the gmail thread to match the labels and state of the issue.

Go get it at [https://github.com/arkarkark/gmail-github-labels](https://github.com/arkarkark/gmail-github-labels).

It was inspired by a passing thought in [this blog post](/2014/12/github-tweaks-and-cson-to-json-in.html).
