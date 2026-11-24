"""Batch 2: Dec 8, 1926 to Jan 7, 1927. Same standard as batch 1: read off the page images."""
PAGES2 = [
 {'date': '1926-12-08', 'lccn': 'sn82016181', 'paper': 'The Washington Daily News', 'city': 'Washington', 'state': 'DC', 'family': 'care',
  'family_note': 'Small stories in the bottom half cover accidental deaths and a sledding injury.',
  'headlines': [
   {'text': 'Denby Says He Asked Harding to Transfer Naval Reserves', 'family': True},
   {'text': 'Local Budget Nearly Two Millions Above Sum for This Year', 'family': True},
   {'text': 'Palace at Bucharest Burns; Queen Marie and Family Safe', 'family': True},
   {'text': 'Former Navy Chief on Stand in Trial of Fall-Doheny', 'family': True}],
  'spots': [
   {'spot': 'The price, 2 cents, printed big inside the weather box', 'where': 'top left corner'},
   {'spot': 'A photo of a woman in a long coat and a close-fitting 1920s hat, walking toward the camera', 'where': 'top left of center'},
   {'spot': 'A drawn portrait of Edwin Denby, a former Secretary of the Navy', 'where': 'top right of center'},
   {'spot': 'The city budget includes $150,000 for bathing pools', 'where': 'top left column'},
   {'spot': 'The paper calls itself "The News" with a little Capitol dome in the middle of its name', 'where': 'top'}],
  'then_vs_now': {'kind': 'change', 'text': 'The Washington Daily News was a separate paper in 1926. In 1972 it merged with the Evening Star, and the combined paper closed in 1981.',
                  'source': 'Library of Congress, About Evening Star', 'url': 'https://www.loc.gov/item/sn83045462/'},
  'question': 'Queen Marie, who sailed home from America two weeks earlier, is safe after a palace fire. What would you grab first if you had to leave home in a hurry?'},

 {'date': '1926-12-10', 'lccn': 'sn92073229', 'paper': 'The Chapel Hill Weekly', 'city': 'Chapel Hill', 'state': 'NC', 'family': 'ok',
  'family_note': '',
  'headlines': [
   {'text': 'School Children Prepare for Big Christmas Show', 'family': True},
   {'text': 'Site in Ravine Is Chosen for Kenan Stadium', 'family': True},
   {'text': 'Alarm Interrupts Firemen\'s Party', 'family': True},
   {'text': 'A Feast of Light', 'family': True}],
  'spots': [
   {'spot': 'A fire alarm that went off in the middle of the firemen\'s own supper party', 'where': 'top center'},
   {'spot': '"The Mysterious Turkey": a turkey left at a professor\'s door by someone who never gave a name', 'where': 'top right of center'},
   {'spot': 'A notice that "A Christmas Carol" by Charles Dickens will be read aloud on Sunday', 'where': 'bottom left'},
   {'spot': 'The schoolchildren\'s Christmas show set in an old English manor, with a yule log and a boar\'s head', 'where': 'top left column'},
   {'spot': 'The price: $1.50 a year in advance, or 5 cents a copy', 'where': 'top right'}],
  'then_vs_now': {'kind': 'change', 'text': 'A week after our Dec 3 page, the stadium site was picked: the ravine. Kenan Stadium hosted its first game on November 12, 1927, and the Tar Heels are playing their 100th season there this fall.',
                  'source': 'UNC-Chapel Hill, 100 seasons later, Kenan Stadium remains a campus fixture', 'url': 'https://www.unc.edu/story/100-seasons-later-kenan-stadium-remains-a-campus-fixture/'},
  'question': 'The firemen had to leave their own party for a real alarm. When have you stopped something fun to help someone?'},
]

ALTERNATES2 = [
 {'date': '1926-12-09', 'lccn': 'sn85042243', 'paper': 'The Bismarck Tribune', 'city': 'Bismarck', 'state': 'ND', 'family': 'no',
  'family_note': 'A mine disaster and a headline about famine and cannibalism in China. Adult mode only, and only if the owner picked North Dakota.',
  'headlines': [{'text': 'Ormiston Found in Pennsylvania City', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
 {'date': '1926-12-12', 'lccn': 'sn84020064', 'paper': 'Douglas Daily Dispatch', 'city': 'Douglas', 'state': 'AZ', 'family': 'no',
  'family_note': 'Two stories describe killings in detail. Adult mode only, and only if the owner picked Arizona.',
  'headlines': [{'text': 'Damage Suit Filed Against S. White', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
]
ALTERNATES2 += [
 {'date': '1926-12-13', 'lccn': 'sn82015313', 'paper': 'The Indianapolis Times', 'city': 'Indianapolis', 'state': 'IN', 'family': 'no',
  'family_note': 'Lead story is a poisoning plot and another headline describes a body found with a crushed skull. Adult mode only, and only if the owner picked Indiana.',
  'headlines': [{'text': 'Cold Wave Descending From West', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
]
ALTERNATES2 += [
 {'date': '1926-12-14', 'lccn': 'sn92070146', 'paper': 'Imperial Valley Press', 'city': 'El Centro', 'state': 'CA', 'family': 'no',
  'family_note': 'Headlines about a suicide and a murder. Adult mode only, and only if the owner picked California. Also carries "Missing Novelist Reported Found" (Agatha Christie).',
  'headlines': [{'text': 'Missing Novelist Reported Found', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
]
PAGES2 += [
 {'date': '1926-12-09', 'lccn': 'sn87093042', 'paper': 'The Kennewick Courier-Reporter', 'city': 'Kennewick', 'state': 'WA', 'family': 'ok',
  'family_note': '',
  'headlines': [
   {'text': 'Urges More Berries and Asparagus', 'family': True},
   {'text': 'Ask Patrons to Mail Early', 'family': True},
   {'text': 'Car Licenses Show Growth', 'family': True},
   {'text': 'Schools Are Now Closed', 'family': True}],
  'spots': [
   {'spot': 'A grammar puzzle box: "Is is is, or is is are?"', 'where': 'top right corner'},
   {'spot': '"Winter Bananas Head the Apple Prices" (Winter Banana is a kind of apple)', 'where': 'top, fourth column'},
   {'spot': 'The state expects 40,000 more cars next year, and the new license plates reverse their colors', 'where': 'middle center'},
   {'spot': 'A boxed notice telling rural mail patrons what the carriers may and may not pick up', 'where': 'top center'},
   {'spot': 'Schools closed by a light form of smallpox, to open again on the 20th', 'where': 'top right'}],
  'then_vs_now': {'kind': 'change', 'text': 'In 1926 a smallpox outbreak could close the schools in a town. Smallpox has since been wiped out worldwide: the World Health Organization declared it eradicated in 1980.',
                  'source': 'World Health Organization, Smallpox', 'url': 'https://www.who.int/health-topics/smallpox'},
  'question': 'The paper asks: in "Three-fourths of the oats raised in the United States is (are) shipped over our road," should it be "is" or "are"? What do you think, and why?'},
]
ALTERNATES2 += [
 {'date': '1926-12-11', 'lccn': 'sn83045499', 'paper': 'The Daily Alaska Empire', 'city': 'Juneau', 'state': 'AK', 'family': 'no',
  'family_note': 'Front page carries a headline about lynchings. Adult mode only, and only if the owner picked Alaska.',
  'headlines': [{'text': 'Oil Scandal Evidence Complete', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
]
PAGES2 += [
 {'date': '1926-12-13', 'lccn': 'sn87062169', 'paper': 'Seward Daily Gateway', 'city': 'Seward', 'state': 'AK', 'family': 'care',
  'family_note': 'Lower headlines cover a bank robbery, a gunman\'s body being exhumed, and a boxing story that uses a period racial label. Stick to the railroad, the planes and the spots.',
  'headlines': [
   {'text': 'Ten Million Dollars Are Required to Complete the Alaska Railroad and Modernize System\'s Equipment', 'family': True},
   {'text': 'Stenographer of Governor-Elect Is Bank Robber', 'family': False},
   {'text': 'Europe Be Dry Some Time Says the "Pussyfoot"', 'family': True},
   {'text': 'Trans-Continental Planes at San Diego', 'family': True},
   {'text': 'Body Notorious Gunman Exhumed San Francisco', 'family': False}],
  'spots': [
   {'spot': 'A $10 million price tag to finish the Alaska Railroad', 'where': 'top left, lead story'},
   {'spot': 'Six Marine Corps planes finish a coast-to-coast flight from Quantico, Virginia, to San Diego', 'where': 'bottom right'},
   {'spot': 'A storm at Unga: dories lost, boats wrecked, shingles blown from houses', 'where': 'middle left'},
   {'spot': '"Last Call Sounded for Adjusted Compensation": World War veterans must apply before January 1', 'where': 'bottom, fourth column'},
   {'spot': 'A short item: more cases of scarlet fever in Anchorage', 'where': 'bottom, fourth column'}],
  'then_vs_now': {'kind': 'change', 'text': 'In 1926 the Alaska Railroad was run by the federal government, and Washington paid its bills. Ownership passed to the State of Alaska in 1985.',
                  'source': 'Alaska Railroad, Our History', 'url': 'https://www.alaskarailroad.com/corporate/history'},
  'question': 'In 1926 almost no roads connected Alaska towns. Why would a railroad matter so much to a place like Seward?'},
]
ALTERNATES2 += [
 {'date': '1926-12-13', 'lccn': '2022239700', 'paper': 'The Cordele Dispatch', 'city': 'Cordele', 'state': 'GA', 'family': 'no',
  'family_note': 'A banner headline about a widow describing her husband\'s murder. Adult mode only, and only if the owner picked Georgia.',
  'headlines': [{'text': 'Move to Turn Muscle Shoals Over to Alabama Power Co.', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
]
PAGES2 += [
 {"date": "1926-12-12", "lccn": "sn96060774", "paper": "Nogales International", "city": "Nogales", "state": "AZ", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "Amigo Mining Claims Near Patagonia Sold", "family": True},
   {"text": "300 New Families May Locate Here", "family": True},
   {"text": "Nogales Player on All-Southern Team", "family": True},
   {"text": "Human Fly to Climb Front of Bowman Hotel Building", "family": True},
   {"text": "Nogales Must and Will Have Paved Streets in 1927", "family": True}],
  "spots": [
   {"spot": "A cartoon of Santa and a man with a brush pasting up a \"Do your Xmas shopping early\" sign", "where": "top center"},
   {"spot": "A photo of a Chicago hockey team on the ice, in sweaters with a big C", "where": "bottom left"},
   {"spot": "\"The Human Fly\": a photo of Babe White climbing the side of a tall building", "where": "bottom center"},
   {"spot": "A banner across the bottom promising paved streets in 1927", "where": "very bottom"},
   {"spot": "\"11 days left to shop\"", "where": "bottom center, small box"}],
  "then_vs_now": {"kind": "continuity", "text": "This page shows a Chicago team joining a hockey league. The same winter, 1926-27, was the first season for Chicago's NHL team, now the Blackhawks, which still plays today.",
                  "source": "NHL Records, franchise data for the Chicago Blackhawks (first season 1926-27)", "url": "https://records.nhl.com/site/api/franchise?cayenneExp=id=11"},
  "question": "The paper promises paved streets in 1927. What would a town with dirt streets look, sound and smell like?"},
]
ALTERNATES2 += [
 {"date": "1926-12-11", "lccn": "sn87062169", "paper": "Seward Daily Gateway", "city": "Seward", "state": "AK", "family": "no",
  "family_note": "A headline about famine and cannibalism in China. Adult mode only.",
  "headlines": [{"text": "Rumanian Situation Growing More Tense; War Clouds Looming", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
 {"date": "1926-12-11", "lccn": "sn82014248", "paper": "Daily Kennebec Journal", "city": "Augusta", "state": "ME", "family": "no",
  "family_note": "Headlines about lynchings, a killing of dry agents and a hunting death. Adult mode only, and only if the owner picked Maine.",
  "headlines": [{"text": "Wet Rout in Showdown on Dry Law", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1926-12-14", "lccn": "sn83045462", "paper": "Evening Star", "city": "Washington", "state": "DC", "family": "care",
  "family_note": "The lower half has disaster headlines: a chemical blast, a fight in Mexico, an auto wreck and a shipwreck. Stick to the top half and the spots.",
  "headlines": [
   {"text": "U.S. Workers Get Assurance of Half Day Christmas Eve", "family": True},
   {"text": "Cold Snap Is Due in Capital Tonight; Drop to 24 Likely", "family": True},
   {"text": "Fog Wrecks Trains and Holds Up Ships", "family": True},
   {"text": "Bill to Purchase Triangle Put on Senate Calendar", "family": True},
   {"text": "19 Killed, 70 Hurt in Chemical Blast", "family": False}],
  "spots": [
   {"spot": "A cartoon of a worried grandmother in a rocking chair, with newspapers spread on the floor", "where": "top center"},
   {"spot": "\"Yesterday's Circulation, 103,514\": how many papers were sold", "where": "top right, under the masthead"},
   {"spot": "The page count in the date line: fifty-four pages", "where": "top, date line"},
   {"spot": "A box: \"Only 11 More Days, Christmas Will Be Here, Shop Now!\"", "where": "bottom right"},
   {"spot": "\"Radio Programs, Page 38\"", "where": "bottom right corner"}],
  "then_vs_now": {"kind": "change", "text": "This page reports a bill to buy \"the triangle\" for government buildings. That 70-acre area became the Federal Triangle, where the EPA works today in buildings finished in 1934.",
                  "source": "U.S. General Services Administration, EPA East and West Buildings history", "url": "https://www.gsa.gov/real-estate/explore-historic-buildings/find-a-historic-federal-building/epa-east-and-west-building-washington-dc"},
  "question": "Federal workers got a half day off on Christmas Eve. Who decides when people get a holiday, and should they?"},
]
ALTERNATES2 += []
ALTERNATES2 += [
 {"date": "1926-12-15", "lccn": "sn82014519", "paper": "New Britain Herald", "city": "New Britain", "state": "CT", "family": "no",
  "family_note": "A large headline describes a man run over and killed by a bus, plus a body found in a snowbank and a murder charge. Adult mode only, and only if the owner picked Connecticut.",
  "headlines": [{"text": "Senator Edge Now Trying to Unite Workers for Wets", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1926-12-11", "lccn": "sn82015295", "paper": "The McCarthy Weekly News", "city": "McCarthy", "state": "AK", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "Bridge Across the Kennecott River", "family": True},
   {"text": "The Following Petition Is Being Circulated", "family": True},
   {"text": "New Ship for Alaska Run", "family": True},
   {"text": "Kennecott Movies", "family": True}],
  "spots": [
   {"spot": "Farmers built a temporary bridge across the Kennecott River so they could sell farm products", "where": "top, second column"},
   {"spot": "A petition asking for a road so tractors can haul freight from McCarthy to Chisana", "where": "top, third column"},
   {"spot": "\"Lutefisk at Marshall\": a one-line ad for a Norwegian fish dish", "where": "bottom, second column"},
   {"spot": "The movie list: Will Rogers in a comedy, and \"Lorraine of the Lions\"", "where": "bottom right"},
   {"spot": "A New Year's Eve masquerade ball planned at the Kennecott Recreation Hall", "where": "top left, Brief Locals"}],
  "then_vs_now": {"kind": "change", "text": "In 1926 McCarthy sat next to Kennecott, a busy copper mining town. The mines closed in 1938, and Kennecott is now a National Historic Landmark inside Wrangell-St. Elias National Park.",
                  "source": "National Park Service, Kennecott Mines National Historic Landmark", "url": "https://www.nps.gov/wrst/learn/historyculture/kennecott-mines-national-historic-landmark.htm"},
  "question": "This whole front page is local news: who went where, a new bridge, a dance. How is that different from the news you see today?"},
]
PAGES2 += [
 {"date": "1926-12-25", "lccn": "sn83045462", "paper": "Evening Star", "city": "Washington", "state": "DC", "family": "care",
  "family_note": "The middle row has crime headlines: a murder trial, a missing woman feared dead, a store hold-up. Stick to the Christmas stories, the cartoon and the spots.",
  "headlines": [
   {"text": "Simple, Happy Christmas Day Is Observed at White House", "family": True},
   {"text": "Capital Is Aglow With Yule Spirit, Led by President", "family": True},
   {"text": "Hirohito Ascends as Japan Mourns", "family": True},
   {"text": "Revenue Building Construction Will Begin in February", "family": True},
   {"text": "McDermott Faces Life for Murder", "family": False}],
  "spots": [
   {"spot": "The cartoon \"Christmas Day, 1926\": Santa sprawled asleep on a bed in his boots, with his empty sack on the floor", "where": "top right"},
   {"spot": "President Coolidge spent an hour opening gifts, and Mrs. Coolidge got many flowers", "where": "top, second column"},
   {"spot": "\"Fund Is Started for Fatherless 7\": readers can send gifts through the Star", "where": "bottom right"},
   {"spot": "\"Yesterday's Circulation, 97,741\"", "where": "top right, under the masthead"},
   {"spot": "Hirohito becomes Emperor of Japan", "where": "middle left"}],
  "then_vs_now": {"kind": "continuity", "text": "Three Christmases before this paper, in 1923, President Coolidge lit the first National Christmas Tree near the White House. Every president since has taken part in that tradition.",
                  "source": "National Park Service, History of the National Christmas Tree", "url": "https://www.nps.gov/whho/learn/historyculture/national-christmas-tree-history.htm"},
  "question": "The cartoonist drew Santa worn out on Christmas Day. What does that say about Christmas Eve in 1926? Would you draw it the same way today?"},
]
ALTERNATES2 += [
 {"date": "1926-12-24", "lccn": "sn83045462", "paper": "Evening Star", "city": "Washington", "state": "DC", "family": "no",
  "family_note": "A large top headline about a train wreck with people crushed to death. Adult mode only. Also carries the story of Rebecca, the raccoon sent for the President's dinner who became a White House pet.",
  "headlines": [{"text": "Imposing Program Ushers Christmas Into City Tonight", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1926-12-15", "lccn": "sn84022374", "paper": "The Ellsworth American", "city": "Ellsworth", "state": "ME", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "Local Affairs", "family": True},
   {"text": "No School Signals", "family": True},
   {"text": "Join Our 1927 Christmas Club", "family": True},
   {"text": "Higgins' Battery Service", "family": True}],
  "spots": [
   {"spot": "Grocery prices: Stanzalone Coffee 47 cents a pound, canned tomatoes 2 for 25 cents", "where": "top left, Thorsen Farms ad"},
   {"spot": "The no-school signal: two blasts, repeated after a short interval, means no school that morning", "where": "top center, under the weather table"},
   {"spot": "A weather table for the week, with snow and cloudy days", "where": "top center"},
   {"spot": "A badge reading \"Member Federal Reserve System\"", "where": "top right, Union Trust Company ad"},
   {"spot": "An eye doctor's ad with a drawing of a big eye: \"Running on One Cylinder\"", "where": "bottom left"}],
  "then_vs_now": {"kind": "change", "text": "The bank ad shows a \"Member Federal Reserve System\" badge. The Federal Reserve was new then: the Federal Reserve Act of 1913 created it as the central bank of the United States, and it still is today.",
                  "source": "Board of Governors of the Federal Reserve System, Federal Reserve Act", "url": "https://www.federalreserve.gov/aboutthefed/fract.htm"},
  "question": "Most of this front page is ads. What do the ads tell you about what people in Ellsworth wanted to buy before Christmas 1926?"},
]
PAGES2 += [
 {"date": "1926-12-16", "lccn": "sn82007642", "paper": "Watauga Democrat", "city": "Boone", "state": "NC", "family": "care",
  "family_note": "One headline gives World War battle deaths, and a small item at the bottom left reports a mayor shot in Illinois. Everything else is local and gentle.",
  "headlines": [
   {"text": "Radium Springs to Be Developed in Ashe Co.", "family": True},
   {"text": "News of a Week at Blowing Rock", "family": True},
   {"text": "Banquet at Daniel Boone Hotel Tonight", "family": True},
   {"text": "Southern Air Mail Route Likely Be Realized Fact", "family": True},
   {"text": "50,510 Yankees Killed in World War Battles", "family": False}],
  "spots": [
   {"spot": "The Blowing Rock School honor roll, listed grade by grade", "where": "top, third column"},
   {"spot": "A banquet menu: cream of tomato soup, roast turkey with dressing, cranberry sauce, ice cream and cake", "where": "top, fifth column"},
   {"spot": "The cast list for the play \"The Path Across the Hill,\" including \"Zuzu, the cook\"", "where": "top, third column"},
   {"spot": "A short item: motor-driven roller skates are one of the latest fads in Europe", "where": "bottom, second column"},
   {"spot": "Plans for an air mail route linking New York and Atlanta", "where": "bottom, fourth column"}],
  "then_vs_now": {"kind": "change", "text": "In 1926 people hoped springs with radium in them could make them healthier. Today the U.S. Environmental Protection Agency warns that long exposure to high levels of radium can raise the risk of cancer.",
                  "source": "U.S. Environmental Protection Agency, Radionuclide Basics: Radium", "url": "https://www.epa.gov/radiation/radionuclide-basics-radium"},
  "question": "This paper lists every honor roll student by name. Why would a small-town paper print that? Would you want your name in the paper?"},
]
PAGES2 += [
 {"date": "1926-12-17", "lccn": "sn92073229", "paper": "The Chapel Hill Weekly", "city": "Chapel Hill", "state": "NC", "family": "care",
  "family_note": "A story about Paul Green's new play uses the period word for Black Americans. Explain that the word is no longer used. The rest is gentle village news.",
  "headlines": [
   {"text": "The Newspaper Institute Will Open January 5", "family": True},
   {"text": "Two Guests Make Briefest Social Call in History of the Village", "family": True},
   {"text": "Hill's Building Stirs Curiosity of the Village", "family": True},
   {"text": "Holiday Calm Begins", "family": True},
   {"text": "Christmas Mail", "family": True}],
  "spots": [
   {"spot": "The funny story of two guests who came in the wrong door of a party and left at once", "where": "top center"},
   {"spot": "Bim, the Abernethys' fox terrier, who likes ice cream", "where": "Chapel Hill Chaff column, bottom of second column"},
   {"spot": "\"The Community Tree\": a Christmas Eve tree lit with hundreds of colored lights", "where": "top, middle"},
   {"spot": "Trees cleared off the site for the new Kenan stadium", "where": "bottom, middle"},
   {"spot": "The Postmaster General's advice for Christmas mail, including writing \"special delivery\" on packages", "where": "right column"}],
  "then_vs_now": {"kind": "change", "text": "The Christmas mail notice tells people they can pay for \"special delivery.\" That service began in 1885 and ended in 1997.",
                  "source": "United States Postal Service Historian, On This Day in Postal History", "url": "https://about.usps.com/who-we-are/postal-history/on-this-day.pdf"},
  "question": "A whole story is about two guests who walked in the wrong door. Why would a town paper print a story like that?"},
]
PAGES2 += [
 {"date": "1926-12-18", "lccn": "sn82015295", "paper": "The McCarthy Weekly News", "city": "McCarthy", "state": "AK", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "A Mecca for Prospectors", "family": True},
   {"text": "Real Detectives Needed to Trace This Thief", "family": True},
   {"text": "Wonderful Display of Toys at Ben Jackson's", "family": True},
   {"text": "For Your Xmas Dinner", "family": True}],
  "spots": [
   {"spot": "A thief stole 560 skunks from a skunk farm in Montana", "where": "top, third column"},
   {"spot": "A black wolf pup arrived from Chitina", "where": "bottom left, Brief Locals"},
   {"spot": "The toy list: baby dolls, Charleston dolls, automobiles, red roadsters, mechanical toys", "where": "bottom, third column"},
   {"spot": "The Christmas dinner list: ripe olives, fresh oysters, turkey, goose, mince meat, plum pudding", "where": "bottom right"},
   {"spot": "The school children's Christmas entertainment and tree on Friday, December 24, at two o'clock", "where": "bottom left"}],
  "then_vs_now": {"kind": "change", "text": "In 1926 prospectors hauled supplies over a winter sled road. Today visitors drive the 60-mile McCarthy Road, which follows the old Copper River and Northwestern Railroad route.",
                  "source": "National Park Service, Wrangell-St. Elias: Driving Park Roads", "url": "https://www.nps.gov/wrst/planyourvisit/driving-park-roads.htm"},
  "question": "Who would steal 560 skunks, and how? Make up the story the paper did not tell."},
]
ALTERNATES2 += [
 {"date": "1926-12-18", "lccn": "sn87062013", "paper": "The Nome Nugget", "city": "Nome", "state": "AK", "family": "care",
  "family_note": "Lead story is about the Ormiston and Aimee Semple McPherson scandal. Usable as an Alaska alternate in adult mode.",
  "headlines": [{"text": "Ormiston Has Waived Extradition", "family": False}, {"text": "John Aikman Stewart Aged 104 Years, Died", "family": True}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1926-12-19", "lccn": "sn96060774", "paper": "Nogales International", "city": "Nogales", "state": "AZ", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "First Train on New Line Feb. 28", "family": True},
   {"text": "Passenger Train Service From Nogales to Mexico City Starts in February", "family": True},
   {"text": "Local Ford Car Travels 40.34 Miles on Gallon of Gasoline", "family": True},
   {"text": "Michaels Succeeds Curtis as Fire Department Chief", "family": True},
   {"text": "Racing Speedboats Collide", "family": True}],
  "spots": [
   {"spot": "The cartoon \"A Possible Mistake\": a man cheers \"Hooray! Santa Claus at my house\" while a burglar carries off a sack marked LOOT", "where": "top center"},
   {"spot": "A photo of two racing speedboats, one overturning", "where": "bottom center"},
   {"spot": "A smiling man in a Scottish cap: \"He's With Us Again\"", "where": "bottom left"},
   {"spot": "The \"Bill the Barber Says\" cartoon ad", "where": "bottom right"},
   {"spot": "\"5 days left to shop\"", "where": "bottom center"}],
  "then_vs_now": {"kind": "change", "text": "A 1924 Ford won a local contest by going 40.34 miles on a gallon of gas. The average new vehicle in model year 2024 got 27.2 miles per gallon, a record high for the average, though many of today's cars are far bigger and faster.",
                  "source": "U.S. Environmental Protection Agency, Highlights of the Automotive Trends Report", "url": "https://www.epa.gov/automotive-trends/highlights-automotive-trends-report"},
  "question": "The Ford won a contest, so it was driven very carefully. Is it fair to compare a contest winner with an average car? What would a fair test look like?"},
]
PAGES2 += [
 {"date": "1926-12-20", "lccn": "sn94050047", "paper": "Hyder Weekly Herald", "city": "Hyder", "state": "AK", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "Texas Creek Wagon Road Extension Practically Assured", "family": True},
   {"text": "Says District Will Produce More Gold Than California", "family": True},
   {"text": "November Exports Show Big Gain", "family": True},
   {"text": "Christmas Tree Plans Making Good Progress", "family": True},
   {"text": "Storm Douses Lights", "family": True}],
  "spots": [
   {"spot": "A long list of Alaska's November exports: salmon, halibut, herring, furs and copper", "where": "right column"},
   {"spot": "Odd items in the export list: reindeer meat, reindeer moss, walrus skins and whalebone", "where": "bottom right"},
   {"spot": "Heavy wet snow broke the power lines and plunged the camp into \"Stygian gloom\"", "where": "bottom, fifth column"},
   {"spot": "The steamer Border Queen arrives with one passenger and 60 tons of freight", "where": "bottom, third column"},
   {"spot": "The subscription price in the corner: $5.00 a year, or fifty cents a copy", "where": "top corners"}],
  "then_vs_now": {"kind": "continuity", "text": "Canned salmon tops Alaska's export list on this page. Salmon still matters most: about 98 percent of the wild salmon caught in the United States comes from Alaska waters.",
                  "source": "Alaska Seafood Marketing Institute, Alaska Wild Salmon Day release, Aug. 10, 2023", "url": "https://www.alaskaseafood.org/news/for-release-alaska-wild-salmon-day-honors-our-nations-favorite-fish-and-the-people-who-provide-it/"},
  "question": "Hyder was a tiny mining town. Why do you think the paper printed a whole list of exports with numbers?"},
]
PAGES2 += [
 {"date": "1926-12-21", "lccn": "sn86063758", "paper": "The Herald and News", "city": "Newberry", "state": "SC", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "News of Interest From Prosperity", "family": True},
   {"text": "Christmas Tree Before Your Store Door", "family": True},
   {"text": "Goodfellows Still Need Some Ready Cash", "family": True},
   {"text": "White Christmas", "family": True},
   {"text": "Christmas Exercises at St. Philips School", "family": True}],
  "spots": [
   {"spot": "The Goodfellows club needs $200 more for Christmas baskets, and lists every member who gave", "where": "top, fifth column"},
   {"spot": "A plan to put a Christmas tree with lights in front of every Main Street store", "where": "top, second column"},
   {"spot": "A Christmas program list: songs, a play called \"Christmas Gifts\", and \"Five Little Girls\"", "where": "bottom center"},
   {"spot": "\"Twice a Week, $1.50 a Year\"", "where": "top right, date line"},
   {"spot": "A short item: Christmas seals for a penny help fight tuberculosis", "where": "bottom, fourth column"}],
  "then_vs_now": {"kind": "change", "text": "In 1926 this paper came out twice a week. Library of Congress records show it switched to weekly by 1932 and stopped in February 1937.",
                  "source": "Library of Congress catalog record, The Herald and News (Newberry, S.C.) 1903-1937", "url": "https://www.loc.gov/item/sn86063758/"},
  "question": "This page is full of names: who gave money, who is in the play. Why would people in 1926 want to see their names in the paper?"},
 {"date": "1926-12-22", "lccn": "sn92066930", "paper": "The Cody Enterprise and the Park County Herald", "city": "Cody", "state": "WY", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "Contract Let for Cody's Post Office", "family": True},
   {"text": "Rock Slide in Canyon Fills Spillway", "family": True},
   {"text": "Cody Stampede Elects Officers New Year", "family": True},
   {"text": "Cody's Christmas Windows Beautiful", "family": True},
   {"text": "Greybull Ranchers Dispute Ownership of Saddle Horse", "family": True}],
  "spots": [
   {"spot": "A drawing of Buffalo Bill in the masthead, and the note \"Founded in 1899 by Col. W. F. Cody\"", "where": "top center and top left"},
   {"spot": "A Merry Christmas box with a candle and a snowy village", "where": "top center"},
   {"spot": "The 1927 Stampede dates: July 4th, 5th and 6th", "where": "top right"},
   {"spot": "A Christmas greeting from \"The Cody Bronc,\" the students' paper", "where": "bottom center"},
   {"spot": "A court case over who owns a saddle horse", "where": "bottom right"}],
  "then_vs_now": {"kind": "change", "text": "The rock slide hit the spillway of the Shoshone reservoir dam near Cody. In 1946 it was renamed Buffalo Bill Dam, for the 100th anniversary of the birth of Buffalo Bill, who also started this newspaper.",
                  "source": "National Park Service, Wyoming: Buffalo Bill Dam", "url": "https://www.nps.gov/articles/wyoming-buffalo-bill-dam.htm"},
  "question": "Two ranchers went to court over one saddle horse. Why might a horse be worth a court case in 1926 Wyoming?"},
]
PAGES2 += [
 {"date": "1926-12-23", "lccn": "sn85053343", "paper": "The Kevin Review", "city": "Kevin", "state": "MT", "family": "ok", "page_type": "picture",
  "family_note": "",
  "headlines": [
   {"text": "The Kevin Review (a full-page Christmas picture instead of news)", "family": True}],
  "spots": [
   {"spot": "A grandfather reading a book titled \"The Night Before Xmas\" to three children", "where": "center"},
   {"spot": "Santa's sleigh and reindeer flying over snowy rooftops", "where": "top right"},
   {"spot": "Three riders on camels following a star", "where": "very top, left"},
   {"spot": "Toys tumbling from the sky: a drum, a doll, a sailboat", "where": "right side, under the sleigh"},
   {"spot": "A clock on the wall and stockings hanging by the fire", "where": "top left"}],
  "then_vs_now": {"kind": "continuity", "text": "The grandfather is reading \"The Night Before Christmas.\" The poem, first called \"A Visit from St. Nicholas,\" was first published in the Troy Sentinel on December 23, 1823, exactly 103 years before this page.",
                  "source": "Library of Congress, Printed Ephemera Collection record for \"A visit from St. Nicholas\"", "url": "https://www.loc.gov/item/rbpe.11804300/"},
  "question": "This tiny Montana paper used its whole front page for one picture. If you made the front page for Christmas Eve, what would you put on it?"},
]
PAGES2 += [
 {"date": "1926-12-24", "lccn": "sn87093323", "paper": "Vashon Island News-Record", "city": "Vashon", "state": "WA", "family": "care",
  "family_note": "Two short obituaries and a state news roundup that mentions a man who died of burns and a missing fishing boat. The family reunion and Christmas items are the heart of the page.",
  "headlines": [
   {"text": "Magowan Family Christmas Reunion", "family": True},
   {"text": "Condensed Synopsis of Late State News", "family": True},
   {"text": "Community Growth", "family": True},
   {"text": "Rousing Meeting Commercial Club", "family": True},
   {"text": "Island Octogenarian Passes Into Beyond", "family": False}],
  "spots": [
   {"spot": "All the Magowan children coming home for one big Christmas dinner, the first time in many years", "where": "top left"},
   {"spot": "A new electric elevator that will lift 2 1/2 tons 100 feet a minute at a Vancouver dock", "where": "top center"},
   {"spot": "A young deer doe that wandered into town", "where": "top center, state news"},
   {"spot": "A \"Coming Events\" box: list your dates here at no charge", "where": "bottom left"},
   {"spot": "The price in the corner: $2.00 per year", "where": "top right"}],
  "then_vs_now": {"kind": "continuity", "text": "In 1926 people reached Vashon Island by boat. They still do: Washington State Ferries runs routes to Vashon from Fauntleroy in Seattle, from Southworth, and from Point Defiance in Tacoma.",
                  "source": "Washington State Department of Transportation, Washington State Ferries routes", "url": "https://wsdot.wa.gov/travel/washington-state-ferries"},
  "question": "The whole Magowan family is coming home for Christmas for the first time in years. What makes a family reunion news?"},
]
ALTERNATES2 += [
 {"date": "1926-12-24", "lccn": "sn87062055", "paper": "The Coconino Sun", "city": "Flagstaff", "state": "AZ", "family": "no",
  "family_note": "A headline reports a suicide. Adult mode only.",
  "headlines": [{"text": "On Christmas Morn", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1926-12-26", "lccn": "sn96060774", "paper": "Nogales International (Holiday Edition)", "city": "Nogales", "state": "AZ", "family": "ok", "page_type": "picture",
  "family_note": "",
  "headlines": [
   {"text": "Santa Claus' Workshop (a full-page holiday picture)", "family": True},
   {"text": "Holiday Greetings to All", "family": True}],
  "spots": [
   {"spot": "Santa in glasses, smiling as he paints a small wooden toy", "where": "center"},
   {"spot": "A quill pen in an ink pot and a list pinned to the wall", "where": "top left"},
   {"spot": "Tools on the workbench: a hammer, a mug and a vise", "where": "bottom left"},
   {"spot": "The painter's signature: can you read it?", "where": "bottom right corner of the picture"},
   {"spot": "\"Copyright by Western Newspaper Union\"", "where": "under the picture, right"}],
  "then_vs_now": {"kind": "change", "text": "In 1926 this picture was printed with a copyright notice. Today the Library of Congress says U.S. newspapers published more than 95 years ago are in the public domain in their entirety, which is why we can share this page.",
                  "source": "Library of Congress, Chronicling America: Rights and Access", "url": "https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/"},
  "question": "Santa is making toys by hand at a workbench. Where do most toys come from today? What would a 2026 Santa's workshop look like?"},
]
PAGES2 += [
 {"date": "1926-12-27", "lccn": "sn96060765", "paper": "The Winslow Mail", "city": "Winslow", "state": "AZ", "family": "care",
  "family_note": "The lower half has short items about a slaying trial, a train wreck and a house fire. A photo shows a fake \"spirit\" from a seance. Stick to the meteor, the toboggan slide and the spots.",
  "headlines": [
   {"text": "Lowell Observatory at Flagstaff Seeks Data on New Winslow Meteor", "family": True},
   {"text": "Santa Fe Adds New Equipment to Phoenix Train", "family": True},
   {"text": "Flagstaff's New Toboggan Slide Is Nearly Ready", "family": True},
   {"text": "Winslow Gridders on All-Star Squad", "family": True},
   {"text": "Bisbee Cattleman Freed in Slaying", "family": False}],
  "spots": [
   {"spot": "The observatory's list of questions for anyone who saw the meteor: what time, which direction, what color", "where": "top left"},
   {"spot": "A notice that this is the last weekly Winslow Mail, because the daily paper is taking over", "where": "top center"},
   {"spot": "Two portrait photos under the heading \"With Interest\"", "where": "top, second column"},
   {"spot": "Three hundred turkeys from Chino Valley for Fred Harvey Christmas tables", "where": "bottom left"},
   {"spot": "Auto license applications now in order, with plates for 1927", "where": "bottom right"}],
  "then_vs_now": {"kind": "what_next", "text": "Lowell Observatory was asking the public for help tracking a meteor. Just over three years later, in 1930, Clyde Tombaugh discovered Pluto at that same observatory.",
                  "source": "Lowell Observatory, Pluto", "url": "https://lowell.edu/discover/pluto/"},
  "question": "The observatory asked ordinary people what they saw in the sky. Why would scientists want reports from lots of people instead of just one?"},
]
PAGES2 += [
 {"date": "1926-12-28", "lccn": "sn91064030", "paper": "The Pleasantville Press", "city": "Pleasantville", "state": "NJ", "family": "care",
  "family_note": "A few smaller headlines cover an embezzlement arrest, a car crash and an obituary. The rest is cheerful holiday news.",
  "headlines": [
   {"text": "Will Not Hold New Year's Parade in City This Year", "family": True},
   {"text": "Postoffice Has Largest Year in Its History", "family": True},
   {"text": "Boys Have Narrow Escape Christmas", "family": True},
   {"text": "Community Tree Spreads Cheer", "family": True},
   {"text": "Umbrella Sets Bus on Fire", "family": True},
   {"text": "Farnum Charged With Embezzlement", "family": False}],
  "spots": [
   {"spot": "A photo of a man in a cap standing by a car: James Moore, building inspector", "where": "top left"},
   {"spot": "Two boys whose motorboat stopped in the bay, rescued by searchers on Christmas", "where": "top center"},
   {"spot": "A celluloid umbrella handle that caught fire on a bus heater", "where": "top right"},
   {"spot": "Police officers given Christmas gifts by the children", "where": "top, fourth column"},
   {"spot": "\"Keech Captures Lions' Shoot\" with a list of scores", "where": "bottom center"}],
  "then_vs_now": {"kind": "continuity", "text": "Pleasantville dropped its New Year's parade, which copied the big one in Philadelphia. Philadelphia's Mummers Parade held its first official parade on New Year's Day 1901 and is still run by the city today.",
                  "source": "City of Philadelphia Parks and Recreation, The Mummers Parade: A PPR Tradition", "url": "https://www.phila.gov/Newsletters/parksnrecsnewsletter/pdfs/Mummers.pdf"},
  "question": "The town canceled its parade because not enough groups would help. What would it take to get your town to put on a parade?"},
]
PAGES2 += [
 {"date": "1926-12-29", "lccn": "sn92051419", "paper": "Windham County Observer", "city": "Putnam", "state": "CT", "family": "care",
  "family_note": "Two obituaries and a story about a World War veteran, gassed overseas, found dazed by a roadside. The ads, sports and fish story are the fun parts.",
  "headlines": [
   {"text": "Three Teams Tied Now for First Place", "family": True},
   {"text": "Familiar Score Monday Evening", "family": True},
   {"text": "Caught Large Pickerel in Alexander's Lake", "family": True},
   {"text": "Stores Closed All Day New Year's", "family": True},
   {"text": "Morley Is Name of \"Dazed\" Man", "family": False}],
  "spots": [
   {"spot": "\"Happy New Year\" printed on both sides of the masthead", "where": "top corners"},
   {"spot": "A big pickerel caught through the ice", "where": "top center box"},
   {"spot": "The Bugbee Corporation sale: children's dresses $1.69, boys' wool blouses $1.00", "where": "bottom, big ad"},
   {"spot": "Basketball box scores for the Celtics and the Collegians", "where": "right column"},
   {"spot": "A notice that all stores will close on New Year's Day, Saturday, January 1", "where": "middle, boxed"}],
  "then_vs_now": {"kind": "continuity", "text": "Every store in Putnam closed for New Year's Day in 1927. New Year's Day is still a federal holiday today, and it comes first on the government's yearly holiday list.",
                  "source": "U.S. Office of Personnel Management, Federal Holidays", "url": "https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/"},
  "question": "Look at the sale prices in the big ad. Which item would you buy with one dollar, and what can a dollar buy today?"},
]
ALTERNATES2 += [
 {"date": "1926-12-29", "lccn": "sn85025570", "paper": "The Redwood Gazette", "city": "Redwood Falls", "state": "MN", "family": "no",
  "family_note": "A headline about a youth who shot two people. Adult mode only, and only if the owner picked Minnesota.",
  "headlines": [{"text": "Schandera's Death Recalls Days of Pioneer", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1926-12-30", "lccn": "sn83004262", "paper": "The Pocahontas Times", "city": "Marlinton", "state": "WV", "family": "care",
  "family_note": "Headlines report an accident where two men drowned in a creek and a man fatally hurt in a wreck. Stick to the Christmas items, the bear story and the ads.",
  "headlines": [
   {"text": "Community Christmas Tree", "family": True},
   {"text": "County Court", "family": True},
   {"text": "Big Bear", "family": True},
   {"text": "A Christmas Greeting", "family": True},
   {"text": "Awful Accident", "family": False}],
  "spots": [
   {"spot": "A hunters' story about one of the biggest bears ever taken in the county", "where": "top, fourth column"},
   {"spot": "A Christmas Club ad: save from $25.00 to $500.00 for next Christmas", "where": "bottom center"},
   {"spot": "The movie ad for \"Beverly of Graustark\" with Marion Davies, and a Greta Garbo film later in the week", "where": "bottom right"},
   {"spot": "A list of births with dates", "where": "bottom, third column"},
   {"spot": "Someone wrote in pen across the top of this copy", "where": "top right corner"}],
  "then_vs_now": {"kind": "change", "text": "In 1926 a big bear was hunting news in Pocahontas County. In 1973 the West Virginia Legislature made the black bear the official state animal.",
                  "source": "West Virginia State Museum Education, West Virginia State Symbols", "url": "https://wvstatemuseumed.wv.gov/site/state-symbols.html"},
  "question": "The paper prints a whole column just of births, weddings and visitors. What would a page like that look like for your street?"},
]
ALTERNATES2 += [
 {"date": "1926-12-30", "lccn": "sn89064914", "paper": "Askov American", "city": "Askov", "state": "MN", "family": "no",
  "family_note": "A joke at the bottom uses a racial slur. Never shown in family mode.",
  "headlines": [{"text": "News Among Scandinavians", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1926-12-31", "lccn": "sn87062224", "paper": "Milford Chronicle", "city": "Milford", "state": "DE", "family": "care",
  "family_note": "A headline reports a railroad man who lost a leg under a train, and another a runaway horse killed by a train. Stick to the long-life list, the chickens, the Sunday school and the spots.",
  "headlines": [
   {"text": "Long Life Seems Rule Among Sussex People", "family": True},
   {"text": "Milford Poultryman Buys Fancy Chickens", "family": True},
   {"text": "Methodist Episcopal Sunday School Is 100 Years of Age", "family": True},
   {"text": "Ask Legislation to Settle Boundary", "family": True},
   {"text": "Railroad Man Badly Hurt at Harrington", "family": False}],
  "spots": [
   {"spot": "A list of the ages of old residents in Sussex County: many in their 70s, 80s and 90s", "where": "top, second column"},
   {"spot": "Oystermen asking for a law to settle the boundary between Delaware and New Jersey in the bay", "where": "top, fourth column"},
   {"spot": "A drawing of a man in round glasses: the Sunday school superintendent", "where": "top right"},
   {"spot": "A box bragging that there are 12,000 rural weekly papers and the Chronicle is one of the top ones", "where": "top right corner"},
   {"spot": "\"Milford Fire Trucks Are Equipped With Green Lights\"", "where": "bottom right"}],
  "then_vs_now": {"kind": "change", "text": "A Milford man is buying fancy chickens. Three years earlier, in 1923, a Sussex County woman ordered 50 chicks and got 500 by mistake. That mix-up started the modern broiler chicken industry, and Sussex County became the leading broiler county in the nation.",
                  "source": "Sussex County, Delaware, History of Sussex County", "url": "https://sussexcountyde.gov/history"},
  "question": "This paper lists how old people in the county are, as good news. Why might long lives have been big news in 1926?"},
]
ALTERNATES2 += [
 {"date": "1926-12-31", "lccn": "sn86075113", "paper": "The Bozeman Courier", "city": "Bozeman", "state": "MT", "family": "no",
  "family_note": "A large photo of a boat disaster where thirty people drowned. Adult mode only, and only if the owner picked Montana.",
  "headlines": [{"text": "Thirty Drowned in Hudson River Boat Disaster", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1927-01-01", "lccn": "sn82015295", "paper": "The McCarthy Weekly News", "city": "McCarthy", "state": "AK", "family": "care",
  "family_note": "One column reports a new treatment for drug addiction. Skip it with younger readers; the rest is New Year's greetings and local news.",
  "headlines": [
   {"text": "The News Wishes You a Happy New Year", "family": True},
   {"text": "Finds Strange Stone in Turkey's Gizzard", "family": True},
   {"text": "Reindeer Fair at Nome Next March", "family": True},
   {"text": "Steese Gets Promotion", "family": True},
   {"text": "Dope Cure Found", "family": False}],
  "spots": [
   {"spot": "Nine stones found in a Christmas turkey's gizzard: two red, three blue, two purple and two white", "where": "bottom, third column"},
   {"spot": "A Reindeer Fair with reindeer races and dog races planned near Nome", "where": "bottom, second column"},
   {"spot": "\"Pope Takes Rap at Modern Fashions\"", "where": "middle, second column"},
   {"spot": "The Kennecott movies: Syd Chaplin in \"The Man on the Box\" and Marion Davies in \"The Lights of Old Broadway\"", "where": "bottom, third column"},
   {"spot": "The big masquerade at Kennecott tonight", "where": "bottom left"}],
  "then_vs_now": {"kind": "change", "text": "The Nome Reindeer Fair would feature reindeer races. Reindeer herding was new on the Seward Peninsula then: reindeer had been imported from Siberia, and young Inupiaq men were trained to manage the herds.",
                  "source": "National Park Service, Bering Land Bridge: Alaska Natives and Early People", "url": "https://www.nps.gov/bela/learn/historyculture/alaska-natives-and-early-people.htm"},
  "question": "Mrs. Barrett thinks the colored stones from the turkey might be precious. What would you do to find out?"},
]
ALTERNATES2 += [
 {"date": "1927-01-01", "lccn": "sn86076141", "paper": "Las Vegas Age", "city": "Las Vegas", "state": "NV", "family": "no",
  "family_note": "A headline reports a suicide and another a man who shot himself. Adult mode only, and only if the owner picked Nevada.",
  "headlines": [{"text": "Burglars Enter Two Las Vegas Stores", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1927-01-02", "lccn": "sn96060774", "paper": "Nogales International", "city": "Nogales", "state": "AZ", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "Good Year Forecast for Nogales", "family": True},
   {"text": "Paved Streets to Be Reality This Year", "family": True},
   {"text": "Big Year Predicted for City of Nogales by Prominent Men", "family": True},
   {"text": "Popper-Roaster Left by Santa", "family": True},
   {"text": "Local People to Make World Tour", "family": True}],
  "spots": [
   {"spot": "A Happy New Year banner with a baby in goggles flying an airplane", "where": "very top"},
   {"spot": "The cartoon \"Ships that Pass in the Night\": a 1926 ship sails off as a 1927 baby waves", "where": "top center"},
   {"spot": "Santa left a popcorn popper and peanut roaster at a candy shop", "where": "bottom, fifth column"},
   {"spot": "Two baby New Year drawings wishing success and bounty in 1927", "where": "bottom corners"},
   {"spot": "A list of health \"Don'ts\" for the holidays", "where": "top left column"}],
  "then_vs_now": {"kind": "continuity", "text": "The \"Line or Two\" column quotes George Bernard Shaw grumbling about Christmas shopping. He had just won the 1925 Nobel Prize in Literature, a prize the Nobel Foundation still awards today.",
                  "source": "Nobel Foundation, The Nobel Prize in Literature 1925", "url": "https://www.nobelprize.org/prizes/literature/1925/summary/"},
  "question": "Everyone on this page predicts a great 1927. What is one prediction you would make for next year?"},
]
ALTERNATES2 += [
 {"date": "1927-01-03", "lccn": "sn94050047", "paper": "Hyder Weekly Herald", "city": "Hyder", "state": "AK", "family": "no",
  "family_note": "A story about a costume party uses racial slurs. Never shown in family mode.",
  "headlines": [{"text": "Mineral Production in Alaska in 1926", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
ALTERNATES2 += [
 {"date": "1927-01-03", "lccn": "sn82016181", "paper": "The Washington Daily News", "city": "Washington", "state": "DC", "family": "no",
  "family_note": "Headlines about a suicide and a murdered bride. Adult mode only.",
  "headlines": [{"text": "Kellogg Cancels Date With Press for Foreign Quiz", "family": False}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1927-01-04", "lccn": "sn91064030", "paper": "The Pleasantville Press", "city": "Pleasantville", "state": "NJ", "family": "ok",
  "family_note": "",
  "headlines": [
   {"text": "Spirit of Mainland Progress Shown in Inaugurals", "family": True},
   {"text": "Adequate Police and Fire Protection Urged by Jackson", "family": True},
   {"text": "Need of City Hall at Absecon Pointed Out by Mayor Mattson", "family": True},
   {"text": "Swilkey Hits Prohibition Act in Message", "family": True},
   {"text": "Brown Urges New Borough Hall for Linwood", "family": True}],
  "spots": [
   {"spot": "Two lines of type printed upside down in the story about Officer McGhee, the school crossing guard", "where": "bottom, third column"},
   {"spot": "The word TWICE A WEEK in a box: how often this paper came out", "where": "top right corner"},
   {"spot": "Ads asking \"Know Your Coal\" and selling coal to heat homes", "where": "bottom right"},
   {"spot": "Five towns swearing in new mayors and councils on the same page", "where": "top half"},
   {"spot": "The price: three cents", "where": "under the name, right side"}],
  "then_vs_now": {"kind": "change", "text": "Coal dealers advertise all over this page because many homes burned coal for heat. The U.S. Energy Information Administration says coal was once common in homes, but today its main use in the United States is to make electricity.",
                  "source": "U.S. Energy Information Administration, Use of coal", "url": "https://www.eia.gov/energyexplained/coal/use-of-coal.php"},
  "question": "If you were a new mayor, what is the first thing you would fix in your town?"},
]
PAGES2 += [
 {"date": "1927-01-05", "lccn": "sn89081022", "paper": "Willmar Tribune", "city": "Willmar", "state": "MN", "family": "care",
  "family_note": "Skip three short items: two horses killed by a freight train, a death notice, and a man burned in an explosion. The cartoon jokes about undertakers and doctors on an icy street.",
  "headlines": [
   {"text": "Willmar Banks in Good Condition", "family": True},
   {"text": "First Debate of Season on Monday", "family": True},
   {"text": "New Directory Just Issued", "family": True},
   {"text": "Poultry Show Here Next Week", "family": True},
   {"text": "Lost Two Horses When Struck by R. R. Freight", "family": False}],
  "spots": [
   {"spot": "A cartoon of people slipping and sliding on an icy Litchfield Avenue last Monday morning", "where": "bottom center"},
   {"spot": "The debate question: should there be a Federal Department of Education?", "where": "top, fifth column"},
   {"spot": "A box telling readers to watch the date stamp on their paper", "where": "top left corner"},
   {"spot": "A list of births with dates in late December", "where": "bottom, third column"},
   {"spot": "The words DEFECTIVE PAGE stamped when the page was put on microfilm", "where": "very bottom"}],
  "then_vs_now": {"kind": "what_next", "text": "Willmar High School debated whether America should have a Federal Department of Education. Congress created one in the Department of Education Organization Act of October 17, 1979, and it began work on May 4, 1980.",
                  "source": "National Archives, General Records of the Department of Education (Record Group 441)", "url": "https://www.archives.gov/research/guide-fed-records/groups/441.html"},
  "question": "Should the country have a Department of Education? Pick a side and give one reason, like the Willmar debaters."},
]
PAGES2 += [
 {"date": "1927-01-06", "lccn": "sn86075298", "paper": "The Ronan Pioneer", "city": "Ronan", "state": "MT", "family": "care",
  "family_note": "Skip one short item about a businessman found dead in a hotel room. Nothing graphic.",
  "headlines": [
   {"text": "Lake County Takes a Big Lead in the Dairy Industry", "family": True},
   {"text": "Lake County Passes Into the Hands of New Set of Officials", "family": True},
   {"text": "Moiese and Round Butte Will Protest District Division", "family": True},
   {"text": "Sheep on Flathead Are Wintering Well", "family": True},
   {"text": "Farmers of Lake and Sanders Sell $25,000 Worth of Turkeys", "family": True}],
  "spots": [
   {"spot": "Two boxes bragging \"Ronan, the Best Town on the Flathead\" and \"Flathead, Garden of the Rockies\"", "where": "top corners"},
   {"spot": "The town calls itself the geographic center of the Flathead Reservation", "where": "under the name"},
   {"spot": "A notice that you need your 1926 receipt to get new 1927 license plates", "where": "bottom right"},
   {"spot": "A P.T.A. dance to raise money for the school", "where": "bottom, third column"},
   {"spot": "A boys' and girls' basketball double-header", "where": "bottom right corner"}],
  "then_vs_now": {"kind": "change", "text": "Moiese, in one of today's headlines, is home to the National Bison Range, set up in 1908. In June 2021 the Interior Department transferred its lands to be held in trust for the Confederated Salish and Kootenai Tribes of the Flathead Reservation.",
                  "source": "U.S. Department of the Interior press release, June 23, 2021", "url": "https://www.doi.gov/pressreleases/interior-transfers-national-bison-range-lands-trust-confederated-salish-and-kootenai"},
  "question": "Ronan calls itself the best town on the Flathead. What slogan would you write for your town?"},
]
ALTERNATES2 += [
 {"date": "1927-01-07", "lccn": "sn90051693", "paper": "The Guernsey Gazette", "city": "Guernsey", "state": "WY", "family": "no",
  "family_note": "A headline about a man burned to death in his cabin, with details of the body. Adult mode only. Fun note: the masthead misprints the year as 1926.",
  "headlines": [{"text": "Haystack Game Preserve", "family": True}], "spots": [], "then_vs_now": None, "question": ""},
]
PAGES2 += [
 {"date": "1927-01-07", "lccn": "sn92067173", "paper": "Thermopolis Independent", "city": "Thermopolis", "state": "WY", "family": "care",
  "family_note": "Short death notices in the middle columns, including an infant. Nothing graphic, but skip them with younger kids.",
  "headlines": [
   {"text": "Independent Installs Big Model 26 Linotype", "family": True},
   {"text": "Flying School to Be Located in Thermop", "family": True},
   {"text": "Baby Show at the Whiting", "family": True},
   {"text": "Thermopolis Wins Over Lander Here", "family": True},
   {"text": "Independent Starts on Its 21st Year", "family": True}],
  "spots": [
   {"spot": "Lines that say \"Independent Want Ads Pay!\" over and over in different type styles, to show off the new machine", "where": "top left"},
   {"spot": "A drawing of the Linotype machine", "where": "bottom left"},
   {"spot": "A story about a man who caught a possum", "where": "bottom, second column"},
   {"spot": "A bank report with every dollar listed", "where": "bottom right"},
   {"spot": "Number 1 next to the date: the first issue of the paper's new year", "where": "top right, under the name"}],
  "then_vs_now": {"kind": "change", "text": "The Linotype cast whole lines of type from hot metal. The Library of Congress explains that when computers came into printing in the 1960s, they were called cold type, and hot type faded away.",
                  "source": "Library of Congress, Headlines and Heroes blog, The Linotype: The Machine that Revolutionized Movable Type", "url": "https://blogs.loc.gov/headlinesandheroes/2022/06/the-linotype-the-machine-that-revolutionized-movable-type/"},
  "question": "The paper was proud of its new machine. What new machine would you show off on a front page?"},
]

PAGES2 += [
 {"date": "1927-01-03", "lccn": "sn84037526", "paper": "St. Croix Avis", "city": "Christiansted", "state": "VI", "family": "care",
  "family_note": "A police notice says dogs without a 1927 tag can be caught, and put down if no owner claims them. Easy to skip.",
  "headlines": [
   {"text": "Christiansted Theatre: The Iron Man, Monday Night 8.15", "family": True},
   {"text": "Publication from the Police: dog tags for 1927", "family": True},
   {"text": "Horse, Carriage and Boat Taxes Due", "family": True},
   {"text": "Eveready Flashlights Turn Night Into Day", "family": True},
   {"text": "Sensational Sale of Marathon Flexhide Belts", "family": True}],
  "spots": [
   {"spot": "Prices in francs (Frcs.), money left over from when the islands were Danish", "where": "police notices, top half"},
   {"spot": "V. I. U. S. A., short for Virgin Islands, U.S.A., next to the date", "where": "under the name"},
   {"spot": "A taxes list for horses, carriages and boats, and another for cars", "where": "middle and right columns"},
   {"spot": "A flashlight that shines 1,000 to 1,500 feet, sold at an ice cream parlor", "where": "bottom center"},
   {"spot": "A movie serial, The Iron Man, continued from last time", "where": "top center"}],
  "then_vs_now": {"kind": "continuity", "text": "Christiansted's Danish-era waterfront buildings became Christiansted National Historic Site in 1952, the first National Park Service unit in the Virgin Islands. You can still visit them.",
                  "source": "National Park Service, Christiansted National Historic Site", "url": "https://www.nps.gov/chri/index.htm"},
  "question": "This paper paid in francs, sold belts at an ice cream parlor, and taxed boats. Which detail surprises you most?"},
]
ALTERNATES2 += [
 {"date": "1927-01-03", "lccn": "2022239700", "paper": "The Cordele Dispatch", "city": "Cordele", "state": "GA", "family": "no",
  "family_note": "War headlines describing a bloody battle and human butchery. Adult mode only.",
  "headlines": [{"text": "Quake Cities Build While Earth Still Trembles", "family": True}], "spots": [], "then_vs_now": None, "question": ""},
 {"date": "1927-01-03", "lccn": "sn87062169", "paper": "Seward Daily Gateway", "city": "Seward", "state": "AK", "family": "no",
  "family_note": "A race riot story and a gangster found with bullet holes in his skull. Adult mode only. Also has the Stanford and Alabama 7-7 Rose Bowl tie.",
  "headlines": [{"text": "Stanford, Alabama Play 7-7 Tie Game at Pasadena Annual New Year's Classic", "family": True}], "spots": [], "then_vs_now": None, "question": ""},
 {"date": "1927-01-03", "lccn": "sn92070146", "paper": "Imperial Valley Press", "city": "El Centro", "state": "CA", "family": "no",
  "family_note": "Headlines about suicides and an infant killed. Adult mode only.",
  "headlines": [{"text": "Calexico Resumes Business", "family": True}], "spots": [], "then_vs_now": None, "question": ""},
]
