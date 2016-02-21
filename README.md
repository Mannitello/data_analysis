# README

This project shows data reports with Django-Jinja2 and Weasyprint.

The data used were taken from https://chinookdatabase.codeplex.com/, a sample database. The purpouse of this app is only to show basic reporting. 

Overview
========

The app generates a report with the following information:

  - Table of the top 20 artist that the music shop has sold 
  - Table of the top Rock Tracks sold from the music shop
  - Pie chart with available music divided by Genre

Dependencies
==========
   - python
   - django
   - numpy
   - matplotlib
   - jinja
   - weasyprint
   - pandas


Compiling instruction
=========

  - Download the project from github 
  - cd into the base directory of the project (data_analysis)
  - run python report.py
  - a report will be generated into: data_analysis/data_analysis/analysis/reports/report.pdf

