#!/usr/bin/env python

fajl='domainowners2'

try:

   f=open(fajl,'r')
   sor=f.readline()
   while sor <> '':
      print sor
      sor=f.readline()
   f.close()
   print '-> fajl vege.'

except IOError, e:
   print 'Nincs ilyen fajl:', fajl
