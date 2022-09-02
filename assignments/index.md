---
layout: page
# don't make the name 'assignments' which would
# matcho
name: index-assignment
title: Assignments
---

{% assign this_page = page %}
{% for page in site.pages %}
{% assign prefix = page.name | slice: 0, 10 %}
{% if prefix == "assignment" and page.name != this_page.name %}
- [{{ page.title }}]({{page.url}})
{% endif %}
{% endfor %}
