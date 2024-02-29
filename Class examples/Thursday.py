Season = int(input("What's the season is in Boston at the moment? "))
if Season < 1 or Season > 12:
    print ("no")
elif Season >= 4 and Season <= 6:
    print ("it is spring in Boston")
elif Season >= 7 and Season <= 9:
    print ("it is summer in Boston")
elif Season >= 10 and Season <= 11:
    print ("it is autumn in Boston")
elif Season >= 1 and Season <= 3:
    print ("it is winter in Boston")
elif Season == 12:
    print ("it is winter in Boston")