# Phonetic Songs
Repo of tools developed as part of the Phonetic Songs project for transcribing song lyrics in X-SAMPA

This project requires Python 3.5.x or greater. 

1. Get song lyrics
    * Get songs from Billboard Hot 100
    * Get songs and lyrics from:
      * MetroLyrics
      * Genius
      * AZLyrics
      * VocaDB (and related DBs)
      * Piapro
2. Rough conversion from words to ARPABET (w/ CMUDict) to X-SAMPA
3. Have humans correct the transcriptions https://discord.gg/wBAAub6
4. Use final transcriptions for fun projects, like statistical analysis or UTAU reclist generation
    * Train a model based on lyrics fetched and produce a sample output

To get started, run:
> git clone --recurse-submodules -j2 https://github.com/adlez27/phonetic-songs.git

> python3 main.py