"""Hand-curated content for each front page. Every headline and spot below was read
off the page image (not the OCR) during the Nov 24, 2026 build. Facts carry a source URL.
family: ok = nothing a parent must explain in the big headlines or photos;
        care = a big headline is about crime, death, disaster or scandal (bot stays on the spots, adds a parent note);
        no = never shown in family mode (graphic violence, lynching, slurs, racist caricature in a lead story or picture)."""

LOC_RIGHTS_URL = 'https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/'

PAGES = [
 {'date': '1926-11-24', 'lccn': 'sn83045462', 'paper': 'Evening Star', 'city': 'Washington', 'state': 'DC', 'family': 'care',
  'family_note': 'The left column is about a famous murder trial. Stick to the spots below.',
  'headlines': [
   {'text': 'U.S. Gives Mexico Final Warning on Retroactive Laws', 'family': True},
   {'text': 'U.S. Would Share Thanksgiving Day', 'family': True},
   {'text': 'Queen Lauds U.S. on Eve of Sailing', 'family': True},
   {'text': 'Defense Attacks Hall-Mills Story of "Pig Woman"', 'family': False}],
  'spots': [
   {'spot': 'A cartoon goat labeled "Third Party" holding a sign that says "Tomorrow is Thanksgiving Day"', 'where': 'top center'},
   {'spot': 'The price of the paper: two cents', 'where': 'top right, under the name'},
   {'spot': 'A hiker marooned on a ledge for 3 days and saved by a boat crew', 'where': 'middle, center'},
   {'spot': 'An English village with twenty golden weddings in one month', 'where': 'top right'},
   {'spot': 'The weather box: lowest temperature tonight about 36 degrees', 'where': 'top left corner'}],
  'then_vs_now': {'kind': 'change', 'text': 'The Evening Star was Washington\'s big afternoon paper in 1926. It closed for good on August 7, 1981, with "FINAL EDITION" across its front page.',
                  'source': 'Library of Congress, About Evening Star', 'url': 'https://www.loc.gov/item/sn83045462/'},
  'question': 'Queen Marie of Romania was sailing home after a visit to America. If a queen visited your town, where would you take her first?'},

 {'date': '1926-11-25', 'lccn': 'sn82015313', 'paper': 'The Indianapolis Times', 'city': 'Indianapolis', 'state': 'IN', 'family': 'care',
  'family_note': 'A few crime stories sit in the bottom half. The top half is all Thanksgiving.',
  'headlines': [
   {'text': 'City Gives Thanks for Past Year', 'family': True},
   {'text': 'Technical H.S. Students Aid With Family Dinners', 'family': True},
   {'text': 'Two Planes Will Resume Broken Trip', 'family': True},
   {'text': 'Quiet Holiday at White House', 'family': True}],
  'spots': [
   {'spot': 'Two high school students in white caps holding the pies they baked for family Thanksgiving dinners', 'where': 'top, left of center'},
   {'spot': 'A short story headlined "Roaster, Bird and All Gone" about a family\'s missing Thanksgiving turkey', 'where': 'middle right, in a box'},
   {'spot': 'A cartoon box: "25 Shopping Days Till Christmas"', 'where': 'bottom left'},
   {'spot': 'Two different prices for the paper, one for inside Marion County and one for outside', 'where': 'top right, under the name'},
   {'spot': 'The forecast: "Unsettled with rain tonight and Friday"', 'where': 'top right corner'}],
  'then_vs_now': {'kind': 'change', 'text': 'In 1926 Thanksgiving fell on the last Thursday of November, a custom since Lincoln\'s 1863 proclamation. Since a law President Roosevelt signed on December 26, 1941, it has been the fourth Thursday.',
                  'source': 'National Archives, Congress Establishes Thanksgiving', 'url': 'https://www.archives.gov/legislative/features/thanksgiving'},
  'question': 'These students baked pies for families who needed a holiday dinner. What could your family make or share with someone this year?'},

 {'date': '1926-11-26', 'lccn': 'sn85042243', 'paper': 'The Bismarck Tribune', 'city': 'Bismarck', 'state': 'ND', 'family': 'care',
  'family_note': 'The big banner is about deadly tornadoes in the South. The spots stay on football and a royal wedding.',
  'headlines': [
   {'text': 'Windy City Is Preparing for Army-Navy Mix', 'family': True},
   {'text': 'Royal Marriage Completed', 'family': True},
   {'text': 'Gov. Sorlie Tells East About N.D.', 'family': True},
   {'text': 'Tornadoes Bring Death and Destruction', 'family': False}],
  'spots': [
   {'spot': '"110,000 Will See Game": the crowd expected for the Army-Navy football game in Chicago', 'where': 'top left column'},
   {'spot': 'A royal wedding photo: Belgium\'s crown prince and princess walking under a canopy of crossed swords', 'where': 'center'},
   {'spot': 'The silver service of the battleship North Dakota going on display', 'where': 'top, second column'},
   {'spot': 'A notice that the Army-Navy game will be broadcast', 'where': 'bottom right of the top half'},
   {'spot': 'The price: five cents, and the words "Final Edition"', 'where': 'top right'}],
  'then_vs_now': {'kind': 'what_next', 'text': 'What happened next: the next day Army and Navy played to a 21 to 21 tie at Chicago\'s Soldier Field, before a crowd reported at more than 110,000.',
                  'source': 'Seward Daily Gateway, Nov 29, 1926, front page (Library of Congress)', 'url': 'https://www.loc.gov/resource/sn87062169/1926-11-29/ed-1/?sp=1'},
  'question': 'More than 110,000 people came to one football game. What is the biggest crowd you have ever been part of?'},

 {'date': '1926-11-27', 'lccn': 'sn84020657', 'paper': 'The Alaska Daily Empire', 'city': 'Juneau', 'state': 'AK', 'family': 'care',
  'family_note': 'The banner is about liquor smuggling during Prohibition, and one small story is about a murder trial in England.',
  'headlines': [
   {'text': 'Liquor Smuggling Investigated', 'family': True},
   {'text': 'Here\'s Barber, Parson, Legislator', 'family': True},
   {'text': 'Manufacturer of Rifles Is Dead, Belgium', 'family': True},
   {'text': 'No Unwritten Law, England', 'family': False}],
  'spots': [
   {'spot': 'A photo of a preacher who was also a barber, cutting a man\'s hair. He had just been elected to his state legislature', 'where': 'top, left of center'},
   {'spot': 'The paper\'s motto: "All the News All the Time"', 'where': 'under the name'},
   {'spot': 'A story about an armed fleet being urged to stop smuggling ships from Canada', 'where': 'top right'},
   {'spot': 'The date line: Juneau, Alaska, Saturday, November 27, 1926', 'where': 'under the name'}],
  'then_vs_now': {'kind': 'change', 'text': 'In 1926 making and selling alcohol was against national law (Prohibition). That ended on December 5, 1933, when the 21st Amendment was ratified.',
                  'source': 'US House History, Art and Archives, Ratification of the Twenty-first Amendment', 'url': 'https://history.house.gov/Historical-Highlights/1901-1950/1932_12_05_Twenty-first_Amendment/'},
  'question': 'This man was a barber, a preacher and a lawmaker all at once. Which three jobs would you want to do at the same time?'},

 {'date': '1926-11-28', 'lccn': 'sn96060774', 'paper': 'Nogales International', 'city': 'Nogales', 'state': 'AZ', 'family': 'care',
  'family_note': 'One story in the bottom half is about a convict sentenced to hang.',
  'headlines': [
   {'text': 'S.P. Line Near Completion', 'family': True},
   {'text': '1926-27 Basketball Schedule Announced', 'family': True},
   {'text': 'Thanksgiving Motorcade Biggest Ever Held Nogales to Tucson', 'family': True},
   {'text': 'Henry O\'Toole Mentioned for Position on All State Team', 'family': True}],
  'spots': [
   {'spot': 'The price and size: 5 cents a copy, 8 pages', 'where': 'under the name'},
   {'spot': 'A photo of the opera star Mary Garden standing beside a big bunch of flowers', 'where': 'top, left of center'},
   {'spot': 'Fourteen games on the schedule of the Nogales Apaches high school team', 'where': 'top left column'},
   {'spot': 'A banner promise: "Nogales Must and Will Have Paved Streets in 1927"', 'where': 'very bottom'},
   {'spot': 'A little cartoon counting down: 23 days left to shop', 'where': 'bottom right'}],
  'then_vs_now': {'kind': 'change', 'text': 'On Thanksgiving 1926, a record 600 to 750 people drove from Nogales to Tucson for a high school football game. Today Interstate 19 links the two cities, 63.37 miles from end to end.',
                  'source': 'Federal Highway Administration, Route Log and Finder List, Table 1', 'url': 'https://www.fhwa.dot.gov/planning/national_highway_system/interstate_highway_system/routefinder/table01.cfm'},
  'question': 'The town wanted paved streets in 1927. What is one thing you would want your town to build next year?'},

 {'date': '1926-11-29', 'lccn': 'sn87062169', 'paper': 'Seward Daily Gateway', 'city': 'Seward', 'state': 'AK', 'family': 'care',
  'family_note': 'The right column covers a murder trial. Stick to the spots below.',
  'headlines': [
   {'text': 'Army and Navy Battle to Tie in Great Game', 'family': True},
   {'text': 'Women Will Rule All Business, 20 Years', 'family': True},
   {'text': 'Aimee McPherson Plans Start Weekly Paper', 'family': True},
   {'text': 'Davis Enters Pleas Guilty of Disposing Securities Cheaply', 'family': True}],
  'spots': [
   {'spot': 'The price: ten cents', 'where': 'top right'},
   {'spot': '"Largest crowd in history of American football sees gridiron battle"', 'where': 'top, second column'},
   {'spot': 'A British publicist predicting women will run business within 20 years', 'where': 'center'},
   {'spot': 'A boxed story about a preacher planning to start her own newspaper', 'where': 'top center, dotted box'}],
  'then_vs_now': {'kind': 'change', 'text': 'In 1926 Alaska was a US territory, not a state. It became the 49th state on January 3, 1959.',
                  'source': 'National Archives, Proclamation 3269', 'url': 'https://www.archives.gov/federal-register/codification/proclamations/03269.html'},
  'question': 'In 1926 someone predicted women would run business within 20 years. Make your own prediction: what will be different 20 years from now?'},

 {'date': '1926-11-30', 'lccn': 'sn82014519', 'paper': 'New Britain Herald', 'city': 'New Britain', 'state': 'CT', 'family': 'care',
  'family_note': 'Several headlines cover a murder trial and a missing-person case. Stick to the spots below.',
  'headlines': [
   {'text': 'Four New Britain Athletes Win Fordham Grid Letter', 'family': True},
   {'text': 'Al Smith Signs Name on Hard Boiled Egg for Kensington Boy', 'family': True},
   {'text': 'Tilson Is Outspoken in His Hope That Insurgent Republicans Will Return to Fold of the Old Party', 'family': True},
   {'text': 'One of State\'s Own Witnesses on Stand Says That Mrs. Gibson Has Bad Reputation for Truthfulness', 'family': False}],
  'spots': [
   {'spot': 'Governor Al Smith signing his name on a hard boiled egg for a college student', 'where': 'bottom left of the top half'},
   {'spot': 'Average daily circulation for the week: 14,027', 'where': 'top right box'},
   {'spot': 'The size and price: twenty pages, three cents', 'where': 'under the name'},
   {'spot': 'Four local athletes earning their football letters at Fordham', 'where': 'middle left'}],
  'then_vs_now': {'kind': 'change', 'text': 'Al Smith was governor of New York in 1926. In 1928 he became the first Catholic nominated for president by a major party.',
                  'source': 'Gilder Lehrman Center, Yale, Alfred Emanuel Smith', 'url': 'https://macmillan.yale.edu/glc/smith-alfred-emanuel-1873-1944'},
  'question': 'Someone asked a governor to sign an egg. If you could get a famous person to sign anything, what would you pick?'},

 {'date': '1926-12-01', 'lccn': 'sn92070146', 'paper': 'Imperial Valley Press', 'city': 'El Centro', 'state': 'CA', 'family': 'care',
  'family_note': 'Two small stories cover a robbery and a murder trial.',
  'headlines': [
   {'text': 'Imperial Valley Mid-Winter Fair Opens Gates Today', 'family': True},
   {'text': 'Government Declines to Coerce Chinese', 'family': True},
   {'text': 'Court of Honor for Boy Scouts Well Attended', 'family': True},
   {'text': 'Middle West to Have Cold Wave', 'family': True}],
  'spots': [
   {'spot': 'A photo titled "It Still Rings": an old bell hanging in a wooden frame', 'where': 'top center'},
   {'spot': 'The paper\'s motto: "Covers the Valley Like the Sunshine"', 'where': 'under the name'},
   {'spot': 'Troop 14 winning a prize for having the most visitors', 'where': 'top, third column'},
   {'spot': 'A banner inviting readers to the Mid-Winter Fair at Brawley', 'where': 'very bottom'},
   {'spot': 'The price: five cents', 'where': 'top right'}],
  'then_vs_now': {'kind': 'continuity', 'text': 'The Imperial Valley Press is still published today. The Library of Congress lists it from 1907 to the present.',
                  'source': 'Library of Congress, About Imperial Valley Press', 'url': 'https://www.loc.gov/item/sn92070146/'},
  'question': 'The fair opened today in 1926. What would you enter in a county fair: a cake, an animal, a drawing, or something else?'},

 {'date': '1926-12-02', 'lccn': 'sn82014248', 'paper': 'Daily Kennebec Journal', 'city': 'Augusta', 'state': 'ME', 'family': 'care',
  'family_note': 'One top headline is about a murder trial. Stick to the spots below.',
  'headlines': [
   {'text': 'Aroostook Bids Godspeed to Sen.-Elect A. R. Gould', 'family': True},
   {'text': '100th Date of Church in Litchfield', 'family': True},
   {'text': 'Bull Rages in Streets of Dallas in Lieu of China Shop', 'family': True},
   {'text': 'Cautions Congress to Keep Radio Laws Free From Politics', 'family': True},
   {'text': 'Deny Move for Mistrial Hall-Mills', 'family': False}],
  'spots': [
   {'spot': 'A bull loose in the streets of Dallas', 'where': 'top center'},
   {'spot': '"Gov. Nellie Ross Tells Women Power They Are in Politics"', 'where': 'bottom right'},
   {'spot': 'A car ad for a 1925 Packard Sedan', 'where': 'bottom right corner'},
   {'spot': 'Black cats favored by the crew of a freighter, the San Pablo', 'where': 'bottom center'},
   {'spot': 'The price: three cents', 'where': 'top right'}],
  'then_vs_now': {'kind': 'change', 'text': 'Nellie Tayloe Ross of Wyoming was the first woman to serve as a US state governor, sworn in on January 5, 1925. In 1933 she became the first woman to direct the US Mint, and she led it until 1953.',
                  'source': 'WyoHistory.org, Nellie Ross; US Mint, Former Directors', 'url': 'https://www.wyohistory.org/encyclopedia/nellie-ross',
                  'url2': 'https://www.usmint.gov/about/leadership/former-directors'},
  'question': 'Nellie Ross was the first woman governor. What is something you would like to be the first to do?'},

 {'date': '1926-12-03', 'lccn': 'sn92073229', 'paper': 'The Chapel Hill Weekly', 'city': 'Chapel Hill', 'state': 'NC', 'family': 'ok',
  'family_note': '',
  'headlines': [
   {'text': 'Committee Postpones Decision on Stadium Site; Will Meet Monday to Say the Final Word', 'family': True},
   {'text': 'Village Must Have a Better Phone System', 'family': True},
   {'text': 'A Clavilux Recital', 'family': True},
   {'text': 'Christmas Seals to Be Put on Sale Wednesday', 'family': True}],
  'spots': [
   {'spot': 'University squirrels running along the electric and telephone wires', 'where': 'bottom right ("Squirrels Travel by Wire")'},
   {'spot': 'The price: $1.50 a year in advance, or 5 cents a copy', 'where': 'top right'},
   {'spot': 'A high school football championship: Sanford vs. Charlotte', 'where': 'bottom center'},
   {'spot': 'A light-art concert on a "clavilux", an instrument played with light instead of sound', 'where': 'top, fourth column'},
   {'spot': 'The village phone exchange outgrowing its switchboard', 'where': 'top right column'}],
  'then_vs_now': {'kind': 'change', 'text': 'The stadium the committee was arguing about became Kenan Stadium. Construction began in November 1926 and the first game was played there on November 12, 1927. The Tar Heels still play there.',
                  'source': 'UNC Athletics, Kenan Stadium', 'url': 'https://goheels.com/facilities/kenan-stadium/159'},
  'question': 'The whole town needed a bigger phone system. How many different ways can your family send a message today?'},

 {'date': '1926-12-04', 'lccn': 'sn84026749', 'paper': 'The Washington Times', 'city': 'Washington', 'state': 'DC', 'family': 'care',
  'family_note': 'The biggest headline is about a murder trial. Stick to the spots below.',
  'headlines': [
   {'text': 'Taliaferro to Take Oath of Office Today', 'family': True},
   {'text': 'Robinson Gives Veiled War Scare Details', 'family': True},
   {'text': 'Littlepage Seen As New D.C. "Boss"', 'family': True},
   {'text': 'Hall Charges Quashed Over Simpson\'s Protest', 'family': False}],
  'spots': [
   {'spot': 'A photo of the new city commissioner being congratulated, with his wife beside him', 'where': 'top left'},
   {'spot': 'A little clock drawing in the weather box', 'where': 'top left corner'},
   {'spot': 'The words "Home Edition" in a black box', 'where': 'top right'},
   {'spot': 'A photo headlined "Why Shouldn\'t She Smile?"', 'where': 'middle'}],
  'then_vs_now': {'kind': 'change', 'text': 'In 1926 Washington, DC was run by commissioners the President appointed. Since the Home Rule Act of 1973, DC residents elect their own mayor and a 13-member council.',
                  'source': 'Congressional Research Service, IF12577', 'url': 'https://www.congress.gov/crs_external_products/IF/HTML/IF12577.html'},
  'question': 'Back then the people of Washington could not vote for their own city leaders. Why do you think voting for local leaders matters?'},

 {'date': '1926-12-05', 'lccn': 'sn84020645', 'paper': 'The Montgomery Advertiser', 'city': 'Montgomery', 'state': 'AL', 'family': 'care',
  'family_note': 'The bottom half has crime stories and a short item about the Ku Klux Klan. Stick to the top half.',
  'headlines': [
   {'text': 'State Strong Box Is Tapped for Education', 'family': True},
   {'text': 'Million Dollar Theater Seen in Officials\' Visit', 'family': True},
   {'text': 'Montgomery Post Office Building Outlook Brighter', 'family': True},
   {'text': 'Brother and Sister Take First Vacation at Ages of 76 and 77', 'family': True}],
  'spots': [
   {'spot': 'A giant cartoon, "Old Santy Is a Mighty Busy Body", packed with little scenes. Can you find the word "California"?', 'where': 'center'},
   {'spot': 'The size and price: 46 pages, 5 cents', 'where': 'top right'},
   {'spot': 'A brother and sister taking their first vacation ever, at ages 76 and 77', 'where': 'bottom center'},
   {'spot': 'Plans for a new million-dollar movie theater', 'where': 'top, third column'}],
  'then_vs_now': {'kind': 'change', 'text': 'The post office story quotes Congressman Lister Hill. He later served in the US Senate, and in 1946 co-sponsored the Hill-Burton Act, which paid for new hospitals across the country.',
                  'source': 'Encyclopedia of Alabama, Hill-Burton Act', 'url': 'https://encyclopediaofalabama.org/article/hill-burton-act/',
                  'url2': 'https://history.house.gov/People/Detail/15026'},
  'question': 'A brother and sister took their first vacation in their seventies. Where would you go on your very first vacation if you could pick anywhere?'},

 {'date': '1926-12-06', 'lccn': 'sn86092280', 'paper': 'The Elkins Inter-Mountain', 'city': 'Elkins', 'state': 'WV', 'family': 'care',
  'family_note': 'Two headlines are about a reform school and a robbery.',
  'headlines': [
   {'text': 'Congress Begins Session With Mass of Incompleted and New Legislation', 'family': True},
   {'text': 'Elks\' Memorial Held Yesterday', 'family': True},
   {'text': 'D. & E. and W. V. U. Game Settled', 'family': True},
   {'text': 'Father Corcoran Talks at Chapel', 'family': True}],
  'spots': [
   {'spot': 'A photo titled "Growing Up": a little boy in a big buttoned coat and cap', 'where': 'top center'},
   {'spot': 'A banner across the very top inviting people to a church mission, December 6 to 10', 'where': 'very top'},
   {'spot': 'The price: single copy three cents', 'where': 'top right'},
   {'spot': 'A small snowy drawing in the weather box, next to a forecast of "rain or snow"', 'where': 'top left corner'}],
  'then_vs_now': {'kind': 'change', 'text': 'Congress used to open its final session in December, after the election, with many members already voted out (a "lame duck" session). The 20th Amendment, ratified in 1933, moved the start of a new Congress to January 3.',
                  'source': 'US House History, Art and Archives, The Twentieth Amendment', 'url': 'https://history.house.gov/HistoricalHighlight/Detail/35272'},
  'question': 'Congress came back with a "mass" of unfinished work. What is one unfinished thing you would like to finish this month?'},

 {'date': '1926-12-07', 'lccn': 'sn87055779', 'paper': 'South Bend News-Times', 'city': 'South Bend', 'state': 'IN', 'family': 'care',
  'family_note': 'The left column is about a murder case. Stick to the spots below.',
  'headlines': [
   {'text': 'Walsh Moves to Oust Maine Solon', 'family': True},
   {'text': 'Seven Ice-Locked Ships Are Freed; 120 Still Caught', 'family': True},
   {'text': 'Fall Will Face Another Trial for Conspiracy', 'family': True},
   {'text': 'Storm to Abate', 'family': True}],
  'spots': [
   {'spot': 'A big Santa cartoon: "Do Your Christmas Shopping Now!" with four reasons listed', 'where': 'center'},
   {'spot': 'Ships trapped in ice near Sault Ste. Marie, Michigan: 7 freed, 120 still stuck', 'where': 'top right'},
   {'spot': 'The size: 24 pages, in two parts', 'where': 'top left box and under the name'},
   {'spot': 'Monday\'s paid circulation: 27,524', 'where': 'top right box'}],
  'then_vs_now': {'kind': 'change', 'text': 'In 1926, ships could be caught by early ice near the Soo Locks. Today the locks close on purpose each winter for repairs: in 2026 they closed on January 15 and reopened on March 25.',
                  'source': 'US Army Corps of Engineers, Soo Locks to open for 2026 shipping season', 'url': 'https://www.lrd.usace.army.mil/News/News-Releases/Article/4429668/soo-locks-to-open-for-2026-shipping-season/'},
  'question': 'The cartoon says shop early for "less congestion." What does congestion mean, and where do you see it today?'},
]

ALTERNATES = [
 {'date': '1926-11-29', 'lccn': 'sn86063730', 'paper': 'Brownsville Herald', 'city': 'Brownsville', 'state': 'TX', 'family': 'no',
  'family_note': 'Lead story and two others describe killings. Adult mode only, and only if the owner picked Texas.',
  'headlines': [{'text': '$6,000,000 Road Bond Election Is Called Today', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
 {'date': '1926-12-03', 'lccn': 'sn83045293', 'paper': 'The Milwaukee Leader', 'city': 'Milwaukee', 'state': 'WI', 'family': 'no',
  'family_note': 'Lead stories are about bodies found and an autopsy. Adult mode only, and only if the owner picked Wisconsin.',
  'headlines': [{'text': 'Fight to Free 40 Ice-Locked Ships', 'family': False}], 'spots': [], 'then_vs_now': None, 'question': ''},
]
