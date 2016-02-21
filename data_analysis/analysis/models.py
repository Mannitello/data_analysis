# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    albumid = models.IntegerField(primary_key=True, db_column='AlbumId', unique=True) # Field name made lowercase.
    title = models.TextField(db_column='Title') # Field name made lowercase. This field type is a guess.
    artist = models.ForeignKey('analysis.Artist',db_column='ArtistId') # Field name made lowercase.
    class Meta:
        db_table = 'Album'

class Artist(models.Model):
    artistid = models.IntegerField(primary_key=True, db_column='ArtistId', unique=True) # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'Artist'

class Customer(models.Model):
    customerid = models.IntegerField(primary_key=True, db_column='CustomerId', unique=True) # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName') # Field name made lowercase. This field type is a guess.
    lastname = models.TextField(db_column='LastName') # Field name made lowercase. This field type is a guess.
    company = models.TextField(db_column='Company', blank=True) # Field name made lowercase. This field type is a guess.
    address = models.TextField(db_column='Address', blank=True) # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True) # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True) # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True) # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email') # Field name made lowercase. This field type is a guess.
    supportrepid = models.IntegerField(db_column='SupportRepId', blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'Customer'

class Employee(models.Model):
    employeeid = models.IntegerField(primary_key=True, db_column='EmployeeId', unique=True) # Field name made lowercase.
    lastname = models.TextField(db_column='LastName') # Field name made lowercase. This field type is a guess.
    firstname = models.TextField(db_column='FirstName') # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True) # Field name made lowercase. This field type is a guess.
    reportsto = models.IntegerField(db_column='ReportsTo', blank=True, null=True) # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True) # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True) # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True) # Field name made lowercase. This field type is a guess.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase. This field type is a guess.
    state = models.TextField(db_column='State', blank=True) # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase. This field type is a guess.
    postalcode = models.TextField(db_column='PostalCode', blank=True) # Field name made lowercase. This field type is a guess.
    phone = models.TextField(db_column='Phone', blank=True) # Field name made lowercase. This field type is a guess.
    fax = models.TextField(db_column='Fax', blank=True) # Field name made lowercase. This field type is a guess.
    email = models.TextField(db_column='Email', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'Employee'

class Genre(models.Model):
    genreid = models.IntegerField(primary_key=True, db_column='GenreId', unique=True) # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'Genre'

class Invoice(models.Model):
    invoiceid = models.IntegerField(primary_key=True, db_column='InvoiceId', unique=True) # Field name made lowercase.
    customerid = models.ForeignKey('analysis.Customer', db_column='Customer')
    invoicedate = models.DateTimeField(db_column='InvoiceDate') # Field name made lowercase.
    billingaddress = models.TextField(db_column='BillingAddress', blank=True) # Field name made lowercase. This field type is a guess.
    billingcity = models.TextField(db_column='BillingCity', blank=True) # Field name made lowercase. This field type is a guess.
    billingstate = models.TextField(db_column='BillingState', blank=True) # Field name made lowercase. This field type is a guess.
    billingcountry = models.TextField(db_column='BillingCountry', blank=True) # Field name made lowercase. This field type is a guess.
    billingpostalcode = models.TextField(db_column='BillingPostalCode', blank=True) # Field name made lowercase. This field type is a guess.
    total = models.TextField(db_column='Total') # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'Invoice'

class Invoiceline(models.Model):
    invoicelineid = models.IntegerField(primary_key=True, db_column='InvoiceLineId', unique=True) # Field name made lowercase.
    invoiceid = models.ForeignKey('analysis.Invoice', db_column='Invoice') # Field name made lowercase.
    trackid = models.ForeignKey('analysis.Track', db_column='TrackId') # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice') # Field name made lowercase. This field type is a guess.
    quantity = models.IntegerField(db_column='Quantity') # Field name made lowercase.
    class Meta:
        db_table = 'InvoiceLine'

class Mediatype(models.Model):
    mediatypeid = models.IntegerField(primary_key=True, db_column='MediaTypeId', unique=True) # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'MediaType'

class Playlist(models.Model):
    playlistid = models.IntegerField(primary_key=True, db_column='PlaylistId', unique=True) # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'Playlist'

class Playlisttrack(models.Model):
    playlistid = models.IntegerField(primary_key=True, db_column='PlaylistId') # Field name made lowercase.
    trackid = models.ForeignKey('analysis.Track', db_column='Track') # Field name made lowercase.
    class Meta:
        db_table = 'PlaylistTrack'

class Track(models.Model):
    trackid = models.IntegerField(primary_key=True, db_column='TrackId', unique=True) # Field name made lowercase.
    name = models.TextField(db_column='Name') # Field name made lowercase. This field type is a guess.
    albumid = models.ForeignKey('analysis.Album',db_column='AlbumId', blank=True, null=True) # Field name made lowercase.
    mediatypeid = models.ForeignKey('analysis.Mediatype',db_column='MediaTypeId') # Field name made lowercase.
    genreid = models.ForeignKey('analysis.Genre',db_column='GenreId', blank=True, null=True) # Field name made lowercase.
    composer = models.TextField(db_column='Composer', blank=True) # Field name made lowercase. This field type is a guess.
    milliseconds = models.IntegerField(db_column='Milliseconds') # Field name made lowercase.
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True) # Field name made lowercase.
    unitprice = models.TextField(db_column='UnitPrice') # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'Track'

