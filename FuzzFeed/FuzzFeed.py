from twython import Twython

import random
import time


class Fuzzfeed(object):

    def __init__(self, post, iterations):

        self.post = post

        self.iterations = iterations

        self.appKey = 'INSERT_APP_KEY'

        self.appSecret = 'INSERT_APP_SECRET'

        self.tokenKey = 'INSERT_TOKEN_KEY'

        self.tokenSecret = 'INSERT_TOKEN_SECRET'

        self.numbers = [
            '2',
            '3',
            '4',
            '5',
            '9',
            '10',
            '11',
            '12',
            '13',
            '15',
            '20',
            '25',
            '32',
            '33',
            '36',
            '42',
            '49',
            '50',
            '72',
            '99',
            '100',
            '101',
            '110',
            '111',
            ]

        self.adjectives = [
            'Cringeworthy',
            'Unbelievable',
            'Underrated',
            'Intriguing',
            'Fanstastic',
            'Gruesome',
            'Adorable',
            'Arousing',
            'Unexpected',
            'Functional',
            'Unaccounted-For',
            'Digital',
            'Unexpected',
            'Analytical',
            'Unbiased',
            'Wise',
            'Lewd',
            'Belligerent',
            'Decisive',
            'Divisive',
            'Cultured',
            'Uncultured',
            'Credible',
            'Fortuitous',
            'Deadly',
            'Brand-New',
            'Critical',
            'American',
            'Unbearable',
            'Ancient',
            'Politically-Correct',
            'Politically-Incorrect',
            'Medieval',
            'Fictonal',
            'Modern',
            'Motherly',
            'Sarcastic',
            'Cross-Platform',
            'Cutting Edge',
            'Bleeding Edge',
            'For-Sale',
            'For-Profit',
            'Colorful',
            'Platonic',
            'Undeniable',
            'Impossible',
            'Depressing',
            'One-Sided',
            'Non-Profit',
            'Online',
            'Beautiful',
            'Disappointing',
            'Deterministic',
            'Existential',
            'Morally-Bankrupt',
            'Extra-Friendly',
            'Satisfying',
            'Objective',
            'Original',
            'Entropic',
            'Euphoric',
            'Cuddly',
            'Flaky',
            'Itsy-Bitsy',
            'Deafening',
            'Golden',
            'Pursuasive',
            'Exploratory',
            'Expository',
            'Womanly',
            'Tacky',
            'Accidental',
            'Alcoholic',
            'Pointless',
            'Repetitive',
            'Unoriginal',
            'Nonsensical',
            'Nonchalant',
            'Anticlimactic',
            'Bipartisan',
            'Exclusive',
            'Complete',
            'Incomplete',
            'Creative',
            'Masterful',
            'Explicit',
            'Implicit',
            'Obscene',
            'Vulgar',
            'Dubstep',
            'Metallic',
            'Metal',
            'Final',
            'Qualitative',
            'Quantitative',
            'Canadian',
            'Northern',
            'Beats',
            'Poorly-Made',
            'Overly-Compressed',
            'Genetically-Engineered',
            'Fluffy',
            'Memetic',
            'Primal',
            'Drastic',
            'Dastardly',
            'Cruel',
            'Tragic',
            'Misinformed',
            'Inept',
            'Inopportune',
            'Next-Gen',
            'Discounted',
            ]

        self.nouns = [
            'Military Officers',
            'Police Officers',
            'Tertiary Colors',
            'Primary Colors',
            'Secondary Colors',
            'Geniuses',
            'Topics',
            'Billboards',
            'Memes',
            'Things',
            'Tweets',
            'Moments',
            'Fanarts',
            'Paintings',
            'Items',
            'Reddit Posts',
            'Reddit Users',
            'Buzzwords',
            'GIFs',
            'JPEGs',
            'WAVs',
            'MP4s',
            'Images',
            'Doctors',
            'Subhumans',
            'Anime Characters',
            'Physicians',
            'Rappers',
            'Famous People',
            'Professors',
            'Corpses',
            'Corporations',
            'Grandmas',
            'Nurses',
            'Poisions',
            'Jokes In Bad Taste',
            'Politicians',
            'Plebians',
            'Businessmen',
            'Misogynists',
            'Martyrs',
            'Leaders',
            'Presidents',
            'Geocachers',
            'Serial Killers',
            'Congressmen',
            'Senators',
            'Followers Of Voldemort',
            'Drug Dealers',
            'Pharmacists',
            'Pharmaceuticals',
            'Conspiracy-Theorists',
            'Human Beings',
            'Programs',
            'Chemists',
            'Lawyers',
            'Kings',
            'Nobility',
            'Citizens',
            'Sentient Creatures',
            'Chimeras',
            'Image-Macros',
            'Old People',
            'TV Shows',
            'Apps',
            'Bosses',
            'Lists',
            'Public-Service Workers',
            'Food-Service Workers',
            'Prepaid Giftcards',
            'Keyboards',
            'Episodes Of Breaking Bad',
            'Episodes Of Game of Thrones',
            'Episodes Of The Walking Dead',
            'Episodes Of Malcolm In The Middle',
            'Episodes Of The Simpsons',
            'Countries Without Free Healthcare',
            'Liberal Arts Professors',
            'Kittens',
            'Hygiene Products',
            'Children Of Veterans',
            'Uncles',
            'Aunts',
            'Obscure Shows',
            'Lists Of Lists',
            'Lists Of Lists Of Lists',
            'Anti-Jokes',
            'Homecooked Meals',
            'Abbreviations',
            'Initialisms',
            'Parents',
            'Distant Relatives',
            'Etymologies',
            'Prime Ministers',
            'Sitcoms',
            'Powerpoint Presentations',
            'Buzzfeed Title Generators',
            'Lies Your Parents Told You',
            'Senior Citizens',
            'College Presidents',
            'Phenotypes',
            'Genotypes',
            'Alleles',
            'Nucleotides',
            'Prions',
            'Bacteriophages',
            'Mammals',
            'Laws Of Thermodynamics',
            'Physicists',
            'Geneticists',
            'Biologists',
            'Shrinks',
            'Binary Search Trees',
            'Logarithmic Equations',
            'Turing Machines',
            'Hair Gels',
            'Mathematicans',
            'Inequalities',
            'Matrices',
            'Vector Spaces',
            'Foreigners',
            'Standard Models',
            'Alcohoholic Beverages',
            'Low-Cost Sources Of Friendship',
            'Human Psyches',
            'Moons',
            'Plural Nouns',
            'Mad-Libs',
            'Direct Messages',
            'Friendster Users',
            'Ways To Talk About The World',
            'Nigerian Princes',
            'Examples Of Divine Intervention',
            'Santa Clauses',
            'Eigenspaces',
            'Videos',
            'Insects',
            'Bunnies',
            'Evolutionary Biologists',
            'College Classes',
            'Evolutionary Advantages',
            'Monetary Quantities',
            'Visible Light Wavelengths',
            'Code-Snippets',
            'Telegrams',
            'Contracts',
            'Viral Infections',
            'Bacterial Infections',
            'Nuns',
            'Priests',
            'Monks',
            'Popes',
            'Benefactors',
            'Times You Forgot To Do Your Laundry',
            'Times You Bumped Into Someone',
            'Times You Brushed Your Teeth',
            'Times You Should\'t Press The Red Button',
            'Times You Shouldn\'t Have Pressed The Red Button',
            'Times You Pressed The Red Button',
            'Times You Forgot Your Password',
            'Times You Forgot Your Carkeys',
            'Bacteria',
            'Viruses',
            'Lessons',
            'Ecoreps',
            'Logicians',
            'Philosophers',
            'Ends Of Lists',
            ]

        self.reasonsPart1 = [
            'That Will Make You Hate',
            'That Aren\'t As Cool As',
            'That Cover The Topic Of',
            'That Exemplify',
            'That Make Fun Of',
            'That Undermine',
            'That Disregard',
            'That Lie About',
            'That Take Too Long To Talk About',
            'That Remind You Of',
            'That Tell The Story Of',
            'That Will Surprise You About',
            'That Prevent Productive Discourse On',
            'That Defeat The Purpose Of',
            'That Will Make You Think Differently About',
            'That Promote The Stereotypes Of',
            'That Lie To You About',
            'That Don\'t Mention',
            'That Will Make You Forget All About',
            'That Are Not About',
            'That Don\'t Want You To Know About',
            'That Are The Opposite Of',
            'That Fail To Properly Explain',
            'That Have Nothing To Do With',
            'That Prove Nobody Cares About',
            'That Mothers Hate Because Of',
            'That Caused Horrible Results In',
            'That Forgot About',
            'That Talk A Lot About',
            'That Exaggerate',
            'That Force You To Remember',
            'That Sound Just Like',
            'That Force You To Believe In',
            'That Doctors Hate Because Of',
            'That Really Want To Be',
            'That Really Want You To Be',
            'That Nurture',
            'That Act Like They Own',
            'That Want To Stop',
            'That Can\'t Stop',
            'That Will Never Understand',
            'That Have Always Understood',
            'That Your Kids Won\'t Tell You About',
            'That Know All About Your Relationship With',
            'That Over-Complicate',
            'That Show It\'s Not About',
            'That Show It\'s Never Been About',
            'That Remind You How Wrong It Is To Talk About',
            'That Prove The Existence Of',
            'That Disprove The Existence Of',
            'That Fear',
            'That Deny',
            'That Promote',
            'That Exemplify The Failures Of',
            'That Show No Evidence For',
            'That Are Pessimistic About',
            'That Grandparents Hate Because Of',
            'That Discovered The True Meaning Of',
            'That Wound Up In',
            'That Adore',
            'That Are Privileged Enough To Talk About',
            'That Are About',
            'That Can\'t Handle',
            'That Are In Facebook Posts About',
            'That Are In Twitter Statuses About',
            'That Are In Reddit Posts About',
            'That Can\'t Seem To Grasp',
            'That Hate Christmas Because Of',
            'That Hate Halloween Because Of',
            'That Hate Thanksgiving Because Of',
            'That Contain Information Pertaining To',
            'That Doubt',
            'That Determine It Is Inconsequential To Discuss',
            'That Pertain To',
            'That Raised The Price Of',
            'That Make You Think Your Parents Will Take Away',
            'That Make You Want To Put Away',
            'That Buzzfeed Never Mentions About',
            'That Think Professors Care About',
            'That Totally Forgot To Mention',
            'That Absolutely Meant To Mention',
            'That Fear The Wrath Of',
            'That Repetitively Mention',
            'That Don\'t Need',
            'That Could Do Without',
            'That Would Be Fine Without',
            'That Used To Mean Something About',
            ]

        self.reasonsPart2 = [
            'The World',
            'The Universe',
            'The Galaxy',
            'The Moon',
            'The Solar System',
            'Being In Your 30s',
            'Being In Your 20s',
            'Being In Your Teens',
            'Being An Adult',
            'Honeybooboo',
            'Honeybooboo\'s Mom',
            'The Inexorable Passage Of Time',
            'The End Of All Microbial Life',
            'That Time You Did That Thing You Did',
            'Facetime',
            'The American Dream',
            'Diversity',
            'Driving',
            'Corporate',
            'Human Resources',
            'Crying',
            'The Impact',
            'Higher-Order Thinking',
            'Common-Core',
            'Monty Python',
            'Programmers',
            'Computer Science',
            'Computer Scientists',
            'Third-World Countries',
            'The Patriarchy',
            'Gandhi',
            'Obama',
            'Stalin',
            'Python',
            'Corpses',
            'Sports',
            'The All-Father Odin',
            'Mother Theresa',
            'Vladimir Putin',
            'Madamir Putin',
            'Gladamir Putin',
            'Sadamir Putin',
            'North Korea',
            'Japan',
            'Vietnam',
            'The Boston Tea Party',
            'Heat Death',
            'Absolute Zero',
            'Kittens',
            'Pornography',
            'America',
            'HTML5',
            'The Information Highway',
            'The New iPhone',
            'The Latest Linux Distro',
            'Vlogging',
            'Portal',
            'Portal 2',
            'Half Life 3',
            'Fifth World Problems',
            'Digital Literacy',
            'Being Literally Hitler',
            'Your Mom',
            'Alcohol Poisoning',
            'Hitler Youth',
            'The Rules Of The Internet',
            'Cards Against Humanity',
            'The Quadratic Equation',
            'Mad Sociology',
            'Jokes In Bad Taste',
            'XKCD',
            'Webcomics',
            'The Police',
            'Fighting The Man',
            'Anime',
            'Object-Oriented Programming',
            'Purity',
            'Hatred',
            'Sociopathy',
            'Satanism',
            'Anarchism',
            'Anarchy',
            'A Very Convenient Truth',
            'Nuclear Fission',
            'Your Highschool Sweetheart',
            'Your Least Favorite Brand Of Clothing',
            'Your Least Favorite Book',
            'Your Least Favorite Ice Cream Flavor',
            'Your Least Favorite College Class',
            'Your Least Favorite Reddit User',
            'Your Favorite Fruit',
            'Your Greatest Fear',
            'Human Nature',
            'Religious Uncertainty',
            'A Greater Feeling Of Togetherness',
            'The Hiccups',
            'Eating Too Much',
            'Being Tall',
            'Being Famous',
            'Exhibiting Empathy',
            'A Shakespearean Tragedy',
            'Quantum Physics',
            'YOLO Swag',
            'Avogadro\'s Constant',
            'Science Fiction',
            '1337 Speak',
            'Our Collective Consciousness',
            'Genetics',
            'Palindromes',
            'Anagrams',
            'International Affairs',
            'Moving Forward',
            'All The Bandwidth',
            'The Observable Universe',
            'Love',
            'Maternal Instincts',
            'Pop Music',
            'Getting Good Grades',
            'Procrastination',
            'Reddit',
            'iFunny',
            'Nouns',
            'Adjectives',
            'Numbers',
            'Calculus',
            'College',
            'Linear Algebra',
            'Trigonometry',
            'Proto-Indo European',
            'Our Ancenstral Origin',
            'Crowdfunding',
            'Ragnarok',
            'The Continental United States',
            'Orphans',
            'Nicolas Cage, The One True God',
            'Vampires Kissing',
            'Loving Yourself Like Kanye Loves Kanye',
            'Taking It Too Far',
            'Morgan Freeman',
            'Michio Kaku',
            'Neil DeGrasse Tyson',
            'Stephen Hawking',
            'Stephen King',
            'Learning Something New',
            'The Gradual Decline Of Sega\'s Popularity',
            'Mario',
            'Luigi',
            'Sonic',
            'Donkey Kong',
            'Super Smash Brothers',
            'Being A Student',
            'Being A Professor',
            'Crying In Your Sleep',
            'Intrusive Thoughts',
            'Drug Abuse',
            'The War',
            'The US Legal System',
            'Ageism',
            'The Nintendo Wii',
            'The Original Playstation',
            'Dumbledore',
            'The Death Of Harry Potter\'s Parents',
            'The Lack Of Substantial Evidence',
            'Growing Up',
            'Aging Backwards',
            'Selling Your Organs',
            'Maternal Ingenuity',
            'The National German Socialist Workers Party',
            'Peace On Earth',
            'World Hunger',
            'The Profitability Of The Drug Trade',
            'The Free Market Economy',
            'Dynamics',
            'Chaos Theory',
            'The Big Crunch',
            'Game Theory',
            'String Theory',
            'Mammalian Lactation',
            'Manifest Destiny',
            'The San Andreas Fault',
            'Al Capone',
            'Buzz Aldrin',
            'Alan Turing',
            'Dying Of Mercury Posoining',
            'Asphyxiating In The Vacuum Of Space',
            'Checking Your Privilege',
            'The Twilight Saga',
            'The Success Of The Matrix Trilogy',
            'George Lucas',
            'Han Shooting First',
            'Descartes',
            'John Locke',
            'Narrowly Escaping Death',
            'Excaping The Paparazzi',
            'Being Too Big To Fail',
            'The Titanic',
            'Captain Ahab',
            'When Kline Closes At 7:30PM',
            'Petting A Doggy',
            'Petting A Kitty',
            'Helping A Cow Give Birth',
            'The Olfactory Lobe',
            'Singles In Your Area',
            '1 Weird Trick This Mom Learned',
            'A Reverse Turing Machine',
            'Proof That Santa Is Real',
            'The WinRAR EULA',
            'The iTunes EULA',
            'The Calico EULA',
            'The EULA',
            'The DMCA',
            'All Acronyms Ever',
            'Spock',
            'Being An Astronaut',
            'Being A Cosmonaut',
            'Screaming Internally',
            'Studying',
            'The Finite Volume Of The Observable Universe',
            'Wolfram Alpha',
            'The Greek Alphabet',
            'Roman Numerals',
            'Arabic Numerals',
            'Forgetting One Character And Breaking All Your Code',
            'Almost Forgetting To Go To Class',
            'Pulling Your Hair Out',
            'Agoraphobia',
            'Political Comics',
            'Medical Advertisements',
            'Isaac Asimov',
            'Bard College',
            'Reading',
            'Writing',
            'Critical Thinking',
            'Logic',
            'LOTR Characters',
            'Being Useful',
            'Being Productive',
            'Being Inept',
            'Being Good With Your Hands',
            'An Inconvenient Truth',
            'Reading Your Emails',
            'Star Wars',
            'Pulp Fiction Quotes',
            'Pulp Fiction',
            'Occasional Irregularity',
            'Ending A List',
            'Yelling Obscenities',
            'Polymorphism',
            'On-Campus Dining',
            'Gabe Newell',
            'Valve',
            'Steam',
            'The Source Engine',
            'DRM',
            'PayPal',
            ]

        self.twitter = Twython(self.appKey, self.appSecret,
                               self.tokenKey, self.tokenSecret)

        self.titles = []

        for i in range(self.iterations):

            self.number = random.choice(self.numbers)

            self.adjective = random.choice(self.adjectives)

            self.noun = random.choice(self.nouns)

            self.reasonPart1 = random.choice(self.reasonsPart1)

            self.reasonPart2 = random.choice(self.reasonsPart2)

            self.title = self.number + ' ' + self.adjective + ' ' \
                + self.noun + ' ' + self.reasonPart1 + ' ' \
                + self.reasonPart2

            if self.post and len(self.title) <= 140:

                self.twitter.update_status(status=self.title)

            self.titles.append(self.title)

            self.titles.append(self.post)

    def __len__(self):

        return self.iterations

    def __repr__(self):

        print str(self.titles)

    def __str__(self):

        return str(self.titles)


for i in range(1000000):

    feed = Fuzzfeed(True, 1)

    print 'The posted feed reads: ' + str(feed)

    time.sleep(300)
