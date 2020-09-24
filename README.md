[![Build Status](https://travis-ci.org/Anastasiya-Taranova/travel_blog_by_taranova.svg?branch=master)](https://travis-ci.org/Anastasiya-Taranova/travel_blog_by_taranova)
[![codecov](https://codecov.io/gh/Anastasiya-Taranova/travel_blog_by_taranova/branch/master/graph/badge.svg)](https://codecov.io/gh/Anastasiya-Taranova/travel_blog_by_taranova)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Travel blog by Taranova
Travel blog made with Python(Django).
You can see it on https://taranova-travel.herokuapp.com
<h2><a id="user-content-built-with" class="anchor" aria-hidden="true" href="#built-with"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Built With:</h2>
<ul>
<li> Django framework</li>
<li> PostgreSQL</li>
<li> AWS S3 </li>
<li> Celery</li>
 <li> Redis</li>
 <li> Dynaconf</li>
  <li> Rest API</li>
 <li> Swagger</li>
 <li> Redoc</li>
  <li> 2Gis-Maps</li>

</ul>
<h2><a id="user-content-built-with" class="anchor" aria-hidden="true" href="#built-with"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>A quick tour of the functionality in my app:</h2>
1) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/onboarding"> App – onboarding: </a> <br><br>
<ul> 
<li> Sign in </li>
<li> Sign up with help of Celery, Redis </li>
<li> Change password, user information </li>
 </ul>
2) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/account"> App – account: </a><br><br>
<ul> 
<li> The ability to plan(Create) your trip </li>
<li> Delete, Edit and Rewiew it </li>
 </ul>
3) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/api"> App – api: </a><br><br>
<ul><li> Provide your site api with the help of Swagger, Redoc </li>
 </ul>
4) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/preparation"> App – preparation: </a><br><br>
<ul>
<li> Connect to API aviasales.com </li>
<li> Find the minimum flight price for the specified parameters </li>
 </ul>
5) App – blog:<br>
– Create, Review, Delete posts <br>
– Create, Review, Delete comments <br><br>
6) App – photos:<br>
– Adding photos of new countries through the admin panel and adding an url to view subsequent ones through tags on instagram<br><br>
7) App – trips:<br>
– Dynamically adding new countries<br>
– Information display depending on the country: content and a map showing points with interesting places (coordinates are added to the map through the admin panel) with the help of 2Gis-Maps<br><br>
8) App – index:<br>
– Display of random photos(through context_processors), links to which can be added through the admin panel<br>
– Displaying random posts(through context_processors) that are added to the "Blog" section<br>



