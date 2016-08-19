from random import *

salutations1 = ["I RESPECT YOU", "WELL DONE", "KEEP IT UP",
                "YOU DESERVE A PROMOTION", "YOU\'VE BEEN SO PROACTIVE", 
                "GOOD WORK", "DON\'T GIVE UP", "YOU ARE ADMIRABLE", 
                "YOUR EFFORT IS NOT WASTED", "QUIT AND BE MY PARTNER",
                "YOU ARE CERTAINLY MOVING UP IN THE WORLD",
                "I'\'M IN AWE OF YOU", "PLEASE KEEP WORKING HERE"]

salutations2 = ["COWORKER", "SUBORDINATE", "BOSS", "MANAGER",
                "FELLOW EMPLOYEE", "ASSISTANT", "REGIONAL MANAGER",
                "SENPAI", "SENSEI", "MASTER", "LORD", "KING",
                "YOUR HIGHNESS", "SIR", "MADAME", "SERVANT"]

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

def letter(iterations):
    message = "\n" + choice(salutations1) + " " + choice(salutations2) + "," + "\n"
    for i in range(iterations):
        rnum = randint(1, 6)
        if rnum == 1:
            message += "I BELIEVE YOUR " + choice(nouns) + " IS " + choice(adjectives) + "! "
        elif rnum == 2:
            message += "AROUND HERE, YOU ARE THE " + choice(nouns) + " THAT " + choice(adverbs) + " KEEPS US RUNNING " + choice(adverbs) + ". "
        elif rnum == 3:
            message += "MY " + choice(nouns) + " " + choice(verbs) + " YOUR " + choice(adverbs) + " " + choice(adjectives) + " " + choice(nouns)+ ". "
        elif rnum == 4:
            message += "CONTINUE YOUR " + choice(nouns) + ", PLEASE. "
        elif rnum == 5:
            message += "I JUST WANTED TO CONGRATULATE YOU ON " + choice(adverbs) + " GAINING THE RANK OF " + choice(salutations2) + "! "
        else:
            message += "WOULD YOU BE ABLE TO PROVIDE SOME " + choice(nouns) + " TO MY " + choice(salutations2) + "? "
    message += "\n\nYOURS " + choice(adverbs) + "," + "\n\n" + "CORPORATE."
    print(message)

letter(5)
