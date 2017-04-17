from pydub import AudioSegment

import pygame
from time import sleep

import wave, array, math, time, argparse, sys
import numpy, pywt
from scipy import signal
import pdb
from bpmDetection import read_wav, bpm_detector
import findLyrics

import os.path

# playlist = ["ASkyFullofStars"]
# playlist = ["ASkyFullofStars","BestDayOfMyLife", "BlankSpace"]
# playlist = ["ASkyFullofStars","BestDayOfMyLife", "BlankSpace", "FakePlasticTrees", "FightSong", "FixYou"]
# playlist = ["ASkyFullofStars","BestDayOfMyLife", "BlankSpace", "FakePlasticTrees", "FightSong", "FixYou", "Halo", "HeyJude", "Levels"]
playlist = ["OneDance","WorkFromHome", "Work", "ITookAPillInIbiza", "MeMyself&I", "ColdWater", "IHateUILoveU", "Youth", "7Years","PillowTalk"]
name = ["One Dance", "Work From Home", "Work", "I Took A Pill In Ibiza", "Me Myself & I", "Cold Water", "I Hate U I Love U", "Youth", "7 Years", "PillowTalk" ]
artist = ["Drake", "Fifth Harmony", "Rihanna", "Mike Posner", "G-Eazy", "Major Lazer", "Gnash", "Troye Sivan", "Lukas Graham", "Zayn"]

for p in playlist:
	sound = AudioSegment.from_mp3("/Users/tapan/acads/aic/project/cutsongs/"+p+".mp3")
	# if not os.path.isfile("/Users/tapan/acads/aic/project/cutsongs/"+p+".wav"):
	sound.export("/Users/tapan/acads/aic/project/cutsongs/"+p+".wav", format="wav")
	print "WAV Generated For ",p
	sleep(1)

print
print "Retrieving Lyrics"
print

for x in range(len(playlist)):
	song = findLyrics.Song(artist=artist[x], title=name[x])
	lyr = song.lyricwikia()
	if(lyr is not None):
		print "Song: ", name[x]
		print
		print(lyr)
		print

print
print "Slicing The Songs"
print 
sleep(10)

pygame.init()
pygame.mixer.init()

avgBPMArray = []
for p in playlist:
	#BPM CALCULATION
	filename = "/Users/tapan/acads/aic/project/cutsongs/"+p+".wav"
	samps,fs = read_wav(filename)

	data = []
	correl=[]
	bpm = 0
	n=0
	nsamps = len(samps)
	window_samps = int(3*fs)         
	samps_ndx = 0;
	max_window_ndx = nsamps / window_samps;
	bpms = numpy.zeros(max_window_ndx)

	for window_ndx in xrange(0,max_window_ndx):
	    data = samps[samps_ndx:samps_ndx+window_samps]
	    if not ((len(data) % window_samps) == 0):
	        raise AssertionError( str(len(data) ) ) 
	    bpm, correl_temp = bpm_detector(data,fs)
	    if bpm == None:
	        continue
	    bpms[window_ndx] = bpm
	    correl = correl_temp
	    samps_ndx = samps_ndx+window_samps;
	    n=n+1;

	bpm = numpy.median(bpms)
	print 'Estimated Beats Per Minute for song '+ p +':', bpm
	sleep(1)
	avgBPMArray.append((bpm,p))

avgBPMArray = sorted(avgBPMArray, key = lambda x:x[0])
# startTime = time.time()
sleep(5)

for p in avgBPMArray:
	print p[1]
	pygame.mixer.music.load("/Users/tapan/acads/aic/project/cutsongs/"+p[1]+".wav")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		sleep(1)
	# sleep(5)
	pygame.mixer.music.stop()

# endTime = time.time()
# timeElapsed = endTime - startTime
# print timeElapsed
# print 5*len(avgBPMArray)
# print (timeElapsed - 5*len(avgBPMArray))*1000