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

    r "Welcome to the snowy Hendrix campus. This is a typical snowy day."

    r "Where would you like to go?"
    
    menu:
        "Enchanted snow forest":
            jump snow_forest
            
        "Alien landing site":
            jump alien_landing
    
label snow_forest:

    with Dissolve(0.5)
    pause 0.25
    
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
        r "Enjoy the sublime beauty of the enchanted forest."
    
    return
    
label alien_landing:

    with Dissolve(0.5)
    pause 0.25
    
    scene bg spaceship_crop
    
    show robot smallcrop:
        xalign 0.0
        yalign 1.0
        size (80, 80)
 
    r "Look out, here they come!"
    
    r "What do you want to do?"
    
    menu: 
        "Escape to the enchanted forest.":
            $ escaped = True
            jump snow_forest
            
        "Attack the aliens.":
            jump alien_attack
        
        "Talk to the aliens.":
            jump alien_talk
            
label alien_talk:
    scene bg alien_talk_2

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
    
    return
    
