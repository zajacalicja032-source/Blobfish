# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Emily = Character(_("Emily"), color="#dd71dc")
define Aria = Character(_("Aria"), color="#770808")
define Michael = Character(_("Michael"), color="#a06608")
define Goro = Character(_("Goro"), color= "#a6b705")
define MC = Character(_("???"), color= "#5e19ad")

default aria_trust = 0
default emily_trust = 0

default preferences.text_cps = 50

label start:
    scene penthouse
    show goro 

    Goro "You ungrateful child!"
    Goro "You are a disgrace to OUR family!"
    Goro "You didn't go to college like I told you. You still have no job and you're a parasite. You are a failure and a disappointment to me!"
    Goro "You don't deserve to live in this house"
    Goro "Get lost!"

    hide Goro

    scene black
    with dissolve


    MC "I have nowhere to go. I'm so sorry father. I should have done better. I should have gone to college. I should have made you and mom proud of me."
    MC "It's starting to rain. I should look for a place to hide."
    MC "I guess I will wander around."
label street:
    scene street
    MC "After hours of walking, I saw a girl."
    show aria at center
    with move
    Aria "You're outside when it's raining. Not very wise, but who am I to judge."
    MC "Hey! you're here too."
    Aria "You don't look like you belong here. Are you from the clouds?"
    scene black
    "The clouds - the highest social class."
    scene street
    show aria
    MC "Yes. Yes, I am and that's something I'm very proud of."
    Aria "If that's the matter, then I'd want to ask you something."
    python:
        MC = renpy.input ("May I have thou name please?")

    MC "They call me [MC]."
    Aria "I think sweety suits you better. That's what I'll call you."
    MC "And what is your name?"
    Aria "I'm Aria. If you don't wanna be sick, you should come with me."

    menu:
        "Follow Aria":
            show aria
            jump aria_house
        "Refuse her offer":
            jump rick_roll

    hide aria
    with dissolve
label rick_roll:
    scene pestulinek
    "plot hole or smth."
    "I wanted to rick roll you, but the link didn't work. So be kind and find the video on yt and rick roll yourself."
    jump end
label aria_house:
    scene aria_house
    show aria
    MC "That's where you live?"
    MC "I didn't know that those poor people live in this city."
    Aria "Thanks..."
    Aria "You know how to compliment"
    MC "Sorry, I didn't meant to sound rude."
    Aria "But you did."
    Aria "Anyway, you can stay here if you want. There's a room at the back of the hallway."
    scene black
    "A week later..."
    with dissolve
    

label help_from_brother:
    scene street
    show emily
    with move
    Emily "Your brother is a real jerk. Tell him that, when you see him. Can't believe he sent me here. 
    To be clear I only did it because of our friendship." 
    Emily "He sent me to give you some money, he couldn't give you more, 
    he's worried your father would find out."
    MC "Stop complaining and say the real reason why you came here. I know you wouldn't come if it was only about the money, 
    even considering the fact we're close friends."
    Emily "I wanted to see how pathetic and miserable you are right now. I wanted to have a good laugh."
    menu:
        "Just give me the money and go away!":
            show emily
            Emily "After all my effort to come here, that's how you treat me? Okey, I'll leave but don't ever talk to me again."
            hide emily 
            menu:
                "I just want to live with aria, live the poor man's life":
                    scene black
                    with dissolve
                    jump aria_end
                "I just want to get back home, to my family":
                    jump bad_end

        "Guess I really did miss you.":
            scene street
            show emily
            MC "All you care about is yourself and your privileged life. You don't care about people who weren't born in filthy rich families."
            Emily "Don't act like you do. At least you didn't when you lived in a penthouse and could buy an entire mall. Have you really changed that much?"
            Emily "But I was thinking about a new business idea to make people love me even more. Perfect multibillionaire daughter. I could 'Help' pesants whom live here and you could help me."
            MC "Why should I help you?"     
            Emily "I'll help you if you help me, fair deal."
            MC "I'll think about it."
            hide emily
            scene black
            with dissolve
label Unexpected_call:
    scene aria_house
    "ring... ring... ring..." 
    MC "Its Emi. I'll answer."
    Emily "I'll show you my plan, we'll meet in 15 minutes."
    MC "But I don't know where."
    Emily "Don't worry about that."
    scene black
    with dissolve
    scene street
    show emily_casual
    Emily "Hello, I'm sorry that we have to discuss such a serious matter in such terrible conditions."
    MC "Cut the act!"
    Emily "For you, I will."
    MC "See? If you want to, then you can be really cute."
    hide emily_casual
    show emily_love
    Emily "Thanks..<3"
    hide emily_love
    show emily_casual
    Emily "So... My idea is that we'll do some charity work, we could donate a lot of money and find some jobs for the poor." 
    Emily "People see you doing crap like and you'll regain your honor and your father will take you back under his roof. 
    And maybe we'll help someone for real"
    Emily "I'll give you time to think trough. Call you later! <3"
    scene black 
    with dissolve
    MC "After that, we talked about this so called 'business' she gave me a month to decide whether i want to help her or not. Also,
    I realized that she's much more empathic than I thought. 
    I always knew that she acts this way only to fit in."
label Conversacion1:
    scene aria_house
    show aria
    Aria "How did the meeting go?"
    menu:
        "Teribble":
            Aria "What a pity, sweety. She's your friend after all, real friends are one of the most important things in your life, 
    
            they the ones who rescue you in tough situations, the ones that got your back when everything is falling apart. Don't lose her." 
        "Great":
            Aria "That's really pleasant to hear. She's not evil after all. It's good to have that kind of friends in city like that.
            I trust her already. She could have not give a damn about you at all, yet she came to you and became a link between you and
            your brother."
            MC "She could've helped me for free."
            Aria "Don't be greedy, sweety, she's done more than most people from your previous life."
            Aria "Still..."
label conversacion2:
    scene aria_house
    show aria
    Aria "I think that her idea is ridiculous.."      
    Aria "It sounds like she wants to change the world or something. She doesn't know real life." 
    Aria "I won't force you to refuse her. You should do what you think is the best, 
    but with that attitude you won't give any real help to these people" 
    MC "I know. And I don't know what to do about it. She gave me some time to think about it."
    scene black
    hide aria
label Brother:
    scene street
    show michael
    Michael "Haven't seen you in a while, I really missed you. It's really good to see my older sibling again."
    Michael "Mom threatend dad with divorce, she force him to go to rehab. He also had to end with his gambling addiction. 
    Now he wants to be the perfect man that he had been claiming to the world he was. He wants you to come back."
    menu:
        "There's no f*cking way!":
            show michael
            scene street
            Michael "I'll tell him that you declined his generous offer, but you're welcome in the house, whenever you want to return. 
            That choice doesn't supprise me at all. Goodbye."
            scene black
            with dissolve
            jump date

        "He's my father after all.":
            show michael
            scene street
            Michael "Wow. I'm really supprised. It'll be good to see you around"
            scene black
            with dissolve
            jump bad_end
label date:
    scene black
    "Time passed by..."
    MC "I want to finally do something fun and go out."
    MC "Maybe I should go on a date? But who should I choose?"
    MC "I recently can't stop thinking of..."
    menu:
        "Aria":
            $ aria_trust += 1
            jump date_aria
        "Emily":
            $ emily_trust += 1
            jump date_emily
        "Actually, I don't think of anyone.":
            scene black
            "Time passes by..."
            jump plan
label date_aria:
    scene restaurant
    show aria_date
    MC "You came."
    Aria "You live with me, you know I don't have anything better to do and you said that you'd pay, so of course I came."
    hide aria_date
    show aria_date_blush
    Aria "You look adorable in that outfit. Guess you really put in some effort, sweety. Local dinner, 
    that's how you spend money from your brother? Really, really, nice"
    MC "I've been a parasite my whole life, that's how I always spent my money. I spend them on pleasures."
    hide aria_date_blush
    show aria_date
    Aria "So I'm just a pleasure to you???"
    MC "OF COURSE NOT!!! I just wanted to share those nice moments with you..."
    Aria "Relax. I'm just playing with you. You've turned down your father's offer. What now?"
    MC "I don't know. This is all messed up and should't have happend in a first place."
    Aria "I know sweety, but I'll try my best to help you."
    hide aria_date
    show aria_date_blush
    "She put her hand on the table and slowly moved it closer to your hand, you felt her fingertips on your palm,
    you coudn't hold back a little laughter."
    MC "It tickles."
    "You flipped your hand and began to interlace your fingers, later, for just a moment 
    you sat at this dinner, holding hands in complete silence." 
    scene black
    "You wanted this moment to last forever, but you knew it couldn't."
    jump plan

label date_emily:
    scene restaurant
    show emily_date
    MC "Don't you think that your outfit is a little too elegant for a place like this?"
    Emily "I heard that you asked me on a date, so I dressed as if I'm going to."
    MC "Fair point."
    Emily "So... once you almost lost me, you finally understood how important I am to you, and decided to date me?"
    MC "More or less, but you can say that."
    Emily "So... Pathetic! Exacly how I like it."
    hide emily_date
    show emily_date_blush
    MC "Anything else for you Madam???"
    Emily "Since you asked... May I plese get a big hug from my dearest friend?"
    MC "Of course, Madam."
    scene black
    with dissolve
    "You leave your chair and ask her for the same, when she gets up, you immediately close her in a tight hug. 
    This time it's more than just a friendly hug and you both know it." 
    "This touch transfers emotions that connot be said.
    Her touch is something that can't be described,
    You wish you could just frezee time and live this moment forever."


label plan:
    scene aria_house
    "ring... ring... ring..."
    Aria "Pick up the phone already!"
    MC "COMING!"
    Emily "I'm calling to remind you of your deadline. Which happend to be passing today. 
    So what do you think? Will you do it?"
    menu:
        "Yes. Whatever you tell me, I'll do it.":
            Emily "That's very pleasent to hear."
            jump true_end
        "Yes, but I have my requirements.":
            Emily "I'm all ears."
            MC "We'll listen to Ari and do as she says, she knows this city like nobady else."
            Emily "Agree."
            jump good_end

        "No, I'll just return to my father without all this crap.":
            Emily "Really? Guess maybe I don't know you at all. I wish you all best, but without me. Goodbye forever."
            jump bad_end

label true_end:
    scene emily_house
    show aria
    Aria "Maybe it's better that way. You have to understand that sometimes things don't go like we want them to.
    We are in really good position. We have a house, something to eat, and real friends."
    show michael
    Michael "What are talking about guys?"
    Aria "About the charity plan that doesn't work out."
    Michael "That's rough, buddy."
    hide michael
    show aria
    MC "Maybe you're right, but I'll always think about what it could be."
    Aria "Woulda, coulda, shoulda..."
    scene black
    with dissolve
    "Your charity plan didn't work out, but don't worry. Emily with her fathers' money bought a penthouse
    now four of you live together. Now you can enjoy your quiet and peaceful life. "
    jump end


label good_end:
    scene mc_house_day
    if aria_trust > emily_trust:
        scene mc_house_day
        show aria_date
        Aria "Good morning, sweety!"
        "She kissed you on your forehead."
        Aria "Your morning coffee waits on you on the counter. Media once again were in awe of you. You did amazing. I'm very proud of you."
    if emily_trust > aria_trust:
        scene mc_house_day
        show emily
        Emily "We have to leave in 10 minutes. Hurry up!"
        "She quicly kissed you and then began to look for her purse."
        Emily "We have over 20 business proposals. We're amazing. That's the best life I could ever imagined."
    if emily_trust == aria_trust:
        scene mc_house_day
        MC "Nothing's better than looking at reports from work, while drinking morning coffee. At least after work, I'll go to Aria's house..."
    scene black
    "You are loaded. You have found real friends and maybe even love. That's what most people would call a perfect life. And you agree with them."
    jump end
    scene black
    with dissolve
    "GOOD ENDING"
    "You're better than ever. You live in your own villa. Your brother is now less scared of father, so you two can normally meet up. 
    You just opened a new buissnes and with help of Emily, you earn money, because of your charity people know and respect you, 
    so you have a lot of clients and you're becoming rich again."
    "You're really happy with your life now."
    "Good job!"
    jump end

label aria_end:
    scene aria_house
    
    show aria_end
    Aria "You really just told her to get lost. I thought she was your childhood friend. That was kinda rude, you told me
    that she has always been this way."
    Aria "But who am I to judge. Remember. I'll always support you and your decisions."
    MC "Thank you. Thank you so so much."
    "You're hugging."
    jump end

label bad_end:
    scene penthouse
    show goro_rehub
    Goro "Guess who finaly showed up. Apologize."
    MC "I'm so sorry father. You're right, I'm a failure. I'll try my best at becoming a better child."
    Goro "Good. Now you may go to your room. Dinner at 8. Don't be late."
    MC "Father, your too kind to me, thank you for all your effort."
    scene black
    with dissolve
    "In the room.."
    MC "I HATE HIM. WHY I SHOULD BE THE ONE APOLOGIZING? WHY IS HE EVEN WORSE WHEN HE'S SOBER? I HATE HIM!!"
    "BAD ENDING"
    "You came back, when he said, he changed. You trusted him. That was a big mistake. 
    All this anventure, only to change nothing."
    "You wasted your chance to live a better life."
    "Some changes are needed."


label end:
    scene black
    "You finally understood how the city works and did your best to bouce back from the bottom, even though it was deep below your usual social level."
label napisy:
    scene black
    "Made with love and depression."
    with dissolve
    scene napisy
    "Made with love and depression"


    return
