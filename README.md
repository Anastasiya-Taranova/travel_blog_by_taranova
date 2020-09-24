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
 <img src="https://travel-taranova.s3.us-east-1.amazonaws.com/login.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCmV1LW5vcnRoLTEiRzBFAiEAj81U4OXKmwvv8s9Hp5zY4W0jaZs6lgsC%2Fgw8pKHBEGYCIGskilayXqZJySy52rNh8YgdGzpZIAQARgGhBy3D6EpMKs0CCLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMDgwNTE1NTY3OTk2IgzopUOjYDmVXZ%2Bjg18qoQLWgjzfAlHgaQsc%2BjdBc6iMpa0dEFsTkfwy4PjLvAq6MCBDHurKxstGFHC8R7HjcjQKTZ8vgf4duGT0VG%2BASn5J%2FL6oia3qNKHPxwdl1kba%2B2pkvszouHDtcpYzv9Kg4NzwPkaPJ9IK4TmtqxQcv1dlg4mxrJMTCJMzL7a0KAnUjj1dMehyxHUo9NiilfxsKtK81k6jq%2B1qqs9rWJoMEcyiHEtTwWH2XM%2Be0OpBjpsgyVnJmNYlzHtyYNqVencyLQEJpPd8VcJYdLPEdjUqJBujqyt0mS%2FmFcsFXdsfp8XiHycnQzk4Xhd4BpvjejExR%2FOU9RIZfGmiC9JRko7DofJJuPCdH%2BsaHO%2FiZDpFDwzPIlkS0OC97pSi%2Bn4o5RodIAtcMKL%2BsfsFOrACkp9mMIebN6405rzueuoIkypP2%2BAcNdIQZdPljTpBY%2BIcV1YTBD79t%2Fme8grA5bEYAiPbSnnm9kkzYV5kGJmDWmFSH4jljCjjNqMetVXqKHrQx%2Bj8e82lK1cMx3uVFCD06BLkyIkuOSm4czS6hfDP4hHFz2lZwquSkcJIvqFFdrW3hVh5Nwy71PKYHrT9hqkBbhGG6lgOpJfYETNdOGsEgulAiF%2BtONQjfJDB9e5ZzlPrxfu8sQvzN0fJSx1ECaEvbSJe9zzGseSnSegI%2FTfd%2BXG2rviq9r9a%2FjAdkr%2Fg2EQA0ngr8KXFp7gO03x%2FTmdDHlQQxmIhFzHuk9OVzB2Eub8YsMzZMq%2FSESRb1MixtEikCM4%2BipHrzBOjWpvdenyjQbtX6ryZvDHNjpYXkAWXQA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200924T180303Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIARFPY2CF6ONINBQNS%2F20200924%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=455861b3403652fa5ae98afec5dd50ae22f4c28c7cc82596ab5371cf6ce44f38"/>
<li> Sign up with the help of Celery, Redis </li>
<li> Change password, user information </li>
 </ul><br>
2) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/account"> App – account: </a><br><br>
<ul> 
<li> The ability to plan(Create) your trip </li>
<li> Delete, Edit and Rewiew it </li>
 </ul><br>
3) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/api"> App – api: </a><br><br>
<ul><li> Provide your site api with the help of Swagger, Redoc </li>
 </ul><br>
4) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/preparation"> App – preparation: </a><br><br>
<ul>
<li> Connect to API aviasales.com </li>
<li> Find the minimum flight price for the specified parameters </li>
 </ul><br>
5) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/blog"> App – blog: </a><br><br>
<ul>
<li> Create, Review, Delete posts </li>
<li> Create, Review, Delete comments </li>
 </ul><br>
6) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/photos"> App – photos: </a><br><br>
<ul>
<li> Adding photos of new countries through the admin panel and adding an url to view subsequent ones through tags on instagram </li> </ul><br>
7) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/trips"> App – trips: </a><br><br>
<ul> <li> Dynamically adding new countries</li>
<li> Information display depending on the country: content and a map showing points with interesting places (coordinates are added to the map through the admin panel) with the help of 2Gis-Maps</li></ul><br>
8) <a href="https://github.com/Anastasiya-Taranova/travel_blog_by_taranova/tree/master/src/apps/index"> App – index: </a><br><br>
<ul> <li>Display of random photos(through context_processors), links to which can be added through the admin panel</li>
<li> Displaying random posts(through context_processors) that are added to the "Blog" section</li></ul><br>



