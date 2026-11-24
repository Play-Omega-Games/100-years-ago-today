# Sources

Rev 2, Tue Nov 24, 2026 (ET). Generated from plans/front-pages.json, then hand-checked.

## Rights
- Library of Congress, Chronicling America, Rights and Access: https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/
- The same statement is in every item's `rights` field (checked by build_plan.py and tests): "Newspapers published in the United States more than 95 years ago are in the public domain in their entirety." Every page in the plan is from 1926 or 1927.

## APIs used
- Search by date: https://www.loc.gov/collections/chronicling-america/?dates=YYYY-MM-DD/YYYY-MM-DD&fa=online-format:image&fo=json&c=160
- Front page metadata: https://www.loc.gov/resource/<lccn>/<date>/ed-1/?sp=1&fo=json (page images, OCR link, rights)
- Images: IIIF at tile.loc.gov, `<iiif_base>/full/pct:25/0/default.jpg`; regions with `<iiif_base>/pct:x,y,w,h/pct:50/0/default.jpg`
- PDFs (tile.loc.gov/storage-services) return 403 to scripts, so the plan has no PDF links.

## Then-vs-now sources (45 days)
Kinds: change (then vs now), continuity (still true today), what_next (what happened later). No Wikipedia. Every URL was opened and the quoted fact found on the page before use.

| Date | Paper | Family | Kind | Source |
|---|---|---|---|---|
| Wed Nov 24, 1926 | Evening Star, Washington DC | care | change | Library of Congress, About Evening Star: https://www.loc.gov/item/sn83045462/ |
| Thu Nov 25, 1926 | The Indianapolis Times, Indianapolis IN | care | change | National Archives, Congress Establishes Thanksgiving: https://www.archives.gov/legislative/features/thanksgiving |
| Fri Nov 26, 1926 | The Bismarck Tribune, Bismarck ND | care | what_next | Seward Daily Gateway, Nov 29, 1926, front page (Library of Congress): https://www.loc.gov/resource/sn87062169/1926-11-29/ed-1/?sp=1 |
| Sat Nov 27, 1926 | The Alaska Daily Empire, Juneau AK | care | change | US House History, Art and Archives, Ratification of the Twenty-first Amendment: https://history.house.gov/Historical-Highlights/1901-1950/1932_12_05_Twenty-first_Amendment/ |
| Sun Nov 28, 1926 | Nogales International, Nogales AZ | care | change | Federal Highway Administration, Route Log and Finder List, Table 1: https://www.fhwa.dot.gov/planning/national_highway_system/interstate_highway_system/routefinder/table01.cfm |
| Mon Nov 29, 1926 | Seward Daily Gateway, Seward AK | care | change | National Archives, Proclamation 3269: https://www.archives.gov/federal-register/codification/proclamations/03269.html |
| Tue Nov 30, 1926 | New Britain Herald, New Britain CT | care | change | Gilder Lehrman Center, Yale, Alfred Emanuel Smith: https://macmillan.yale.edu/glc/smith-alfred-emanuel-1873-1944 |
| Wed Dec 1, 1926 | Imperial Valley Press, El Centro CA | care | continuity | Library of Congress, About Imperial Valley Press: https://www.loc.gov/item/sn92070146/ |
| Thu Dec 2, 1926 | Daily Kennebec Journal, Augusta ME | care | change | WyoHistory.org, Nellie Ross; US Mint, Former Directors: https://www.wyohistory.org/encyclopedia/nellie-ross |
| Fri Dec 3, 1926 | The Chapel Hill Weekly, Chapel Hill NC | ok | change | UNC Athletics, Kenan Stadium: https://goheels.com/facilities/kenan-stadium/159 |
| Sat Dec 4, 1926 | The Washington Times, Washington DC | care | change | Congressional Research Service, IF12577: https://www.congress.gov/crs_external_products/IF/HTML/IF12577.html |
| Sun Dec 5, 1926 | The Montgomery Advertiser, Montgomery AL | care | change | Encyclopedia of Alabama, Hill-Burton Act: https://encyclopediaofalabama.org/article/hill-burton-act/ |
| Mon Dec 6, 1926 | The Elkins Inter-Mountain, Elkins WV | care | change | US House History, Art and Archives, The Twentieth Amendment: https://history.house.gov/HistoricalHighlight/Detail/35272 |
| Tue Dec 7, 1926 | South Bend News-Times, South Bend IN | care | change | US Army Corps of Engineers, Soo Locks to open for 2026 shipping season: https://www.lrd.usace.army.mil/News/News-Releases/Article/4429668/soo-locks-to-open-for-2026-shipping-season/ |
| Wed Dec 8, 1926 | The Washington Daily News, Washington DC | care | change | Library of Congress, About Evening Star: https://www.loc.gov/item/sn83045462/ |
| Thu Dec 9, 1926 | The Kennewick Courier-Reporter, Kennewick WA | ok | change | World Health Organization, Smallpox: https://www.who.int/health-topics/smallpox |
| Fri Dec 10, 1926 | The Chapel Hill Weekly, Chapel Hill NC | ok | change | UNC-Chapel Hill, 100 seasons later, Kenan Stadium remains a campus fixture: https://www.unc.edu/story/100-seasons-later-kenan-stadium-remains-a-campus-fixture/ |
| Sat Dec 11, 1926 | The McCarthy Weekly News, McCarthy AK | ok | change | National Park Service, Kennecott Mines National Historic Landmark: https://www.nps.gov/wrst/learn/historyculture/kennecott-mines-national-historic-landmark.htm |
| Sun Dec 12, 1926 | Nogales International, Nogales AZ | ok | continuity | NHL Records, franchise data for the Chicago Blackhawks (first season 1926-27): https://records.nhl.com/site/api/franchise?cayenneExp=id=11 |
| Mon Dec 13, 1926 | Seward Daily Gateway, Seward AK | care | change | Alaska Railroad, Our History: https://www.alaskarailroad.com/corporate/history |
| Tue Dec 14, 1926 | Evening Star, Washington DC | care | change | U.S. General Services Administration, EPA East and West Buildings history: https://www.gsa.gov/real-estate/explore-historic-buildings/find-a-historic-federal-building/epa-east-and-west-building-washington-dc |
| Wed Dec 15, 1926 | The Ellsworth American, Ellsworth ME | ok | change | Board of Governors of the Federal Reserve System, Federal Reserve Act: https://www.federalreserve.gov/aboutthefed/fract.htm |
| Thu Dec 16, 1926 | Watauga Democrat, Boone NC | care | change | U.S. Environmental Protection Agency, Radionuclide Basics: Radium: https://www.epa.gov/radiation/radionuclide-basics-radium |
| Fri Dec 17, 1926 | The Chapel Hill Weekly, Chapel Hill NC | care | change | United States Postal Service Historian, On This Day in Postal History: https://about.usps.com/who-we-are/postal-history/on-this-day.pdf |
| Sat Dec 18, 1926 | The McCarthy Weekly News, McCarthy AK | ok | change | National Park Service, Wrangell-St. Elias: Driving Park Roads: https://www.nps.gov/wrst/planyourvisit/driving-park-roads.htm |
| Sun Dec 19, 1926 | Nogales International, Nogales AZ | ok | change | U.S. Environmental Protection Agency, Highlights of the Automotive Trends Report: https://www.epa.gov/automotive-trends/highlights-automotive-trends-report |
| Mon Dec 20, 1926 | Hyder Weekly Herald, Hyder AK | ok | continuity | Alaska Seafood Marketing Institute, Alaska Wild Salmon Day release, Aug. 10, 2023: https://www.alaskaseafood.org/news/for-release-alaska-wild-salmon-day-honors-our-nations-favorite-fish-and-the-people-who-provide-it/ |
| Tue Dec 21, 1926 | The Herald and News, Newberry SC | ok | change | Library of Congress catalog record, The Herald and News (Newberry, S.C.) 1903-1937: https://www.loc.gov/item/sn86063758/ |
| Wed Dec 22, 1926 | The Cody Enterprise and the Park County Herald, Cody WY | ok | change | National Park Service, Wyoming: Buffalo Bill Dam: https://www.nps.gov/articles/wyoming-buffalo-bill-dam.htm |
| Thu Dec 23, 1926 | The Kevin Review, Kevin MT | ok | continuity | Library of Congress, Printed Ephemera Collection record for "A visit from St. Nicholas": https://www.loc.gov/item/rbpe.11804300/ |
| Fri Dec 24, 1926 | Vashon Island News-Record, Vashon WA | care | continuity | Washington State Department of Transportation, Washington State Ferries routes: https://wsdot.wa.gov/travel/washington-state-ferries |
| Sat Dec 25, 1926 | Evening Star, Washington DC | care | continuity | National Park Service, History of the National Christmas Tree: https://www.nps.gov/whho/learn/historyculture/national-christmas-tree-history.htm |
| Sun Dec 26, 1926 | Nogales International (Holiday Edition), Nogales AZ | ok | change | Library of Congress, Chronicling America: Rights and Access: https://www.loc.gov/collections/chronicling-america/about-this-collection/rights-and-access/ |
| Mon Dec 27, 1926 | The Winslow Mail, Winslow AZ | care | what_next | Lowell Observatory, Pluto: https://lowell.edu/discover/pluto/ |
| Tue Dec 28, 1926 | The Pleasantville Press, Pleasantville NJ | care | continuity | City of Philadelphia Parks and Recreation, The Mummers Parade: A PPR Tradition: https://www.phila.gov/Newsletters/parksnrecsnewsletter/pdfs/Mummers.pdf |
| Wed Dec 29, 1926 | Windham County Observer, Putnam CT | care | continuity | U.S. Office of Personnel Management, Federal Holidays: https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ |
| Thu Dec 30, 1926 | The Pocahontas Times, Marlinton WV | care | change | West Virginia State Museum Education, West Virginia State Symbols: https://wvstatemuseumed.wv.gov/site/state-symbols.html |
| Fri Dec 31, 1926 | Milford Chronicle, Milford DE | care | change | Sussex County, Delaware, History of Sussex County: https://sussexcountyde.gov/history |
| Sat Jan 1, 1927 | The McCarthy Weekly News, McCarthy AK | care | change | National Park Service, Bering Land Bridge: Alaska Natives and Early People: https://www.nps.gov/bela/learn/historyculture/alaska-natives-and-early-people.htm |
| Sun Jan 2, 1927 | Nogales International, Nogales AZ | ok | continuity | Nobel Foundation, The Nobel Prize in Literature 1925: https://www.nobelprize.org/prizes/literature/1925/summary/ |
| Mon Jan 3, 1927 | St. Croix Avis, Christiansted VI | care | continuity | National Park Service, Christiansted National Historic Site: https://www.nps.gov/chri/index.htm |
| Tue Jan 4, 1927 | The Pleasantville Press, Pleasantville NJ | ok | change | U.S. Energy Information Administration, Use of coal: https://www.eia.gov/energyexplained/coal/use-of-coal.php |
| Wed Jan 5, 1927 | Willmar Tribune, Willmar MN | care | what_next | National Archives, General Records of the Department of Education (Record Group 441): https://www.archives.gov/research/guide-fed-records/groups/441.html |
| Thu Jan 6, 1927 | The Ronan Pioneer, Ronan MT | care | change | U.S. Department of the Interior press release, June 23, 2021: https://www.doi.gov/pressreleases/interior-transfers-national-bison-range-lands-trust-confederated-salish-and-kootenai |
| Fri Jan 7, 1927 | Thermopolis Independent, Thermopolis WY | care | change | Library of Congress, Headlines and Heroes blog, The Linotype: The Machine that Revolutionized Movable Type: https://blogs.loc.gov/headlinesandheroes/2022/06/the-linotype-the-machine-that-revolutionized-movable-type/ |

## Alternates (not in the daily rotation)
| Date | Paper | Level | Why |
|---|---|---|---|
| Mon Nov 29, 1926 | Brownsville Herald, TX | no | Lead story and two others describe killings. Adult mode only, and only if the owner picked Texas. |
| Fri Dec 3, 1926 | The Milwaukee Leader, WI | no | Lead stories are about bodies found and an autopsy. Adult mode only, and only if the owner picked Wisconsin. |
| Thu Dec 9, 1926 | The Bismarck Tribune, ND | no | A mine disaster and a headline about famine and cannibalism in China. Adult mode only, and only if the owner picked North Dakota. |
| Sat Dec 11, 1926 | Daily Kennebec Journal, ME | no | Headlines about lynchings, a killing of dry agents and a hunting death. Adult mode only, and only if the owner picked Maine. |
| Sat Dec 11, 1926 | The Daily Alaska Empire, AK | no | Front page carries a headline about lynchings. Adult mode only, and only if the owner picked Alaska. |
| Sat Dec 11, 1926 | Seward Daily Gateway, AK | no | A headline about famine and cannibalism in China. Adult mode only. |
| Sun Dec 12, 1926 | Douglas Daily Dispatch, AZ | no | Two stories describe killings in detail. Adult mode only, and only if the owner picked Arizona. |
| Mon Dec 13, 1926 | The Cordele Dispatch, GA | no | A banner headline about a widow describing her husband's murder. Adult mode only, and only if the owner picked Georgia. |
| Mon Dec 13, 1926 | The Indianapolis Times, IN | no | Lead story is a poisoning plot and another headline describes a body found with a crushed skull. Adult mode only, and only if the owner picked Indiana. |
| Tue Dec 14, 1926 | Imperial Valley Press, CA | no | Headlines about a suicide and a murder. Adult mode only, and only if the owner picked California. Also carries "Missing Novelist Reported Found" (Agatha Christie). |
| Wed Dec 15, 1926 | New Britain Herald, CT | no | A large headline describes a man run over and killed by a bus, plus a body found in a snowbank and a murder charge. Adult mode only, and only if the owner picked Connecticut. |
| Sat Dec 18, 1926 | The Nome Nugget, AK | care | Lead story is about the Ormiston and Aimee Semple McPherson scandal. Usable as an Alaska alternate in adult mode. |
| Fri Dec 24, 1926 | Evening Star, DC | no | A large top headline about a train wreck with people crushed to death. Adult mode only. Also carries the story of Rebecca, the raccoon sent for the President's dinner who became a White House pet. |
| Fri Dec 24, 1926 | The Coconino Sun, AZ | no | A headline reports a suicide. Adult mode only. |
| Wed Dec 29, 1926 | The Redwood Gazette, MN | no | A headline about a youth who shot two people. Adult mode only, and only if the owner picked Minnesota. |
| Thu Dec 30, 1926 | Askov American, MN | no | A joke at the bottom uses a racial slur. Never shown in family mode. |
| Fri Dec 31, 1926 | The Bozeman Courier, MT | no | A large photo of a boat disaster where thirty people drowned. Adult mode only, and only if the owner picked Montana. |
| Sat Jan 1, 1927 | Las Vegas Age, NV | no | A headline reports a suicide and another a man who shot himself. Adult mode only, and only if the owner picked Nevada. |
| Mon Jan 3, 1927 | The Cordele Dispatch, GA | no | War headlines describing a bloody battle and human butchery. Adult mode only. |
| Mon Jan 3, 1927 | The Washington Daily News, DC | no | Headlines about a suicide and a murdered bride. Adult mode only. |
| Mon Jan 3, 1927 | Seward Daily Gateway, AK | no | A race riot story and a gangster found with bullet holes in his skull. Adult mode only. Also has the Stanford and Alabama 7-7 Rose Bowl tie. |
| Mon Jan 3, 1927 | Imperial Valley Press, CA | no | Headlines about suicides and an infant killed. Adult mode only. |
| Mon Jan 3, 1927 | Hyder Weekly Herald, AK | no | A story about a costume party uses racial slurs. Never shown in family mode. |
| Fri Jan 7, 1927 | The Guernsey Gazette, WY | no | A headline about a man burned to death in his cabin, with details of the body. Adult mode only. Fun note: the masthead misprints the year as 1926. |

## Standards codes (verified Nov 24, 2026 against the official texts)
Wording is always "supports practice toward". Not a full curriculum and not accredited.

| Code | Framework | Band | Text | Source |
|---|---|---|---|---|
| D2.His.2.3-5 | C3 | 3-5 | Compare life in specific historical time periods to life today. | https://www.socialstudies.org/standards/c3 |
| D2.His.2.6-8 | C3 | 6-8 | Classify series of historical events and developments as examples of change and/or continuity. | https://www.socialstudies.org/standards/c3 |
| D2.His.10.3-5 | C3 | 3-5 | Compare information provided by different historical sources about the past. | https://www.socialstudies.org/standards/c3 |
| D2.His.11.3-5 | C3 | 3-5 | Infer the intended audience and purpose of a historical source from information within the source itself. | https://www.socialstudies.org/standards/c3 |
| RI.3.7 | CCSS-ELA | 3 | Use information gained from illustrations (e.g., maps, photographs) and the words in a text to demonstrate understanding of the text (e.g., where, when, why, and how key events occur). | https://www.cde.ca.gov/be/st/ss/documents/finalelaccssstandards.pdf |
| RH.6-8.7 | CCSS-ELA | 6-8 | Integrate visual information (e.g., in charts, graphs, photographs, videos, or maps) with other information in print and digital texts. | https://www.cde.ca.gov/be/st/ss/documents/finalelaccssstandards.pdf |

## Facts dropped because the source could not be verified by opening it
- Pulitzer Prize for Paul Green (pulitzer.org returns 403 to scripts; UNC pages timed out).
- Christmas Seals history (American Lung Association pages did not contain the claim).
- Tuberculosis then vs now (CDC returns 403 to scripts).
- Cody Stampede history (the official site is JavaScript only).
- 1926 consumer prices (BLS public API would not return 1926 data).
- Steese Highway history (the BLM page did not match the claim).
- Nogales rail line (Wikipedia; replaced by FHWA Interstate 19 route data).
- A second Prohibition repeal fact on Jan 4 (would repeat Nov 27; replaced by EIA coal use).
- Dec 30 source moved (Nov 24, 2026): the West Virginia Legislature kids' State Symbols page was down all day (TLS errors, 500, 504). The same fact (black bear adopted as state animal by House Concurrent Resolution No. 6 in 1973) is on the West Virginia State Museum Education page, verified 200.
