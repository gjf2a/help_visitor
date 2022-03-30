# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Robot")


# The game starts here.

label start:

    scene bg landsnow
    
    play music "audio/scene1.mp3"

    with Dissolve(0.5)
    pause 0.5

    show robot smallcrop:
        xalign 0.25
        yalign 0.75

    # These display lines of dialogue.

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

    r "I need to put a cool picture here."
    
    return
    
label alien_landing:

    with Dissolve(0.5)
    pause 0.25
    
    scene bg spaceship_crop
 
    r "Look out, here they come!"
    
    return
