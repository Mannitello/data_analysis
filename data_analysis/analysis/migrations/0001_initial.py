# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'Album', (
            ('albumid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'AlbumId')),
            ('title', self.gf('django.db.models.fields.TextField')(db_column=u'Title')),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Artist'], db_column=u'ArtistId')),
        ))
        db.send_create_signal(u'analysis', ['Album'])

        # Adding model 'Artist'
        db.create_table(u'Artist', (
            ('artistid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'ArtistId')),
            ('name', self.gf('django.db.models.fields.TextField')(db_column=u'Name', blank=True)),
        ))
        db.send_create_signal(u'analysis', ['Artist'])

        # Adding model 'Customer'
        db.create_table(u'Customer', (
            ('customerid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'CustomerId')),
            ('firstname', self.gf('django.db.models.fields.TextField')(db_column=u'FirstName')),
            ('lastname', self.gf('django.db.models.fields.TextField')(db_column=u'LastName')),
            ('company', self.gf('django.db.models.fields.TextField')(db_column=u'Company', blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(db_column=u'Address', blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(db_column=u'City', blank=True)),
            ('state', self.gf('django.db.models.fields.TextField')(db_column=u'State', blank=True)),
            ('country', self.gf('django.db.models.fields.TextField')(db_column=u'Country', blank=True)),
            ('postalcode', self.gf('django.db.models.fields.TextField')(db_column=u'PostalCode', blank=True)),
            ('phone', self.gf('django.db.models.fields.TextField')(db_column=u'Phone', blank=True)),
            ('fax', self.gf('django.db.models.fields.TextField')(db_column=u'Fax', blank=True)),
            ('email', self.gf('django.db.models.fields.TextField')(db_column=u'Email')),
            ('supportrepid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SupportRepId', blank=True)),
        ))
        db.send_create_signal(u'analysis', ['Customer'])

        # Adding model 'Employee'
        db.create_table(u'Employee', (
            ('employeeid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'EmployeeId')),
            ('lastname', self.gf('django.db.models.fields.TextField')(db_column=u'LastName')),
            ('firstname', self.gf('django.db.models.fields.TextField')(db_column=u'FirstName')),
            ('title', self.gf('django.db.models.fields.TextField')(db_column=u'Title', blank=True)),
            ('reportsto', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ReportsTo', blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'BirthDate', blank=True)),
            ('hiredate', self.gf('django.db.models.fields.DateTimeField')(null=True, db_column=u'HireDate', blank=True)),
            ('address', self.gf('django.db.models.fields.TextField')(db_column=u'Address', blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(db_column=u'City', blank=True)),
            ('state', self.gf('django.db.models.fields.TextField')(db_column=u'State', blank=True)),
            ('country', self.gf('django.db.models.fields.TextField')(db_column=u'Country', blank=True)),
            ('postalcode', self.gf('django.db.models.fields.TextField')(db_column=u'PostalCode', blank=True)),
            ('phone', self.gf('django.db.models.fields.TextField')(db_column=u'Phone', blank=True)),
            ('fax', self.gf('django.db.models.fields.TextField')(db_column=u'Fax', blank=True)),
            ('email', self.gf('django.db.models.fields.TextField')(db_column=u'Email', blank=True)),
        ))
        db.send_create_signal(u'analysis', ['Employee'])

        # Adding model 'Genre'
        db.create_table(u'Genre', (
            ('genreid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'GenreId')),
            ('name', self.gf('django.db.models.fields.TextField')(db_column=u'Name', blank=True)),
        ))
        db.send_create_signal(u'analysis', ['Genre'])

        # Adding model 'Invoice'
        db.create_table(u'Invoice', (
            ('invoiceid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'InvoiceId')),
            ('customerid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Customer'], db_column=u'Customer')),
            ('invoicedate', self.gf('django.db.models.fields.DateTimeField')(db_column=u'InvoiceDate')),
            ('billingaddress', self.gf('django.db.models.fields.TextField')(db_column=u'BillingAddress', blank=True)),
            ('billingcity', self.gf('django.db.models.fields.TextField')(db_column=u'BillingCity', blank=True)),
            ('billingstate', self.gf('django.db.models.fields.TextField')(db_column=u'BillingState', blank=True)),
            ('billingcountry', self.gf('django.db.models.fields.TextField')(db_column=u'BillingCountry', blank=True)),
            ('billingpostalcode', self.gf('django.db.models.fields.TextField')(db_column=u'BillingPostalCode', blank=True)),
            ('total', self.gf('django.db.models.fields.TextField')(db_column=u'Total')),
        ))
        db.send_create_signal(u'analysis', ['Invoice'])

        # Adding model 'Invoiceline'
        db.create_table(u'InvoiceLine', (
            ('invoicelineid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'InvoiceLineId')),
            ('invoiceid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Invoice'], db_column=u'Invoice')),
            ('trackid', self.gf('django.db.models.fields.IntegerField')(db_column=u'TrackId')),
            ('unitprice', self.gf('django.db.models.fields.TextField')(db_column=u'UnitPrice')),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(db_column=u'Quantity')),
        ))
        db.send_create_signal(u'analysis', ['Invoiceline'])

        # Adding model 'Mediatype'
        db.create_table(u'MediaType', (
            ('mediatypeid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'MediaTypeId')),
            ('name', self.gf('django.db.models.fields.TextField')(db_column=u'Name', blank=True)),
        ))
        db.send_create_signal(u'analysis', ['Mediatype'])

        # Adding model 'Playlist'
        db.create_table(u'Playlist', (
            ('playlistid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'PlaylistId')),
            ('name', self.gf('django.db.models.fields.TextField')(db_column=u'Name', blank=True)),
        ))
        db.send_create_signal(u'analysis', ['Playlist'])

        # Adding model 'Playlisttrack'
        db.create_table(u'PlaylistTrack', (
            ('playlistid', self.gf('django.db.models.fields.IntegerField')(primary_key=True, db_column=u'PlaylistId')),
            ('trackid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['analysis.Track'], db_column=u'Track')),
        ))
        db.send_create_signal(u'analysis', ['Playlisttrack'])

        # Adding model 'Track'
        db.create_table(u'Track', (
            ('trackid', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True, db_column=u'TrackId')),
            ('name', self.gf('django.db.models.fields.TextField')(db_column=u'Name')),
            ('albumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AlbumId', blank=True)),
            ('mediatypeid', self.gf('django.db.models.fields.IntegerField')(db_column=u'MediaTypeId')),
            ('genreid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'GenreId', blank=True)),
            ('composer', self.gf('django.db.models.fields.TextField')(db_column=u'Composer', blank=True)),
            ('milliseconds', self.gf('django.db.models.fields.IntegerField')(db_column=u'Milliseconds')),
            ('bytes', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Bytes', blank=True)),
            ('unitprice', self.gf('django.db.models.fields.TextField')(db_column=u'UnitPrice')),
        ))
        db.send_create_signal(u'analysis', ['Track'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'Album')

        # Deleting model 'Artist'
        db.delete_table(u'Artist')

        # Deleting model 'Customer'
        db.delete_table(u'Customer')

        # Deleting model 'Employee'
        db.delete_table(u'Employee')

        # Deleting model 'Genre'
        db.delete_table(u'Genre')

        # Deleting model 'Invoice'
        db.delete_table(u'Invoice')

        # Deleting model 'Invoiceline'
        db.delete_table(u'InvoiceLine')

        # Deleting model 'Mediatype'
        db.delete_table(u'MediaType')

        # Deleting model 'Playlist'
        db.delete_table(u'Playlist')

        # Deleting model 'Playlisttrack'
        db.delete_table(u'PlaylistTrack')

        # Deleting model 'Track'
        db.delete_table(u'Track')


    models = {
        u'analysis.album': {
            'Meta': {'object_name': 'Album', 'db_table': "u'Album'"},
            'albumid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'AlbumId'"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Artist']", 'db_column': "u'ArtistId'"}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "u'Title'"})
        },
        u'analysis.artist': {
            'Meta': {'object_name': 'Artist', 'db_table': "u'Artist'"},
            'artistid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'ArtistId'"}),
            'name': ('django.db.models.fields.TextField', [], {'db_column': "u'Name'", 'blank': 'True'})
        },
        u'analysis.customer': {
            'Meta': {'object_name': 'Customer', 'db_table': "u'Customer'"},
            'address': ('django.db.models.fields.TextField', [], {'db_column': "u'Address'", 'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'db_column': "u'City'", 'blank': 'True'}),
            'company': ('django.db.models.fields.TextField', [], {'db_column': "u'Company'", 'blank': 'True'}),
            'country': ('django.db.models.fields.TextField', [], {'db_column': "u'Country'", 'blank': 'True'}),
            'customerid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'CustomerId'"}),
            'email': ('django.db.models.fields.TextField', [], {'db_column': "u'Email'"}),
            'fax': ('django.db.models.fields.TextField', [], {'db_column': "u'Fax'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.TextField', [], {'db_column': "u'FirstName'"}),
            'lastname': ('django.db.models.fields.TextField', [], {'db_column': "u'LastName'"}),
            'phone': ('django.db.models.fields.TextField', [], {'db_column': "u'Phone'", 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.TextField', [], {'db_column': "u'PostalCode'", 'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'db_column': "u'State'", 'blank': 'True'}),
            'supportrepid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SupportRepId'", 'blank': 'True'})
        },
        u'analysis.employee': {
            'Meta': {'object_name': 'Employee', 'db_table': "u'Employee'"},
            'address': ('django.db.models.fields.TextField', [], {'db_column': "u'Address'", 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'BirthDate'", 'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'db_column': "u'City'", 'blank': 'True'}),
            'country': ('django.db.models.fields.TextField', [], {'db_column': "u'Country'", 'blank': 'True'}),
            'email': ('django.db.models.fields.TextField', [], {'db_column': "u'Email'", 'blank': 'True'}),
            'employeeid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'EmployeeId'"}),
            'fax': ('django.db.models.fields.TextField', [], {'db_column': "u'Fax'", 'blank': 'True'}),
            'firstname': ('django.db.models.fields.TextField', [], {'db_column': "u'FirstName'"}),
            'hiredate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_column': "u'HireDate'", 'blank': 'True'}),
            'lastname': ('django.db.models.fields.TextField', [], {'db_column': "u'LastName'"}),
            'phone': ('django.db.models.fields.TextField', [], {'db_column': "u'Phone'", 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.TextField', [], {'db_column': "u'PostalCode'", 'blank': 'True'}),
            'reportsto': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ReportsTo'", 'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'db_column': "u'State'", 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'db_column': "u'Title'", 'blank': 'True'})
        },
        u'analysis.genre': {
            'Meta': {'object_name': 'Genre', 'db_table': "u'Genre'"},
            'genreid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'GenreId'"}),
            'name': ('django.db.models.fields.TextField', [], {'db_column': "u'Name'", 'blank': 'True'})
        },
        u'analysis.invoice': {
            'Meta': {'object_name': 'Invoice', 'db_table': "u'Invoice'"},
            'billingaddress': ('django.db.models.fields.TextField', [], {'db_column': "u'BillingAddress'", 'blank': 'True'}),
            'billingcity': ('django.db.models.fields.TextField', [], {'db_column': "u'BillingCity'", 'blank': 'True'}),
            'billingcountry': ('django.db.models.fields.TextField', [], {'db_column': "u'BillingCountry'", 'blank': 'True'}),
            'billingpostalcode': ('django.db.models.fields.TextField', [], {'db_column': "u'BillingPostalCode'", 'blank': 'True'}),
            'billingstate': ('django.db.models.fields.TextField', [], {'db_column': "u'BillingState'", 'blank': 'True'}),
            'customerid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Customer']", 'db_column': "u'Customer'"}),
            'invoicedate': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'InvoiceDate'"}),
            'invoiceid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'InvoiceId'"}),
            'total': ('django.db.models.fields.TextField', [], {'db_column': "u'Total'"})
        },
        u'analysis.invoiceline': {
            'Meta': {'object_name': 'Invoiceline', 'db_table': "u'InvoiceLine'"},
            'invoiceid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Invoice']", 'db_column': "u'Invoice'"}),
            'invoicelineid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'InvoiceLineId'"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'db_column': "u'Quantity'"}),
            'trackid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'TrackId'"}),
            'unitprice': ('django.db.models.fields.TextField', [], {'db_column': "u'UnitPrice'"})
        },
        u'analysis.mediatype': {
            'Meta': {'object_name': 'Mediatype', 'db_table': "u'MediaType'"},
            'mediatypeid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'MediaTypeId'"}),
            'name': ('django.db.models.fields.TextField', [], {'db_column': "u'Name'", 'blank': 'True'})
        },
        u'analysis.playlist': {
            'Meta': {'object_name': 'Playlist', 'db_table': "u'Playlist'"},
            'name': ('django.db.models.fields.TextField', [], {'db_column': "u'Name'", 'blank': 'True'}),
            'playlistid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'PlaylistId'"})
        },
        u'analysis.playlisttrack': {
            'Meta': {'object_name': 'Playlisttrack', 'db_table': "u'PlaylistTrack'"},
            'playlistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "u'PlaylistId'"}),
            'trackid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['analysis.Track']", 'db_column': "u'Track'"})
        },
        u'analysis.track': {
            'Meta': {'object_name': 'Track', 'db_table': "u'Track'"},
            'albumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AlbumId'", 'blank': 'True'}),
            'bytes': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Bytes'", 'blank': 'True'}),
            'composer': ('django.db.models.fields.TextField', [], {'db_column': "u'Composer'", 'blank': 'True'}),
            'genreid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'GenreId'", 'blank': 'True'}),
            'mediatypeid': ('django.db.models.fields.IntegerField', [], {'db_column': "u'MediaTypeId'"}),
            'milliseconds': ('django.db.models.fields.IntegerField', [], {'db_column': "u'Milliseconds'"}),
            'name': ('django.db.models.fields.TextField', [], {'db_column': "u'Name'"}),
            'trackid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True', 'db_column': "u'TrackId'"}),
            'unitprice': ('django.db.models.fields.TextField', [], {'db_column': "u'UnitPrice'"})
        }
    }

    complete_apps = ['analysis']