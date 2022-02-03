---
layout: project_jp
title: "About"
description: "C-PROOF Mission"
header-img: "img/MikeSaanich19.jpg"
---

<style>

html,body
{
    overflow-x: hidden; 
}

</style>

<body>
The Canadian Pacific Robotic Ocean Observing Facility is a state of the art facility to observe ocean changes in the Northeast Pacific Ocean.

Ocean change, its potential for life, and its potential as a source of energy are still poorly understood largely because of a lack of data. We want to understand what drives ocean and climate variability, which will allow us to better predict the weather and climate changes across Canada. We want to be able to better predict fish stocks in a timely manner so that competing economic and ecological concerns are properly balanced. We want to help move remote coastal communities and the country as a whole towards carbon-free energy sources by exploiting ocean waves and wind.
</body>

<div class="containerjp">
<figure>
<img src="img/CPROOFSketch.jpg" alt="C-PROOF Schematic">
<figcaption style="text-align:left;padding: 6px;position:relative;left:500px;font-style: italic;font-size: 16px;">Fig1. Caption caption</figcaption>
</figure>
</div>


<body>
<h3> </h3>
C-PROOF will deploy autonomous gliders and floats to explore and monitor the ocean using revolutionary new sensors to track life, quantify turbulence, and measure ocean nutrients. We will also deploy mooring arrays with innovative instrumentation capable of measuring ocean winds and waves with unprecedented fidelity.

These data sources will be shared with a wide array of partners and user groups for the benefits of Canadians; the data will inform ecosystem managers, climate and weather forecasters, and electric utilities on the state of the ocean so that we can better plan for the future, and drive development of the technological solutions needed to enable those plans.

<h3>What We Do</h3>

words about what C-PROOF is actively accomplishing. 
<a href= '/platforms/'>Platforms</a>


<hr/>
<h2>Publications</h2> 
<h2>
    In The News
</h2>

{% for post in site.data.inthenews %}{% if post.visible == true %}   <!---jp added  --->
<div class="post-preview">
    <a href="{{ post.url | prepend: site.baseurl }}">
        <h4 class="post-title">            {{ post.title }}
        </h4>
        {% if post.subtitle %}
        <h5 class="post-subtitle">
            {{ post.subtitle }}
        </h5>
        {% endif %}
    </a>
    <p class="post-meta" style="margin-bottom:5px">{% if post.author %}Posted by {{ post.author }} on {% endif %}  {{ post.date | date: "%B %-d, %Y" }}</p>
	<div class="notepad-index-post-tags" style="">
		{% for tag in post.tags %}<a href="{{ site.baseurl }}/search/index.html#{{ tag | cgi_encode }}" title="Other posts from the {{ tag | capitalize }} tag">{{ tag | capitalize }}</a>{% unless forloop.last %}&nbsp;{% endunless %}{% endfor %}
	</div>
</div>
<hr>
{% endif %}
{% endfor %}


</body>
