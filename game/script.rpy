# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Haca", color = "#00c217")
define u = Character("Unknown", color = "#000000")

transform smallright:
    zoom 0.2
    xalign 0.95
    yalign 1.0

transform smallleft:
    zoom 0.2
    xalign -0.05
    yalign 1.0

# The game starts here.

label start:
    play music "technology-beeping-192222.mp3" fadein 5.0
    scene earth with Fade(0.0, 0.0, 5.0)

    show unkown at smallright with pixellate

    u "Oh... Look what I found..."
    u "Detected a new life-bearing planet."
    u "Quite beautiful isn't it?"
    u "The most advanced life form is currently identified as this thing called humans..."
    u "Precise information has not yet been collected."
    u "It is necessary to dispatch one individual to gather intellidence..."
    u "Uh..."
    u "Because the captain thought there would be no intelligent beings here, only I was sent out..."
    u "So I guess I'll have to gather the information myself..."
    scene hack
    with fade
    u "Human target acquired. Initiating system entry."
    scene check
    play music "kids-happy-469474.mp3" fadein 1.5
    with Fade(0.0, 0.0, 3.0)
    pause 2.5
    show haca happy at smallleft 
    with moveinright
    h "Yayyy! I finally finished all my essential work!"
    h "Time to play games using my--"
    scene brain
    with vpunch
    play sound "goodresult-82807.mp3"
    pause 2.0
    h "HARD-TO-GET LIMITED-EDITION GAMING HEASET!!!"

    
    # This ends the game.

    return
