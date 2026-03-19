import json

new_questions = [
# ── BASKETBALL ──
{"q":"Who won the 2017 NBA Finals MVP?","a":"Kevin Durant","choices":["Kevin Durant","Stephen Curry","Klay Thompson","Andre Iguodala"],"sport":"basketball","difficulty":"medium"},
{"q":"Which NBA team is nicknamed the Nuggets?","a":"Denver Nuggets","choices":["Denver Nuggets","Golden State Warriors","Phoenix Suns","Utah Jazz"],"sport":"basketball","difficulty":"easy"},
{"q":"What is the NBA's luxury tax?","a":"A penalty teams pay for spending above a set salary threshold, distributed to other teams","choices":["A penalty teams pay for spending above a set salary threshold, distributed to other teams","A fee for playoff teams","A tax on jersey sales","A fine for technical fouls"],"sport":"basketball","difficulty":"medium"},
{"q":"Who won the NBA Finals in 2015?","a":"Golden State Warriors","choices":["Golden State Warriors","Cleveland Cavaliers","Oklahoma City Thunder","San Antonio Spurs"],"sport":"basketball","difficulty":"medium"},
{"q":"Which player is nicknamed 'Chef Curry'?","a":"Stephen Curry","choices":["Stephen Curry","Klay Thompson","Draymond Green","Jordan Poole"],"sport":"basketball","difficulty":"easy"},
{"q":"How many seconds does an NBA team have to advance the ball past halfcourt?","a":"8 seconds","choices":["8 seconds","10 seconds","5 seconds","15 seconds"],"sport":"basketball","difficulty":"medium"},
{"q":"Who was selected first overall in the 2014 NBA Draft?","a":"Andrew Wiggins","choices":["Andrew Wiggins","Jabari Parker","Joel Embiid","Julius Randle"],"sport":"basketball","difficulty":"medium"},
{"q":"Which arena do the Cleveland Cavaliers play in?","a":"Rocket Mortgage FieldHouse","choices":["Rocket Mortgage FieldHouse","Quicken Loans Arena","KeyBank Center","Nationwide Arena"],"sport":"basketball","difficulty":"medium"},
{"q":"Who scored 71 points in a single NBA game in 2023?","a":"Donovan Mitchell","choices":["Donovan Mitchell","Luka Doncic","Joel Embiid","Karl-Anthony Towns"],"sport":"basketball","difficulty":"medium"},
{"q":"Which player won the NBA Finals MVP in 2016?","a":"LeBron James","choices":["LeBron James","Kyrie Irving","Kevin Love","Draymond Green"],"sport":"basketball","difficulty":"medium"},
{"q":"Who was the first overall pick in the 2019 NBA Draft?","a":"Zion Williamson","choices":["Zion Williamson","Ja Morant","R.J. Barrett","De'Andre Hunter"],"sport":"basketball","difficulty":"easy"},
{"q":"What is the restricted area in the NBA?","a":"The 4-foot arc under the basket where no charge can be drawn","choices":["The 4-foot arc under the basket where no charge can be drawn","The lane area","The 3-second zone","The area between the free-throw line and the basket"],"sport":"basketball","difficulty":"medium"},
{"q":"Who won the NBA's inaugural Clutch Player of the Year award in 2023?","a":"Kawhi Leonard","choices":["Kawhi Leonard","LeBron James","Jayson Tatum","Devin Booker"],"sport":"basketball","difficulty":"hard"},
{"q":"Which team did Pau Gasol win two NBA championships with?","a":"Los Angeles Lakers","choices":["Los Angeles Lakers","Memphis Grizzlies","Chicago Bulls","San Antonio Spurs"],"sport":"basketball","difficulty":"medium"},
{"q":"How many teams are in the NBA?","a":"30","choices":["30","28","32","29"],"sport":"basketball","difficulty":"easy"},
{"q":"Which player wore number 45 during a brief return from retirement?","a":"Michael Jordan","choices":["Michael Jordan","Shaquille O'Neal","Allen Iverson","Kobe Bryant"],"sport":"basketball","difficulty":"medium"},
{"q":"Who won the 2016 NBA championship?","a":"Cleveland Cavaliers","choices":["Cleveland Cavaliers","Golden State Warriors","Oklahoma City Thunder","Toronto Raptors"],"sport":"basketball","difficulty":"easy"},
{"q":"Which player is known as 'The Claw' or 'Kawhi'?","a":"Kawhi Leonard","choices":["Kawhi Leonard","Paul George","Jimmy Butler","DeMar DeRozan"],"sport":"basketball","difficulty":"easy"},
{"q":"What team drafted Kyrie Irving first overall in 2011?","a":"Cleveland Cavaliers","choices":["Cleveland Cavaliers","Dallas Mavericks","Utah Jazz","Minnesota Timberwolves"],"sport":"basketball","difficulty":"medium"},
{"q":"Who coached the Golden State Warriors to their first championship in 40 years in 2015?","a":"Steve Kerr","choices":["Steve Kerr","Mark Jackson","Don Nelson","Alvin Gentry"],"sport":"basketball","difficulty":"medium"},
{"q":"Which player won the NBA MVP award in 2018?","a":"James Harden","choices":["James Harden","LeBron James","Kevin Durant","Russell Westbrook"],"sport":"basketball","difficulty":"medium"},
{"q":"What is the NBA salary cap?","a":"A limit on the total amount teams can pay all players combined","choices":["A limit on the total amount teams can pay all players combined","The minimum salary for any player","The maximum any single player can earn","The revenue sharing amount"],"sport":"basketball","difficulty":"easy"},
{"q":"Who won the NBA championship in 2018?","a":"Golden State Warriors","choices":["Golden State Warriors","Cleveland Cavaliers","Boston Celtics","Houston Rockets"],"sport":"basketball","difficulty":"easy"},
{"q":"Which player was nicknamed 'His Airness'?","a":"Michael Jordan","choices":["Michael Jordan","Vince Carter","Julius Erving","Clyde Drexler"],"sport":"basketball","difficulty":"easy"},
{"q":"Who won the NBA Finals MVP in 2019?","a":"Kawhi Leonard","choices":["Kawhi Leonard","Kyle Lowry","Pascal Siakam","Fred VanVleet"],"sport":"basketball","difficulty":"medium"},
{"q":"What city do the Grizzlies play in?","a":"Memphis","choices":["Memphis","Nashville","Little Rock","Jackson"],"sport":"basketball","difficulty":"easy"},
{"q":"Which player is the Portland Trail Blazers all-time leading scorer?","a":"Damian Lillard","choices":["Damian Lillard","Clyde Drexler","Bill Walton","Brandon Roy"],"sport":"basketball","difficulty":"medium"},
{"q":"What is a transition offense in basketball?","a":"Fast break scoring opportunities before the defense is set","choices":["Fast break scoring opportunities before the defense is set","A slow methodical half-court offense","A motion offense run by smaller lineups","A set play for end of quarter situations"],"sport":"basketball","difficulty":"easy"},
{"q":"Who won the 2024 NBA Finals MVP?","a":"Jaylen Brown","choices":["Jaylen Brown","Jayson Tatum","Al Horford","Kristaps Porzingis"],"sport":"basketball","difficulty":"medium"},
{"q":"Which arena do the Dallas Mavericks play in?","a":"American Airlines Center","choices":["American Airlines Center","Paycom Center","Ball Arena","FedEx Forum"],"sport":"basketball","difficulty":"medium"},

# ── FOOTBALL ──
{"q":"What is a screen pass in football?","a":"A short pass to a receiver who has blockers set up in front of him","choices":["A short pass to a receiver who has blockers set up in front of him","A pass thrown behind the line of scrimmage","A play-action pass","A pass thrown to the flat"],"sport":"football","difficulty":"easy"},
{"q":"Who won the 2021 Super Bowl?","a":"Tampa Bay Buccaneers","choices":["Tampa Bay Buccaneers","Kansas City Chiefs","Green Bay Packers","Buffalo Bills"],"sport":"football","difficulty":"medium"},
{"q":"Which player was first overall in the 2019 NFL Draft?","a":"Kyler Murray","choices":["Kyler Murray","Nick Bosa","Quinnen Williams","Josh Allen"],"sport":"football","difficulty":"medium"},
{"q":"What is the shotgun formation?","a":"When the quarterback lines up several yards behind the center to receive the snap","choices":["When the quarterback lines up several yards behind the center to receive the snap","A formation with three tight ends","A no-huddle spread offense","A wildcat variant with two QBs"],"sport":"football","difficulty":"easy"},
{"q":"Which team won Super Bowl XL?","a":"Pittsburgh Steelers","choices":["Pittsburgh Steelers","Seattle Seahawks","New England Patriots","Philadelphia Eagles"],"sport":"football","difficulty":"medium"},
{"q":"Who won the 2023 NFL MVP?","a":"Lamar Jackson","choices":["Lamar Jackson","Patrick Mahomes","Josh Allen","CJ Stroud"],"sport":"football","difficulty":"medium"},
{"q":"What is an audible in football?","a":"When the quarterback changes the play at the line of scrimmage by calling out new signals","choices":["When the quarterback changes the play at the line of scrimmage by calling out new signals","When the crowd noise is too loud for the team to hear","A review of a challenged play","A special timeout called by the coach"],"sport":"football","difficulty":"easy"},
{"q":"Which team drafted Jalen Hurts in the second round of the 2020 NFL Draft?","a":"Philadelphia Eagles","choices":["Philadelphia Eagles","Dallas Cowboys","Arizona Cardinals","Kansas City Chiefs"],"sport":"football","difficulty":"medium"},
{"q":"How many points does a safety score for the defending team?","a":"2","choices":["2","3","1","4"],"sport":"football","difficulty":"easy"},
{"q":"Who holds the NFL record for most passing yards in a single playoff game?","a":"Patrick Mahomes (430 yards in 2024)","choices":["Patrick Mahomes (430 yards in 2024)","Tom Brady","Peyton Manning","Brett Favre"],"sport":"football","difficulty":"hard"},
{"q":"What city are the Bears from?","a":"Chicago","choices":["Chicago","Green Bay","Detroit","Minneapolis"],"sport":"football","difficulty":"easy"},
{"q":"Which quarterback threw for the most yards in a Super Bowl?","a":"Tom Brady (505 yards in Super Bowl LV)","choices":["Tom Brady (505 yards in Super Bowl LV)","Kurt Warner","Peyton Manning","Drew Brees"],"sport":"football","difficulty":"hard"},
{"q":"What team plays home games at Empower Field at Mile High?","a":"Denver Broncos","choices":["Denver Broncos","Kansas City Chiefs","Los Angeles Rams","Las Vegas Raiders"],"sport":"football","difficulty":"medium"},
{"q":"Who was the first overall pick in the 2016 NFL Draft?","a":"Jared Goff","choices":["Jared Goff","Carson Wentz","Ezekiel Elliott","Joey Bosa"],"sport":"football","difficulty":"medium"},
{"q":"Which player won three straight NFL MVP awards?","a":"No player has won three straight NFL MVP awards","choices":["No player has won three straight NFL MVP awards","Tom Brady","Peyton Manning","Aaron Rodgers"],"sport":"football","difficulty":"hard"},
{"q":"What is the Lombardi Award given to?","a":"The best college football lineman (offensive or defensive)","choices":["The best college football lineman (offensive or defensive)","The Super Bowl winner","The NFL's best offensive lineman","The college player of the year"],"sport":"football","difficulty":"hard"},
{"q":"Which NFL team plays in Nashville?","a":"Tennessee Titans","choices":["Tennessee Titans","Louisville Cardinals","Memphis Blues","Nashville SC"],"sport":"football","difficulty":"easy"},
{"q":"How many yards is each hash mark from the sideline in the NFL?","a":"The hash marks are 70 feet 9 inches from each sideline","choices":["The hash marks are 70 feet 9 inches from each sideline","50 yards","15 yards","The hash marks are in the middle of the field"],"sport":"football","difficulty":"hard"},
{"q":"Who was the first wide receiver to be inducted into the Pro Football Hall of Fame?","a":"Don Hutson (1963)","choices":["Don Hutson (1963)","Raymond Berry","Elroy Hirsch","Tom Fears"],"sport":"football","difficulty":"hard"},
{"q":"Which team drafted Josh Allen in the 2018 NFL Draft?","a":"Buffalo Bills","choices":["Buffalo Bills","San Francisco 49ers","Cleveland Browns","Arizona Cardinals"],"sport":"football","difficulty":"easy"},
{"q":"What is the fair catch rule in football?","a":"A receiver signals that he will not run after catching a kick, protecting himself from being tackled","choices":["A receiver signals that he will not run after catching a kick, protecting himself from being tackled","A rule preventing tackles after the ball changes possession","A call for a replay review","A signal to the quarterback to abort the play"],"sport":"football","difficulty":"easy"},
{"q":"Who won the Super Bowl MVP in Super Bowl L (50)?","a":"Von Miller","choices":["Von Miller","Peyton Manning","Cam Newton","C.J. Anderson"],"sport":"football","difficulty":"medium"},
{"q":"Which city are the Browns from?","a":"Cleveland","choices":["Cleveland","Cincinnati","Columbus","Akron"],"sport":"football","difficulty":"easy"},
{"q":"What is the prevent defense in football?","a":"A soft zone defense used at the end of games to prevent big plays and let the clock run","choices":["A soft zone defense used at the end of games to prevent big plays and let the clock run","An all-out blitz on every down","A goal-line defensive stance","A defensive formation with 7 DBs"],"sport":"football","difficulty":"medium"},
{"q":"Which team won Super Bowl XLII?","a":"New York Giants","choices":["New York Giants","New England Patriots","Pittsburgh Steelers","Indianapolis Colts"],"sport":"football","difficulty":"medium"},
{"q":"Who was first overall in the 2022 NFL Draft?","a":"Travon Walker","choices":["Travon Walker","Aidan Hutchinson","Evan Neal","Drake London"],"sport":"football","difficulty":"hard"},
{"q":"What city are the Lions from?","a":"Detroit","choices":["Detroit","Chicago","Cleveland","Indianapolis"],"sport":"football","difficulty":"easy"},
{"q":"Which player holds the record for most interceptions in a single NFL season?","a":"Night Train Lane (14 in 1952)","choices":["Night Train Lane (14 in 1952)","Dick Butkus","Emlen Tunnell","Yale Lary"],"sport":"football","difficulty":"hard"},
{"q":"Who won the NFL MVP in 2021?","a":"Aaron Rodgers","choices":["Aaron Rodgers","Tom Brady","Cooper Kupp","Matthew Stafford"],"sport":"football","difficulty":"medium"},
{"q":"Which team played in the first Monday Night Football game in 1970?","a":"New York Jets vs Cleveland Browns","choices":["New York Jets vs Cleveland Browns","Dallas Cowboys vs Los Angeles Rams","Miami Dolphins vs Kansas City Chiefs","Green Bay Packers vs Chicago Bears"],"sport":"football","difficulty":"hard"},

# ── HOCKEY ──
{"q":"Which team won the most recent Stanley Cup (as of 2025)?","a":"Florida Panthers","choices":["Florida Panthers","Vegas Golden Knights","Edmonton Oilers","Colorado Avalanche"],"sport":"hockey","difficulty":"medium"},
{"q":"What year did Wayne Gretzky retire?","a":"1999","choices":["1999","2000","1997","2001"],"sport":"hockey","difficulty":"medium"},
{"q":"Which player scored 50 goals in his first NHL season?","a":"Mike Bossy (1977-78)","choices":["Mike Bossy (1977-78)","Wayne Gretzky","Mario Lemieux","Teemu Selanne"],"sport":"hockey","difficulty":"hard"},
{"q":"What city are the Ducks from?","a":"Anaheim","choices":["Anaheim","Los Angeles","San Diego","Sacramento"],"sport":"hockey","difficulty":"easy"},
{"q":"Which team traded Wayne Gretzky to the Los Angeles Kings?","a":"Edmonton Oilers","choices":["Edmonton Oilers","New York Rangers","St. Louis Blues","Pittsburgh Penguins"],"sport":"hockey","difficulty":"medium"},
{"q":"How long is an NHL rink in feet?","a":"200 feet","choices":["200 feet","185 feet","210 feet","180 feet"],"sport":"hockey","difficulty":"medium"},
{"q":"Who won the Conn Smythe Trophy in 2022?","a":"Cale Makar","choices":["Cale Makar","Nathan MacKinnon","Darcy Kuemper","Devon Toews"],"sport":"hockey","difficulty":"medium"},
{"q":"Which team plays at Rogers Arena?","a":"Vancouver Canucks","choices":["Vancouver Canucks","Calgary Flames","Edmonton Oilers","Winnipeg Jets"],"sport":"hockey","difficulty":"medium"},
{"q":"What is a wraparound goal in hockey?","a":"When a player skates around the back of the net and tucks the puck in from behind","choices":["When a player skates around the back of the net and tucks the puck in from behind","A goal scored from a rebound","A goal off a player's skate","A tip-in off a long shot"],"sport":"hockey","difficulty":"easy"},
{"q":"Who won the Vezina Trophy in 2022?","a":"Igor Shesterkin","choices":["Igor Shesterkin","Andrei Vasilevskiy","Juuse Saros","Tristan Jarry"],"sport":"hockey","difficulty":"hard"},
{"q":"Which team plays at Canadian Tire Centre?","a":"Ottawa Senators","choices":["Ottawa Senators","Toronto Maple Leafs","Montreal Canadiens","Winnipeg Jets"],"sport":"hockey","difficulty":"medium"},
{"q":"How many NHL teams are currently in Canada?","a":"7","choices":["7","6","8","5"],"sport":"hockey","difficulty":"medium"},
{"q":"Who won the Hart Trophy (NHL MVP) in 2019?","a":"Nikita Kucherov","choices":["Nikita Kucherov","Nathan MacKinnon","Sidney Crosby","Connor McDavid"],"sport":"hockey","difficulty":"medium"},
{"q":"What is a deke in hockey?","a":"A fake or feint move to get past a defender or goalie","choices":["A fake or feint move to get past a defender or goalie","A backward skating technique","A type of slapshot","A defensive rotation"],"sport":"hockey","difficulty":"easy"},
{"q":"Which player set the NHL record for most points by a rookie with 132 points?","a":"Teemu Selanne (1992-93) set the goals record; Peter Stastny holds some records","choices":["Teemu Selanne set the rookie goals record (76) but not total points","Wayne Gretzky holds most records","Mario Lemieux","Peter Stastny (109 points) held it before Selanne's goals record"],"sport":"hockey","difficulty":"hard"},
{"q":"What city are the Blue Jackets from?","a":"Columbus","choices":["Columbus","Cleveland","Cincinnati","Indianapolis"],"sport":"hockey","difficulty":"easy"},
{"q":"Who won the Art Ross Trophy in 2022?","a":"Connor McDavid","choices":["Connor McDavid","Leon Draisaitl","Auston Matthews","Jonathan Huberdeau"],"sport":"hockey","difficulty":"medium"},
{"q":"Which team plays at PPG Paints Arena?","a":"Pittsburgh Penguins","choices":["Pittsburgh Penguins","Philadelphia Flyers","Columbus Blue Jackets","Buffalo Sabres"],"sport":"hockey","difficulty":"medium"},
{"q":"What is goaltender interference in hockey?","a":"When an attacking player makes contact with the goalie while in the crease, causing a no-goal ruling","choices":["When an attacking player makes contact with the goalie while in the crease, causing a no-goal ruling","When a defender trips a shooter","When a goalie leaves the crease to play the puck","A delay of game penalty by the goalie"],"sport":"hockey","difficulty":"medium"},
{"q":"How many times did Mario Lemieux win the NHL scoring title?","a":"6 times","choices":["6 times","3 times","5 times","4 times"],"sport":"hockey","difficulty":"hard"},
{"q":"Which team plays at SAP Center?","a":"San Jose Sharks","choices":["San Jose Sharks","Anaheim Ducks","Los Angeles Kings","Vegas Golden Knights"],"sport":"hockey","difficulty":"medium"},
{"q":"Who scored the Cup-winning goal for the Chicago Blackhawks in 2013?","a":"Dave Bolland","choices":["Dave Bolland","Jonathan Toews","Patrick Kane","Bryan Bickell"],"sport":"hockey","difficulty":"hard"},
{"q":"What is a poke check in hockey?","a":"When a defender reaches out to knock the puck off an attacker's stick","choices":["When a defender reaches out to knock the puck off an attacker's stick","A hit from behind","A check against the boards","A stick lift technique"],"sport":"hockey","difficulty":"easy"},
{"q":"Which city are the Jets from?","a":"Winnipeg","choices":["Winnipeg","Edmonton","Calgary","Regina"],"sport":"hockey","difficulty":"easy"},
{"q":"Who holds the NHL record for most points in a single playoff year?","a":"Wayne Gretzky (47 points in 1985)","choices":["Wayne Gretzky (47 points in 1985)","Mario Lemieux","Mark Messier","Bernie Parent"],"sport":"hockey","difficulty":"hard"},
]

with open('questions.json') as f:
    existing = json.load(f)

existing_set = set(q['q'].strip().lower() for q in existing)
added = [q for q in new_questions if q['q'].strip().lower() not in existing_set]
existing.extend(added)

with open('questions.json', 'w') as f:
    json.dump(existing, f, indent=2)

print(f"Added {len(added)} questions. Total now: {len(existing)}")
