---
layout: page
name: assignments
title: Assignments
---

{% for page in site.pages %}
{% if page.kind == "assignment" %}
- [{{ page.title }}]({{page.url}})
{% endif %}
{% endfor %}
