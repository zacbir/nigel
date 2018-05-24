## Nigel - a command line Pelican publishing tool

Nigel lets you easily create static blog posts for Pelican.

Example usage:

```
$ echo $NIGEL_DIRECTORY

$ nigel --title "A new post" -t blog -t beginning
Title: A new post
Date: 2018-05-24 16:55
Slug: a-new-post
Tags: blog, beginning


$ nigel --title "A new post" -t blog -t beginning | vim -
[ begin a vim session with the base content ]
```
