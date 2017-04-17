from pydub import AudioSegment

import pygame
from time import sleep

import wave, array, math, time, argparse, sys
import numpy, pywt
from scipy import signal
import pdb
from bpmDetection import read_wav, bpm_detector

import os.path

playlist = ["ASkyFullofStars","BestDayOfMyLife", "BlankSpace", "FakePlasticTrees", "FightSong", "FixYou", "Halo", "HeyJude", "Levels"]
# playlist = ["BrothersAnthem","KingsNeverDie"]

for p in playlist:
	sound = AudioSegment.from_mp3("/Users/tapan/acads/aic/project/playlist/"+p+".mp3")
	if not os.path.isfile("/Users/tapan/acads/aic/project/playlist/"+p+".wav"):
		sound.export("/Users/tapan/acads/aic/project/playlist/"+p+".wav", format="wav")

pygame.init()
pygame.mixer.init()

for p in playlist:
	pygame.mixer.music.load("/Users/tapan/acads/aic/project/playlist/"+p+".wav")
	pygame.mixer.music.play()
	sleep(5)
	pygame.mixer.music.stop()

	#BPM CALCULATION
	filename = "/Users/tapan/acads/aic/project/playlist/"+p+".wav"
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