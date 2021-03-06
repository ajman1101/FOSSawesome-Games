#!/usr/bin/env python

import json

if __name__ == "__main__":
    ret = 0
    fgn = open('FOSSawesomeGames.json', 'r')
    lgn = open('licenses.json', 'r')

    fsjson = json.load(fgn)
    lsjson = json.load(lgn)

    osidb = lsjson['OSI']

    # Validate License
    for content in fsjson:
        cdata = fsjson[content]
        for game in cdata:
            validated = False
            license = game['license']

            for dblicense in osidb:
                if dblicense['title'] == license:
                    validated = True
                elif dblicense['alias'] == license:
                    validated = True

            if validated == True:
                print "OK: " + game['title']
            else:
                print "FAIL: " + game['title'] + ", INVALID LICENSE (" + license + ")"
                ret = 1

    fgn.close()
    exit(ret)
        
