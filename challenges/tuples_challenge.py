imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, track = imelda
print(title)
print(artist)
print(year)
for song in track:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))