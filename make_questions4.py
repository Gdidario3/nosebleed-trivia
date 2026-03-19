#!/usr/bin/env python3
"""Part 4 - More statistical data questions"""
import json, random, os
random.seed(789)

def q(question, answer, wrongs, sport, difficulty):
    c = [answer] + list(wrongs[:3])
    random.shuffle(c)
    return {"q":question,"a":answer,"choices":c,"sport":sport,"difficulty":difficulty}

questions = []

# ============================================================
# NBA ASSISTS LEADERS
# ============================================================
nba_assist_leaders = [
    (2024,"Tyrese Haliburton"),(2023,"James Harden"),(2022,"Chris Paul"),
    (2021,"Russell Westbrook"),(2020,"LeBron James"),(2019,"Russell Westbrook"),
    (2018,"Rajon Rondo"),(2017,"Russell Westbrook"),(2016,"Rajon Rondo"),
    (2015,"Chris Paul"),(2014,"Chris Paul"),(2013,"Rajon Rondo"),
    (2012,"Rajon Rondo"),(2011,"Steve Nash"),(2010,"Steve Nash"),
    (2009,"Chris Paul"),(2008,"Chris Paul"),(2007,"Steve Nash"),
    (2006,"Steve Nash"),(2005,"Steve Nash"),(2004,"Jason Kidd"),
    (2003,"Jason Kidd"),(2002,"Andre Miller"),(2001,"Jason Kidd"),
    (2000,"Jason Kidd"),(1999,"Jason Kidd"),(1998,"Rod Strickland"),
    (1997,"Mark Jackson"),(1996,"John Stockton"),(1995,"John Stockton"),
    (1994,"John Stockton"),(1993,"John Stockton"),(1992,"John Stockton"),
    (1991,"John Stockton"),(1990,"John Stockton"),(1989,"John Stockton"),
    (1988,"John Stockton"),(1987,"Magic Johnson"),(1986,"Magic Johnson"),
    (1985,"Magic Johnson"),(1984,"Magic Johnson"),(1983,"Magic Johnson"),
    (1982,"Magic Johnson"),(1981,"Kevin Porter"),(1980,"Michael Ray Richardson"),
    (1979,"Kevin Porter"),(1978,"Kevin Porter"),(1977,"Don Buse"),
    (1976,"Slick Watts"),(1975,"Kevin Porter"),(1974,"Ernie DiGregorio"),
    (1973,"Lenny Wilkens"),(1972,"Jerry West"),(1971,"Norm Van Lier"),
    (1970,"Len Wilkens"),(1969,"Oscar Robertson"),(1968,"Len Wilkens"),
    (1967,"Guy Rodgers"),(1966,"Oscar Robertson"),(1965,"Oscar Robertson"),
    (1964,"Oscar Robertson"),(1963,"Oscar Robertson"),(1962,"Oscar Robertson"),
    (1961,"Oscar Robertson"),(1960,"Bob Cousy"),(1959,"Bob Cousy"),
    (1958,"Bob Cousy"),(1957,"Bob Cousy"),(1956,"Bob Cousy"),
    (1955,"Bob Cousy"),
]

assist_pool = ["Tyrese Haliburton","James Harden","Chris Paul","Russell Westbrook","LeBron James",
    "Rajon Rondo","Steve Nash","Jason Kidd","John Stockton","Magic Johnson",
    "Bob Cousy","Oscar Robertson","Kevin Porter","Mark Jackson","Rod Strickland",
    "Andre Miller","Len Wilkens","Jerry West","Norm Van Lier","Lenny Wilkens",
    "Ernie DiGregorio","Don Buse","Slick Watts","Michael Ray Richardson","Kevin Durant",
    "Damian Lillard","Kyrie Irving","Trae Young","Ja Morant","Nikola Jokic","Luka Doncic",
    "Stephen Curry","Isiah Thomas","Penny Hardaway","Gary Payton"]

for yr, player in nba_assist_leaders:
    w = [p for p in assist_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who led the NBA in assists per game for the {yr-1}-{str(yr)[2:]} season?", player, w[:3], "basketball","hard"))

print(f"NBA assists done: {len(questions)}")

# ============================================================
# NBA REBOUNDING LEADERS
# ============================================================
nba_reb_leaders = [
    (2024,"Domantas Sabonis"),(2023,"Domantas Sabonis"),(2022,"Rudy Gobert"),
    (2021,"Clint Capela"),(2020,"Andre Drummond"),(2019,"Andre Drummond"),
    (2018,"DeAndre Jordan"),(2017,"Hassan Whiteside"),(2016,"Hassan Whiteside"),
    (2015,"DeAndre Jordan"),(2014,"DeAndre Jordan"),(2013,"Dwight Howard"),
    (2012,"Dwight Howard"),(2011,"Kevin Love"),(2010,"Marcus Camby"),
    (2009,"Dwight Howard"),(2008,"Marcus Camby"),(2007,"Kevin Garnett"),
    (2006,"Kevin Garnett"),(2005,"Kevin Garnett"),(2004,"Ben Wallace"),
    (2003,"Ben Wallace"),(2002,"Ben Wallace"),(2001,"Dikembe Mutombo"),
    (2000,"Dikembe Mutombo"),(1999,"Chris Webber"),(1998,"Dennis Rodman"),
    (1997,"Dennis Rodman"),(1996,"Dennis Rodman"),(1995,"Dennis Rodman"),
    (1994,"Dennis Rodman"),(1993,"Dennis Rodman"),(1992,"Dennis Rodman"),
    (1991,"David Robinson"),(1990,"Hakeem Olajuwon"),(1989,"Hakeem Olajuwon"),
    (1988,"Michael Cage"),(1987,"Charles Barkley"),(1986,"Bill Laimbeer"),
    (1985,"Moses Malone"),(1984,"Moses Malone"),(1983,"Moses Malone"),
    (1982,"Moses Malone"),(1981,"Moses Malone"),(1980,"Swen Nater"),
    (1979,"Moses Malone"),(1978,"Len Robinson"),(1977,"Bill Walton"),
    (1976,"Kareem Abdul-Jabbar"),(1975,"Wes Unseld"),(1974,"Elvin Hayes"),
    (1973,"Dave Cowens"),(1972,"Wilt Chamberlain"),(1971,"Wilt Chamberlain"),
    (1970,"Elvin Hayes"),(1969,"Wilt Chamberlain"),(1968,"Wilt Chamberlain"),
    (1967,"Wilt Chamberlain"),(1966,"Wilt Chamberlain"),(1965,"Bill Russell"),
    (1964,"Bill Russell"),(1963,"Wilt Chamberlain"),(1962,"Wilt Chamberlain"),
    (1961,"Wilt Chamberlain"),(1960,"Wilt Chamberlain"),(1959,"Bill Russell"),
    (1958,"Bill Russell"),(1957,"Bill Russell"),
]

reb_pool = ["Domantas Sabonis","Rudy Gobert","Clint Capela","Andre Drummond","DeAndre Jordan",
    "Hassan Whiteside","Dwight Howard","Kevin Love","Marcus Camby","Kevin Garnett",
    "Ben Wallace","Dikembe Mutombo","Chris Webber","Dennis Rodman","David Robinson",
    "Hakeem Olajuwon","Charles Barkley","Bill Laimbeer","Moses Malone","Swen Nater",
    "Bill Walton","Kareem Abdul-Jabbar","Wes Unseld","Elvin Hayes","Dave Cowens",
    "Wilt Chamberlain","Bill Russell","Bob Pettit","Jerry Lucas","Nate Thurmond",
    "Dave DeBusschere","Walt Bellamy","Len Wilkens","Michael Cage","Len Robinson"]

for yr, player in nba_reb_leaders:
    w = [p for p in reb_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who led the NBA in rebounds per game for the {yr-1}-{str(yr)[2:]} season?", player, w[:3], "basketball","hard"))

print(f"NBA rebounds done: {len(questions)}")

# ============================================================
# NFL PASSING LEADERS
# ============================================================
nfl_pass_leaders = [
    (2023,"Dak Prescott",4516),(2022,"Patrick Mahomes",5250),(2021,"Matthew Stafford",4886),
    (2020,"Deshaun Watson",4823),(2019,"Jameis Winston",5109),(2018,"Ben Roethlisberger",5129),
    (2017,"Ben Roethlisberger",4251),(2016,"Drew Brees",4494),(2015,"Russell Wilson",4024),
    (2014,"Ben Roethlisberger",4952),(2013,"Peyton Manning",5477),(2012,"Drew Brees",5177),
    (2011,"Drew Brees",5476),(2010,"Philip Rivers",4710),(2009,"Peyton Manning",4500),
    (2008,"Drew Brees",5069),(2007,"Tom Brady",4806),(2006,"Drew Brees",4418),
    (2005,"Carson Palmer",3836),(2004,"Peyton Manning",4557),(2003,"Peyton Manning",4267),
    (2002,"Rich Gannon",4689),(2001,"Kurt Warner",4830),(2000,"Peyton Manning",4413),
    (1999,"Steve Beuerlein",4436),(1998,"Brett Favre",4212),(1997,"Jeff George",3917),
    (1996,"Mark Brunell",4367),(1995,"Brett Favre",4413),(1994,"Drew Bledsoe",4555),
    (1993,"John Elway",4030),(1992,"Jim Kelly",3844),(1991,"Mark Rypien",3564),
    (1990,"Warren Moon",4689),(1989,"Don Majkowski",4318),(1988,"Dan Marino",4434),
    (1987,"Neil Lomax",3387),(1986,"Dan Marino",4746),(1985,"Dan Marino",4137),
    (1984,"Dan Marino",5084),(1983,"Steve Bartkowski",3167),(1982,"Dan Fouts",2883),
    (1981,"Dan Fouts",4802),(1980,"Brian Sipe",4132),(1979,"Dan Fouts",4082),
    (1978,"Fran Tarkenton",2916),(1977,"Bob Griese",2252),(1976,"James Harris",1460),
    (1975,"Fran Tarkenton",2994),(1974,"Sonny Jurgensen",1185),(1973,"Roman Gabriel",2621),
    (1972,"Joe Namath",2816),(1971,"John Hadl",2054),(1970,"John Brodie",2941),
    (1969,"Sonny Jurgensen",3102),(1968,"Earl Morrall",2909),(1967,"Sonny Jurgensen",3747),
    (1966,"Sonny Jurgensen",3209),(1965,"Rudy Bukich",2641),(1964,"Len Dawson",2879),
    (1963,"Y.A. Tittle",3145),(1962,"Sonny Jurgensen",3261),(1961,"George Blanda",3330),
    (1960,"Jack Kemp",3018),
]

pass_pool = ["Dak Prescott","Patrick Mahomes","Matthew Stafford","Deshaun Watson","Jameis Winston",
    "Ben Roethlisberger","Drew Brees","Russell Wilson","Peyton Manning","Philip Rivers",
    "Tom Brady","Carson Palmer","Rich Gannon","Kurt Warner","Brett Favre","Jeff George",
    "Mark Brunell","Drew Bledsoe","John Elway","Jim Kelly","Mark Rypien","Warren Moon",
    "Dan Marino","Dan Fouts","Joe Montana","Steve Young","Fran Tarkenton","Bob Griese",
    "Roger Staubach","Bart Starr","Joe Namath","Sonny Jurgensen","Y.A. Tittle","John Hadl",
    "Roman Gabriel","John Brodie","Earl Morrall","Len Dawson","George Blanda","Jack Kemp"]

for yr, player, yards in nfl_pass_leaders:
    w = [p for p in pass_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who led the NFL in passing yards in {yr}?", player, w[:3], "football","hard"))

print(f"NFL passing leaders done: {len(questions)}")

# ============================================================
# NFL RECEIVING LEADERS
# ============================================================
nfl_rec_leaders = [
    (2023,"Tyreek Hill",1799),(2022,"Justin Jefferson",1809),(2021,"Cooper Kupp",1947),
    (2020,"Stefon Diggs",1535),(2019,"Michael Thomas",1725),(2018,"DeAndre Hopkins",1572),
    (2017,"DeAndre Hopkins",1378),(2016,"Jordy Nelson",1257),(2015,"Brandon Marshall",1502),
    (2014,"Antonio Brown",1698),(2013,"Josh Gordon",1646),(2012,"Calvin Johnson",1964),
    (2011,"Calvin Johnson",1681),(2010,"Brandon Lloyd",1448),(2009,"Wes Welker",1348),
    (2008,"Andre Johnson",1575),(2007,"T.J. Houshmandzadeh",1081),(2006,"Chad Johnson",1369),
    (2005,"Steve Smith",1563),(2004,"Chad Johnson",1432),(2003,"Torry Holt",1696),
    (2002,"Marvin Harrison",1722),(2001,"David Boston",1598),(2000,"Torry Holt",1635),
    (1999,"Marvin Harrison",1663),(1998,"Antonio Freeman",1424),(1997,"Rob Moore",1584),
    (1996,"Jerry Rice",1254),(1995,"Jerry Rice",1848),(1994,"Jerry Rice",1499),
    (1993,"Sterling Sharpe",1274),(1992,"Sterling Sharpe",1461),(1991,"Haywood Jeffires",1181),
    (1990,"Jerry Rice",1502),(1989,"Jerry Rice",1483),(1988,"Henry Ellard",1414),
    (1987,"J.T. Smith",1117),(1986,"Jerry Rice",1570),(1985,"Steve Largent",1287),
    (1984,"Roy Green",1555),(1983,"Mike Quick",1409),(1982,"Wes Chandler",1032),
    (1981,"Alfred Jenkins",1358),(1980,"John Jefferson",1340),(1979,"Steve Largent",1237),
    (1978,"Wesley Walker",1168),(1977,"Drew Pearson",870),(1976,"Roger Carr",1112),
    (1975,"Ken Burrough",1063),(1974,"Cliff Branch",1092),(1973,"Harold Jackson",1116),
    (1972,"Harold Jackson",1048),(1971,"Otis Taylor",1110),(1970,"Dick Gordon",1026),
    (1969,"Warren Wells",1260),(1968,"Lance Alworth",1312),(1967,"Don Maynard",1434),
    (1966,"Lance Alworth",1383),(1965,"Dave Parks",1344),(1964,"Charley Hennigan",1546),
    (1963,"Bobby Mitchell",1436),(1962,"Sonny Randle",1158),(1961,"Lionel Taylor",1176),
    (1960,"Raymond Berry",1298),
]

rec_pool = ["Tyreek Hill","Justin Jefferson","Cooper Kupp","Stefon Diggs","Michael Thomas",
    "DeAndre Hopkins","Jordy Nelson","Brandon Marshall","Antonio Brown","Josh Gordon",
    "Calvin Johnson","Wes Welker","Andre Johnson","Chad Johnson","Steve Smith","Torry Holt",
    "Marvin Harrison","David Boston","Jerry Rice","Sterling Sharpe","Henry Ellard","Steve Largent",
    "Roy Green","Alfred Jenkins","Drew Pearson","Roger Carr","Harold Jackson","Lance Alworth",
    "Don Maynard","Charley Hennigan","Bobby Mitchell","Raymond Berry","Randy Moss",
    "Terrell Owens","Cris Carter","Larry Fitzgerald","T.J. Houshmandzadeh","Rob Moore",
    "Antonio Freeman","Haywood Jeffires","Mike Quick","Wesley Walker","John Jefferson"]

for yr, player, yards in nfl_rec_leaders:
    w = [p for p in rec_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who led the NFL in receiving yards in {yr}?", player, w[:3], "football","hard"))

print(f"NFL receiving done: {len(questions)}")

# ============================================================
# SOCCER - LA LIGA CHAMPIONS
# ============================================================
la_liga_champs = [
    (2023,"Barcelona"),(2022,"Real Madrid"),(2021,"Atletico Madrid"),
    (2020,"Real Madrid"),(2019,"Barcelona"),(2018,"Barcelona"),
    (2017,"Real Madrid"),(2016,"Real Madrid"),(2015,"Barcelona"),
    (2014,"Atletico Madrid"),(2013,"Barcelona"),(2012,"Real Madrid"),
    (2011,"Barcelona"),(2010,"Barcelona"),(2009,"Barcelona"),
    (2008,"Real Madrid"),(2007,"Real Madrid"),(2006,"Barcelona"),
    (2005,"Barcelona"),(2004,"Valencia"),(2003,"Real Madrid"),
    (2002,"Valencia"),(2001,"Real Madrid"),(2000,"Deportivo La Coruna"),
    (1999,"Barcelona"),(1998,"Barcelona"),(1997,"Real Madrid"),
    (1996,"Atletico Madrid"),(1995,"Real Madrid"),(1994,"Barcelona"),
    (1993,"Barcelona"),(1992,"Real Madrid"),(1991,"Barcelona"),
    (1990,"Real Madrid"),(1989,"Real Madrid"),(1988,"Real Madrid"),
    (1987,"Real Madrid"),(1986,"Real Madrid"),(1985,"Barcelona"),
    (1984,"Athletic Club"),(1983,"Athletic Club"),(1982,"Real Sociedad"),
    (1981,"Real Sociedad"),(1980,"Real Madrid"),(1979,"Real Madrid"),
    (1978,"Real Madrid"),(1977,"Atletico Madrid"),(1976,"Real Madrid"),
    (1975,"Real Madrid"),(1974,"Barcelona"),(1973,"Atletico Madrid"),
    (1972,"Real Madrid"),(1971,"Valencia"),(1970,"Atletico Madrid"),
    (1969,"Real Madrid"),(1968,"Real Madrid"),(1967,"Real Madrid"),
    (1966,"Atletico Madrid"),(1965,"Real Madrid"),(1964,"Real Madrid"),
    (1963,"Real Madrid"),(1962,"Real Madrid"),(1961,"Real Madrid"),
    (1960,"Barcelona"),(1959,"Barcelona"),(1958,"Real Madrid"),
    (1957,"Real Madrid"),(1956,"Athletic Club"),
]

la_liga_teams = ["Real Madrid","Barcelona","Atletico Madrid","Valencia","Sevilla","Athletic Club",
    "Real Sociedad","Deportivo La Coruna","Villarreal","Getafe","Betis","Celta Vigo",
    "Espanyol","Osasuna","Mallorca","Racing Santander","Real Valladolid"]

for yr, champ in la_liga_champs:
    w = [t for t in la_liga_teams if t != champ]
    random.shuffle(w)
    questions.append(q(f"Which club won the La Liga (Spanish top division) title in the {yr-1}-{str(yr)[2:]} season?", champ, w[:3], "soccer","hard"))

print(f"La Liga done: {len(questions)}")

# Bundesliga Champions
bundesliga_champs = [
    (2024,"Bayer Leverkusen"),(2023,"Bayern Munich"),(2022,"Bayern Munich"),
    (2021,"Bayern Munich"),(2020,"Bayern Munich"),(2019,"Bayern Munich"),
    (2018,"Bayern Munich"),(2017,"Bayern Munich"),(2016,"Bayern Munich"),
    (2015,"Bayern Munich"),(2014,"Bayern Munich"),(2013,"Bayern Munich"),
    (2012,"Borussia Dortmund"),(2011,"Borussia Dortmund"),(2010,"Bayern Munich"),
    (2009,"VfL Wolfsburg"),(2008,"Bayern Munich"),(2007,"VfB Stuttgart"),
    (2006,"Bayern Munich"),(2005,"Bayern Munich"),(2004,"Werder Bremen"),
    (2003,"Bayern Munich"),(2002,"Borussia Dortmund"),(2001,"Bayern Munich"),
    (2000,"Bayern Munich"),(1999,"Bayern Munich"),(1998,"Kaiserslautern"),
    (1997,"Bayern Munich"),(1996,"Borussia Dortmund"),(1995,"Borussia Dortmund"),
    (1994,"Bayern Munich"),(1993,"Werder Bremen"),(1992,"VfB Stuttgart"),
    (1991,"Kaiserslautern"),(1990,"Bayern Munich"),(1989,"Borussia Dortmund"),
    (1988,"Werder Bremen"),(1987,"Bayern Munich"),(1986,"Bayern Munich"),
    (1985,"Bayern Munich"),(1984,"VfB Stuttgart"),(1983,"Hamburg SV"),
    (1982,"Hamburg SV"),(1981,"Bayern Munich"),(1980,"Bayern Munich"),
    (1979,"Hamburg SV"),(1978,"Borussia Monchengladbach"),(1977,"Borussia Monchengladbach"),
    (1976,"Borussia Monchengladbach"),(1975,"Borussia Monchengladbach"),(1974,"Bayern Munich"),
    (1973,"Bayern Munich"),(1972,"Bayern Munich"),(1971,"Borussia Monchengladbach"),
    (1970,"Borussia Monchengladbach"),
]

bundesliga_teams = ["Bayern Munich","Borussia Dortmund","Bayer Leverkusen","Borussia Monchengladbach",
    "Werder Bremen","Hamburg SV","VfB Stuttgart","VfL Wolfsburg","Kaiserslautern","Schalke 04",
    "Bayer Uerdingen","1. FC Koln","Eintracht Frankfurt","RB Leipzig","Hertha BSC"]

for yr, champ in bundesliga_champs:
    w = [t for t in bundesliga_teams if t != champ]
    random.shuffle(w)
    questions.append(q(f"Which club won the Bundesliga (German top division) title in the {yr-1}-{str(yr)[2:]} season?", champ, w[:3], "soccer","hard"))

print(f"Bundesliga done: {len(questions)}")

# Serie A Champions  
serie_a_champs = [
    (2024,"Inter Milan"),(2023,"Napoli"),(2022,"AC Milan"),(2021,"Inter Milan"),
    (2020,"Juventus"),(2019,"Juventus"),(2018,"Juventus"),(2017,"Juventus"),
    (2016,"Juventus"),(2015,"Juventus"),(2014,"Juventus"),(2013,"Juventus"),
    (2012,"Juventus"),(2011,"AC Milan"),(2010,"Inter Milan"),(2009,"Inter Milan"),
    (2008,"Inter Milan"),(2007,"Inter Milan"),(2006,"Inter Milan"),(2005,"Juventus (stripped)"),
    (2004,"AC Milan"),(2003,"Juventus"),(2002,"Juventus"),(2001,"AS Roma"),
    (2000,"Lazio"),(1999,"AC Milan"),(1998,"Juventus"),(1997,"Juventus"),
    (1996,"AC Milan"),(1995,"Juventus"),(1994,"AC Milan"),(1993,"AC Milan"),
    (1992,"AC Milan"),(1991,"Sampdoria"),(1990,"Napoli"),(1989,"Inter Milan"),
    (1988,"AC Milan"),(1987,"Napoli"),(1986,"Juventus"),(1985,"Verona"),
    (1984,"Juventus"),(1983,"AS Roma"),(1982,"Juventus"),(1981,"Juventus"),
    (1980,"Inter Milan"),(1979,"AC Milan"),(1978,"Juventus"),(1977,"Juventus"),
    (1976,"Torino"),(1975,"Juventus"),(1974,"Lazio"),(1973,"Juventus"),
    (1972,"Juventus"),(1971,"Inter Milan"),(1970,"Cagliari"),
]

serie_a_teams = ["Juventus","Inter Milan","AC Milan","AS Roma","Lazio","Napoli","Fiorentina",
    "Sampdoria","Torino","Atalanta","Cagliari","Verona","Bologna","Parma","Udinese"]

for yr, champ in serie_a_champs:
    if "(stripped)" in champ:
        continue
    w = [t for t in serie_a_teams if t != champ]
    random.shuffle(w)
    questions.append(q(f"Which club won the Serie A (Italian top division) title in the {yr-1}-{str(yr)[2:]} season?", champ, w[:3], "soccer","hard"))

print(f"Serie A done: {len(questions)}")

# Premier League champions
premier_league_champs = [
    (2024,"Manchester City"),(2023,"Manchester City"),(2022,"Manchester City"),
    (2021,"Manchester City"),(2020,"Liverpool"),(2019,"Manchester City"),
    (2018,"Manchester City"),(2017,"Chelsea"),(2016,"Leicester City"),
    (2015,"Chelsea"),(2014,"Manchester City"),(2013,"Manchester United"),
    (2012,"Manchester City"),(2011,"Manchester United"),(2010,"Chelsea"),
    (2009,"Manchester United"),(2008,"Manchester United"),(2007,"Manchester United"),
    (2006,"Chelsea"),(2005,"Chelsea"),(2004,"Arsenal"),
    (2003,"Manchester United"),(2002,"Arsenal"),(2001,"Manchester United"),
    (2000,"Manchester United"),(1999,"Manchester United"),(1998,"Arsenal"),
    (1997,"Manchester United"),(1996,"Manchester United"),(1995,"Blackburn Rovers"),
    (1994,"Manchester United"),(1993,"Manchester United"),
]

pl_teams = ["Manchester City","Manchester United","Liverpool","Chelsea","Arsenal","Leicester City",
    "Blackburn Rovers","Tottenham","Everton","Aston Villa","Leeds United","Newcastle United",
    "West Ham","Nottingham Forest","Wolverhampton"]

for yr, champ in premier_league_champs:
    w = [t for t in pl_teams if t != champ]
    random.shuffle(w)
    questions.append(q(f"Which club won the English Premier League title in the {yr-1}-{str(yr)[2:]} season?", champ, w[:3], "soccer","hard"))

print(f"Premier League done: {len(questions)}")

# Copa America (selected)
copa_america = [
    (2021,"Argentina"),(2019,"Brazil"),(2016,"Chile"),(2015,"Chile"),
    (2011,"Uruguay"),(2007,"Brazil"),(2004,"Brazil"),(2001,"Colombia"),
    (1999,"Brazil"),(1997,"Brazil"),(1995,"Uruguay"),(1993,"Argentina"),
    (1991,"Argentina"),(1989,"Brazil"),(1987,"Uruguay"),(1983,"Uruguay"),
    (1979,"Paraguay"),(1975,"Peru"),(1967,"Uruguay"),(1963,"Bolivia"),
    (1959,"Argentina"),(1957,"Argentina"),(1955,"Argentina"),(1953,"Paraguay"),
    (1949,"Brazil"),(1947,"Argentina"),(1945,"Argentina"),(1942,"Uruguay"),
    (1941,"Argentina"),(1939,"Peru"),(1937,"Argentina"),
    (1935,"Uruguay"),(1929,"Argentina"),(1927,"Argentina"),(1926,"Uruguay"),
    (1925,"Argentina"),(1924,"Uruguay"),(1923,"Uruguay"),(1922,"Brazil"),
    (1921,"Argentina"),(1920,"Uruguay"),(1919,"Brazil"),(1917,"Uruguay"),
    (1916,"Uruguay"),
]

sa_teams = ["Argentina","Brazil","Uruguay","Chile","Paraguay","Colombia","Peru","Bolivia",
    "Ecuador","Venezuela","Mexico","USA","Honduras","Costa Rica","Panama"]

for yr, champ in copa_america:
    w = [t for t in sa_teams if t != champ]
    random.shuffle(w)
    questions.append(q(f"Which country won the Copa America in {yr}?", champ, w[:3], "soccer","hard"))

print(f"Copa America done: {len(questions)}")

# ============================================================
# OLYMPICS - SWIMMING RECORDS & GOLD MEDALISTS
# ============================================================
oly_swimming = [
    ("Michael Phelps","8 gold medals at the 2008 Beijing Olympics","100m butterfly, 200m butterfly, 200m IM, 400m IM, 4x100m free relay, 4x200m free relay, 4x100m medley relay, and 200m freestyle","swimming","medium"),
    ("Katie Ledecky","holds the world record in the 800m freestyle","800m freestyle","swimming","medium"),
    ("Ian Thorpe","was nicknamed 'Thorpedo' and won 5 Olympic gold medals representing which country?","Australia","swimming","easy"),
    ("Mark Spitz","won 7 gold medals at the 1972 Munich Olympics and broke how many world records?","7","swimming","medium"),
    ("Ryan Lochte","won 12 Olympic medals in swimming but was best known for rivalry with?","Michael Phelps","swimming","medium"),
    ("Caeleb Dressel","won 5 gold medals at the 2020 Tokyo Olympics","swimming","swimming","hard"),
    ("Kristin Otto","won 6 gold medals at the 1988 Seoul Olympics in swimming representing","East Germany","swimming","hard"),
    ("Shane Gould","won 3 individual gold medals and set world records at the 1972 Olympics at what age?","15","swimming","hard"),
    ("Janet Evans","dominated women's distance swimming in the late 1980s representing","United States","swimming","medium"),
    ("Inge de Bruijn","dominated the sprints at the 2000 Sydney Olympics representing","Netherlands","swimming","hard"),
]

for facts in oly_swimming:
    if len(facts) == 5:
        player, event, answer, sport_name, diff = facts
        questions.append(q(f"{player} {event}. This sport is known as?", answer if answer not in ["swimming","hard","medium"] else player,
            ["Lochte","Spitz","Thorpe","Dressel"] if answer in ["swimming"] else [answer+"wrong1",answer+"wrong2",answer+"wrong3"],
            "olympics","medium"))

# More targeted Olympics questions
more_oly_questions = [
    ("Michael Phelps has won the most Olympic medals all-time. How many total?", "28 medals", ["23 medals","25 medals","31 medals"], "olympics","easy"),
    ("Which female swimmer won 4 Olympic gold medals at the 1956 Melbourne Games?", "Dawn Fraser", ["Shane Gould","Kristin Otto","Janet Evans"], "olympics","hard"),
    ("How many gold medals did Mark Spitz win at the 1972 Munich Olympics?", "7", ["5","6","8"], "olympics","medium"),
    ("Michael Phelps set an Olympic record by winning how many gold medals at one Games (Beijing 2008)?", "8", ["7","6","9"], "olympics","easy"),
    ("Katie Ledecky has won how many Olympic gold medals as of the 2020 Tokyo Games?", "7", ["5","9","6"], "olympics","medium"),
    ("Simone Biles won how many Olympic medals at the 2016 Rio Olympics?", "5 (4 gold, 1 bronze)", ["4","6","7"], "olympics","medium"),
    ("The 1896 Athens Olympics had participants from how many countries?", "14", ["10","20","6"], "olympics","hard"),
    ("What was the first country to win the Olympic marathon in 1896?", "Greece (Spyridon Louis)", ["France","USA","UK"], "olympics","hard"),
    ("How many times has Brazil hosted the Summer Olympics?", "1 (2016 Rio)", ["2","0","3"], "olympics","medium"),
    ("Eric Heiden won 5 gold medals at which Winter Olympics?", "1980 Lake Placid", ["1984 Sarajevo","1976 Innsbruck","1988 Calgary"], "olympics","medium"),
    ("Which country has hosted the most Summer Olympic Games?", "USA (4 times)", ["UK","France","Greece"], "olympics","medium"),
    ("What year did South Korea first host the Summer Olympics?", "1988 (Seoul)", ["1984","1992","1980"], "olympics","easy"),
    ("Nadia Comaneci scored the first perfect 10 in Olympic gymnastics at age?", "14", ["16","12","18"], "olympics","medium"),
    ("Bob Beamon's long jump record at the 1968 Olympics stood for how many years?", "23 years", ["12 years","35 years","10 years"], "olympics","hard"),
    ("Which runner is the only person to win both the 100m and 200m at three consecutive Olympics?", "Usain Bolt", ["Carl Lewis","Jesse Owens","Michael Johnson"], "olympics","easy"),
    ("Florence Griffith-Joyner (Flo-Jo) set the women's 100m world record in 1988 at what time?", "10.49 seconds", ["10.62 seconds","10.38 seconds","10.55 seconds"], "olympics","hard"),
    ("The Olympic marathon distance is 26.2 miles. What is the distance in kilometers?", "42.195 km", ["40.0 km","44.5 km","38.0 km"], "olympics","medium"),
    ("Which country banned from the 1920 Olympics was re-invited and won gold that year?", "Germany was banned; Hungary was also banned", ["No country was banned","Germany","Russia"], "olympics","hard"),
    ("Who was the first female Olympic champion?", "Charlotte Cooper (tennis, 1900 Paris)", ["Madge Syers","Margaret Abbott","Helena Madison"], "olympics","hard"),
    ("Carl Lewis won 10 Olympic medals. How many were gold?", "9", ["8","10","7"], "olympics","medium"),
    ("The first African athlete to win an Olympic gold medal was from which country?", "South Africa (Reggie Walker, 100m 1908)", ["Ethiopia","Kenya","Nigeria"], "olympics","hard"),
    ("Paavo Nurmi won how many Olympic gold medals in his career?", "9", ["7","11","5"], "olympics","hard"),
    ("Which sport was removed from the Summer Olympics and then reintroduced?", "Baseball/Softball", ["Cricket","Polo","Lacrosse"], "olympics","medium"),
    ("Cathy Freeman won gold at the 2000 Sydney Olympics in which event?", "400m", ["100m","200m","400m hurdles"], "olympics","medium"),
    ("Which country has won the most Summer Olympic gold medals in athletics (track and field)?", "United States", ["Kenya","Jamaica","Ethiopia"], "olympics","medium"),
]

for text, ans, wrongs, sport_name, diff in more_oly_questions:
    questions.append(q(text, ans, wrongs, sport_name, diff))

print(f"Olympics done: {len(questions)}")

# ============================================================
# MORE F1 - GERMAN/JAPANESE/SPANISH GP WINNERS
# ============================================================
german_gp = [
    (2018,"Lewis Hamilton"),(2016,"Nico Rosberg"),(2014,"Nico Rosberg"),
    (2013,"Sebastian Vettel"),(2012,"Fernando Alonso"),(2011,"Lewis Hamilton"),
    (2010,"Fernando Alonso"),(2009,"Mark Webber"),(2008,"Lewis Hamilton"),
    (2007,"Lewis Hamilton"),(2006,"Michael Schumacher"),(2005,"Fernando Alonso"),
    (2004,"Michael Schumacher"),(2003,"Juan Pablo Montoya"),(2002,"Michael Schumacher"),
    (2001,"Ralf Schumacher"),(2000,"Rubens Barrichello"),(1999,"Eddie Irvine"),
    (1998,"Mika Hakkinen"),(1997,"Gerhard Berger"),(1996,"Damon Hill"),
    (1995,"Michael Schumacher"),(1994,"Gerhard Berger"),(1993,"Michael Schumacher"),
    (1992,"Nigel Mansell"),(1991,"Nigel Mansell"),(1990,"Ayrton Senna"),
    (1989,"Ayrton Senna"),(1988,"Ayrton Senna"),(1987,"Nelson Piquet"),
    (1986,"Nelson Piquet"),(1985,"Michele Alboreto"),(1984,"Alain Prost"),
    (1983,"Rene Arnoux"),(1982,"Patrick Tambay"),(1981,"Nelson Piquet"),
    (1980,"Jacques Laffite"),(1979,"Alan Jones"),(1978,"Mario Andretti"),
    (1977,"Niki Lauda"),(1976,"Jody Scheckter"),(1975,"Carlos Reutemann"),
    (1974,"Clay Regazzoni"),(1973,"Jackie Stewart"),
]

f1_pool2 = ["Lewis Hamilton","Sebastian Vettel","Nico Rosberg","Fernando Alonso","Michael Schumacher",
    "Mark Webber","Juan Pablo Montoya","Ralf Schumacher","Rubens Barrichello","Eddie Irvine",
    "Mika Hakkinen","Gerhard Berger","Damon Hill","Nigel Mansell","Ayrton Senna","Nelson Piquet",
    "Michele Alboreto","Alain Prost","Rene Arnoux","Patrick Tambay","Jacques Laffite","Alan Jones",
    "Mario Andretti","Niki Lauda","Jody Scheckter","Carlos Reutemann","Clay Regazzoni","Jackie Stewart",
    "Max Verstappen","Charles Leclerc","Carlos Sainz","Sergio Perez","Lando Norris","George Russell",
    "Kimi Raikkonen","Valtteri Bottas","Daniel Ricciardo","Pierre Gasly","Lance Stroll"]

for yr, driver in german_gp:
    w = [p for p in f1_pool2 if p != driver]
    random.shuffle(w)
    questions.append(q(f"Who won the German Grand Prix in {yr}?", driver, w[:3], "f1","hard"))

print(f"German GP done: {len(questions)}")

japanese_gp = [
    (2023,"Max Verstappen"),(2022,"Max Verstappen"),(2019,"Valtteri Bottas"),
    (2018,"Lewis Hamilton"),(2017,"Lewis Hamilton"),(2016,"Nico Rosberg"),
    (2015,"Lewis Hamilton"),(2014,"Lewis Hamilton"),(2013,"Sebastian Vettel"),
    (2012,"Sebastian Vettel"),(2011,"Jenson Button"),(2010,"Sebastian Vettel"),
    (2009,"Sebastian Vettel"),(2008,"Fernando Alonso"),(2007,"Lewis Hamilton"),
    (2006,"Michael Schumacher"),(2005,"Kimi Raikkonen"),(2004,"Michael Schumacher"),
    (2003,"Rubens Barrichello"),(2002,"Michael Schumacher"),(2001,"Michael Schumacher"),
    (2000,"Michael Schumacher"),(1999,"Mika Hakkinen"),(1998,"Mika Hakkinen"),
    (1997,"Michael Schumacher"),(1996,"Damon Hill"),(1995,"Michael Schumacher"),
    (1994,"Damon Hill"),(1993,"Ayrton Senna"),(1992,"Riccardo Patrese"),
    (1991,"Gerhard Berger"),(1990,"Nelson Piquet"),(1989,"Alessandro Nannini"),
    (1988,"Ayrton Senna"),(1987,"Gerhard Berger"),(1986,"Ayrton Senna"),
    (1985,"Ayrton Senna"),(1984,"Alain Prost"),
]

for yr, driver in japanese_gp:
    w = [p for p in f1_pool2 + ["Riccardo Patrese","Alessandro Nannini","Jenson Button",
        "Valtteri Bottas"] if p != driver]
    random.shuffle(w)
    questions.append(q(f"Who won the Japanese Grand Prix at Suzuka in {yr}?", driver, w[:3], "f1","hard"))

print(f"Japanese GP done: {len(questions)}")

# ============================================================
# COLLEGE FOOTBALL - HEISMAN TROPHY
# ============================================================
heisman_winners = [
    (2023,"Jayden Daniels","LSU"),(2022,"Caleb Williams","USC"),
    (2021,"Bryce Young","Alabama"),(2020,"DeVonta Smith","Alabama"),
    (2019,"Joe Burrow","LSU"),(2018,"Kyler Murray","Oklahoma"),
    (2017,"Baker Mayfield","Oklahoma"),(2016,"Lamar Jackson","Louisville"),
    (2015,"Derrick Henry","Alabama"),(2014,"Marcus Mariota","Oregon"),
    (2013,"Jameis Winston","Florida State"),(2012,"Johnny Manziel","Texas A&M"),
    (2011,"Robert Griffin III","Baylor"),(2010,"Cam Newton","Auburn"),
    (2009,"Mark Ingram Jr.","Alabama"),(2008,"Sam Bradford","Oklahoma"),
    (2007,"Tim Tebow","Florida"),(2006,"Troy Smith","Ohio State"),
    (2005,"Reggie Bush","USC"),(2004,"Matt Leinart","USC"),
    (2003,"Jason White","Oklahoma"),(2002,"Carson Palmer","USC"),
    (2001,"Eric Crouch","Nebraska"),(2000,"Chris Weinke","Florida State"),
    (1999,"Ron Dayne","Wisconsin"),(1998,"Ricky Williams","Texas"),
    (1997,"Charles Woodson","Michigan"),(1996,"Danny Wuerffel","Florida"),
    (1995,"Eddie George","Ohio State"),(1994,"Rashaan Salaam","Colorado"),
    (1993,"Charlie Ward","Florida State"),(1992,"Gino Torretta","Miami"),
    (1991,"Desmond Howard","Michigan"),(1990,"Ty Detmer","Brigham Young"),
    (1989,"Andre Ware","Houston"),(1988,"Barry Sanders","Oklahoma State"),
    (1987,"Tim Brown","Notre Dame"),(1986,"Vinny Testaverde","Miami"),
    (1985,"Bo Jackson","Auburn"),(1984,"Doug Flutie","Boston College"),
    (1983,"Mike Rozier","Nebraska"),(1982,"Herschel Walker","Georgia"),
    (1981,"Marcus Allen","USC"),(1980,"George Rogers","South Carolina"),
    (1979,"Charles White","USC"),(1978,"Billy Sims","Oklahoma"),
    (1977,"Earl Campbell","Texas"),(1976,"Tony Dorsett","Pittsburgh"),
    (1975,"Archie Griffin","Ohio State"),(1974,"Archie Griffin","Ohio State"),
    (1973,"John Cappelletti","Penn State"),(1972,"Johnny Rodgers","Nebraska"),
    (1971,"Pat Sullivan","Auburn"),(1970,"Jim Plunkett","Stanford"),
]

heisman_players = ["Jayden Daniels","Caleb Williams","Bryce Young","DeVonta Smith","Joe Burrow",
    "Kyler Murray","Baker Mayfield","Lamar Jackson","Derrick Henry","Marcus Mariota",
    "Jameis Winston","Johnny Manziel","Robert Griffin III","Cam Newton","Mark Ingram Jr.",
    "Sam Bradford","Tim Tebow","Troy Smith","Reggie Bush","Matt Leinart","Carson Palmer",
    "Eric Crouch","Chris Weinke","Ron Dayne","Ricky Williams","Charles Woodson","Danny Wuerffel",
    "Eddie George","Charlie Ward","Desmond Howard","Barry Sanders","Tim Brown","Vinny Testaverde",
    "Bo Jackson","Doug Flutie","Mike Rozier","Herschel Walker","Marcus Allen","George Rogers",
    "Charles White","Billy Sims","Earl Campbell","Tony Dorsett","Archie Griffin","Jim Plunkett"]

for yr, player, school in heisman_winners:
    w = [p for p in heisman_players if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the Heisman Trophy in {yr}?", player, w[:3], "football","hard"))
    w2 = ["Alabama","Ohio State","Oklahoma","USC","Florida","Texas","Michigan","Notre Dame","LSU",
        "Georgia","Nebraska","Clemson","Penn State","Auburn","Oregon"]
    w2 = [s for s in w2 if s != school]
    random.shuffle(w2)
    questions.append(q(f"Heisman Trophy winner {player} played college football at which school?", school, w2[:3], "football","hard"))

print(f"Heisman done: {len(questions)}")

# ============================================================
# NCAA BASKETBALL TOURNAMENT CHAMPIONS
# ============================================================
ncaa_bball_champs = [
    (2024,"Connecticut"),(2023,"Connecticut"),(2022,"Kansas"),
    (2021,"Baylor"),(2020,"No tournament - COVID"),(2019,"Virginia"),
    (2018,"Villanova"),(2017,"North Carolina"),(2016,"Villanova"),
    (2015,"Duke"),(2014,"Connecticut"),(2013,"Louisville"),
    (2012,"Kentucky"),(2011,"Connecticut"),(2010,"Duke"),
    (2009,"North Carolina"),(2008,"Kansas"),(2007,"Florida"),
    (2006,"Florida"),(2005,"North Carolina"),(2004,"Connecticut"),
    (2003,"Syracuse"),(2002,"Maryland"),(2001,"Duke"),
    (2000,"Michigan State"),(1999,"Connecticut"),(1998,"Kentucky"),
    (1997,"Arizona"),(1996,"Kentucky"),(1995,"UCLA"),
    (1994,"Duke"),(1993,"North Carolina"),(1992,"Duke"),
    (1991,"Duke"),(1990,"UNLV"),(1989,"Michigan"),
    (1988,"Kansas"),(1987,"Indiana"),(1986,"Louisville"),
    (1985,"Villanova"),(1984,"Georgetown"),(1983,"NC State"),
    (1982,"North Carolina"),(1981,"Indiana"),(1980,"Louisville"),
    (1979,"Michigan State"),(1978,"Kentucky"),(1977,"Marquette"),
    (1976,"Indiana"),(1975,"UCLA"),(1974,"NC State"),
    (1973,"UCLA"),(1972,"UCLA"),(1971,"UCLA"),
    (1970,"UCLA"),(1969,"UCLA"),(1968,"Houston"),
    (1967,"UCLA"),(1966,"Texas Western"),(1965,"UCLA"),
    (1964,"UCLA"),
]

ncaa_schools = ["Connecticut","Kansas","Baylor","Virginia","Villanova","North Carolina","Duke",
    "Kentucky","Florida","Maryland","Syracuse","Michigan State","Arizona","UCLA","Indiana",
    "Louisville","Georgetown","NC State","UNLV","Michigan","Marquette","Texas Western",
    "Houston","Ohio State","Michigan","Arizona State","Wisconsin","Gonzaga","Purdue","Auburn"]

for yr, champ in ncaa_bball_champs:
    if "No tournament" in champ:
        continue
    w = [s for s in ncaa_schools if s != champ]
    random.shuffle(w)
    questions.append(q(f"Which school won the NCAA Men's Basketball Tournament in {yr}?", champ, w[:3], "basketball","hard"))

print(f"NCAA bball done: {len(questions)}")

# ============================================================
# BOXING DATA
# ============================================================
boxing_champs = [
    ("Muhammad Ali","Cassius Clay","World Heavyweight Champion 3 times","ufc","medium"),
    ("Sugar Ray Robinson","considered pound-for-pound greatest boxer ever","World welterweight and middleweight champion","ufc","hard"),
    ("Joe Louis","defended the heavyweight title a record 25 times from 1937 to 1949","1937","ufc","hard"),
    ("Rocky Marciano","retired as the only undefeated heavyweight champion","49-0","ufc","hard"),
    ("Mike Tyson","became the youngest world heavyweight champion in history at age","20","ufc","medium"),
    ("Floyd Mayweather","retired with an undefeated record of","50-0","ufc","medium"),
    ("Manny Pacquiao","is from which country","Philippines","ufc","easy"),
    ("Evander Holyfield","is famous for what happened in his ear during the rematch with Mike Tyson","Tyson bit his ear","ufc","easy"),
    ("Larry Holmes","defended the WBC heavyweight title how many times between 1978 and 1983","20","ufc","hard"),
    ("Marvelous Marvin Hagler","held the middleweight title from 1980 to 1987. He lost to who?","Sugar Ray Leonard","ufc","medium"),
    ("Roberto Duran","defeated Sugar Ray Leonard in 1980 but then quit in the rematch saying what?","No mas (No more)","ufc","medium"),
    ("Lennox Lewis","was a two-time heavyweight champion from which country","United Kingdom/Canada","ufc","medium"),
    ("George Foreman","regained the heavyweight title at age 45 in 1994 defeating","Michael Moorer","ufc","hard"),
    ("Joe Frazier","defeated Muhammad Ali in the 'Fight of the Century' in which year","1971","ufc","medium"),
    ("Jack Dempsey","was the first boxing champion to appear in a match that grossed over $1 million. He held which title","Heavyweight","ufc","hard"),
]

for player, event, answer, sport_name, diff in boxing_champs:
    w = ["Muhammad Ali","Sugar Ray Robinson","Rocky Marciano","Mike Tyson","Floyd Mayweather",
         "Manny Pacquiao","Evander Holyfield","Larry Holmes","Marvin Hagler","Roberto Duran",
         "Lennox Lewis","George Foreman","Joe Frazier","Jack Dempsey","Joe Louis","Sonny Liston"]
    w = [x for x in w if x not in [player, answer]]
    random.shuffle(w)
    if answer not in ["Philippines","50-0","49-0","20","Heavyweight"]:
        questions.append(q(f"{player} {event}. What/who is the answer?", answer, w[:3], sport_name, diff))

print(f"Boxing done: {len(questions)}")

# ============================================================
# NFL SCORING LEADERS / TD LEADERS
# ============================================================
nfl_td_leaders = [
    (2023,"Christian McCaffrey",21),(2022,"Austin Ekeler",18),(2021,"Cooper Kupp",16),
    (2020,"Davante Adams",18),(2019,"Derrick Henry",16),(2018,"Tyreek Hill",15),
    (2017,"LeVeon Bell",14),(2016,"Mike Gillislee",11),(2015,"Greg Olsen",12),
    (2014,"Dez Bryant",16),(2013,"LeSean McCoy",9),(2012,"Arian Foster",15),
    (2011,"Rob Gronkowski",17),(2010,"Arian Foster",18),(2009,"Larry Fitzgerald",13),
    (2008,"Clinton Portis",14),(2007,"Randy Moss",23),(2006,"LaDainian Tomlinson",28),
    (2005,"Shaun Alexander",27),(2004,"Shaun Alexander",16),(2003,"Priest Holmes",27),
    (2002,"Priest Holmes",21),(2001,"Marshall Faulk",21),(2000,"Marshall Faulk",26),
    (1999,"Stephen Davis",17),(1998,"Terrell Davis",23),(1997,"Barry Sanders",14),
    (1996,"Carl Pickens",17),(1995,"Emmitt Smith",25),(1994,"Marshall Faulk",12),
    (1993,"Jerry Rice",16),(1992,"Emmitt Smith",19),(1991,"Barry Sanders",17),
    (1990,"Barry Sanders",16),(1989,"Christian Okoye",12),(1988,"Greg Bell",18),
    (1987,"Jerry Rice",23),(1986,"George Rogers",18),(1985,"Marcus Allen",14),
    (1984,"Marcus Allen",18),(1983,"John Riggins",24),(1982,"Marcus Allen",14),
    (1981,"Chuck Muncie",19),(1980,"Billy Sims",16),(1979,"Earl Campbell",19),
]

td_pool = ["Christian McCaffrey","Cooper Kupp","Davante Adams","Derrick Henry","LeSean McCoy",
    "Rob Gronkowski","Arian Foster","Randy Moss","LaDainian Tomlinson","Shaun Alexander",
    "Priest Holmes","Marshall Faulk","Terrell Davis","Barry Sanders","Emmitt Smith","Jerry Rice",
    "Marcus Allen","John Riggins","Earl Campbell","Walter Payton","Eric Dickerson","Jim Brown",
    "Austin Ekeler","Tyreek Hill","Dez Bryant","Clinton Portis","Larry Fitzgerald","Mike Gillislee"]

for yr, player, tds in nfl_td_leaders:
    w = [p for p in td_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who led the NFL in touchdowns scored in {yr}?", player, w[:3], "football","hard"))

print(f"NFL TD leaders done: {len(questions)}")

# ============================================================
# MLB - BATTING TITLE (leading average) BY YEAR
# ============================================================
mlb_batting_title = [
    (2023,"Luis Arraez",.354),(2022,"Luis Arraez",.316),(2021,"Trea Turner",.328),
    (2020,"DJ LeMahieu",.364),(2019,"DJ LeMahieu",.327),(2018,"Mookie Betts",.346),
    (2017,"Jose Altuve",.346),(2016,"DJ LeMahieu",.348),(2015,"Dee Gordon",.333),
    (2014,"Jose Altuve",.341),(2013,"Miguel Cabrera",.348),(2012,"Miguel Cabrera",.330),
    (2011,"Jose Reyes",.337),(2010,"Josh Hamilton",.359),(2009,"Joe Mauer",.365),
    (2008,"Chipper Jones",.364),(2007,"Magglio Ordonez",.363),(2006,"Freddy Sanchez",.344),
    (2005,"Michael Young",.331),(2004,"Ichiro Suzuki",.372),(2003,"Bill Mueller",.326),
    (2002,"Manny Ramirez",.349),(2001,"Larry Walker",.350),(2000,"Darin Erstad",.355),
    (1999,"Larry Walker",.379),(1998,"Bernie Williams",.339),(1997,"Tony Gwynn",.372),
    (1996,"Tony Gwynn",.353),(1995,"Tony Gwynn",.368),(1994,"Tony Gwynn",.394),
    (1993,"Andres Galarraga",.370),(1992,"Gary Sheffield",.330),(1991,"Julio Franco",.341),
    (1990,"George Brett",.329),(1989,"Tony Gwynn",.336),(1988,"Tony Gwynn",.313),
    (1987,"Tony Gwynn",.370),(1986,"Wade Boggs",.357),(1985,"Wade Boggs",.368),
    (1984,"Don Mattingly",.343),(1983,"Bill Madlock",.323),(1982,"Al Oliver",.331),
    (1981,"Carney Lansford",.336),(1980,"George Brett",.390),(1979,"Keith Hernandez",.344),
    (1978,"Rod Carew",.333),(1977,"Rod Carew",.388),(1976,"Bill Madlock",.339),
    (1975,"Bill Madlock",.354),(1974,"Keith Hernandez",.309),(1973,"Rod Carew",.350),
    (1972,"Billy Williams",.333),(1971,"Joe Torre",.363),(1970,"Rico Carty",.366),
    (1969,"Pete Rose",.348),(1968,"Carl Yastrzemski",.301),(1967,"Roberto Clemente",.357),
    (1966,"Matty Alou",.342),(1965,"Roberto Clemente",.329),(1964,"Roberto Clemente",.339),
    (1963,"Tommy Davis",.326),(1962,"Tommy Davis",.346),(1961,"Norm Cash",.361),
    (1960,"Dick Groat",.325),(1959,"Hank Aaron",.355),(1958,"Richie Ashburn",.350),
    (1957,"Ted Williams",.388),(1956,"Mickey Mantle",.353),(1955,"Richie Ashburn",.338),
    (1954,"Willie Mays",.345),(1953,"Carl Furillo",.344),(1952,"Ferris Fain",.327),
    (1951,"Ferris Fain",.344),(1950,"Billy Goodman",.354),(1949,"George Kell",.343),
    (1948,"Stan Musial",.376),(1947,"Harry Walker",.363),(1946,"Mickey Vernon",.353),
    (1945,"Snuffy Stirnweiss",.309),(1944,"Lou Boudreau",.327),(1943,"Stan Musial",.357),
    (1942,"Ted Williams",.356),(1941,"Ted Williams",.406),(1940,"Debs Garms",.355),
    (1939,"Joe DiMaggio",.381),(1938,"Jimmie Foxx",.349),(1937,"Joe Medwick",.374),
    (1936,"Paul Waner",.373),(1935,"Arky Vaughan",.385),(1934,"Paul Waner",.362),
    (1933,"Lefty O'Doul",.349),(1932,"Dale Alexander",.367),(1931,"Chick Hafey",.349),
    (1930,"Bill Terry",.401),(1929,"Lefty O'Doul",.398),(1928,"Goose Goslin",.379),
    (1927,"Harry Heilmann",.398),(1926,"Heinie Manush",.378),(1925,"Rogers Hornsby",.403),
    (1924,"Babe Herman",.393),(1923,"Harry Heilmann",.403),(1922,"George Sisler",.420),
    (1921,"Harry Heilmann",.394),(1920,"George Sisler",.407),(1919,"Ty Cobb",.384),
]

batting_pool = ["Luis Arraez","Trea Turner","DJ LeMahieu","Mookie Betts","Jose Altuve","Dee Gordon",
    "Miguel Cabrera","Jose Reyes","Josh Hamilton","Joe Mauer","Chipper Jones","Magglio Ordonez",
    "Ichiro Suzuki","Tony Gwynn","Larry Walker","Mike Trout","Wade Boggs","Rod Carew","Ted Williams",
    "Stan Musial","Rogers Hornsby","Ty Cobb","George Sisler","Harry Heilmann","Bill Terry",
    "Roberto Clemente","Pete Rose","Carl Yastrzemski","Mickey Mantle","Hank Aaron","Willie Mays",
    "George Brett","Don Mattingly","Keith Hernandez","Joe DiMaggio","Paul Waner"]

for yr, player, avg in mlb_batting_title:
    w = [p for p in batting_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the MLB batting title in {yr}?", player, w[:3], "baseball","hard"))

print(f"MLB batting titles done: {len(questions)}")

# ============================================================
# UFC CHAMPIONS - BY WEIGHT CLASS AND YEAR
# ============================================================
ufc_champs_data = [
    ("Heavyweight","Jon Jones",2023),("Heavyweight","Francis Ngannou",2021),
    ("Heavyweight","Stipe Miocic",2019),("Heavyweight","Daniel Cormier",2018),
    ("Heavyweight","Stipe Miocic",2016),("Heavyweight","Fabricio Werdum",2015),
    ("Heavyweight","Cain Velasquez",2012),("Heavyweight","Junior dos Santos",2011),
    ("Heavyweight","Brock Lesnar",2008),("Heavyweight","Randy Couture",2007),
    ("Light Heavyweight","Alex Pereira",2023),("Light Heavyweight","Jiri Prochazka",2022),
    ("Light Heavyweight","Jan Blachowicz",2020),("Light Heavyweight","Jon Jones",2018),
    ("Light Heavyweight","Daniel Cormier",2015),("Light Heavyweight","Jon Jones",2012),
    ("Light Heavyweight","Lyoto Machida",2009),("Light Heavyweight","Rashad Evans",2008),
    ("Light Heavyweight","Quinton Jackson",2007),("Light Heavyweight","Chuck Liddell",2004),
    ("Middleweight","Dricus du Plessis",2023),("Middleweight","Israel Adesanya",2022),
    ("Middleweight","Robert Whittaker",2017),("Middleweight","Michael Bisping",2016),
    ("Middleweight","Chris Weidman",2013),("Middleweight","Anderson Silva",2006),
    ("Welterweight","Leon Edwards",2022),("Welterweight","Kamaru Usman",2019),
    ("Welterweight","Tyron Woodley",2016),("Welterweight","Georges St-Pierre",2013),
    ("Welterweight","Carlos Condit",2012),("Welterweight","Johny Hendricks",2013),
    ("Lightweight","Islam Makhachev",2022),("Lightweight","Charles Oliveira",2021),
    ("Lightweight","Khabib Nurmagomedov",2018),("Lightweight","Eddie Alvarez",2016),
    ("Lightweight","Rafael dos Anjos",2015),("Lightweight","Anthony Pettis",2012),
    ("Lightweight","Frank Edgar",2010),("Lightweight","BJ Penn",2008),
    ("Featherweight","Ilia Topuria",2024),("Featherweight","Alexander Volkanovski",2019),
    ("Featherweight","Max Holloway",2017),("Featherweight","Conor McGregor",2015),
    ("Featherweight","Jose Aldo",2010),("Featherweight","Sean O'Malley",2023),
    ("Bantamweight","Dominick Cruz",2016),("Bantamweight","TJ Dillashaw",2014),
    ("Bantamweight","Urijah Faber",2013),("Bantamweight","Renan Barao",2012),
    ("Flyweight","Demetrious Johnson",2012),("Flyweight","Henry Cejudo",2018),
    ("Flyweight","Brandon Moreno",2021),
    ("Women's Strawweight","Joanna Jedrzejczyk",2015),("Women's Strawweight","Zhang Weili",2019),
    ("Women's Strawweight","Rose Namajunas",2021),("Women's Strawweight","Carla Esparza",2022),
    ("Women's Bantamweight","Ronda Rousey",2012),("Women's Bantamweight","Amanda Nunes",2016),
    ("Women's Bantamweight","Holly Holm",2015),
]

ufc_pool = ["Jon Jones","Francis Ngannou","Stipe Miocic","Daniel Cormier","Brock Lesnar",
    "Randy Couture","Cain Velasquez","Junior dos Santos","Alex Pereira","Jiri Prochazka",
    "Jan Blachowicz","Lyoto Machida","Rashad Evans","Chuck Liddell","Quinton Jackson",
    "Anderson Silva","Chris Weidman","Michael Bisping","Robert Whittaker","Israel Adesanya",
    "Leon Edwards","Kamaru Usman","Georges St-Pierre","Tyron Woodley","Islam Makhachev",
    "Charles Oliveira","Khabib Nurmagomedov","Eddie Alvarez","Anthony Pettis","Frank Edgar",
    "Conor McGregor","Jose Aldo","Alexander Volkanovski","Max Holloway","Ronda Rousey",
    "Amanda Nunes","Holly Holm","Demetrious Johnson","Henry Cejudo","Ilia Topuria",
    "Dricus du Plessis","Brandon Moreno","Rose Namajunas","Joanna Jedrzejczyk","Zhang Weili",
    "Sean O'Malley","TJ Dillashaw","BJ Penn","Rafael dos Anjos","Carlos Condit"]

for weight, champ, yr in ufc_champs_data:
    w = [p for p in ufc_pool if p != champ]
    random.shuffle(w)
    questions.append(q(f"Who was the UFC {weight} champion in {yr}?", champ, w[:3], "ufc","hard"))
    questions.append(q(f"Which UFC weight class did {champ} hold the title in {yr}?", weight,
        [wc for wc in ["Heavyweight","Light Heavyweight","Middleweight","Welterweight","Lightweight",
            "Featherweight","Bantamweight","Flyweight","Women's Strawweight","Women's Bantamweight"] if wc != weight][:3],
        "ufc","hard"))

print(f"UFC champs done: {len(questions)}")

# ============================================================
# SAVE
# ============================================================
with open('/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/questions.json') as f:
    existing = json.load(f)

print(f"Loaded {len(existing)} existing questions")
all_q = existing + questions

seen = set()
unique = []
for item in all_q:
    key = item['q'].strip().lower()[:100]
    if key not in seen:
        seen.add(key)
        unique.append(item)

from collections import Counter
sport_counts = Counter(q['sport'] for q in unique)
diff_counts = Counter(q['difficulty'] for q in unique)
print("Sport breakdown:", dict(sorted(sport_counts.items())))
print("Difficulty breakdown:", dict(diff_counts))
print(f"TOTAL: {len(unique)} questions")

with open('/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/questions.json','w') as f:
    json.dump(unique, f, separators=(',',':'))

print(f"File size: {os.path.getsize('/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/questions.json'):,} bytes")
