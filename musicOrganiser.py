import eyeD3
import os
import sys
import urllib2
import re
from optparse import OptionParser

readCmdline = OptionParser()
readCmdline.add_option("-f",dest='filePath',help="The path to the files to be organised")
readCmdline.add_option("--Artist",dest='ArtistBased',default='false',help="Sort and create directories based on artists")
readCmdline.add_option("--Album",dest='AlbumBased',default='false',help='Sort and create directories based on albums')
(options,args)=readCmdline.parse_args()
print options.ArtistBased

filePath ="/media/Music Maza/Western/"

songList = os.listdir(filePath)
metaDataList={}
artistList=[]
albumList=[]
#print songList
for song in songList:
	#print song
	try:
		music = eyeD3.Mp3AudioFile(filePath+song)	#load a song
	except eyeD3.tag.InvalidAudioFormatException:
		continue 
	except IOError:
		print "couldn't read the ",song
		print "Continuing"
		continue
	musicData = music.getTag()			#reuse the variable and get all tags
	if musicData:
		artistList.append(musicData.getArtist())
		albumList.append(musicData.getAlbum())
		metaDataList[music.fileName]=[musicData.getArtist().lower().strip(),musicData.getAlbum().lower().strip()]
	
# print "Hingide vishaya"
# print metaDataList
if artistList and albumList:
	artistList.sort()
	albumList.sort()
	artistList = [x.lower().strip() for x in artistList ]		#removed spaces and case imbalance from artistList
	albumList =[ x.lower().strip() for x in albumList]			#removed spaces and case imbalance from albumList
keys={}
#artistList = [key for key in artistList ]
for i in range(0,len(artistList)):
	if artistList[i]:
		keys[artistList[i]]=1
artistList=keys.keys()
keys={}
for i in range(0,len(albumList)):
	if albumList[i]:
		keys[albumList[i]]=1
albumList=keys.keys();
print "Artist count",len(artistList)
print "\n".join(artistList)
print "\n"
print "Album count",len(albumList)
print "\n".join(albumList)
url=re.compile('(http[ s]://)?[ ]www.*.[ ]*com')
#Now to remove urls

print artistList

for key in metaDataList.keys():
    if metaDataList[key][0]:
        print key
        name = key.replace(filePath,'')
        os.renames(key,filePath+metaDataList[key][0]+"/"+name)
