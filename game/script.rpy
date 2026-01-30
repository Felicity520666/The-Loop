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
    stop music fadeout 2.5
    play music "kids-happy-469474.mp3" fadein 1.5
    scene check
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
    h "HARD-TO-GET LIMITED-EDITION GAMING HEADSET!!!"
    scene wifi
    with fade
    pause 1.5
    h "Let me just connect it real quick..."
    pause 2.5
    play sound "ding-402325.mp3" volume 6.5
    h "Ok! Connected!"
    h "And let me put on my gaming helmet..."
    pause 1.5
    scene getin
    with hpunch
    play music "sucking-in-48042.mp3"
    h "Wait--what's hapening?! Nooo! Ahhhhh--I'm being pulled in!"
    h "HELP!!!"
    stop music fadeout 1.0
    scene entre with pixellate
    play music "game-electronic-music-421999.mp3" fadein 1.0
    h "What...? Where am I?"
    h "Why so I look so freaking blocky and angular."
    show unkown at smallright
    with dissolve
    u "Hello there, little human."
    h "Who... who are you?"
    u "I choose not to tell you..."
    u "But, anyway. Welcome to this tes... no, I mean, ahem--"
    play sound "8-bit-video-game-win-level-sound-version-1-145827.mp3"
    u "WELCOME TO THE GAME!"
    h "Game...? What game?"
    h "This feels too random..."
    h "Oh wait---I understand now!"
    u "You... you do...?"
    h "Yes! I'm not that stupid!"
    h "So the game, the helmet... It's actually meant to be played in person, right?"
    h "Looks like I seriously underestimated what limited-edition games are capable of..."
    u "Exactly! You're just too clever! {i}(phew...){/i}"
    u "But anyway, here's the gameplay."
    u "Your goal is to dodge all the blocks before the hourglass at the top left corner runs out."
    u "Good luck."
    play music "retro-game-music-245230.mp3" fadein 2.0
    scene dodge
    with pixellate
    pause 5.5
    stop music fadeout 2.0
    scene later
    with pixellate
    play sound "later.mp3"
    pause 4.5
    scene 1
    with fade
    show haca game at smallleft
    with dissolve
    h "{i}Phew{/i}, just in time! Great jo..."
    play music "desert-danger-34602.mp3" fadein 1.5
    scene 2 
    with Fade(3.0, 0.0, 3.0)
    pause 3.5
    scene 3
    with Fade(3.0, 0.0, 3.0)
    pause 4.5
    scene entre
    with pixellate
    play music "game-electronic-music-421999.mp3" fadein 1.0
    pause 1.0
    h "What?! Why am I here again!"
    show unkown at smallright
    with dissolve
    u "Ha, sorry, dude."
    u "The hourglass has been reset, so you have to start over again."
    u "This also means you can't exit the game right now, so..."
    h "What?! So it's a loop?"
    h "{i}Sign{/i}... At least this is a fun game, good thing it's not boring. Fine. I'll play it again."
    play music "retro-game-music-245230.mp3" fadein 2.0
    scene dodge
    with pixellate
    pause 5.5
    stop music fadeout 2.0
    scene later
    with pixellate
    play sound "later.mp3"
    pause 4.5
    scene 1
    with fade
    show haca game at smallleft
    with dissolve
    h "Yeah! I did..."
    play music "desert-danger-34602.mp3" fadein 1.5
    scene 2 
    with Fade(3.0, 0.0, 3.0)
    pause 3.5
    scene 3
    with Fade(3.0, 0.0, 3.0)
    pause 4.5
    scene entre
    with pixellate
    play music "game-electronic-music-421999.mp3" fadein 1.0
    pause 1.0
    h "What?! Not again..."
    h "Why am I back again?"
    h "Oh well, never mind... I actually kind of like this game..."
    h "I'll just run through it a few more times, I can treat it as exercise!"
    play music "retro-game-music-245230.mp3" fadein 2.0
    scene dodge
    with pixellate
    pause 5.5
    stop music fadeout 2.0
    scene hour
    with pixellate
    play sound "later.mp3"
    pause 4.5
    play music "desert-danger-34602.mp3" fadein 1.5
    scene 1
    with fade
    scene 2 
    with Fade(3.0, 0.0, 3.0)
    pause 3.5
    scene 3
    with Fade(3.0, 0.0, 3.0)
    pause 4.5
    scene entre
    with pixellate
    play music "game-electronic-music-421999.mp3" fadein 1.0
    pause 1.0
    h "No! This looks like an endless loop!"
    h "Does anything I do even matter! Umm... it's time to make a decision..."
    h "When I was pulled in, I happened to have my laptop with me."
    h "In that split second, I grabbed it too!"
    h "I could try hacking into the system and destroy it..."
    h "...or keep running, see how it goes?"
    menu:
        "Hack into the system.":
            jump hack
        "Keep playing the game.":
            jump play
    
label hack:
    show code
    with pixellate
    play music "typing.mp3"
    show confident at smallleft
    with dissolve
    h "Haha, I am a senior member of the amazing Hack Club!"
    h "My hacking skills are already solid!"
    h "All I need to do is hack into the game's system and stop the hourglass from ever resetting."
    h "Once the loop is broken, I could finally clear the game and escape!"
    h "Just wait..."
    stop music
    play sound "correct.mp3"
    pause 0.5
    h "Yeah! Got it!"
    scene broke
    with vpunch
    play sound "glitch.mp3"
    pause 2.5
    scene getin
    with vpunch
    play sound "quick-swing-sound-419581.mp3"
    pause 1.5
    play music "happy-473961.mp3" fadein 2.0
    scene room
    with fade
    show haca normal at smallleft
    with moveinright
    h "I... I'm out?"
    show haca happy at smallleft 
    with dissolve
    h "I think... I DID IT!"
    show haca normal at smallleft
    with dissolve
    h "Thank goodness I acted in time..."
    show haca happy at smallleft
    with dissolve
    h "Looks like programming really can save lives!"
    play music "yay.mp3"
    scene end
    with fade
    pause 2.5
    return

label play:
    play music "retro-game-music-245230.mp3" fadein 2.0
    scene dodge
    with pixellate
    pause 5.5
    scene tired
    with fade
    play sound "breathing-fast-247449.mp3" volume 10.0
    pause 5.5
    scene years
    with pixellate
    pause 2.5
    scene old
    with fade
    play music "alejandro-afro-dancehall-music-163897.mp3" fadein 1.5
    play sound "man.mp3" volume 5.0
    h "Oh... my poor back..."
    h "How many years have I been running in here already?!"
    h "Why can't I get out!!!"
    h "Looks like I'm going to be trapped in this endless loop forever..."
    stop music fadeout 1.0
    scene end  
    play sound "lose.mp3"
    pause 5.5
    return
 
    

    
    # This ends the game.

    return
