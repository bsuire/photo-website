photo-website
=============

Django based photography website

Author: Benjamin Suire
Date: July 12, 2014

Hello! This code is for a personal photography website which you can view here: http://bsuire.com/

Frontend: 
- bootstrap.js : responsive grids for displaying pictures, navigation bar that collapses on small screen,
- swipebox.js : lightbox feature that makes it possible to swipe through the pictures on touchscreen enabled devices.

Backend: Django.

Even though this is a front-end intensive project, I am using Django to facilitate content management. 

Currently I only use it for URL routing and especially its template engine. A single html template is used to generate all galleries, which is arguably much easier to maintain than N different gallery.html files, as their number increases.

However, in the future I plan to implement a number of different features that will require more backend programming: 
1. admin access and full automation of the process of adding pictures, server-side.
2. user registration and private galleries.
3. dynamic gallery generation using keywords. 

Feel free to contact me if you have any questions or comments.
