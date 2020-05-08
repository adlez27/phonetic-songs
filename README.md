# Phonetic Songs
Repo of tools developed as part of the Phonetic Songs project for transcribing song lyrics in X-SAMPA

1. Get song lyrics
    * Get songs from Billboard Hot 100
    * Get songs and lyrics from:
      * MetroLyrics
      * Genius
      * AZLyrics
      * VocaDB (and related DBs)
2. Rough conversion from words to ARPABET (w/ CMUDict) to X-SAMPA
3. Have humans correct the transcriptions https://discord.gg/wBAAub6
4. Use final transcriptions for fun projects, like statistical analysis or UTAU reclist generation
    * Train a model based on lyrics fetched
      * This requires PyTorch 1.1. Download your flavour [here](https://pytorch.org/get-started/previous-versions/#v110).

To get started, run:
> python3 main.py