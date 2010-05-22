from __future__ import division
import numpy as np
import pylab as pl

n = 10
buildings = {'Supply depot': (18000, 1000)
             , 'Refinery' : (150000, 6500)
             , 'Weapons factory' : (540000, 16500)
             , 'Power plant': (2700000, 56000)
            }
origgot = {'Supply depot': 0
           , 'Refinery' : 0
           , 'Weapons factory': 0
           , 'Power plant': 0
          }

# buildings = {'Bunker': (30000, 3)
#              , 'Guard tower': (20000, 10)
#              , 'Anti-aircraft': (560000, 15)
#             }
# origgot = {'Bunker': 0
#            , 'Guard tower': 0
#            , 'Anti-aircraft': 0
#           }



def price(info, n):
    """ Calculate price / unit income """
    return info[0]*(1+n*0.1) / info[1]

def income(got, buildings):
    inc = 0
    for name in got:
       inc += got[name] * buildings[name][1] 
    return inc

build = []
got = {}
for name in buildings:
    got[name] = origgot[name]

for i in xrange(0, n):
    temp = None
    best = None
    for name in buildings:
        p = price(buildings[name], got[name])
        if (temp is None) or (temp > p):
            best = name
            temp = p
    got[best] += 1
    build.append(best)

print ">> Building plan for the next %d buildings <<" %(n)
print "%3s -> %-15s (%3s) [%5s] {%s}" %('Idx'
                                        , 'Name'
                                        , 'Tot'
                                        , 'CpG'
                                        , 'TGain'
                                       )
print "---------------------------------------------"
for name in buildings:
    got[name] = origgot[name]
for index, name in enumerate(build):
    got[name] += 1
    print "%3d -> %-15s (%3d) [%5.2f] {%d}" %(index+1
                                              , name
                                              , got[name]
                                              , price(buildings[name], got[name]-1)
                                              , income(got, buildings)
                                              )
