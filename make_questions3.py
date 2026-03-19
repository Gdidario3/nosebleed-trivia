#!/usr/bin/env python3
"""Part 3 - More award data and questions"""
import json, random, os
from collections import Counter
random.seed(456)

def q(question, answer, wrongs, sport, difficulty):
    c = [answer] + list(wrongs[:3])
    random.shuffle(c)
    return {"q":question,"a":answer,"choices":c,"sport":sport,"difficulty":difficulty}

questions = []

# ============================================================
# NHL CONN SMYTHE (Playoff MVP)
# ============================================================
conn_smythe = [
    (2024,"Aleksander Barkov"),(2023,"Adin Hill"),(2022,"Cale Makar"),
    (2021,"Andrei Vasilevskiy"),(2020,"Victor Hedman"),(2019,"Ryan O'Reilly"),
    (2018,"Alex Ovechkin"),(2017,"Sidney Crosby"),(2016,"Sidney Crosby"),
    (2015,"Duncan Keith"),(2014,"Justin Williams"),(2013,"Patrick Kane"),
    (2012,"Jonathan Quick"),(2011,"Tim Thomas"),(2010,"Jonathan Toews"),
    (2009,"Evgeni Malkin"),(2008,"Henrik Zetterberg"),(2007,"Scott Niedermayer"),
    (2006,"Cam Ward"),(2004,"Brad Richards"),(2003,"Jean-Sebastien Giguere"),
    (2002,"Nicklas Lidstrom"),(2001,"Patrick Roy"),(2000,"Scott Stevens"),
    (1999,"Joe nieuwendyk"),(1998,"Steve Yzerman"),(1997,"Mike Vernon"),
    (1996,"Joe Sakic"),(1995,"Claude Lemieux"),(1994,"Brian Leetch"),
    (1993,"Patrick Roy"),(1992,"Mario Lemieux"),(1991,"Mario Lemieux"),
    (1990,"Bill Ranford"),(1989,"Al MacInnis"),(1988,"Wayne Gretzky"),
    (1987,"Ron Hextall"),(1986,"Patrick Roy"),(1985,"Wayne Gretzky"),
    (1984,"Mark Messier"),(1983,"Billy Smith"),(1982,"Mike Bossy"),
    (1981,"Butch Goring"),(1980,"Bryan Trottier"),(1979,"Bob Gainey"),
    (1978,"Larry Robinson"),(1977,"Guy Lafleur"),(1976,"Reggie Leach"),
    (1975,"Bernie Parent"),(1974,"Bernie Parent"),(1973,"Yvan Cournoyer"),
    (1972,"Bobby Orr"),(1971,"Ken Dryden"),(1970,"Bobby Orr"),
    (1969,"Serge Savard"),(1968,"Glenn Hall"),(1967,"Dave Keon"),
    (1966,"Roger Crozier"),
]

nhl_pool = ["Wayne Gretzky","Mario Lemieux","Sidney Crosby","Alex Ovechkin","Patrick Roy",
    "Martin Brodeur","Mark Messier","Steve Yzerman","Nicklas Lidstrom","Bobby Orr",
    "Jean Beliveau","Gordie Howe","Guy Lafleur","Bobby Hull","Phil Esposito",
    "Joe Sakic","Peter Forsberg","Teemu Selanne","Jaromir Jagr","Patrick Kane",
    "Jonathan Toews","Evgeni Malkin","Victor Hedman","Cale Makar","Connor McDavid",
    "Nathan MacKinnon","Auston Matthews","Leon Draisaitl","Brad Richards","Claude Lemieux",
    "Brian Leetch","Scott Niedermayer","Joe Nieuwendyk","Bill Ranford","Ron Hextall",
    "Al MacInnis","Bernie Parent","Butch Goring","Bryan Trottier","Bob Gainey",
    "Larry Robinson","Reggie Leach","Yvan Cournoyer","Ken Dryden","Serge Savard",
    "Glenn Hall","Dave Keon","Roger Crozier","Cam Ward","Henrik Zetterberg",
    "Jonathan Quick","Tim Thomas","Duncan Keith","Justin Williams","Scott Stevens"]

for yr, player in conn_smythe:
    w = [p for p in nhl_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the Conn Smythe Trophy (NHL playoff MVP) in {yr}?", player, w[:3], "hockey","hard"))

print(f"Conn Smythe done: {len(questions)}")

# ============================================================
# NHL VEZINA TROPHY (Best Goaltender)
# ============================================================
vezina = [
    (2024,"Connor Hellebuyck"),(2023,"Linus Ullmark"),(2022,"Igor Shesterkin"),
    (2021,"Marc-Andre Fleury"),(2020,"Connor Hellebuyck"),(2019,"Andrei Vasilevskiy"),
    (2018,"Pekka Rinne"),(2017,"Sergei Bobrovsky"),(2016,"Braden Holtby"),
    (2015,"Carey Price"),(2014,"Tuukka Rask"),(2013,"Sergei Bobrovsky"),
    (2012,"Henrik Lundqvist"),(2011,"Tim Thomas"),(2010,"Ryan Miller"),
    (2009,"Tim Thomas"),(2008,"Martin Brodeur"),(2007,"Martin Brodeur"),
    (2006,"Miikka Kiprusoff"),(2004,"Martin Brodeur"),(2003,"Martin Brodeur"),
    (2002,"Jose Theodore"),(2001,"Dominik Hasek"),(2000,"Olaf Kolzig"),
    (1999,"Dominik Hasek"),(1998,"Dominik Hasek"),(1997,"Dominik Hasek"),
    (1996,"Jim Carey"),(1995,"Dominik Hasek"),(1994,"Dominik Hasek"),
    (1993,"Ed Belfour"),(1992,"Patrick Roy"),(1991,"Ed Belfour"),
    (1990,"Patrick Roy"),(1989,"Patrick Roy"),(1988,"Grant Fuhr"),
    (1987,"Ron Hextall"),(1986,"John Vanbiesbrouck"),(1985,"Pelle Lindbergh"),
    (1984,"Tom Barrasso"),(1983,"Pete Peeters"),(1982,"Billy Smith"),
    (1981,"Richard Sevigny, Denis Herron, Michel Larocque"),(1980,"Don Edwards/Bob Sauve"),
    (1979,"Ken Dryden and Michel Larocque"),(1978,"Ken Dryden and Michel Larocque"),
    (1977,"Ken Dryden and Michel Larocque"),(1976,"Ken Dryden"),
    (1975,"Bernie Parent"),(1974,"Bernie Parent"),(1973,"Ken Dryden"),
    (1972,"Tony Esposito and Gary Smith"),(1971,"Eddie Giacomin and Gilles Villemure"),
    (1970,"Tony Esposito"),(1969,"Jacques Plante and Glenn Hall"),
    (1968,"Gump Worsley and Rogie Vachon"),(1967,"Glenn Hall and Denis DeJordy"),
]

goalie_pool = ["Martin Brodeur","Patrick Roy","Dominik Hasek","Ken Dryden","Bernie Parent",
    "Connor Hellebuyck","Andrei Vasilevskiy","Igor Shesterkin","Marc-Andre Fleury","Carey Price",
    "Henrik Lundqvist","Pekka Rinne","Sergei Bobrovsky","Braden Holtby","Tim Thomas",
    "Ryan Miller","Miikka Kiprusoff","Jose Theodore","Olaf Kolzig","Ed Belfour",
    "Grant Fuhr","Ron Hextall","Tom Barrasso","Pete Peeters","Billy Smith","Tony Esposito",
    "Glenn Hall","Jacques Plante","Terry Sawchuk","Johnny Bower","Frank Brimsek",
    "Mike Vernon","Kirk McLean","John Vanbiesbrouck","Roberto Luongo","Luongo","Linus Ullmark",
    "Tuukka Rask","Mike Smith","Chris Osgood","Curtis Joseph"]

for yr, player in vezina:
    if "and" in player or "," in player:
        continue
    w = [p for p in goalie_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the Vezina Trophy (NHL's best goaltender) for the {yr} season?", player, w[:3], "hockey","hard"))

print(f"Vezina done: {len(questions)}")

# ============================================================
# NHL CALDER TROPHY (Top Rookie)
# ============================================================
calder = [
    (2024,"Macklin Celebrini"),(2023,"Matty Beniers"),(2022,"Moritz Seider"),
    (2021,"Kirill Kaprizov"),(2020,"Cale Makar"),(2019,"Elias Pettersson"),
    (2018,"Mathew Barzal"),(2017,"Auston Matthews"),(2016,"Artemi Panarin"),
    (2015,"Aaron Ekblad"),(2014,"Brendan Gallagher"),(2013,"Jonathan Huberdeau"),
    (2012,"Gabriel Landeskog"),(2011,"Jeff Skinner"),(2010,"Tyler Myers"),
    (2009,"Steve Mason"),(2008,"Patrick Kane"),(2007,"Evgeni Malkin"),
    (2006,"Alexander Ovechkin"),(2004,"Andrew Raycroft"),(2003,"Barret Jackman"),
    (2002,"Dany Heatley"),(2001,"Evgeni Nabokov"),(2000,"Scott Gomez"),
    (1999,"Chris Drury"),(1998,"Sergei Samsonov"),(1997,"Bryan Berard"),
    (1996,"Daniel Alfredsson"),(1995,"Peter Forsberg"),(1994,"Martin Brodeur"),
    (1993,"Teemu Selanne"),(1992,"Pavel Bure"),(1991,"Ed Belfour"),
    (1990,"Sergei Makarov"),(1989,"Brian Leetch"),(1988,"Joe Nieuwendyk"),
    (1987,"Luc Robitaille"),(1986,"Gary Suter"),(1985,"Mario Lemieux"),
    (1984,"Tom Barrasso"),(1983,"Steve Larmer"),(1982,"Dale Hawerchuk"),
    (1981,"Peter Stastny"),(1980,"Raymond Bourque"),(1979,"Bobby Smith"),
    (1978,"Mike Bossy"),(1977,"Willi Plett"),(1976,"Bryan Trottier"),
    (1975,"Eric Vail"),(1974,"Denis Potvin"),(1973,"Steve Vickers"),
    (1972,"Ken Dryden"),(1971,"Gilbert Perreault"),(1970,"Tony Esposito"),
    (1969,"Danny Grant"),(1968,"Derek Sanderson"),(1967,"Bobby Orr"),
]

rookie_pool = ["Patrick Kane","Evgeni Malkin","Alexander Ovechkin","Peter Forsberg","Martin Brodeur",
    "Teemu Selanne","Pavel Bure","Mario Lemieux","Dale Hawerchuk","Raymond Bourque",
    "Mike Bossy","Bryan Trottier","Denis Potvin","Ken Dryden","Gilbert Perreault","Tony Esposito",
    "Bobby Orr","Auston Matthews","Cale Makar","Connor McDavid","Nathan MacKinnon",
    "Leon Draisaitl","Jack Hughes","Nico Hischier","Moritz Seider","Kirill Kaprizov",
    "Elias Pettersson","Mathew Barzal","Artemi Panarin","Aaron Ekblad","Gabriel Landeskog",
    "Jeff Skinner","Steve Mason","Brendan Gallagher","Jonathan Huberdeau","Brian Leetch",
    "Luc Robitaille","Tom Barrasso","Peter Stastny","Bryan Berard","Daniel Alfredsson"]

for yr, player in calder:
    w = [p for p in rookie_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the Calder Trophy (NHL top rookie) for the {yr} season?", player, w[:3], "hockey","hard"))

print(f"Calder done: {len(questions)}")

# ============================================================
# NHL ROCKET RICHARD TROPHY (Top Goal Scorer)
# ============================================================
rocket_richard = [
    (2024,"Auston Matthews"),(2023,"David Pastrnak"),(2022,"Auston Matthews"),
    (2021,"Auston Matthews"),(2020,"David Pastrnak and Alex Ovechkin"),(2019,"Alex Ovechkin"),
    (2018,"Alex Ovechkin"),(2017,"Sidney Crosby and Evgeni Malkin"),(2016,"Alex Ovechkin"),
    (2015,"Alex Ovechkin"),(2014,"Alex Ovechkin"),(2013,"Alex Ovechkin"),
    (2012,"Steven Stamkos"),(2011,"Corey Perry"),(2010,"Steven Stamkos"),
    (2009,"Alexander Ovechkin"),(2008,"Alexander Ovechkin"),(2007,"Vincent Lecavalier"),
    (2006,"Jonathan Cheechoo"),(2004,"Ilya Kovalchuk and Rick Nash and Jarome Iginla"),
    (2003,"Milan Hejduk"),(2002,"Jarome Iginla"),(2001,"Tony Amonte and Pavel Bure"),
]

rr_pool = ["Auston Matthews","David Pastrnak","Alex Ovechkin","Sidney Crosby","Steven Stamkos",
    "Corey Perry","Vincent Lecavalier","Jonathan Cheechoo","Jarome Iginla","Milan Hejduk",
    "Ilya Kovalchuk","Rick Nash","Pavel Bure","Tony Amonte","Joe Sakic","Brett Hull",
    "Teemu Selanne","Mats Sundin","Keith Tkachuk","Eric Lindros","Jaromir Jagr",
    "Patrick Kane","John Tavares","Leon Draisaitl","Connor McDavid","Nathan MacKinnon"]

for yr, player in rocket_richard:
    if " and " in player:
        continue
    w = [p for p in rr_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the Rocket Richard Trophy (NHL top goal scorer) for the {yr} season?", player, w[:3], "hockey","hard"))

print(f"Rocket Richard done: {len(questions)}")

# ============================================================
# F1 RACE WINNERS - MONACO GP (selected years)
# ============================================================
monaco_gp = [
    (2023,"Max Verstappen"),(2022,"Sergio Perez"),(2021,"Max Verstappen"),
    (2019,"Lewis Hamilton"),(2018,"Daniel Ricciardo"),(2017,"Sebastian Vettel"),
    (2016,"Lewis Hamilton"),(2015,"Nico Rosberg"),(2014,"Nico Rosberg"),
    (2013,"Nico Rosberg"),(2012,"Mark Webber"),(2011,"Sebastian Vettel"),
    (2010,"Mark Webber"),(2009,"Jenson Button"),(2008,"Lewis Hamilton"),
    (2007,"Fernando Alonso"),(2006,"David Coulthard"),(2005,"Kimi Raikkonen"),
    (2004,"Jarno Trulli"),(2003,"Juan Pablo Montoya"),(2002,"David Coulthard"),
    (2001,"Michael Schumacher"),(2000,"Mika Hakkinen"),(1999,"Michael Schumacher"),
    (1998,"Mika Hakkinen"),(1997,"Michael Schumacher"),(1996,"Olivier Panis"),
    (1995,"Michael Schumacher"),(1994,"Michael Schumacher"),(1993,"Ayrton Senna"),
    (1992,"Ayrton Senna"),(1991,"Ayrton Senna"),(1990,"Ayrton Senna"),
    (1989,"Ayrton Senna"),(1988,"Alain Prost"),(1987,"Ayrton Senna"),
    (1986,"Keke Rosberg"),(1985,"Alain Prost"),(1984,"Alain Prost"),
    (1983,"Keke Rosberg"),(1982,"Riccardo Patrese"),(1981,"Gilles Villeneuve"),
    (1980,"Carlos Reutemann"),(1979,"Jody Scheckter"),(1978,"Patrick Depailler"),
    (1977,"Jody Scheckter"),(1976,"Niki Lauda"),(1975,"Niki Lauda"),
    (1974,"Ronnie Peterson"),(1973,"Jackie Stewart"),(1972,"Jean-Pierre Beltoise"),
    (1971,"Jackie Stewart"),(1970,"Jochen Rindt"),(1969,"Graham Hill"),
    (1968,"Graham Hill"),(1967,"Denny Hulme"),(1966,"Jackie Stewart"),
    (1965,"Graham Hill"),(1964,"Graham Hill"),(1963,"Graham Hill"),
    (1962,"Bruce McLaren"),(1961,"Stirling Moss"),(1960,"Stirling Moss"),
    (1959,"Jack Brabham"),(1958,"Maurice Trintignant"),(1957,"Juan Manuel Fangio"),
    (1956,"Stirling Moss"),(1955,"Maurice Trintignant"),(1950,"Juan Manuel Fangio"),
]

f1_pool = ["Max Verstappen","Lewis Hamilton","Sebastian Vettel","Michael Schumacher","Ayrton Senna",
    "Alain Prost","Niki Lauda","Fernando Alonso","Kimi Raikkonen","Mika Hakkinen",
    "Nigel Mansell","Nelson Piquet","Sergio Perez","Daniel Ricciardo","Nico Rosberg",
    "Mark Webber","David Coulthard","Jenson Button","Juan Pablo Montoya","Jarno Trulli",
    "Gilles Villeneuve","Jody Scheckter","Jackie Stewart","Carlos Reutemann","Graham Hill",
    "Jack Brabham","Stirling Moss","Juan Manuel Fangio","Jim Clark","Denny Hulme",
    "Jochen Rindt","Ronnie Peterson","Patrick Depailler","Jean-Pierre Beltoise","Bruce McLaren",
    "Keke Rosberg","Riccardo Patrese","Carlos Sainz","Charles Leclerc","Valtteri Bottas",
    "George Russell","Lando Norris","Lance Stroll","Pierre Gasly","Esteban Ocon"]

for yr, driver in monaco_gp:
    w = [p for p in f1_pool if p != driver]
    random.shuffle(w)
    questions.append(q(f"Who won the Monaco Grand Prix in {yr}?", driver, w[:3], "f1","hard"))

print(f"Monaco GP done: {len(questions)}")

# F1 British GP winners (selected)
british_gp = [
    (2023,"Max Verstappen"),(2022,"Carlos Sainz"),(2021,"Lewis Hamilton"),
    (2020,"Lewis Hamilton"),(2019,"Lewis Hamilton"),(2018,"Sebastian Vettel"),
    (2017,"Lewis Hamilton"),(2016,"Lewis Hamilton"),(2015,"Lewis Hamilton"),
    (2014,"Lewis Hamilton"),(2013,"Nico Rosberg"),(2012,"Mark Webber"),
    (2011,"Fernando Alonso"),(2010,"Mark Webber"),(2009,"Sebastian Vettel"),
    (2008,"Lewis Hamilton"),(2007,"Kimi Raikkonen"),(2006,"Michael Schumacher"),
    (2005,"Juan Pablo Montoya"),(2004,"Michael Schumacher"),(2003,"Rubens Barrichello"),
    (2002,"Michael Schumacher"),(2001,"Mika Hakkinen"),(2000,"David Coulthard"),
    (1999,"David Coulthard"),(1998,"Michael Schumacher"),(1997,"Jacques Villeneuve"),
    (1996,"Jacques Villeneuve"),(1995,"Johnny Herbert"),(1994,"Damon Hill"),
    (1993,"Alain Prost"),(1992,"Nigel Mansell"),(1991,"Nigel Mansell"),
    (1990,"Alain Prost"),(1989,"Alain Prost"),(1988,"Ayrton Senna"),
    (1987,"Nigel Mansell"),(1986,"Nigel Mansell"),(1985,"Alain Prost"),
    (1984,"Niki Lauda"),(1983,"Alain Prost"),(1982,"Niki Lauda"),
    (1981,"John Watson"),(1980,"Alan Jones"),(1979,"Clay Regazzoni"),
    (1978,"Carlos Reutemann"),(1977,"James Hunt"),(1976,"Niki Lauda"),
    (1975,"Emerson Fittipaldi"),(1974,"Jody Scheckter"),(1973,"Peter Revson"),
]

for yr, driver in british_gp:
    w = [p for p in f1_pool + ["Rubens Barrichello","Jacques Villeneuve","Johnny Herbert",
        "Damon Hill","Juan Pablo Montoya","Clay Regazzoni","Alan Jones","John Watson",
        "James Hunt","Peter Revson","Emerson Fittipaldi","Carlos Sainz","George Russell"] if p != driver]
    random.shuffle(w)
    questions.append(q(f"Who won the British Grand Prix at Silverstone in {yr}?", driver, w[:3], "f1","hard"))

print(f"British GP done: {len(questions)}")

# F1 Italian GP (Monza) winners
italian_gp = [
    (2023,"Max Verstappen"),(2022,"George Russell"),(2021,"Daniel Ricciardo"),
    (2020,"Pierre Gasly"),(2019,"Charles Leclerc"),(2018,"Lewis Hamilton"),
    (2017,"Lewis Hamilton"),(2016,"Nico Rosberg"),(2015,"Lewis Hamilton"),
    (2014,"Lewis Hamilton"),(2013,"Sebastian Vettel"),(2012,"Lewis Hamilton"),
    (2011,"Sebastian Vettel"),(2010,"Fernando Alonso"),(2009,"Rubens Barrichello"),
    (2008,"Sebastian Vettel"),(2007,"Fernando Alonso"),(2006,"Michael Schumacher"),
    (2005,"Juan Pablo Montoya"),(2004,"Rubens Barrichello"),(2003,"Michael Schumacher"),
    (2002,"Rubens Barrichello"),(2001,"Juan Pablo Montoya"),(2000,"Michael Schumacher"),
    (1999,"Heinz-Harald Frentzen"),(1998,"Michael Schumacher"),(1997,"David Coulthard"),
    (1996,"Michael Schumacher"),(1995,"Johnny Herbert"),(1994,"Damon Hill"),
    (1993,"Damon Hill"),(1992,"Ayrton Senna"),(1991,"Nigel Mansell"),
    (1990,"Ayrton Senna"),(1989,"Alain Prost"),(1988,"Gerhard Berger"),
    (1987,"Nelson Piquet"),(1986,"Nelson Piquet"),(1985,"Alain Prost"),
    (1984,"Niki Lauda"),(1983,"Nelson Piquet"),(1982,"Rene Arnoux"),
]

for yr, driver in italian_gp:
    w = [p for p in f1_pool + ["George Russell","Pierre Gasly","Charles Leclerc",
        "Rubens Barrichello","Heinz-Harald Frentzen","Gerhard Berger","Rene Arnoux"] if p != driver]
    random.shuffle(w)
    questions.append(q(f"Who won the Italian Grand Prix at Monza in {yr}?", driver, w[:3], "f1","hard"))

print(f"Italian GP done: {len(questions)}")

# ============================================================
# TENNIS - French Open Womens
# ============================================================
french_open_womens = [
    (2023,"Iga Swiatek"),(2022,"Iga Swiatek"),(2021,"Barbora Krejcikova"),
    (2020,"Iga Swiatek"),(2019,"Ashleigh Barty"),(2018,"Simona Halep"),
    (2017,"Jelena Ostapenko"),(2016,"Garbine Muguruza"),(2015,"Serena Williams"),
    (2014,"Maria Sharapova"),(2013,"Serena Williams"),(2012,"Maria Sharapova"),
    (2011,"Li Na"),(2010,"Francesca Schiavone"),(2009,"Svetlana Kuznetsova"),
    (2008,"Ana Ivanovic"),(2007,"Justine Henin"),(2006,"Justine Henin"),
    (2005,"Justine Henin"),(2004,"Anastasia Myskina"),(2003,"Justine Henin"),
    (2002,"Serena Williams"),(2001,"Jennifer Capriati"),(2000,"Mary Pierce"),
    (1999,"Steffi Graf"),(1998,"Arantxa Sanchez Vicario"),(1997,"Iva Majoli"),
    (1996,"Steffi Graf"),(1995,"Steffi Graf"),(1994,"Arantxa Sanchez Vicario"),
    (1993,"Steffi Graf"),(1992,"Monica Seles"),(1991,"Monica Seles"),
    (1990,"Monica Seles"),(1989,"Arantxa Sanchez Vicario"),(1988,"Steffi Graf"),
    (1987,"Steffi Graf"),(1986,"Chris Evert"),(1985,"Chris Evert"),
    (1984,"Martina Navratilova"),(1983,"Chris Evert"),(1982,"Martina Navratilova"),
    (1981,"Hana Mandlikova"),(1980,"Chris Evert"),(1979,"Chris Evert"),
    (1978,"Virginia Ruzici"),(1977,"Mima Jausovec"),(1976,"Sue Barker"),
    (1975,"Chris Evert"),(1974,"Chris Evert"),(1973,"Margaret Court"),
    (1972,"Billie Jean King"),(1971,"Evonne Goolagong"),(1970,"Margaret Court"),
]

women_pool = ["Iga Swiatek","Serena Williams","Maria Sharapova","Steffi Graf","Martina Navratilova",
    "Chris Evert","Monica Seles","Justine Henin","Simona Halep","Ashleigh Barty",
    "Garbine Muguruza","Venus Williams","Angelique Kerber","Petra Kvitova","Victoria Azarenka",
    "Kim Clijsters","Jennifer Capriati","Arantxa Sanchez Vicario","Conchita Martinez",
    "Lindsay Davenport","Martina Hingis","Jana Novotna","Mary Pierce","Ana Ivanovic",
    "Francesca Schiavone","Li Na","Svetlana Kuznetsova","Jelena Ostapenko","Barbora Krejcikova",
    "Billie Jean King","Margaret Court","Evonne Goolagong","Hana Mandlikova","Naomi Osaka",
    "Coco Gauff","Elena Rybakina","Bianca Andreescu","Caroline Wozniacki","Virginia Ruzici"]

for yr, player in french_open_womens:
    w = [p for p in women_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the French Open (Roland Garros) women's singles title in {yr}?", player, w[:3], "tennis","hard"))

print(f"French Open womens done: {len(questions)}")

# Australian Open womens
aus_open_womens = [
    (2024,"Aryna Sabalenka"),(2023,"Aryna Sabalenka"),(2022,"Ashleigh Barty"),
    (2021,"Naomi Osaka"),(2020,"Sofia Kenin"),(2019,"Naomi Osaka"),
    (2018,"Caroline Wozniacki"),(2017,"Serena Williams"),(2016,"Angelique Kerber"),
    (2015,"Serena Williams"),(2014,"Li Na"),(2013,"Victoria Azarenka"),
    (2012,"Victoria Azarenka"),(2011,"Kim Clijsters"),(2010,"Serena Williams"),
    (2009,"Serena Williams"),(2008,"Maria Sharapova"),(2007,"Serena Williams"),
    (2006,"Amelie Mauresmo"),(2005,"Serena Williams"),(2004,"Justine Henin"),
    (2003,"Serena Williams"),(2002,"Jennifer Capriati"),(2001,"Jennifer Capriati"),
    (2000,"Lindsay Davenport"),(1999,"Martina Hingis"),(1998,"Martina Hingis"),
    (1997,"Martina Hingis"),(1996,"Monica Seles"),(1995,"Mary Pierce"),
    (1994,"Steffi Graf"),(1993,"Monica Seles"),(1992,"Monica Seles"),
    (1991,"Monica Seles"),(1990,"Steffi Graf"),(1989,"Steffi Graf"),
    (1988,"Steffi Graf"),(1987,"Hana Mandlikova"),(1985,"Martina Navratilova"),
    (1984,"Chris Evert"),(1983,"Martina Navratilova"),(1982,"Chris Evert"),
    (1981,"Martina Navratilova"),(1980,"Hana Mandlikova"),(1979,"Barbara Jordan"),
    (1978,"Chris O'Neil"),(1977,"Kerry Reid and Evonne Goolagong"),
    (1976,"Evonne Goolagong"),(1975,"Evonne Goolagong"),(1974,"Evonne Goolagong"),
]

for yr, player in aus_open_womens:
    if " and " in player:
        continue
    w = [p for p in women_pool + ["Aryna Sabalenka","Sofia Kenin","Amelie Mauresmo",
        "Barbara Jordan","Chris O'Neil","Kerry Reid"] if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the Australian Open women's singles title in {yr}?", player, w[:3], "tennis","hard"))

print(f"Australian Open womens done: {len(questions)}")

# ============================================================
# MLB - HOME RUN LEADERS BY YEAR
# ============================================================
mlb_hr_leaders = [
    (2023, "Matt Olson", 54), (2022, "Kyle Schwarber", 46), (2021, "Salvador Perez", 48),
    (2020, "Luke Voit", 22), (2019, "Pete Alonso", 53), (2018, "Khris Davis", 48),
    (2017, "Giancarlo Stanton", 59), (2016, "Mark Trumbo", 47), (2015, "Chris Davis", 47),
    (2014, "Nelson Cruz", 40), (2013, "Chris Davis", 53), (2012, "Miguel Cabrera", 44),
    (2011, "Jose Bautista", 43), (2010, "Jose Bautista", 54), (2009, "Albert Pujols", 47),
    (2008, "Ryan Howard", 48), (2007, "Alex Rodriguez", 54), (2006, "Ryan Howard", 58),
    (2005, "Andrew Jones", 51), (2004, "Adrian Beltre", 48), (2003, "Jim Thome", 47),
    (2002, "Alex Rodriguez", 57), (2001, "Barry Bonds", 73), (2000, "Sammy Sosa", 50),
    (1999, "Mark McGwire", 65), (1998, "Mark McGwire", 70), (1997, "Mark McGwire", 58),
    (1996, "Mark McGwire", 52), (1995, "Albert Belle", 50), (1994, "Ken Griffey Jr.", 40),
    (1993, "Juan Gonzalez", 46), (1992, "Juan Gonzalez", 43), (1991, "Jose Canseco", 44),
    (1990, "Cecil Fielder", 51), (1989, "Kevin Mitchell", 47), (1988, "Jose Canseco", 42),
    (1987, "Mark McGwire", 49), (1986, "Jesse Barfield", 40), (1985, "Darrell Evans", 40),
    (1984, "Mike Schmidt", 36), (1983, "Mike Schmidt", 40), (1982, "Gorman Thomas", 39),
    (1981, "Mike Schmidt", 31), (1980, "Mike Schmidt", 48), (1979, "Gorman Thomas", 45),
    (1978, "Jim Rice", 46), (1977, "George Foster", 52), (1976, "Mike Schmidt", 38),
    (1975, "Mike Schmidt", 38), (1974, "Mike Schmidt", 36), (1973, "Willie Stargell", 44),
    (1972, "Johnny Bench", 40), (1971, "Willie Stargell", 48), (1970, "Johnny Bench", 45),
    (1969, "Harmon Killebrew", 49), (1968, "Frank Howard", 44), (1967, "Harmon Killebrew", 44),
    (1966, "Frank Robinson", 49), (1965, "Willie Mays", 52), (1964, "Harmon Killebrew", 49),
    (1963, "Harmon Killebrew", 45), (1962, "Willie Mays", 49), (1961, "Roger Maris", 61),
    (1960, "Mickey Mantle", 40), (1959, "Eddie Mathews", 46), (1958, "Ernie Banks", 47),
    (1957, "Hank Aaron", 44), (1956, "Mickey Mantle", 52), (1955, "Mike Schmidt", 37),
    (1954, "Ted Kluszewski", 49), (1953, "Eddie Mathews", 47), (1952, "Ralph Kiner", 37),
    (1951, "Ralph Kiner", 42), (1950, "Ralph Kiner", 47), (1949, "Ralph Kiner", 54),
    (1948, "Ralph Kiner", 40), (1947, "Ralph Kiner", 51), (1946, "Hank Greenberg", 44),
    (1945, "Tommy Holmes", 28), (1944, "Nick Etten", 22), (1943, "Nick Etten", 14),
    (1942, "Ted Williams", 36), (1941, "Ted Williams", 37), (1940, "Hank Greenberg", 41),
    (1939, "Jimmie Foxx", 35), (1938, "Hank Greenberg", 58), (1937, "Joe DiMaggio", 46),
    (1936, "Lou Gehrig", 49), (1935, "Jimmie Foxx", 36), (1934, "Lou Gehrig", 49),
    (1933, "Jimmie Foxx", 48), (1932, "Jimmie Foxx", 58), (1931, "Babe Ruth", 46),
    (1930, "Hack Wilson", 56), (1929, "Babe Ruth", 46), (1928, "Babe Ruth", 54),
    (1927, "Babe Ruth", 60), (1926, "Babe Ruth", 47), (1925, "Rogers Hornsby", 39),
    (1924, "Babe Ruth", 46), (1923, "Babe Ruth", 41), (1922, "Ken Williams", 39),
    (1921, "Babe Ruth", 59), (1920, "Babe Ruth", 54), (1919, "Babe Ruth", 29),
]

mlb_pool = ["Barry Bonds","Mark McGwire","Sammy Sosa","Babe Ruth","Roger Maris","Hank Aaron",
    "Willie Mays","Mickey Mantle","Harmon Killebrew","Mike Schmidt","Frank Robinson","Ralph Kiner",
    "Jimmie Foxx","Lou Gehrig","Hack Wilson","George Foster","Cecil Fielder","Jose Canseco",
    "Jim Rice","Ryan Howard","Albert Pujols","Alex Rodriguez","Pete Alonso","Matt Olson",
    "Kyle Schwarber","Chris Davis","Giancarlo Stanton","Jose Bautista","Mark Trumbo",
    "Ted Williams","Joe DiMaggio","Hank Greenberg","Ernie Banks","Eddie Mathews",
    "Orlando Cepeda","Willie Stargell","Johnny Bench","Juan Gonzalez","Ken Griffey Jr.",
    "Albert Belle","Jim Thome","Adrian Beltre","Salvador Perez","Luke Voit"]

for yr, player, count in mlb_hr_leaders:
    w = [p for p in mlb_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who led the major leagues in home runs in {yr}?", player, w[:3], "baseball","hard"))
    questions.append(q(f"How many home runs did {player} hit to lead the major leagues in {yr}?", str(count), 
        [str(count+random.randint(3,12)), str(count-random.randint(3,10)), str(count+random.randint(15,25))], "baseball","hard"))

print(f"MLB HR leaders done: {len(questions)}")

# ============================================================
# NBA SCORING TITLE BY YEAR
# ============================================================
nba_scoring_title = [
    (2024,"Luka Doncic",33.9),(2023,"Joel Embiid",33.1),(2022,"Joel Embiid",30.6),
    (2021,"Bradley Beal",31.3),(2020,"James Harden",34.3),(2019,"James Harden",36.1),
    (2018,"James Harden",30.4),(2017,"Russell Westbrook",31.6),(2016,"Stephen Curry",30.1),
    (2015,"Russell Westbrook",28.1),(2014,"Kevin Durant",32.0),(2013,"Carmelo Anthony",28.7),
    (2012,"Kevin Durant",28.0),(2011,"Kevin Durant",27.7),(2010,"Kevin Durant",30.1),
    (2009,"Dwyane Wade",30.2),(2008,"LeBron James",30.0),(2007,"Kobe Bryant",31.6),
    (2006,"Kobe Bryant",35.4),(2005,"Allen Iverson",30.7),(2004,"Tracy McGrady",28.0),
    (2003,"Tracy McGrady",32.1),(2002,"Allen Iverson",31.4),(2001,"Allen Iverson",31.1),
    (2000,"Shaquille O'Neal",29.7),(1999,"Allen Iverson",26.8),(1998,"Michael Jordan",28.7),
    (1997,"Michael Jordan",29.6),(1996,"Michael Jordan",30.4),(1995,"David Robinson",29.8),
    (1994,"David Robinson",29.8),(1993,"Michael Jordan",32.6),(1992,"Michael Jordan",30.1),
    (1991,"Michael Jordan",31.5),(1990,"Michael Jordan",33.6),(1989,"Michael Jordan",32.5),
    (1988,"Michael Jordan",35.0),(1987,"Michael Jordan",37.1),(1986,"Dominique Wilkins",30.3),
    (1985,"Bernard King",32.9),(1984,"Adrian Dantley",30.6),(1983,"Alex English",28.4),
    (1982,"George Gervin",32.3),(1981,"Adrian Dantley",30.7),(1980,"George Gervin",33.1),
    (1979,"George Gervin",29.6),(1978,"George Gervin",27.2),(1977,"Pete Maravich",31.1),
    (1976,"Bob McAdoo",31.1),(1975,"Bob McAdoo",34.5),(1974,"Bob McAdoo",30.6),
    (1973,"Nate Archibald",34.0),(1972,"Kareem Abdul-Jabbar",34.8),(1971,"Kareem Abdul-Jabbar",31.7),
    (1970,"Jerry West",31.2),(1969,"Elvin Hayes",28.4),(1968,"Dave Bing",27.1),
    (1967,"Rick Barry",35.6),(1966,"Wilt Chamberlain",33.5),(1965,"Wilt Chamberlain",34.7),
    (1964,"Wilt Chamberlain",36.9),(1963,"Wilt Chamberlain",44.8),(1962,"Wilt Chamberlain",50.4),
    (1961,"Wilt Chamberlain",38.4),(1960,"Wilt Chamberlain",37.6),(1959,"Bob Pettit",29.2),
    (1958,"George Yardley",27.8),(1957,"Paul Arizin",25.6),(1956,"Bob Pettit",25.7),
]

nba_scorer_pool = ["Luka Doncic","Joel Embiid","James Harden","Russell Westbrook","Stephen Curry",
    "Kevin Durant","Carmelo Anthony","Dwyane Wade","LeBron James","Kobe Bryant","Allen Iverson",
    "Tracy McGrady","Shaquille O'Neal","Michael Jordan","David Robinson","Dominique Wilkins",
    "Bernard King","Adrian Dantley","Alex English","George Gervin","Pete Maravich","Bob McAdoo",
    "Nate Archibald","Kareem Abdul-Jabbar","Jerry West","Elvin Hayes","Dave Bing","Rick Barry",
    "Wilt Chamberlain","Bob Pettit","Paul Arizin","Elgin Baylor","Oscar Robertson",
    "Walt Bellamy","Bradley Beal","Karl Malone","Charles Barkley","Patrick Ewing","Reggie Miller"]

for yr, player, avg in nba_scoring_title:
    w = [p for p in nba_scorer_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who won the NBA scoring title for the {yr-1}-{str(yr)[2:]} season?", player, w[:3], "basketball","hard"))

print(f"NBA scoring titles done: {len(questions)}")

# ============================================================
# NFL RUSHING LEADERS
# ============================================================
nfl_rush_leaders = [
    (2023,"Christian McCaffrey",1459),(2022,"Derrick Henry",1538),(2021,"Jonathan Taylor",1811),
    (2020,"Dalvin Cook",1557),(2019,"Derrick Henry",1540),(2018,"Ezekiel Elliott",1434),
    (2017,"Kareem Hunt",1327),(2016,"LeSean McCoy",1267),(2015,"Adrian Peterson",1485),
    (2014,"DeMarco Murray",1845),(2013,"LeSean McCoy",1607),(2012,"Adrian Peterson",2097),
    (2011,"Maurice Jones-Drew",1606),(2010,"Jamaal Charles",1616),(2009,"Chris Johnson",2006),
    (2008,"Adrian Peterson",1760),(2007,"LaDainian Tomlinson",1474),(2006,"LaDainian Tomlinson",1815),
    (2005,"Shaun Alexander",1880),(2004,"Curtis Martin",1697),(2003,"Jamal Lewis",2066),
    (2002,"Ricky Williams",1853),(2001,"Priest Holmes",1555),(2000,"Edgerrin James",1709),
    (1999,"Edgerrin James",1553),(1998,"Terrell Davis",2008),(1997,"Barry Sanders",2053),
    (1996,"Barry Sanders",1553),(1995,"Emmitt Smith",1773),(1994,"Barry Sanders",1883),
    (1993,"Emmitt Smith",1486),(1992,"Emmitt Smith",1713),(1991,"Emmitt Smith",1563),
    (1990,"Barry Sanders",1304),(1989,"Christian Okoye",1480),(1988,"Eric Dickerson",1659),
    (1987,"Charles White",1374),(1986,"Eric Dickerson",1821),(1985,"Marcus Allen",1759),
    (1984,"Eric Dickerson",2105),(1983,"Eric Dickerson",1808),(1982,"Tony Dorsett",745),
    (1981,"George Rogers",1674),(1980,"Earl Campbell",1934),(1979,"Earl Campbell",1697),
    (1978,"Earl Campbell",1450),(1977,"Walter Payton",1852),(1976,"O.J. Simpson",1503),
    (1975,"O.J. Simpson",1817),(1974,"Otis Armstrong",1407),(1973,"O.J. Simpson",2003),
    (1972,"O.J. Simpson",1251),(1971,"Floyd Little",1133),(1970,"Larry Brown",1125),
    (1969,"Gale Sayers",1032),(1968,"Leroy Kelly",1239),(1967,"Jim Nance",1216),
    (1966,"Gale Sayers",1231),(1965,"Jim Brown",1544),(1964,"Jim Brown",1446),
    (1963,"Jim Brown",1863),(1962,"Jim Taylor",1474),(1961,"Jim Brown",1408),
    (1960,"Jim Brown",1257),(1959,"Jim Brown",1329),(1958,"Jim Brown",1527),
    (1957,"Jim Brown",942),
]

nfl_rusher_pool = ["Christian McCaffrey","Derrick Henry","Jonathan Taylor","Dalvin Cook","Ezekiel Elliott",
    "Kareem Hunt","LeSean McCoy","Adrian Peterson","DeMarco Murray","Maurice Jones-Drew",
    "Jamaal Charles","Chris Johnson","LaDainian Tomlinson","Shaun Alexander","Curtis Martin",
    "Jamal Lewis","Ricky Williams","Priest Holmes","Edgerrin James","Terrell Davis","Barry Sanders",
    "Emmitt Smith","Walter Payton","Earl Campbell","O.J. Simpson","Eric Dickerson","Marcus Allen",
    "Tony Dorsett","George Rogers","Jim Brown","Gale Sayers","Floyd Little","Larry Brown",
    "Jim Taylor","Leroy Kelly","Marshall Faulk","Frank Gore","Steven Jackson","DeAngelo Williams",
    "Todd Gurley","Saquon Barkley","Le'Veon Bell","Nick Chubb","Alvin Kamara","Clyde Edwards-Helaire"]

for yr, player, yards in nfl_rush_leaders:
    w = [p for p in nfl_rusher_pool if p != player]
    random.shuffle(w)
    questions.append(q(f"Who led the NFL in rushing yards in {yr}?", player, w[:3], "football","hard"))

print(f"NFL rushing leaders done: {len(questions)}")

# ============================================================
# SAVE ALL
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

import os
print(f"File size: {os.path.getsize('/Users/gabrieldidario/.openclaw/workspace/nosebleed-trivia/questions.json'):,} bytes")
