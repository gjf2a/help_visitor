# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Robot")
define a = Character("Alien")


# The game starts here.

label start:

    scene bg landsnow
    
    play music "audio/scene1.mp3"

    with Dissolve(0.5)
    pause 0.5

    show robot smallcrop:
        xalign 0.25
        yalign 0.75
        
    $ escaped = False
    $ alien_visit = False

    r "Welcome to the snowy Hendrix campus. This may seem like a typical snowy day, but..."

    r "Unusual things have been happening. Very unusual things."
    
    r "Within the depths of the snowfall, a portal has opened to an enchanted world."
    
    r "It may be peaceful, or it may be dangerous. Nobody knows."
    
    r "Furthermore, an alien spacecraft has been sighted in the area."
    
    r "They may have come in peace, or not..."
    
    r "Which would you like to see?"
    
    menu:            
        "Alien landing site":
            jump alien_landing
            
        "Enchanted snow forest":
            r "Let us walk through the portal, and find out what we will see."
            
            jump snow_forest
    
label snow_forest:

    with Dissolve(0.5)
    pause 0.25
    
    play music "audio/Cantiga59.mp3"
    
    scene bg enchanted_landscape

    show robot smallcrop:
        xalign 0.0
        yalign 1.0
    
    if escaped:
        r "Wow, we escaped! I hope you enjoy the calm and peace of the enchanted forest, a welcome respite from our narrow escape."
    elif alien_visit:
        show alien alien:
            xalign 0.9
            yalign 1.0
            size (240, 240)
        
        a "This is a place of truly sublime beauty, well worth my interstellar voyage. Thank you!"
    else:
        r "This is a place of peace and truly sublime beauty. Enjoy your visit!"
    
    return
    
label alien_landing:

    with Dissolve(0.5)
    pause 0.25
    
    play music "audio/alien_scary_ship.mp3"
    
    scene bg spaceship_crop
    
    show robot smallcrop:
        xalign 0.0
        yalign 1.0
        size (80, 80)
 
    r "Behold, the alien spacecraft. They have landed!"
    
    r "I am not sure what they are going to do. They seem to be waiting for us to make the first move."
    
    r "What do you want to do?"
    
    menu: 
        "Escape to the portal to the enchanted forest.":
            $ escaped = True
            
            r "If we are quick, perhaps they will not react."
            
            r "Here is the portal. Let us enter before they follow us."
            
            jump snow_forest
            
        "Attack the aliens.":
            r "I hope you are well-armed, for their capabilities are unclear..."
        
            jump alien_attack
        
        "Talk to the aliens.":
            jump alien_talk
            
label alien_talk:
    scene bg alien_talk_2

    play music "audio/scene1.mp3"
    
    a "I am in search of the enchanted forest. Can you take me there?"
    
    menu:
        "Yes":
            $ alien_visit = True
            jump snow_forest
            
        "No":
            jump alien_no
            
label alien_attack:
    scene bg alien_attack_2

    a "We came in peace but you brought us war. Suffer the consequences."
    
    return
    
label alien_no:
    a "I'm sorry to have come all this way. Farewell..."
    
    r "The alien has departed. Let us be on our way."
    
    return
    
