---
title: /dev
layout: home
permalink: /dev
---

# Development and related

<section>
<h1>{{ page.title }}</h1>
<ul>
{% for post in site.rambling %}
  {% if post.categories contains 'dev' %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>
</section>
