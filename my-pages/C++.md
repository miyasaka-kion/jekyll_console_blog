---
title: /C++
layout: home
permalink: /C++
---

# Modern C++, and some configuration specs;

<section>
<h1>{{ page.title }}</h1>
<ul>
{% for post in site.rambling %}
  {% if post.categories contains 'cpp' %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>
</section>