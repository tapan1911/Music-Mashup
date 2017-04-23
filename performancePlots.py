###################################
### CODE FILE TO CREATE MASHUPS ###
###################################

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


playlist = ["OneDance","WorkFromHome", "Work", "ITookAPillInIbiza", "MeMyself&I", "ColdWater", "IHateUILoveU", "Youth", "7Years","PillowTalk"]
name = ["One Dance", "Work From Home", "Work", "I Took A Pill In Ibiza", "Me Myself & I", "Cold Water", "I Hate U I Love U", "Youth", "7 Years", "PillowTalk" ]
artist = ["Drake", "Fifth Harmony", "Rihanna", "Mike Posner", "G-Eazy", "Major Lazer", "Gnash", "Troye Sivan", "Lukas Graham", "Zayn"]

######### TIME TO CONVERT TO WAV #########
for i in [1,3,6,9]:
	startTime = time.time()
	for j in range(i):
		sound = AudioSegment.from_mp3("/Users/tapan/acads/aic/Music-Mashup/cutsongs/"+playlist[j]+".mp3")
		sound.export("/Users/tapan/acads/aic/Music-Mashup/cutsongs/"+playlist[j]+".wav", format="wav")
	totalTime = (time.time()-startTime)
	print totalTime, totalTime*1000 


print 
print 
######### TIME TO FIND LYRICS #########
for i in [1,3,6,9]:
	startTime = time.time()
	for j in range(i):
		song = findLyrics.Song(artist=artist[j], title=name[j])
		lyr = song.lyricwikia()
	totalTime = (time.time()-startTime)
	print totalTime, totalTime*1000


print 
print
######### TIME TO CALCULATE BPM #########
pygame.init()
pygame.mixer.init()

for i in [1,3,6,9]:
	avgBPMArray = []
	startTime = time.time()
	for j in range(i):
		print i,j
	#BPM CALCULATION
		filename = "/Users/tapan/acads/aic/Music-Mashup/cutsongs/"+playlist[j]+".wav"
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
		avgBPMArray.append((bpm,playlist[j]))

	totalTime = (time.time()-startTime)
	print totalTime, totalTime*1000
