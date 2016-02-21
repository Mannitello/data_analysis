"""
Generate PDF reports from data included in several Pandas DataFrames
From pbpython.com
"""
from __future__ import print_function
from django.conf import settings
import sqlite3
from data_analysis import settings
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def top_20_composer_for_track(conn):
    """
    Create a pivot table from a raw DataFrame and return it as a DataFrame
    """
    table_top_20_composer_for_track = pd.read_sql('select composer as Composer, count(trackid) as Number_Of_Track ' + 
        'from Track group by composer order by Number_Of_Track desc limit 20', conn)
    return table_top_20_composer_for_track

def information(conn):
    table_information = pd.read_sql('select a.name as Track_Name, a.composer as Composer,' + 
        'b.title as Album_title, c.name as genre_name from Track as a, Album as b, Genre as c ' + 
        'where a.albumid=b.albumid and a.genreid=c.genreid limit 10;', conn)
    return table_information

def charts(conn):
    sql_query = pd.read_sql('select b.name as Name, count(a.trackid) as nb_of_track from Track as a, ' + 
        ' Genre as b where a.genreid=b.genreid group by b.genreid;', conn)
    df = pd.DataFrame(sql_query.values, index=[item[0] for item in sql_query.values])
    plot=df.plot(kind='pie', subplots=True, figsize=(10, 10), legend=False)
    image_directory = os.getcwd() + "/data_analysis/analysis/static/analysis/images/genre_chart.png"
    plt.savefig(image_directory)
    return image_directory



if __name__ == "__main__":
    database_name=settings.DATABASES['default']['NAME']
    conn=sqlite3.connect(database_name)
    #report_directory = os.getcwd() + "/data_analysis/analysis/reports/report.pdf"
    genre_chart_directory = charts(conn) 
    report_directory = os.getcwd() + "/data_analysis/analysis/reports/report.pdf"
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("/data_analysis/analysis/templates/report.html")
    template_vars = {"title" : "Music Shop Report",
                     "top_20_composer" : top_20_composer_for_track(conn).to_html(index=False),
                     "information" : information(conn).to_html(index=False)}
    # Render our file and create the PDF using our css style file
    html_out = template.render(template_vars)
    HTML(string=html_out, base_url=settings.STATICFILES_DIRS[0]).write_pdf(report_directory)