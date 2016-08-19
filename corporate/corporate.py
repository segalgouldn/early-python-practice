from twython import Twython

from random import *

import time

salutations1 = ["I RESPECT YOU", "WELL DONE", "KEEP IT UP",
                "YOU DESERVE A PROMOTION", "YOU\'VE BEEN SO PROACTIVE", 
                "GOOD WORK", "DON\'T GIVE UP", "YOU ARE ADMIRABLE", 
                "YOUR EFFORT IS NOT WASTED", "QUIT AND BE MY PARTNER",
                "YOU ARE CERTAINLY MOVING UP IN THE WORLD",
                "I\'M IN AWE OF YOU", "PLEASE KEEP WORKING HERE"]

salutations2 = ["COWORKER", "SUBORDINATE", "BOSS", "MANAGER",
                "FELLOW EMPLOYEE", "ASSISTANT", "REGIONAL MANAGER",
                "SENPAI", "SENSEI", "MASTER", "LORD", "KING",
                "HIGHNESS", "SIR", "MADAME", "SERVANT"]

adverbs      = ["SYNERGISTICALLY", "REASONABLY", "CAREFULLY",
                "RESPECTFULLY", "DIRECTLY", "ECONOMICALLY",
                "POLITICALLY", "TECHNOLOGICALLY", "PROACTIVELY",
                "ANALYTICALLY", "KNOWLEDGEABLY", "SEAMLESSLY",
                "EFFICIENTLY", "IMMEDIATELY", "ENTIRELY"]

adjectives   =  ["SYNERGISTIC", "REASONABLE", "CAREFUL", 
                "RESPECTFUL", "DIRECT", "ECONOMIC",
                "POLITICALLY CORRECT", "TECHNOLOGICAL",
                "PROACTIVE", "ANALYTICAL", "KNOWLEDGEABLE",
                "SEAMLESS", "BALLPARK", "BUSINESS-TO-BUSINESS",
                "CUSTOMER-CENTRIC", "INTEGRATED", "COMPETENT",
                "CREATIVE", "VISIBLE", "HANDY", "PASSIONATE",
                "UNDERRATED", "INTRIGUING", "FANTASTIC", 
                "FUNCTIONAL", "WISE", "CRITICAL", "IMPRESSIVE",
                "SATISFYING", "COMPLETE", "APT", "QUALITY", 
                "HOLISTIC", "GENUINE", "PROFITABLE"]

nouns        = ["SYNERGY", "CAREFULNESS", "RESPECTFULNESS",
                "DIRECTNESS", "ECONOMY", "POLITICAL CORRECTNESS",
                "TECHNOLOGY", "PROACTIVENESS", "ANALYSIS", 
                "KNOWLEDGE", "SEAMLESSNESS", "CUSTOMER-CENTRICITY",
                "INTEGRATION", "COMPETITIVENESS", "HANDINESS",
                "PASSION", "CREATIVITY", "COMPETENCE", "VISIBILITY",
                "BALLPARK FIGURE", "BANDWIDTH", "COMPANY", 
                "LOW HANGING FRUIT", "ENTITLEMENT", "OUTSOURCING",
                "COMPLIANCE", "ENTERPRISE"]

verbs        = ["RESPECTS", "PROMOTES", "LIKES", "LISTENS TO", 
                "COMPLIMENTS", "COMPLEMENTS", "SUPPORTS", "OUTSOURCES",
                "MIMICS", "PRACTICES", "OBSERVES", "WATCHES", 
                "APPROVES OF", "HOPES FOR THE CONTINUATION OF",
                "ENDORSES", "FINANCIALLY SUPPORTS", "PAYS FOR"]

def corporate(iterations):
    appKey = "INSERT_APP_KEY"
    
    appSecret = "INSERT_APP_SECRET"

    tokenKey =  "INSERT_TOKEN_KEY"

    tokenSecret = "INSERT_TOKEN_SECRET"

    twitter = Twython(appKey, appSecret, tokenKey, tokenSecret)

    for iteration in range(iterations):
        rnum = randint(1, 6)
        noun1 = choice(nouns)
        noun2 = choice(nouns)
        adjective = choice(adjectives)
        adverb1 = choice(adverbs)
        adverb2 = choice(adverbs)
        verb = choice(verbs)
        salutation2 = choice(salutations2)
        if rnum == 1 and len("I BELIEVE YOUR " + noun1 + " IS " + adjective + "!") <= 140:
            twitter.update_status(status = "I BELIEVE YOUR " + noun1 + " IS " + adjective + "!")
        elif rnum == 2 and len("AROUND HERE, YOU ARE THE " + noun1 + " THAT " + adverb1 + " KEEPS US RUNNING " + adverb2 + ".") <= 140:
            twitter.update_status(status = "AROUND HERE, YOU ARE THE " + noun1 + " THAT " + adverb1 + " KEEPS US RUNNING " + adverb2 + ".")
        elif rnum == 3 and len(noun1 + " " + verb + " YOUR " + adverb1 + " " + adjective + " " + noun2+ ".") <= 140:
            twitter.update_status(status = noun1 + " " + verb + " YOUR " + adverb1 + " " + adjective + " " + noun2 + ".")
        elif rnum == 4 and len("WOULD YOU BE ABLE TO PROVIDE SOME " + noun1 + " TO MY " + salutation2 + "?") <= 140:
            twitter.update_status(status = "WOULD YOU BE ABLE TO PROVIDE SOME " + noun1 + " TO MY " + salutation2 + "?")
        elif rnum == 5 and len("I JUST WANTED TO CONGRATULATE YOU ON " + adverb1 + " GAINING THE RANK OF " + salutation2 + "!") <= 140:
            twitter.update_status(status = "I JUST WANTED TO CONGRATULATE YOU ON " + adverb1 + " GAINING THE RANK OF " + salutation2 + "!")
        else:
            twitter.update_status(status = "CONTINUE YOUR " + noun1 + ", PLEASE.")
        time.sleep(300)

corporate(1000000)
