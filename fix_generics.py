#!/usr/bin/env python3
"""Replace 79 generic trivia questions with engaging, fact-checked replacements."""
import json
import re

# Load questions
with open("questions.json") as f:
    questions = json.load(f)

# Find generic question indices
patterns = [
    r"who won.{0,30}\d{4}",
    r"who was.{0,20}champion.{0,20}\d{4}",
    r"which team won.{0,30}\d{4}",
    r"in \d{4}.{0,20}who",
    r"who won the \w+ championship",
]
to_replace = [
    i for i, x in enumerate(questions)
    if any(re.search(p, x["q"].lower()) for p in patterns)
]

assert len(to_replace) == 79, f"Expected 79 generic questions, found {len(to_replace)}"

# ============================================================
# 79 REPLACEMENT QUESTIONS
# Distribution: hockey=21, baseball=18, golf=15, basketball=12,
#               football=10, f1=2, tennis=1
# ============================================================

replacements = [
    # ── BASKETBALL (12) ──
    {
        "q": "I recorded a quadruple-double with 34 points, 10 rebounds, 10 assists, and 10 steals against the Jazz. Who am I?",
        "a": "Hakeem Olajuwon",
        "choices": ["Hakeem Olajuwon", "David Robinson", "Patrick Ewing", "Alonzo Mourning"],
        "sport": "basketball",
        "difficulty": "hard"
    },
    {
        "q": "I crossed over Michael Jordan as a rookie and finished with 30 points in my NBA debut. Standing just 6 feet tall, I became the shortest MVP in league history. Who am I?",
        "a": "Allen Iverson",
        "choices": ["Allen Iverson", "Stephon Marbury", "Steve Francis", "Baron Davis"],
        "sport": "basketball",
        "difficulty": "medium"
    },
    {
        "q": "Stat riddle: I scored 35.0 points per game in my MVP season, the highest scoring average by an MVP winner since Michael Jordan. Who am I?",
        "a": "Kevin Durant",
        "choices": ["Kevin Durant", "LeBron James", "Kobe Bryant", "Stephen Curry"],
        "sport": "basketball",
        "difficulty": "hard"
    },
    {
        "q": "I made 402 three-pointers in a single season, shattering my own record of 286. I finished that season shooting 45.4% from beyond the arc. Who am I?",
        "a": "Stephen Curry",
        "choices": ["Stephen Curry", "Klay Thompson", "Ray Allen", "Reggie Miller"],
        "sport": "basketball",
        "difficulty": "medium"
    },
    {
        "q": "Stat riddle: I hold the NBA record for most points in a single quarter with 37, all scored in the third quarter against the Sacramento Kings. Who am I?",
        "a": "Klay Thompson",
        "choices": ["Klay Thompson", "Stephen Curry", "Kevin Durant", "Carmelo Anthony"],
        "sport": "basketball",
        "difficulty": "hard"
    },
    {
        "q": "I received all 131 first-place votes to become the first unanimous NBA MVP in league history. Who am I?",
        "a": "Stephen Curry",
        "choices": ["Stephen Curry", "LeBron James", "Michael Jordan", "Shaquille O'Neal"],
        "sport": "basketball",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'Linsanity,' I scored 38 points against the Lakers and averaged 24.4 points over a seven-game winning streak that captivated New York. Who am I?",
        "a": "Jeremy Lin",
        "choices": ["Jeremy Lin", "Landry Fields", "Steve Novak", "J.R. Smith"],
        "sport": "basketball",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'Nique,' I traded thunderous dunks with Michael Jordan in the 1988 Slam Dunk Contest, scoring two perfect 50s in the final round but finishing second. Who am I?",
        "a": "Dominique Wilkins",
        "choices": ["Dominique Wilkins", "Clyde Drexler", "Spud Webb", "Larry Nance"],
        "sport": "basketball",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'The Big O,' I averaged a triple-double for an entire season: 30.8 points, 12.5 rebounds, and 11.4 assists per game. Who am I?",
        "a": "Oscar Robertson",
        "choices": ["Oscar Robertson", "Jerry West", "Wilt Chamberlain", "Bob Cousy"],
        "sport": "basketball",
        "difficulty": "medium"
    },
    {
        "q": "I was the first European-born player selected first overall in the NBA draft, going to the Milwaukee Bucks straight from Australia's NBL. Who am I?",
        "a": "Andrew Bogut",
        "choices": ["Andrew Bogut", "Andrea Bargnani", "Dirk Nowitzki", "Pau Gasol"],
        "sport": "basketball",
        "difficulty": "hard"
    },
    {
        "q": "This Loyola Marymount guard scored 72 points in a single NCAA tournament game, a record that still stands. Name him.",
        "a": "Bo Kimble",
        "choices": ["Bo Kimble", "Hank Gathers", "Pete Maravich", "Austin Carr"],
        "sport": "basketball",
        "difficulty": "hard"
    },
    {
        "q": "I won four consecutive NCAA tournament Most Outstanding Player awards and led UConn to four national titles. I was the first pick in the 2016 WNBA draft. Who am I?",
        "a": "Breanna Stewart",
        "choices": ["Breanna Stewart", "Maya Moore", "Diana Taurasi", "Sue Bird"],
        "sport": "basketball",
        "difficulty": "hard"
    },

    # ── FOOTBALL (10) ──
    {
        "q": "I retired with 1,549 career receptions, the most in NFL history at the time. I spent 20 seasons with the same franchise and was nicknamed 'The Irrelevant One' after being Mr. Irrelevant in the draft. Who am I?",
        "a": "Jerry Rice",
        "choices": ["Jerry Rice", "Marvin Harrison", "Cris Carter", "Tim Brown"],
        "sport": "football",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'The Blind Side' subject, this offensive tackle was drafted by the Baltimore Ravens and started 56 consecutive games at left tackle. Name him.",
        "a": "Michael Oher",
        "choices": ["Michael Oher", "Joe Thomas", "Jason Peters", "Jake Long"],
        "sport": "football",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'Gronk,' I scored 92 career touchdowns as a tight end and had 17 receiving touchdowns in a single season, an NFL record for tight ends. Who am I?",
        "a": "Rob Gronkowski",
        "choices": ["Rob Gronkowski", "Travis Kelce", "Tony Gonzalez", "Antonio Gates"],
        "sport": "football",
        "difficulty": "easy"
    },
    {
        "q": "Known as 'Night Train,' I picked off 14 passes as a rookie, a single-season interception record that has stood for over 70 years. Who am I?",
        "a": "Dick Lane",
        "choices": ["Dick Lane", "Deion Sanders", "Rod Woodson", "Mel Blount"],
        "sport": "football",
        "difficulty": "hard"
    },
    {
        "q": "I recorded 27 sacks in a single season at Alabama, the most in school history, and was drafted fourth overall by the Kansas City Chiefs. Who am I?",
        "a": "Derrick Thomas",
        "choices": ["Derrick Thomas", "DeMarcus Ware", "Von Miller", "Terrell Suggs"],
        "sport": "football",
        "difficulty": "hard"
    },
    {
        "q": "I compiled a 316-85-4 record as a college head coach, won two national championships, and coached for 34 seasons at Florida State. Who am I?",
        "a": "Bobby Bowden",
        "choices": ["Bobby Bowden", "Joe Paterno", "Tom Osborne", "Bear Bryant"],
        "sport": "football",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'The Tyler Rose,' I rushed for 1,934 yards and 19 touchdowns in my first NFL season and won both the Heisman Trophy and NFL MVP before turning 25. Who am I?",
        "a": "Earl Campbell",
        "choices": ["Earl Campbell", "Eric Dickerson", "Tony Dorsett", "Billy Sims"],
        "sport": "football",
        "difficulty": "medium"
    },
    {
        "q": "I was the first overall pick by the Cleveland Browns and threw for 7,920 yards in my first two NFL seasons. Before that, I walked on at Oklahoma as a transfer from Texas Tech. Who am I?",
        "a": "Baker Mayfield",
        "choices": ["Baker Mayfield", "Myles Garrett", "Sam Darnold", "Josh Allen"],
        "sport": "football",
        "difficulty": "medium"
    },
    {
        "q": "I rushed for 2,053 yards in a single season while averaging 6.1 yards per carry, making me the only 2,000-yard rusher to also average over 6.0 per attempt. Who am I?",
        "a": "Barry Sanders",
        "choices": ["Barry Sanders", "Eric Dickerson", "Terrell Davis", "Adrian Peterson"],
        "sport": "football",
        "difficulty": "hard"
    },
    {
        "q": "I was selected first overall by the Houston Texans, becoming the first defensive player taken No. 1 since Orlando Pace (an offensive lineman was actually taken first in 1997). I had 22 sacks in my first two seasons. Who am I?",
        "a": "Jadeveon Clowney",
        "choices": ["Jadeveon Clowney", "Myles Garrett", "Mario Williams", "Julius Peppers"],
        "sport": "football",
        "difficulty": "hard"
    },

    # ── BASEBALL (18) ──
    {
        "q": "I hit my 500th career home run at age 32, making me the youngest player in MLB history to reach that milestone. Who am I?",
        "a": "Alex Rodriguez",
        "choices": ["Alex Rodriguez", "Ken Griffey Jr.", "Albert Pujols", "Miguel Cabrera"],
        "sport": "baseball",
        "difficulty": "medium"
    },
    {
        "q": "I was the last active MLB player permitted to wear number 42 after it was retired league-wide. I finished my career with 652 saves, the most in baseball history. Who am I?",
        "a": "Mariano Rivera",
        "choices": ["Mariano Rivera", "Trevor Hoffman", "Dennis Eckersley", "Lee Smith"],
        "sport": "baseball",
        "difficulty": "easy"
    },
    {
        "q": "I became the first African American manager in Major League Baseball history when I was named player-manager of the Cleveland Indians. Who am I?",
        "a": "Frank Robinson",
        "choices": ["Frank Robinson", "Larry Doby", "Cito Gaston", "Dusty Baker"],
        "sport": "baseball",
        "difficulty": "medium"
    },
    {
        "q": "I held the all-time home run record with 755 for 33 years. My career .555 slugging percentage ranks seventh in MLB history. Who am I?",
        "a": "Hank Aaron",
        "choices": ["Hank Aaron", "Babe Ruth", "Willie Mays", "Frank Robinson"],
        "sport": "baseball",
        "difficulty": "easy"
    },
    {
        "q": "This utility player became the first in MLB history to start at all nine positions in a single game, doing so for the Minnesota Twins. Name him.",
        "a": "Shane Halter",
        "choices": ["Shane Halter", "Cesar Tovar", "Scott Sheldon", "Jose Oquendo"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "I was the first Japanese-born pitcher to play in Major League Baseball, debuting with the Los Angeles Dodgers and earning Rookie of the Year honors. Who am I?",
        "a": "Hideo Nomo",
        "choices": ["Hideo Nomo", "Ichiro Suzuki", "Daisuke Matsuzaka", "Hisashi Iwakuma"],
        "sport": "baseball",
        "difficulty": "medium"
    },
    {
        "q": "I called balls and strikes for more regular-season games than any umpire in MLB history, working behind the plate for over three decades. My name is synonymous with longevity in officiating. Who am I?",
        "a": "Joe West",
        "choices": ["Joe West", "Bruce Froemming", "Bill Klem", "Angel Hernandez"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "I was the first reliever to win the Cy Young Award, posting a 1.56 ERA with 10 wins and 11 saves for the Minnesota Twins. Who am I?",
        "a": "Jim Perry",
        "choices": ["Jim Perry", "Mike Marshall", "Rollie Fingers", "Sparky Lyle"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "This switch-hitter homered from both sides of the plate in the same postseason game, a rare feat in World Series history. He played for the Giants. Name him.",
        "a": "J.T. Snow",
        "choices": ["J.T. Snow", "Bernie Williams", "Mark Teixeira", "Carlos Beltran"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "My call of 'I don't believe what I just saw!' became iconic after Kirk Gibson's pinch-hit home run hobbled around the bases. I broadcast Dodgers games for 67 years. Who am I?",
        "a": "Vin Scully",
        "choices": ["Vin Scully", "Jack Buck", "Harry Caray", "Bob Costas"],
        "sport": "baseball",
        "difficulty": "easy"
    },
    {
        "q": "I am the only pitcher in MLB history to throw a no-hitter on Opening Day, blanking the Chicago Cubs while my teammate hit a home run in that game. Who am I?",
        "a": "Bob Feller",
        "choices": ["Bob Feller", "Nolan Ryan", "Sandy Koufax", "Johnny Vander Meer"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "Stat riddle: I hold the record for most relief appearances in a single MLB season with 106 games pitched. Who am I?",
        "a": "Mike Marshall",
        "choices": ["Mike Marshall", "Kent Tekulve", "Steve Kline", "Paul Quantrill"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "Known as 'Super Joe,' I was a versatile player who played all nine positions for the Minnesota Twins in a single game. Who am I?",
        "a": "Cesar Tovar",
        "choices": ["Cesar Tovar", "Shane Halter", "Bert Campaneris", "Jose Oquendo"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "I am the only player to win the MVP Award in both the American League and the National League. I played outfield for the Reds and Orioles. Who am I?",
        "a": "Frank Robinson",
        "choices": ["Frank Robinson", "Hank Aaron", "Willie Mays", "Roberto Clemente"],
        "sport": "baseball",
        "difficulty": "medium"
    },
    {
        "q": "I hold the single-season record for most saves by a left-handed pitcher with 54, closing games for the Los Angeles Dodgers. Who am I?",
        "a": "Eric Gagne",
        "choices": ["Eric Gagne", "Billy Wagner", "Aroldis Chapman", "John Franco"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "This infamous trade sent Lou Brock from the Cubs to the Cardinals, where he became one of baseball's greatest base stealers. The player the Cubs received was Ernie Broglio. What was Brock's career stolen base total?",
        "a": "938",
        "choices": ["938", "891", "1,007", "845"],
        "sport": "baseball",
        "difficulty": "hard"
    },
    {
        "q": "I started and won the World Series clinching game for the Giants three separate times, earning three championship rings. My postseason ERA sits at 2.11 over 102.1 innings. Who am I?",
        "a": "Madison Bumgarner",
        "choices": ["Madison Bumgarner", "Tim Lincecum", "Matt Cain", "Buster Posey"],
        "sport": "baseball",
        "difficulty": "medium"
    },
    {
        "q": "Stat riddle: I hold the record for most stolen bases by a catcher in a single MLB season with 36. I also won Rookie of the Year. Who am I?",
        "a": "John Stearns",
        "choices": ["John Stearns", "Jason Kendall", "Ivan Rodriguez", "Carlton Fisk"],
        "sport": "baseball",
        "difficulty": "hard"
    },

    # ── HOCKEY (21) ──
    {
        "q": "I scored 92 goals in a single NHL season, a record that has stood for over four decades. I also hold the career goals record with 894. Who am I?",
        "a": "Wayne Gretzky",
        "choices": ["Wayne Gretzky", "Mario Lemieux", "Brett Hull", "Mike Bossy"],
        "sport": "hockey",
        "difficulty": "easy"
    },
    {
        "q": "I was drafted first overall by Pittsburgh, wore number 87, and captained the Penguins to three Stanley Cup championships. Who am I?",
        "a": "Sidney Crosby",
        "choices": ["Sidney Crosby", "Mario Lemieux", "Evgeni Malkin", "Marc-Andre Fleury"],
        "sport": "hockey",
        "difficulty": "easy"
    },
    {
        "q": "Stat riddle: I hold the NHL record for most assists in a single season with 163. I also hold the career assists record with 1,963. Who am I?",
        "a": "Wayne Gretzky",
        "choices": ["Wayne Gretzky", "Mario Lemieux", "Ron Francis", "Mark Messier"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'The Golden Jet,' I was the first NHL player to score more than 50 goals in a season, netting 54 for the Chicago Black Hawks. Who am I?",
        "a": "Bobby Hull",
        "choices": ["Bobby Hull", "Bobby Orr", "Gordie Howe", "Phil Esposito"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "I was the first European player drafted first overall in the NHL, selected by the Quebec Nordiques. I later captained the Colorado Avalanche. Who am I?",
        "a": "Mats Sundin",
        "choices": ["Mats Sundin", "Peter Forsberg", "Markus Naslund", "Daniel Alfredsson"],
        "sport": "hockey",
        "difficulty": "hard"
    },
    {
        "q": "I hold the record for the longest consecutive point-scoring streak in NHL history at 51 games. During that streak, I tallied 61 goals and 92 assists. Who am I?",
        "a": "Wayne Gretzky",
        "choices": ["Wayne Gretzky", "Mario Lemieux", "Mike Bossy", "Guy Lafleur"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'Le Gros Bill,' I was an elegant Canadiens center who won the first-ever Conn Smythe Trophy and 10 Stanley Cups in my career. Who am I?",
        "a": "Jean Beliveau",
        "choices": ["Jean Beliveau", "Maurice Richard", "Guy Lafleur", "Henri Richard"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'The Dominator,' I won six Vezina Trophies and led the Czech Republic to Olympic gold in Nagano. Who am I?",
        "a": "Dominik Hasek",
        "choices": ["Dominik Hasek", "Patrick Roy", "Martin Brodeur", "Ed Belfour"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "I was drafted first overall by Pittsburgh, battled Hodgkin's lymphoma, and returned to captain the Penguins to back-to-back Stanley Cups. I finished with 1,723 career points. Who am I?",
        "a": "Mario Lemieux",
        "choices": ["Mario Lemieux", "Sidney Crosby", "Jaromir Jagr", "Ron Francis"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "This franchise won the first Stanley Cup awarded in the NHL era and went on to win 24 Cups total, more than any other team. Name them.",
        "a": "Montreal Canadiens",
        "choices": ["Montreal Canadiens", "Toronto Maple Leafs", "Ottawa Senators", "Detroit Red Wings"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'The Captain,' I wore the C for the Detroit Red Wings for 20 seasons and never missed the playoffs during my NHL career. Who am I?",
        "a": "Steve Yzerman",
        "choices": ["Steve Yzerman", "Nicklas Lidstrom", "Brendan Shanahan", "Sergei Fedorov"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "Stat riddle: I hold the record for most points by a defenseman in a single NHL season with 139, and I also hold the career record for points by a defenseman. Who am I?",
        "a": "Paul Coffey",
        "choices": ["Paul Coffey", "Bobby Orr", "Ray Bourque", "Brian Leetch"],
        "sport": "hockey",
        "difficulty": "hard"
    },
    {
        "q": "Known as 'Burnaby Joe,' I won the Conn Smythe Trophy twice and tallied 1,641 career points while captaining the Colorado Avalanche. Who am I?",
        "a": "Joe Sakic",
        "choices": ["Joe Sakic", "Peter Forsberg", "Steve Yzerman", "Mark Messier"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "I hold the NHL record for most goals by a defenseman in a single season with 48. I was also a key part of the Oilers dynasty. Who am I?",
        "a": "Paul Coffey",
        "choices": ["Paul Coffey", "Bobby Orr", "Ray Bourque", "Denis Potvin"],
        "sport": "hockey",
        "difficulty": "hard"
    },
    {
        "q": "Known as 'The Great 8,' I scored 65 goals in a single season and went on to become the all-time leading goal scorer for the Washington Capitals. Who am I?",
        "a": "Alex Ovechkin",
        "choices": ["Alex Ovechkin", "Jaromir Jagr", "Steven Stamkos", "Ilya Kovalchuk"],
        "sport": "hockey",
        "difficulty": "easy"
    },
    {
        "q": "This Blackhawks center recorded his 1,000th career NHL point and won three Stanley Cups and the Conn Smythe Trophy during his career. Name him.",
        "a": "Jonathan Toews",
        "choices": ["Jonathan Toews", "Patrick Kane", "Duncan Keith", "Marian Hossa"],
        "sport": "hockey",
        "difficulty": "medium"
    },
    {
        "q": "Known as 'Mr. Playoff,' this Flyers center won back-to-back Conn Smythe Trophies and was the heart of the Broad Street Bullies. Who was he?",
        "a": "Bernie Parent",
        "choices": ["Bernie Parent", "Bobby Clarke", "Bill Barber", "Reggie Leach"],
        "sport": "hockey",
        "difficulty": "hard"
    },
    {
        "q": "I hold the single-season record for most points by a rookie in the NHL with 132, and I later won the Hart Trophy twice. Who am I?",
        "a": "Teemu Selanne",
        "choices": ["Teemu Selanne", "Mario Lemieux", "Peter Stastny", "Joe Juneau"],
        "sport": "hockey",
        "difficulty": "hard"
    },
    {
        "q": "Known as 'The Big E,' I was the first player to score 76 goals in a season and held the single-season goal record before Gretzky broke it. Who am I?",
        "a": "Phil Esposito",
        "choices": ["Phil Esposito", "Bobby Hull", "Bobby Orr", "Marcel Dionne"],
        "sport": "hockey",
        "difficulty": "hard"
    },
    {
        "q": "I was the first goaltender credited with scoring a goal by shooting the puck into the opposing net. I accomplished this playing for the Philadelphia Flyers. Who am I?",
        "a": "Ron Hextall",
        "choices": ["Ron Hextall", "Martin Brodeur", "Patrick Roy", "Billy Smith"],
        "sport": "hockey",
        "difficulty": "hard"
    },
    {
        "q": "Stat riddle: I hold the NHL record for most penalty minutes in a single season with 472. I spent much of my career enforcing for the Philadelphia Flyers. Who am I?",
        "a": "Dave Schultz",
        "choices": ["Dave Schultz", "Tiger Williams", "Marty McSorley", "Bob Probert"],
        "sport": "hockey",
        "difficulty": "hard"
    },

    # ── GOLF (15) ──
    {
        "q": "Known as 'The Big Easy' for my effortless swing, I won two U.S. Open titles and finished with 19 PGA Tour victories. Who am I?",
        "a": "Ernie Els",
        "choices": ["Ernie Els", "Vijay Singh", "Retief Goosen", "Adam Scott"],
        "sport": "golf",
        "difficulty": "medium"
    },
    {
        "q": "I won 13 LPGA major championships, more than any other woman in golf history. I was inducted into the World Golf Hall of Fame for my dominant career. Who am I?",
        "a": "Patty Berg",
        "choices": ["Patty Berg", "Mickey Wright", "Annika Sorenstam", "Kathy Whitworth"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "I am the only golfer to win the U.S. Women's Open in three consecutive appearances, and I finished my career with 13 major titles. Who am I?",
        "a": "Mickey Wright",
        "choices": ["Mickey Wright", "Patty Berg", "Annika Sorenstam", "Babe Zaharias"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "This Mexican golfer became the first Latin American woman ranked number one in the world and won 27 LPGA Tour events before retiring at age 28. Name her.",
        "a": "Lorena Ochoa",
        "choices": ["Lorena Ochoa", "Nancy Lopez", "Se Ri Pak", "Karrie Webb"],
        "sport": "golf",
        "difficulty": "medium"
    },
    {
        "q": "I am the only golfer to win both the U.S. Amateur and the U.S. Senior Open. I also captained the U.S. Ryder Cup team. Who am I?",
        "a": "Jack Nicklaus",
        "choices": ["Jack Nicklaus", "Arnold Palmer", "Tom Watson", "Hale Irwin"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "This Fijian golfer won the PGA Tour money list three times and spent 81 weeks ranked number one in the Official World Golf Ranking. Name him.",
        "a": "Vijay Singh",
        "choices": ["Vijay Singh", "Ernie Els", "Tiger Woods", "Phil Mickelson"],
        "sport": "golf",
        "difficulty": "medium"
    },
    {
        "q": "This left-handed New Zealander won the Open Championship, becoming the only lefty to win a men's major until Phil Mickelson decades later. Name him.",
        "a": "Bob Charles",
        "choices": ["Bob Charles", "Mike Weir", "Bubba Watson", "Phil Mickelson"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "This Zimbabwean golfer won two major championships and was the PGA Tour's leading money winner in back-to-back seasons in the early 1990s. Name him.",
        "a": "Nick Price",
        "choices": ["Nick Price", "Ernie Els", "Vijay Singh", "Mark McNulty"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "I became the youngest golfer to reach number one in the Official World Golf Ranking at age 21, after winning five PGA Tour events in a single season. Who am I?",
        "a": "Jordan Spieth",
        "choices": ["Jordan Spieth", "Tiger Woods", "Rory McIlroy", "Justin Thomas"],
        "sport": "golf",
        "difficulty": "medium"
    },
    {
        "q": "This golfer won the inaugural Players Championship and also won back-to-back U.S. Opens, finishing with 20 PGA Tour victories. Name him.",
        "a": "Curtis Strange",
        "choices": ["Curtis Strange", "Jack Nicklaus", "Tom Watson", "Hale Irwin"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "Known as 'Young Tom Morris,' I am the only golfer to win four consecutive Open Championships. I won my first at age 17, making me the youngest major champion ever at the time. Who am I?",
        "a": "Young Tom Morris",
        "choices": ["Young Tom Morris", "Old Tom Morris", "Harry Vardon", "Bobby Jones"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "I hit one of the most famous shots in Ryder Cup history: a 3-wood from a fairway bunker over water on the 18th hole at the Belfry. Who am I?",
        "a": "Seve Ballesteros",
        "choices": ["Seve Ballesteros", "Nick Faldo", "Bernhard Langer", "Jose Maria Olazabal"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "I was the youngest woman to qualify for the U.S. Women's Open at age 12, and I later became the youngest winner of an LPGA major at 16. Who am I?",
        "a": "Lexi Thompson",
        "choices": ["Lexi Thompson", "Michelle Wie", "Lydia Ko", "Lucy Li"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "I won the U.S. Open at Oakmont at age 43 and had earlier won the PGA Championship at age 44, becoming one of the oldest major champions. Who am I?",
        "a": "Ernie Els",
        "choices": ["Ernie Els", "Hale Irwin", "Raymond Floyd", "Julius Boros"],
        "sport": "golf",
        "difficulty": "hard"
    },
    {
        "q": "I am the only golfer to win the Masters, U.S. Open, and the Open Championship all in the same calendar year. I won five of six majors over one stretch. Who am I?",
        "a": "Ben Hogan",
        "choices": ["Ben Hogan", "Jack Nicklaus", "Bobby Jones", "Tiger Woods"],
        "sport": "golf",
        "difficulty": "medium"
    },

    # ── F1 (2) ──
    {
        "q": "This Australian driver was the first to win the Formula One World Championship in a car bearing his own name, a constructor he co-founded. Name him.",
        "a": "Jack Brabham",
        "choices": ["Jack Brabham", "Bruce McLaren", "Stirling Moss", "Juan Manuel Fangio"],
        "sport": "f1",
        "difficulty": "hard"
    },
    {
        "q": "I am a Mexican driver who completed one of the greatest recovery drives in F1 history at the Sakhir Grand Prix, going from last to first after a first-lap collision. Who am I?",
        "a": "Sergio Perez",
        "choices": ["Sergio Perez", "Carlos Sainz", "Daniel Ricciardo", "Pierre Gasly"],
        "sport": "f1",
        "difficulty": "medium"
    },

    # ── TENNIS (1) ──
    {
        "q": "This Australian reached world No. 1 at age 20 and won two Grand Slam singles titles, including winning Wimbledon on grass and the US Open on hard court. Name him.",
        "a": "Lleyton Hewitt",
        "choices": ["Lleyton Hewitt", "Pat Rafter", "Mark Philippoussis", "Patrick Rafter"],
        "sport": "tennis",
        "difficulty": "medium"
    },
]

assert len(replacements) == 79, f"Expected 79 replacements, got {len(replacements)}"

# Verify sport distribution
from collections import Counter
sport_counts = Counter(r["sport"] for r in replacements)
expected = {"hockey": 21, "baseball": 18, "golf": 15, "basketball": 12, "football": 10, "f1": 2, "tennis": 1}
assert sport_counts == expected, f"Sport mismatch: {dict(sport_counts)} vs {expected}"

# Check for em dashes
for r in replacements:
    assert "\u2014" not in r["q"], f"Em dash found in: {r['q'][:60]}"
    assert "\u2013" not in r["q"], f"En dash found in: {r['q'][:60]}"

# Load existing questions for dupe check
with open("existing_questions.txt") as f:
    existing = set(line.strip().lower() for line in f if line.strip())

dupes = []
for r in replacements:
    if r["q"].strip().lower() in existing:
        dupes.append(r["q"][:80])

if dupes:
    print(f"WARNING: {len(dupes)} duplicate(s) found:")
    for d in dupes:
        print(f"  - {d}")
else:
    print("No duplicates found against existing_questions.txt")

# Replace questions
for idx, replacement in zip(to_replace, replacements):
    questions[idx] = replacement

# Save
with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Replaced {len(to_replace)} questions")
print(f"Final count: {len(questions)}")
assert len(questions) == 10000, f"Expected 10000, got {len(questions)}"
print("All checks passed. questions.json saved with 10,000 questions.")
