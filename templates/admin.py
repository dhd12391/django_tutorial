{% extends "admin/base.html" %}

{% block title %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">The Cave of Polls</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}
