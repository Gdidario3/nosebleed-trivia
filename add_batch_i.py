import json

new_questions = [
# ── NBA HISTORY 1950s-1980s ──
{"q":"Who was the NBA's first African-American player?","a":"Earl Lloyd (1950)","choices":["Earl Lloyd (1950)","Chuck Cooper","Nat Clifton","Don Barksdale"],"sport":"basketball","difficulty":"hard"},
{"q":"Which team won the first BAA (later NBA) championship in 1947?","a":"Philadelphia Warriors","choices":["Philadelphia Warriors","Chicago Stags","Boston Celtics","St. Louis Bombers"],"sport":"basketball","difficulty":"hard"},
{"q":"Who won the NBA scoring title in 1972-73?","a":"Nate Archibald (34.0 ppg)","choices":["Nate Archibald (34.0 ppg)","Kareem Abdul-Jabbar","Pete Maravich","Spencer Haywood"],"sport":"basketball","difficulty":"hard"},
{"q":"Which team did Julius Erving (Dr. J) spend most of his NBA career with?","a":"Philadelphia 76ers","choices":["Philadelphia 76ers","New York Nets","Atlanta Hawks","Boston Celtics"],"sport":"basketball","difficulty":"medium"},
{"q":"What year was the NBA's three-point shooting contest introduced at All-Star Weekend?","a":"1986","choices":["1986","1979","1990","1983"],"sport":"basketball","difficulty":"hard"},
{"q":"Who won the NBA MVP in 1986?","a":"Larry Bird","choices":["Larry Bird","Magic Johnson","Kareem Abdul-Jabbar","Julius Erving"],"sport":"basketball","difficulty":"medium"},
{"q":"Which player was nicknamed 'Pistol Pete'?","a":"Pete Maravich","choices":["Pete Maravich","Jerry West","Billy Cunningham","Earl Monroe"],"sport":"basketball","difficulty":"medium"},
{"q":"What year did the Boston Celtics win their last championship of the Russell era?","a":"1969","choices":["1969","1966","1971","1973"],"sport":"basketball","difficulty":"hard"},
{"q":"Who won the NBA MVP in 1967?","a":"Wilt Chamberlain","choices":["Wilt Chamberlain","Bill Russell","Jerry West","Oscar Robertson"],"sport":"basketball","difficulty":"hard"},
{"q":"Which NBA franchise was originally from Rochester?","a":"Sacramento Kings (originally Rochester Royals)","choices":["Sacramento Kings (originally Rochester Royals)","Los Angeles Clippers","Indiana Pacers","New Orleans Pelicans"],"sport":"basketball","difficulty":"hard"},
{"q":"Who scored 100 points on March 2, 1962?","a":"Wilt Chamberlain","choices":["Wilt Chamberlain","Elgin Baylor","Bob Pettit","Jerry West"],"sport":"basketball","difficulty":"easy"},
{"q":"What franchise did Moses Malone win his MVP with in 1983?","a":"Philadelphia 76ers","choices":["Philadelphia 76ers","Houston Rockets","Washington Bullets","Atlanta Hawks"],"sport":"basketball","difficulty":"medium"},
{"q":"Who won the NBA Finals MVP in 1980?","a":"Magic Johnson","choices":["Magic Johnson","Kareem Abdul-Jabbar","Jamaal Wilkes","Michael Cooper"],"sport":"basketball","difficulty":"hard"},
{"q":"Which player led the NBA in assists during the 1979-80 season?","a":"Norm Nixon","choices":["Norm Nixon","Magic Johnson","John Lucas","Foots Walker"],"sport":"basketball","difficulty":"hard"},
{"q":"What team won the ABA championship in 1975?","a":"Kentucky Colonels","choices":["Kentucky Colonels","New York Nets","Denver Nuggets","Indiana Pacers"],"sport":"basketball","difficulty":"hard"},

# ── NFL HISTORY 1950s-1980s ──
{"q":"Who was the quarterback of the famous 'Greatest Game Ever Played' in 1958?","a":"Johnny Unitas (Baltimore Colts)","choices":["Johnny Unitas (Baltimore Colts)","Charlie Conerly","Y.A. Tittle","Bobby Layne"],"sport":"football","difficulty":"hard"},
{"q":"Which team did Paul Brown found and coach in the NFL?","a":"Cleveland Browns (and later Cincinnati Bengals)","choices":["Cleveland Browns (and later Cincinnati Bengals)","Baltimore Colts","Chicago Bears","Green Bay Packers"],"sport":"football","difficulty":"hard"},
{"q":"Who was the first quarterback to throw for 4,000 yards in an NFL season?","a":"Joe Namath (4,007 yards in 1967)","choices":["Joe Namath (4,007 yards in 1967)","Fran Tarkenton","Dan Fouts","Roger Staubach"],"sport":"football","difficulty":"hard"},
{"q":"Which team did Johnny Unitas play for?","a":"Baltimore Colts (mainly)","choices":["Baltimore Colts (mainly)","Pittsburgh Steelers","Cleveland Browns","New York Giants"],"sport":"football","difficulty":"medium"},
{"q":"Who was the first player selected in the first NFL Draft in 1936?","a":"Jay Berwanger (never played)","choices":["Jay Berwanger (never played)","Bronko Nagurski","Don Hutson","Sammy Baugh"],"sport":"football","difficulty":"hard"},
{"q":"Which team won Super Bowl VI in 1972?","a":"Dallas Cowboys","choices":["Dallas Cowboys","Miami Dolphins","Washington Redskins","Minnesota Vikings"],"sport":"football","difficulty":"hard"},
{"q":"Who quarterbacked the Miami Dolphins through their perfect 17-0 season in 1972?","a":"Bob Griese","choices":["Bob Griese","Earl Morrall","Dan Marino","Don Strock"],"sport":"football","difficulty":"hard"},
{"q":"Which NFL team was originally called the Decatur Staleys?","a":"Chicago Bears","choices":["Chicago Bears","Green Bay Packers","Cleveland Browns","Detroit Lions"],"sport":"football","difficulty":"hard"},
{"q":"Who won the MVP of Super Bowl III?","a":"Joe Namath","choices":["Joe Namath","Don Maynard","Matt Snell","George Sauer"],"sport":"football","difficulty":"medium"},
{"q":"Which running back was nicknamed 'The Kansas Comet'?","a":"Gale Sayers","choices":["Gale Sayers","O.J. Simpson","Lenny Moore","Hugh McElhenny"],"sport":"football","difficulty":"hard"},

# ── NHL HISTORY 1920s-1960s ──
{"q":"Who was the first player to score 50 goals in one NHL season?","a":"Maurice Richard (1944-45)","choices":["Maurice Richard (1944-45)","Gordie Howe","Bobby Hull","Boom Boom Geoffrion"],"sport":"hockey","difficulty":"hard"},
{"q":"Which team won the first Stanley Cup in the NHL era in 1918?","a":"Toronto Arenas","choices":["Toronto Arenas","Montreal Canadiens","Ottawa Senators","Quebec Bulldogs"],"sport":"hockey","difficulty":"hard"},
{"q":"How many consecutive Stanley Cups did the Montreal Canadiens win from 1956-1960?","a":"5","choices":["5","4","6","3"],"sport":"hockey","difficulty":"medium"},
{"q":"Who was the first NHL player to score 500 career goals?","a":"Maurice Richard","choices":["Maurice Richard","Gordie Howe","Boom Boom Geoffrion","Bobby Hull"],"sport":"hockey","difficulty":"hard"},
{"q":"What were the 'Original Six' NHL teams?","a":"Montreal, Toronto, Boston, Chicago, Detroit, New York Rangers","choices":["Montreal, Toronto, Boston, Chicago, Detroit, New York Rangers","Montreal, Toronto, Ottawa, Boston, Chicago, Detroit","Montreal, Toronto, Boston, Detroit, Rangers, Americans","All 6 founding teams in 1917"],"sport":"hockey","difficulty":"medium"},
{"q":"Which player wore number 9 for the Detroit Red Wings and is nicknamed 'Mr. Hockey'?","a":"Gordie Howe","choices":["Gordie Howe","Ted Lindsay","Sid Abel","Alex Delvecchio"],"sport":"hockey","difficulty":"medium"},
{"q":"Who was the first NHL goalie to wear a mask in a regular season game?","a":"Jacques Plante (1959)","choices":["Jacques Plante (1959)","Gump Worsley","Terry Sawchuk","Glenn Hall"],"sport":"hockey","difficulty":"hard"},
{"q":"How many times did the Edmonton Oilers win the Stanley Cup in the 1980s?","a":"4 times (1984, 1985, 1987, 1988)","choices":["4 times (1984, 1985, 1987, 1988)","3 times","5 times","2 times"],"sport":"hockey","difficulty":"medium"},

# ── MLB HISTORY 1900s-1960s ──
{"q":"Which pitcher had a perfect 511 career wins record?","a":"Cy Young (511 wins)","choices":["Cy Young (511 wins)","Walter Johnson","Christy Mathewson","Grover Alexander"],"sport":"baseball","difficulty":"hard"},
{"q":"Who is credited with inventing the curveball in baseball?","a":"Candy Cummings is generally credited (1867)","choices":["Candy Cummings is generally credited (1867)","Cy Young","Walter Johnson","Rube Waddell"],"sport":"baseball","difficulty":"hard"},
{"q":"Which team did Babe Ruth play for before the New York Yankees?","a":"Boston Red Sox","choices":["Boston Red Sox","Baltimore Orioles","Providence Grays","Detroit Tigers"],"sport":"baseball","difficulty":"medium"},
{"q":"What year did the Brooklyn Dodgers move to Los Angeles?","a":"1958","choices":["1958","1955","1960","1962"],"sport":"baseball","difficulty":"medium"},
{"q":"Who was known as 'Shoeless Joe'?","a":"Joe Jackson","choices":["Joe Jackson","Joe DiMaggio","Joe Cronin","Joe Gordon"],"sport":"baseball","difficulty":"medium"},
{"q":"Which team won the most World Series titles in the 1950s?","a":"New York Yankees (won in 1950, 1951, 1952, 1953, 1956, 1958)","choices":["New York Yankees (won in 1950, 1951, 1952, 1953, 1956, 1958)","Brooklyn Dodgers","Milwaukee Braves","Cleveland Indians"],"sport":"baseball","difficulty":"hard"},
{"q":"What is the 'Dead Ball Era' in baseball history?","a":"The period roughly 1900-1919 when home runs were rare and pitching dominated","choices":["The period roughly 1900-1919 when home runs were rare and pitching dominated","When the DH was introduced","During World War II","The 1990s steroid era"],"sport":"baseball","difficulty":"hard"},
{"q":"Who hit four home runs in a single World Series game in 1926?","a":"Babe Ruth","choices":["Babe Ruth","Lou Gehrig","Rogers Hornsby","Jesse Haines"],"sport":"baseball","difficulty":"hard"},
{"q":"Which MLB team plays in Cincinnati?","a":"Reds","choices":["Reds","Browns","Indians","Cardinals"],"sport":"baseball","difficulty":"easy"},
{"q":"What year did the National League adopt the DH?","a":"2022 (expanded from AL only to both leagues)","choices":["2022 (expanded from AL only to both leagues)","2020","2018","2016"],"sport":"baseball","difficulty":"medium"},

# ── SOCCER — La Liga / Bundesliga / Serie A ──
{"q":"Which club has won the most Bundesliga titles?","a":"Bayern Munich","choices":["Bayern Munich","Borussia Dortmund","Schalke","Borussia Monchengladbach"],"sport":"soccer","difficulty":"easy"},
{"q":"Which Italian club is nicknamed 'La Vecchia Signora' (The Old Lady)?","a":"Juventus","choices":["Juventus","AC Milan","Inter Milan","AS Roma"],"sport":"soccer","difficulty":"medium"},
{"q":"Who won the Bundesliga's top scorer award (Torjagerkanone) the most times?","a":"Gerd Muller (7 times)","choices":["Gerd Muller (7 times)","Robert Lewandowski","Jupp Heynckes","Karl-Heinz Rummenigge"],"sport":"soccer","difficulty":"hard"},
{"q":"Which club plays at the Bernabeu?","a":"Real Madrid","choices":["Real Madrid","Atletico Madrid","Villarreal","Sevilla"],"sport":"soccer","difficulty":"easy"},
{"q":"What country does Robert Lewandowski play for internationally?","a":"Poland","choices":["Poland","Germany","Czech Republic","Slovakia"],"sport":"soccer","difficulty":"easy"},
{"q":"Which club did Diego Maradona famously play for in Serie A?","a":"Napoli","choices":["Napoli","Juventus","AC Milan","Inter Milan"],"sport":"soccer","difficulty":"medium"},
{"q":"What is the Copa del Rey?","a":"The Spanish national football cup competition","choices":["The Spanish national football cup competition","The Spanish league championship","The South American equivalent of Champions League","A pre-season Spanish tournament"],"sport":"soccer","difficulty":"medium"},
{"q":"Which nation has the most players in the English Premier League historically?","a":"England","choices":["England","France","Ireland","Spain"],"sport":"soccer","difficulty":"medium"},
{"q":"Who won the 2023-24 Champions League?","a":"Real Madrid","choices":["Real Madrid","Borussia Dortmund","Manchester City","Bayern Munich"],"sport":"soccer","difficulty":"medium"},
{"q":"Which country does Vinicius Jr play for internationally?","a":"Brazil","choices":["Brazil","Spain","Portugal","France"],"sport":"soccer","difficulty":"easy"},
{"q":"Who managed Bayern Munich to the Champions League title in 2020?","a":"Hansi Flick","choices":["Hansi Flick","Niko Kovac","Julian Nagelsmann","Thomas Tuchel"],"sport":"soccer","difficulty":"hard"},
{"q":"Which club did Thierry Henry play for in the Premier League?","a":"Arsenal","choices":["Arsenal","Chelsea","Manchester United","Tottenham"],"sport":"soccer","difficulty":"easy"},
{"q":"How many times did Ajax win the European Cup / Champions League?","a":"4 times (1971, 1972, 1973, 1995)","choices":["4 times (1971, 1972, 1973, 1995)","3 times","5 times","2 times"],"sport":"soccer","difficulty":"hard"},
{"q":"Which player has won the most Serie A titles?","a":"Paolo Maldini (7 with AC Milan)","choices":["Paolo Maldini (7 with AC Milan)","Alessandro Del Piero","Francesco Totti","Roberto Baggio"],"sport":"soccer","difficulty":"hard"},
{"q":"What is the correct name of the annual award for the best player in European leagues?","a":"Ballon d'Or","choices":["Ballon d'Or","Golden Ball","UEFA Player of the Year","European Golden Boot"],"sport":"soccer","difficulty":"easy"},

# ── F1 — specific records and seasons ──
{"q":"Which driver holds the F1 record for most wins at the Monaco Grand Prix?","a":"Ayrton Senna (6 wins)","choices":["Ayrton Senna (6 wins)","Michael Schumacher","Graham Hill","Lewis Hamilton"],"sport":"f1","difficulty":"hard"},
{"q":"What was the first team to win 100 F1 races?","a":"Ferrari","choices":["Ferrari","McLaren","Mercedes","Williams"],"sport":"f1","difficulty":"medium"},
{"q":"Which driver won the F1 World Championship in 2008?","a":"Lewis Hamilton","choices":["Lewis Hamilton","Felipe Massa","Kimi Raikkonen","Fernando Alonso"],"sport":"f1","difficulty":"medium"},
{"q":"Who was Michael Schumacher's teammate at Ferrari for most of his championship years?","a":"Rubens Barrichello","choices":["Rubens Barrichello","Eddie Irvine","Felipe Massa","Nico Rosberg"],"sport":"f1","difficulty":"medium"},
{"q":"Which circuit hosts the Italian Grand Prix?","a":"Monza","choices":["Monza","Imola","Mugello","Bremgarten"],"sport":"f1","difficulty":"easy"},
{"q":"Who won the F1 World Championship in 2016?","a":"Nico Rosberg","choices":["Nico Rosberg","Lewis Hamilton","Sebastian Vettel","Daniel Ricciardo"],"sport":"f1","difficulty":"medium"},
{"q":"What does the checkered flag signify in F1?","a":"The end of the race","choices":["The end of the race","A safety car period","A yellow flag warning","The start of the final lap"],"sport":"f1","difficulty":"easy"},
{"q":"Which team won the F1 Constructors Championship in 2020?","a":"Mercedes","choices":["Mercedes","Red Bull","Ferrari","Racing Point"],"sport":"f1","difficulty":"medium"},
{"q":"Who holds the record for most F1 pole positions?","a":"Lewis Hamilton (104)","choices":["Lewis Hamilton (104)","Michael Schumacher","Ayrton Senna","Sebastian Vettel"],"sport":"f1","difficulty":"medium"},
{"q":"What nationality is Charles Leclerc?","a":"Monegasque (from Monaco)","choices":["Monegasque (from Monaco)","French","Italian","Swiss"],"sport":"f1","difficulty":"medium"},
{"q":"Which F1 team is based in Woking, England?","a":"McLaren","choices":["McLaren","Williams","Aston Martin","Alpine"],"sport":"f1","difficulty":"medium"},
{"q":"Who won the 2022 F1 World Championship?","a":"Max Verstappen","choices":["Max Verstappen","Charles Leclerc","Lewis Hamilton","Sergio Perez"],"sport":"f1","difficulty":"medium"},

# ── TENNIS — specific records ──
{"q":"How many Grand Slam titles did Pete Sampras win?","a":"14","choices":["14","12","16","10"],"sport":"tennis","difficulty":"medium"},
{"q":"Which player has won the most French Open titles (men's singles)?","a":"Rafael Nadal (14)","choices":["Rafael Nadal (14)","Bjorn Borg","Ivan Lendl","Novak Djokovic"],"sport":"tennis","difficulty":"medium"},
{"q":"What surface is Wimbledon played on?","a":"Grass","choices":["Grass","Clay","Hard court","Carpet"],"sport":"tennis","difficulty":"easy"},
{"q":"How many sets does a men's Grand Slam match use?","a":"Best of 5 sets","choices":["Best of 5 sets","Best of 3 sets","First to 4 sets","First to 6 games"],"sport":"tennis","difficulty":"easy"},
{"q":"Who won the US Open in 2022 (women's singles)?","a":"Iga Swiatek","choices":["Iga Swiatek","Coco Gauff","Ons Jabeur","Caroline Garcia"],"sport":"tennis","difficulty":"medium"},
{"q":"Which player is nicknamed 'The King of Clay'?","a":"Rafael Nadal","choices":["Rafael Nadal","Novak Djokovic","Roger Federer","Bjorn Borg"],"sport":"tennis","difficulty":"easy"},
{"q":"Who was the first man to win all four Grand Slams in the same calendar year?","a":"Don Budge (1938)","choices":["Don Budge (1938)","Rod Laver","Pete Sampras","Bjorn Borg"],"sport":"tennis","difficulty":"hard"},
{"q":"What is a tiebreak in tennis?","a":"A game played when a set reaches 6-6, first to 7 points (win by 2) wins the set","choices":["A game played when a set reaches 6-6, first to 7 points (win by 2) wins the set","Extra games added if tied after 40-40","A third set played to decide a match","A scoring format used only in doubles"],"sport":"tennis","difficulty":"easy"},
{"q":"How many Wimbledon singles titles did Roger Federer win?","a":"8","choices":["8","7","9","6"],"sport":"tennis","difficulty":"medium"},
{"q":"Which player won the 2023 Wimbledon women's title?","a":"Marketa Vondrousova","choices":["Marketa Vondrousova","Ons Jabeur","Aryna Sabalenka","Coco Gauff"],"sport":"tennis","difficulty":"hard"},
{"q":"Who won the 2023 Australian Open (men's singles)?","a":"Novak Djokovic","choices":["Novak Djokovic","Stefanos Tsitsipas","Karen Khachanov","Tommy Paul"],"sport":"tennis","difficulty":"medium"},
{"q":"What is a 'bagel' in tennis slang?","a":"Winning a set 6-0","choices":["Winning a set 6-0","An ace serve","A double fault on set point","Winning a match without losing a game"],"sport":"tennis","difficulty":"medium"},

# ── GOLF ──
{"q":"How many majors did Jack Nicklaus win?","a":"18","choices":["18","14","20","16"],"sport":"golf","difficulty":"medium"},
{"q":"What is the Masters Tournament played at?","a":"Augusta National Golf Club","choices":["Augusta National Golf Club","Pebble Beach","St Andrews","Pinehurst"],"sport":"golf","difficulty":"easy"},
{"q":"Who won the 2023 US Open (golf)?","a":"Wyndham Clark","choices":["Wyndham Clark","Rory McIlroy","Scottie Scheffler","Cameron Young"],"sport":"golf","difficulty":"hard"},
{"q":"What is an albatross in golf?","a":"Three under par on a single hole","choices":["Three under par on a single hole","Two under par","Four under par","One under par"],"sport":"golf","difficulty":"medium"},
{"q":"Which player is nicknamed 'The Big Easy'?","a":"Ernie Els","choices":["Ernie Els","Phil Mickelson","Retief Goosen","Vijay Singh"],"sport":"golf","difficulty":"medium"},
{"q":"How many holes are in a standard round of golf?","a":"18","choices":["18","9","27","21"],"sport":"golf","difficulty":"easy"},
{"q":"Which country does Rory McIlroy represent?","a":"Northern Ireland","choices":["Northern Ireland","Republic of Ireland","England","Scotland"],"sport":"golf","difficulty":"medium"},
{"q":"What is the lowest score ever recorded in a PGA Tour event?","a":"58 (Jim Furyk in 2016)","choices":["58 (Jim Furyk in 2016)","60","56","59"],"sport":"golf","difficulty":"hard"},
{"q":"Who won the 2024 Masters?","a":"Scottie Scheffler","choices":["Scottie Scheffler","Collin Morikawa","Jon Rahm","Rory McIlroy"],"sport":"golf","difficulty":"medium"},
{"q":"What is the Ryder Cup?","a":"A biennial golf competition between teams from the United States and Europe","choices":["A biennial golf competition between teams from the United States and Europe","A match play event between top-ranked individual players","An annual event at St Andrews","A tournament open to amateurs and professionals"],"sport":"golf","difficulty":"easy"},
{"q":"Who holds the PGA Tour record for most career wins?","a":"Sam Snead (82 wins)","choices":["Sam Snead (82 wins)","Tiger Woods (82 wins - tied)","Jack Nicklaus","Ben Hogan"],"sport":"golf","difficulty":"hard"},
{"q":"Which player won three consecutive US Open golf titles from 2005-2007?","a":"No player won three straight US Opens","choices":["No player won three straight US Opens in recent history","Tiger Woods (two consecutive)","Phil Mickelson","Retief Goosen"],"sport":"golf","difficulty":"hard"},

# ── UFC / MMA ──
{"q":"Who was the first UFC Heavyweight Champion?","a":"Royce Gracie won UFC 1 but the title concept came later; Mark Coleman is often cited as first champ","choices":["Mark Coleman (first official UFC heavyweight champ in 1996)","Royce Gracie","Dan Severn","Ken Shamrock"],"sport":"ufc","difficulty":"hard"},
{"q":"Which fighter holds the UFC record for most consecutive wins?","a":"Khabib Nurmagomedov went 29-0 undefeated","choices":["Khabib Nurmagomedov (13-0 in UFC, 29-0 overall)","Anderson Silva","Jon Jones","Georges St-Pierre"],"sport":"ufc","difficulty":"hard"},
{"q":"What weight class does Conor McGregor typically compete in?","a":"Lightweight and Featherweight","choices":["Lightweight and Featherweight","Welterweight","Middleweight","Bantamweight"],"sport":"ufc","difficulty":"easy"},
{"q":"Who is known as 'The Spider' in MMA?","a":"Anderson Silva","choices":["Anderson Silva","Conor McGregor","Jon Jones","Georges St-Pierre"],"sport":"ufc","difficulty":"medium"},
{"q":"How many rounds are in a non-title UFC main event?","a":"3 rounds (5-minute rounds)","choices":["3 rounds (5-minute rounds)","5 rounds","4 rounds","2 rounds"],"sport":"ufc","difficulty":"easy"},
{"q":"Who was the first simultaneous two-division UFC champion?","a":"Conor McGregor (Featherweight + Lightweight)","choices":["Conor McGregor (Featherweight + Lightweight)","Daniel Cormier","Jon Jones","Randy Couture"],"sport":"ufc","difficulty":"medium"},
{"q":"What does KO stand for in MMA?","a":"Knockout","choices":["Knockout","Keep On","Kicking Out","Key Offense"],"sport":"ufc","difficulty":"easy"},
{"q":"Which city hosts the most UFC events annually?","a":"Las Vegas","choices":["Las Vegas","New York","Los Angeles","Miami"],"sport":"ufc","difficulty":"medium"},

# ── OLYMPICS — specific sports and moments ──
{"q":"Who won the men's 100m sprint at the 1988 Seoul Olympics and was later disqualified?","a":"Ben Johnson","choices":["Ben Johnson","Carl Lewis","Linford Christie","Leroy Burrell"],"sport":"olympics","difficulty":"medium"},
{"q":"Which country has won the most gold medals at the Winter Olympics?","a":"Norway","choices":["Norway","United States","Germany","Soviet Union"],"sport":"olympics","difficulty":"medium"},
{"q":"Who was the first athlete to win gold medals at both Summer and Winter Olympics?","a":"Eddie Eagan (boxing 1920, bobsled 1932)","choices":["Eddie Eagan (boxing 1920, bobsled 1932)","Carl Lewis","Jim Thorpe","Rafer Johnson"],"sport":"olympics","difficulty":"hard"},
{"q":"What sport did Carl Lewis dominate at the 1984 Los Angeles Olympics, winning 4 gold medals?","a":"Track and field (100m, 200m, 4x100m relay, long jump)","choices":["Track and field (100m, 200m, 4x100m relay, long jump)","Decathlon","Heptathlon","Triathlon"],"sport":"olympics","difficulty":"medium"},
{"q":"Which city hosted the 1980 Summer Olympics that the US boycotted?","a":"Moscow","choices":["Moscow","Montreal","Munich","Mexico City"],"sport":"olympics","difficulty":"medium"},
{"q":"Who is the only gymnast to ever receive a perfect 10 at the Olympics?","a":"Nadia Comaneci (1976 Montreal)","choices":["Nadia Comaneci (1976 Montreal)","Olga Korbut","Mary Lou Retton","Simone Biles"],"sport":"olympics","difficulty":"medium"},
{"q":"What sport did the Dream Team play at the 1992 Barcelona Olympics?","a":"Basketball","choices":["Basketball","Volleyball","Track and Field","Water Polo"],"sport":"olympics","difficulty":"easy"},
{"q":"Which city hosted the 1996 Summer Olympics where Muhammad Ali lit the torch?","a":"Atlanta","choices":["Atlanta","Los Angeles","Seoul","Barcelona"],"sport":"olympics","difficulty":"easy"},
{"q":"Who won the 1980 Miracle on Ice game in ice hockey at the Lake Placid Winter Olympics?","a":"United States","choices":["United States","Soviet Union","Canada","Sweden"],"sport":"olympics","difficulty":"easy"},
{"q":"Which country won the most gold medals at the 2024 Paris Summer Olympics?","a":"United States","choices":["United States","China","Great Britain","Australia"],"sport":"olympics","difficulty":"medium"},
]

with open('questions.json') as f:
    existing = json.load(f)

existing_set = set(q['q'].strip().lower() for q in existing)
added = [q for q in new_questions if q['q'].strip().lower() not in existing_set]
existing.extend(added)

with open('questions.json', 'w') as f:
    json.dump(existing, f, indent=2)

print(f"Added {len(added)} questions. Total now: {len(existing)}")
