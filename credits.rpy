# simple credits screen
# usage:
# >    window hide
# >    call credits #from _call_credits_2
# >    pause(999999.0)

label credits:
    $ credits_speed = 15 #scrolling speed 0 - superfast, 100 - slow

    scene black
    with dissolve

    show cred at Move((0.5, 3.2), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")

    with Pause(credits_speed)
    return

init python:
    #adding order is important!
    credits = [('Writing', 'Div'), ('Programming', 'Div')]
    credits += [('CG', 'Div')]

    #duplicates by key must be added exact that way
    credits += [('Music', 'Tango')]
    credits += [('Music', 'Foxtrot')]
    
    credits += [('QA', 'Jack')]
    credits += [('QA', 'Jim')]

    credits += [('Engine', renpy.version())]


    creditsText = "{size=80}Credits\n\n"

    lastKey = ''
    for item in credits:
        if not lastKey == item[0]:
            creditsText += "\n{size=40}" + unicode(item[0]) + "\n"
        creditsText += "{size=50}" + unicode(item[1]) + "\n"
        lastKey = item[0]

   
init:
    image cred = Text(creditsText, text_align=0.5)
