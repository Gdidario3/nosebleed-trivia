#!/usr/bin/env python3
"""
Part 2 - Additional question generation to reach 10,000+
"""
import json
import random
import os
from collections import Counter

random.seed(123)

# Shared player pools
tennis_players = ["Roger Federer","Rafael Nadal","Novak Djokovic","Pete Sampras","Bjorn Borg",
    "John McEnroe","Andre Agassi","Jimmy Connors","Boris Becker","Stefan Edberg",
    "Andy Murray","Carlos Alcaraz","Lleyton Hewitt","Goran Ivanisevic","Richard Krajicek",
    "Pat Cash","Michael Stich","Mats Wilander","Ivan Lendl","Guillermo Vilas",
    "Ilie Nastase","Arthur Ashe","Stan Smith","Marcelo Rios","Andy Roddick"]

golf_players = ["Tiger Woods","Jack Nicklaus","Arnold Palmer","Phil Mickelson","Nick Faldo",
    "Gary Player","Tom Watson","Seve Ballesteros","Rory McIlroy","Jordan Spieth","Dustin Johnson",
    "Scottie Scheffler","Jon Rahm","Brooks Koepka","Justin Thomas","Adam Scott","Bubba Watson",
    "Sergio Garcia","Greg Norman","Bernhard Langer","Nick Price","Lee Trevino","Sam Snead",
    "Ben Hogan","Byron Nelson","Gene Sarazen","Walter Hagen","Bobby Jones","Billy Casper",
    "Johnny Miller","Tom Kite","Vijay Singh","Ernie Els","Retief Goosen","Colin Montgomerie"]

def shuffle_choices(correct, wrongs):
    choices = [correct] + list(wrongs[:3])
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

# ============================================================
# NBA FINALS MVP DATA
# ============================================================
nba_finals_mvp = [
    (2023, "Nikola Jokic"), (2022, "Stephen Curry"), (2021, "Giannis Antetokounmpo"),
    (2020, "LeBron James"), (2019, "Kawhi Leonard"), (2018, "Kevin Durant"),
    (2017, "Kevin Durant"), (2016, "LeBron James"), (2015, "Andre Iguodala"),
    (2014, "Kawhi Leonard"), (2013, "LeBron James"), (2012, "LeBron James"),
    (2011, "Dirk Nowitzki"), (2010, "Kobe Bryant"), (2009, "Kobe Bryant"),
    (2008, "Paul Pierce"), (2007, "Tony Parker"), (2006, "Dwyane Wade"),
    (2005, "Tim Duncan"), (2004, "Chauncey Billups"), (2003, "Tim Duncan"),
    (2002, "Shaquille O'Neal"), (2001, "Shaquille O'Neal"), (2000, "Shaquille O'Neal"),
    (1999, "Tim Duncan"), (1998, "Michael Jordan"), (1997, "Michael Jordan"),
    (1996, "Michael Jordan"), (1995, "Hakeem Olajuwon"), (1994, "Hakeem Olajuwon"),
    (1993, "Michael Jordan"), (1992, "Michael Jordan"), (1991, "Michael Jordan"),
    (1990, "Isiah Thomas"), (1989, "Joe Dumars"), (1988, "James Worthy"),
    (1987, "Magic Johnson"), (1986, "Larry Bird"), (1985, "Kareem Abdul-Jabbar"),
    (1984, "Larry Bird"), (1983, "Moses Malone"), (1982, "Magic Johnson"),
    (1981, "Cedric Maxwell"), (1980, "Magic Johnson"), (1979, "Dennis Johnson"),
    (1978, "Wes Unseld"), (1977, "Bill Walton"), (1976, "Jo Jo White"),
    (1975, "Rick Barry"), (1974, "John Havlicek"), (1973, "Willis Reed"),
    (1972, "Wilt Chamberlain"), (1971, "Kareem Abdul-Jabbar"), (1970, "Willis Reed"),
    (1969, "Jerry West"),
]

nba_players = ["Nikola Jokic","Stephen Curry","Giannis Antetokounmpo","LeBron James","Kawhi Leonard",
    "Kevin Durant","Andre Iguodala","Dirk Nowitzki","Kobe Bryant","Paul Pierce","Tony Parker",
    "Dwyane Wade","Tim Duncan","Chauncey Billups","Shaquille O'Neal","Michael Jordan","Hakeem Olajuwon",
    "Isiah Thomas","Joe Dumars","James Worthy","Magic Johnson","Larry Bird","Kareem Abdul-Jabbar",
    "Moses Malone","Willis Reed","Bill Walton","Rick Barry","Jerry West","Wilt Chamberlain",
    "John Havlicek","Jo Jo White","Dennis Johnson","Patrick Ewing","Karl Malone","Charles Barkley",
    "Reggie Miller","Ray Allen","Chris Paul","Damian Lillard","Kyrie Irving","Russell Westbrook",
    "James Harden","Blake Griffin","Derrick Rose","Chris Bosh","Dwight Howard","Paul George"]

for yr, mvp in nba_finals_mvp:
    wrongs = [p for p in nba_players if p != mvp]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the NBA Finals MVP award in {yr}?",
        mvp,
        wrongs[:3],
        "basketball", "hard"
    ))

# NBA MVP Award
nba_mvp_data = [
    (2024, "Nikola Jokic"), (2023, "Joel Embiid"), (2022, "Nikola Jokic"),
    (2021, "Nikola Jokic"), (2020, "Giannis Antetokounmpo"), (2019, "Giannis Antetokounmpo"),
    (2018, "James Harden"), (2017, "Russell Westbrook"), (2016, "Stephen Curry"),
    (2015, "Stephen Curry"), (2014, "Kevin Durant"), (2013, "LeBron James"),
    (2012, "LeBron James"), (2011, "Derrick Rose"), (2010, "LeBron James"),
    (2009, "LeBron James"), (2008, "Kobe Bryant"), (2007, "Dirk Nowitzki"),
    (2006, "Steve Nash"), (2005, "Steve Nash"), (2004, "Kevin Garnett"),
    (2003, "Tim Duncan"), (2002, "Tim Duncan"), (2001, "Allen Iverson"),
    (2000, "Shaquille O'Neal"), (1999, "Karl Malone"), (1998, "Michael Jordan"),
    (1997, "Karl Malone"), (1996, "Michael Jordan"), (1995, "David Robinson"),
    (1994, "Hakeem Olajuwon"), (1993, "Charles Barkley"), (1992, "Michael Jordan"),
    (1991, "Michael Jordan"), (1990, "Magic Johnson"), (1989, "Magic Johnson"),
    (1988, "Michael Jordan"), (1987, "Magic Johnson"), (1986, "Larry Bird"),
    (1985, "Larry Bird"), (1984, "Larry Bird"), (1983, "Moses Malone"),
    (1982, "Moses Malone"), (1981, "Julius Erving"), (1980, "Kareem Abdul-Jabbar"),
    (1979, "Moses Malone"), (1978, "Bill Walton"), (1977, "Kareem Abdul-Jabbar"),
    (1976, "Kareem Abdul-Jabbar"), (1975, "Bob McAdoo"), (1974, "Kareem Abdul-Jabbar"),
    (1973, "Dave Cowens"), (1972, "Kareem Abdul-Jabbar"), (1971, "Kareem Abdul-Jabbar"),
    (1970, "Willis Reed"), (1969, "Wes Unseld"), (1968, "Wilt Chamberlain"),
    (1967, "Wilt Chamberlain"), (1966, "Wilt Chamberlain"), (1965, "Bill Russell"),
    (1964, "Oscar Robertson"), (1963, "Bill Russell"), (1962, "Bill Russell"),
    (1961, "Bill Russell"), (1960, "Wilt Chamberlain"), (1959, "Bob Pettit"),
    (1958, "Bill Russell"), (1957, "Bob Cousy"), (1956, "Bob Pettit"),
]

for yr, mvp in nba_mvp_data:
    wrongs = [p for p in nba_players + ["Bob Pettit","Dave Cowens","Bob McAdoo","Bill Walton",
        "Julius Erving","David Robinson","Wes Unseld","Bob Cousy","Oscar Robertson",
        "Dave Bing","Elgin Baylor","Sam Jones"] if p != mvp]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the NBA Most Valuable Player award for the {yr} season?",
        mvp,
        wrongs[:3],
        "basketball", "hard"
    ))

print(f"After NBA awards: {len(questions)}")

# NBA Draft picks 2-5 for key years
nba_draft_picks = [
    # (year, pick_num, player, team)
    (2003, 2, "Carmelo Anthony", "Denver Nuggets"),
    (2003, 3, "Chris Bosh", "Toronto Raptors"),
    (2003, 5, "Dwyane Wade", "Miami Heat"),
    (2003, 7, "Chris Kaman", "Los Angeles Clippers"),
    (2003, 18, "Leandro Barbosa", "San Antonio Spurs"),
    (2003, 22, "David West", "New Orleans Hornets"),
    (1984, 2, "Sam Bowie", "Portland Trail Blazers"),
    (1984, 3, "Michael Jordan", "Chicago Bulls"),
    (1984, 5, "Charles Barkley", "Philadelphia 76ers"),
    (1984, 16, "John Stockton", "Utah Jazz"),
    (1985, 2, "Wayman Tisdale", "Indiana Pacers"),
    (1985, 5, "Karl Malone", "Utah Jazz"),
    (1996, 2, "Allen Iverson was 1st, then 2nd overall Shareef Abdur-Rahim", "Vancouver Grizzlies"),
    (1996, 13, "Kobe Bryant", "Charlotte Hornets"),
    (2012, 2, "Michael Kidd-Gilchrist", "Charlotte Bobcats"),
    (2012, 3, "Bradley Beal", "Washington Wizards"),
    (1997, 2, "Keith Van Horn", "New Jersey Nets"),
    (1997, 3, "Chauncey Billups", "Boston Celtics"),
    (2001, 2, "Shane Battier", "Memphis Grizzlies"),
    (2001, 4, "Pau Gasol", "Atlanta Hawks"),
    (2005, 2, "Marvin Williams", "Atlanta Hawks"),
    (2005, 3, "Deron Williams", "Utah Jazz"),
    (2005, 4, "Chris Paul", "New Orleans Hornets"),
    (2009, 2, "Hasheem Thabeet", "Memphis Grizzlies"),
    (2009, 3, "James Harden", "Oklahoma City Thunder"),
    (2009, 4, "Tyreke Evans", "Sacramento Kings"),
    (2010, 2, "Evan Turner", "Philadelphia 76ers"),
    (2010, 3, "Derrick Favors", "New Jersey Nets"),
    (2010, 4, "Wesley Johnson", "Minnesota Timberwolves"),
    (1992, 2, "Alonzo Mourning", "Charlotte Hornets"),
    (1992, 3, "Jim Jackson", "Dallas Mavericks"),
    (1998, 2, "Mike Bibby", "Vancouver Grizzlies"),
    (1998, 5, "Vince Carter", "Golden State Warriors"),
    (2007, 2, "Kevin Durant", "Seattle SuperSonics"),
    (2007, 3, "Al Horford", "Atlanta Hawks"),
    (2008, 2, "Michael Beasley", "Miami Heat"),
    (2008, 5, "Kevin Love", "Memphis Grizzlies"),
    (2014, 2, "Joel Embiid", "Philadelphia 76ers"),
    (2014, 3, "Dante Exum", "Utah Jazz"),
    (2014, 5, "Marcus Smart", "Boston Celtics"),
    (2015, 2, "D'Angelo Russell", "Los Angeles Lakers"),
    (2015, 4, "Kristaps Porzingis", "New York Knicks"),
    (2016, 2, "Brandon Ingram", "Los Angeles Lakers"),
    (2016, 4, "Dragan Bender", "Phoenix Suns"),
    (2017, 2, "Lonzo Ball", "Los Angeles Lakers"),
    (2017, 3, "Jayson Tatum", "Boston Celtics"),
    (2018, 3, "Luka Doncic", "Atlanta Hawks"),
    (2018, 4, "Jaren Jackson Jr.", "Memphis Grizzlies"),
    (2019, 2, "Ja Morant", "Memphis Grizzlies"),
    (2019, 3, "RJ Barrett", "New York Knicks"),
    (2020, 2, "James Wiseman", "Golden State Warriors"),
    (2020, 3, "LaMelo Ball", "Charlotte Hornets"),
    (2021, 2, "Jalen Green", "Houston Rockets"),
    (2021, 5, "Josh Giddey", "Oklahoma City Thunder"),
    (2022, 2, "Chet Holmgren", "Oklahoma City Thunder"),
    (2022, 3, "Jabari Smith Jr.", "Houston Rockets"),
    (2023, 2, "Brandon Miller", "Charlotte Hornets"),
    (2023, 3, "Scoot Henderson", "Portland Trail Blazers"),
]

all_nba_teams_full = ["Denver Nuggets","New Orleans Hornets","Miami Heat","Los Angeles Clippers",
    "San Antonio Spurs","Portland Trail Blazers","Chicago Bulls","Philadelphia 76ers","Utah Jazz",
    "Indiana Pacers","Vancouver Grizzlies","Charlotte Hornets","New Jersey Nets","Boston Celtics",
    "Washington Wizards","Memphis Grizzlies","Oklahoma City Thunder","Atlanta Hawks","Sacramento Kings",
    "Minnesota Timberwolves","Golden State Warriors","Charlotte Bobcats","Houston Rockets",
    "Los Angeles Lakers","New York Knicks","Cleveland Cavaliers","Dallas Mavericks","Detroit Pistons",
    "Phoenix Suns","Milwaukee Bucks","Orlando Magic","Brooklyn Nets","Charlotte Hornets"]

for yr, pick, player, team in nba_draft_picks:
    wrongs_p = [p for p in nba_players + ["Michael Kidd-Gilchrist","Bradley Beal","Keith Van Horn",
        "Chauncey Billups","Shane Battier","Marvin Williams","Deron Williams","Chris Paul",
        "Alonzo Mourning","Vince Carter","Josh Giddey","Scoot Henderson","Brandon Miller"] if p != player]
    random.shuffle(wrongs_p)
    wrongs_t = [t for t in all_nba_teams_full if t != team]
    random.shuffle(wrongs_t)
    questions.append(q(
        f"Who was selected with the {pick}nd/rd/th overall pick in the {yr} NBA Draft?",
        player,
        wrongs_p[:3],
        "basketball", "hard"
    ))
    questions.append(q(
        f"Which team drafted {player} in the {yr} NBA Draft?",
        team,
        wrongs_t[:3],
        "basketball", "hard"
    ))

print(f"After NBA draft picks 2-5: {len(questions)}")

# ============================================================
# NFL SUPER BOWL MVP DATA
# ============================================================
super_bowl_mvp = [
    (58, 2024, "Patrick Mahomes"), (57, 2023, "Patrick Mahomes"),
    (56, 2022, "Cooper Kupp"), (55, 2021, "Tom Brady"),
    (54, 2020, "Patrick Mahomes"), (53, 2019, "Julian Edelman"),
    (52, 2018, "Nick Foles"), (51, 2017, "Tom Brady"),
    (50, 2016, "Von Miller"), (49, 2015, "Tom Brady"),
    (48, 2014, "Malcolm Smith"), (47, 2013, "Joe Flacco"),
    (46, 2012, "Eli Manning"), (45, 2011, "Aaron Rodgers"),
    (44, 2010, "Drew Brees"), (43, 2009, "Santonio Holmes"),
    (42, 2008, "Eli Manning"), (41, 2007, "Peyton Manning"),
    (40, 2006, "Hines Ward"), (39, 2005, "Deion Branch"),
    (38, 2004, "Tom Brady"), (37, 2003, "Dexter Jackson"),
    (36, 2002, "Tom Brady"), (35, 2001, "Ray Lewis"),
    (34, 2000, "Kurt Warner"), (33, 1999, "John Elway"),
    (32, 1998, "Terrell Davis"), (31, 1997, "Desmond Howard"),
    (30, 1996, "Larry Brown"), (29, 1995, "Steve Young"),
    (28, 1994, "Emmitt Smith"), (27, 1993, "Troy Aikman"),
    (26, 1992, "Mark Rypien"), (25, 1991, "Ottis Anderson"),
    (24, 1990, "Joe Montana"), (23, 1989, "Jerry Rice"),
    (22, 1988, "Doug Williams"), (21, 1987, "Phil Simms"),
    (20, 1986, "Richard Dent"), (19, 1985, "Joe Montana"),
    (18, 1984, "Marcus Allen"), (17, 1983, "John Riggins"),
    (16, 1982, "Joe Montana"), (15, 1981, "Jim Plunkett"),
    (14, 1980, "Terry Bradshaw"), (13, 1979, "Terry Bradshaw"),
    (12, 1978, "Harvey Martin/Randy White"), (11, 1977, "Fred Biletnikoff"),
    (10, 1976, "Lynn Swann"), (9, 1975, "Franco Harris"),
    (8, 1974, "Larry Csonka"), (7, 1973, "Jake Scott"),
    (6, 1972, "Roger Staubach"), (5, 1971, "Chuck Howley"),
    (4, 1970, "Len Dawson"), (3, 1969, "Joe Namath"),
    (2, 1968, "Bart Starr"), (1, 1967, "Bart Starr"),
]

nfl_players = ["Patrick Mahomes","Tom Brady","Cooper Kupp","Julian Edelman","Nick Foles",
    "Von Miller","Malcolm Smith","Joe Flacco","Eli Manning","Aaron Rodgers","Drew Brees",
    "Santonio Holmes","Peyton Manning","Hines Ward","Deion Branch","Dexter Jackson","Ray Lewis",
    "Kurt Warner","John Elway","Terrell Davis","Desmond Howard","Larry Brown","Steve Young",
    "Emmitt Smith","Troy Aikman","Mark Rypien","Ottis Anderson","Joe Montana","Jerry Rice",
    "Doug Williams","Phil Simms","Richard Dent","Marcus Allen","John Riggins","Jim Plunkett",
    "Terry Bradshaw","Fred Biletnikoff","Lynn Swann","Franco Harris","Larry Csonka",
    "Roger Staubach","Bart Starr","Joe Namath","Len Dawson","Chuck Howley","Jake Scott",
    "Lamar Jackson","Josh Allen","Dak Prescott","Jalen Hurts","Joe Burrow","Justin Herbert",
    "Derrick Henry","Travis Kelce","Justin Jefferson","Davante Adams","Stefon Diggs"]

for sb_num, yr, mvp in super_bowl_mvp:
    wrongs = [p for p in nfl_players if p != mvp]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who was the Super Bowl MVP in Super Bowl {sb_num} ({yr})?",
        mvp,
        wrongs[:3],
        "football", "hard"
    ))

print(f"After Super Bowl MVPs: {len(questions)}")

# NFL Draft 1st overall picks
nfl_draft_1st = [
    (2024, "Caleb Williams", "Chicago Bears"),
    (2023, "Bryce Young", "Carolina Panthers"),
    (2022, "Travon Walker", "Jacksonville Jaguars"),
    (2021, "Trevor Lawrence", "Jacksonville Jaguars"),
    (2020, "Joe Burrow", "Cincinnati Bengals"),
    (2019, "Kyler Murray", "Arizona Cardinals"),
    (2018, "Baker Mayfield", "Cleveland Browns"),
    (2017, "Myles Garrett", "Cleveland Browns"),
    (2016, "Jared Goff", "Los Angeles Rams"),
    (2015, "Marcus Mariota", "Tennessee Titans"),
    (2014, "Jadeveon Clowney", "Houston Texans"),
    (2013, "Eric Fisher", "Kansas City Chiefs"),
    (2012, "Andrew Luck", "Indianapolis Colts"),
    (2011, "Cam Newton", "Carolina Panthers"),
    (2010, "Sam Bradford", "St. Louis Rams"),
    (2009, "Matthew Stafford", "Detroit Lions"),
    (2008, "Jake Long", "Miami Dolphins"),
    (2007, "JaMarcus Russell", "Oakland Raiders"),
    (2006, "Mario Williams", "Houston Texans"),
    (2005, "Alex Smith", "San Francisco 49ers"),
    (2004, "Eli Manning", "San Diego Chargers"),
    (2003, "Carson Palmer", "Cincinnati Bengals"),
    (2002, "David Carr", "Houston Texans"),
    (2001, "Michael Vick", "Atlanta Falcons"),
    (2000, "Courtney Brown", "Cleveland Browns"),
    (1999, "Tim Couch", "Cleveland Browns"),
    (1998, "Peyton Manning", "Indianapolis Colts"),
    (1997, "Orlando Pace", "St. Louis Rams"),
    (1996, "Keyshawn Johnson", "New York Jets"),
    (1995, "Ki-Jana Carter", "Cincinnati Bengals"),
    (1994, "Dan Wilkinson", "Cincinnati Bengals"),
    (1993, "Drew Bledsoe", "New England Patriots"),
    (1992, "Steve Emtman", "Indianapolis Colts"),
    (1991, "Russell Maryland", "Dallas Cowboys"),
    (1990, "Jeff George", "Indianapolis Colts"),
    (1989, "Troy Aikman", "Dallas Cowboys"),
    (1988, "Aundray Bruce", "Atlanta Falcons"),
    (1987, "Vinny Testaverde", "Tampa Bay Buccaneers"),
    (1986, "Bo Jackson", "Tampa Bay Buccaneers"),
    (1985, "Bruce Smith", "Buffalo Bills"),
    (1984, "Irving Fryar", "New England Patriots"),
    (1983, "John Elway", "Baltimore Colts"),
    (1982, "Kenneth Sims", "New England Patriots"),
    (1981, "George Rogers", "New Orleans Saints"),
    (1980, "Billy Sims", "Detroit Lions"),
    (1979, "Tom Cousineau", "Buffalo Bills"),
    (1978, "Earl Campbell", "Houston Oilers"),
    (1977, "Ricky Bell", "Tampa Bay Buccaneers"),
    (1976, "Lee Roy Selmon", "Tampa Bay Buccaneers"),
    (1975, "Steve Bartkowski", "Atlanta Falcons"),
    (1974, "Ed Jones", "Dallas Cowboys"),
    (1973, "John Matuszak", "Houston Oilers"),
    (1972, "Walt Patulski", "Buffalo Bills"),
    (1971, "Jim Plunkett", "New England Patriots"),
    (1970, "Terry Bradshaw", "Pittsburgh Steelers"),
    (1969, "O.J. Simpson", "Buffalo Bills"),
    (1968, "Ron Yary", "Minnesota Vikings"),
    (1967, "Bubba Smith", "Baltimore Colts"),
    (1966, "Tommy Nobis", "Atlanta Falcons"),
    (1965, "Tucker Frederickson", "New York Giants"),
    (1964, "Dave Parks", "San Francisco 49ers"),
    (1963, "Terry Baker", "Los Angeles Rams"),
    (1962, "Ernie Davis", "Washington Redskins"),
    (1961, "Tommy Mason", "Minnesota Vikings"),
    (1960, "Billy Cannon", "Los Angeles Rams"),
]

all_nfl_teams = ["Chicago Bears","Carolina Panthers","Jacksonville Jaguars","Cincinnati Bengals",
    "Arizona Cardinals","Cleveland Browns","Los Angeles Rams","Tennessee Titans","Houston Texans",
    "Kansas City Chiefs","Indianapolis Colts","New England Patriots","Oakland Raiders",
    "San Francisco 49ers","San Diego Chargers","St. Louis Rams","Detroit Lions","Miami Dolphins",
    "Dallas Cowboys","Atlanta Falcons","New York Jets","Tampa Bay Buccaneers","Buffalo Bills",
    "New Orleans Saints","Baltimore Colts","Pittsburgh Steelers","Minnesota Vikings",
    "Green Bay Packers","Denver Broncos","Seattle Seahawks","New York Giants","Washington Redskins",
    "Philadelphia Eagles","Los Angeles Raiders","Las Vegas Raiders"]

for yr, player, team in nfl_draft_1st:
    wrongs_p = [p for p in nfl_players + ["O.J. Simpson","Terry Bradshaw","Jim Plunkett","Walt Patulski",
        "Earl Campbell","Billy Sims","Tom Cousineau","Steve Bartkowski","Ed Jones",
        "Lee Roy Selmon","Ricky Bell","Bruce Smith","Bo Jackson","Vinny Testaverde",
        "Aundray Bruce","Troy Aikman","Jeff George","Drew Bledsoe","Dan Wilkinson",
        "Ki-Jana Carter","Keyshawn Johnson","Courtney Brown","Tim Couch","Caleb Williams",
        "Bryce Young","Travon Walker","Trevor Lawrence","Kyler Murray","Baker Mayfield",
        "Myles Garrett","Jared Goff","Marcus Mariota","Jadeveon Clowney","Eric Fisher",
        "Andrew Luck","Cam Newton","Sam Bradford","Matthew Stafford","JaMarcus Russell"] if p != player]
    random.shuffle(wrongs_p)
    wrongs_t = [t for t in all_nfl_teams if t != team]
    random.shuffle(wrongs_t)
    questions.append(q(
        f"Who was the first overall pick in the {yr} NFL Draft?",
        player,
        wrongs_p[:3],
        "football", "hard"
    ))
    questions.append(q(
        f"Which team selected {player} first overall in the {yr} NFL Draft?",
        team,
        wrongs_t[:3],
        "football", "hard"
    ))

print(f"After NFL draft: {len(questions)}")

# ============================================================
# MLB - AWARD WINNERS
# ============================================================
# AL/NL MVP per year (just AL for simplicity, then NL)
al_mvp = [
    (2023, "Shohei Ohtani"), (2022, "Aaron Judge"), (2021, "Shohei Ohtani"),
    (2020, "Jose Abreu"), (2019, "Mike Trout"), (2018, "Mookie Betts"),
    (2017, "Jose Altuve"), (2016, "Mike Trout"), (2015, "Josh Donaldson"),
    (2014, "Mike Trout"), (2013, "Miguel Cabrera"), (2012, "Miguel Cabrera"),
    (2011, "Justin Verlander"), (2010, "Josh Hamilton"), (2009, "Joe Mauer"),
    (2008, "Dustin Pedroia"), (2007, "Alex Rodriguez"), (2006, "Justin Morneau"),
    (2005, "Alex Rodriguez"), (2004, "Vladimir Guerrero"), (2003, "Alex Rodriguez"),
    (2002, "Miguel Tejada"), (2001, "Ichiro Suzuki"), (2000, "Jason Giambi"),
    (1999, "Ivan Rodriguez"), (1998, "Juan Gonzalez"), (1997, "Ken Griffey Jr."),
    (1996, "Juan Gonzalez"), (1995, "Mo Vaughn"), (1994, "Frank Thomas"),
    (1993, "Frank Thomas"), (1992, "Dennis Eckersley"), (1991, "Cal Ripken Jr."),
    (1990, "Rickey Henderson"), (1989, "Robin Yount"), (1988, "Jose Canseco"),
    (1987, "George Bell"), (1986, "Roger Clemens"), (1985, "Don Mattingly"),
    (1984, "Willie Hernandez"), (1983, "Cal Ripken Jr."), (1982, "Robin Yount"),
    (1981, "Rollie Fingers"), (1980, "George Brett"), (1979, "Don Baylor"),
    (1978, "Jim Rice"), (1977, "Rod Carew"), (1976, "Thurman Munson"),
    (1975, "Fred Lynn"), (1974, "Jeff Burroughs"), (1973, "Reggie Jackson"),
    (1972, "Dick Allen"), (1971, "Vida Blue"), (1970, "Boog Powell"),
    (1969, "Harmon Killebrew"), (1968, "Denny McLain"), (1967, "Carl Yastrzemski"),
    (1966, "Frank Robinson"), (1965, "Zoilo Versalles"), (1964, "Brooks Robinson"),
    (1963, "Elston Howard"), (1962, "Mickey Mantle"), (1961, "Roger Maris"),
    (1960, "Roger Maris"), (1959, "Nellie Fox"), (1958, "Jackie Jensen"),
    (1957, "Mickey Mantle"), (1956, "Mickey Mantle"), (1955, "Yogi Berra"),
]

nl_mvp = [
    (2023, "Ronald Acuna Jr."), (2022, "Paul Goldschmidt"), (2021, "Bryce Harper"),
    (2020, "Freddie Freeman"), (2019, "Cody Bellinger"), (2018, "Christian Yelich"),
    (2017, "Giancarlo Stanton"), (2016, "Kris Bryant"), (2015, "Bryce Harper"),
    (2014, "Clayton Kershaw"), (2013, "Andrew McCutchen"), (2012, "Buster Posey"),
    (2011, "Ryan Braun"), (2010, "Joey Votto"), (2009, "Albert Pujols"),
    (2008, "Albert Pujols"), (2007, "Jimmy Rollins"), (2006, "Ryan Howard"),
    (2005, "Albert Pujols"), (2004, "Barry Bonds"), (2003, "Barry Bonds"),
    (2002, "Barry Bonds"), (2001, "Barry Bonds"), (2000, "Jeff Kent"),
    (1999, "Chipper Jones"), (1998, "Sammy Sosa"), (1997, "Larry Walker"),
    (1996, "Ken Caminiti"), (1995, "Barry Larkin"), (1994, "Jeff Bagwell"),
    (1993, "Barry Bonds"), (1992, "Barry Bonds"), (1991, "Terry Pendleton"),
    (1990, "Barry Bonds"), (1989, "Kevin Mitchell"), (1988, "Kirk Gibson"),
    (1987, "Andre Dawson"), (1986, "Mike Schmidt"), (1985, "Willie McGee"),
    (1984, "Ryne Sandberg"), (1983, "Dale Murphy"), (1982, "Dale Murphy"),
    (1981, "Mike Schmidt"), (1980, "Mike Schmidt"), (1979, "Keith Hernandez and Willie Stargell"),
    (1978, "Dave Parker"), (1977, "George Foster"), (1976, "George Foster"),
    (1975, "Joe Morgan"), (1974, "Steve Garvey"), (1973, "Pete Rose"),
]

mlb_players = ["Shohei Ohtani","Aaron Judge","Jose Abreu","Mike Trout","Mookie Betts","Jose Altuve",
    "Josh Donaldson","Miguel Cabrera","Justin Verlander","Josh Hamilton","Joe Mauer","Alex Rodriguez",
    "Ivan Rodriguez","Ken Griffey Jr.","Frank Thomas","Cal Ripken Jr.","Rickey Henderson","Roger Clemens",
    "Don Mattingly","George Brett","Jim Rice","Rod Carew","Fred Lynn","Carl Yastrzemski","Frank Robinson",
    "Mickey Mantle","Roger Maris","Yogi Berra","Ronald Acuna Jr.","Paul Goldschmidt","Bryce Harper",
    "Freddie Freeman","Cody Bellinger","Christian Yelich","Giancarlo Stanton","Kris Bryant",
    "Clayton Kershaw","Andrew McCutchen","Buster Posey","Ryan Braun","Joey Votto","Albert Pujols",
    "Barry Bonds","Jeff Kent","Chipper Jones","Sammy Sosa","Larry Walker","Jeff Bagwell",
    "Kirk Gibson","Andre Dawson","Mike Schmidt","Ryne Sandberg","Dale Murphy","Pete Rose"]

for yr, mvp in al_mvp:
    wrongs = [p for p in mlb_players if p != mvp]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the American League MVP award in {yr}?",
        mvp,
        wrongs[:3],
        "baseball", "hard"
    ))

for yr, mvp in nl_mvp:
    wrongs = [p for p in mlb_players if p != mvp]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the National League MVP award in {yr}?",
        mvp,
        wrongs[:3],
        "baseball", "hard"
    ))

print(f"After MLB MVPs: {len(questions)}")

# Cy Young Award winners (AL)
al_cy_young = [
    (2023, "Gerrit Cole"), (2022, "Justin Verlander"), (2021, "Robbie Ray"),
    (2020, "Shane Bieber"), (2019, "Justin Verlander"), (2018, "Blake Snell"),
    (2017, "Corey Kluber"), (2016, "Rick Porcello"), (2015, "Dallas Keuchel"),
    (2014, "Corey Kluber"), (2013, "Max Scherzer"), (2012, "David Price"),
    (2011, "Justin Verlander"), (2010, "Felix Hernandez"), (2009, "Zack Greinke"),
    (2008, "Cliff Lee"), (2007, "CC Sabathia"), (2006, "Johan Santana"),
    (2005, "Bartolo Colon"), (2004, "Johan Santana"), (2003, "Roy Halladay"),
    (2002, "Barry Zito"), (2001, "Roger Clemens"), (2000, "Pedro Martinez"),
    (1999, "Pedro Martinez"), (1998, "Roger Clemens"), (1997, "Roger Clemens"),
    (1996, "Pat Hentgen"), (1995, "Randy Johnson"), (1994, "David Cone"),
    (1993, "Jack McDowell"), (1992, "Dennis Eckersley"), (1991, "Roger Clemens"),
    (1990, "Bob Welch"), (1989, "Bret Saberhagen"), (1988, "Frank Viola"),
    (1987, "Roger Clemens"), (1986, "Roger Clemens"), (1985, "Bret Saberhagen"),
    (1984, "Willie Hernandez"), (1983, "LaMarr Hoyt"), (1982, "Pete Vuckovich"),
    (1981, "Rollie Fingers"), (1980, "Steve Stone"), (1979, "Mike Flanagan"),
    (1978, "Ron Guidry"), (1977, "Sparky Lyle"), (1976, "Jim Palmer"),
    (1975, "Jim Palmer"), (1974, "Catfish Hunter"), (1973, "Jim Palmer"),
    (1972, "Gaylord Perry"), (1971, "Vida Blue"),
]

nl_cy_young = [
    (2023, "Blake Snell"), (2022, "Sandy Alcantara"), (2021, "Corbin Burnes"),
    (2020, "Trevor Bauer"), (2019, "Jacob deGrom"), (2018, "Jacob deGrom"),
    (2017, "Max Scherzer"), (2016, "Max Scherzer"), (2015, "Jake Arrieta"),
    (2014, "Clayton Kershaw"), (2013, "Clayton Kershaw"), (2012, "R.A. Dickey"),
    (2011, "Clayton Kershaw"), (2010, "Roy Halladay"), (2009, "Tim Lincecum"),
    (2008, "Tim Lincecum"), (2007, "Jake Peavy"), (2006, "Brandon Webb"),
    (2005, "Chris Carpenter"), (2004, "Roger Clemens"), (2003, "Eric Gagne"),
    (2002, "Randy Johnson"), (2001, "Randy Johnson"), (2000, "Randy Johnson"),
    (1999, "Randy Johnson"), (1998, "Tom Glavine"), (1997, "Pedro Martinez"),
    (1996, "John Smoltz"), (1995, "Tom Glavine"), (1994, "Greg Maddux"),
    (1993, "Greg Maddux"), (1992, "Greg Maddux"), (1991, "Tom Glavine"),
    (1990, "Doug Drabek"), (1989, "Mike Scott"), (1988, "Orel Hershiser"),
    (1987, "Steve Bedrosian"), (1986, "Mike Scott"), (1985, "Dwight Gooden"),
    (1984, "Rick Sutcliffe"), (1983, "John Denny"), (1982, "Steve Carlton"),
    (1981, "Fernando Valenzuela"), (1980, "Steve Carlton"), (1979, "Bruce Sutter"),
    (1978, "Gaylord Perry"), (1977, "Steve Carlton"), (1976, "Randy Jones"),
    (1975, "Tom Seaver"), (1974, "Mike Marshall"), (1973, "Tom Seaver"),
    (1972, "Steve Carlton"), (1971, "Ferguson Jenkins"),
]

pitchers = ["Gerrit Cole","Justin Verlander","Robbie Ray","Shane Bieber","Blake Snell","Corey Kluber",
    "Rick Porcello","Dallas Keuchel","Max Scherzer","David Price","Felix Hernandez","Zack Greinke",
    "Cliff Lee","CC Sabathia","Johan Santana","Bartolo Colon","Roy Halladay","Barry Zito",
    "Roger Clemens","Pedro Martinez","Randy Johnson","Greg Maddux","Tom Glavine","John Smoltz",
    "Clayton Kershaw","Jacob deGrom","Sandy Alcantara","Corbin Burnes","Trevor Bauer","Jake Arrieta",
    "R.A. Dickey","Tim Lincecum","Jake Peavy","Brandon Webb","Chris Carpenter","Eric Gagne",
    "John Denny","Steve Carlton","Tom Seaver","Dwight Gooden","Orel Hershiser","Nolan Ryan",
    "Bob Gibson","Sandy Koufax","Whitey Ford","Don Drysdale","Jim Palmer","Catfish Hunter",
    "Mike Flanagan","Ron Guidry","Sparky Lyle","Bret Saberhagen","Bob Welch","Jack McDowell"]

for yr, pitcher in al_cy_young:
    wrongs = [p for p in pitchers if p != pitcher]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the American League Cy Young Award in {yr}?",
        pitcher,
        wrongs[:3],
        "baseball", "hard"
    ))

for yr, pitcher in nl_cy_young:
    wrongs = [p for p in pitchers if p != pitcher]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the National League Cy Young Award in {yr}?",
        pitcher,
        wrongs[:3],
        "baseball", "hard"
    ))

print(f"After Cy Young: {len(questions)}")

# ============================================================
# NHL - AWARD WINNERS
# ============================================================
# Hart Trophy (NHL MVP)
nhl_hart = [
    (2024, "Nathan MacKinnon"), (2023, "Connor McDavid"), (2022, "Auston Matthews"),
    (2021, "Connor McDavid"), (2020, "Leon Draisaitl"), (2019, "Nikita Kucherov"),
    (2018, "Taylor Hall"), (2017, "Connor McDavid"), (2016, "Patrick Kane"),
    (2015, "Carey Price"), (2014, "Ryan Getzlaf"), (2013, "Alex Ovechkin"),
    (2012, "Evgeni Malkin"), (2011, "Corey Perry"), (2010, "Henrik Sedin"),
    (2009, "Alexander Ovechkin"), (2008, "Alexander Ovechkin"), (2007, "Sidney Crosby"),
    (2006, "Joe Thornton"), (2005, "No award - lockout"), (2004, "Martin St. Louis"),
    (2003, "Peter Forsberg"), (2002, "Jose Theodore"), (2001, "Joe Sakic"),
    (2000, "Chris Pronger"), (1999, "Jaromir Jagr"), (1998, "Dominik Hasek"),
    (1997, "Dominik Hasek"), (1996, "Mario Lemieux"), (1995, "Eric Lindros"),
    (1994, "Sergei Fedorov"), (1993, "Mario Lemieux"), (1992, "Mark Messier"),
    (1991, "Brett Hull"), (1990, "Mark Messier"), (1989, "Wayne Gretzky"),
    (1988, "Mario Lemieux"), (1987, "Wayne Gretzky"), (1986, "Wayne Gretzky"),
    (1985, "Wayne Gretzky"), (1984, "Wayne Gretzky"), (1983, "Wayne Gretzky"),
    (1982, "Wayne Gretzky"), (1981, "Wayne Gretzky"), (1980, "Wayne Gretzky"),
    (1979, "Bryan Trottier"), (1978, "Guy Lafleur"), (1977, "Guy Lafleur"),
    (1976, "Bobby Clarke"), (1975, "Bobby Clarke"), (1974, "Phil Esposito"),
    (1973, "Bobby Clarke"), (1972, "Bobby Orr"), (1971, "Bobby Orr"),
    (1970, "Bobby Orr"), (1969, "Phil Esposito"), (1968, "Stan Mikita"),
    (1967, "Stan Mikita"), (1966, "Bobby Hull"), (1965, "Bobby Hull"),
    (1964, "Jean Beliveau"), (1963, "Gordie Howe"), (1962, "Jacques Plante"),
    (1961, "Bernie Geoffrion"), (1960, "Gordie Howe"), (1959, "Andy Bathgate"),
    (1958, "Gordie Howe"), (1957, "Gordie Howe"), (1956, "Jean Beliveau"),
    (1955, "Ted Kennedy"), (1954, "Al Rollins"), (1953, "Gordie Howe"),
    (1952, "Gordie Howe"), (1951, "Milt Schmidt"),
]

nhl_players = ["Nathan MacKinnon","Connor McDavid","Auston Matthews","Leon Draisaitl","Nikita Kucherov",
    "Taylor Hall","Patrick Kane","Carey Price","Ryan Getzlaf","Alex Ovechkin","Evgeni Malkin",
    "Corey Perry","Henrik Sedin","Sidney Crosby","Joe Thornton","Martin St. Louis","Peter Forsberg",
    "Joe Sakic","Chris Pronger","Jaromir Jagr","Dominik Hasek","Mario Lemieux","Eric Lindros",
    "Sergei Fedorov","Mark Messier","Brett Hull","Wayne Gretzky","Bryan Trottier","Guy Lafleur",
    "Bobby Clarke","Phil Esposito","Bobby Orr","Stan Mikita","Bobby Hull","Jean Beliveau",
    "Gordie Howe","Jacques Plante","Bernie Geoffrion","Andy Bathgate","Ted Kennedy",
    "Martin Brodeur","Patrick Roy","Mats Sundin","Steve Yzerman","Steve Stamkos","Niklas Backstrom",
    "Brendan Shanahan","Scott Stevens","Rob Blake","Nicklas Lidstrom","Henrik Lundqvist"]

for yr, player in nhl_hart:
    if "No award" in player:
        continue
    wrongs = [p for p in nhl_players if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the Hart Trophy (NHL MVP) for the {yr} season?",
        player,
        wrongs[:3],
        "hockey", "hard"
    ))

print(f"After NHL Hart Trophy: {len(questions)}")

# Art Ross Trophy (NHL scoring title)
nhl_art_ross = [
    (2024, "Nathan MacKinnon"), (2023, "Connor McDavid"), (2022, "Connor McDavid"),
    (2021, "Connor McDavid"), (2020, "Leon Draisaitl"), (2019, "Nikita Kucherov"),
    (2018, "Nikita Kucherov"), (2017, "Connor McDavid"), (2016, "Jamie Benn"),
    (2015, "John Tavares"), (2014, "Ryan Getzlaf"), (2013, "Martin St. Louis"),
    (2012, "Evgeni Malkin"), (2011, "Daniel Sedin"), (2010, "Henrik Sedin"),
    (2009, "Evgeni Malkin"), (2008, "Alexander Ovechkin"), (2007, "Sidney Crosby"),
    (2006, "Joe Thornton"), (2004, "Martin St. Louis"), (2003, "Peter Forsberg"),
    (2002, "Jarome Iginla"), (2001, "Jaromir Jagr"), (2000, "Jaromir Jagr"),
    (1999, "Jaromir Jagr"), (1998, "Jaromir Jagr"), (1997, "Mario Lemieux"),
    (1996, "Mario Lemieux"), (1995, "Jaromir Jagr"), (1994, "Wayne Gretzky"),
    (1993, "Mario Lemieux"), (1992, "Mario Lemieux"), (1991, "Wayne Gretzky"),
    (1990, "Wayne Gretzky"), (1989, "Mario Lemieux"), (1988, "Mario Lemieux"),
    (1987, "Wayne Gretzky"), (1986, "Wayne Gretzky"), (1985, "Wayne Gretzky"),
    (1984, "Wayne Gretzky"), (1983, "Wayne Gretzky"), (1982, "Wayne Gretzky"),
    (1981, "Wayne Gretzky"), (1980, "Marcel Dionne"), (1979, "Bryan Trottier"),
    (1978, "Guy Lafleur"), (1977, "Guy Lafleur"), (1976, "Guy Lafleur"),
    (1975, "Bobby Orr"), (1974, "Phil Esposito"), (1973, "Phil Esposito"),
    (1972, "Phil Esposito"), (1971, "Phil Esposito"), (1970, "Bobby Orr"),
    (1969, "Phil Esposito"), (1968, "Stan Mikita"), (1967, "Stan Mikita"),
    (1966, "Bobby Hull"), (1965, "Stan Mikita"), (1964, "Stan Mikita"),
]

for yr, player in nhl_art_ross:
    wrongs = [p for p in nhl_players + ["Marcel Dionne","Jarome Iginla","Daniel Sedin","John Tavares",
        "Jamie Benn","Ryan Getzlaf"] if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the Art Ross Trophy (NHL scoring title) for the {yr} season?",
        player,
        wrongs[:3],
        "hockey", "hard"
    ))

print(f"After Art Ross: {len(questions)}")

# Norris Trophy (best defenseman)
nhl_norris = [
    (2024, "Quinn Hughes"), (2023, "Erik Karlsson"), (2022, "Cale Makar"),
    (2021, "Adam Fox"), (2020, "Roman Josi"), (2019, "Mark Giordano"),
    (2018, "Victor Hedman"), (2017, "Brent Burns"), (2016, "Drew Doughty"),
    (2015, "Erik Karlsson"), (2014, "Duncan Keith"), (2013, "P.K. Subban"),
    (2012, "Erik Karlsson"), (2011, "Nicklas Lidstrom"), (2010, "Duncan Keith"),
    (2009, "Zdeno Chara"), (2008, "Nicklas Lidstrom"), (2007, "Nicklas Lidstrom"),
    (2006, "Nicklas Lidstrom"), (2004, "Scott Niedermayer"), (2003, "Nicklas Lidstrom"),
    (2002, "Nicklas Lidstrom"), (2001, "Nicklas Lidstrom"), (2000, "Chris Pronger"),
    (1999, "Al MacInnis"), (1998, "Rob Blake"), (1997, "Chris Chelios"),
    (1996, "Chris Chelios"), (1995, "Paul Coffey"), (1994, "Ray Bourque"),
    (1993, "Chris Chelios"), (1992, "Brian Leetch"), (1991, "Ray Bourque"),
    (1990, "Ray Bourque"), (1989, "Chris Chelios"), (1988, "Ray Bourque"),
    (1987, "Ray Bourque"), (1986, "Paul Coffey"), (1985, "Paul Coffey"),
    (1984, "Rod Langway"), (1983, "Rod Langway"), (1982, "Doug Wilson"),
    (1981, "Randy Carlyle"), (1980, "Larry Robinson"), (1979, "Denis Potvin"),
    (1978, "Denis Potvin"), (1977, "Larry Robinson"), (1976, "Denis Potvin"),
    (1975, "Bobby Orr"), (1974, "Bobby Orr"), (1973, "Bobby Orr"),
    (1972, "Bobby Orr"), (1971, "Bobby Orr"), (1970, "Bobby Orr"),
    (1969, "Bobby Orr"), (1968, "Bobby Orr"),
]

nhl_d_players = ["Quinn Hughes","Erik Karlsson","Cale Makar","Adam Fox","Roman Josi","Mark Giordano",
    "Victor Hedman","Brent Burns","Drew Doughty","Duncan Keith","P.K. Subban","Nicklas Lidstrom",
    "Zdeno Chara","Scott Niedermayer","Chris Pronger","Al MacInnis","Rob Blake","Chris Chelios",
    "Paul Coffey","Ray Bourque","Brian Leetch","Rod Langway","Denis Potvin","Larry Robinson",
    "Bobby Orr","Doug Harvey","Tim Horton","Brad Park","Scott Stevens","Eric Lindros",
    "Sergei Gonchar","Dion Phaneuf","Shea Weber","Cam Fowler"]

for yr, player in nhl_norris:
    wrongs = [p for p in nhl_d_players if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the Norris Trophy (best NHL defenseman) for the {yr} season?",
        player,
        wrongs[:3],
        "hockey", "hard"
    ))

print(f"After Norris: {len(questions)}")

# ============================================================
# TENNIS - WOMENS GRAND SLAMS
# ============================================================
wimbledon_womens = [
    (2023, "Marketa Vondrousova"), (2022, "Elena Rybakina"), (2021, "Ashleigh Barty"),
    (2019, "Simona Halep"), (2018, "Angelique Kerber"), (2017, "Garbine Muguruza"),
    (2016, "Serena Williams"), (2015, "Serena Williams"), (2014, "Petra Kvitova"),
    (2013, "Marion Bartoli"), (2012, "Serena Williams"), (2011, "Petra Kvitova"),
    (2010, "Serena Williams"), (2009, "Serena Williams"), (2008, "Venus Williams"),
    (2007, "Venus Williams"), (2006, "Amelie Mauresmo"), (2005, "Venus Williams"),
    (2004, "Maria Sharapova"), (2003, "Serena Williams"), (2002, "Serena Williams"),
    (2001, "Venus Williams"), (2000, "Venus Williams"), (1999, "Lindsay Davenport"),
    (1998, "Jana Novotna"), (1997, "Martina Hingis"), (1996, "Steffi Graf"),
    (1995, "Steffi Graf"), (1994, "Conchita Martinez"), (1993, "Steffi Graf"),
    (1992, "Steffi Graf"), (1991, "Steffi Graf"), (1990, "Martina Navratilova"),
    (1989, "Steffi Graf"), (1988, "Steffi Graf"), (1987, "Martina Navratilova"),
    (1986, "Martina Navratilova"), (1985, "Martina Navratilova"), (1984, "Martina Navratilova"),
    (1983, "Martina Navratilova"), (1982, "Martina Navratilova"), (1981, "Chris Evert"),
    (1980, "Evonne Goolagong"), (1979, "Martina Navratilova"), (1978, "Martina Navratilova"),
    (1977, "Virginia Ruzici"), (1976, "Chris Evert"), (1975, "Billie Jean King"),
    (1974, "Chris Evert"), (1973, "Billie Jean King"), (1972, "Billie Jean King"),
]

women_tennis = ["Marketa Vondrousova","Elena Rybakina","Ashleigh Barty","Simona Halep","Angelique Kerber",
    "Garbine Muguruza","Serena Williams","Petra Kvitova","Marion Bartoli","Venus Williams",
    "Amelie Mauresmo","Maria Sharapova","Lindsay Davenport","Jana Novotna","Martina Hingis",
    "Steffi Graf","Conchita Martinez","Martina Navratilova","Chris Evert","Billie Jean King",
    "Evonne Goolagong","Monica Seles","Gabriela Sabatini","Mary Pierce","Jennifer Capriati",
    "Kim Clijsters","Justine Henin","Victoria Azarenka","Caroline Wozniacki","Naomi Osaka",
    "Bianca Andreescu","Iga Swiatek","Coco Gauff","Elena Dementieva","Svetlana Kuznetsova"]

for yr, player in wimbledon_womens:
    wrongs = [p for p in women_tennis if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the Wimbledon women's singles title in {yr}?",
        player,
        wrongs[:3],
        "tennis", "hard"
    ))

# US Open womens
us_open_womens = [
    (2023, "Coco Gauff"), (2022, "Iga Swiatek"), (2021, "Emma Raducanu"),
    (2020, "Naomi Osaka"), (2019, "Bianca Andreescu"), (2018, "Naomi Osaka"),
    (2017, "Sloane Stephens"), (2016, "Angelique Kerber"), (2015, "Flavia Pennetta"),
    (2014, "Serena Williams"), (2013, "Serena Williams"), (2012, "Serena Williams"),
    (2011, "Samantha Stosur"), (2010, "Kim Clijsters"), (2009, "Kim Clijsters"),
    (2008, "Serena Williams"), (2007, "Justine Henin"), (2006, "Maria Sharapova"),
    (2005, "Kim Clijsters"), (2004, "Svetlana Kuznetsova"), (2003, "Justine Henin"),
    (2002, "Serena Williams"), (2001, "Venus Williams"), (2000, "Venus Williams"),
    (1999, "Serena Williams"), (1998, "Lindsay Davenport"), (1997, "Martina Hingis"),
    (1996, "Steffi Graf"), (1995, "Steffi Graf"), (1994, "Arantxa Sanchez Vicario"),
    (1993, "Steffi Graf"), (1992, "Monica Seles"), (1991, "Monica Seles"),
    (1990, "Gabriela Sabatini"), (1989, "Steffi Graf"), (1988, "Steffi Graf"),
    (1987, "Martina Navratilova"), (1986, "Martina Navratilova"), (1985, "Hana Mandlikova"),
    (1984, "Martina Navratilova"), (1983, "Martina Navratilova"), (1982, "Chris Evert"),
    (1981, "Tracy Austin"), (1980, "Chris Evert"), (1979, "Tracy Austin"),
    (1978, "Chris Evert"), (1977, "Chris Evert"), (1976, "Chris Evert"),
]

for yr, player in us_open_womens:
    wrongs = [p for p in women_tennis + ["Emma Raducanu","Sloane Stephens","Flavia Pennetta",
        "Samantha Stosur","Tracy Austin","Hana Mandlikova","Arantxa Sanchez Vicario",
        "Coco Gauff","Iga Swiatek","Bianca Andreescu"] if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the US Open women's singles title in {yr}?",
        player,
        wrongs[:3],
        "tennis", "hard"
    ))

# Australian Open mens
aus_open_mens = [
    (2024, "Jannik Sinner"), (2023, "Novak Djokovic"), (2022, "Rafael Nadal"),
    (2021, "Novak Djokovic"), (2020, "Novak Djokovic"), (2019, "Novak Djokovic"),
    (2018, "Roger Federer"), (2017, "Roger Federer"), (2016, "Novak Djokovic"),
    (2015, "Novak Djokovic"), (2014, "Stan Wawrinka"), (2013, "Novak Djokovic"),
    (2012, "Novak Djokovic"), (2011, "Novak Djokovic"), (2010, "Roger Federer"),
    (2009, "Rafael Nadal"), (2008, "Novak Djokovic"), (2007, "Roger Federer"),
    (2006, "Roger Federer"), (2005, "Marat Safin"), (2004, "Roger Federer"),
    (2003, "Andre Agassi"), (2002, "Thomas Johansson"), (2001, "Andre Agassi"),
    (2000, "Andre Agassi"), (1999, "Yevgeny Kafelnikov"), (1998, "Petr Korda"),
    (1997, "Pete Sampras"), (1996, "Boris Becker"), (1995, "Andre Agassi"),
    (1994, "Pete Sampras"), (1993, "Jim Courier"), (1992, "Jim Courier"),
    (1991, "Boris Becker"), (1990, "Ivan Lendl"), (1989, "Ivan Lendl"),
    (1988, "Mats Wilander"), (1987, "Stefan Edberg"), (1986, "Not held"),
    (1985, "Stefan Edberg"), (1984, "Mats Wilander"), (1983, "Mats Wilander"),
    (1982, "Johan Kriek"), (1981, "Johan Kriek"), (1980, "Brian Teacher"),
]

for yr, player in aus_open_mens:
    if "Not held" in player:
        continue
    wrongs = [p for p in tennis_players + ["Jannik Sinner","Stan Wawrinka","Marat Safin",
        "Yevgeny Kafelnikov","Petr Korda","Thomas Johansson","Johan Kriek","Brian Teacher"] if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the Australian Open men's singles title in {yr}?",
        player,
        wrongs[:3],
        "tennis", "hard"
    ))

print(f"After tennis womens/Aus Open: {len(questions)}")

# ============================================================
# GOLF - Major Championships (US Open, The Open Championship, PGA)
# ============================================================
us_open_golf = [
    (2024, "Bryson DeChambeau"), (2023, "Wyndham Clark"), (2022, "Matt Fitzpatrick"),
    (2021, "Jon Rahm"), (2020, "Bryson DeChambeau"), (2019, "Gary Woodland"),
    (2018, "Brooks Koepka"), (2017, "Brooks Koepka"), (2016, "Dustin Johnson"),
    (2015, "Jordan Spieth"), (2014, "Martin Kaymer"), (2013, "Justin Rose"),
    (2012, "Webb Simpson"), (2011, "Rory McIlroy"), (2010, "Graeme McDowell"),
    (2009, "Lucas Glover"), (2008, "Tiger Woods"), (2007, "Angel Cabrera"),
    (2006, "Geoff Ogilvy"), (2005, "Michael Campbell"), (2004, "Retief Goosen"),
    (2003, "Jim Furyk"), (2002, "Tiger Woods"), (2001, "Retief Goosen"),
    (2000, "Tiger Woods"), (1999, "Payne Stewart"), (1998, "Lee Janzen"),
    (1997, "Ernie Els"), (1996, "Steve Jones"), (1995, "Corey Pavin"),
    (1994, "Ernie Els"), (1993, "Lee Janzen"), (1992, "Tom Kite"),
    (1991, "Payne Stewart"), (1990, "Hale Irwin"), (1989, "Curtis Strange"),
    (1988, "Curtis Strange"), (1987, "Scott Simpson"), (1986, "Ray Floyd"),
    (1985, "Andy North"), (1984, "Fuzzy Zoeller"), (1983, "Larry Nelson"),
    (1982, "Tom Watson"), (1981, "David Graham"), (1980, "Jack Nicklaus"),
    (1979, "Hale Irwin"), (1978, "Andy North"), (1977, "Hubert Green"),
    (1976, "Jerry Pate"), (1975, "Lou Graham"), (1974, "Hale Irwin"),
    (1973, "Johnny Miller"), (1972, "Jack Nicklaus"), (1971, "Lee Trevino"),
    (1970, "Tony Jacklin"), (1969, "Orville Moody"), (1968, "Lee Trevino"),
    (1967, "Jack Nicklaus"), (1966, "Billy Casper"), (1965, "Gary Player"),
    (1964, "Ken Venturi"), (1963, "Julius Boros"), (1962, "Jack Nicklaus"),
    (1961, "Gene Littler"), (1960, "Arnold Palmer"), (1959, "Billy Casper"),
    (1958, "Tommy Bolt"),
]

for yr, player in us_open_golf:
    wrongs = [p for p in golf_players + ["Bryson DeChambeau","Wyndham Clark","Matt Fitzpatrick",
        "Gary Woodland","Brooks Koepka","Martin Kaymer","Justin Rose","Webb Simpson","Rory McIlroy",
        "Graeme McDowell","Lucas Glover","Geoff Ogilvy","Michael Campbell","Jim Furyk","Payne Stewart",
        "Lee Janzen","Steve Jones","Corey Pavin","Tom Kite","Hale Irwin","Curtis Strange",
        "Scott Simpson","Larry Nelson","Tom Watson","Johnny Miller","Lee Trevino","Tony Jacklin",
        "Ken Venturi","Gene Littler","Tommy Bolt","Ernie Els","Retief Goosen","Jim Furyk"] if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the US Open golf championship in {yr}?",
        player,
        wrongs[:3],
        "golf", "hard"
    ))

print(f"After US Open golf: {len(questions)}")

# The Open Championship (British Open)
the_open = [
    (2024, "Xander Schauffele"), (2023, "Brian Harman"), (2022, "Cameron Smith"),
    (2021, "Collin Morikawa"), (2020, "No event"), (2019, "Shane Lowry"),
    (2018, "Francesco Molinari"), (2017, "Jordan Spieth"), (2016, "Henrik Stenson"),
    (2015, "Zach Johnson"), (2014, "Rory McIlroy"), (2013, "Phil Mickelson"),
    (2012, "Ernie Els"), (2011, "Darren Clarke"), (2010, "Louis Oosthuizen"),
    (2009, "Stewart Cink"), (2008, "Padraig Harrington"), (2007, "Padraig Harrington"),
    (2006, "Tiger Woods"), (2005, "Tiger Woods"), (2004, "Todd Hamilton"),
    (2003, "Ben Curtis"), (2002, "Ernie Els"), (2001, "David Duval"),
    (2000, "Tiger Woods"), (1999, "Paul Lawrie"), (1998, "Mark O'Meara"),
    (1997, "Justin Leonard"), (1996, "Tom Lehman"), (1995, "John Daly"),
    (1994, "Nick Price"), (1993, "Greg Norman"), (1992, "Nick Faldo"),
    (1991, "Ian Baker-Finch"), (1990, "Nick Faldo"), (1989, "Mark Calcavecchia"),
    (1988, "Seve Ballesteros"), (1987, "Nick Faldo"), (1986, "Greg Norman"),
    (1985, "Sandy Lyle"), (1984, "Seve Ballesteros"), (1983, "Tom Watson"),
    (1982, "Tom Watson"), (1981, "Bill Rogers"), (1980, "Tom Watson"),
    (1979, "Seve Ballesteros"), (1978, "Jack Nicklaus"), (1977, "Tom Watson"),
    (1976, "Johnny Miller"), (1975, "Tom Watson"), (1974, "Gary Player"),
    (1973, "Tom Weiskopf"), (1972, "Lee Trevino"), (1971, "Lee Trevino"),
    (1970, "Jack Nicklaus"), (1969, "Tony Jacklin"), (1968, "Gary Player"),
    (1967, "Roberto De Vicenzo"), (1966, "Jack Nicklaus"), (1965, "Peter Thomson"),
    (1964, "Tony Lema"), (1963, "Bob Charles"), (1962, "Arnold Palmer"),
    (1961, "Arnold Palmer"), (1960, "Kel Nagle"),
]

for yr, player in the_open:
    if "No event" in player:
        continue
    wrongs = [p for p in golf_players + ["Xander Schauffele","Brian Harman","Cameron Smith",
        "Collin Morikawa","Shane Lowry","Francesco Molinari","Henrik Stenson","Zach Johnson",
        "Rory McIlroy","Darren Clarke","Louis Oosthuizen","Stewart Cink","Padraig Harrington",
        "Todd Hamilton","Ben Curtis","David Duval","Paul Lawrie","Justin Leonard","Tom Lehman",
        "John Daly","Nick Price","Greg Norman","Ian Baker-Finch","Mark Calcavecchia","Peter Thomson",
        "Sandy Lyle","Ian Woosnam","Lee Janzen","Tom Weiskopf","Roberto De Vicenzo","Tony Lema",
        "Bob Charles","Kel Nagle"] if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won The Open Championship (British Open) in {yr}?",
        player,
        wrongs[:3],
        "golf", "hard"
    ))

print(f"After The Open: {len(questions)}")

# PGA Championship winners
pga_champ = [
    (2024, "Xander Schauffele"), (2023, "Brooks Koepka"), (2022, "Justin Thomas"),
    (2021, "Phil Mickelson"), (2020, "Collin Morikawa"), (2019, "Brooks Koepka"),
    (2018, "Brooks Koepka"), (2017, "Justin Thomas"), (2016, "Jimmy Walker"),
    (2015, "Jason Day"), (2014, "Rory McIlroy"), (2013, "Jason Dufner"),
    (2012, "Rory McIlroy"), (2011, "Keegan Bradley"), (2010, "Martin Kaymer"),
    (2009, "Yang Yong-eun"), (2008, "Padraig Harrington"), (2007, "Tiger Woods"),
    (2006, "Tiger Woods"), (2005, "Phil Mickelson"), (2004, "Vijay Singh"),
    (2003, "Shaun Micheel"), (2002, "Rich Beem"), (2001, "David Toms"),
    (2000, "Tiger Woods"), (1999, "Tiger Woods"), (1998, "Vijay Singh"),
    (1997, "Davis Love III"), (1996, "Mark Brooks"), (1995, "Steve Elkington"),
    (1994, "Nick Price"), (1993, "Paul Azinger"), (1992, "Nick Price"),
    (1991, "John Daly"), (1990, "Wayne Grady"), (1989, "Payne Stewart"),
    (1988, "Jeff Sluman"), (1987, "Larry Nelson"), (1986, "Bob Tway"),
    (1985, "Hubert Green"), (1984, "Lee Trevino"), (1983, "Hal Sutton"),
    (1982, "Raymond Floyd"), (1981, "Larry Nelson"), (1980, "Jack Nicklaus"),
    (1979, "David Graham"), (1978, "John Mahaffey"), (1977, "Lanny Wadkins"),
    (1976, "Dave Stockton"), (1975, "Jack Nicklaus"), (1974, "Lee Trevino"),
    (1973, "Jack Nicklaus"), (1972, "Gary Player"), (1971, "Jack Nicklaus"),
    (1970, "Dave Stockton"), (1969, "Raymond Floyd"), (1968, "Julius Boros"),
    (1967, "Don January"), (1966, "Al Geiberger"), (1965, "Dave Marr"),
    (1964, "Bobby Nichols"), (1963, "Jack Nicklaus"), (1962, "Gary Player"),
]

for yr, player in pga_champ:
    wrongs = [p for p in golf_players + ["Xander Schauffele","Brooks Koepka","Justin Thomas",
        "Collin Morikawa","Jimmy Walker","Jason Day","Jason Dufner","Keegan Bradley",
        "Martin Kaymer","Yang Yong-eun","Padraig Harrington","Vijay Singh","Shaun Micheel",
        "Rich Beem","David Toms","Davis Love III","Mark Brooks","Steve Elkington","Paul Azinger",
        "John Daly","Wayne Grady","Jeff Sluman","Bob Tway","Hal Sutton","Raymond Floyd",
        "John Mahaffey","Lanny Wadkins","Dave Stockton","Julius Boros","Bobby Nichols",
        "Dave Marr","Al Geiberger","Don January"] if p != player]
    random.shuffle(wrongs)
    questions.append(q(
        f"Who won the PGA Championship in {yr}?",
        player,
        wrongs[:3],
        "golf", "hard"
    ))

print(f"After PGA Championship: {len(questions)}")

# ============================================================
# ADDITIONAL STATIC QUESTIONS BY SPORT
# ============================================================

# Extra basketball facts
extra_basketball = [
    ("Which team plays home games at Crypto.com Arena?", "Los Angeles Lakers/Clippers", ["Sacramento Kings","Phoenix Suns","Utah Jazz"], "easy"),
    ("Which player was drafted by the Toronto Raptors in 2013 but was traded before playing?", "Giannis Antetokounmpo's trade had nothing to do with Toronto", ["Anthony Bennett","Andrew Wiggins","Andrew Nicholson"], "hard"),
    ("The 1986 Boston Celtics finished the regular season with what record?", "67-15", ["64-18","70-12","65-17"], "hard"),
    ("Which player was the first to win both the NBA title and the EuroBasket championship in the same year?", "Tony Parker (2007)", ["Dirk Nowitzki","Manu Ginobili","Andrei Kirilenko"], "hard"),
    ("Who holds the record for most points scored in an NBA All-Star Game?", "Anthony Davis (52 in 2017)", ["Michael Jordan","Wilt Chamberlain","Bob Pettit"], "hard"),
    ("The Houston Rockets' back-to-back championship teams were led by which two Hall of Famers?", "Hakeem Olajuwon and Clyde Drexler", ["Karl Malone and John Stockton","Shaquille O'Neal and Kobe Bryant","Tim Duncan and Tony Parker"], "medium"),
    ("What year did the Dallas Mavericks win their first and only NBA Championship?", "2011", ["2006","2014","2019"], "medium"),
    ("Pau Gasol is from which country?", "Spain", ["Argentina","Italy","Serbia"], "easy"),
    ("Which player was the first to win back-to-back All-Star Game MVPs?", "Bob Pettit (1958 and 1959)", ["Oscar Robertson","Elgin Baylor","Wilt Chamberlain"], "hard"),
    ("The 'Spurs system' under Gregg Popovich is based on which philosophy?", "Team-first, unselfish basketball with the pass as the primary weapon", ["Fast-break basketball","Heavy isolation plays","Zone defense"], "medium"),
    ("Which team won the first-ever NBA title in 1947?", "Philadelphia Warriors", ["Chicago Stags","Boston Celtics","New York Knicks"], "hard"),
    ("The Boston Celtics won how many championships in the 1960s?", "9", ["8","7","10"], "hard"),
    ("Wilt Chamberlain and Bill Russell faced each other in how many Finals?", "2", ["3","4","1"], "hard"),
    ("Which coach developed the triangle offense used by the Chicago Bulls and Lakers?", "Tex Winter", ["Phil Jackson","Doug Collins","Pete Newell"], "hard"),
    ("Larry Bird won how many regular-season MVP awards?", "3", ["2","4","1"], "medium"),
    ("What is the name of the shot clock violation in basketball?", "Shot clock violation or 24-second violation", ["Carry","Travel","Back court violation"], "easy"),
    ("The San Antonio Spurs drafted Tony Parker with what pick in 2001?", "28th overall", ["13th","5th","20th"], "hard"),
    ("Which player holds the single-game record for assists in NBA history?", "Scott Skiles (30 in 1990)", ["John Stockton","Magic Johnson","Isiah Thomas"], "hard"),
    ("Kawhi Leonard won Finals MVP with which team in 2019?", "Toronto Raptors", ["San Antonio Spurs","Los Angeles Clippers","Boston Celtics"], "medium"),
    ("The first NBA player to score 70 points in a game was who?", "Wilt Chamberlain (100 points)", ["David Thompson (73)","Michael Jordan","Pete Maravich"], "hard"),
]

for text, ans, wrongs, diff in extra_basketball:
    questions.append(q(text, ans, wrongs, "basketball", diff))

# Extra football
extra_football = [
    ("Who is the only player to be selected to the Pro Bowl at five different positions?", "Bo Jackson", ["Deion Sanders","Bullet Bill Dudley","Chuck Bednarik"], "hard"),
    ("Which franchise holds the record for most consecutive losses?", "Tampa Bay Buccaneers (26 games in 1976-1977)", ["Cleveland Browns","Detroit Lions","Oakland Raiders"], "hard"),
    ("Who won the Heisman Trophy in 2023?", "Jayden Daniels", ["Marvin Harrison Jr.","Drake Maye","Caleb Williams"], "medium"),
    ("Patrick Mahomes went to which college?", "Texas Tech", ["Kansas State","Oklahoma","Kansas"], "medium"),
    ("The Detroit Lions last won the NFL title in what year?", "1957", ["1952","1964","1953"], "hard"),
    ("Who was the first player to rush for 1,000 yards in consecutive AFL seasons?", "Clem Daniels", ["Paul Lowe","Jim Nance","Cookie Gilchrist"], "hard"),
    ("Joe Montana never threw an interception in which Super Bowl?", "Super Bowl XIX (1985 vs Dolphins)", ["Super Bowl XVI","Super Bowl XXIII","Super Bowl XXIV"], "hard"),
    ("Which player was known as 'White Shoes' and played for the Houston Oilers?", "Billy 'White Shoes' Johnson", ["Earl Campbell","Dan Pastorini","Kenny Burrough"], "hard"),
    ("The XFL was originally founded by which media mogul?", "Vince McMahon", ["Rupert Murdoch","Ted Turner","George Steinbrenner"], "medium"),
    ("Roger Staubach won the Heisman Trophy playing for which college?", "Navy", ["Army","Texas","Oklahoma"], "medium"),
    ("Which team moved from Oakland to Las Vegas for the 2020 season?", "Las Vegas Raiders", ["Los Angeles Chargers","Arizona Cardinals","San Diego Chargers"], "easy"),
    ("The NFL salary cap was introduced in what year?", "1994", ["1990","1998","1987"], "medium"),
    ("Which Hall of Fame coach was known for his defense in the 'Fearsome Foursome'?", "George Allen (Los Angeles Rams/Redskins)", ["Chuck Knox","Sid Gillman","Bud Grant"], "hard"),
    ("Who is the only quarterback to win the Super Bowl with multiple different teams?", "No QB has won with multiple different teams", ["Tom Brady (one team each time)","Peyton Manning","Roger Staubach"], "hard"),
    ("The Cleveland Browns have never appeared in a Super Bowl. True or False?", "True", ["False","They appeared in Super Bowl I","They appeared in Super Bowl V"], "medium"),
    ("Which running back was known as 'The Galloping Ghost'?", "Red Grange", ["Bronko Nagurski","Jim Brown","Ernie Nevers"], "hard"),
    ("The NFL Players Association was formed in which decade?", "1950s (1956)", ["1940s","1960s","1970s"], "hard"),
    ("Who caught the 'Immaculate Reception' for Pittsburgh in 1972?", "Franco Harris", ["Lynn Swann","John Stallworth","Rocky Bleier"], "medium"),
    ("Marcus Allen's record-breaking run in Super Bowl XVIII was what length?", "74 yards", ["54 yards","43 yards","82 yards"], "hard"),
    ("Bo Jackson was a two-sport star in football and which other sport?", "Baseball", ["Basketball","Track","Hockey"], "easy"),
]

for text, ans, wrongs, diff in extra_football:
    questions.append(q(text, ans, wrongs, "football", diff))

# Extra baseball
extra_baseball = [
    ("Sandy Koufax's peak was during which decade?", "1960s", ["1950s","1970s","1980s"], "easy"),
    ("The 'Big Red Machine' of the 1970s referred to which team?", "Cincinnati Reds", ["St. Louis Cardinals","Oakland Athletics","Pittsburgh Pirates"], "medium"),
    ("Tony Gwynn hit .394 in the strike-shortened 1994 season. Which team did he play for?", "San Diego Padres", ["Los Angeles Dodgers","San Francisco Giants","Colorado Rockies"], "medium"),
    ("Derek Jeter won how many World Series rings?", "5", ["4","6","3"], "medium"),
    ("Which pitcher famously hit 7 home runs in his career, more than any pitcher since Ruth?", "Don Drysdale", ["Bob Gibson","Bob Lemon","Wes Ferrell"], "hard"),
    ("The Montreal Expos never won a World Series. In what year were they founded?", "1969", ["1966","1972","1975"], "medium"),
    ("Randy Johnson famously struck out a bird with a fastball in spring training. What year?", "2001", ["1999","2003","1998"], "hard"),
    ("Which player holds the record for hitting home runs in the most consecutive games (8)?", "Dale Long (1956) and Don Mattingly (1987) and Ken Griffey Jr. (1993)", ["Barry Bonds","Mark McGwire","Hank Aaron"], "hard"),
    ("Which team has appeared in the most World Series?", "New York Yankees (40+ times)", ["New York Giants","Boston Red Sox","St. Louis Cardinals"], "medium"),
    ("The 'Curse of the Billy Goat' was associated with which team?", "Chicago Cubs", ["Boston Red Sox","Cleveland Indians","Chicago White Sox"], "medium"),
    ("Reggie Jackson hit how many career home runs?", "563", ["527","584","510"], "hard"),
    ("Which pitcher set the record for most games pitched in a career?", "Jesse Orosco (1,252 games)", ["Kent Tekulve","Hoyt Wilhelm","Mike Stanton"], "hard"),
    ("The Tampa Bay Rays changed their name from 'Devil Rays' in what year?", "2008", ["2010","2005","2012"], "medium"),
    ("Who was the last pitcher to win 30 games in a season?", "Denny McLain (31 in 1968)", ["Sandy Koufax","Bob Gibson","Whitey Ford"], "hard"),
    ("How many innings must be completed for an official MLB game?", "5 (for a 9-inning game)", ["4","7","6"], "medium"),
    ("The '27 Yankees are considered the greatest team ever. How many of their players went to the Hall of Fame?", "7 to 12 (depending on criteria)", ["3","2","1"], "hard"),
    ("Willie McCovey played for which team during his Hall of Fame career?", "San Francisco Giants", ["Los Angeles Dodgers","Pittsburgh Pirates","San Diego Padres"], "medium"),
    ("The New York Yankees won the pennant how many times in a row from 1949 to 1953?", "5 consecutive pennants", ["4","3","6"], "hard"),
    ("Which player was involved in the controversial 'Steve Bartman incident' in 2003?", "Moises Alou would have caught the ball", ["Sammy Sosa","Kerry Wood","Aramis Ramirez"], "hard"),
    ("Johnny Bench is considered the greatest catcher ever. He played his whole career with?", "Cincinnati Reds", ["Pittsburgh Pirates","New York Yankees","Houston Astros"], "medium"),
]

for text, ans, wrongs, diff in extra_baseball:
    questions.append(q(text, ans, wrongs, "baseball", diff))

# Extra hockey
extra_hockey = [
    ("Which player holds the record for most goals in a single NHL season by a forward?", "Wayne Gretzky (92)", ["Mario Lemieux","Brett Hull","Jari Kurri"], "hard"),
    ("What position did Wayne Gretzky primarily play?", "Center", ["Right wing","Left wing","Defenseman"], "easy"),
    ("Which team's mascot is a penguin?", "Pittsburgh Penguins", ["Columbus Blue Jackets","Anaheim Ducks","San Jose Sharks"], "easy"),
    ("The 'Battle of Alberta' refers to matchups between which two teams?", "Edmonton Oilers and Calgary Flames", ["Edmonton Oilers and Vancouver Canucks","Calgary Flames and Vancouver Canucks","Edmonton and Winnipeg"], "medium"),
    ("Who was the 'Finnish Flash' who played for the Jets and Ducks?", "Teemu Selanne", ["Jari Kurri","Esa Tikkanen","Timo Jutila"], "medium"),
    ("Brett Hull is the son of which Hall of Fame player?", "Bobby Hull", ["Dennis Hull","Red Kelly","Phil Esposito"], "medium"),
    ("The Buffalo Sabres have never won the Stanley Cup. True or False?", "True", ["False","They won in 1975","They won in 1980"], "easy"),
    ("Which player was nicknamed 'The Russian Rocket' for the Vancouver Canucks?", "Pavel Bure", ["Evgeni Malkin","Ilya Kovalchuk","Alexei Zhamnov"], "medium"),
    ("Conn Smythe, after whom the playoff MVP trophy is named, built which arena?", "Maple Leaf Gardens (Toronto)", ["Montreal Forum","Boston Garden","Chicago Stadium"], "hard"),
    ("Which coach behind the bench holds the record for most playoff wins?","Scotty Bowman (223)", ["Al Arbour","Joel Quenneville","Mike Babcock"], "hard"),
    ("In the NHL, how long is a major penalty?", "5 minutes", ["2 minutes","10 minutes","3 minutes"], "easy"),
    ("Which team drafted Mario Lemieux first overall in 1984?", "Pittsburgh Penguins", ["Montreal Canadiens","Buffalo Sabres","New York Rangers"], "medium"),
    ("The Colorado Avalanche won their first Stanley Cup in their first season after relocating from Quebec in what year?", "1996", ["1998","1995","2000"], "medium"),
    ("Who scored the most famous overtime goal in Stanley Cup history for the Toronto Maple Leafs in 1951?", "Bill Barilko", ["Max Bentley","Syl Apps","Teeder Kennedy"], "hard"),
    ("Which European country won Olympic gold at the 2006 Torino Olympics in hockey?", "Sweden", ["Russia","Czech Republic","Finland"], "hard"),
    ("Patrick Roy's nickname was?", "Saint Patrick", ["Rocky","The Wall","The Net King"], "medium"),
    ("Which NHL team plays in the same arena as an NBA team in Boston?", "Boston Bruins (TD Garden, also home to Celtics)", ["New York Rangers","Chicago Blackhawks","Washington Capitals"], "easy"),
    ("The modern NHL uses video review for controversial goals. When was this introduced?", "1991", ["1995","1999","1985"], "hard"),
    ("How many teams are in the NHL as of 2024?", "32", ["30","28","31"], "easy"),
    ("Which player scored 76 career overtime goals, the most in NHL history?", "Jaromir Jagr", ["Wayne Gretzky","Mario Lemieux","Brendan Shanahan"], "hard"),
]

for text, ans, wrongs, diff in extra_hockey:
    questions.append(q(text, ans, wrongs, "hockey", diff))

# Extra soccer
extra_soccer = [
    ("Pele won his first World Cup at what age?", "17", ["19","21","16"], "medium"),
    ("Which country invented modern association football?", "England", ["Scotland","Brazil","Italy"], "easy"),
    ("David Beckham is most famous for playing for which two clubs?", "Manchester United and Real Madrid", ["Chelsea and Barcelona","Arsenal and Juventus","Liverpool and Bayern Munich"], "easy"),
    ("The offside rule in soccer requires how many defenders between an attacker and goal?", "2 (including goalkeeper)", ["1","3","The goalkeeper only"], "medium"),
    ("Messi won how many Copa America titles with Argentina?", "1", ["0","2","3"], "medium"),
    ("Which club has won the most La Liga titles?", "Real Madrid", ["Barcelona","Atletico Madrid","Valencia"], "medium"),
    ("The first soccer World Cup was held in which continent?", "South America", ["Europe","North America","Africa"], "medium"),
    ("Who was the top scorer at the 2022 World Cup?", "Kylian Mbappe (8 goals)", ["Lionel Messi","Olivier Giroud","Julian Alvarez"], "medium"),
    ("Which country has the most FIFA World Cup titles?", "Brazil (5)", ["Germany (4)","Italy (4)","Argentina (3)"], "easy"),
    ("The Champions League replaced which competition in 1992?", "European Cup", ["UEFA Cup","Cup Winners Cup","Intercontinental Cup"], "medium"),
    ("In soccer, how many substitutions are typically allowed per game in FIFA competitions?", "5", ["3","4","6"], "medium"),
    ("Ronaldo (Brazilian) scored how many goals in World Cup tournaments?", "15", ["12","17","10"], "hard"),
    ("Which team won the first UEFA Champions League in 1956?", "Real Madrid", ["Barcelona","AC Milan","Benfica"], "hard"),
    ("The English Premier League was founded in which year?", "1992", ["1985","1990","1995"], "medium"),
    ("Which South American country won the 2021 Copa America?", "Argentina", ["Brazil","Colombia","Uruguay"], "medium"),
    ("Eusebio 'The Black Panther' played for which Portuguese club?", "Benfica", ["Porto","Sporting CP","Braga"], "hard"),
    ("Who is the all-time leading scorer in Premier League history?", "Alan Shearer", ["Andrew Cole","Frank Lampard","Wayne Rooney"], "medium"),
    ("The 'Maracanazo' refers to Uruguay's World Cup win over Brazil in which year?", "1950", ["1958","1962","1954"], "hard"),
    ("Which player had their World Cup final goal controversially disallowed in 2010?", "Carlos Tevez (no, Frank Lampard's goal was disallowed)", ["Frank Lampard","Carlos Tevez","Miroslav Klose"], "hard"),
    ("Andrés Iniesta scored the winning goal in the 2010 World Cup Final. For which country?", "Spain", ["Germany","Netherlands","France"], "medium"),
]

for text, ans, wrongs, diff in extra_soccer:
    questions.append(q(text, ans, wrongs, "soccer", diff))

# Extra f1
extra_f1 = [
    ("The Formula 1 World Championship was first held in what year?", "1950", ["1945","1955","1948"], "easy"),
    ("Ferrari is based in which Italian city?", "Maranello", ["Turin","Milan","Rome"], "easy"),
    ("Which safety device was introduced to F1 cockpits in 2018?", "The Halo", ["HANS device","Roll hoop","Side pods"], "medium"),
    ("Which F1 driver died at the same 1994 San Marino Grand Prix as Ayrton Senna?", "Roland Ratzenberger", ["Michele Alboreto","Erik Comas","Martin Donnelly"], "hard"),
    ("The Baku circuit hosts the Grand Prix of which country?", "Azerbaijan", ["Georgia","Kazakhstan","Armenia"], "medium"),
    ("Lewis Hamilton drives car number?", "44", ["3","77","11"], "easy"),
    ("Which team did Michael Schumacher join after leaving Ferrari?", "Mercedes", ["Red Bull","BMW","Renault"], "medium"),
    ("The Circuit de la Sarthe is famous for which endurance race (not F1)?", "24 Hours of Le Mans", ["Daytona 500","Indianapolis 500","Nurburgring 24h"], "medium"),
    ("Red Bull Racing is based in which country?", "United Kingdom (Milton Keynes)", ["Austria","USA","Italy"], "medium"),
    ("Which driver holds the record for fastest ever F1 lap at a Grand Prix?", "Varies by circuit - Verstappen holds many", ["Michael Schumacher","Lewis Hamilton","Nico Rosberg"], "hard"),
    ("The 1988 McLaren-Honda team won how many races out of 16?", "15", ["14","16","13"], "hard"),
    ("The iconic turquoise color of the Lotus F1 cars in the 1960s was sponsored by which company?", "Imperial Tobacco (Gold Leaf)", ["Elf","Castrol","BP"], "hard"),
    ("Ayrton Senna's nationality was?", "Brazilian", ["Portuguese","Argentine","Italian"], "easy"),
    ("Max Verstappen drove for which team before Red Bull Racing in F1?", "Toro Rosso (now AlphaTauri)", ["Force India","Haas","Williams"], "medium"),
    ("The Indianapolis 500 was part of the Formula 1 World Championship from what year to what year?", "1950 to 1960", ["1948 to 1955","1965 to 1975","1950 to 1965"], "hard"),
    ("The Verstappen family's first F1 driver was not Max, but which parent?", "Jos Verstappen (his father)", ["Sophie Kumpen (his mother)","Max himself","His older brother"], "medium"),
    ("Which team dominated F1 with their 'double diffuser' advantage in 2009?", "Brawn GP (later became Mercedes)", ["Red Bull","McLaren","Toyota"], "hard"),
    ("Carlos Sainz Jr. is the son of which famous rally driver?", "Carlos Sainz Sr.", ["Walter Rohrl","Sebastien Loeb","Juha Kankkunen"], "medium"),
    ("The Autodromo Nazionale Monza was built in which year?", "1922", ["1930","1948","1955"], "hard"),
    ("Which F1 driver is known as 'Iceman' for his cool demeanor?", "Kimi Raikkonen", ["Nico Rosberg","Valtteri Bottas","Sebastian Vettel"], "easy"),
]

for text, ans, wrongs, diff in extra_f1:
    questions.append(q(text, ans, wrongs, "f1", diff))

# Extra tennis
extra_tennis = [
    ("Arthur Ashe won Wimbledon in 1975 against which player?", "Jimmy Connors", ["Bjorn Borg","Ilie Nastase","Manuel Orantes"], "hard"),
    ("Billie Jean King famously beat Bobby Riggs in the 'Battle of the Sexes' in what year?", "1973", ["1975","1970","1971"], "medium"),
    ("Which tennis player was known as 'The Crocodile'?", "Rene Lacoste", ["Jean Borotra","Henri Cochet","Jacques Brugnon"], "hard"),
    ("Andy Murray has won Wimbledon how many times?", "2", ["1","3","4"], "medium"),
    ("Which surface is the Australian Open played on?", "Hard (Plexicushion)", ["Clay","Grass","Carpet"], "easy"),
    ("The Davis Cup is a team competition in which sport?", "Tennis", ["Badminton","Squash","Table Tennis"], "easy"),
    ("Monica Seles was stabbed during a match in 1993 by a fan of which player?", "Steffi Graf", ["Martina Navratilova","Jennifer Capriati","Gabriela Sabatini"], "hard"),
    ("Lleyton Hewitt won Wimbledon in which year?", "2002", ["2001","2000","2003"], "medium"),
    ("John McEnroe famously feuded with which tennis official at Wimbledon 1981?", "Edward James (chair umpire)", ["Alan Mills","Fred Hoyles","Ted Tinling"], "hard"),
    ("Rod Laver is the only player to win the calendar Grand Slam twice. In what years?", "1962 and 1969", ["1960 and 1966","1965 and 1971","1961 and 1969"], "hard"),
    ("The WTA (Women's Tennis Association) was founded in which year?", "1973", ["1968","1980","1975"], "medium"),
    ("Pete Sampras won how many Grand Slam titles?", "14", ["12","16","13"], "medium"),
    ("Who was the first player to complete the 'Sunshine Double' (Indian Wells and Miami in the same year)?", "Steffi Graf (1994)", ["Martina Navratilova","Chris Evert","Monica Seles"], "hard"),
    ("Novak Djokovic holds the record for most weeks at world number one. How many?", "400+ weeks", ["200 weeks","300 weeks","150 weeks"], "medium"),
    ("Which tennis player made the 'Super Slam' by winning all four Grands Slams and the Olympics in the same year?", "No player has achieved this in open era", ["Steffi Graf won Olympic gold AND calendar Grand Slam in 1988","Rod Laver","Roger Federer"], "hard"),
    ("Iga Swiatek is from which country?", "Poland", ["Czech Republic","Slovakia","Hungary"], "easy"),
    ("Who was the first unseeded player to win Wimbledon?", "Boris Becker (1985, aged 17)", ["Goran Ivanisevic","Pat Cash","Michael Chang"], "hard"),
    ("Kim Clijsters won how many Grand Slam titles?", "4", ["3","5","2"], "medium"),
    ("The Australian Open moved to its current Melbourne Park location in which year?", "1988", ["1985","1992","1980"], "hard"),
    ("Jimmy Connors won how many Grand Slam singles titles?", "8", ["6","10","5"], "medium"),
]

for text, ans, wrongs, diff in extra_tennis:
    questions.append(q(text, ans, wrongs, "tennis", diff))

# Extra golf
extra_golf = [
    ("Who was the first player to win the 'Tiger Slam' (4 consecutive Majors)?", "Tiger Woods (2000-2001)", ["Jack Nicklaus","Ben Hogan","Bobby Jones"], "medium"),
    ("The Ryder Cup is played every how many years?", "2", ["4","3","1"], "easy"),
    ("Arnold Palmer's four Majors were all won in what decade?", "1960s (and late 1950s - 1958-1964)", ["1950s","1970s","1960s"], "medium"),
    ("Phil Mickelson became the oldest Major champion in history by winning the 2021 PGA Championship at what age?", "50", ["47","52","48"], "medium"),
    ("Greg Norman was known as what nickname?", "The Great White Shark", ["The White Lion","The Australian Eagle","The Shark Hunter"], "easy"),
    ("Tiger Woods missed the 2017-2018 season primarily due to what injury?", "Back surgery (spinal fusion)", ["Knee injury","Shoulder surgery","Hip replacement"], "medium"),
    ("Who was the first player to break Jack Nicklaus's record of 18 major championships?", "No player has broken it (Tiger Woods has 15)", ["Tiger Woods is closest with 15","Rory McIlroy","Phil Mickelson"], "medium"),
    ("The term 'links' in golf refers to what type of course?", "Coastal courses built on linksland near the sea", ["Mountain courses","Parkland courses","Desert courses"], "medium"),
    ("Chi Chi Rodriguez was famous for his antics after a putt went in. He pretended his putter was?", "A sword (or matador's sword)", ["A gun","A magic wand","A baseball bat"], "hard"),
    ("The 'Stableford' scoring system in golf awards points based on what?", "Score relative to par on each hole", ["Total strokes","Handicap adjusted score","Birdies only"], "medium"),
    ("Bobby Jones won the Grand Slam in 1930, winning the four major championships of the era. What were they?", "US Open, British Open, US Amateur, British Amateur", ["Masters, US Open, British Open, PGA","Masters, US Open, US Amateur, PGA","British Open, French Open, US Amateur, British Amateur"], "hard"),
    ("Jack Nicklaus won his last major at the age of how old at the 1986 Masters?", "46", ["44","48","42"], "medium"),
    ("Which course hosts The Open Championship most often?", "St. Andrews (The Old Course)", ["Royal Birkdale","Muirfield","Turnberry"], "medium"),
    ("The Masters invites the previous year's champion to do what unique honor?", "Select the menu for the Champions Dinner", ["Design a hole","Pick the venue","Choose the pairings"], "medium"),
    ("Tiger Woods made his first PGA Tour start at which event in 1996?", "Greater Milwaukee Open", ["US Open","PGA Championship","Buick Classic"], "hard"),
    ("Lee Trevino won six major championships. Which national championships did he win twice each?", "US Open (1968, 1971), British Open (1971, 1972), PGA Championship (1974, 1984)", ["Masters twice","US Open three times","PGA Championship three times"], "hard"),
    ("Who has won the most money in PGA Tour history?", "Tiger Woods (over $120 million)", ["Phil Mickelson","Vijay Singh","Jim Furyk"], "medium"),
    ("The 'Hogan Slam' refers to Ben Hogan winning which three majors in 1953?", "Masters, US Open, and The Open Championship", ["Masters, PGA Championship, US Open","US Open, PGA Championship, The Open","Masters, British Amateur, US Open"], "hard"),
    ("Retief Goosen won the US Open twice in which years?", "2001 and 2004", ["1999 and 2003","2002 and 2005","2000 and 2003"], "hard"),
    ("Which golfer created the 'PGA Tour Skins Game'?", "It was created as a made-for-TV event in 1983", ["Arnold Palmer","Jack Nicklaus","Gary Player"], "hard"),
]

for text, ans, wrongs, diff in extra_golf:
    questions.append(q(text, ans, wrongs, "golf", diff))

# Extra olympics
extra_olympics = [
    ("Michael Phelps won how many gold medals in a single Olympics (Beijing 2008)?", "8", ["7","6","9"], "easy"),
    ("Who ran the first sub-4-minute mile in 1954?", "Roger Bannister", ["John Landy","Jim Ryun","Peter Snell"], "medium"),
    ("Which sprinter was banned after testing positive for steroids at the 1988 Olympics?", "Ben Johnson", ["Carl Lewis","Linford Christie","Dennis Mitchell"], "easy"),
    ("Nadia Comaneci scored the first perfect 10 in gymnastics at which Olympics?", "1976 Montreal", ["1972 Munich","1980 Moscow","1984 Los Angeles"], "medium"),
    ("The 2000 Summer Olympics were held in which city?", "Sydney", ["Melbourne","Brisbane","Adelaide"], "easy"),
    ("Which distance race did Haile Gebrselassie and Kenenisa Bekele dominate?", "10,000 meters", ["5,000 meters","Marathon","3,000 meter steeplechase"], "medium"),
    ("The Winter Olympics were held in the same year as Summer Olympics until when?", "1992 (separated after 1994)", ["1988","1996","1984"], "medium"),
    ("Which famous boxer won the Olympic gold medal in 1960 under his birth name Cassius Clay?", "Muhammad Ali", ["Joe Frazier","George Foreman","Sugar Ray Leonard"], "medium"),
    ("The Black Power salute at the 1968 Olympics was made by which two American athletes?", "Tommie Smith and John Carlos", ["Lee Evans and Larry James","Vince Matthews and Wayne Collett","Jim Hines and Charlie Greene"], "hard"),
    ("Which country has won the most Winter Olympic gold medals all-time?", "Norway", ["United States","Germany","Soviet Union"], "hard"),
    ("Who was the first woman to win multiple Olympic gold medals in the same sport?", "Fanny Blankers-Koen (1948 - 4 golds)", ["Wilma Rudolph","Dawn Fraser","Wyomia Tyus"], "hard"),
    ("The 'Flying Finn' nickname belonged to which Olympic runner?", "Paavo Nurmi", ["Emil Zatopek","Hannes Kolehmainen","Lasse Viren"], "hard"),
    ("Tara Lipinski became the youngest Olympic figure skating champion in 1998 at what age?", "15", ["16","14","17"], "medium"),
    ("Which country boycotted the 1984 Los Angeles Olympics in retaliation for the 1980 boycott?", "Soviet Union and Eastern bloc countries", ["China","Cuba","East Germany"], "medium"),
    ("Usain Bolt won three consecutive Olympic 100m gold medals in which years?", "2008, 2012, and 2016", ["2004, 2008, and 2012","2008, 2012, and 2016 (correct)","2012, 2016, and 2020"], "medium"),
    ("The 1972 Munich Olympics had how many Israeli athletes killed?", "11", ["9","12","7"], "hard"),
    ("Which country hosted the Winter Olympics twice before 2024?", "USA (1932 and 1980 Lake Placid, plus 1960 Squaw Valley)", ["France","Norway","Switzerland"], "hard"),
    ("Mary Lou Retton won the Olympic all-around gymnastics gold in which year?", "1984", ["1988","1980","1976"], "medium"),
    ("Who holds the record for most Olympic gold medals in a single Winter Games?", "Eric Heiden (5 in 1980 speed skating)", ["Bjorn Daehlie","Ole Einar Bjoerndalen","Apolo Ohno"], "hard"),
    ("The marathon distance of 26.2 miles was standardized at the 1908 London Olympics. Why that distance?", "To run from Windsor Castle to the Olympic stadium, plus the extra distance to the royal box", ["It's the distance from Athens to Marathon","A committee decision in 1896","Ancient Greek tradition"], "hard"),
]

for text, ans, wrongs, diff in extra_olympics:
    questions.append(q(text, ans, wrongs, "olympics", diff))

# Extra UFC
extra_ufc = [
    ("Who won the first UFC 1 tournament in 1993?", "Royce Gracie", ["Ken Shamrock","Tito Ortiz","Chuck Liddell"], "medium"),
    ("Georges St-Pierre retired as undefeated welterweight champion and returned to win which title?", "Middleweight title (briefly in 2017)", ["Lightweight title","Featherweight title","Light Heavyweight title"], "hard"),
    ("The UFC was initially banned in which state before being legalized with the Nevada model?", "New York (banned 1997-2016)", ["California","Florida","Texas"], "medium"),
    ("Which fighter is known as 'The Notorious' and has held titles in Featherweight and Lightweight?", "Conor McGregor", ["Tony Ferguson","Dustin Poirier","Eddie Alvarez"], "easy"),
    ("Anderson Silva defended the middleweight title how many times?", "10", ["8","12","7"], "medium"),
    ("The UFC introduced which organization to create a uniform set of drug testing rules?", "USADA (United States Anti-Doping Agency)", ["WADA","VADA","NSAC"], "medium"),
    ("What nationality is Khabib Nurmagomedov?", "Russian (Dagestani)", ["Chechen","Azeri","Kazakh"], "easy"),
    ("Which fighter won TUF Season 1 and became a multi-time champion?", "Forrest Griffin (won TUF 1 but not champion - he won the light heavyweight title later)", ["Rashad Evans","Diego Sanchez","Nate Quarry"], "hard"),
    ("Conor McGregor submitted Jose Aldo in how many seconds to win the featherweight title?", "13 seconds", ["19 seconds","31 seconds","7 seconds"], "medium"),
    ("The biggest gate in boxing history was the Canelo vs Alvarez vs Triple G rematch vs which opponent?", "Gennadiy Golovkin (Triple G)", ["Floyd Mayweather","Oscar De La Hoya","Daniel Jacobs"], "hard"),
    ("Jon Jones has been stripped of the light heavyweight title due to what?", "USADA violations and other issues", ["Age limit","Retirement","Injury"], "medium"),
    ("Stipe Miocic is from which US city and state?", "Euclid, Ohio (Cleveland area)", ["Detroit, Michigan","Pittsburgh, Pennsylvania","Chicago, Illinois"], "hard"),
    ("Which UFC weight class starts at what maximum weight?", "Flyweight at 125 lbs", ["Bantamweight at 135 lbs","Strawweight at 115 lbs","Atomweight at 105 lbs"], "medium"),
    ("Rose Namajunas won the women's strawweight title twice. She is nicknamed what?", "Thug Rose", ["Iron Rose","The Crusher","Wild Rose"], "medium"),
    ("The first UFC event sold on pay-per-view in the US was UFC 1 or which number?", "UFC 1", ["UFC 3","UFC 5","UFC 8"], "hard"),
    ("Which MMA fighter was known as 'The People's Warrior' who fought in PRIDE FC?", "Mirko Cro Cop Filipovic", ["Wanderlei Silva","Fedor Emelianenko","Antonio Rodrigo Nogueira"], "hard"),
    ("Israel Adesanya defeated Robert Whittaker to win the middleweight title in which year?", "2019", ["2018","2020","2021"], "medium"),
    ("UFC Bantamweight champion TJ Dillashaw tested positive for which substance?", "EPO (erythropoietin)", ["Testosterone","HGH","Clomiphene"], "hard"),
    ("Which female MMA fighter is considered the GOAT by many in women's MMA?", "Amanda Nunes", ["Ronda Rousey","Valentina Shevchenko","Cris Cyborg"], "medium"),
    ("The UFC's 'Fight of the Night' bonus is typically how much money?", "$50,000", ["$25,000","$100,000","$75,000"], "medium"),
]

for text, ans, wrongs, diff in extra_ufc:
    questions.append(q(text, ans, wrongs, "ufc", diff))

print(f"After all extra questions: {len(questions)}")

# ============================================================
# ADDITIONAL DATA-DRIVEN QUESTIONS
# ============================================================

# NBA teams info (founding year, arena, division)
nba_team_info = [
    ("Atlanta Hawks", "State Farm Arena", "Southeast", "1946"),
    ("Boston Celtics", "TD Garden", "Atlantic", "1946"),
    ("Brooklyn Nets", "Barclays Center", "Atlantic", "1967"),
    ("Charlotte Hornets", "Spectrum Center", "Southeast", "1988"),
    ("Chicago Bulls", "United Center", "Central", "1966"),
    ("Cleveland Cavaliers", "Rocket Mortgage FieldHouse", "Central", "1970"),
    ("Dallas Mavericks", "American Airlines Center", "Southwest", "1980"),
    ("Denver Nuggets", "Ball Arena", "Northwest", "1967"),
    ("Detroit Pistons", "Little Caesars Arena", "Central", "1941"),
    ("Golden State Warriors", "Chase Center", "Pacific", "1946"),
    ("Houston Rockets", "Toyota Center", "Southwest", "1967"),
    ("Indiana Pacers", "Gainbridge Fieldhouse", "Central", "1967"),
    ("Los Angeles Clippers", "Crypto.com Arena", "Pacific", "1970"),
    ("Los Angeles Lakers", "Crypto.com Arena", "Pacific", "1947"),
    ("Memphis Grizzlies", "FedExForum", "Southwest", "1995"),
    ("Miami Heat", "Kaseya Center", "Southeast", "1988"),
    ("Milwaukee Bucks", "Fiserv Forum", "Central", "1968"),
    ("Minnesota Timberwolves", "Target Center", "Northwest", "1989"),
    ("New Orleans Pelicans", "Smoothie King Center", "Southwest", "2002"),
    ("New York Knicks", "Madison Square Garden", "Atlantic", "1946"),
    ("Oklahoma City Thunder", "Paycom Center", "Northwest", "1967"),
    ("Orlando Magic", "Amway Center", "Southeast", "1989"),
    ("Philadelphia 76ers", "Wells Fargo Center", "Atlantic", "1946"),
    ("Phoenix Suns", "Footprint Center", "Pacific", "1968"),
    ("Portland Trail Blazers", "Moda Center", "Northwest", "1970"),
    ("Sacramento Kings", "Golden 1 Center", "Pacific", "1945"),
    ("San Antonio Spurs", "AT&T Center", "Southwest", "1967"),
    ("Toronto Raptors", "Scotiabank Arena", "Atlantic", "1995"),
    ("Utah Jazz", "Delta Center", "Northwest", "1974"),
    ("Washington Wizards", "Capital One Arena", "Southeast", "1961"),
]

arenas = [info[1] for info in nba_team_info]

for team, arena, division, year in nba_team_info:
    wrong_arenas = [a for a in arenas if a != arena]
    random.shuffle(wrong_arenas)
    questions.append(q(
        f"Which arena do the {team} play their home games in?",
        arena,
        wrong_arenas[:3],
        "basketball", "medium"
    ))
    questions.append(q(
        f"The {team} play in which NBA division?",
        f"{division} Division",
        [f"{d} Division" for d in ["Atlantic","Pacific","Central","Northwest","Southeast","Southwest"] if d != division][:3],
        "basketball", "hard"
    ))

print(f"After NBA team info: {len(questions)}")

# NFL Team Founding Years and Stadiums
nfl_team_info = [
    ("Arizona Cardinals", "State Farm Stadium", "1898"),
    ("Atlanta Falcons", "Mercedes-Benz Stadium", "1966"),
    ("Baltimore Ravens", "M&T Bank Stadium", "1996"),
    ("Buffalo Bills", "Highmark Stadium", "1960"),
    ("Carolina Panthers", "Bank of America Stadium", "1995"),
    ("Chicago Bears", "Soldier Field", "1920"),
    ("Cincinnati Bengals", "Paycor Stadium", "1968"),
    ("Cleveland Browns", "FirstEnergy Stadium", "1946"),
    ("Dallas Cowboys", "AT&T Stadium", "1960"),
    ("Denver Broncos", "Empower Field at Mile High", "1960"),
    ("Detroit Lions", "Ford Field", "1930"),
    ("Green Bay Packers", "Lambeau Field", "1919"),
    ("Houston Texans", "NRG Stadium", "2002"),
    ("Indianapolis Colts", "Lucas Oil Stadium", "1953"),
    ("Jacksonville Jaguars", "EverBank Stadium", "1995"),
    ("Kansas City Chiefs", "Arrowhead Stadium", "1960"),
    ("Las Vegas Raiders", "Allegiant Stadium", "1960"),
    ("Los Angeles Chargers", "SoFi Stadium", "1960"),
    ("Los Angeles Rams", "SoFi Stadium", "1936"),
    ("Miami Dolphins", "Hard Rock Stadium", "1966"),
    ("Minnesota Vikings", "U.S. Bank Stadium", "1961"),
    ("New England Patriots", "Gillette Stadium", "1960"),
    ("New Orleans Saints", "Caesars Superdome", "1967"),
    ("New York Giants", "MetLife Stadium", "1925"),
    ("New York Jets", "MetLife Stadium", "1960"),
    ("Philadelphia Eagles", "Lincoln Financial Field", "1933"),
    ("Pittsburgh Steelers", "Acrisure Stadium", "1933"),
    ("San Francisco 49ers", "Levi's Stadium", "1946"),
    ("Seattle Seahawks", "Lumen Field", "1976"),
    ("Tampa Bay Buccaneers", "Raymond James Stadium", "1976"),
    ("Tennessee Titans", "Nissan Stadium", "1960"),
    ("Washington Commanders", "FedExField", "1932"),
]

nfl_stadiums = [info[1] for info in nfl_team_info]

for team, stadium, year in nfl_team_info:
    wrong_stadiums = [s for s in nfl_stadiums if s != stadium]
    random.shuffle(wrong_stadiums)
    questions.append(q(
        f"Which stadium do the {team} play their home games in?",
        stadium,
        wrong_stadiums[:3],
        "football", "medium"
    ))

print(f"After NFL stadiums: {len(questions)}")

# MLB Team Info
mlb_team_info = [
    ("Arizona Diamondbacks", "Chase Field", "1998"),
    ("Atlanta Braves", "Truist Park", "1876"),
    ("Baltimore Orioles", "Oriole Park at Camden Yards", "1901"),
    ("Boston Red Sox", "Fenway Park", "1901"),
    ("Chicago Cubs", "Wrigley Field", "1876"),
    ("Chicago White Sox", "Guaranteed Rate Field", "1900"),
    ("Cincinnati Reds", "Great American Ball Park", "1882"),
    ("Cleveland Guardians", "Progressive Field", "1894"),
    ("Colorado Rockies", "Coors Field", "1993"),
    ("Detroit Tigers", "Comerica Park", "1901"),
    ("Houston Astros", "Minute Maid Park", "1962"),
    ("Kansas City Royals", "Kauffman Stadium", "1969"),
    ("Los Angeles Angels", "Angel Stadium", "1961"),
    ("Los Angeles Dodgers", "Dodger Stadium", "1883"),
    ("Miami Marlins", "loanDepot park", "1993"),
    ("Milwaukee Brewers", "American Family Field", "1969"),
    ("Minnesota Twins", "Target Field", "1901"),
    ("New York Mets", "Citi Field", "1962"),
    ("New York Yankees", "Yankee Stadium", "1901"),
    ("Oakland Athletics", "Oakland Coliseum", "1901"),
    ("Philadelphia Phillies", "Citizens Bank Park", "1883"),
    ("Pittsburgh Pirates", "PNC Park", "1882"),
    ("San Diego Padres", "Petco Park", "1969"),
    ("San Francisco Giants", "Oracle Park", "1883"),
    ("Seattle Mariners", "T-Mobile Park", "1977"),
    ("St. Louis Cardinals", "Busch Stadium", "1882"),
    ("Tampa Bay Rays", "Tropicana Field", "1998"),
    ("Texas Rangers", "Globe Life Field", "1961"),
    ("Toronto Blue Jays", "Rogers Centre", "1977"),
    ("Washington Nationals", "Nationals Park", "2005"),
]

mlb_stadiums = [info[1] for info in mlb_team_info]

for team, stadium, year in mlb_team_info:
    wrong_stadiums = [s for s in mlb_stadiums if s != stadium]
    random.shuffle(wrong_stadiums)
    questions.append(q(
        f"Which stadium do the {team} play their home games in?",
        stadium,
        wrong_stadiums[:3],
        "baseball", "medium"
    ))
    questions.append(q(
        f"The {team} were founded in approximately which year?",
        year,
        [str(int(year)+random.randint(5,20)) for _ in range(3)],
        "baseball", "hard"
    ))

print(f"After MLB stadiums: {len(questions)}")

# NHL Team Info  
nhl_team_info = [
    ("Anaheim Ducks", "Honda Center", "1993"),
    ("Arizona Coyotes", "Mullett Arena", "1972"),
    ("Boston Bruins", "TD Garden", "1924"),
    ("Buffalo Sabres", "KeyBank Center", "1970"),
    ("Calgary Flames", "Scotiabank Saddledome", "1972"),
    ("Carolina Hurricanes", "PNC Arena", "1972"),
    ("Chicago Blackhawks", "United Center", "1926"),
    ("Colorado Avalanche", "Ball Arena", "1972"),
    ("Columbus Blue Jackets", "Nationwide Arena", "2000"),
    ("Dallas Stars", "American Airlines Center", "1967"),
    ("Detroit Red Wings", "Little Caesars Arena", "1926"),
    ("Edmonton Oilers", "Rogers Place", "1972"),
    ("Florida Panthers", "Amerant Bank Arena", "1993"),
    ("Los Angeles Kings", "Crypto.com Arena", "1967"),
    ("Minnesota Wild", "Xcel Energy Center", "2000"),
    ("Montreal Canadiens", "Bell Centre", "1909"),
    ("Nashville Predators", "Bridgestone Arena", "1998"),
    ("New Jersey Devils", "Prudential Center", "1974"),
    ("New York Islanders", "UBS Arena", "1972"),
    ("New York Rangers", "Madison Square Garden", "1926"),
    ("Ottawa Senators", "Canadian Tire Centre", "1992"),
    ("Philadelphia Flyers", "Wells Fargo Center", "1967"),
    ("Pittsburgh Penguins", "PPG Paints Arena", "1967"),
    ("San Jose Sharks", "SAP Center", "1991"),
    ("Seattle Kraken", "Climate Pledge Arena", "2021"),
    ("St. Louis Blues", "Enterprise Center", "1967"),
    ("Tampa Bay Lightning", "Amalie Arena", "1992"),
    ("Toronto Maple Leafs", "Scotiabank Arena", "1917"),
    ("Vancouver Canucks", "Rogers Arena", "1970"),
    ("Vegas Golden Knights", "T-Mobile Arena", "2017"),
    ("Washington Capitals", "Capital One Arena", "1974"),
    ("Winnipeg Jets", "Canada Life Centre", "1999"),
]

nhl_arenas = [info[1] for info in nhl_team_info]

for team, arena, year in nhl_team_info:
    wrong_arenas = [a for a in nhl_arenas if a != arena]
    random.shuffle(wrong_arenas)
    questions.append(q(
        f"Which arena do the {team} play their home games in?",
        arena,
        wrong_arenas[:3],
        "hockey", "medium"
    ))

print(f"After NHL arenas: {len(questions)}")

# ============================================================
# DEDUP AND SAVE
# ============================================================
# Load existing questions
with open('/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/questions.json') as f:
    existing = json.load(f)

print(f"Loaded {len(existing)} existing questions")

# Combine
all_questions = existing + questions

# Dedup
seen = set()
unique = []
for item in all_questions:
    key = item['q'].strip().lower()[:100]
    if key not in seen:
        seen.add(key)
        unique.append(item)

print(f"Total after dedup: {len(unique)}")

from collections import Counter
sport_counts = Counter(q['sport'] for q in unique)
diff_counts = Counter(q['difficulty'] for q in unique)
print("Sport breakdown:", dict(sorted(sport_counts.items())))
print("Difficulty breakdown:", dict(diff_counts))

out_path = '/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/questions.json'
with open(out_path, 'w') as f:
    json.dump(unique, f, separators=(',', ':'))

import os
print(f"TOTAL: {len(unique)} questions saved")
print(f"File size: {os.path.getsize(out_path):,} bytes")
