# coding: utf-8

import urllib

fields = [ "Photo/video identifier",
"User NSID",
"User nickname", 
"Date taken", 
"Date uploaded", 
"Capture device", 
"Title", 
"Description", 
"User tags (comma-separated)", 
"Machine tags (comma-separated)", 
"Longitude", 
"Latitude", 
"Accuracy", 
"Photo/video page URL", 
"Photo/video download URL", 
"License name", 
"License URL", 
"Photo/video server identifier", 
"Photo/video farm identifier", 
"Photo/video secret", 
"Photo/video secret original", 
"Photo/video extension original", 
"Photos/video marker (0 = photo, 1 = video)" ]

cities = set(["konya", "ankara", "urfa", "karaman", "adana", "istanbul", "antalya", "izmir", u"muğla"])

# cities listesi 71 il
# her set elemanı için o isimle 

cities2 = set()
for city in cities:
  city2 = urllib.quote(city.encode("utf-8"))
  if city2 != city: cities2.add(city2)

print cities2

# cities = set(["cambodia", "365"])

found = dict()
for city in cities:
  found[city] = []

def readfile(part):
   filename = "yfcc100m_dataset-%d" % part
   f = open(filename, "r")
   for i,line in enumerate(f):
      arr = line.split("\t")
      if (arr[22] == 1): continue    # if video bypass loop      
      # for j,v in enumerate(arr):
         # print "%d %s : %s" % (j,fields[j], v)    
      tags = set(arr[8].split(","))
      if (len(tags) > 1):
        if any(city in tags for city in cities):          
           print i,(tags & cities),arr[13] 
           for t in (tags & cities):
              found[t].append(arr[13]) 
        if any(city in tags for city in cities2):
           print i,(tags & cities2),arr[13]
           for t in (tags & cities2):
              found[urllib.unquote(t).decode("utf8")].append(arr[13])         
      # if i==50: break
   print "LAST", i
   f.close()
   
readfile(2)
found
