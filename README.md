# Music-Mashup
Music-Mashup is an application which helps playing a playlist allowing for smooth mid-song transitions while ensuring lyrical
and emotional relevance tailored to your personal preferences aka your own “in-house DJ”. 

In today's world, on one hand there are applications like Spotify, SoundCloud etc. which provide great playlists for every
mood and event but DO NOT allow smooth mid-song transitions and on the other hand there are applications like Pacemaker which
allow for cropping and editing of music files but require in depth domain knowledge and are not automated. Music Mashup covers all the limitations present in the existing systems and has the following core features:

* Smart Queueing: Grouping relevant songs based on tempo, genre tag and emotion analysis.

* Identifying Highlights: Selecting highlights of a song based on lyrical analysis and repetition to create audio slices.

* Transitions: Ensuring smooth transitions based on tempo.

* Flexibility: In case of multiple ordering options allows for refresh option which creates a unique mashup each time.

# Workflow
Music-Mashup takes the following steps to generate the mashup :

* Read audio file and convert to wav format
* Retrieve the lyrics for a song by web crawling
* Extract highlights of songs by lyrical analysis
* Calculate BPM for each frame of audio files and relatively order the audio slices using the avg. BPM to ensure smooth transitions
* Play the ordered audio slices using Pygame

# Project Architecture Overview
![Alt text](/img/Picture1.png?raw=true "Music-Mashup System Design")

# Author
Music-Mashup is developed by Tapan Bohra and Medha Shrivastava under the supervision of Professor Ling Liu of Georgia Institute
of Technology. For help, please contact tbohra3@gatech.edu


