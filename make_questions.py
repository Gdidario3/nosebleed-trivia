#!/usr/bin/env python3
"""
Nosebleed Sports Trivia - Question Generator
Generates 10,000+ accurate sports trivia questions from curated data tables.
"""

import json
import random
import os

random.seed(42)

def shuffle_choices(correct, wrongs):
    choices = [correct] + wrongs[:3]
    random.shuffle(choices)
    return choices

def q(question, answer, wrongs, sport, difficulty):
    return {
        "q": question,
        "a": answer,
        "choices": shuffle_choices(answer, wrongs),
        "sport": sport,
        "difficulty": difficulty
    }

questions = []

# Load manually-written basketball questions
with open('/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/gen1_basketball.json') as f:
    questions.extend(json.load(f))

print(f"Loaded {len(questions)} basketball questions")

# ============================================================
# NFL CHAMPIONS DATA
# ============================================================
nfl_champs = [
    (2023, "Kansas City Chiefs", "San Francisco 49ers"),
    (2022, "Kansas City Chiefs", "Philadelphia Eagles"),
    (2021, "Los Angeles Rams", "Cincinnati Bengals"),
    (2020, "Tampa Bay Buccaneers", "Kansas City Chiefs"),
    (2019, "Kansas City Chiefs", "San Francisco 49ers"),
    (2018, "New England Patriots", "Los Angeles Rams"),
    (2017, "Philadelphia Eagles", "New England Patriots"),
    (2016, "New England Patriots", "Atlanta Falcons"),
    (2015, "Denver Broncos", "Carolina Panthers"),
    (2014, "New England Patriots", "Seattle Seahawks"),
    (2013, "Seattle Seahawks", "Denver Broncos"),
    (2012, "Baltimore Ravens", "San Francisco 49ers"),
    (2011, "New York Giants", "New England Patriots"),
    (2010, "Green Bay Packers", "Pittsburgh Steelers"),
    (2009, "New Orleans Saints", "Indianapolis Colts"),
    (2008, "Pittsburgh Steelers", "Arizona Cardinals"),
    (2007, "New York Giants", "New England Patriots"),
    (2006, "Indianapolis Colts", "Chicago Bears"),
    (2005, "Pittsburgh Steelers", "Seattle Seahawks"),
    (2004, "New England Patriots", "Philadelphia Eagles"),
    (2003, "New England Patriots", "Carolina Panthers"),
    (2002, "Tampa Bay Buccaneers", "Oakland Raiders"),
    (2001, "New England Patriots", "St. Louis Rams"),
    (2000, "Baltimore Ravens", "New York Giants"),
    (1999, "St. Louis Rams", "Tennessee Titans"),
    (1998, "Denver Broncos", "Atlanta Falcons"),
    (1997, "Denver Broncos", "Green Bay Packers"),
    (1996, "Green Bay Packers", "New England Patriots"),
    (1995, "Dallas Cowboys", "Pittsburgh Steelers"),
    (1994, "San Francisco 49ers", "San Diego Chargers"),
    (1993, "Dallas Cowboys", "Buffalo Bills"),
    (1992, "Dallas Cowboys", "Buffalo Bills"),
    (1991, "Washington Redskins", "Buffalo Bills"),
    (1990, "New York Giants", "Buffalo Bills"),
    (1989, "San Francisco 49ers", "Denver Broncos"),
    (1988, "San Francisco 49ers", "Cincinnati Bengals"),
    (1987, "Washington Redskins", "Denver Broncos"),
    (1986, "New York Giants", "Denver Broncos"),
    (1985, "Chicago Bears", "New England Patriots"),
    (1984, "San Francisco 49ers", "Miami Dolphins"),
    (1983, "Los Angeles Raiders", "Washington Redskins"),
    (1982, "Washington Redskins", "Miami Dolphins"),
    (1981, "San Francisco 49ers", "Cincinnati Bengals"),
    (1980, "Oakland Raiders", "Philadelphia Eagles"),
    (1979, "Pittsburgh Steelers", "Los Angeles Rams"),
    (1978, "Pittsburgh Steelers", "Dallas Cowboys"),
    (1977, "Dallas Cowboys", "Denver Broncos"),
    (1976, "Oakland Raiders", "Minnesota Vikings"),
    (1975, "Pittsburgh Steelers", "Dallas Cowboys"),
    (1974, "Pittsburgh Steelers", "Minnesota Vikings"),
    (1973, "Miami Dolphins", "Minnesota Vikings"),
    (1972, "Miami Dolphins", "Washington Redskins"),
    (1971, "Dallas Cowboys", "Miami Dolphins"),
    (1970, "Baltimore Colts", "Dallas Cowboys"),
    (1969, "Kansas City Chiefs", "Minnesota Vikings"),
    (1968, "New York Jets", "Baltimore Colts"),
    (1967, "Green Bay Packers", "Oakland Raiders"),
    (1966, "Green Bay Packers", "Kansas City Chiefs"),
]

all_nfl_teams = ["Kansas City Chiefs","San Francisco 49ers","New England Patriots","Dallas Cowboys",
    "Pittsburgh Steelers","Green Bay Packers","Chicago Bears","Miami Dolphins","Denver Broncos",
    "New York Giants","Los Angeles Rams","Seattle Seahawks","Baltimore Ravens","Tampa Bay Buccaneers",
    "Indianapolis Colts","Philadelphia Eagles","Oakland Raiders","Minnesota Vikings","Cincinnati Bengals",
    "Buffalo Bills","Washington Redskins","Tennessee Titans","San Diego Chargers","Carolina Panthers",
    "Atlanta Falcons","Arizona Cardinals","Jacksonville Jaguars","New Orleans Saints","Houston Texans",
    "New York Jets","Detroit Lions","Cleveland Browns","Los Angeles Chargers","Las Vegas Raiders"]

for yr, champ, runner_up in nfl_champs:
    wrongs = [t for t in all_nfl_teams if t not in [champ, runner_up]][:3]
    questions.append(q(
        f"Which team won the Super Bowl after the {yr} NFL season?",
        champ,
        [runner_up] + wrongs[:2],
        "football", "medium"
    ))
    questions.append(q(
        f"Which team lost the Super Bowl after the {yr} NFL season?",
        runner_up,
        [champ] + wrongs[:2],
        "football", "hard"
    ))

print(f"After NFL champs: {len(questions)}")

# NFL MVPs
nfl_mvps = [
    (2023, "Lamar Jackson"), (2022, "Patrick Mahomes"), (2021, "Cooper Kupp"),
    (2020, "Aaron Rodgers"), (2019, "Lamar Jackson"), (2018, "Patrick Mahomes"),
    (2017, "Carson Wentz"), (2016, "Matt Ryan"), (2015, "Cam Newton"),
    (2014, "Aaron Rodgers"), (2013, "Peyton Manning"), (2012, "Adrian Peterson"),
    (2011, "Aaron Rodgers"), (2010, "Tom Brady"), (2009, "Peyton Manning"),
    (2008, "Peyton Manning"), (2007, "Tom Brady"), (2006, "LaDainian Tomlinson"),
    (2005, "Shaun Alexander"), (2004, "Peyton Manning"), (2003, "Steve McNair and Peyton Manning"),
    (2002, "Rich Gannon"), (2001, "Kurt Warner"), (2000, "Marshall Faulk"),
    (1999, "Kurt Warner"), (1998, "Terrell Davis"), (1997, "Barry Sanders and Brett Favre"),
    (1996, "Brett Favre"), (1995, "Brett Favre"), (1994, "Steve Young"),
    (1993, "Emmitt Smith"), (1992, "Emmitt Smith"), (1991, "Thurman Thomas"),
    (1990, "Joe Montana"), (1989, "Joe Montana"), (1988, "Boomer Esiason"),
    (1987, "John Elway"), (1986, "Lawrence Taylor"), (1985, "Marcus Allen"),
    (1984, "Dan Marino"), (1983, "Joe Theismann"), (1982, "Mark Moseley"),
]

nfl_players = ["Patrick Mahomes","Tom Brady","Aaron Rodgers","Peyton Manning","Drew Brees","Brett Favre",
    "Lamar Jackson","Joe Montana","John Elway","LaDainian Tomlinson","Barry Sanders","Emmitt Smith",
    "Adrian Peterson","Kurt Warner","Steve Young","Dan Marino","Russell Wilson","Cam Newton",
    "Roger Staubach","Terry Bradshaw","Jim Kelly","Troy Aikman","Joe Namath","Fran Tarkenton",
    "Jerry Rice","Randy Moss","Terrell Owens","Lawrence Taylor","Reggie White","Deion Sanders"]

for yr, mvp in nfl_mvps:
    wrongs = [p for p in nfl_players if p != mvp]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the NFL MVP award for the {yr} season?",
        mvp,
        wrongs[:3],
        "football", "hard"
    ))

print(f"After NFL MVPs: {len(questions)}")

# ============================================================
# NFL TEAMS / PLAYERS DATA
# ============================================================
nfl_questions = [
    ("How many points is a touchdown worth in American football?", "6", ["7","5","8"], "easy"),
    ("The Super Bowl is the championship game of which league?", "NFL", ["CFL","AFL","USFL"], "easy"),
    ("Tom Brady won how many Super Bowl titles during his career?", "7", ["6","5","8"], "easy"),
    ("Which team has the most Super Bowl championships?", "New England Patriots", ["Pittsburgh Steelers","San Francisco 49ers","Dallas Cowboys"], "easy"),
    ("The Dallas Cowboys are nicknamed what?", "America's Team", ["The Cowboys","God's Team","The Legends"], "easy"),
    ("A field goal in football is worth how many points?", "3", ["2","4","1"], "easy"),
    ("Jerry Rice is widely considered the greatest at which position?", "Wide receiver", ["Quarterback","Running back","Tight end"], "easy"),
    ("How many players are on the field per team in American football?", "11", ["12","10","9"], "easy"),
    ("Peyton Manning played most of his career with which team?", "Indianapolis Colts", ["Denver Broncos","Tennessee Volunteers","New York Giants"], "easy"),
    ("The Lombardi Trophy is named after coach Vince Lombardi who coached which team?", "Green Bay Packers", ["Dallas Cowboys","Chicago Bears","New York Giants"], "easy"),
    ("Brett Favre played most of his career with which team?", "Green Bay Packers", ["Minnesota Vikings","New York Jets","Atlanta Falcons"], "easy"),
    ("How many yards is a first down in football?", "10 yards", ["5 yards","15 yards","20 yards"], "easy"),
    ("Joe Montana won how many Super Bowls with the San Francisco 49ers?", "4", ["3","5","2"], "easy"),
    ("Walter Payton was a legendary running back for which team?", "Chicago Bears", ["Houston Oilers","Los Angeles Rams","Pittsburgh Steelers"], "easy"),
    ("A safety in football scores how many points?", "2", ["1","3","4"], "easy"),
    ("Lawrence Taylor was known as what kind of player for the New York Giants?", "Linebacker", ["Defensive tackle","Cornerback","Safety"], "easy"),
    ("The Pittsburgh Steelers won how many Super Bowls total?", "6", ["4","5","7"], "easy"),
    ("John Elway spent his entire career with which team?", "Denver Broncos", ["San Francisco 49ers","New England Patriots","Miami Dolphins"], "easy"),
    ("Which player was known as 'The Bus' for the Pittsburgh Steelers?", "Jerome Bettis", ["Franco Harris","Barry Foster","Barry Sanders"], "easy"),
    ("Aaron Rodgers won his Super Bowl title with which team?", "Green Bay Packers", ["New York Jets","Tennessee Titans","Denver Broncos"], "easy"),
    ("Which quarterback holds the NFL record for most career passing yards?", "Tom Brady", ["Peyton Manning","Brett Favre","Drew Brees"], "medium"),
    ("Who was the first player to rush for 2,000 yards in a single NFL season?", "O.J. Simpson", ["Eric Dickerson","Barry Sanders","Earl Campbell"], "medium"),
    ("Which coach holds the record for most NFL wins?", "Don Shula", ["Bill Belichick","Chuck Noll","Tom Landry"], "medium"),
    ("Eric Dickerson set the single-season rushing record in 1984 with how many yards?", "2,105", ["1,997","2,003","2,050"], "medium"),
    ("The Miami Dolphins went undefeated in what season?", "1972", ["1974","1970","1975"], "medium"),
    ("The San Francisco 49ers' famous 'The Catch' was caught by which player?", "Dwight Clark", ["Jerry Rice","Roger Craig","Fred Dean"], "medium"),
    ("Randy Moss set the single-season touchdown reception record while playing for which team?", "New England Patriots", ["Minnesota Vikings","Oakland Raiders","San Francisco 49ers"], "medium"),
    ("Which player has the most career touchdown passes in NFL history?", "Tom Brady", ["Peyton Manning","Brett Favre","Drew Brees"], "medium"),
    ("Which running back holds the record for most career rushing yards?", "Emmitt Smith", ["Walter Payton","Barry Sanders","Frank Gore"], "medium"),
    ("Drew Brees spent most of his career with which team?", "New Orleans Saints", ["San Diego Chargers","Indianapolis Colts","Denver Broncos"], "medium"),
    ("The Minnesota Vikings lost how many Super Bowls?", "4", ["3","5","2"], "medium"),
    ("Which player made the 'Helmet Catch' in Super Bowl XLII for the New York Giants?", "David Tyree", ["Plaxico Burress","Amani Toomer","Steve Smith"], "medium"),
    ("LaDainian Tomlinson set the single-season touchdown record in 2006 with how many?", "28", ["26","31","23"], "medium"),
    ("Who was the NFL's first Black head coach in the modern era?", "Art Shell", ["Tony Dungy","Mike Tomlin","Lovie Smith"], "medium"),
    ("Which receiver holds the record for most touchdown receptions in NFL history?", "Jerry Rice", ["Randy Moss","Terrell Owens","Steve Smith"], "medium"),
    ("Which team did Reggie White play for in the 1996 Super Bowl-winning season?", "Green Bay Packers", ["Philadelphia Eagles","Carolina Panthers","San Francisco 49ers"], "medium"),
    ("In 2007, the Patriots went undefeated in the regular season. What was their record?", "16-0", ["15-1","14-2","17-0"], "medium"),
    ("Ray Lewis won his first Super Bowl title with the Baltimore Ravens in which year?", "2001", ["2000","2003","2006"], "medium"),
    ("Who quarterbacked the New York Jets to their only Super Bowl win?", "Joe Namath", ["Matt Snell","Don Maynard","Emerson Boozer"], "medium"),
    ("Which player holds the NFL record for most career interceptions?", "Paul Krause", ["Night Train Lane","Emlen Tunnell","Rod Woodson"], "hard"),
    ("The AFL was founded in what year?", "1960", ["1955","1962","1958"], "hard"),
    ("The 1958 NFL Championship Game is often called what?", "The Greatest Game Ever Played", ["The OT Classic","The Ice Bowl","The Century Game"], "hard"),
    ("Who was the head coach of the Miami Dolphins during their perfect 1972 season?", "Don Shula", ["Bud Grant","Tom Landry","George Allen"], "hard"),
    ("Jim Brown averaged how many yards per carry in his NFL career?", "5.22", ["4.87","5.65","4.51"], "hard"),
    ("Which player holds the NFL record for most career sacks?", "Bruce Smith", ["Reggie White","Lawrence Taylor","Deacon Jones"], "hard"),
    ("The '46 Defense' was pioneered by which coach?", "Buddy Ryan", ["Tom Landry","Bill Walsh","Don Shula"], "hard"),
    ("Walter Payton's career rushing average per carry was?", "4.4 yards per carry", ["5.0 yards per carry","3.9 yards per carry","4.8 yards per carry"], "hard"),
    ("The Dallas Cowboys were originally founded and coached by whom?", "Tom Landry", ["Jimmy Johnson","Barry Switzer","Wade Phillips"], "hard"),
    ("Which team did the Houston Oilers become after relocating?", "Tennessee Titans", ["Jacksonville Jaguars","Baltimore Ravens","Carolina Panthers"], "hard"),
    ("Deacon Jones popularized what term for sacking the quarterback?", "Sack", ["Blitz","Rush","Pressure"], "hard"),
    ("Art Rooney founded which NFL franchise in 1933?", "Pittsburgh Steelers", ["Chicago Bears","Baltimore Colts","Detroit Lions"], "hard"),
    ("What year did the Cleveland Browns win their last NFL Championship?", "1964", ["1954","1957","1968"], "hard"),
    ("The 'Ice Bowl' game in 1967 between Green Bay and Dallas was played at what temperature?", "-13 degrees Fahrenheit", ["-20 degrees Fahrenheit","-5 degrees Fahrenheit","0 degrees Fahrenheit"], "hard"),
    ("Which college did Jerry Rice attend before being drafted?", "Mississippi Valley State", ["Notre Dame","Alabama","USC"], "hard"),
    ("The Buffalo Bills lost 4 consecutive Super Bowls from 1991 to 1994. Their record was?", "0-4", ["1-3","2-2","0-3"], "hard"),
    ("Who was the first tight end inducted into the Pro Football Hall of Fame?", "Mike Ditka", ["Ozzie Newsome","Dave Casper","Jackie Smith"], "hard"),
    ("Super Bowl XVIII saw the Los Angeles Raiders defeat which team?", "Washington Redskins", ["Miami Dolphins","Pittsburgh Steelers","New York Giants"], "hard"),
    ("The Houston Texans joined the NFL as an expansion team in which year?", "2002", ["1999","2005","2000"], "hard"),
    ("The 'Music City Miracle' in 2000 was a touchdown for which team?", "Tennessee Titans", ["Jacksonville Jaguars","Indianapolis Colts","New York Jets"], "hard"),
    ("The NFL introduced the two-point conversion in which year?", "1994", ["1990","1998","1986"], "hard"),
    ("Who was the MVP of Super Bowl XI in 1977 for the Oakland Raiders?", "Fred Biletnikoff", ["Ken Stabler","Clarence Davis","Willie Brown"], "hard"),
    ("Which player is credited with the most interceptions in a single season (14 in 1952)?", "Night Train Lane", ["Paul Krause","Mel Blount","Darrell Green"], "hard"),
    ("John Madden won his only Super Bowl as head coach with which team?", "Oakland Raiders (Super Bowl XI)", ["Pittsburgh Steelers","Dallas Cowboys","Miami Dolphins"], "hard"),
    ("Emmitt Smith became the NFL's all-time leading rusher by surpassing whose record?", "Walter Payton", ["Barry Sanders","Eric Dickerson","Jim Brown"], "hard"),
    ("Which team won the NFC Championship three years in a row from 1988 to 1990?", "San Francisco 49ers", ["New York Giants","Los Angeles Rams","Chicago Bears"], "hard"),
    ("Marcus Allen won the Super Bowl MVP in Super Bowl XVIII playing for which team?", "Los Angeles Raiders", ["Kansas City Chiefs","San Diego Chargers","Denver Broncos"], "hard"),
    ("The Carolina Panthers and Jacksonville Jaguars entered the NFL as expansion teams in which year?", "1995", ["1993","1997","1992"], "hard"),
]

for text, ans, wrongs, diff in nfl_questions:
    questions.append(q(text, ans, wrongs, "football", diff))

print(f"After NFL questions: {len(questions)}")

# ============================================================
# NBA CHAMPIONS DATA (additional from data)
# ============================================================
nba_champs = [
    (2023, "Denver Nuggets", "Miami Heat"),
    (2022, "Golden State Warriors", "Boston Celtics"),
    (2021, "Milwaukee Bucks", "Phoenix Suns"),
    (2020, "Los Angeles Lakers", "Miami Heat"),
    (2019, "Toronto Raptors", "Golden State Warriors"),
    (2018, "Golden State Warriors", "Cleveland Cavaliers"),
    (2017, "Golden State Warriors", "Cleveland Cavaliers"),
    (2016, "Cleveland Cavaliers", "Golden State Warriors"),
    (2015, "Golden State Warriors", "Cleveland Cavaliers"),
    (2014, "San Antonio Spurs", "Miami Heat"),
    (2013, "Miami Heat", "San Antonio Spurs"),
    (2012, "Miami Heat", "Oklahoma City Thunder"),
    (2011, "Dallas Mavericks", "Miami Heat"),
    (2010, "Los Angeles Lakers", "Boston Celtics"),
    (2009, "Los Angeles Lakers", "Orlando Magic"),
    (2008, "Boston Celtics", "Los Angeles Lakers"),
    (2007, "San Antonio Spurs", "Cleveland Cavaliers"),
    (2006, "Miami Heat", "Dallas Mavericks"),
    (2005, "San Antonio Spurs", "Detroit Pistons"),
    (2004, "Detroit Pistons", "Los Angeles Lakers"),
    (2003, "San Antonio Spurs", "New Jersey Nets"),
    (2002, "Los Angeles Lakers", "New Jersey Nets"),
    (2001, "Los Angeles Lakers", "Philadelphia 76ers"),
    (2000, "Los Angeles Lakers", "Indiana Pacers"),
    (1999, "San Antonio Spurs", "New York Knicks"),
    (1998, "Chicago Bulls", "Utah Jazz"),
    (1997, "Chicago Bulls", "Utah Jazz"),
    (1996, "Chicago Bulls", "Seattle SuperSonics"),
    (1995, "Houston Rockets", "Orlando Magic"),
    (1994, "Houston Rockets", "New York Knicks"),
    (1993, "Chicago Bulls", "Phoenix Suns"),
    (1992, "Chicago Bulls", "Portland Trail Blazers"),
    (1991, "Chicago Bulls", "Los Angeles Lakers"),
    (1990, "Detroit Pistons", "Portland Trail Blazers"),
    (1989, "Detroit Pistons", "Los Angeles Lakers"),
    (1988, "Los Angeles Lakers", "Detroit Pistons"),
    (1987, "Los Angeles Lakers", "Boston Celtics"),
    (1986, "Boston Celtics", "Houston Rockets"),
    (1985, "Los Angeles Lakers", "Boston Celtics"),
    (1984, "Boston Celtics", "Los Angeles Lakers"),
    (1983, "Philadelphia 76ers", "Los Angeles Lakers"),
    (1982, "Los Angeles Lakers", "Philadelphia 76ers"),
    (1981, "Boston Celtics", "Houston Rockets"),
    (1980, "Los Angeles Lakers", "Philadelphia 76ers"),
    (1979, "Seattle SuperSonics", "Washington Bullets"),
    (1978, "Washington Bullets", "Seattle SuperSonics"),
    (1977, "Portland Trail Blazers", "Philadelphia 76ers"),
    (1976, "Boston Celtics", "Phoenix Suns"),
    (1975, "Golden State Warriors", "Washington Bullets"),
    (1974, "Boston Celtics", "Milwaukee Bucks"),
    (1973, "New York Knicks", "Los Angeles Lakers"),
    (1972, "Los Angeles Lakers", "New York Knicks"),
    (1971, "Milwaukee Bucks", "Baltimore Bullets"),
    (1970, "New York Knicks", "Los Angeles Lakers"),
    (1969, "Boston Celtics", "Los Angeles Lakers"),
    (1968, "Boston Celtics", "Los Angeles Lakers"),
    (1967, "Philadelphia 76ers", "San Francisco Warriors"),
    (1966, "Boston Celtics", "Los Angeles Lakers"),
    (1965, "Boston Celtics", "Los Angeles Lakers"),
    (1964, "Boston Celtics", "San Francisco Warriors"),
    (1963, "Boston Celtics", "Los Angeles Lakers"),
    (1962, "Boston Celtics", "Los Angeles Lakers"),
    (1961, "Boston Celtics", "St. Louis Hawks"),
    (1960, "Boston Celtics", "St. Louis Hawks"),
    (1959, "Boston Celtics", "Minneapolis Lakers"),
    (1958, "St. Louis Hawks", "Boston Celtics"),
    (1957, "Boston Celtics", "St. Louis Hawks"),
    (1956, "Philadelphia Warriors", "Fort Wayne Pistons"),
]

all_nba_teams = ["Boston Celtics","Los Angeles Lakers","Chicago Bulls","San Antonio Spurs",
    "Golden State Warriors","Miami Heat","Detroit Pistons","Houston Rockets","Cleveland Cavaliers",
    "Oklahoma City Thunder","Dallas Mavericks","Toronto Raptors","Milwaukee Bucks","Denver Nuggets",
    "New York Knicks","Philadelphia 76ers","Phoenix Suns","Portland Trail Blazers","Utah Jazz",
    "Indiana Pacers","Atlanta Hawks","Brooklyn Nets","Sacramento Kings","Minnesota Timberwolves",
    "Memphis Grizzlies","New Orleans Pelicans","Orlando Magic","Washington Wizards","Charlotte Hornets"]

for yr, champ, runner_up in nba_champs:
    wrongs = [t for t in all_nba_teams if t not in [champ, runner_up]][:3]
    questions.append(q(
        f"Which team won the NBA championship in {yr}?",
        champ,
        [runner_up] + wrongs[:2],
        "basketball", "medium"
    ))

print(f"After NBA champs: {len(questions)}")

# NBA Draft data
nba_draft_1st_picks = [
    (2023, "Victor Wembanyama", "San Antonio Spurs"),
    (2022, "Paolo Banchero", "Orlando Magic"),
    (2021, "Cade Cunningham", "Detroit Pistons"),
    (2020, "Anthony Edwards", "Minnesota Timberwolves"),
    (2019, "Zion Williamson", "New Orleans Pelicans"),
    (2018, "Deandre Ayton", "Phoenix Suns"),
    (2017, "Markelle Fultz", "Philadelphia 76ers"),
    (2016, "Ben Simmons", "Philadelphia 76ers"),
    (2015, "Karl-Anthony Towns", "Minnesota Timberwolves"),
    (2014, "Andrew Wiggins", "Cleveland Cavaliers"),
    (2013, "Anthony Bennett", "Cleveland Cavaliers"),
    (2012, "Anthony Davis", "New Orleans Hornets"),
    (2011, "Kyrie Irving", "Cleveland Cavaliers"),
    (2010, "John Wall", "Washington Wizards"),
    (2009, "Blake Griffin", "Los Angeles Clippers"),
    (2008, "Derrick Rose", "Chicago Bulls"),
    (2007, "Greg Oden", "Portland Trail Blazers"),
    (2006, "Andrea Bargnani", "Toronto Raptors"),
    (2005, "Andrew Bogut", "Milwaukee Bucks"),
    (2004, "Dwight Howard", "Orlando Magic"),
    (2003, "LeBron James", "Cleveland Cavaliers"),
    (2002, "Yao Ming", "Houston Rockets"),
    (2001, "Kwame Brown", "Washington Wizards"),
    (2000, "Kenyon Martin", "New Jersey Nets"),
    (1999, "Elton Brand", "Chicago Bulls"),
    (1998, "Michael Olowokandi", "Los Angeles Clippers"),
    (1997, "Tim Duncan", "San Antonio Spurs"),
    (1996, "Allen Iverson", "Philadelphia 76ers"),
    (1995, "Joe Smith", "Golden State Warriors"),
    (1994, "Glenn Robinson", "Milwaukee Bucks"),
    (1993, "Chris Webber", "Orlando Magic"),
    (1992, "Shaquille O'Neal", "Orlando Magic"),
    (1991, "Larry Johnson", "Charlotte Hornets"),
    (1990, "Derrick Coleman", "New Jersey Nets"),
    (1989, "Pervis Ellison", "Sacramento Kings"),
    (1988, "Danny Manning", "Los Angeles Clippers"),
    (1987, "David Robinson", "San Antonio Spurs"),
    (1986, "Brad Daugherty", "Cleveland Cavaliers"),
    (1985, "Patrick Ewing", "New York Knicks"),
    (1984, "Hakeem Olajuwon", "Houston Rockets"),
    (1983, "Ralph Sampson", "Houston Rockets"),
    (1982, "James Worthy", "Los Angeles Lakers"),
    (1981, "Mark Aguirre", "Dallas Mavericks"),
    (1980, "Joe Barry Carroll", "Golden State Warriors"),
    (1979, "Earvin Magic Johnson", "Los Angeles Lakers"),
    (1978, "Mychal Thompson", "Portland Trail Blazers"),
    (1977, "Kent Benson", "Milwaukee Bucks"),
    (1976, "John Lucas", "Houston Rockets"),
    (1975, "David Thompson", "Atlanta Hawks"),
    (1974, "Bill Walton", "Portland Trail Blazers"),
    (1973, "Doug Collins", "Philadelphia 76ers"),
    (1972, "LaRue Martin", "Portland Trail Blazers"),
    (1971, "Austin Carr", "Cleveland Cavaliers"),
    (1970, "Bob Lanier", "Detroit Pistons"),
    (1969, "Kareem Abdul-Jabbar", "Milwaukee Bucks"),
    (1968, "Elvin Hayes", "San Diego Rockets"),
    (1967, "Jimmy Walker", "Detroit Pistons"),
    (1966, "Cazzie Russell", "New York Knicks"),
    (1965, "Fred Hetzel", "San Francisco Warriors"),
]

nba_players = ["Victor Wembanyama","Paolo Banchero","Cade Cunningham","Anthony Edwards","Zion Williamson",
    "Deandre Ayton","Markelle Fultz","Ben Simmons","Karl-Anthony Towns","Andrew Wiggins","Anthony Davis",
    "Kyrie Irving","John Wall","Blake Griffin","Derrick Rose","Greg Oden","Andrea Bargnani","Andrew Bogut",
    "Dwight Howard","LeBron James","Yao Ming","Kwame Brown","Tim Duncan","Allen Iverson","Shaquille O'Neal",
    "Patrick Ewing","Hakeem Olajuwon","Ralph Sampson","James Worthy","Magic Johnson","Bill Walton"]

for yr, player, team in nba_draft_1st_picks:
    wrongs_p = [p for p in nba_players if p != player]
    random.shuffle(wrongs_p)
    wrongs_t = [t for t in all_nba_teams if t != team]
    random.shuffle(wrongs_t)
    questions.append(q(
        f"Who was the first overall pick in the {yr} NBA Draft?",
        player,
        wrongs_p[:3],
        "basketball", "hard"
    ))
    questions.append(q(
        f"Which team selected {player} with the first overall pick in the {yr} NBA Draft?",
        team,
        wrongs_t[:3],
        "basketball", "hard"
    ))

print(f"After NBA draft picks: {len(questions)}")

# ============================================================
# BASEBALL DATA
# ============================================================
mlb_ws_champs = [
    (2023, "Texas Rangers", "Arizona Diamondbacks"),
    (2022, "Houston Astros", "Philadelphia Phillies"),
    (2021, "Atlanta Braves", "Houston Astros"),
    (2020, "Los Angeles Dodgers", "Tampa Bay Rays"),
    (2019, "Washington Nationals", "Houston Astros"),
    (2018, "Boston Red Sox", "Los Angeles Dodgers"),
    (2017, "Houston Astros", "Los Angeles Dodgers"),
    (2016, "Chicago Cubs", "Cleveland Indians"),
    (2015, "Kansas City Royals", "New York Mets"),
    (2014, "San Francisco Giants", "Kansas City Royals"),
    (2013, "Boston Red Sox", "St. Louis Cardinals"),
    (2012, "San Francisco Giants", "Detroit Tigers"),
    (2011, "St. Louis Cardinals", "Texas Rangers"),
    (2010, "San Francisco Giants", "Texas Rangers"),
    (2009, "New York Yankees", "Philadelphia Phillies"),
    (2008, "Philadelphia Phillies", "Tampa Bay Rays"),
    (2007, "Boston Red Sox", "Colorado Rockies"),
    (2006, "St. Louis Cardinals", "Detroit Tigers"),
    (2005, "Chicago White Sox", "Houston Astros"),
    (2004, "Boston Red Sox", "St. Louis Cardinals"),
    (2003, "Florida Marlins", "New York Yankees"),
    (2002, "Anaheim Angels", "San Francisco Giants"),
    (2001, "Arizona Diamondbacks", "New York Yankees"),
    (2000, "New York Yankees", "New York Mets"),
    (1999, "New York Yankees", "Atlanta Braves"),
    (1998, "New York Yankees", "San Diego Padres"),
    (1997, "Florida Marlins", "Cleveland Indians"),
    (1996, "New York Yankees", "Atlanta Braves"),
    (1995, "Atlanta Braves", "Cleveland Indians"),
    (1993, "Toronto Blue Jays", "Philadelphia Phillies"),
    (1992, "Toronto Blue Jays", "Atlanta Braves"),
    (1991, "Minnesota Twins", "Atlanta Braves"),
    (1990, "Cincinnati Reds", "Oakland Athletics"),
    (1989, "Oakland Athletics", "San Francisco Giants"),
    (1988, "Los Angeles Dodgers", "Oakland Athletics"),
    (1987, "Minnesota Twins", "St. Louis Cardinals"),
    (1986, "New York Mets", "Boston Red Sox"),
    (1985, "Kansas City Royals", "St. Louis Cardinals"),
    (1984, "Detroit Tigers", "San Diego Padres"),
    (1983, "Baltimore Orioles", "Philadelphia Phillies"),
    (1982, "St. Louis Cardinals", "Milwaukee Brewers"),
    (1981, "Los Angeles Dodgers", "New York Yankees"),
    (1980, "Philadelphia Phillies", "Kansas City Royals"),
    (1979, "Pittsburgh Pirates", "Baltimore Orioles"),
    (1978, "New York Yankees", "Los Angeles Dodgers"),
    (1977, "New York Yankees", "Los Angeles Dodgers"),
    (1976, "Cincinnati Reds", "New York Yankees"),
    (1975, "Cincinnati Reds", "Boston Red Sox"),
    (1974, "Oakland Athletics", "Los Angeles Dodgers"),
    (1973, "Oakland Athletics", "New York Mets"),
    (1972, "Oakland Athletics", "Cincinnati Reds"),
    (1971, "Pittsburgh Pirates", "Baltimore Orioles"),
    (1970, "Baltimore Orioles", "Cincinnati Reds"),
    (1969, "New York Mets", "Baltimore Orioles"),
    (1968, "Detroit Tigers", "St. Louis Cardinals"),
    (1967, "St. Louis Cardinals", "Boston Red Sox"),
    (1966, "Baltimore Orioles", "Los Angeles Dodgers"),
    (1965, "Los Angeles Dodgers", "Minnesota Twins"),
    (1964, "St. Louis Cardinals", "New York Yankees"),
    (1963, "Los Angeles Dodgers", "New York Yankees"),
    (1962, "New York Yankees", "San Francisco Giants"),
    (1961, "New York Yankees", "Cincinnati Reds"),
    (1960, "Pittsburgh Pirates", "New York Yankees"),
    (1959, "Los Angeles Dodgers", "Chicago White Sox"),
    (1958, "New York Yankees", "Milwaukee Braves"),
    (1957, "Milwaukee Braves", "New York Yankees"),
    (1956, "New York Yankees", "Brooklyn Dodgers"),
    (1955, "Brooklyn Dodgers", "New York Yankees"),
    (1954, "New York Giants", "Cleveland Indians"),
    (1953, "New York Yankees", "Brooklyn Dodgers"),
    (1952, "New York Yankees", "Brooklyn Dodgers"),
    (1951, "New York Yankees", "New York Giants"),
    (1950, "New York Yankees", "Philadelphia Phillies"),
    (1949, "New York Yankees", "Brooklyn Dodgers"),
    (1948, "Cleveland Indians", "Boston Braves"),
    (1947, "New York Yankees", "Brooklyn Dodgers"),
    (1946, "St. Louis Cardinals", "Boston Red Sox"),
    (1945, "Detroit Tigers", "Chicago Cubs"),
    (1944, "St. Louis Cardinals", "St. Louis Browns"),
    (1943, "New York Yankees", "St. Louis Cardinals"),
    (1942, "St. Louis Cardinals", "New York Yankees"),
    (1941, "New York Yankees", "Brooklyn Dodgers"),
    (1940, "Cincinnati Reds", "Detroit Tigers"),
    (1939, "New York Yankees", "Cincinnati Reds"),
    (1938, "New York Yankees", "Chicago Cubs"),
    (1937, "New York Yankees", "New York Giants"),
    (1936, "New York Yankees", "New York Giants"),
    (1935, "Detroit Tigers", "Chicago Cubs"),
    (1934, "St. Louis Cardinals", "Detroit Tigers"),
    (1933, "New York Giants", "Washington Senators"),
    (1932, "New York Yankees", "Chicago Cubs"),
    (1931, "St. Louis Cardinals", "Philadelphia Athletics"),
    (1930, "Philadelphia Athletics", "St. Louis Cardinals"),
    (1929, "Philadelphia Athletics", "Chicago Cubs"),
    (1928, "New York Yankees", "St. Louis Cardinals"),
    (1927, "New York Yankees", "Pittsburgh Pirates"),
    (1926, "St. Louis Cardinals", "New York Yankees"),
    (1925, "Pittsburgh Pirates", "Washington Senators"),
    (1924, "Washington Senators", "New York Giants"),
    (1923, "New York Yankees", "New York Giants"),
    (1922, "New York Giants", "New York Yankees"),
    (1921, "New York Giants", "New York Yankees"),
    (1920, "Cleveland Indians", "Brooklyn Robins"),
    (1919, "Cincinnati Reds", "Chicago White Sox"),
    (1918, "Boston Red Sox", "Chicago Cubs"),
    (1917, "Chicago White Sox", "New York Giants"),
    (1916, "Boston Red Sox", "Brooklyn Robins"),
    (1915, "Boston Red Sox", "Philadelphia Phillies"),
    (1914, "Boston Braves", "Philadelphia Athletics"),
    (1913, "Philadelphia Athletics", "New York Giants"),
    (1912, "Boston Red Sox", "New York Giants"),
    (1911, "Philadelphia Athletics", "New York Giants"),
    (1910, "Philadelphia Athletics", "Chicago Cubs"),
    (1909, "Pittsburgh Pirates", "Detroit Tigers"),
    (1908, "Chicago Cubs", "Detroit Tigers"),
    (1907, "Chicago Cubs", "Detroit Tigers"),
    (1906, "Chicago White Sox", "Chicago Cubs"),
    (1905, "New York Giants", "Philadelphia Athletics"),
    (1904, "No World Series played", "No World Series played"),
    (1903, "Boston Americans", "Pittsburgh Pirates"),
]

all_mlb_teams = ["New York Yankees","Boston Red Sox","Los Angeles Dodgers","San Francisco Giants",
    "Chicago Cubs","St. Louis Cardinals","Oakland Athletics","Atlanta Braves","Cincinnati Reds",
    "Pittsburgh Pirates","Detroit Tigers","Cleveland Indians","Minnesota Twins","Baltimore Orioles",
    "Kansas City Royals","Philadelphia Phillies","Toronto Blue Jays","Houston Astros","Texas Rangers",
    "Seattle Mariners","Colorado Rockies","Arizona Diamondbacks","Tampa Bay Rays","Miami Marlins",
    "Washington Nationals","San Diego Padres","Milwaukee Brewers","Chicago White Sox","New York Mets"]

for yr, champ, runner_up in mlb_ws_champs:
    if champ == "No World Series played":
        continue
    wrongs = [t for t in all_mlb_teams if t not in [champ, runner_up]][:3]
    questions.append(q(
        f"Which team won the World Series in {yr}?",
        champ,
        [runner_up] + wrongs[:2],
        "baseball", "medium"
    ))

print(f"After MLB WS champs: {len(questions)}")

# Additional baseball static questions
baseball_questions = [
    ("How many outs are in an inning per team in baseball?", "3", ["4","2","6"], "easy"),
    ("Babe Ruth hit how many career home runs?", "714", ["755","762","660"], "easy"),
    ("Who was known as 'The Say Hey Kid'?", "Willie Mays", ["Hank Aaron","Ken Griffey Jr.","Mickey Mantle"], "easy"),
    ("How many bases are on a baseball diamond?", "4", ["3","5","6"], "easy"),
    ("Derek Jeter played his entire career with which team?", "New York Yankees", ["Boston Red Sox","Chicago White Sox","Toronto Blue Jays"], "easy"),
    ("Who holds the MLB record for most career home runs?", "Barry Bonds", ["Hank Aaron","Babe Ruth","Alex Rodriguez"], "easy"),
    ("The Boston Red Sox broke their 86-year drought by winning the World Series in what year?", "2004", ["2000","2007","1986"], "easy"),
    ("How many players are in a standard batting lineup in baseball?", "9", ["8","10","11"], "easy"),
    ("What does ERA stand for in baseball?", "Earned Run Average", ["Extra Runs Allowed","Earned Runs Allowed","Extra Run Average"], "easy"),
    ("The 2016 World Series was won by the Chicago Cubs after a drought of how many years?", "108", ["87","71","45"], "easy"),
    ("Jackie Robinson broke the color barrier in MLB playing for which team in 1947?", "Brooklyn Dodgers", ["New York Giants","Boston Braves","Cincinnati Reds"], "easy"),
    ("Mariano Rivera played for which team his entire career?", "New York Yankees", ["Chicago White Sox","Boston Red Sox","Houston Astros"], "easy"),
    ("The MLB regular season consists of how many games?", "162", ["154","145","180"], "easy"),
    ("What is a 'perfect game' in baseball?", "Retiring all 27 batters without a hit, walk, or error", ["Winning 1-0","Striking out every batter","Hitting a home run in every at-bat"], "easy"),
    ("Lou Gehrig was nicknamed what?", "The Iron Horse", ["The Bambino","The Sultan of Swat","The Kid"], "easy"),
    ("Cal Ripken Jr. broke Lou Gehrig's consecutive games record. How many games did Ripken play in a row?", "2,632", ["2,130","2,514","2,800"], "medium"),
    ("Which pitcher had the most no-hitters in MLB history?", "Nolan Ryan", ["Sandy Koufax","Randy Johnson","Bob Feller"], "medium"),
    ("Roger Maris broke Babe Ruth's single-season home run record in 1961 with how many?", "61", ["60","65","58"], "medium"),
    ("Joe DiMaggio had a consecutive-game hitting streak of how many games in 1941?", "56", ["44","61","50"], "medium"),
    ("Pete Rose is the all-time MLB hits leader with how many career hits?", "4,256", ["3,980","4,102","3,771"], "medium"),
    ("In 1998, Mark McGwire hit 70 home runs. Which team was he playing for?", "St. Louis Cardinals", ["Oakland Athletics","Pittsburgh Pirates","Cincinnati Reds"], "medium"),
    ("Which pitcher won the most Cy Young Awards with 7?", "Roger Clemens", ["Randy Johnson","Greg Maddux","Tom Seaver"], "medium"),
    ("Mickey Mantle's primary position was?", "Center field", ["Shortstop","Third base","Left field"], "medium"),
    ("Roberto Clemente played his career with which team before dying in a plane crash?", "Pittsburgh Pirates", ["Atlanta Braves","Cincinnati Reds","San Francisco Giants"], "medium"),
    ("Ted Williams was the last player to hit .400 in a season. What was his average?", ".406", [".412",".394",".401"], "medium"),
    ("Which team won the most World Series titles in the 1950s?", "New York Yankees", ["Brooklyn Dodgers","Milwaukee Braves","Cleveland Indians"], "medium"),
    ("Mike Trout has played his entire career with which team?", "Los Angeles Angels", ["Boston Red Sox","Houston Astros","Cleveland Guardians"], "medium"),
    ("What position did Ozzie Smith famously play?", "Shortstop", ["Second base","Third base","Outfield"], "medium"),
    ("Barry Bonds set the single-season on-base percentage record in 2004. What was it?", ".609", [".565",".588",".523"], "medium"),
    ("Ichiro Suzuki set the single-season hits record in 2004 with how many?", "262", ["257","248","270"], "medium"),
    ("Which player holds the MLB record for most career stolen bases?", "Rickey Henderson", ["Lou Brock","Tim Raines","Vince Coleman"], "hard"),
    ("Bob Gibson's ERA in 1968 was what, considered one of the best ever?", "1.12", ["0.96","1.45","1.27"], "hard"),
    ("The 1919 Black Sox Scandal involved players from which team throwing the World Series?", "Chicago White Sox", ["New York Giants","Cincinnati Reds","Detroit Tigers"], "hard"),
    ("Which pitcher threw the first perfect game in World Series history?", "Don Larsen", ["Sandy Koufax","Whitey Ford","Bob Gibson"], "hard"),
    ("Cy Young won how many career games?", "511", ["482","530","490"], "hard"),
    ("What was Hack Wilson's RBI record set in 1930?", "191", ["184","202","175"], "hard"),
    ("Rogers Hornsby's batting average in 1924 was what?", ".424", [".406",".440",".398"], "hard"),
    ("Which player had the highest career batting average in MLB history?", "Ty Cobb (.366)", ["Rogers Hornsby (.358)","Shoeless Joe Jackson (.356)","Tris Speaker (.345)"], "hard"),
    ("The 'Pine Tar Incident' of 1983 involved George Brett of which team?", "Kansas City Royals", ["New York Yankees","Boston Red Sox","Detroit Tigers"], "hard"),
    ("Pete Rose was banned from baseball for life for what reason?", "Betting on baseball games", ["Using steroids","Match fixing","Throwing games"], "hard"),
    ("The first World Series was played in which year?", "1903", ["1910","1897","1908"], "hard"),
    ("Which pitcher was known as 'Big Train' for his fastball?", "Walter Johnson", ["Cy Young","Grover Cleveland Alexander","Pete Alexander"], "hard"),
    ("Eddie Gaedel, the shortest player to bat in baseball, was how tall?", "3 feet 7 inches", ["4 feet 0 inches","3 feet 9 inches","4 feet 3 inches"], "hard"),
    ("Which team won the only championship for Brooklyn in 1955?", "Brooklyn Dodgers", ["New York Giants","Cleveland Indians","Milwaukee Braves"], "hard"),
    ("What year did the Montreal Expos become the Washington Nationals?", "2005", ["2002","2007","2004"], "hard"),
    ("Which pitcher holds the record for most strikeouts in a single game at 20?", "Roger Clemens and Kerry Wood (tied)", ["Nolan Ryan","Randy Johnson","Bob Feller"], "hard"),
    ("Babe Ruth was sold from the Boston Red Sox to the New York Yankees for how much?", "$100,000", ["$50,000","$200,000","$75,000"], "hard"),
    ("Satchel Paige was the oldest player to start a major league game. How old was he when he last pitched?", "59", ["52","47","55"], "hard"),
    ("Sandy Koufax struck out how many batters in his 1965 perfect game?", "14", ["12","27","9"], "hard"),
    ("What year did Nolan Ryan throw his 7th and final no-hitter?", "1991", ["1989","1993","1987"], "hard"),
    ("Which catcher won the most Gold Glove awards?", "Ivan Rodriguez (13)", ["Johnny Bench (10)","Yadier Molina (9)","Bob Boone (7)"], "hard"),
    ("The Oakland Athletics won how many consecutive World Series titles from 1972 to 1974?", "3", ["2","4","1"], "hard"),
    ("Which team had a record 116 wins in the 2001 regular season?", "Seattle Mariners", ["Oakland Athletics","New York Yankees","Chicago Cubs"], "hard"),
    ("Ernie Banks was known as 'Mr. Cub'. He hit how many career home runs?", "512", ["476","456","528"], "hard"),
    ("The 2017 Houston Astros World Series win was later tainted by which scandal?", "Sign-stealing scandal", ["Corked bat scandal","PED scandal","Gambling scandal"], "hard"),
    ("Who managed the New York Yankees to four World Series titles in five years from 1996 to 2000?", "Joe Torre", ["Buck Showalter","Billy Martin","Bob Lemon"], "hard"),
]

for text, ans, wrongs, diff in baseball_questions:
    questions.append(q(text, ans, wrongs, "baseball", diff))

print(f"After baseball: {len(questions)}")

# ============================================================
# HOCKEY DATA
# ============================================================
nhl_cup_champs = [
    (2024, "Florida Panthers", "Edmonton Oilers"),
    (2023, "Vegas Golden Knights", "Florida Panthers"),
    (2022, "Colorado Avalanche", "Tampa Bay Lightning"),
    (2021, "Tampa Bay Lightning", "Montreal Canadiens"),
    (2020, "Tampa Bay Lightning", "Dallas Stars"),
    (2019, "St. Louis Blues", "Boston Bruins"),
    (2018, "Washington Capitals", "Vegas Golden Knights"),
    (2017, "Pittsburgh Penguins", "Nashville Predators"),
    (2016, "Pittsburgh Penguins", "San Jose Sharks"),
    (2015, "Chicago Blackhawks", "Tampa Bay Lightning"),
    (2014, "Los Angeles Kings", "New York Rangers"),
    (2013, "Chicago Blackhawks", "Boston Bruins"),
    (2012, "Los Angeles Kings", "New Jersey Devils"),
    (2011, "Boston Bruins", "Vancouver Canucks"),
    (2010, "Chicago Blackhawks", "Philadelphia Flyers"),
    (2009, "Pittsburgh Penguins", "Detroit Red Wings"),
    (2008, "Detroit Red Wings", "Pittsburgh Penguins"),
    (2007, "Anaheim Ducks", "Ottawa Senators"),
    (2006, "Carolina Hurricanes", "Edmonton Oilers"),
    (2004, "Tampa Bay Lightning", "Calgary Flames"),
    (2003, "New Jersey Devils", "Mighty Ducks of Anaheim"),
    (2002, "Detroit Red Wings", "Carolina Hurricanes"),
    (2001, "Colorado Avalanche", "New Jersey Devils"),
    (2000, "New Jersey Devils", "Dallas Stars"),
    (1999, "Dallas Stars", "Buffalo Sabres"),
    (1998, "Detroit Red Wings", "Washington Capitals"),
    (1997, "Detroit Red Wings", "Philadelphia Flyers"),
    (1996, "Colorado Avalanche", "Florida Panthers"),
    (1995, "New Jersey Devils", "Detroit Red Wings"),
    (1994, "New York Rangers", "Vancouver Canucks"),
    (1993, "Montreal Canadiens", "Los Angeles Kings"),
    (1992, "Pittsburgh Penguins", "Chicago Blackhawks"),
    (1991, "Pittsburgh Penguins", "Minnesota North Stars"),
    (1990, "Edmonton Oilers", "Boston Bruins"),
    (1989, "Calgary Flames", "Montreal Canadiens"),
    (1988, "Edmonton Oilers", "Boston Bruins"),
    (1987, "Edmonton Oilers", "Philadelphia Flyers"),
    (1986, "Montreal Canadiens", "Calgary Flames"),
    (1985, "Edmonton Oilers", "Philadelphia Flyers"),
    (1984, "Edmonton Oilers", "New York Islanders"),
    (1983, "New York Islanders", "Edmonton Oilers"),
    (1982, "New York Islanders", "Vancouver Canucks"),
    (1981, "New York Islanders", "Minnesota North Stars"),
    (1980, "New York Islanders", "Philadelphia Flyers"),
    (1979, "Montreal Canadiens", "New York Rangers"),
    (1978, "Montreal Canadiens", "Boston Bruins"),
    (1977, "Montreal Canadiens", "Boston Bruins"),
    (1976, "Montreal Canadiens", "Philadelphia Flyers"),
    (1975, "Philadelphia Flyers", "Buffalo Sabres"),
    (1974, "Philadelphia Flyers", "Boston Bruins"),
    (1973, "Montreal Canadiens", "Chicago Blackhawks"),
    (1972, "Boston Bruins", "New York Rangers"),
    (1971, "Montreal Canadiens", "Chicago Blackhawks"),
    (1970, "Boston Bruins", "St. Louis Blues"),
    (1969, "Montreal Canadiens", "St. Louis Blues"),
    (1968, "Montreal Canadiens", "St. Louis Blues"),
    (1967, "Toronto Maple Leafs", "Montreal Canadiens"),
    (1966, "Montreal Canadiens", "Detroit Red Wings"),
    (1965, "Montreal Canadiens", "Chicago Blackhawks"),
    (1964, "Toronto Maple Leafs", "Detroit Red Wings"),
    (1963, "Toronto Maple Leafs", "Detroit Red Wings"),
    (1962, "Toronto Maple Leafs", "Chicago Blackhawks"),
    (1961, "Chicago Blackhawks", "Detroit Red Wings"),
    (1960, "Montreal Canadiens", "Toronto Maple Leafs"),
    (1959, "Montreal Canadiens", "Toronto Maple Leafs"),
    (1958, "Montreal Canadiens", "Boston Bruins"),
    (1957, "Montreal Canadiens", "Boston Bruins"),
    (1956, "Montreal Canadiens", "Detroit Red Wings"),
    (1955, "Detroit Red Wings", "Montreal Canadiens"),
    (1954, "Detroit Red Wings", "Montreal Canadiens"),
    (1953, "Montreal Canadiens", "Boston Bruins"),
    (1952, "Detroit Red Wings", "Montreal Canadiens"),
    (1951, "Toronto Maple Leafs", "Montreal Canadiens"),
    (1950, "Detroit Red Wings", "New York Rangers"),
    (1949, "Toronto Maple Leafs", "Detroit Red Wings"),
    (1948, "Toronto Maple Leafs", "Detroit Red Wings"),
    (1947, "Toronto Maple Leafs", "Montreal Canadiens"),
    (1946, "Montreal Canadiens", "Boston Bruins"),
    (1945, "Toronto Maple Leafs", "Detroit Red Wings"),
    (1944, "Montreal Canadiens", "Chicago Blackhawks"),
    (1943, "Detroit Red Wings", "Boston Bruins"),
    (1942, "Toronto Maple Leafs", "Detroit Red Wings"),
    (1941, "Boston Bruins", "Detroit Red Wings"),
    (1940, "New York Rangers", "Toronto Maple Leafs"),
    (1939, "Boston Bruins", "Toronto Maple Leafs"),
    (1938, "Chicago Blackhawks", "Toronto Maple Leafs"),
    (1937, "Detroit Red Wings", "New York Rangers"),
    (1936, "Detroit Red Wings", "Toronto Maple Leafs"),
    (1935, "Montreal Maroons", "Toronto Maple Leafs"),
    (1934, "Chicago Blackhawks", "Detroit Red Wings"),
    (1933, "New York Rangers", "Toronto Maple Leafs"),
    (1932, "Toronto Maple Leafs", "New York Rangers"),
    (1931, "Montreal Canadiens", "Chicago Blackhawks"),
    (1930, "Montreal Canadiens", "Boston Bruins"),
    (1929, "Boston Bruins", "New York Rangers"),
    (1928, "New York Rangers", "Montreal Maroons"),
    (1927, "Ottawa Senators", "Boston Bruins"),
    (1926, "Montreal Maroons", "Victoria Cougars"),
    (1925, "Victoria Cougars", "Montreal Canadiens"),
    (1924, "Montreal Canadiens", "Vancouver Maroons"),
    (1923, "Ottawa Senators", "Edmonton Eskimos"),
    (1922, "Toronto St. Patricks", "Vancouver Millionaires"),
    (1921, "Ottawa Senators", "Vancouver Millionaires"),
    (1920, "Ottawa Senators", "Seattle Metropolitans"),
    (1919, "No champion (influenza pandemic)", "Montreal Canadiens vs Seattle"),
    (1918, "Toronto Arenas", "Vancouver Millionaires"),
]

all_nhl_teams = ["Montreal Canadiens","Toronto Maple Leafs","Detroit Red Wings","Boston Bruins",
    "Chicago Blackhawks","Edmonton Oilers","New York Rangers","Philadelphia Flyers","Pittsburgh Penguins",
    "New York Islanders","Colorado Avalanche","Tampa Bay Lightning","Washington Capitals","Dallas Stars",
    "New Jersey Devils","St. Louis Blues","Calgary Flames","Vancouver Canucks","Ottawa Senators",
    "Carolina Hurricanes","Anaheim Ducks","Los Angeles Kings","San Jose Sharks","Vegas Golden Knights",
    "Minnesota Wild","Florida Panthers","Nashville Predators","Winnipeg Jets","Buffalo Sabres",
    "Columbus Blue Jackets","Arizona Coyotes","Seattle Kraken"]

for yr, champ, runner_up in nhl_cup_champs:
    if "No champion" in champ:
        continue
    wrongs = [t for t in all_nhl_teams if t not in [champ, runner_up]][:3]
    questions.append(q(
        f"Which team won the Stanley Cup in {yr}?",
        champ,
        [runner_up] + wrongs[:2],
        "hockey", "medium"
    ))

print(f"After NHL champs: {len(questions)}")

# Additional hockey static questions
hockey_questions = [
    ("How many players are on the ice per team in hockey?", "6", ["5","7","4"], "easy"),
    ("Wayne Gretzky played most of his career with which team?", "Edmonton Oilers", ["Los Angeles Kings","New York Rangers","St. Louis Blues"], "easy"),
    ("How many periods are in a standard NHL game?", "3", ["4","2","5"], "easy"),
    ("A hat trick in hockey means a player scored how many goals?", "3", ["2","4","5"], "easy"),
    ("Sidney Crosby plays for which team?", "Pittsburgh Penguins", ["Washington Capitals","Toronto Maple Leafs","Boston Bruins"], "easy"),
    ("The Montreal Canadiens have won the most Stanley Cup championships. How many?", "24", ["20","18","23"], "easy"),
    ("Wayne Gretzky's career points record is how many?", "2,857", ["2,345","3,021","2,665"], "easy"),
    ("Alexander Ovechkin plays for which team?", "Washington Capitals", ["New York Rangers","Tampa Bay Lightning","Pittsburgh Penguins"], "easy"),
    ("Mario Lemieux played his entire career with which team?", "Pittsburgh Penguins", ["Montreal Canadiens","Detroit Red Wings","Boston Bruins"], "easy"),
    ("How long is a minor penalty in hockey?", "2 minutes", ["5 minutes","3 minutes","1 minute"], "easy"),
    ("Gordie Howe was nicknamed what?", "Mr. Hockey", ["The Tank","The Machine","The Rocket"], "easy"),
    ("The 'Miracle on Ice' at the 1980 Olympics featured the USA defeating which team?", "Soviet Union", ["Canada","Sweden","Finland"], "easy"),
    ("Which player is called 'The Great One'?", "Wayne Gretzky", ["Mario Lemieux","Bobby Orr","Gordie Howe"], "easy"),
    ("Bobby Orr is regarded as the greatest defenseman in NHL history. He played for which team?", "Boston Bruins", ["Montreal Canadiens","Toronto Maple Leafs","Chicago Blackhawks"], "easy"),
    ("In hockey, a 'Gordie Howe hat trick' consists of what three feats?", "A goal, an assist, and a fight", ["Three goals","A goal, a fight, and a penalty","Two goals and an assist"], "easy"),
    ("Connor McDavid plays for which team?", "Edmonton Oilers", ["Vancouver Canucks","Toronto Maple Leafs","Calgary Flames"], "easy"),
    ("The ice hockey puck is made of what material?", "Vulcanized rubber", ["Hard plastic","Compressed foam","Frozen water"], "easy"),
    ("In what country did ice hockey originate?", "Canada", ["United States","Sweden","Russia"], "easy"),
    ("Wayne Gretzky was traded from the Edmonton Oilers to which team in 1988?", "Los Angeles Kings", ["New York Rangers","St. Louis Blues","Hartford Whalers"], "medium"),
    ("Martin Brodeur holds the record for most career wins by an NHL goalie. How many?", "691", ["660","552","705"], "medium"),
    ("Steve Yzerman captained which team to three Stanley Cup titles?", "Detroit Red Wings", ["Pittsburgh Penguins","Tampa Bay Lightning","Colorado Avalanche"], "medium"),
    ("Which player won the Norris Trophy (best defenseman) the most times?", "Bobby Orr", ["Raymond Bourque","Nicklas Lidstrom","Chris Chelios"], "medium"),
    ("The Colorado Avalanche were previously known as which team?", "Quebec Nordiques", ["Hartford Whalers","Minnesota North Stars","Winnipeg Jets"], "medium"),
    ("The Mighty Ducks of Anaheim were founded and partly owned by which company?", "The Walt Disney Company", ["Warner Bros.","Universal Studios","Paramount Pictures"], "medium"),
    ("Patrick Kane won how many Stanley Cups with the Chicago Blackhawks?", "3", ["2","4","1"], "medium"),
    ("The Tampa Bay Lightning won back-to-back Stanley Cups in which years?", "2020 and 2021", ["2019 and 2020","2021 and 2022","2018 and 2019"], "medium"),
    ("Scotty Bowman is the winningest coach in NHL history with how many wins?", "1,244", ["1,100","987","1,350"], "medium"),
    ("The Vegas Golden Knights became an expansion team in what year?", "2017", ["2015","2019","2013"], "medium"),
    ("Which player was nicknamed 'The Golden Jet' for the Chicago Blackhawks?", "Bobby Hull", ["Phil Esposito","Stan Mikita","Tony Esposito"], "medium"),
    ("Guy Lafleur won how many Stanley Cups with the Montreal Canadiens?", "5", ["4","3","6"], "medium"),
    ("The 1994 Rangers Stanley Cup win ended a drought of how many years?", "54", ["40","46","62"], "medium"),
    ("Dominik Hasek won the Hart Trophy twice. He played primarily for which team?", "Buffalo Sabres", ["Ottawa Senators","Detroit Red Wings","Colorado Avalanche"], "medium"),
    ("Wayne Gretzky scored how many goals in the 1981-82 season?", "92", ["87","76","100"], "hard"),
    ("Who was the head coach of the US team during the 1980 Miracle on Ice?", "Herb Brooks", ["Bob Johnson","John Mariucci","Tim Taylor"], "hard"),
    ("Which defenseman scored the Stanley Cup-winning goal for Boston in 1970 while airborne?", "Bobby Orr", ["Ted Green","Don Awrey","Dallas Smith"], "hard"),
    ("Phil Esposito set the NHL single-season goal record in 1970-71 with how many goals?", "76", ["70","80","65"], "hard"),
    ("Maurice Richard was the first player to score how many goals in NHL history?", "500", ["400","600","300"], "hard"),
    ("Paul Henderson scored the series winner in Game 8 of the 1972 Summit Series. Who was he playing for?", "Canada", ["Soviet Union","Czech Republic","Sweden"], "hard"),
    ("The Hartford Whalers relocated to which city in 1997?", "Raleigh, NC (becoming Carolina Hurricanes)", ["Nashville","Atlanta","Phoenix"], "hard"),
    ("Who was the goalie for the 1976-77 Montreal Canadiens who went 60-8-12?", "Ken Dryden", ["Gerry Cheevers","Tony Esposito","Rogie Vachon"], "hard"),
    ("The first NHL game was played in what year?", "1917", ["1920","1915","1919"], "hard"),
    ("Wayne Gretzky set the record for most points in a single playoff year with 47. What year?", "1985", ["1983","1987","1981"], "hard"),
    ("The Quebec Nordiques relocated to become which team in 1995?", "Colorado Avalanche", ["Florida Panthers","Dallas Stars","Nashville Predators"], "hard"),
    ("Who was the general manager who assembled the Edmonton Oilers dynasty?", "Glen Sather", ["Lester Patrick","Sam Pollock","Lou Lamoriello"], "hard"),
    ("The Carolina Hurricanes won their only Stanley Cup in which year?", "2006", ["2002","2009","2011"], "hard"),
    ("Which defenseman won the Norris Trophy 8 times total in his career?", "Bobby Orr", ["Nicklas Lidstrom","Ray Bourque","Doug Harvey"], "hard"),
    ("The Atlanta Thrashers relocated to Winnipeg in what year to become the Jets?", "2011", ["2009","2013","2007"], "hard"),
    ("The Minnesota North Stars relocated to which city in 1993?", "Dallas (becoming the Dallas Stars)", ["Denver","Nashville","Columbus"], "hard"),
    ("Who scored the 'Miracle on Ice' winning goal for the USA against the Soviet Union?", "Mike Eruzione", ["Mark Johnson","Jim Craig","Neal Broten"], "hard"),
    ("The Detroit Red Wings won four Stanley Cups from 1997 to 2002. Who was their coach for all four?", "Scotty Bowman", ["Dave Lewis","Barry Smith","Mike Babcock"], "hard"),
    ("Which NHL team was the first US-based team to win the Stanley Cup?", "Seattle Metropolitans (1917, PCHA not NHL)", ["Boston Bruins (1929)","New York Rangers (1928)","Chicago Blackhawks (1934)"], "hard"),
]

for text, ans, wrongs, diff in hockey_questions:
    questions.append(q(text, ans, wrongs, "hockey", diff))

print(f"After hockey: {len(questions)}")

# ============================================================
# SOCCER DATA
# ============================================================
fifa_wc_champs = [
    (2022, "Argentina", "France"),
    (2018, "France", "Croatia"),
    (2014, "Germany", "Argentina"),
    (2010, "Spain", "Netherlands"),
    (2006, "Italy", "France"),
    (2002, "Brazil", "Germany"),
    (1998, "France", "Brazil"),
    (1994, "Brazil", "Italy"),
    (1990, "West Germany", "Argentina"),
    (1986, "Argentina", "West Germany"),
    (1982, "Italy", "West Germany"),
    (1978, "Argentina", "Netherlands"),
    (1974, "West Germany", "Netherlands"),
    (1970, "Brazil", "Italy"),
    (1966, "England", "West Germany"),
    (1962, "Brazil", "Czechoslovakia"),
    (1958, "Brazil", "Sweden"),
    (1954, "West Germany", "Hungary"),
    (1950, "Uruguay", "Brazil"),
    (1938, "Italy", "Hungary"),
    (1934, "Italy", "Czechoslovakia"),
    (1930, "Uruguay", "Argentina"),
]

all_soccer_teams = ["Brazil","Germany","Italy","Argentina","France","Spain","England","Netherlands",
    "Uruguay","Portugal","Belgium","Croatia","Mexico","Poland","Japan","South Korea","Australia",
    "Colombia","Chile","Denmark","Sweden","Czech Republic","Hungary","United States"]

for yr, champ, runner_up in fifa_wc_champs:
    wrongs = [t for t in all_soccer_teams if t not in [champ, runner_up]][:3]
    questions.append(q(
        f"Which country won the FIFA World Cup in {yr}?",
        champ,
        [runner_up] + wrongs[:2],
        "soccer", "medium"
    ))
    questions.append(q(
        f"Which country was the runner-up in the {yr} FIFA World Cup?",
        runner_up,
        [champ] + wrongs[:2],
        "soccer", "hard"
    ))

print(f"After FIFA WC: {len(questions)}")

# UEFA Champions League winners (selected)
ucl_champs = [
    (2023, "Manchester City"), (2022, "Real Madrid"), (2021, "Chelsea"),
    (2020, "Bayern Munich"), (2019, "Liverpool"), (2018, "Real Madrid"),
    (2017, "Real Madrid"), (2016, "Real Madrid"), (2015, "Barcelona"),
    (2014, "Real Madrid"), (2013, "Bayern Munich"), (2012, "Chelsea"),
    (2011, "Barcelona"), (2010, "Inter Milan"), (2009, "Barcelona"),
    (2008, "Manchester United"), (2007, "AC Milan"), (2006, "Barcelona"),
    (2005, "Liverpool"), (2004, "Porto"), (2003, "AC Milan"),
    (2002, "Real Madrid"), (2001, "Bayern Munich"), (2000, "Real Madrid"),
    (1999, "Manchester United"), (1998, "Real Madrid"), (1997, "Borussia Dortmund"),
    (1996, "Juventus"), (1995, "Ajax"), (1994, "AC Milan"),
    (1993, "Marseille"), (1992, "Barcelona"),
]

ucl_clubs = ["Real Madrid","Barcelona","Bayern Munich","Liverpool","Manchester United","Manchester City",
    "Juventus","AC Milan","Inter Milan","Chelsea","Atletico Madrid","Borussia Dortmund","Ajax","Porto",
    "PSG","Arsenal","Tottenham","AS Roma","Sevilla","Valencia","Bayer Leverkusen","Lyon","Napoli"]

for yr, champ in ucl_champs:
    wrongs = [t for t in ucl_clubs if t != champ]
    random.shuffle(wrongs)
    questions.append(q(
        f"Which club won the UEFA Champions League in {yr}?",
        champ,
        wrongs[:3],
        "soccer", "hard"
    ))

print(f"After UCL: {len(questions)}")

# Additional soccer static questions
soccer_questions = [
    ("How many players are on the field per team in soccer?", "11", ["10","12","9"], "easy"),
    ("What is the maximum time in a standard soccer match?", "90 minutes", ["120 minutes","80 minutes","100 minutes"], "easy"),
    ("Lionel Messi played most of his career for which club?", "FC Barcelona", ["Paris Saint-Germain","Inter Miami","Real Madrid"], "easy"),
    ("Cristiano Ronaldo is from which country?", "Portugal", ["Spain","Brazil","Argentina"], "easy"),
    ("Which country has won the most FIFA World Cups?", "Brazil (5)", ["Germany (4)","Italy (4)","Argentina (3)"], "easy"),
    ("What is a 'hat trick' in soccer?", "Three goals in one game by the same player", ["Three assists in one game","Three games without conceding","Three consecutive wins"], "easy"),
    ("Pelé is from which country?", "Brazil", ["Argentina","Portugal","Colombia"], "easy"),
    ("What does FIFA stand for?", "Federation Internationale de Football Association", ["Football International Federation Association","Federation de International Football Athletics","Foot International Football Association"], "easy"),
    ("The penalty spot in soccer is how many yards from the goal?", "12 yards (11 meters)", ["10 yards","15 yards","8 yards"], "easy"),
    ("Which country hosted the 2022 FIFA World Cup?", "Qatar", ["Saudi Arabia","UAE","Bahrain"], "easy"),
    ("Lionel Messi won how many Ballon d'Or awards (as of 2023)?", "8", ["6","7","5"], "easy"),
    ("Which club won the Premier League the most times?", "Manchester United", ["Arsenal","Liverpool","Manchester City"], "easy"),
    ("The 'Yellow Card' in soccer means what?", "A caution/warning to the player", ["Immediate ejection","5-minute penalty","Loss of a substitution"], "easy"),
    ("Two yellow cards equal what in soccer?", "A red card (ejection)", ["A penalty kick","A free kick","A 10-minute suspension"], "easy"),
    ("Which player scored the 'Hand of God' goal in the 1986 World Cup?", "Diego Maradona", ["Pelé","Ronaldo","Zinedine Zidane"], "easy"),
    ("Real Madrid plays home games at which stadium?", "Santiago Bernabeu", ["Camp Nou","Old Trafford","Anfield"], "easy"),
    ("FC Barcelona plays home games at which stadium?", "Camp Nou", ["Santiago Bernabeu","Nou Mestalla","Wanda Metropolitano"], "easy"),
    ("Thierry Henry played for which club during his most famous spell?", "Arsenal", ["Barcelona","AS Monaco","New York Red Bulls"], "medium"),
    ("Zinedine Zidane is from which country?", "France", ["Algeria","Tunisia","Morocco"], "medium"),
    ("Which country won back-to-back World Cups in 1934 and 1938?", "Italy", ["Brazil","Germany","Argentina"], "medium"),
    ("Pele won how many FIFA World Cups?", "3", ["2","1","4"], "medium"),
    ("The MLS (Major League Soccer) was founded in which year?", "1996", ["1993","1999","2000"], "medium"),
    ("Who was the manager of France when they won the 1998 World Cup?", "Aime Jacquet", ["Roger Lemerre","Gerard Houllier","Didier Deschamps"], "medium"),
    ("Which player was known as 'The Divine Ponytail'?", "Roberto Baggio", ["Franco Baresi","Paolo Maldini","Alessandro Del Piero"], "medium"),
    ("Ronaldo (the Brazilian), not Cristiano, scored how many goals at FIFA World Cups?", "15", ["12","17","9"], "medium"),
    ("Manchester United's famous 'Class of 92' included which players?", "Giggs, Beckham, Scholes, Neville brothers, Butt", ["Rush, Hughes, Cantona, Robson, Pallister","Shearer, Sheringham, Cole, Fowler, McManaman","Ferdinand, Cole, Yorke, Keane, Irwin"], "medium"),
    ("Who is the all-time leading scorer in the UEFA Champions League?", "Cristiano Ronaldo", ["Lionel Messi","Raul","Robert Lewandowski"], "medium"),
    ("Which country won the first ever Women's World Cup in 1991?", "United States", ["Germany","Norway","China"], "medium"),
    ("Lev Yashin is considered the greatest goalkeeper of all time and played for which club?", "Dynamo Moscow", ["Spartak Moscow","CSKA Moscow","Lokomotiv Moscow"], "hard"),
    ("Johan Cruyff famously played for which two clubs?", "Ajax and FC Barcelona", ["PSV and Ajax","Barcelona and Real Madrid","Feyenoord and Ajax"], "hard"),
    ("The 'Golden Generation' of Portuguese football in the early 2000s was built around which academy?", "Sporting CP", ["Benfica","Porto","Nacional"], "hard"),
    ("Which Brazilian player won the 1994 and 2002 World Cups?", "Ronaldo", ["Cafu","Rivaldo","Roberto Carlos"], "hard"),
    ("The UEFA Euro 2004 was won by which massive underdog?", "Greece", ["Czech Republic","Portugal","Germany"], "hard"),
    ("What was the score of the infamous Brazil vs Germany semifinal at the 2014 World Cup?", "7-1", ["6-0","5-1","8-0"], "hard"),
    ("Germany won how many consecutive matches to win the 2014 World Cup?", "7", ["6","5","8"], "hard"),
    ("Which player's volley in the 2002 Champions League Final is considered one of the best goals ever?", "Zinedine Zidane", ["Raul","Roberto Carlos","Ronaldo"], "hard"),
    ("In which year did the Premier League replace the First Division in England?", "1992", ["1990","1995","1988"], "hard"),
    ("The 'Invincibles' season in 2003-04 was achieved by which club?", "Arsenal", ["Manchester United","Chelsea","Liverpool"], "hard"),
    ("Which South American tournament is equivalent to the UEFA Champions League?", "Copa Libertadores", ["Copa America","CONMEBOL Cup","Sudamericana"], "hard"),
    ("Diego Maradona's '5 second goal' against England in 1986 covered how many meters?", "60 meters (approximately)", ["90 meters","45 meters","75 meters"], "hard"),
]

for text, ans, wrongs, diff in soccer_questions:
    questions.append(q(text, ans, wrongs, "soccer", diff))

print(f"After soccer: {len(questions)}")

# ============================================================
# F1 DATA
# ============================================================
f1_champs = [
    (2023, "Max Verstappen", "Red Bull"),
    (2022, "Max Verstappen", "Red Bull"),
    (2021, "Max Verstappen", "Red Bull"),
    (2020, "Lewis Hamilton", "Mercedes"),
    (2019, "Lewis Hamilton", "Mercedes"),
    (2018, "Lewis Hamilton", "Mercedes"),
    (2017, "Lewis Hamilton", "Mercedes"),
    (2016, "Nico Rosberg", "Mercedes"),
    (2015, "Lewis Hamilton", "Mercedes"),
    (2014, "Lewis Hamilton", "Mercedes"),
    (2013, "Sebastian Vettel", "Red Bull"),
    (2012, "Sebastian Vettel", "Red Bull"),
    (2011, "Sebastian Vettel", "Red Bull"),
    (2010, "Sebastian Vettel", "Red Bull"),
    (2009, "Jenson Button", "Brawn GP"),
    (2008, "Lewis Hamilton", "McLaren"),
    (2007, "Kimi Raikkonen", "Ferrari"),
    (2006, "Fernando Alonso", "Renault"),
    (2005, "Fernando Alonso", "Renault"),
    (2004, "Michael Schumacher", "Ferrari"),
    (2003, "Michael Schumacher", "Ferrari"),
    (2002, "Michael Schumacher", "Ferrari"),
    (2001, "Michael Schumacher", "Ferrari"),
    (2000, "Michael Schumacher", "Ferrari"),
    (1999, "Mika Hakkinen", "McLaren"),
    (1998, "Mika Hakkinen", "McLaren"),
    (1997, "Jacques Villeneuve", "Williams"),
    (1996, "Damon Hill", "Williams"),
    (1995, "Michael Schumacher", "Benetton"),
    (1994, "Michael Schumacher", "Benetton"),
    (1993, "Alain Prost", "Williams"),
    (1992, "Nigel Mansell", "Williams"),
    (1991, "Ayrton Senna", "McLaren"),
    (1990, "Ayrton Senna", "McLaren"),
    (1989, "Alain Prost", "McLaren"),
    (1988, "Ayrton Senna", "McLaren"),
    (1987, "Nelson Piquet", "Williams"),
    (1986, "Alain Prost", "McLaren"),
    (1985, "Alain Prost", "McLaren"),
    (1984, "Niki Lauda", "McLaren"),
    (1983, "Nelson Piquet", "Brabham"),
    (1982, "Keke Rosberg", "Williams"),
    (1981, "Nelson Piquet", "Brabham"),
    (1980, "Alan Jones", "Williams"),
    (1979, "Jody Scheckter", "Ferrari"),
    (1978, "Mario Andretti", "Lotus"),
    (1977, "Niki Lauda", "Ferrari"),
    (1976, "James Hunt", "McLaren"),
    (1975, "Niki Lauda", "Ferrari"),
    (1974, "Emerson Fittipaldi", "McLaren"),
    (1973, "Jackie Stewart", "Tyrrell"),
    (1972, "Emerson Fittipaldi", "Lotus"),
    (1971, "Jackie Stewart", "Tyrrell"),
    (1970, "Jochen Rindt", "Lotus"),
    (1969, "Jackie Stewart", "Matra"),
    (1968, "Graham Hill", "Lotus"),
    (1967, "Denny Hulme", "Brabham"),
    (1966, "Jack Brabham", "Brabham"),
    (1965, "Jim Clark", "Lotus"),
    (1964, "John Surtees", "Ferrari"),
    (1963, "Jim Clark", "Lotus"),
    (1962, "Graham Hill", "BRM"),
    (1961, "Phil Hill", "Ferrari"),
    (1960, "Jack Brabham", "Cooper"),
    (1959, "Jack Brabham", "Cooper"),
    (1958, "Mike Hawthorn", "Ferrari"),
    (1957, "Juan Manuel Fangio", "Maserati"),
    (1956, "Juan Manuel Fangio", "Ferrari"),
    (1955, "Juan Manuel Fangio", "Mercedes"),
    (1954, "Juan Manuel Fangio", "Mercedes/Maserati"),
    (1953, "Alberto Ascari", "Ferrari"),
    (1952, "Alberto Ascari", "Ferrari"),
    (1951, "Juan Manuel Fangio", "Alfa Romeo"),
    (1950, "Giuseppe Farina", "Alfa Romeo"),
]

f1_drivers = ["Max Verstappen","Lewis Hamilton","Sebastian Vettel","Michael Schumacher","Ayrton Senna",
    "Alain Prost","Niki Lauda","Fernando Alonso","Kimi Raikkonen","Mika Hakkinen","Nigel Mansell",
    "Nelson Piquet","Juan Manuel Fangio","Jim Clark","Jackie Stewart","Damon Hill","Jenson Button",
    "Valtteri Bottas","Charles Leclerc","Lando Norris","Daniel Ricciardo","Sergio Perez",
    "Carlos Sainz","George Russell","Jacques Villeneuve","Jack Brabham","Graham Hill"]

f1_teams = ["Red Bull","Mercedes","Ferrari","McLaren","Williams","Renault","Benetton","Brawn GP",
    "Lotus","Maserati","Alfa Romeo","Brabham","Tyrrell","Matra","BRM","Cooper","Jordan",
    "Force India","Haas","Alfa Romeo Racing","Aston Martin","AlphaTauri","Alpine"]

for yr, driver, team in f1_champs:
    wrongs_d = [d for d in f1_drivers if d != driver]
    random.shuffle(wrongs_d)
    wrongs_t = [t for t in f1_teams if t != team]
    random.shuffle(wrongs_t)
    questions.append(q(
        f"Who won the Formula 1 World Drivers Championship in {yr}?",
        driver,
        wrongs_d[:3],
        "f1", "hard"
    ))
    questions.append(q(
        f"Which constructor won the F1 World Championship with {driver} in {yr}?",
        team,
        wrongs_t[:3],
        "f1", "hard"
    ))

print(f"After F1 champs: {len(questions)}")

# Additional F1 static questions
f1_questions = [
    ("How many races does a Formula 1 season typically have in the modern era?", "Around 20-24 races", ["10-12 races","15-18 races","25-30 races"], "easy"),
    ("Lewis Hamilton drives for which team?", "Mercedes", ["Ferrari","Red Bull","McLaren"], "easy"),
    ("Which F1 team is based in Maranello, Italy?", "Ferrari", ["Alfa Romeo","AlphaTauri","Aston Martin"], "easy"),
    ("Max Verstappen races for which F1 team?", "Red Bull Racing", ["Ferrari","Mercedes","McLaren"], "easy"),
    ("How many points does the race winner receive in F1?", "25", ["20","30","15"], "easy"),
    ("Which F1 track is known as 'The Temple of Speed'?", "Monza (Italian Grand Prix)", ["Monaco","Spa","Silverstone"], "easy"),
    ("Ayrton Senna died in a crash at which Grand Prix in 1994?", "San Marino Grand Prix (Imola)", ["Spanish Grand Prix","Brazilian Grand Prix","Monaco Grand Prix"], "easy"),
    ("Who won the most Formula 1 World Championships?", "Lewis Hamilton and Michael Schumacher (7 each)", ["Ayrton Senna","Juan Manuel Fangio","Alain Prost"], "easy"),
    ("Michael Schumacher won his last F1 title with which team?", "Ferrari", ["Benetton","Mercedes","Jordan"], "easy"),
    ("The Monaco Grand Prix is held on the streets of which city?", "Monaco (Monte Carlo)", ["Nice","Cannes","Marseille"], "easy"),
    ("Which circuit hosts the British Grand Prix?", "Silverstone", ["Brands Hatch","Donington Park","Goodwood"], "easy"),
    ("Formula 1 cars are powered by engines of what displacement since 2014?", "1.6-liter turbocharged V6", ["2.4-liter V8","3.0-liter V10","1.0-liter V4"], "medium"),
    ("Who was the youngest F1 World Champion when he won in 2010?", "Sebastian Vettel (23 years old)", ["Max Verstappen","Fernando Alonso","Nico Rosberg"], "medium"),
    ("The DRS (Drag Reduction System) was introduced in F1 in which year?", "2011", ["2008","2014","2009"], "medium"),
    ("Which F1 team won eight consecutive constructors championships from 2010 to 2020?", "Mercedes", ["Red Bull","Ferrari","McLaren"], "medium"),
    ("Juan Manuel Fangio won how many F1 World Championships?", "5", ["4","3","6"], "medium"),
    ("Who holds the record for most F1 race wins?", "Lewis Hamilton (103+)", ["Michael Schumacher","Sebastian Vettel","Ayrton Senna"], "medium"),
    ("The Nurburgring Nordschleife is located in which country?", "Germany", ["Austria","Belgium","Netherlands"], "medium"),
    ("Which F1 driver was famous for saying 'Leave me alone, I know what I'm doing'?", "Kimi Raikkonen", ["Nico Rosberg","Felipe Massa","Valtteri Bottas"], "medium"),
    ("The HANS device in motorsport stands for?", "Head and Neck Support", ["Head and Neck System","High Acceleration Neck Support","Head Armor Neck Support"], "medium"),
    ("Max Verstappen became World Champion for the first time in which dramatic final race?", "Abu Dhabi 2021", ["Saudi Arabia 2021","Brazil 2021","Mexico 2021"], "hard"),
    ("Niki Lauda survived a fiery crash at which 1976 Grand Prix?", "German Grand Prix (Nurburgring)", ["Austrian Grand Prix","Italian Grand Prix","Swiss Grand Prix"], "hard"),
    ("Which circuit was famous for the 'Eau Rouge' corner?", "Spa-Francorchamps (Belgian GP)", ["Monza","Silverstone","Suzuka"], "hard"),
    ("The McLaren MP4/4 is considered the most dominant F1 car ever. Who drove it to the title?", "Ayrton Senna (1988)", ["Alain Prost","Gerhard Berger","Damon Hill"], "hard"),
    ("Which Japanese circuit hosts the Japanese Grand Prix?", "Suzuka", ["Fuji Speedway","Twin Ring Motegi","Okayama"], "hard"),
    ("What was the revolutionary engine configuration Ferrari introduced in 2000?", "3.0-liter V10", ["2.4-liter V8","1.6-liter V6 Turbo","3.5-liter V12"], "hard"),
    ("The 'Death Lap' at Monaco refers to which sector?", "From Ste. Devote to Casino Square", ["Tunnel exit","Swimming Pool section","Anthony Noghes corner"], "hard"),
    ("Who was James Hunt's main rival when they battled for the 1976 championship?", "Niki Lauda", ["Jody Scheckter","Clay Regazzoni","Carlos Reutemann"], "hard"),
    ("What is the minimum weight for an F1 car (plus driver) in the modern era?", "798 kg (as of 2022)", ["700 kg","650 kg","750 kg"], "hard"),
    ("Which team used a 'twin-deck' diffuser to gain a huge advantage in early 2009?", "Brawn GP", ["Red Bull","McLaren","Toyota"], "hard"),
]

for text, ans, wrongs, diff in f1_questions:
    questions.append(q(text, ans, wrongs, "f1", diff))

print(f"After F1: {len(questions)}")

# ============================================================
# TENNIS DATA
# ============================================================
wimbledon_mens = [
    (2023, "Carlos Alcaraz"), (2022, "Novak Djokovic"), (2021, "Novak Djokovic"),
    (2019, "Novak Djokovic"), (2018, "Novak Djokovic"), (2017, "Roger Federer"),
    (2016, "Andy Murray"), (2015, "Novak Djokovic"), (2014, "Novak Djokovic"),
    (2013, "Andy Murray"), (2012, "Roger Federer"), (2011, "Novak Djokovic"),
    (2010, "Rafael Nadal"), (2009, "Roger Federer"), (2008, "Rafael Nadal"),
    (2007, "Roger Federer"), (2006, "Roger Federer"), (2005, "Roger Federer"),
    (2004, "Roger Federer"), (2003, "Roger Federer"), (2002, "Lleyton Hewitt"),
    (2001, "Goran Ivanisevic"), (2000, "Pete Sampras"), (1999, "Pete Sampras"),
    (1998, "Pete Sampras"), (1997, "Pete Sampras"), (1996, "Richard Krajicek"),
    (1995, "Pete Sampras"), (1994, "Pete Sampras"), (1993, "Pete Sampras"),
    (1992, "Andre Agassi"), (1991, "Michael Stich"), (1990, "Stefan Edberg"),
    (1989, "Boris Becker"), (1988, "Stefan Edberg"), (1987, "Pat Cash"),
    (1986, "Boris Becker"), (1985, "Boris Becker"), (1984, "John McEnroe"),
    (1983, "John McEnroe"), (1982, "Jimmy Connors"), (1981, "John McEnroe"),
    (1980, "Bjorn Borg"), (1979, "Bjorn Borg"), (1978, "Bjorn Borg"),
    (1977, "Bjorn Borg"), (1976, "Bjorn Borg"),
]

tennis_players = ["Roger Federer","Rafael Nadal","Novak Djokovic","Pete Sampras","Bjorn Borg",
    "John McEnroe","Andre Agassi","Jimmy Connors","Boris Becker","Stefan Edberg",
    "Andy Murray","Carlos Alcaraz","Lleyton Hewitt","Goran Ivanisevic","Richard Krajicek",
    "Pat Cash","Michael Stich","Mats Wilander","Ivan Lendl","Guillermo Vilas",
    "Ilie Nastase","Arthur Ashe","Stan Smith","Marcelo Rios","Andy Roddick"]

for yr, champ in wimbledon_mens:
    wrongs = [p for p in tennis_players if p != champ]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the Wimbledon men's singles title in {yr}?",
        champ,
        wrongs[:3],
        "tennis", "hard"
    ))

# French Open (Roland Garros) mens
french_open_mens = [
    (2023, "Novak Djokovic"), (2022, "Rafael Nadal"), (2021, "Novak Djokovic"),
    (2020, "Rafael Nadal"), (2019, "Rafael Nadal"), (2018, "Rafael Nadal"),
    (2017, "Rafael Nadal"), (2016, "Novak Djokovic"), (2015, "Stan Wawrinka"),
    (2014, "Rafael Nadal"), (2013, "Rafael Nadal"), (2012, "Rafael Nadal"),
    (2011, "Rafael Nadal"), (2010, "Rafael Nadal"), (2009, "Roger Federer"),
    (2008, "Rafael Nadal"), (2007, "Rafael Nadal"), (2006, "Rafael Nadal"),
    (2005, "Rafael Nadal"), (2004, "Gaston Gaudio"), (2003, "Juan Carlos Ferrero"),
    (2002, "Albert Costa"), (2001, "Gustavo Kuerten"), (2000, "Gustavo Kuerten"),
    (1999, "Andre Agassi"), (1998, "Carlos Moya"), (1997, "Gustavo Kuerten"),
    (1996, "Yevgeny Kafelnikov"), (1995, "Thomas Muster"), (1994, "Sergi Bruguera"),
    (1993, "Sergi Bruguera"), (1992, "Jim Courier"), (1991, "Jim Courier"),
    (1990, "Andres Gomez"), (1989, "Michael Chang"), (1988, "Mats Wilander"),
    (1987, "Ivan Lendl"), (1986, "Ivan Lendl"), (1985, "Mats Wilander"),
    (1984, "Ivan Lendl"), (1983, "Yannick Noah"), (1982, "Mats Wilander"),
]

for yr, champ in french_open_mens:
    wrongs = [p for p in tennis_players if p != champ]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the French Open (Roland Garros) men's singles title in {yr}?",
        champ,
        wrongs[:3],
        "tennis", "hard"
    ))

print(f"After tennis champs: {len(questions)}")

# US Open mens
us_open_mens = [
    (2023, "Novak Djokovic"), (2022, "Carlos Alcaraz"), (2021, "Daniil Medvedev"),
    (2020, "Dominic Thiem"), (2019, "Rafael Nadal"), (2018, "Novak Djokovic"),
    (2017, "Rafael Nadal"), (2016, "Stan Wawrinka"), (2015, "Novak Djokovic"),
    (2014, "Marin Cilic"), (2013, "Rafael Nadal"), (2012, "Andy Murray"),
    (2011, "Novak Djokovic"), (2010, "Rafael Nadal"), (2009, "Juan Martin del Potro"),
    (2008, "Roger Federer"), (2007, "Roger Federer"), (2006, "Roger Federer"),
    (2005, "Roger Federer"), (2004, "Roger Federer"), (2003, "Andy Roddick"),
    (2002, "Pete Sampras"), (2001, "Lleyton Hewitt"), (2000, "Marat Safin"),
    (1999, "Andre Agassi"), (1998, "Patrick Rafter"), (1997, "Patrick Rafter"),
    (1996, "Pete Sampras"), (1995, "Pete Sampras"), (1994, "Andre Agassi"),
    (1993, "Pete Sampras"), (1992, "Stefan Edberg"), (1991, "Stefan Edberg"),
    (1990, "Pete Sampras"), (1989, "Boris Becker"), (1988, "Mats Wilander"),
    (1987, "Ivan Lendl"), (1986, "Ivan Lendl"), (1985, "Ivan Lendl"),
    (1984, "John McEnroe"), (1983, "Jimmy Connors"), (1982, "Jimmy Connors"),
    (1981, "John McEnroe"), (1980, "John McEnroe"), (1979, "John McEnroe"),
]

for yr, champ in us_open_mens:
    wrongs = [p for p in tennis_players if p != champ]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the US Open men's singles title in {yr}?",
        champ,
        wrongs[:3],
        "tennis", "hard"
    ))

print(f"After US Open: {len(questions)}")

# Additional tennis static questions
tennis_questions = [
    ("How many Grand Slam tournaments are there in tennis?", "4", ["3","5","6"], "easy"),
    ("The four Grand Slam tournaments are Wimbledon, US Open, French Open, and what?", "Australian Open", ["Italian Open","Canadian Open","German Open"], "easy"),
    ("Rafael Nadal has won the most French Open titles. How many?", "14", ["11","12","13"], "easy"),
    ("Which surface is Wimbledon played on?", "Grass", ["Clay","Hard court","Carpet"], "easy"),
    ("Which surface is the French Open (Roland Garros) played on?", "Clay", ["Grass","Hard court","Carpet"], "easy"),
    ("Roger Federer won how many Grand Slam titles?", "20", ["18","22","17"], "easy"),
    ("Novak Djokovic has won how many Grand Slam titles?", "24", ["20","21","22"], "easy"),
    ("Serena Williams won how many Grand Slam singles titles?", "23", ["21","19","25"], "easy"),
    ("The tie-break in tennis is played to how many points?", "7 (with a 2-point lead)", ["10","6","5"], "easy"),
    ("What is 'love' equivalent to in tennis scoring?", "Zero (0)", ["One","Half point","A win"], "easy"),
    ("Which country has produced both Roger Federer and Martina Hingis?", "Switzerland", ["Germany","Austria","Liechtenstein"], "easy"),
    ("Pete Sampras won how many Wimbledon titles?", "7", ["6","8","5"], "medium"),
    ("Bjorn Borg won 5 consecutive Wimbledon titles from 1976 to 1980. He retired at what age?", "26", ["28","30","32"], "medium"),
    ("John McEnroe was famous for his arguments with chair umpires. Which year did he famously say 'You cannot be serious'?", "1981", ["1979","1983","1977"], "medium"),
    ("Which player won the Golden Grand Slam in 1988 (all 4 Grand Slams and Olympic gold)?", "Steffi Graf", ["Martina Navratilova","Monica Seles","Arantxa Sanchez Vicario"], "medium"),
    ("Who was the first American man to win the French Open in the Open Era?", "Andre Agassi (1999)", ["Pete Sampras","Jim Courier","Andy Roddick"], "medium"),
    ("What is the fastest serve ever recorded in a Grand Slam match?", "263 km/h by Sam Groth", ["251 km/h by Andy Roddick","258 km/h by John Isner","247 km/h by Ivo Karlovic"], "medium"),
    ("The longest match in Grand Slam history lasted 11 hours. It was at which tournament?", "Wimbledon 2010 (Isner vs Mahut)", ["US Open 2009","French Open 2004","Australian Open 2012"], "medium"),
    ("Which player was known as 'The Swiss Miss' before Federer emerged?", "Martina Hingis", ["Steffi Graf","Chris Evert","Monica Seles"], "medium"),
    ("Andre Agassi won the career Grand Slam. He won all four Slams. What year did he complete it?", "1999 (French Open)", ["1998 (Australian Open)","2001 (US Open)","2000 (Wimbledon)"], "medium"),
    ("Jim Courier won back-to-back French Open titles in which years?", "1991 and 1992", ["1990 and 1991","1992 and 1993","1989 and 1990"], "hard"),
    ("Which female player holds the record for most Grand Slam singles titles?", "Margaret Court (24)", ["Serena Williams (23)","Steffi Graf (22)","Helen Wills (19)"], "hard"),
    ("Arantxa Sanchez Vicario won how many Grand Slam singles titles?", "4", ["3","6","2"], "hard"),
    ("The first Open Era Wimbledon was in which year?", "1968", ["1965","1970","1972"], "hard"),
    ("Which player was the first man to reach a career Grand Slam (all 4 Slams)?", "Don Budge (1938)", ["Rod Laver","Andre Agassi","Roy Emerson"], "hard"),
    ("Mats Wilander won how many Grand Slam titles?", "7", ["5","9","4"], "hard"),
    ("Which player won Wimbledon in 2001 as a wild card at age 29?", "Goran Ivanisevic", ["Lleyton Hewitt","Tim Henman","Andrew Agassi"], "hard"),
    ("The ATP ranking system was introduced in which year?", "1973", ["1968","1980","1975"], "hard"),
    ("Which Grand Slam has the most prize money historically?", "US Open", ["Wimbledon","Australian Open","French Open"], "hard"),
    ("Ivan Lendl won how many Grand Slam titles in his career?", "8", ["6","10","4"], "hard"),
]

for text, ans, wrongs, diff in tennis_questions:
    questions.append(q(text, ans, wrongs, "tennis", diff))

print(f"After tennis: {len(questions)}")

# ============================================================
# GOLF DATA
# ============================================================
masters_champs = [
    (2024, "Scottie Scheffler"), (2023, "Jon Rahm"), (2022, "Scottie Scheffler"),
    (2021, "Hideki Matsuyama"), (2020, "Dustin Johnson"), (2019, "Tiger Woods"),
    (2018, "Patrick Reed"), (2017, "Sergio Garcia"), (2016, "Danny Willett"),
    (2015, "Jordan Spieth"), (2014, "Bubba Watson"), (2013, "Adam Scott"),
    (2012, "Bubba Watson"), (2011, "Charl Schwartzel"), (2010, "Phil Mickelson"),
    (2009, "Angel Cabrera"), (2008, "Trevor Immelman"), (2007, "Zach Johnson"),
    (2006, "Phil Mickelson"), (2005, "Tiger Woods"), (2004, "Phil Mickelson"),
    (2003, "Mike Weir"), (2002, "Tiger Woods"), (2001, "Tiger Woods"),
    (2000, "Vijay Singh"), (1999, "Jose Maria Olazabal"), (1998, "Mark O'Meara"),
    (1997, "Tiger Woods"), (1996, "Nick Faldo"), (1995, "Ben Crenshaw"),
    (1994, "Jose Maria Olazabal"), (1993, "Bernhard Langer"), (1992, "Fred Couples"),
    (1991, "Ian Woosnam"), (1990, "Nick Faldo"), (1989, "Nick Faldo"),
    (1988, "Sandy Lyle"), (1987, "Larry Mize"), (1986, "Jack Nicklaus"),
    (1985, "Bernhard Langer"), (1984, "Ben Crenshaw"), (1983, "Seve Ballesteros"),
    (1982, "Craig Stadler"), (1981, "Tom Watson"), (1980, "Seve Ballesteros"),
    (1979, "Fuzzy Zoeller"), (1978, "Gary Player"), (1977, "Tom Watson"),
    (1976, "Raymond Floyd"), (1975, "Jack Nicklaus"), (1974, "Gary Player"),
    (1973, "Tommy Aaron"), (1972, "Jack Nicklaus"), (1971, "Charles Coody"),
    (1970, "Billy Casper"), (1969, "George Archer"), (1968, "Bob Goalby"),
    (1967, "Gay Brewer"), (1966, "Jack Nicklaus"), (1965, "Jack Nicklaus"),
    (1964, "Arnold Palmer"), (1963, "Jack Nicklaus"), (1962, "Arnold Palmer"),
    (1961, "Gary Player"), (1960, "Arnold Palmer"), (1959, "Art Wall Jr."),
    (1958, "Arnold Palmer"), (1957, "Doug Ford"), (1956, "Jack Burke Jr."),
    (1955, "Cary Middlecoff"), (1954, "Sam Snead"), (1953, "Ben Hogan"),
    (1952, "Sam Snead"), (1951, "Ben Hogan"), (1950, "Jimmy Demaret"),
    (1949, "Sam Snead"), (1948, "Claude Harmon"), (1947, "Jimmy Demaret"),
    (1946, "Herman Keiser"), (1942, "Byron Nelson"), (1941, "Craig Wood"),
    (1940, "Jimmy Demaret"), (1939, "Ralph Guldahl"), (1938, "Henry Picard"),
    (1937, "Byron Nelson"), (1936, "Horton Smith"), (1935, "Gene Sarazen"),
    (1934, "Horton Smith"),
]

golf_players = ["Tiger Woods","Jack Nicklaus","Arnold Palmer","Phil Mickelson","Nick Faldo",
    "Gary Player","Tom Watson","Seve Ballesteros","Rory McIlroy","Jordan Spieth","Dustin Johnson",
    "Scottie Scheffler","Jon Rahm","Brooks Koepka","Justin Thomas","Adam Scott","Bubba Watson",
    "Sergio Garcia","Greg Norman","Bernhard Langer","Nick Price","Lee Trevino","Sam Snead",
    "Ben Hogan","Byron Nelson","Gene Sarazen","Walter Hagen","Bobby Jones","Billy Casper",
    "Johnny Miller","Tom Kite","Vijay Singh","Ernie Els","Retief Goosen","Colin Montgomerie"]

for yr, champ in masters_champs:
    wrongs = [p for p in golf_players if p != champ]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won The Masters golf tournament in {yr}?",
        champ,
        wrongs[:3],
        "golf", "hard"
    ))

print(f"After Masters: {len(questions)}")

# Additional golf static questions
golf_questions = [
    ("What is the name of the most famous golf tournament held at Augusta National?", "The Masters", ["The Open Championship","The US Open","The PGA Championship"], "easy"),
    ("The four golf Major championships are The Masters, US Open, The Open Championship, and which other?", "PGA Championship", ["Players Championship","World Match Play","WGC Championship"], "easy"),
    ("Tiger Woods won how many major championships?", "15", ["14","18","12"], "easy"),
    ("Jack Nicklaus won how many major championships (the all-time record)?", "18", ["15","16","20"], "easy"),
    ("A 'birdie' in golf means scoring how many strokes under par?", "1 stroke under par", ["2 strokes under par","3 strokes under par","Equal to par"], "easy"),
    ("An 'eagle' in golf means scoring how many strokes under par?", "2 strokes under par", ["1 stroke under par","3 strokes under par","4 strokes under par"], "easy"),
    ("The Open Championship is played on which type of course?", "Links course", ["Parkland course","Desert course","Heathland course"], "easy"),
    ("Phil Mickelson is known for which shot in golf?", "His left-handed swing as a naturally right-handed person", ["His chip shots","His sand shots","His putting style"], "easy"),
    ("Tiger Woods won The Masters in 1997 at what age?", "21", ["23","18","25"], "easy"),
    ("What does PGA stand for in golf?", "Professional Golfers Association", ["Professional Golf Alliance","Players Golf Association","Premier Golf Association"], "easy"),
    ("The Ryder Cup is played between which two groups?", "Europe and the United States", ["USA and Great Britain","USA and the Rest of World","Europe and Australasia"], "medium"),
    ("Rory McIlroy is from which country?", "Northern Ireland", ["Republic of Ireland","England","Scotland"], "medium"),
    ("Which golfer is known as 'The Golden Bear'?", "Jack Nicklaus", ["Arnold Palmer","Gary Player","Lee Trevino"], "medium"),
    ("Who won the 1986 Masters at age 46, the oldest Masters champion ever?", "Jack Nicklaus", ["Arnold Palmer","Gary Player","Tom Watson"], "medium"),
    ("Seve Ballesteros was from which country?", "Spain", ["Portugal","Argentina","Italy"], "medium"),
    ("Tiger Woods's longest winning streak was how many consecutive PGA Tour victories?", "7", ["5","9","11"], "medium"),
    ("Which country dominated the Ryder Cup from 1985 to present, winning more than the USA?", "Europe", ["Great Britain","USA","Rest of World"], "medium"),
    ("Arnold Palmer's first Masters win was in which year?", "1958", ["1954","1960","1962"], "medium"),
    ("Greg Norman famously blew a 6-shot lead on the final day of the 1996 Masters. Who won?", "Nick Faldo", ["Nick Price","Fred Couples","Jose Maria Olazabal"], "medium"),
    ("The term 'bogey' in golf (a score of one over par) originated in the late 1800s. What was it originally named after?", "A fictional bogeyman golfer", ["A British military officer","A poor golfer named Bogey","An old Scottish word for trouble"], "medium"),
    ("Which golfer was known as 'The Black Knight' and won 9 major championships?", "Gary Player", ["Vijay Singh","Calvin Peete","Harold Henning"], "hard"),
    ("How many times did Ben Hogan win The Masters?", "2", ["1","3","4"], "hard"),
    ("Sam Snead is the PGA Tour's all-time wins leader with how many victories?", "82", ["76","71","90"], "hard"),
    ("The term 'birdie' in golf is said to have originated with a shot from which player?", "Ab Smith in 1898", ["Harry Vardon","Old Tom Morris","Willie Park"], "hard"),
    ("Which golfer was the first to shoot a 59 in a PGA Tour event?", "Al Geiberger (1977)", ["Chip Beck","David Duval","Tiger Woods"], "hard"),
    ("Byron Nelson won how many consecutive PGA Tour events in his legendary 1945 season?", "11", ["9","13","7"], "hard"),
    ("Tom Watson won The Open Championship how many times?", "5", ["4","6","3"], "hard"),
    ("Which year did Tiger Woods win all four Majors consecutively (the Tiger Slam)?", "2000-2001", ["2001-2002","1999-2000","2002-2003"], "hard"),
    ("Who was the first golfer to complete the career Grand Slam in the modern era?", "Gene Sarazen (1935)", ["Ben Hogan","Sam Snead","Byron Nelson"], "hard"),
    ("The Walker Cup in golf is an amateur competition between which two countries?", "USA and Great Britain/Ireland", ["USA and Europe","USA and Canada","Europe and Australia"], "hard"),
]

for text, ans, wrongs, diff in golf_questions:
    questions.append(q(text, ans, wrongs, "golf", diff))

print(f"After golf: {len(questions)}")

# ============================================================
# OLYMPICS DATA
# ============================================================
olympics_hosts = [
    (2024, "Paris", "France"), (2021, "Tokyo", "Japan"), (2016, "Rio de Janeiro", "Brazil"),
    (2012, "London", "United Kingdom"), (2008, "Beijing", "China"), (2004, "Athens", "Greece"),
    (2000, "Sydney", "Australia"), (1996, "Atlanta", "USA"), (1992, "Barcelona", "Spain"),
    (1988, "Seoul", "South Korea"), (1984, "Los Angeles", "USA"), (1980, "Moscow", "Soviet Union"),
    (1976, "Montreal", "Canada"), (1972, "Munich", "West Germany"), (1968, "Mexico City", "Mexico"),
    (1964, "Tokyo", "Japan"), (1960, "Rome", "Italy"), (1956, "Melbourne", "Australia"),
    (1952, "Helsinki", "Finland"), (1948, "London", "United Kingdom"), (1936, "Berlin", "Germany"),
    (1932, "Los Angeles", "USA"), (1928, "Amsterdam", "Netherlands"), (1924, "Paris", "France"),
    (1920, "Antwerp", "Belgium"), (1912, "Stockholm", "Sweden"), (1908, "London", "United Kingdom"),
    (1904, "St. Louis", "USA"), (1900, "Paris", "France"), (1896, "Athens", "Greece"),
]

all_cities = ["Paris","Tokyo","London","Rio de Janeiro","Beijing","Athens","Sydney","Atlanta",
    "Barcelona","Seoul","Los Angeles","Moscow","Montreal","Munich","Mexico City","Rome",
    "Melbourne","Helsinki","Berlin","Amsterdam","Antwerp","Stockholm","St. Louis","Madrid",
    "New York","Sydney","Chicago","Toronto"]

for yr, city, country in olympics_hosts:
    wrongs = [c for c in all_cities if c != city]
    random.shuffle(wrongs)
    questions.append(q(
        f"Which city hosted the Summer Olympics in {yr}?",
        city,
        wrongs[:3],
        "olympics", "medium"
    ))
    questions.append(q(
        f"The {yr} Summer Olympics were held in which country?",
        country,
        [c for c in ["France","Japan","Brazil","United Kingdom","China","Greece","Australia","USA","Spain","South Korea","Soviet Union","Canada","West Germany","Mexico","Italy","Finland","Germany","Netherlands","Belgium","Sweden"] if c != country][:3],
        "olympics", "medium"
    ))

print(f"After Olympics hosts: {len(questions)}")

# Olympics static questions
olympics_questions = [
    ("In which year were the modern Olympics first held?", "1896", ["1904","1900","1892"], "easy"),
    ("The ancient Olympics were held in which Greek city?", "Olympia", ["Athens","Sparta","Corinth"], "easy"),
    ("How often are the Summer Olympics held?", "Every 4 years", ["Every 2 years","Every 3 years","Every 5 years"], "easy"),
    ("Usain Bolt is from which country?", "Jamaica", ["Trinidad and Tobago","Barbados","Bahamas"], "easy"),
    ("Michael Phelps won how many total Olympic medals?", "28", ["23","25","30"], "easy"),
    ("The Olympic rings represent which five continents?", "Africa, Americas, Asia, Europe, Oceania", ["North America, South America, Europe, Asia, Africa","All six inhabited continents","The five founding nations"], "easy"),
    ("Which country has won the most Summer Olympic gold medals all-time?", "United States", ["Soviet Union","China","Germany"], "easy"),
    ("Jesse Owens won 4 gold medals at which Olympics, embarrassing the Nazi regime?", "1936 Berlin", ["1932 Los Angeles","1928 Amsterdam","1940 (cancelled)"], "easy"),
    ("In which year did the Olympics ban professional athletes from competing?", "They never fully banned professionals - the Open Era began in 1992", ["1988","1984","1972"], "easy"),
    ("Carl Lewis won how many Olympic gold medals?", "9", ["8","10","7"], "easy"),
    ("The 1980 Summer Olympics boycott was led by the United States in protest of what?", "The Soviet invasion of Afghanistan", ["The Iran hostage crisis","Nuclear testing","Human rights abuses"], "medium"),
    ("Which female gymnast scored the first perfect 10 in Olympic history?", "Nadia Comaneci (1976)", ["Olga Korbut","Larissa Latynina","Mary Lou Retton"], "medium"),
    ("The 1972 Munich Olympics were tragically marred by what event?", "The murder of Israeli athletes by Palestinian terrorists", ["A doping scandal","A political boycott","A stadium fire"], "medium"),
    ("Which marathon runner collapsed but finished the race at the 1908 London Olympics?", "Dorando Pietri", ["Spiridon Louis","Thaddeus Shideler","John Hayes"], "medium"),
    ("Usain Bolt set the 100m world record at the 2009 World Championships with what time?", "9.58 seconds", ["9.63 seconds","9.72 seconds","9.69 seconds"], "medium"),
    ("Who won the first women's marathon at the 1984 Olympics?", "Joan Benoit", ["Grete Waitz","Rosa Mota","Ingrid Kristiansen"], "medium"),
    ("The longest long jump world record stood for over 23 years. Who set it?", "Mike Powell (8.95m in 1991)", ["Carl Lewis","Bob Beamon","Ralph Boston"], "medium"),
    ("Bob Beamon's legendary long jump at the 1968 Mexico City Olympics measured how far?", "8.90 meters (29 ft 2.5 in)", ["8.75 meters","9.05 meters","8.60 meters"], "medium"),
    ("Which swimmer won 7 gold medals at the 1972 Munich Olympics?", "Mark Spitz", ["Michael Phelps","Ian Thorpe","Matt Biondi"], "medium"),
    ("Simone Biles is considered the greatest gymnast ever. How many World Championship titles has she won?", "19 World Championship medals", ["12","15","22"], "medium"),
    ("Jim Thorpe won the decathlon and pentathlon at the 1912 Olympics but had medals stripped for what reason?", "For playing semi-professional baseball", ["For doping","For citizenship issues","For age falsification"], "hard"),
    ("Which country topped the medal table at the 1936 Berlin Olympics?", "Germany", ["United States","Hungary","Finland"], "hard"),
    ("Abebe Bikila ran the 1960 Olympic marathon barefoot and set a world record. He was from which country?", "Ethiopia", ["Kenya","Tanzania","Eritrea"], "hard"),
    ("The first Olympic Games of the modern era took place in Athens in 1896. How many nations participated?", "14", ["10","20","6"], "hard"),
    ("What is the motto of the Olympic Games?", "Faster, Higher, Stronger - Together (Citius, Altius, Fortius - Communiter)", ["Peace, Love, Unity","Excellence, Respect, Friendship","Swifter, Higher, Stronger"], "hard"),
    ("The IOC was founded in which year?", "1894", ["1896","1900","1890"], "hard"),
    ("Who lit the Olympic cauldron at the 1996 Atlanta Games in a surprise appearance?", "Muhammad Ali", ["Carl Lewis","Michael Johnson","Evander Holyfield"], "hard"),
    ("Emil Zatopek won three long-distance gold medals (5K, 10K, Marathon) at which Olympics?", "1952 Helsinki", ["1948 London","1956 Melbourne","1960 Rome"], "hard"),
    ("The first Winter Olympics were held in which year and city?", "1924, Chamonix, France", ["1920, Antwerp, Belgium","1928, St. Moritz, Switzerland","1932, Lake Placid, USA"], "hard"),
    ("Larissa Latynina held the record for most Olympic medals until surpassed by whom?", "Michael Phelps", ["Carl Lewis","Paavo Nurmi","Mark Spitz"], "hard"),
]

for text, ans, wrongs, diff in olympics_questions:
    questions.append(q(text, ans, wrongs, "olympics", diff))

print(f"After olympics: {len(questions)}")

# ============================================================
# UFC / MMA DATA
# ============================================================
ufc_questions = [
    ("Who is known as 'The Notorious' in the UFC?", "Conor McGregor", ["Nate Diaz","Khabib Nurmagomedov","Tony Ferguson"], "easy"),
    ("Who is considered the greatest UFC fighter of all time by many fans?", "Anderson Silva or Jon Jones", ["Conor McGregor","Georges St-Pierre","Khabib Nurmagomedov"], "easy"),
    ("Which fighter went undefeated for 29-0 in the UFC?", "Khabib Nurmagomedov", ["Jon Jones","Stipe Miocic","Fedor Emelianenko"], "easy"),
    ("Jon Jones fights at which weight class?", "Light Heavyweight / Heavyweight", ["Middleweight","Welterweight","Featherweight"], "easy"),
    ("The UFC stands for what?", "Ultimate Fighting Championship", ["Universal Fighting Championship","United Fighting Circuit","Ultra Fighting Championship"], "easy"),
    ("Which fighter is nicknamed 'The Spider'?", "Anderson Silva", ["Jon Jones","Frankie Edgar","Demetrious Johnson"], "easy"),
    ("Conor McGregor was the first UFC fighter to hold titles in how many divisions simultaneously?", "2", ["3","1","4"], "easy"),
    ("Who founded the UFC in 1993?", "Art Davie and Rorion Gracie", ["Dana White","Randy Couture","Chuck Liddell"], "easy"),
    ("Dana White is the current president of which organization?", "UFC", ["Bellator","ONE Championship","PFL"], "easy"),
    ("Which former champion is known as 'Captain America'?", "Chris Weidman", ["Brock Lesnar","Dan Henderson","Randy Couture"], "easy"),
    ("Who did Conor McGregor fight in his boxing match in 2017?", "Floyd Mayweather", ["Manny Pacquiao","Andre Ward","Gennady Golovkin"], "easy"),
    ("Who was Conor McGregor's rival in their famous two-fight series?", "Nate Diaz", ["Jose Aldo","Eddie Alvarez","Max Holloway"], "easy"),
    ("Which fighter holds the record for most title defenses in UFC middleweight history?", "Anderson Silva (10)", ["Jon Jones","Georges St-Pierre","Demetrious Johnson"], "medium"),
    ("Georges St-Pierre is from which country?", "Canada", ["France","USA","Brazil"], "medium"),
    ("Which UFC fighter was the first to win titles in two weight classes?", "Conor McGregor", ["Jon Jones","Daniel Cormier","Frankie Edgar"], "medium"),
    ("Stipe Miocic holds the record for most consecutive UFC heavyweight title defenses. How many?", "3", ["4","2","5"], "medium"),
    ("Which boxer fought Anderson Silva in a boxing match in 2023?", "Jake Paul", ["Logan Paul","Tommy Fury","KSI"], "medium"),
    ("Khabib Nurmagomedov is from which country?", "Russia (Republic of Dagestan)", ["Kazakhstan","Azerbaijan","Chechnya"], "medium"),
    ("Who did Khabib Nurmagomedov defeat to win his first UFC title?", "Al Iaquinta", ["Tony Ferguson","Eddie Alvarez","Dustin Poirier"], "medium"),
    ("Jon Jones first won the light heavyweight title by defeating which fighter?", "Mauricio Shogun Rua", ["Lyoto Machida","Rashad Evans","Quinton Jackson"], "medium"),
    ("UFC 1 was held in which city in 1993?", "Denver, Colorado", ["Las Vegas","New York","Los Angeles"], "medium"),
    ("Demetrious Johnson defended the flyweight title how many times consecutively?", "11", ["9","7","13"], "hard"),
    ("Which UFC event featured the biggest upset when Holly Holm knocked out Ronda Rousey?", "UFC 193", ["UFC 200","UFC 181","UFC 170"], "hard"),
    ("Fedor Emelianenko is considered by many as the greatest heavyweight MMA fighter. He fought primarily in which organization?", "PRIDE FC and Strikeforce", ["UFC","Bellator","ONE Championship"], "hard"),
    ("Which Gracie family member competed in UFC 1 and pioneered Brazilian Jiu-Jitsu in MMA?", "Royce Gracie", ["Rickson Gracie","Royler Gracie","Renzo Gracie"], "hard"),
    ("Alexander Volkanovski holds the record for consecutive wins in the featherweight division. How many?", "12", ["10","8","14"], "hard"),
    ("Who was the first female UFC champion?", "Ronda Rousey", ["Cristiane Justino","Holly Holm","Miesha Tate"], "hard"),
    ("The first UFC event with a woman on the main card featured Ronda Rousey vs which opponent?", "Liz Carmouche", ["Miesha Tate","Sara McMann","Cat Zingano"], "hard"),
    ("Chuck Liddell was known for which striking technique?", "His overhand right (hammer fist)", ["Spinning back kick","Flying knee","Leg kicks"], "hard"),
    ("Randy Couture is the only fighter to win UFC titles in how many different weight classes?", "2 (heavyweight and light heavyweight)", ["3","1","4"], "hard"),
    ("Which fighter won The Ultimate Fighter Season 1 and became a UFC champion?", "Forrest Griffin", ["Stephan Bonnar","Diego Sanchez","Nate Quarry"], "hard"),
    ("Israel Adesanya is from which country?", "New Zealand (born in Nigeria)", ["Nigeria","Australia","Ghana"], "hard"),
    ("Leon Edwards won the welterweight title with a head kick KO in the 5th round against who?", "Kamaru Usman", ["Jorge Masvidal","Colby Covington","Gilbert Burns"], "hard"),
    ("Who did Nate Diaz beat to get his shot at Conor McGregor?", "Michael Johnson", ["Donald Cerrone","Benson Henderson","Edson Barboza"], "hard"),
    ("Which UFC champion was nicknamed 'Do Bronx'?", "Charles Oliveira", ["Dustin Poirier","Islam Makhachev","Michael Chandler"], "hard"),
    ("The UFC was acquired by which investment firm in 2016 for $4 billion?", "WME-IMG (Endeavor)", ["Silver Lake Partners","Blackstone","Apollo Global Management"], "hard"),
    ("Who was the first fighter to score a submission victory by D'Arce choke in UFC history?", "Joe Lauzon", ["Frank Mir","Dean Lister","Kenny Florian"], "hard"),
    ("Sergei Kharitonov vs Mirko Cro Cop is associated with which organization?", "PRIDE FC", ["UFC","Strikeforce","Dream"], "hard"),
]

for text, ans, wrongs, diff in ufc_questions:
    questions.append(q(text, ans, wrongs, "ufc", diff))

print(f"After UFC: {len(questions)}")

# ============================================================
# REMOVE duplicates by question text
# ============================================================
seen = set()
unique = []
for item in questions:
    key = item['q'].strip().lower()
    if key not in seen:
        seen.add(key)
        unique.append(item)

questions = unique
print(f"After dedup: {len(questions)} unique questions")

# ============================================================
# VALIDATE and count by sport
# ============================================================
from collections import Counter
sport_counts = Counter(q['sport'] for q in questions)
diff_counts = Counter(q['difficulty'] for q in questions)
print("Sport breakdown:", dict(sport_counts))
print("Difficulty breakdown:", dict(diff_counts))
print(f"TOTAL: {len(questions)} questions")

# ============================================================
# SAVE
# ============================================================
out_path = '/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/questions.json'
with open(out_path, 'w') as f:
    json.dump(questions, f, separators=(',', ':'))

print(f"Saved to {out_path}")
print(f"File size: {os.path.getsize(out_path):,} bytes")
