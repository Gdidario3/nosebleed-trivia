import json

new_questions = [
# ── BASKETBALL — specific stats / records / moments ──
{"q":"Who was the first player in NBA history to record 50+ points and 25+ rebounds in a game?","a":"Wilt Chamberlain","choices":["Wilt Chamberlain","Kareem Abdul-Jabbar","Bob Pettit","Elgin Baylor"],"sport":"basketball","difficulty":"hard"},
{"q":"Which team drafted Joel Embiid in 2014?","a":"Philadelphia 76ers","choices":["Philadelphia 76ers","New York Knicks","Milwaukee Bucks","Orlando Magic"],"sport":"basketball","difficulty":"medium"},
{"q":"Who won the NBA's inaugural play-in tournament game in 2021?","a":"The Golden State Warriors (beat Memphis to advance to playoffs)","choices":["Golden State Warriors beat Memphis in the inaugural play-in","Memphis Grizzlies","Indiana Pacers","Charlotte Hornets"],"sport":"basketball","difficulty":"hard"},
{"q":"Which player scored 40+ points in four consecutive playoff games in 2021?","a":"Trae Young","choices":["Trae Young","Luka Doncic","Nikola Jokic","Zion Williamson"],"sport":"basketball","difficulty":"hard"},
{"q":"What college did Zion Williamson attend?","a":"Duke University","choices":["Duke University","North Carolina","Kentucky","Kansas"],"sport":"basketball","difficulty":"easy"},
{"q":"Who is the youngest player to start an NBA All-Star Game?","a":"Luka Doncic (19 years old in 2020)","choices":["Luka Doncic (19 years old in 2020)","LeBron James","Kevin Garnett","Stephon Marbury"],"sport":"basketball","difficulty":"hard"},
{"q":"What is the FIBA basketball shot clock?","a":"24 seconds (same as NBA); 14 seconds after offensive rebound","choices":["24 seconds (same as NBA); 14 seconds after offensive rebound","30 seconds","35 seconds","20 seconds"],"sport":"basketball","difficulty":"hard"},
{"q":"Which player won Rookie of the Year in 2021?","a":"LaMelo Ball","choices":["LaMelo Ball","Anthony Edwards","Tyrese Haliburton","Deni Avdija"],"sport":"basketball","difficulty":"medium"},
{"q":"Who was the first player to win NBA Finals MVP with his team trailing 3-1?","a":"LeBron James in 2016","choices":["LeBron James in 2016","Bill Russell","Kareem Abdul-Jabbar","Magic Johnson"],"sport":"basketball","difficulty":"medium"},
{"q":"What is the furthest back-to-back shooting percentage Steph Curry has achieved from three?","a":"45.4% in 2015-16 season","choices":["45.4% in 2015-16 season","50%","48%","42%"],"sport":"basketball","difficulty":"hard"},
{"q":"Which player scored 44 points in his NBA Finals debut in 2023?","a":"Nikola Jokic","choices":["Nikola Jokic","Jimmy Butler","Tyler Herro","Max Strus"],"sport":"basketball","difficulty":"hard"},
{"q":"What team did Dirk Nowitzki spend his entire NBA career with?","a":"Dallas Mavericks","choices":["Dallas Mavericks","San Antonio Spurs","Oklahoma City Thunder","Houston Rockets"],"sport":"basketball","difficulty":"easy"},
{"q":"Which player holds the NBA record for most points in a single postseason?","a":"Michael Jordan (759 in 1992)","choices":["Michael Jordan (759 in 1992)","LeBron James","Wilt Chamberlain","Jerry West"],"sport":"basketball","difficulty":"hard"},
{"q":"What is the college record for three-pointers in a season?","a":"Varies; Doug McDermott and others hold individual school records","choices":["Jeff Boschee holds the single season record for Kansas","Various players hold school-specific records","Pete Maravich","Steph Curry at Davidson"],"sport":"basketball","difficulty":"hard"},
{"q":"Which NBA franchise holds the record for worst single-season record?","a":"Charlotte Bobcats (7-59 in lockout-shortened 2011-12 season)","choices":["Charlotte Bobcats (7-59 in lockout-shortened 2011-12 season)","Philadelphia 76ers","Dallas Mavericks (1992-93)","Denver Nuggets"],"sport":"basketball","difficulty":"hard"},
{"q":"Who won the Most Improved Player award in 2021?","a":"Julius Randle","choices":["Julius Randle","Jordan Poole","Jerami Grant","Michael Porter Jr."],"sport":"basketball","difficulty":"medium"},
{"q":"Which player set the G League record with 81 points in a single game?","a":"Ricky Council IV set a recent record; the record holders changed over the years","choices":["Temple's Ace Sherburne or various players depending on the era","Earl Boykins","Manute Bol","Andrew Goudelock"],"sport":"basketball","difficulty":"hard"},
{"q":"What year did the Miami Heat win back-to-back NBA championships?","a":"2012 and 2013","choices":["2012 and 2013","2011 and 2012","2013 and 2014","2010 and 2011"],"sport":"basketball","difficulty":"easy"},
{"q":"Who was the first overall pick in the 2009 NBA Draft?","a":"Blake Griffin","choices":["Blake Griffin","Hasheem Thabeet","James Harden","Stephen Curry"],"sport":"basketball","difficulty":"medium"},
{"q":"Which college team has produced the most NBA first-round draft picks in history?","a":"Kentucky","choices":["Kentucky","Duke","Kansas","North Carolina"],"sport":"basketball","difficulty":"medium"},
{"q":"Who was named the 2023 NBA Finals MVP after winning with Miami?","a":"Miami Heat lost the 2023 Finals to Denver; Nikola Jokic won MVP","choices":["Nikola Jokic won the Finals MVP (Denver beat Miami)","Jimmy Butler","Bam Adebayo","Nikola Jokic"],"sport":"basketball","difficulty":"medium"},
{"q":"What team did Shawn Kemp team up with Gary Payton on in the 1990s?","a":"Seattle SuperSonics","choices":["Seattle SuperSonics","Oklahoma City Thunder","Portland Trail Blazers","Utah Jazz"],"sport":"basketball","difficulty":"medium"},
{"q":"Which player hit a buzzer-beater to win Game 7 against Philadelphia in the 2019 playoffs?","a":"Kawhi Leonard (Toronto Raptors)","choices":["Kawhi Leonard (Toronto Raptors)","Kyle Lowry","Pascal Siakam","Marc Gasol"],"sport":"basketball","difficulty":"medium"},
{"q":"Who holds the NBA record for most field goals attempted in a career?","a":"Kareem Abdul-Jabbar","choices":["Kareem Abdul-Jabbar","Wilt Chamberlain","Karl Malone","LeBron James"],"sport":"basketball","difficulty":"hard"},
{"q":"Which team did Manu Ginobili spend his entire NBA career with?","a":"San Antonio Spurs","choices":["San Antonio Spurs","Chicago Bulls","Miami Heat","Los Angeles Lakers"],"sport":"basketball","difficulty":"easy"},
{"q":"What number did Dennis Rodman wear for the Chicago Bulls?","a":"91","choices":["91","10","73","33"],"sport":"basketball","difficulty":"hard"},
{"q":"Who won the NBA Defensive Player of the Year in 2022?","a":"Jaren Jackson Jr.","choices":["Jaren Jackson Jr.","Mikal Bridges","Bam Adebayo","Brook Lopez"],"sport":"basketball","difficulty":"hard"},
{"q":"Which player scored 39 points in the first half of a NBA Finals game?","a":"Elgin Baylor (61 total - but not split this way)","choices":["No player has scored 39 in one half of a Finals game","Michael Jordan","LeBron James","Jerry West scored 42 in a Finals game"],"sport":"basketball","difficulty":"hard"},
{"q":"What city do the Hornets play in?","a":"Charlotte","choices":["Charlotte","Raleigh","Greensboro","Winston-Salem"],"sport":"basketball","difficulty":"easy"},
{"q":"Who won the NBA Three-Point Contest in 2022?","a":"Karl-Anthony Towns","choices":["Karl-Anthony Towns","Luke Kennard","Patty Mills","Trae Young"],"sport":"basketball","difficulty":"hard"},

# ── FOOTBALL — specific seasons and plays ──
{"q":"Which team scored 62 points in a single regular season NFL game in 2023?","a":"Miami Dolphins beat the Denver Broncos 70-20 in 2023","choices":["Miami Dolphins scored 70 vs Denver in 2023","San Francisco 49ers","Kansas City Chiefs","Washington Commanders"],"sport":"football","difficulty":"hard"},
{"q":"Who holds the NFL record for most sacks in a single season?","a":"Michael Strahan (22.5 in 2001)","choices":["Michael Strahan (22.5 in 2001)","Lawrence Taylor","Reggie White","Mark Gastineau"],"sport":"football","difficulty":"hard"},
{"q":"Which team drafted Justin Herbert in 2020?","a":"Los Angeles Chargers","choices":["Los Angeles Chargers","Las Vegas Raiders","Arizona Cardinals","Cincinnati Bengals"],"sport":"football","difficulty":"medium"},
{"q":"What year did the New England Patriots complete a 16-0 regular season?","a":"2007","choices":["2007","2006","2004","2003"],"sport":"football","difficulty":"medium"},
{"q":"Who threw for 5,477 yards in a single NFL season?","a":"Drew Brees (2011)","choices":["Drew Brees (2011)","Peyton Manning","Matthew Stafford","Ben Roethlisberger"],"sport":"football","difficulty":"hard"},
{"q":"Which running back won two Super Bowls with the San Francisco 49ers in the 1980s?","a":"Roger Craig","choices":["Roger Craig","Ricky Watters","Tom Rathman","Wendell Tyler"],"sport":"basketball","difficulty":"hard"},
{"q":"Who returned a missed field goal 109 yards for a touchdown in the 2015 playoffs?","a":"Robert McClain returned one, but Antonio Cromartie returned one for Arizona","choices":["Leodis McKelvin or corrrect: Chris Harris or the correct player from that game","Antonio Cromartie","Antrel Rolle","Larry Fitzgerald"],"sport":"football","difficulty":"hard"},
{"q":"Which NFL team plays in the city of Jacksonville?","a":"Jacksonville Jaguars","choices":["Jacksonville Jaguars","Miami Dolphins","Tampa Bay Buccaneers","Carolina Panthers"],"sport":"football","difficulty":"easy"},
{"q":"Who was the first rookie QB to start and win a Super Bowl?","a":"No rookie QB has started and won a Super Bowl","choices":["No rookie QB has started and won a Super Bowl","Ben Roethlisberger","Russell Wilson","Jared Goff"],"sport":"football","difficulty":"hard"},
{"q":"What team won the 2025 NFC Championship?","a":"Philadelphia Eagles","choices":["Philadelphia Eagles","Washington Commanders","Los Angeles Rams","Dallas Cowboys"],"sport":"football","difficulty":"medium"},
{"q":"Which player holds the record for most receiving yards in a single postseason?","a":"Jerry Rice (549 yards in 1988 playoffs)","choices":["Jerry Rice (549 yards in 1988 playoffs)","Julio Jones","Wes Welker","Brandon Marshall"],"sport":"football","difficulty":"hard"},
{"q":"What team does CJ Stroud play for?","a":"Houston Texans","choices":["Houston Texans","Indianapolis Colts","Carolina Panthers","Arizona Cardinals"],"sport":"football","difficulty":"easy"},
{"q":"Who was the first player to rush for 1,000 yards and catch 1,000 yards in same season?","a":"Roger Craig (1985)","choices":["Roger Craig (1985)","Marshall Faulk","Herschel Walker","Chuck Foreman"],"sport":"football","difficulty":"hard"},
{"q":"What is the Rooney Rule in the NFL?","a":"A policy requiring teams to interview minority candidates for head coaching vacancies","choices":["A policy requiring teams to interview minority candidates for head coaching vacancies","A rule limiting contract lengths","A salary cap exception for veterans","An anti-tampering rule"],"sport":"football","difficulty":"medium"},
{"q":"Which team won Super Bowl XXVIII?","a":"Dallas Cowboys","choices":["Dallas Cowboys","Buffalo Bills","San Francisco 49ers","Pittsburgh Steelers"],"sport":"football","difficulty":"hard"},
{"q":"Who scored six touchdowns in a single Super Bowl?","a":"No player has scored six touchdowns in a Super Bowl","choices":["No player has scored 6 TDs in a Super Bowl; Jerry Rice holds the record with 3","Jerry Rice (3 TDs in SB XXIX)","Emmitt Smith","Deion Branch"],"sport":"football","difficulty":"hard"},
{"q":"What does P.A.T. stand for in football?","a":"Point After Touchdown","choices":["Point After Touchdown","Passing Attempt Total","Penalty Assessment Term","Play Action Toss"],"sport":"football","difficulty":"easy"},
{"q":"Which team had the longest winning streak in NFL regular season history?","a":"New England Patriots (21 games from 2003-2004)","choices":["New England Patriots (21 games from 2003-2004)","Chicago Bears","Cleveland Browns","Indianapolis Colts"],"sport":"football","difficulty":"hard"},
{"q":"Who coached the Seattle Seahawks to their only Super Bowl title?","a":"Pete Carroll","choices":["Pete Carroll","Mike Holmgren","Dennis Erickson","Jim Mora Jr."],"sport":"football","difficulty":"medium"},
{"q":"Which quarterback threw the most interceptions in Super Bowl history in a single game?","a":"Rich Gannon (5 interceptions in Super Bowl XXXVII)","choices":["Rich Gannon (5 interceptions in Super Bowl XXXVII)","Peyton Manning","John Elway","Jim Kelly"],"sport":"football","difficulty":"hard"},
{"q":"What team does Jalen Hurts play for?","a":"Philadelphia Eagles","choices":["Philadelphia Eagles","Oklahoma City Thunder","Dallas Cowboys","Washington Commanders"],"sport":"football","difficulty":"easy"},
{"q":"Who won the Super Bowl MVP in Super Bowl XLIX?","a":"Tom Brady","choices":["Tom Brady","Julian Edelman","Brandon LaFell","Rob Gronkowski"],"sport":"football","difficulty":"medium"},
{"q":"Which player wore number 88 for the Dallas Cowboys and is in the Hall of Fame?","a":"Michael Irvin","choices":["Michael Irvin","Drew Pearson","Bob Hayes","Dez Bryant"],"sport":"football","difficulty":"medium"},
{"q":"What college did Joe Burrow attend?","a":"Louisiana State University (LSU)","choices":["Louisiana State University (LSU)","Ohio State","Alabama","Georgia"],"sport":"football","difficulty":"medium"},
{"q":"Which team won the 2026 Super Bowl?","a":"Philadelphia Eagles","choices":["Philadelphia Eagles","Kansas City Chiefs","Washington Commanders","Los Angeles Rams"],"sport":"football","difficulty":"medium"},

# ── HOCKEY — specific seasons and records ──
{"q":"Who won the NHL MVP in 2022 after a remarkable season?","a":"Auston Matthews","choices":["Auston Matthews","Connor McDavid","Nathan MacKinnon","Leon Draisaitl"],"sport":"hockey","difficulty":"medium"},
{"q":"Which team did Bobby Orr win his Norris Trophies (best defenseman) with?","a":"Boston Bruins","choices":["Boston Bruins","New York Rangers","Montreal Canadiens","Toronto Maple Leafs"],"sport":"hockey","difficulty":"medium"},
{"q":"Who scored the Stanley Cup-winning goal for the Colorado Avalanche in 2022?","a":"Andre Burakovsky","choices":["Andre Burakovsky","Nathan MacKinnon","Gabriel Landeskog","Mikko Rantanen"],"sport":"hockey","difficulty":"hard"},
{"q":"What team does Auston Matthews play for?","a":"Toronto Maple Leafs","choices":["Toronto Maple Leafs","Edmonton Oilers","Calgary Flames","Arizona Coyotes"],"sport":"hockey","difficulty":"easy"},
{"q":"Who holds the record for most goals by a defenseman in one NHL season?","a":"Paul Coffey (48 goals in 1985-86)","choices":["Paul Coffey (48 goals in 1985-86)","Bobby Orr","Denis Potvin","Ray Bourque"],"sport":"hockey","difficulty":"hard"},
{"q":"Which player was the first to score 800 career NHL goals?","a":"Wayne Gretzky","choices":["Wayne Gretzky","Gordie Howe","Brett Hull","Mario Lemieux"],"sport":"hockey","difficulty":"medium"},
{"q":"What team does Nathan MacKinnon play for?","a":"Colorado Avalanche","choices":["Colorado Avalanche","Carolina Hurricanes","Ottawa Senators","Minnesota Wild"],"sport":"hockey","difficulty":"easy"},
{"q":"Who holds the NHL record for most career plus-minus?","a":"Wayne Gretzky (+520 approximate)","choices":["Larry Robinson (+730)","Wayne Gretzky","Bobby Orr","Nicklas Lidstrom"],"sport":"hockey","difficulty":"hard"},
{"q":"Which team did Jacques Plante play for when he started wearing a goalie mask in a game in 1959?","a":"Montreal Canadiens","choices":["Montreal Canadiens","New York Rangers","Boston Bruins","Toronto Maple Leafs"],"sport":"hockey","difficulty":"hard"},
{"q":"How many goals did Wayne Gretzky score in the 1983-84 season?","a":"87 goals","choices":["87 goals","92 goals","73 goals","76 goals"],"sport":"hockey","difficulty":"hard"},
{"q":"Which player was known as 'Le Magnifique'?","a":"Mario Lemieux","choices":["Mario Lemieux","Guy Lafleur","Patrick Roy","Jean Beliveau"],"sport":"hockey","difficulty":"medium"},
{"q":"Who won the Calder Trophy in 2023?","a":"Matty Beniers","choices":["Matty Beniers","Cole Caufield","Kent Johnson","Owen Power"],"sport":"hockey","difficulty":"hard"},
{"q":"What team does Sidney Crosby play for?","a":"Pittsburgh Penguins","choices":["Pittsburgh Penguins","Boston Bruins","Washington Capitals","Ottawa Senators"],"sport":"hockey","difficulty":"easy"},
{"q":"Which player scored 76 goals in a single NHL season?","a":"Phil Esposito (76 in 1970-71)","choices":["Phil Esposito (76 in 1970-71)","Wayne Gretzky","Mario Lemieux","Brett Hull"],"sport":"hockey","difficulty":"hard"},
{"q":"Who was the first goalie to record 500 career wins?","a":"Martin Brodeur","choices":["Martin Brodeur","Patrick Roy","Ed Belfour","Dominik Hasek"],"sport":"hockey","difficulty":"medium"},
{"q":"Which team won the Stanley Cup in 2020?","a":"Tampa Bay Lightning","choices":["Tampa Bay Lightning","Dallas Stars","Vegas Golden Knights","Colorado Avalanche"],"sport":"hockey","difficulty":"medium"},
{"q":"What team does David Pastrnak play for?","a":"Boston Bruins","choices":["Boston Bruins","New York Rangers","Pittsburgh Penguins","Minnesota Wild"],"sport":"hockey","difficulty":"medium"},
{"q":"Who won the Norris Trophy in 2023?","a":"Erik Karlsson","choices":["Erik Karlsson","Cale Makar","Josh Morrissey","Victor Hedman"],"sport":"hockey","difficulty":"hard"},
{"q":"Which player holds the record for most career regular season games played in NHL history?","a":"Gordie Howe (1,767 games)","choices":["Gordie Howe (1,767 games)","Mark Messier","Ron Francis","Joe Sakic"],"sport":"hockey","difficulty":"hard"},
{"q":"What team does Elias Pettersson play for?","a":"Vancouver Canucks","choices":["Vancouver Canucks","Colorado Avalanche","Toronto Maple Leafs","Edmonton Oilers"],"sport":"hockey","difficulty":"medium"},
{"q":"Who won the Hart Trophy in 2020?","a":"Leon Draisaitl","choices":["Leon Draisaitl","Nathan MacKinnon","Connor McDavid","David Pastrnak"],"sport":"hockey","difficulty":"medium"},
{"q":"Which city do the Flyers play in?","a":"Philadelphia","choices":["Philadelphia","Pittsburgh","New York","Baltimore"],"sport":"hockey","difficulty":"easy"},
{"q":"Who is the all-time leader in NHL career assists?","a":"Wayne Gretzky (1,963 assists)","choices":["Wayne Gretzky (1,963 assists)","Ron Francis","Mark Messier","Ray Bourque"],"sport":"hockey","difficulty":"medium"},
{"q":"Which team plays at Enterprise Center?","a":"St. Louis Blues","choices":["St. Louis Blues","Nashville Predators","Columbus Blue Jackets","Minnesota Wild"],"sport":"hockey","difficulty":"medium"},
{"q":"Who was the last team to win three consecutive Stanley Cups?","a":"New York Islanders (1980-1983, four in a row)","choices":["New York Islanders won 4 straight (1980-83)","Montreal Canadiens (1976-79, four in a row)","Pittsburgh Penguins (1991-92)","Detroit Red Wings"],"sport":"hockey","difficulty":"hard"},
]

with open('questions.json') as f:
    existing = json.load(f)

existing_set = set(q['q'].strip().lower() for q in existing)
added = [q for q in new_questions if q['q'].strip().lower() not in existing_set]
existing.extend(added)

with open('questions.json', 'w') as f:
    json.dump(existing, f, indent=2)

print(f"Added {len(added)} questions. Total now: {len(existing)}")
