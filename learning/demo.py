# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Imelda May", 2011, (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
#
# print(imelda)
#
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)


imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

# print("{}, {}, {}".format(imelda[0], imelda[1], imelda[2]))
# print("{}, {}, {}".format(imelda[3][0], imelda[3][1], imelda[3][2]))

title, artist, year, track = imelda
print(title)
print(artist)
print(year)
for song in track:
    print("\t", song)