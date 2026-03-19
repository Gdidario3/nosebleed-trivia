#!/usr/bin/env python3
"""Batch 3: 125 football + 89 golf + 1 baseball = 215 questions."""

import json
import time

NEW_QUESTIONS = [
    # ========================
    # FOOTBALL (125 questions)
    # ========================

    # --- Famous Plays (1-15) ---
    {"q": "In Super Bowl XLIX, which Patriots DB intercepted Russell Wilson at the goal line to seal the win?", "a": "Malcolm Butler", "choices": ["Malcolm Butler", "Darrelle Revis", "Brandon Browner", "Devin McCourty"], "sport": "football", "difficulty": "medium"},
    {"q": "The 'Immaculate Reception' in 1972 was caught by which Pittsburgh Steelers running back?", "a": "Franco Harris", "choices": ["Franco Harris", "Rocky Bleier", "John Fuqua", "Preston Pearson"], "sport": "football", "difficulty": "medium"},
    {"q": "Which play, involving a lateral and a kick return, is known as 'The Play' between Cal and Stanford in 1982?", "a": "A five-lateral kickoff return through the Stanford band", "choices": ["A five-lateral kickoff return through the Stanford band", "A 99-yard fumble recovery", "A blocked punt returned for a touchdown", "A Hail Mary pass into triple coverage"], "sport": "football", "difficulty": "hard"},
    {"q": "The 'Music City Miracle' in the 1999 AFC Wild Card game featured a lateral play by which team?", "a": "Tennessee Titans", "choices": ["Tennessee Titans", "Buffalo Bills", "Jacksonville Jaguars", "Miami Dolphins"], "sport": "football", "difficulty": "medium"},
    {"q": "In Super Bowl XLII, David Tyree's catch against his helmet while being tackled is known as what?", "a": "The Helmet Catch", "choices": ["The Helmet Catch", "The Miracle Grab", "The Impossible Catch", "The Super Snag"], "sport": "football", "difficulty": "easy"},
    {"q": "The 'Philly Special' trick play in Super Bowl LII featured which Eagles QB catching a touchdown pass?", "a": "Nick Foles", "choices": ["Nick Foles", "Carson Wentz", "Michael Vick", "Donovan McNabb"], "sport": "football", "difficulty": "easy"},
    {"q": "The 'Minneapolis Miracle' in the 2017 NFC Divisional round was a walk-off touchdown by which Vikings receiver?", "a": "Stefon Diggs", "choices": ["Stefon Diggs", "Adam Thielen", "Kyle Rudolph", "Laquon Treadwell"], "sport": "football", "difficulty": "medium"},
    {"q": "In the 1981 NFC Championship, Dwight Clark's leaping catch is famously known as what?", "a": "The Catch", "choices": ["The Catch", "The Reach", "The Grab", "The Leap"], "sport": "football", "difficulty": "easy"},
    {"q": "The 'Hail Flutie' was a last-second Hail Mary thrown by Doug Flutie while playing for which college?", "a": "Boston College", "choices": ["Boston College", "Notre Dame", "Miami", "Syracuse"], "sport": "football", "difficulty": "medium"},
    {"q": "The 'Sea of Hands' game in the 1974 AFC Divisional featured a dramatic last-minute catch by which Raiders player?", "a": "Clarence Davis", "choices": ["Clarence Davis", "Fred Biletnikoff", "Cliff Branch", "Dave Casper"], "sport": "football", "difficulty": "hard"},
    {"q": "In Super Bowl XLIII, which Steelers linebacker returned an interception 100 yards for a touchdown?", "a": "James Harrison", "choices": ["James Harrison", "LaMarr Woodley", "Troy Polamalu", "Lawrence Timmons"], "sport": "football", "difficulty": "medium"},
    {"q": "The 'Fail Mary' controversial call in 2012 occurred during a game officiated by whom?", "a": "Replacement referees", "choices": ["Replacement referees", "Ed Hochuli's crew", "Gene Steratore's crew", "Bill Vinovich's crew"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL play is nicknamed 'The Fumble,' occurring in the 1987 AFC Championship when Earnest Byner lost the ball?", "a": "Earnest Byner's goal-line fumble for the Cleveland Browns", "choices": ["Earnest Byner's goal-line fumble for the Cleveland Browns", "A botched snap in overtime", "A muffed punt return", "A lost fumble on a quarterback sneak"], "sport": "football", "difficulty": "hard"},
    {"q": "The 'Holy Roller' play in 1978 involved a controversial forward fumble by which Raiders quarterback?", "a": "Ken Stabler", "choices": ["Ken Stabler", "Jim Plunkett", "Daryle Lamonica", "David Humm"], "sport": "football", "difficulty": "hard"},
    {"q": "In the 2014 NFC Championship, the Seahawks overcame a 19-7 deficit against the Packers. What is this comeback known as?", "a": "The Collapse in Seattle", "choices": ["The Collapse in Seattle", "The Miracle at CenturyLink", "The 12th Man Rally", "The NFC Meltdown"], "sport": "football", "difficulty": "hard"},

    # --- Rule Facts (16-30) ---
    {"q": "In the NFL, how many points is a safety worth?", "a": "2", "choices": ["2", "1", "3", "6"], "sport": "football", "difficulty": "easy"},
    {"q": "What is the penalty in yards for pass interference in the NFL?", "a": "Spot of the foul", "choices": ["Spot of the foul", "15 yards", "10 yards", "Half the distance to the goal"], "sport": "football", "difficulty": "medium"},
    {"q": "How many timeouts does each NFL team get per half?", "a": "3", "choices": ["3", "2", "4", "5"], "sport": "football", "difficulty": "easy"},
    {"q": "In the NFL, how long is the play clock after a normal play?", "a": "40 seconds", "choices": ["40 seconds", "25 seconds", "30 seconds", "35 seconds"], "sport": "football", "difficulty": "medium"},
    {"q": "What is the NFL overtime period length in the regular season?", "a": "10 minutes", "choices": ["10 minutes", "15 minutes", "12 minutes", "5 minutes"], "sport": "football", "difficulty": "medium"},
    {"q": "In the NFL, what is the maximum number of players allowed on the field per team during a play?", "a": "11", "choices": ["11", "12", "10", "9"], "sport": "football", "difficulty": "easy"},
    {"q": "A touchback on a kickoff in the NFL places the ball at which yard line?", "a": "25-yard line", "choices": ["25-yard line", "20-yard line", "30-yard line", "15-yard line"], "sport": "football", "difficulty": "easy"},
    {"q": "How many downs does a team get to advance 10 yards for a first down in the NFL?", "a": "4", "choices": ["4", "3", "5", "2"], "sport": "football", "difficulty": "easy"},
    {"q": "In the NFL, a fair catch on a punt means the returner cannot do what?", "a": "Advance the ball after catching it", "choices": ["Advance the ball after catching it", "Call a timeout", "Signal for a new ball", "Request a replay review"], "sport": "football", "difficulty": "easy"},
    {"q": "What is the penalty for a false start in the NFL?", "a": "5 yards", "choices": ["5 yards", "10 yards", "15 yards", "Half the distance to the goal"], "sport": "football", "difficulty": "easy"},
    {"q": "In NFL rules, what happens if a game remains tied after the overtime period in the regular season?", "a": "The game ends in a tie", "choices": ["The game ends in a tie", "Another overtime is played", "A coin toss determines the winner", "The home team wins"], "sport": "football", "difficulty": "medium"},
    {"q": "What is the width of an NFL football field in feet?", "a": "160 feet", "choices": ["160 feet", "150 feet", "180 feet", "200 feet"], "sport": "football", "difficulty": "hard"},
    {"q": "In college football, where is the ball placed to start each overtime possession?", "a": "The opponent's 25-yard line", "choices": ["The opponent's 25-yard line", "The 50-yard line", "The opponent's 35-yard line", "The opponent's 20-yard line"], "sport": "football", "difficulty": "medium"},
    {"q": "In the NFL, how many challenges does a head coach receive per game (assuming none are lost)?", "a": "2", "choices": ["2", "3", "1", "Unlimited"], "sport": "football", "difficulty": "medium"},
    {"q": "What is the penalty for an illegal forward pass thrown from beyond the line of scrimmage?", "a": "5 yards and loss of down", "choices": ["5 yards and loss of down", "10 yards", "15 yards", "Turnover on downs"], "sport": "football", "difficulty": "hard"},

    # --- Stadium Facts (31-45) ---
    {"q": "Which NFL stadium is known as 'The Frozen Tundra'?", "a": "Lambeau Field", "choices": ["Lambeau Field", "Soldier Field", "Arrowhead Stadium", "Highmark Stadium"], "sport": "football", "difficulty": "easy"},
    {"q": "SoFi Stadium, which hosted Super Bowl LVI, is located in which California city?", "a": "Inglewood", "choices": ["Inglewood", "Los Angeles", "Pasadena", "Santa Clara"], "sport": "football", "difficulty": "medium"},
    {"q": "Which is the oldest continuously used NFL stadium?", "a": "Soldier Field", "choices": ["Soldier Field", "Lambeau Field", "Los Angeles Memorial Coliseum", "Wrigley Field"], "sport": "football", "difficulty": "hard"},
    {"q": "AT&T Stadium, home of the Dallas Cowboys, features a massive video screen. How long is it approximately?", "a": "160 feet", "choices": ["160 feet", "100 feet", "200 feet", "120 feet"], "sport": "football", "difficulty": "hard"},
    {"q": "MetLife Stadium in New Jersey is shared by which two NFL teams?", "a": "New York Giants and New York Jets", "choices": ["New York Giants and New York Jets", "Philadelphia Eagles and New York Giants", "New York Jets and Buffalo Bills", "New York Giants and New England Patriots"], "sport": "football", "difficulty": "easy"},
    {"q": "Arrowhead Stadium, famous for its crowd noise records, is home to which NFL team?", "a": "Kansas City Chiefs", "choices": ["Kansas City Chiefs", "Denver Broncos", "Las Vegas Raiders", "Los Angeles Chargers"], "sport": "football", "difficulty": "easy"},
    {"q": "Which NFL stadium has a retractable roof and a giant oculus opening, completed in 2020?", "a": "SoFi Stadium", "choices": ["SoFi Stadium", "Allegiant Stadium", "Mercedes-Benz Stadium", "U.S. Bank Stadium"], "sport": "football", "difficulty": "medium"},
    {"q": "The 'Loudest Crowd Roar' Guinness World Record was set at which NFL stadium in 2014?", "a": "CenturyLink Field (now Lumen Field)", "choices": ["CenturyLink Field (now Lumen Field)", "Arrowhead Stadium", "Lambeau Field", "Mercedes-Benz Superdome"], "sport": "football", "difficulty": "hard"},
    {"q": "Mercedes-Benz Stadium, home of the Atlanta Falcons, features what unique architectural element?", "a": "A retractable roof that opens like a camera aperture", "choices": ["A retractable roof that opens like a camera aperture", "An indoor waterfall", "A glass floor over an aquarium", "A rotating stage at midfield"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL team plays its home games at Highmark Stadium, known for extreme winter weather?", "a": "Buffalo Bills", "choices": ["Buffalo Bills", "Green Bay Packers", "Minnesota Vikings", "Chicago Bears"], "sport": "football", "difficulty": "easy"},
    {"q": "Allegiant Stadium, which opened in 2020, is the home of which NFL franchise?", "a": "Las Vegas Raiders", "choices": ["Las Vegas Raiders", "Arizona Cardinals", "Los Angeles Chargers", "Denver Broncos"], "sport": "football", "difficulty": "easy"},
    {"q": "Which stadium hosted the most Super Bowls as of 2024?", "a": "Hard Rock Stadium (Miami)", "choices": ["Hard Rock Stadium (Miami)", "Mercedes-Benz Superdome (New Orleans)", "Rose Bowl (Pasadena)", "AT&T Stadium (Arlington)"], "sport": "football", "difficulty": "hard"},
    {"q": "The 'Black Hole' was a famous fan section located in which NFL stadium?", "a": "Oakland-Alameda County Coliseum", "choices": ["Oakland-Alameda County Coliseum", "Allegiant Stadium", "Candlestick Park", "RingCentral Coliseum"], "sport": "football", "difficulty": "medium"},
    {"q": "U.S. Bank Stadium, home of the Minnesota Vikings, replaced which former venue?", "a": "Hubert H. Humphrey Metrodome", "choices": ["Hubert H. Humphrey Metrodome", "Metropolitan Stadium", "Target Field", "Mall of America Field"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL stadium sits at the highest elevation above sea level?", "a": "Empower Field at Mile High (Denver)", "choices": ["Empower Field at Mile High (Denver)", "State Farm Stadium (Glendale)", "Allegiant Stadium (Las Vegas)", "Levi's Stadium (Santa Clara)"], "sport": "football", "difficulty": "medium"},

    # --- Coaching Records (46-60) ---
    {"q": "Which NFL head coach holds the record for most career wins (regular season)?", "a": "Don Shula", "choices": ["Don Shula", "Bill Belichick", "George Halas", "Tom Landry"], "sport": "football", "difficulty": "medium"},
    {"q": "Bill Belichick's coaching career began as a special teams coach with which NFL team in 1975?", "a": "Baltimore Colts", "choices": ["Baltimore Colts", "Detroit Lions", "New York Giants", "Cleveland Browns"], "sport": "football", "difficulty": "hard"},
    {"q": "Which coach led the Miami Dolphins to the only perfect season (17-0) in NFL history in 1972?", "a": "Don Shula", "choices": ["Don Shula", "Jimmy Johnson", "Joe Robbie", "Howard Schnellenberger"], "sport": "football", "difficulty": "easy"},
    {"q": "Vince Lombardi, for whom the Super Bowl trophy is named, coached which NFL team?", "a": "Green Bay Packers", "choices": ["Green Bay Packers", "Washington Redskins", "New York Giants", "Dallas Cowboys"], "sport": "football", "difficulty": "easy"},
    {"q": "Which head coach won three Super Bowls with the Dallas Cowboys in the 1990s?", "a": "Jimmy Johnson and Barry Switzer", "choices": ["Jimmy Johnson and Barry Switzer", "Tom Landry", "Jimmy Johnson alone", "Bill Parcells"], "sport": "football", "difficulty": "hard"},
    {"q": "Andy Reid's first Super Bowl win as a head coach came with which team?", "a": "Kansas City Chiefs", "choices": ["Kansas City Chiefs", "Philadelphia Eagles", "Green Bay Packers", "St. Louis Rams"], "sport": "football", "difficulty": "easy"},
    {"q": "Which coach is famous for the quote 'Winning isn't everything; it's the only thing'?", "a": "Vince Lombardi", "choices": ["Vince Lombardi", "Bear Bryant", "Knute Rockne", "Bill Walsh"], "sport": "football", "difficulty": "easy"},
    {"q": "The 'West Coast Offense' is credited to which legendary 49ers head coach?", "a": "Bill Walsh", "choices": ["Bill Walsh", "George Seifert", "Steve Mariucci", "Mike Holmgren"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL head coach was known as 'Papa Bear' and co-founded the league?", "a": "George Halas", "choices": ["George Halas", "Curly Lambeau", "Paul Brown", "Art Rooney"], "sport": "football", "difficulty": "medium"},
    {"q": "Mike Tomlin became the youngest head coach to win a Super Bowl at age 36 with which team?", "a": "Pittsburgh Steelers", "choices": ["Pittsburgh Steelers", "Baltimore Ravens", "Tampa Bay Buccaneers", "Indianapolis Colts"], "sport": "football", "difficulty": "medium"},
    {"q": "Which coach led the Tampa Bay Buccaneers to their first Super Bowl victory in Super Bowl XXXVII?", "a": "Jon Gruden", "choices": ["Jon Gruden", "Tony Dungy", "Bruce Arians", "Raheem Morris"], "sport": "football", "difficulty": "medium"},
    {"q": "Tom Landry coached the Dallas Cowboys for how many consecutive seasons?", "a": "29", "choices": ["29", "25", "32", "20"], "sport": "football", "difficulty": "hard"},
    {"q": "Which college football coach holds the record for most national championships with 6?", "a": "Bear Bryant", "choices": ["Bear Bryant", "Nick Saban", "Woody Hayes", "Joe Paterno"], "sport": "football", "difficulty": "hard"},
    {"q": "Sean McVay became the youngest head coach in modern NFL history at what age?", "a": "30", "choices": ["30", "31", "32", "28"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL coach is known for his 'Run It Back' motto after winning Super Bowl LVII?", "a": "Andy Reid", "choices": ["Andy Reid", "Sean McVay", "Kyle Shanahan", "Mike Tomlin"], "sport": "football", "difficulty": "easy"},

    # --- Draft Trade Stories (61-75) ---
    {"q": "The 'Ricky Williams trade' in 1999 saw which team trade its entire draft to move up to pick Williams?", "a": "New Orleans Saints", "choices": ["New Orleans Saints", "Miami Dolphins", "Chicago Bears", "Cleveland Browns"], "sport": "football", "difficulty": "hard"},
    {"q": "In 2004, Eli Manning refused to play for which team that drafted him first overall, forcing a trade?", "a": "San Diego Chargers", "choices": ["San Diego Chargers", "Oakland Raiders", "Cleveland Browns", "Arizona Cardinals"], "sport": "football", "difficulty": "medium"},
    {"q": "The blockbuster 2012 trade that sent the #2 overall pick (Robert Griffin III) to Washington came from which team?", "a": "St. Louis Rams", "choices": ["St. Louis Rams", "Cleveland Browns", "Indianapolis Colts", "Minnesota Vikings"], "sport": "football", "difficulty": "hard"},
    {"q": "John Elway famously refused to play for which team that drafted him in 1983, forcing a trade to Denver?", "a": "Baltimore Colts", "choices": ["Baltimore Colts", "New York Jets", "Houston Oilers", "Tampa Bay Buccaneers"], "sport": "football", "difficulty": "medium"},
    {"q": "In the 2017 NFL Draft, which team traded up from #12 to #2 to select Mitchell Trubisky?", "a": "Chicago Bears", "choices": ["Chicago Bears", "San Francisco 49ers", "Kansas City Chiefs", "Houston Texans"], "sport": "football", "difficulty": "medium"},
    {"q": "The 'Herschel Walker trade' in 1989, considered the most lopsided in NFL history, benefited which team?", "a": "Dallas Cowboys", "choices": ["Dallas Cowboys", "Minnesota Vikings", "Green Bay Packers", "Philadelphia Eagles"], "sport": "football", "difficulty": "medium"},
    {"q": "In 2016, the Los Angeles Rams traded a massive haul of picks to move up to #1 and select which QB?", "a": "Jared Goff", "choices": ["Jared Goff", "Carson Wentz", "Dak Prescott", "Paxton Lynch"], "sport": "football", "difficulty": "medium"},
    {"q": "Bo Jackson was drafted #1 overall in 1986 by Tampa Bay but refused to play there, later joining which team?", "a": "Los Angeles Raiders", "choices": ["Los Angeles Raiders", "Kansas City Chiefs", "Cincinnati Bengals", "Seattle Seahawks"], "sport": "football", "difficulty": "medium"},
    {"q": "Which team drafted Tom Brady in the 6th round (199th overall) of the 2000 NFL Draft?", "a": "New England Patriots", "choices": ["New England Patriots", "San Francisco 49ers", "Detroit Lions", "Cleveland Browns"], "sport": "football", "difficulty": "easy"},
    {"q": "The 2018 NFL Draft saw the Cleveland Browns select which QB first overall?", "a": "Baker Mayfield", "choices": ["Baker Mayfield", "Sam Darnold", "Josh Allen", "Josh Rosen"], "sport": "football", "difficulty": "easy"},
    {"q": "In 1998, the Indianapolis Colts famously chose Peyton Manning over which other QB with the #1 pick?", "a": "Ryan Leaf", "choices": ["Ryan Leaf", "Tim Couch", "Donovan McNabb", "Daunte Culpepper"], "sport": "football", "difficulty": "medium"},
    {"q": "Which team traded up in the 2021 NFL Draft to select QB Trey Lance at #3 overall?", "a": "San Francisco 49ers", "choices": ["San Francisco 49ers", "Chicago Bears", "New York Jets", "Jacksonville Jaguars"], "sport": "football", "difficulty": "medium"},
    {"q": "The 2006 trade that sent Jay Cutler to Chicago involved a package of picks from which team?", "a": "Denver Broncos", "choices": ["Denver Broncos", "Green Bay Packers", "Detroit Lions", "Miami Dolphins"], "sport": "football", "difficulty": "hard"},
    {"q": "In the 1983 NFL Draft, six quarterbacks were taken in the first round. This draft class is often called what?", "a": "The Quarterback Class of '83", "choices": ["The Quarterback Class of '83", "The Golden Six", "The First-Round Frenzy", "The Signal-Caller Showcase"], "sport": "football", "difficulty": "hard"},
    {"q": "JaMarcus Russell, considered one of the biggest draft busts, was selected #1 overall by which team in 2007?", "a": "Oakland Raiders", "choices": ["Oakland Raiders", "Detroit Lions", "Cleveland Browns", "Miami Dolphins"], "sport": "football", "difficulty": "medium"},

    # --- Salary Cap History (76-85) ---
    {"q": "In what year did the NFL first implement a salary cap?", "a": "1994", "choices": ["1994", "1990", "1998", "2000"], "sport": "football", "difficulty": "hard"},
    {"q": "Which term describes when an NFL team restructures a contract to convert salary into a signing bonus?", "a": "Cap restructure", "choices": ["Cap restructure", "Cap rollover", "Cap floor", "Cap exemption"], "sport": "football", "difficulty": "hard"},
    {"q": "The NFL salary cap is primarily funded by which revenue source?", "a": "Television broadcast deals", "choices": ["Television broadcast deals", "Ticket sales", "Merchandise sales", "Sponsorship deals"], "sport": "football", "difficulty": "medium"},
    {"q": "'Dead money' in the NFL salary cap refers to what?", "a": "Cap charges from players no longer on the roster", "choices": ["Cap charges from players no longer on the roster", "Fines paid to the league", "Money reserved for injured players", "Unspent cap space from the previous year"], "sport": "football", "difficulty": "medium"},
    {"q": "Which team was penalized for salary cap violations in 2012, losing $36 million in cap space over two years?", "a": "Washington Redskins", "choices": ["Washington Redskins", "Dallas Cowboys", "New England Patriots", "Denver Broncos"], "sport": "football", "difficulty": "hard"},
    {"q": "The 'franchise tag' in the NFL allows teams to retain a player at what percentage of the top salaries at their position?", "a": "Average of the top 5 salaries", "choices": ["Average of the top 5 salaries", "120% of their previous salary", "The highest salary at their position", "Average of the top 10 salaries"], "sport": "football", "difficulty": "hard"},
    {"q": "What happens to unused salary cap space in the NFL at the end of a season?", "a": "It rolls over to the next year", "choices": ["It rolls over to the next year", "It is forfeited", "It is donated to charity", "It is redistributed among all teams"], "sport": "football", "difficulty": "medium"},
    {"q": "The 'transition tag' differs from the franchise tag in that it gives the original team what right?", "a": "Right of first refusal but no draft pick compensation", "choices": ["Right of first refusal but no draft pick compensation", "Two first-round draft picks as compensation", "The ability to void the contract", "An exclusive negotiating window of 60 days"], "sport": "football", "difficulty": "hard"},
    {"q": "The NFL's 'cap floor' requires teams to spend what minimum percentage of the salary cap?", "a": "89% over a four-year period", "choices": ["89% over a four-year period", "80% each season", "95% each season", "75% over a three-year period"], "sport": "football", "difficulty": "hard"},
    {"q": "Which QB became the first to sign a contract worth over $500 million in total value?", "a": "Patrick Mahomes", "choices": ["Patrick Mahomes", "Deshaun Watson", "Josh Allen", "Joe Burrow"], "sport": "football", "difficulty": "easy"},

    # --- Team Relocation History (86-100) ---
    {"q": "The Baltimore Ravens franchise was originally which team before relocating in 1996?", "a": "Cleveland Browns", "choices": ["Cleveland Browns", "Houston Oilers", "St. Louis Cardinals", "Baltimore Colts"], "sport": "football", "difficulty": "medium"},
    {"q": "The Indianapolis Colts infamously moved from which city in the middle of the night in 1984?", "a": "Baltimore", "choices": ["Baltimore", "Houston", "St. Louis", "Oakland"], "sport": "football", "difficulty": "medium"},
    {"q": "The Tennessee Titans were previously known as what team before relocating from Houston?", "a": "Houston Oilers", "choices": ["Houston Oilers", "Houston Texans", "Memphis Hound Dogs", "Nashville Kats"], "sport": "football", "difficulty": "medium"},
    {"q": "The Las Vegas Raiders moved from Oakland in 2020, but they also played in which city from 1982-1994?", "a": "Los Angeles", "choices": ["Los Angeles", "San Diego", "Sacramento", "San Francisco"], "sport": "football", "difficulty": "medium"},
    {"q": "The St. Louis Rams returned to which city in 2016, where the franchise had originally played?", "a": "Los Angeles", "choices": ["Los Angeles", "Cleveland", "San Francisco", "Chicago"], "sport": "football", "difficulty": "easy"},
    {"q": "Which NFL team moved from San Diego to Los Angeles in 2017?", "a": "Chargers", "choices": ["Chargers", "Raiders", "Rams", "Cardinals"], "sport": "football", "difficulty": "easy"},
    {"q": "The Arizona Cardinals franchise originally played in which city before multiple relocations?", "a": "Chicago", "choices": ["Chicago", "St. Louis", "Phoenix", "Baltimore"], "sport": "football", "difficulty": "hard"},
    {"q": "The Carolina Panthers and Jacksonville Jaguars both entered the NFL as expansion teams in what year?", "a": "1995", "choices": ["1995", "1993", "1996", "1998"], "sport": "football", "difficulty": "medium"},
    {"q": "After the original Cleveland Browns moved to Baltimore, Cleveland received a new expansion team in what year?", "a": "1999", "choices": ["1999", "1997", "2000", "2002"], "sport": "football", "difficulty": "hard"},
    {"q": "The Houston Texans became the NFL's newest franchise when they began play in what year?", "a": "2002", "choices": ["2002", "2000", "1999", "2004"], "sport": "football", "difficulty": "medium"},
    {"q": "Before moving to Tennessee, the Houston Oilers briefly played in which city for one season (1997)?", "a": "Memphis", "choices": ["Memphis", "Nashville", "Knoxville", "Chattanooga"], "sport": "football", "difficulty": "hard"},
    {"q": "Which AFL team became part of the NFL after the AFL-NFL merger in 1970 and is now the Kansas City Chiefs?", "a": "Dallas Texans", "choices": ["Dallas Texans", "Houston Oilers", "Boston Patriots", "Oakland Raiders"], "sport": "football", "difficulty": "hard"},
    {"q": "The New England Patriots were originally founded under what name?", "a": "Boston Patriots", "choices": ["Boston Patriots", "New England Colonials", "Bay State Patriots", "Boston Minutemen"], "sport": "football", "difficulty": "medium"},
    {"q": "Which city did the Rams play in before moving to St. Louis in 1995?", "a": "Los Angeles", "choices": ["Los Angeles", "Cleveland", "Anaheim", "San Diego"], "sport": "football", "difficulty": "medium"},
    {"q": "The NFL's longest continuously active franchise in the same city is which team?", "a": "Green Bay Packers", "choices": ["Green Bay Packers", "Chicago Bears", "New York Giants", "Pittsburgh Steelers"], "sport": "football", "difficulty": "medium"},

    # --- Uniform/Equipment Rules (101-115) ---
    {"q": "In the NFL, what is the allowed jersey number range for quarterbacks?", "a": "1-19", "choices": ["1-19", "1-9", "10-19", "1-49"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL rule change in 2021 allowed players at any position to wear single-digit numbers?", "a": "The jersey number expansion rule", "choices": ["The jersey number expansion rule", "The flex number rule", "The uniform modernization act", "The player expression rule"], "sport": "football", "difficulty": "hard"},
    {"q": "NFL players are required to have what visible on the back of their helmets?", "a": "A concussion warning label", "choices": ["A concussion warning label", "Their jersey number", "The NFL shield logo", "A medical alert symbol"], "sport": "football", "difficulty": "hard"},
    {"q": "What color must the chin strap of an NFL helmet be?", "a": "Any color matching the team's uniform", "choices": ["Any color matching the team's uniform", "White only", "Black only", "Team's primary color"], "sport": "football", "difficulty": "hard"},
    {"q": "The NFL mandates that all players wear what protective equipment on their legs?", "a": "Shin guards (knee and thigh pads are also required)", "choices": ["Shin guards (knee and thigh pads are also required)", "Only knee pads", "Ankle braces", "Compression sleeves only"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL team was the first to put a logo on their helmets?", "a": "Los Angeles Rams", "choices": ["Los Angeles Rams", "Dallas Cowboys", "Pittsburgh Steelers", "Green Bay Packers"], "sport": "football", "difficulty": "hard"},
    {"q": "The Cleveland Browns are notable for being one of the few NFL teams without what on their helmets?", "a": "A logo", "choices": ["A logo", "Face masks", "Chin straps", "Team colors"], "sport": "football", "difficulty": "easy"},
    {"q": "What is the NFL's rule about a player's jersey being tucked in during play?", "a": "Jerseys must be tucked in", "choices": ["Jerseys must be tucked in", "Jerseys can be untucked", "Only skill position players must tuck in", "There is no rule about tucking"], "sport": "football", "difficulty": "medium"},
    {"q": "In the NFL, towels worn by players must not exceed what length?", "a": "6 inches by 8 inches (official size)", "choices": ["6 inches by 8 inches (official size)", "12 inches by 12 inches", "18 inches by 18 inches", "No size restriction exists"], "sport": "football", "difficulty": "hard"},
    {"q": "Which piece of protective equipment became mandatory in the NFL starting in 2022 for certain positions?", "a": "Guardian Caps (soft-shell helmet covers) in practice", "choices": ["Guardian Caps (soft-shell helmet covers) in practice", "Rib protectors", "Neck rolls", "Hip pads"], "sport": "football", "difficulty": "hard"},
    {"q": "NFL footballs used in games must be inflated to what PSI range?", "a": "12.5 to 13.5 PSI", "choices": ["12.5 to 13.5 PSI", "10 to 11 PSI", "14 to 15 PSI", "11 to 12 PSI"], "sport": "football", "difficulty": "medium"},
    {"q": "The Pittsburgh Steelers are unique for displaying their logo on only which side of their helmet?", "a": "The right side", "choices": ["The right side", "The left side", "Both sides but different sizes", "The back of the helmet"], "sport": "football", "difficulty": "medium"},
    {"q": "What is the official weight range of an NFL football?", "a": "14 to 15 ounces", "choices": ["14 to 15 ounces", "12 to 13 ounces", "16 to 17 ounces", "11 to 12 ounces"], "sport": "football", "difficulty": "hard"},
    {"q": "NFL players are prohibited from wearing what type of face covering during games?", "a": "A full face shield without medical approval", "choices": ["A full face shield without medical approval", "A tinted visor at any time", "Any type of visor", "A half visor"], "sport": "football", "difficulty": "hard"},
    {"q": "The 'C' patch on an NFL player's jersey indicates what?", "a": "They are a team captain", "choices": ["They are a team captain", "They are in the Pro Football Hall of Fame", "They have been with the team 10+ years", "They are a community service award winner"], "sport": "football", "difficulty": "easy"},

    # --- Additional Football (116-125) ---
    {"q": "Which NFL field features a unique end zone design with a pirate ship that fires cannons after touchdowns?", "a": "Raymond James Stadium (Tampa Bay)", "choices": ["Raymond James Stadium (Tampa Bay)", "Hard Rock Stadium (Miami)", "TIAA Bank Field (Jacksonville)", "Mercedes-Benz Superdome (New Orleans)"], "sport": "football", "difficulty": "easy"},
    {"q": "In what year did the NFL officially adopt instant replay for the modern era?", "a": "1999", "choices": ["1999", "1986", "2004", "1992"], "sport": "football", "difficulty": "hard"},
    {"q": "The 'Tuck Rule' game in the 2001 playoffs involved Tom Brady and which opposing team?", "a": "Oakland Raiders", "choices": ["Oakland Raiders", "Pittsburgh Steelers", "Denver Broncos", "Miami Dolphins"], "sport": "football", "difficulty": "medium"},
    {"q": "Which NFL team has appeared in four consecutive Super Bowls from 1990-1993, losing all four?", "a": "Buffalo Bills", "choices": ["Buffalo Bills", "Minnesota Vikings", "Denver Broncos", "Dallas Cowboys"], "sport": "football", "difficulty": "easy"},
    {"q": "The 'Iron Curtain' was the nickname for which team's dominant 1970s defense?", "a": "Pittsburgh Steelers (Steel Curtain)", "choices": ["Pittsburgh Steelers (Steel Curtain)", "Dallas Cowboys (Doomsday Defense)", "Minnesota Vikings (Purple People Eaters)", "Chicago Bears (Monsters of the Midway)"], "sport": "football", "difficulty": "medium"},
    {"q": "What is the name of the Green Bay Packers' tradition where players ride kids' bicycles to training camp?", "a": "The Lambeau Bike Ride", "choices": ["The Lambeau Bike Ride", "The Cheesehead Cruise", "The Packers Pedal", "The Green Bay Roll"], "sport": "football", "difficulty": "medium"},
    {"q": "In the NFL, what is a 'Pick 6'?", "a": "An interception returned for a touchdown", "choices": ["An interception returned for a touchdown", "A 6th-round draft pick", "Six consecutive first downs", "A play involving six laterals"], "sport": "football", "difficulty": "easy"},
    {"q": "Which NFL rule, eliminated in 2023, previously prevented teams from using certain hip-drop tackling techniques?", "a": "The hip-drop tackle ban was adopted in 2024, not 2023", "choices": ["The hip-drop tackle ban was adopted in 2024, not 2023", "It was eliminated in the 2020 rule changes", "The horse-collar tackling rule replaced it", "There was never such a rule"], "sport": "football", "difficulty": "hard"},
    {"q": "The 'Dawg Pound' is the name for which NFL team's passionate fan section?", "a": "Cleveland Browns", "choices": ["Cleveland Browns", "Detroit Lions", "Carolina Panthers", "Jacksonville Jaguars"], "sport": "football", "difficulty": "easy"},
    {"q": "In the NFL, what does 'RPO' stand for in offensive playcalling?", "a": "Run-Pass Option", "choices": ["Run-Pass Option", "Right-side Pass Out", "Reverse Play Option", "Read-Play Offense"], "sport": "football", "difficulty": "medium"},

    # ==================
    # GOLF (89 questions)
    # ==================

    # --- Course Design Facts (1-15) ---
    {"q": "Augusta National's 12th hole, 'Golden Bell,' is famous for its difficulty due to swirling winds over what water hazard?", "a": "Rae's Creek", "choices": ["Rae's Creek", "Hogan's Bridge Pond", "Augusta Lake", "Magnolia Run"], "sport": "golf", "difficulty": "medium"},
    {"q": "The 'Road Hole' at St Andrews Old Course is which hole number?", "a": "17th", "choices": ["17th", "18th", "1st", "12th"], "sport": "golf", "difficulty": "medium"},
    {"q": "Pebble Beach Golf Links is situated along the coastline of which California area?", "a": "Monterey Peninsula", "choices": ["Monterey Peninsula", "Malibu Coast", "Big Sur", "San Francisco Bay"], "sport": "golf", "difficulty": "easy"},
    {"q": "The 'Island Green' is the signature 17th hole at which famous golf course?", "a": "TPC Sawgrass", "choices": ["TPC Sawgrass", "Augusta National", "Pebble Beach", "Pinehurst No. 2"], "sport": "golf", "difficulty": "easy"},
    {"q": "Augusta National Golf Club is known for naming its holes after what?", "a": "Flowers and trees", "choices": ["Flowers and trees", "Famous golfers", "Georgia cities", "Civil War battles"], "sport": "golf", "difficulty": "easy"},
    {"q": "Which Scottish course is considered the 'Home of Golf'?", "a": "St Andrews Old Course", "choices": ["St Andrews Old Course", "Muirfield", "Royal Troon", "Carnoustie"], "sport": "golf", "difficulty": "easy"},
    {"q": "Pine Valley Golf Club, often rated the #1 course in the world, is located in which U.S. state?", "a": "New Jersey", "choices": ["New Jersey", "South Carolina", "Georgia", "California"], "sport": "golf", "difficulty": "medium"},
    {"q": "The 'Church Pews' are famous bunkers located on which hole at Oakmont Country Club?", "a": "3rd and 4th holes", "choices": ["3rd and 4th holes", "17th hole", "12th hole", "1st hole"], "sport": "golf", "difficulty": "hard"},
    {"q": "Cypress Point Club's 16th hole requires a tee shot over the Pacific Ocean. What par is this hole?", "a": "Par 3", "choices": ["Par 3", "Par 4", "Par 5", "Par 2"], "sport": "golf", "difficulty": "medium"},
    {"q": "Which course is famous for its 'Hell Bunker' on the 14th hole, one of the deepest bunkers in golf?", "a": "St Andrews Old Course", "choices": ["St Andrews Old Course", "Royal St George's", "Carnoustie", "Muirfield"], "sport": "golf", "difficulty": "hard"},
    {"q": "The Postage Stamp is a famous par-3 hole at which Open Championship venue?", "a": "Royal Troon", "choices": ["Royal Troon", "Royal Birkdale", "Royal Liverpool", "Royal Lytham"], "sport": "golf", "difficulty": "medium"},
    {"q": "Whistling Straits, which hosted the 2021 Ryder Cup, was designed by which course architect?", "a": "Pete Dye", "choices": ["Pete Dye", "Jack Nicklaus", "Tom Fazio", "Robert Trent Jones Jr."], "sport": "golf", "difficulty": "medium"},
    {"q": "The Swilcan Bridge is an iconic landmark on which hole of the Old Course at St Andrews?", "a": "18th hole", "choices": ["18th hole", "1st hole", "17th hole", "9th hole"], "sport": "golf", "difficulty": "medium"},
    {"q": "Amen Corner at Augusta National refers to which three holes?", "a": "Holes 11, 12, and 13", "choices": ["Holes 11, 12, and 13", "Holes 1, 2, and 3", "Holes 15, 16, and 17", "Holes 6, 7, and 8"], "sport": "golf", "difficulty": "medium"},
    {"q": "Which famous course designer is known for creating Augusta National along with Bobby Jones?", "a": "Alister MacKenzie", "choices": ["Alister MacKenzie", "Donald Ross", "A.W. Tillinghast", "Seth Raynor"], "sport": "golf", "difficulty": "hard"},

    # --- Scoring Terminology (16-30) ---
    {"q": "In golf, what is the term for completing a hole in three strokes under par?", "a": "Albatross (or double eagle)", "choices": ["Albatross (or double eagle)", "Eagle", "Condor", "Ace"], "sport": "golf", "difficulty": "easy"},
    {"q": "What is the term for completing a hole in one stroke over par?", "a": "Bogey", "choices": ["Bogey", "Double bogey", "Par", "Birdie"], "sport": "golf", "difficulty": "easy"},
    {"q": "A 'condor' in golf refers to finishing a hole in how many strokes under par?", "a": "4 under par", "choices": ["4 under par", "3 under par", "5 under par", "2 under par"], "sport": "golf", "difficulty": "hard"},
    {"q": "What does the term 'scratch golfer' mean?", "a": "A golfer with a handicap of zero", "choices": ["A golfer with a handicap of zero", "A golfer who has never taken a lesson", "A golfer who plays barefoot", "A professional tournament golfer"], "sport": "golf", "difficulty": "medium"},
    {"q": "In golf scoring, what does 'GIR' stand for?", "a": "Green in Regulation", "choices": ["Green in Regulation", "Golf Impact Rating", "Gross Income Return", "Green Inspection Report"], "sport": "golf", "difficulty": "medium"},
    {"q": "What is a 'snowman' in golf slang?", "a": "A score of 8 on a single hole", "choices": ["A score of 8 on a single hole", "A score of 0", "Playing in winter conditions", "A white-colored golf ball"], "sport": "golf", "difficulty": "medium"},
    {"q": "In match play golf, what does 'dormie' mean?", "a": "Leading by as many holes as there are holes remaining", "choices": ["Leading by as many holes as there are holes remaining", "Being tied after 9 holes", "Losing by exactly one hole", "Winning the first three holes"], "sport": "golf", "difficulty": "hard"},
    {"q": "What is an 'ace' in golf?", "a": "A hole-in-one", "choices": ["A hole-in-one", "A score of one under par", "Winning a tournament by one stroke", "Hitting the fairway on every hole"], "sport": "golf", "difficulty": "easy"},
    {"q": "What is the meaning of 'up and down' in golf?", "a": "Getting the ball in the hole in two shots from off the green", "choices": ["Getting the ball in the hole in two shots from off the green", "Hitting the ball high and then low", "A round with alternating birdies and bogeys", "Playing well on the front nine and poorly on the back nine"], "sport": "golf", "difficulty": "medium"},
    {"q": "What does 'double bogey' mean in golf?", "a": "Two strokes over par on a hole", "choices": ["Two strokes over par on a hole", "Two birdies in a row", "Two penalty strokes", "Playing two rounds in one day"], "sport": "golf", "difficulty": "easy"},
    {"q": "In Stableford scoring, how many points is an eagle worth?", "a": "4 points", "choices": ["4 points", "3 points", "5 points", "2 points"], "sport": "golf", "difficulty": "hard"},
    {"q": "What does 'the cut' refer to in a golf tournament?", "a": "The score threshold to advance to the weekend rounds", "choices": ["The score threshold to advance to the weekend rounds", "Trimming the fairway grass", "A type of golf shot", "The halfway point of the final round"], "sport": "golf", "difficulty": "easy"},
    {"q": "What is a 'sandy' in golf?", "a": "Making par or better after hitting from a bunker", "choices": ["Making par or better after hitting from a bunker", "Landing in a sand trap", "A type of wedge club", "Playing on a desert course"], "sport": "golf", "difficulty": "medium"},
    {"q": "The term 'lip out' in golf refers to what?", "a": "A putt that circles the rim of the cup but doesn't fall in", "choices": ["A putt that circles the rim of the cup but doesn't fall in", "Hitting the ball off the edge of a bunker", "A shot that lands on the fringe", "A drive that hooks out of bounds"], "sport": "golf", "difficulty": "easy"},
    {"q": "What is a 'four-ball' format in golf?", "a": "Two teams of two players each, with the best individual score counting per hole", "choices": ["Two teams of two players each, with the best individual score counting per hole", "Four players competing individually", "Playing four holes at a time", "Using only four clubs per round"], "sport": "golf", "difficulty": "medium"},

    # --- Ryder Cup Stories (31-45) ---
    {"q": "The Ryder Cup is a competition between teams from which two regions?", "a": "Europe and the United States", "choices": ["Europe and the United States", "Europe and Asia", "North America and the Rest of the World", "The United Kingdom and the United States"], "sport": "golf", "difficulty": "easy"},
    {"q": "The 'Miracle at Medinah' in 2012 saw which team overcome a 10-6 deficit on the final day?", "a": "Europe", "choices": ["Europe", "United States", "Great Britain", "International"], "sport": "golf", "difficulty": "medium"},
    {"q": "The 'Battle of Brookline' in the 1999 Ryder Cup was controversial because of what American behavior on the 17th green?", "a": "Players and fans stormed the green prematurely after Justin Leonard's putt", "choices": ["Players and fans stormed the green prematurely after Justin Leonard's putt", "A player threw his putter into the crowd", "The team refused to shake hands", "A caddie was ejected for heckling"], "sport": "golf", "difficulty": "hard"},
    {"q": "The Ryder Cup is held every how many years?", "a": "Every 2 years", "choices": ["Every 2 years", "Every year", "Every 4 years", "Every 3 years"], "sport": "golf", "difficulty": "easy"},
    {"q": "Which iconic golfer captained the European team to a famous Ryder Cup victory at The Belfry in 1985?", "a": "Tony Jacklin", "choices": ["Tony Jacklin", "Seve Ballesteros", "Nick Faldo", "Bernhard Langer"], "sport": "golf", "difficulty": "hard"},
    {"q": "In the 1991 Ryder Cup at Kiawah Island, nicknamed 'The War on the Shore,' who missed the final putt for Europe?", "a": "Bernhard Langer", "choices": ["Bernhard Langer", "Nick Faldo", "Colin Montgomerie", "Ian Woosnam"], "sport": "golf", "difficulty": "hard"},
    {"q": "The Ryder Cup was originally a competition between the United States and which country before it expanded to all of Europe?", "a": "Great Britain", "choices": ["Great Britain", "Scotland", "Ireland", "England"], "sport": "golf", "difficulty": "medium"},
    {"q": "Which American team dominated the Ryder Cup from 1983 to 2008 with multiple decisive victories?", "a": "The U.S. did NOT dominate that period — Europe won most Ryder Cups from 1985-2012", "choices": ["The U.S. did NOT dominate that period — Europe won most Ryder Cups from 1985-2012", "The 1990s Dream Team", "Tiger's Army", "The American Resurgence"], "sport": "golf", "difficulty": "hard"},
    {"q": "At the 2018 Ryder Cup at Le Golf National in France, which team won convincingly by 7.5 points?", "a": "Europe", "choices": ["Europe", "United States", "The match was tied", "Europe won by only 1 point"], "sport": "golf", "difficulty": "medium"},
    {"q": "The 2021 Ryder Cup at Whistling Straits saw the U.S. team win by what record-tying margin?", "a": "19-9", "choices": ["19-9", "17-11", "15-13", "14.5-13.5"], "sport": "golf", "difficulty": "hard"},
    {"q": "Which golfer has earned the most career Ryder Cup points for Europe?", "a": "Sergio Garcia", "choices": ["Sergio Garcia", "Colin Montgomerie", "Nick Faldo", "Ian Poulter"], "sport": "golf", "difficulty": "hard"},
    {"q": "Ian Poulter earned what nickname for his intense Ryder Cup performances?", "a": "The Postman (because he always delivers)", "choices": ["The Postman (because he always delivers)", "The Lion", "Captain Europe", "Mr. Ryder Cup"], "sport": "golf", "difficulty": "medium"},
    {"q": "Samuel Ryder, who donated the Ryder Cup trophy, made his fortune selling what?", "a": "Seed packets", "choices": ["Seed packets", "Golf clubs", "Clothing", "Tobacco"], "sport": "golf", "difficulty": "hard"},
    {"q": "The Presidents Cup is the equivalent of the Ryder Cup but pits the United States against which group?", "a": "An International team (non-European players)", "choices": ["An International team (non-European players)", "A European team", "An Asian team", "A Commonwealth team"], "sport": "golf", "difficulty": "medium"},
    {"q": "At the 2023 Ryder Cup in Rome, which European captain led his team to a dominant home victory?", "a": "Luke Donald", "choices": ["Luke Donald", "Henrik Stenson", "Padraig Harrington", "Thomas Bjorn"], "sport": "golf", "difficulty": "medium"},

    # --- Famous Shot Descriptions (46-60) ---
    {"q": "Tiger Woods' chip-in on the 16th hole at Augusta in 2005 is famous for the ball doing what before dropping in?", "a": "Hanging on the lip of the cup for about two seconds", "choices": ["Hanging on the lip of the cup for about two seconds", "Bouncing off the flagstick twice", "Rolling backward uphill into the hole", "Curving around a bunker"], "sport": "golf", "difficulty": "medium"},
    {"q": "Phil Mickelson's famous 6-iron from the pine straw on the 13th at Augusta in 2010 narrowly avoided what?", "a": "Trees between him and the green", "choices": ["Trees between him and the green", "A water hazard directly in front", "An out-of-bounds fence", "A spectator standing in the fairway"], "sport": "golf", "difficulty": "hard"},
    {"q": "At the 1986 Masters, Jack Nicklaus won his 6th green jacket at what age, making him the oldest Masters winner?", "a": "46 years old", "choices": ["46 years old", "50 years old", "43 years old", "48 years old"], "sport": "golf", "difficulty": "medium"},
    {"q": "Gene Sarazen's 'Shot Heard Round the World' was a double eagle on which hole at Augusta in 1935?", "a": "15th hole", "choices": ["15th hole", "12th hole", "18th hole", "13th hole"], "sport": "golf", "difficulty": "hard"},
    {"q": "Tom Watson nearly won the 2009 Open Championship at age 59 at which course before losing in a playoff?", "a": "Turnberry", "choices": ["Turnberry", "St Andrews", "Royal Birkdale", "Carnoustie"], "sport": "golf", "difficulty": "hard"},
    {"q": "Tiger Woods' 'Better than most' putt at the 2019 Masters on the 18th green clinched his comeback. How many years had it been since his last major?", "a": "11 years", "choices": ["11 years", "8 years", "14 years", "5 years"], "sport": "golf", "difficulty": "medium"},
    {"q": "Jean Van de Velde's meltdown at the 1999 Open Championship at Carnoustie involved him standing where to hit his ball?", "a": "In the Barry Burn (a creek)", "choices": ["In the Barry Burn (a creek)", "On top of a stone wall", "In a hospitality tent", "On a cart path"], "sport": "golf", "difficulty": "hard"},
    {"q": "At the 1991 Masters, which player hit his approach into the water on the 12th hole in a playoff and lost to Ian Woosnam?", "a": "Tom Watson (actually it was not a playoff at 12; Woosnam won outright)", "choices": ["Tom Watson (actually it was not a playoff at 12; Woosnam won outright)", "Greg Norman", "Nick Faldo", "Seve Ballesteros"], "sport": "golf", "difficulty": "hard"},
    {"q": "Bubba Watson's remarkable hooked wedge shot from the trees on the 10th hole in a playoff won him which tournament in 2012?", "a": "The Masters", "choices": ["The Masters", "The U.S. Open", "The PGA Championship", "The Players Championship"], "sport": "golf", "difficulty": "medium"},
    {"q": "At the 2000 U.S. Open at Pebble Beach, Tiger Woods won by how many strokes — a record margin?", "a": "15 strokes", "choices": ["15 strokes", "12 strokes", "8 strokes", "10 strokes"], "sport": "golf", "difficulty": "medium"},
    {"q": "Larry Mize chipped in on the 11th hole in a sudden-death playoff at the 1987 Masters, defeating which favored golfer?", "a": "Greg Norman", "choices": ["Greg Norman", "Seve Ballesteros", "Tom Watson", "Nick Faldo"], "sport": "golf", "difficulty": "hard"},
    {"q": "Costantino Rocca's famous 60-foot birdie putt on the 18th at St Andrews in 1995 forced a playoff against whom?", "a": "John Daly", "choices": ["John Daly", "Tiger Woods", "Nick Faldo", "Greg Norman"], "sport": "golf", "difficulty": "hard"},
    {"q": "Sandy Lyle's famous bunker shot on the 18th hole to win the 1988 Masters made him the first player from which country to win a green jacket?", "a": "Scotland", "choices": ["Scotland", "England", "Ireland", "Wales"], "sport": "golf", "difficulty": "hard"},
    {"q": "At the 2013 Masters, Adam Scott became the first Australian to win. He sank a birdie putt on which playoff hole?", "a": "The 10th hole (second playoff hole)", "choices": ["The 10th hole (second playoff hole)", "The 18th hole", "The 15th hole", "The 12th hole"], "sport": "golf", "difficulty": "hard"},
    {"q": "Tiger Woods' 'Tiger Slam' — holding all four major trophies at once — was completed at which tournament in 2001?", "a": "The Masters", "choices": ["The Masters", "The U.S. Open", "The Open Championship", "The PGA Championship"], "sport": "golf", "difficulty": "medium"},

    # --- Caddie Facts (61-70) ---
    {"q": "What is the traditional role of a caddie in professional golf?", "a": "Carrying the player's bag and providing course strategy advice", "choices": ["Carrying the player's bag and providing course strategy advice", "Keeping score for the group", "Maintaining the golf course", "Coaching the player's swing"], "sport": "golf", "difficulty": "easy"},
    {"q": "Steve Williams, one of the most famous caddies, spent 13 years working for which golfer?", "a": "Tiger Woods", "choices": ["Tiger Woods", "Phil Mickelson", "Jack Nicklaus", "Ernie Els"], "sport": "golf", "difficulty": "easy"},
    {"q": "A caddie is allowed to do all of the following EXCEPT what during a competitive round?", "a": "Line up the player's putt by standing behind them on the putting green", "choices": ["Line up the player's putt by standing behind them on the putting green", "Suggest which club to use", "Read the green", "Clean the player's golf ball on the putting green"], "sport": "golf", "difficulty": "medium"},
    {"q": "At Augusta National during the Masters, what must all caddies traditionally wear?", "a": "White jumpsuits", "choices": ["White jumpsuits", "Green jackets", "Black pants and white shirts", "Team-branded polos"], "sport": "golf", "difficulty": "medium"},
    {"q": "Professional caddies typically earn what percentage of a player's tournament winnings?", "a": "5-10% (with 10% for a win)", "choices": ["5-10% (with 10% for a win)", "1-2%", "15-20%", "25%"], "sport": "golf", "difficulty": "medium"},
    {"q": "In professional golf, how many clubs is a player allowed to carry in their bag?", "a": "14", "choices": ["14", "12", "16", "10"], "sport": "golf", "difficulty": "easy"},
    {"q": "Bones Mackay caddied for which popular golfer for 25 years before moving on?", "a": "Phil Mickelson", "choices": ["Phil Mickelson", "Tiger Woods", "Dustin Johnson", "Rory McIlroy"], "sport": "golf", "difficulty": "medium"},
    {"q": "The word 'caddie' is believed to derive from which language?", "a": "French (from 'cadet')", "choices": ["French (from 'cadet')", "Scottish Gaelic", "Latin", "Dutch"], "sport": "golf", "difficulty": "hard"},
    {"q": "At the Masters, until what year were players required to use Augusta National's own caddies?", "a": "1983", "choices": ["1983", "1975", "1990", "1960"], "sport": "golf", "difficulty": "hard"},
    {"q": "What is a 'looper' in golf slang?", "a": "A caddie", "choices": ["A caddie", "A putt that circles the cup", "A hooked drive", "A player who plays multiple rounds"], "sport": "golf", "difficulty": "medium"},

    # --- Course Conditions & Equipment Rules (71-89) ---
    {"q": "The 'stimpmeter' is used to measure what on a golf course?", "a": "The speed of the greens", "choices": ["The speed of the greens", "Wind speed", "Soil moisture", "Fairway firmness"], "sport": "golf", "difficulty": "medium"},
    {"q": "What is the maximum number of clubs allowed in a golfer's bag during a competitive round?", "a": "14", "choices": ["14", "12", "16", "No limit"], "sport": "golf", "difficulty": "easy"},
    {"q": "In golf, what is a 'links' course characterized by?", "a": "Coastal terrain with sandy soil, few trees, and natural dunes", "choices": ["Coastal terrain with sandy soil, few trees, and natural dunes", "Heavily wooded fairways", "Mountain elevation changes", "Water hazards on every hole"], "sport": "golf", "difficulty": "easy"},
    {"q": "What type of grass is typically used on the greens at Augusta National?", "a": "Bentgrass", "choices": ["Bentgrass", "Bermuda grass", "Poa annua", "Fescue"], "sport": "golf", "difficulty": "hard"},
    {"q": "The USGA limits the maximum volume of a driver clubhead to how many cubic centimeters?", "a": "460cc", "choices": ["460cc", "400cc", "500cc", "350cc"], "sport": "golf", "difficulty": "medium"},
    {"q": "What is a 'preferred lie' or 'lift, clean, and place' rule in golf?", "a": "Allowing a player to pick up their ball in the fairway, clean it, and place it within a specified distance", "choices": ["Allowing a player to pick up their ball in the fairway, clean it, and place it within a specified distance", "Choosing the best angle for a tee shot", "Using a rangefinder to select targets", "Letting the caddie place the ball on the tee"], "sport": "golf", "difficulty": "medium"},
    {"q": "What is the minimum diameter of a regulation golf ball?", "a": "1.680 inches (42.67 mm)", "choices": ["1.680 inches (42.67 mm)", "1.500 inches", "1.750 inches", "2.000 inches"], "sport": "golf", "difficulty": "hard"},
    {"q": "Divots on a fairway should be repaired by doing what?", "a": "Replacing the divot or filling with a sand-seed mixture", "choices": ["Replacing the divot or filling with a sand-seed mixture", "Watering the spot immediately", "Leaving it for the grounds crew", "Covering it with a towel"], "sport": "golf", "difficulty": "easy"},
    {"q": "A 'ground under repair' area on a golf course is marked by what color?", "a": "Blue", "choices": ["Blue", "Red", "White", "Yellow"], "sport": "golf", "difficulty": "medium"},
    {"q": "What does the golf term 'rough' refer to?", "a": "The longer grass bordering the fairway", "choices": ["The longer grass bordering the fairway", "A sandy area near the green", "A water hazard", "An out-of-bounds area"], "sport": "golf", "difficulty": "easy"},
    {"q": "In professional golf, what is the penalty for grounding your club in a bunker before your swing (prior to 2019 rule change)?", "a": "Two-stroke penalty", "choices": ["Two-stroke penalty", "One-stroke penalty", "Disqualification", "Loss of hole in match play only"], "sport": "golf", "difficulty": "hard"},
    {"q": "What color stakes mark a lateral water hazard on a golf course?", "a": "Red", "choices": ["Red", "Yellow", "White", "Blue"], "sport": "golf", "difficulty": "easy"},
    {"q": "Yellow stakes on a golf course indicate what type of hazard?", "a": "Water hazard (regular)", "choices": ["Water hazard (regular)", "Lateral water hazard", "Out of bounds", "Ground under repair"], "sport": "golf", "difficulty": "easy"},
    {"q": "The maximum weight of a golf ball, as specified by the Rules of Golf, is how many ounces?", "a": "1.620 ounces (45.93 grams)", "choices": ["1.620 ounces (45.93 grams)", "2.000 ounces", "1.750 ounces", "1.500 ounces"], "sport": "golf", "difficulty": "hard"},
    {"q": "What is 'aeration' on a golf course?", "a": "Poking holes in the greens to allow air, water, and nutrients to reach the roots", "choices": ["Poking holes in the greens to allow air, water, and nutrients to reach the roots", "Spraying the fairways with fertilizer", "Trimming the rough to a uniform height", "Adding sand to bunkers"], "sport": "golf", "difficulty": "medium"},
    {"q": "The COR (Coefficient of Restitution) limit for a golf driver face is set at what maximum by the USGA?", "a": "0.830", "choices": ["0.830", "0.900", "0.750", "0.800"], "sport": "golf", "difficulty": "hard"},
    {"q": "What is the term for the closely mown area surrounding the putting green?", "a": "The fringe (or apron)", "choices": ["The fringe (or apron)", "The collar", "The rough cut", "The transition zone"], "sport": "golf", "difficulty": "easy"},
    {"q": "In the Rules of Golf, 'OB' (out of bounds) is typically marked by what color stakes?", "a": "White", "choices": ["White", "Red", "Yellow", "Blue"], "sport": "golf", "difficulty": "easy"},
    {"q": "What is the purpose of the 'grain' on a putting green?", "a": "It describes the direction the grass grows, affecting the speed and break of putts", "choices": ["It describes the direction the grass grows, affecting the speed and break of putts", "It indicates the firmness of the soil beneath", "It refers to the type of sand used in the soil mix", "It measures how recently the green was mowed"], "sport": "golf", "difficulty": "medium"},

    # ======================
    # BASEBALL (1 question)
    # ======================
    {"q": "Nolan Ryan holds the all-time MLB record for career strikeouts with how many?", "a": "5,714", "choices": ["5,714", "4,875", "5,243", "6,001"], "sport": "baseball", "difficulty": "medium"},
]

# Validate counts
football_count = sum(1 for q in NEW_QUESTIONS if q["sport"] == "football")
golf_count = sum(1 for q in NEW_QUESTIONS if q["sport"] == "golf")
baseball_count = sum(1 for q in NEW_QUESTIONS if q["sport"] == "baseball")

assert football_count == 125, f"Expected 125 football, got {football_count}"
assert golf_count == 89, f"Expected 89 golf, got {golf_count}"
assert baseball_count == 1, f"Expected 1 baseball, got {baseball_count}"
assert len(NEW_QUESTIONS) == 215, f"Expected 215 total, got {len(NEW_QUESTIONS)}"

print(f"Validated: {football_count} football, {golf_count} golf, {baseball_count} baseball = {len(NEW_QUESTIONS)} total")

# Wait 10 minutes before loading questions.json
print("Sleeping 600 seconds to avoid write conflicts...")
import sys
sys.stdout.flush()
time.sleep(600)
print("Done sleeping. Loading questions.json...")

# Load existing questions
with open("questions.json", "r") as f:
    existing = json.load(f)

print(f"Existing questions: {len(existing)}")

# Append new questions
existing.extend(NEW_QUESTIONS)

# Save
with open("questions.json", "w") as f:
    json.dump(existing, f, indent=2)

print(f"Total questions after append: {len(existing)}")
print("Batch 3 complete.")
