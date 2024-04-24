# Final Project
# CS 111, Hayes & Reckinger
# TODO: Comment here

#BG COLOR: #7b7a77

import turtle
import csv
import matplotlib.pyplot as plt
from PIL import Image

global_turtle_dict = {}
census_data_dict = {}
crime_data_dict = {}
num_area_dict = {}
num_crime_dict = {}
user_inputs = {}
cr_data_list = []
ce_data_list = []
ce_header = []

# Listener function for areaLookup
def areaLookupListen():
    btns_dict = global_turtle_dict["area_lookup"]
    btn1 = btns_dict["btn1"]
    btn2 = btns_dict["btn2"]
    back_btn = btns_dict["back_button"]
    btn1.onclick(searchByNumberArea)
    btn2.onclick(searchByNameArea)
    back_btn.onclick(backToMain)

# clears Screen and returns to mainmenu()
def backToMain(x,y):
    clearScreen()
    buildMainMenu()

# Builds areaLookup menu so users can easily find out what area they're searching for 
# Handles all turtle.onclicks(fx) for area menu
def buildAreaLookup(x,y):
    clearScreen()
    sc.bgpic("AreaLookup/AreaLookup.png")
    global_turtle_dict["onScreen"] = "areaLookup"
    global_turtle_dict["area_lookup"] = {}
    btns_dict = global_turtle_dict["area_lookup"]
    turtle.tracer(False)
    for i in range(1,3):
        btn = turtle.Turtle()
        btn.penup()
        btn.shape(f"AreaLookup/AreaLookup_Button{i}.gif")
        btns_dict[f"btn{i}"] = btn
        if(i == 1):
            btn.goto(100,150)
        elif(i == 2):
            btn.goto(100,0)


    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    btns_dict["text"] = text


    back_btn = turtle.Turtle()
    back_btn.penup()
    btns_dict["back_button"] = back_btn
    back_btn.shape("SharedButtons/backarrow.gif")
    back_btn.goto(-310,-300)

    areaLookupListen()

    sc.update()

# Builds Census Dict for use when searching for specific things
# Initializes listener function
def buildCensusDict(census_data_list):
    for i in range(1,len(census_data_list)):
        line = census_data_list[i]
        split_line = line.split(",")
        census_data_dict[i] = {}
        census_data_dict[i]["area_name"] = split_line[1]
        census_data_dict[i]["%housingcrowded"] = float(split_line[2])
        census_data_dict[i]["%householdbelowpov"] = float(split_line[3])
        census_data_dict[i]["%aged16+unemployed"] = float(split_line[4])
        census_data_dict[i]["%aged25+nohsdiploma"] = float(split_line[5])
        census_data_dict[i]["%minorsenior"] = float(split_line[6])
        census_data_dict[i]["percapitaincome"] = int(split_line[7])
        census_data_dict[i]["hardship_index"] = split_line[8]

# Builds Census Heatmap screen
# Initalizes listener function for back button
def buildCensusHeatmap(x,y):
    clearScreen()
    global_turtle_dict["onScreen"] = "censusHeatmap"
    sc.bgpic("CensusMenu/CensusHeatmap/CensusHeatmap.png")
    global_turtle_dict["census_menu"]["census_heatmap"] = {}
    btns_dict = global_turtle_dict["census_menu"]["census_heatmap"]
    turtle.tracer(False)
    graph = turtle.Turtle()
    graph.penup()
    turtle.addshape("Plots/CorrHeatmap.gif")
    graph.shape("Plots/CorrHeatmap.gif")
    graph.goto(100,-50)
    back_btn = turtle.Turtle()
    back_btn.penup()
    btns_dict["back_button"] = back_btn
    back_btn.shape("SharedButtons/backarrow.gif")
    back_btn.goto(-310,-300)
    censusHeatmapListen()

    sc.update()

# Builds census menu
# Initializes listener for menu
def buildCensusMenu(x,y):
    clearScreen()
    global_turtle_dict["onScreen"] = "censusMenu"
    sc.bgpic("CensusMenu/CensusMenuScene.png")
    global_turtle_dict["census_menu"] = {}
    turtle.tracer(False)
    user_inputs.clear()
    for i in range(1,3):
        btn_turtle = turtle.Turtle()
        btn_turtle.penup()
        btn_turtle.shape(f"CensusMenu/CensusMenuScene_Button{i}.gif")
        global_turtle_dict["census_menu"][f"btn_{i}"] = btn_turtle
        if(i == 1):
            btn_turtle.goto(-160,150)
        elif(i == 2):
            btn_turtle.goto(130,-140)
    back_btn = turtle.Turtle()
    back_btn.shape("CensusMenu/CensusMenuScene_BackButton.gif")
    back_btn.penup()
    global_turtle_dict["census_menu"]["back_button"] = back_btn
    back_btn.goto(155,150)
    
    sc.update()
    censusMenuListen()

# Builds CompareAreaByCensus menu
# Initializes listener function
def buildCompareAreaByCensus(x,y):
    clearScreen()
    sc.bgpic("CensusMenu/CompareAreaCensus/CompareAreaCensus.png")
    global_turtle_dict["onScreen"] = "compareAreaCensus"
    global_turtle_dict["census_menu"]["compare_area_census"] = {}
    btns_dict = global_turtle_dict["census_menu"]["compare_area_census"]
    turtle.tracer(False)

    for i in range(1,3):
        area_btn = turtle.Turtle()
        area_btn.penup()
        area_btn.shape(f"SharedButtons/Area{i}.gif")
        btns_dict[f"area_btn{i}"] = area_btn
        if(i == 1):
            area_btn.goto(-310,200)
        elif(i == 2):
            area_btn.goto(-310,100)
    
    graph_btn = turtle.Turtle()
    graph_btn.hideturtle()
    graph_btn.shape("SharedButtons/Graph.gif")
    btns_dict["graph_button"] = graph_btn
    graph_btn.penup()
    graph_btn.goto(-315,0)

    back_btn = turtle.Turtle()
    back_btn.penup()
    btns_dict["back_button"] = back_btn
    back_btn.shape("SharedButtons/backarrow.gif")
    back_btn.goto(-310,-300)

    compareAreaCensusListen()

    sc.update()

# Builds CompareAreaCrime menu
# Also initalizes listener function
def buildCompareAreaCrime(x,y):
    clearScreen()
    sc.bgpic(f"CrimeMenu/CompareAreaCrime/CompareAreaCrime.png")
    global_turtle_dict["onScreen"] = "compareAreaCrime"
    global_turtle_dict["crime_menu"]["compare_area_crime"] = {}
    btns_dict = global_turtle_dict["crime_menu"]["compare_area_crime"]
    turtle.tracer(False)

    for i in range(1,3):
        area_btn = turtle.Turtle()
        year_btn = turtle.Turtle()
        area_btn.penup()
        year_btn.penup()
        area_btn.shape(f"SharedButtons/Area{i}.gif")
        year_btn.shape(f"SharedButtons/Year{i}.gif")
        btns_dict[f"area_btn_{i}"] = area_btn
        btns_dict[f"year_btn_{i}"] = year_btn
        if(i == 1):
            area_btn.goto(-310,200)
            year_btn.goto(-310,0)
        elif(i == 2):
            area_btn.goto(-310,100)
            year_btn.goto(-310,-100)
    
    graph_btn = turtle.Turtle()
    graph_btn.penup()
    graph_btn.hideturtle()
    btns_dict["graph_button"] = graph_btn
    graph_btn.shape(f"SharedButtons/Graph.gif")
    graph_btn.goto(-315,-200)

    back_btn = turtle.Turtle()
    back_btn.penup()
    btns_dict["back_button"] = back_btn
    back_btn.shape("SharedButtons/backarrow.gif")
    back_btn.goto(-310,-300)

    compareAreaCrimeListen()
   

    sc.update()

# Builds CrimeAllAreas menu
# Also initializes listener function
def buildCrimeAllAreas(x,y):
    clearScreen()
    sc.bgpic("CrimeMenu/CrimeAllAreas/CrimeAllAreas.png")
    global_turtle_dict["onScreen"] = "crimeAllAreas"
    global_turtle_dict["crime_menu"]["crime_all_areas"] = {}
    btns_dict = global_turtle_dict["crime_menu"]["crime_all_areas"]
    turtle.tracer(False)
    for i in range(1,3):
        year_btn = turtle.Turtle()
        year_btn.shape(f"SharedButtons/Year{i}.gif")
        year_btn.penup()
        btns_dict[f"year_btn{i}"] = year_btn
        if(i == 1):
            year_btn.goto(-310,200)
        elif(i == 2):
            year_btn.goto(-310,100)
    
    graph_btn = turtle.Turtle()
    graph_btn.penup()
    graph_btn.hideturtle()
    graph_btn.shape("SharedButtons/Graph.gif")
    graph_btn.goto(-315,0)
    btns_dict["graph_button"] = graph_btn

    back_btn = turtle.Turtle()
    back_btn.penup()
    back_btn.shape("SharedButtons/backarrow.gif")
    back_btn.goto(-310,-300)
    btns_dict["back_button"] = back_btn

    crimeAllAreasListen()

    sc.update()

# Builds CrimeByYearArea menu
# Also initializes listener function for menu
def buildCrimeByYearArea(x,y):
    clearScreen()
    global_turtle_dict["onScreen"] = "crimeByYearArea"
    global_turtle_dict["crime_menu"]["crime_by_year_area"] = {}
    btns_dict = global_turtle_dict["crime_menu"]["crime_by_year_area"]
    sc.bgpic("CrimeMenu/CrimeByYearArea/CrimeByYearArea.png")
    turtle.tracer(False)
    for i in range(1,3):
        year_btn = turtle.Turtle()
        year_btn.shape(f"SharedButtons/Year{i}.gif")
        year_btn.penup()
        btns_dict[f"year_btn{i}"] = year_btn
        if(i == 1):
            year_btn.goto(-310,100)
        elif(i == 2):
            year_btn.goto(-310,0)

    crime_btn = turtle.Turtle()
    crime_btn.penup()
    crime_btn.shape("SharedButtons/Crime.gif")
    crime_btn.goto(-310,-100)
    btns_dict["crime_button"] = crime_btn

    area_btn = turtle.Turtle()
    area_btn.penup()
    area_btn.shape("SharedButtons/Area0.gif")
    area_btn.goto(-310,200)
    btns_dict["area_button"] = area_btn

    graph_btn = turtle.Turtle()
    graph_btn.penup()
    graph_btn.hideturtle()
    graph_btn.shape("SharedButtons/Graph.gif")
    graph_btn.goto(-315,-200)
    btns_dict["graph_button"] = graph_btn

    back_btn = turtle.Turtle()
    back_btn.penup()
    back_btn.shape("SharedButtons/backarrow.gif")
    back_btn.goto(-310,-300)
    btns_dict["back_button"] = back_btn

    crimeByYearAreaListen()

    sc.update()

# Builds Crime Dict for ease of access when searching for specific info
def buildCrimeDictByYear(crime_data_list):
    for i in range(1,len(crime_data_list)):
        line = crime_data_list[i]
        split_line = line.split(",")
        year = int(split_line[0])
        area = split_line[1]
        if(area):
            area = int(area)
        else:
            area = 78
        primary_type = split_line[2]
        count = split_line[3]
        if(year in crime_data_dict):
            if(area in crime_data_dict[year]):
                crime_data_dict[year][area][primary_type] = count
            else:
                crime_data_dict[year][area] = {}
                crime_data_dict[year][area][primary_type] = count
        
        else:
            crime_data_dict[year] = {}

# Builds CrimeLookup menu
# Initializes listener function for CrimeLookup menu
def buildCrimeLookup(x,y):
    clearScreen()
    global_turtle_dict["onScreen"] = "crimeLookup"
    global_turtle_dict["crime_lookup"] = {}
    user_inputs.clear()
    sc.bgpic("CrimeLookup/CrimeLookup.png")
    
    btns_dict = global_turtle_dict["crime_lookup"]
    turtle.tracer(False)
    for i in range(1,3):
        btn = turtle.Turtle()
        btn.penup()
        btn.shape(f"CrimeLookup/CrimeLookup_Button{i}.gif")
        btns_dict[f"btn{i}"] = btn
        if(i == 1):
            btn.goto(100,150)
        elif(i == 2):
            btn.goto(100,0)


    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    btns_dict["text"] = text


    back_btn = turtle.Turtle()
    back_btn.penup()
    btns_dict["back_button"] = back_btn
    back_btn.shape("SharedButtons/backarrow.gif")
    back_btn.goto(-310,-300)

    crimeLookupListen()

    sc.update()

# Builds Crime Menu
# Also initializes listener function
def buildCrimeMenu(x,y):
    clearScreen()
    global_turtle_dict["onScreen"] = "crimeMenu"
    global_turtle_dict["crime_menu"] = {}
    user_inputs.clear()
    sc.bgpic("CrimeMenu/CrimeMenuScene.png")
    turtle.tracer(False)
    for i in range(1,4):
        btn_turtle = turtle.Turtle()
        btn_turtle.penup()
        btn_turtle.shape(f"CrimeMenu/CrimeMenuScene_Button{i}.gif")
        global_turtle_dict["crime_menu"][f"btn_{i}"] = btn_turtle
        if(i == 1):
            btn_turtle.goto(-180,-265)
        elif(i == 2):
            btn_turtle.goto(120,30)
        elif(i == 3):
            btn_turtle.goto(120,-268)
    back_btn = turtle.Turtle()
    back_btn.penup()
    back_btn.shape(f"CrimeMenu/CrimeMenuScene_BackButton.gif")
    global_turtle_dict["crime_menu"]["back_button"] = back_btn
    back_btn.goto(335,-268)
    sc.update()
    crimeMenuListen()

# Builds two dicts for ease of access when searching for specific information
def buildData():
    census_data_list = getFileDataList("Data/Census2008-2012.csv")
    crime_data_list = getFileDataList("Data/CrimeData2001-Present.csv")
    buildCensusDict(census_data_list)
    buildCrimeDictByYear(crime_data_list)

# Builds all variables for a given plotting function based on onScreen
def buildGraph(x,y):
    screen = global_turtle_dict["onScreen"]
    if(screen == "compareAreaCrime"):
        year_range = buildYearRange()
        area1 = user_inputs["area1"]
        area2 = user_inputs["area2"]
        plotTop5CrimeTypes(year_range,area1,area2)
    elif(screen == "crimeByYearArea"):
        year_range = buildYearRange()
        area1 = user_inputs["area1"]
        crime = user_inputs["crime"]
        plotCrimeByYearArea(year_range, area1, crime)
    elif(screen == "crimeAllAreas"):
        year_range = buildYearRange()
        plotScatterArea(year_range)
    elif(screen == "compareAreaCensus"):
        area1 = user_inputs["area1"]
        area2 = user_inputs["area2"]
        plotCensusStack(area1, area2)

# Adds minor highlighting to buttons on the main_menu
def buildMainButtonTracers():


    #Crime Color: #0046aa
    #Census Color: #ffea00
    #AreaLookup Color: #891688
    #CrimeLookup Color: #fea711
    #Background Color: #7b7a77
    turtle.tracer(True)

    width = 3
    speed = 5

    #Crime Tracers
    crime_tracer = turtle.Turtle()
    crime_eraser = turtle.Turtle()
    crime_tracer.hideturtle()
    crime_eraser.hideturtle()
    
    crime_tracer.penup()
    crime_eraser.penup()

    crime_tracer.color("#0046aa")
    crime_eraser.color("#7b7a77")
    crime_top_l_cord = (37,175)
    crime_bot_r_cord = (-133,-20)
    crime_tracer.goto(crime_bot_r_cord[0], crime_bot_r_cord[1])
    crime_eraser.goto(crime_bot_r_cord[0], crime_bot_r_cord[1])
    crime_tracer.pendown()
    crime_eraser.pendown()
    crime_tracer.speed(speed)
    crime_eraser.speed(speed)

    crime_tracer.width(width)
    crime_eraser.width(width)

    #Census Tracers
    census_tracer = turtle.Turtle()
    census_eraser = turtle.Turtle()
    census_tracer.hideturtle()
    census_eraser.hideturtle()
    
    census_tracer.penup()
    census_eraser.penup()

    census_tracer.color("#ffea00")
    census_eraser.color("#7b7a77")
    census_top_l_cord = (37,-130)
    census_bot_r_cord = (-133,-310)
    census_tracer.goto(census_bot_r_cord[0], census_bot_r_cord[1])
    census_eraser.goto(census_bot_r_cord[0], census_bot_r_cord[1])
    census_tracer.pendown()
    census_eraser.pendown()
    census_tracer.speed(speed)
    census_eraser.speed(speed)

    census_tracer.width(width)
    census_eraser.width(width)
    
    #CrimeLkpTurtles
    crimelkp_tracer = turtle.Turtle()
    crimelkp_eraser = turtle.Turtle()
    crimelkp_tracer.hideturtle()
    crimelkp_eraser.hideturtle()
    
    crimelkp_tracer.penup()
    crimelkp_eraser.penup()

    crimelkp_tracer.color("#fea711")
    crimelkp_eraser.color("#7b7a77")
    crimelkp_top_l_cord = (350,-130)
    crimelkp_bot_r_cord = (165,-310)
    crimelkp_tracer.goto(crimelkp_bot_r_cord[0], crimelkp_bot_r_cord[1])
    crimelkp_eraser.goto(crimelkp_bot_r_cord[0], crimelkp_bot_r_cord[1])
    crimelkp_tracer.pendown()
    crimelkp_eraser.pendown()
    crimelkp_tracer.speed(speed)
    crimelkp_eraser.speed(speed)

    crimelkp_tracer.width(width)
    crimelkp_eraser.width(width)

    #ArealkpTurtles
    arealkp_tracer = turtle.Turtle()
    arealkp_eraser = turtle.Turtle()
    arealkp_tracer.hideturtle()
    arealkp_eraser.hideturtle()
    
    arealkp_tracer.penup()
    arealkp_eraser.penup()

    arealkp_tracer.color("#891688")
    arealkp_eraser.color("#7b7a77")
    arealkp_top_l_cord = (350,175)
    arealkp_bot_r_cord = (165,-20)
    arealkp_tracer.goto(arealkp_bot_r_cord[0], arealkp_bot_r_cord[1])
    arealkp_eraser.goto(arealkp_bot_r_cord[0], arealkp_bot_r_cord[1])
    arealkp_tracer.pendown()
    arealkp_eraser.pendown()
    arealkp_tracer.speed(speed)
    arealkp_eraser.speed(speed)

    arealkp_tracer.width(width)
    arealkp_eraser.width(width)


    while(global_turtle_dict["onScreen"] == "mainMenu"):

        #Step1
        crime_tracer.goto(crime_bot_r_cord[0], crime_bot_r_cord[1])
        crime_eraser.goto(crime_bot_r_cord[0], crime_bot_r_cord[1])

        census_tracer.goto(census_bot_r_cord[0], census_bot_r_cord[1])
        census_eraser.goto(census_bot_r_cord[0], census_bot_r_cord[1])

        crimelkp_tracer.goto(crimelkp_bot_r_cord[0], crimelkp_bot_r_cord[1])
        crimelkp_eraser.goto(crimelkp_bot_r_cord[0], crimelkp_bot_r_cord[1])

        arealkp_tracer.goto(arealkp_bot_r_cord[0], arealkp_bot_r_cord[1])
        arealkp_eraser.goto(arealkp_bot_r_cord[0], arealkp_bot_r_cord[1])


        #Step2
        crime_tracer.goto(crime_bot_r_cord[0], crime_top_l_cord[1])
        crime_eraser.goto(crime_bot_r_cord[0], crime_top_l_cord[1])

        census_tracer.goto(census_bot_r_cord[0], census_top_l_cord[1])
        census_eraser.goto(census_bot_r_cord[0], census_top_l_cord[1])

        crimelkp_tracer.goto(crimelkp_bot_r_cord[0], crimelkp_top_l_cord[1])
        crimelkp_eraser.goto(crimelkp_bot_r_cord[0], crimelkp_top_l_cord[1])

        arealkp_tracer.goto(arealkp_bot_r_cord[0], arealkp_top_l_cord[1])
        arealkp_eraser.goto(arealkp_bot_r_cord[0], arealkp_top_l_cord[1])

        #Step3
        crime_tracer.goto(crime_top_l_cord[0], crime_top_l_cord[1])
        crime_eraser.goto(crime_top_l_cord[0], crime_top_l_cord[1])

        census_tracer.goto(census_top_l_cord[0], census_top_l_cord[1])
        census_eraser.goto(census_top_l_cord[0], census_top_l_cord[1])

        crimelkp_tracer.goto(crimelkp_top_l_cord[0], crimelkp_top_l_cord[1])
        crimelkp_eraser.goto(crimelkp_top_l_cord[0], crimelkp_top_l_cord[1])

        arealkp_tracer.goto(arealkp_top_l_cord[0], arealkp_top_l_cord[1])
        arealkp_eraser.goto(arealkp_top_l_cord[0], arealkp_top_l_cord[1])

        #Step4
        crime_tracer.goto(crime_top_l_cord[0], crime_bot_r_cord[1])
        crime_eraser.goto(crime_top_l_cord[0], crime_bot_r_cord[1])

        census_tracer.goto(census_top_l_cord[0], census_bot_r_cord[1])
        census_eraser.goto(census_top_l_cord[0], census_bot_r_cord[1])

        crimelkp_tracer.goto(crimelkp_top_l_cord[0], crimelkp_bot_r_cord[1])
        crimelkp_eraser.goto(crimelkp_top_l_cord[0], crimelkp_bot_r_cord[1])

        arealkp_tracer.goto(arealkp_top_l_cord[0], arealkp_bot_r_cord[1])
        arealkp_eraser.goto(arealkp_top_l_cord[0], arealkp_bot_r_cord[1])

# Builds the Main Menu
# Starts listener and tracer function
def buildMainMenu():
    sc = global_turtle_dict["Screen"]
    user_inputs.clear()
    sc.bgpic('MainMenu/MainScene.png')
    global_turtle_dict["main_menu"] = {}
    global_turtle_dict["onScreen"] = "mainMenu"
    turtle.tracer(False)
    for i in range(1,5):
        btn_turtle = turtle.Turtle()
        btn_turtle.penup()
        btn_turtle.shape(f"MainMenu/MainScene_Button{i}.gif")
        global_turtle_dict["main_menu"][f"btn_{i}"] = btn_turtle
        if(i == 1):
            btn_turtle.goto(-52,77)
        elif(i == 2):
            btn_turtle.goto(-52,-220)
        elif(i == 3):
            btn_turtle.goto(255,77)
        elif(i == 4):
            btn_turtle.goto(255,-220)
    sc.update()

    #buildMainButtonTracers()
    mainMenuListen()
    buildMainButtonTracers()

# Builds another data container for directly pulling area_num or area_name
#1-77 Areas(78 being chicago)
def buildNumAreaDict():
    for num in census_data_dict:
        area_name = census_data_dict[num]["area_name"]
        num_area_dict[num] = area_name

# Builds another data container for directly pulling crime_index or crime_type
# 1-37 Crime Types
def buildNumCrimeDict():
    firstKey = True
    for year in crime_data_dict:
        year_dict = crime_data_dict[year]
        for area in year_dict:
            area_dict = year_dict[area]
            for crime_type in area_dict:
                if(crime_type not in list(num_crime_dict.values())):
                    if(firstKey):
                        max_key = 0
                        firstKey = False
                    else:
                        max_key = max(list(num_crime_dict.keys()))
                    num_crime_dict[max_key + 1] = crime_type
    num_crime_dict[37] = "ALL"

# Builds and sets up the screen for the turtle graphics
def buildScreen():
    sc = turtle.Screen()
    sc.setup(800,700)
    turtle.hideturtle()
    global_turtle_dict["Screen"] = sc

# Builds all static turtle shapes for use as buttons within the menus
def buildShapes():
    main_path = "MainMenu/"
    cr_menu_path = "CrimeMenu/"
    ce_menu_path = "CensusMenu/"
    turtle.addshape(f"{main_path}MainScene_Button1.gif")
    turtle.addshape(f"{main_path}MainScene_Button2.gif")
    turtle.addshape(f"{main_path}MainScene_Button3.gif")
    turtle.addshape(f"{main_path}MainScene_Button4.gif")
    turtle.addshape(f"{cr_menu_path}CrimeMenuScene_BackButton.gif")
    turtle.addshape(f"{cr_menu_path}CrimeMenuScene_Button1.gif")
    turtle.addshape(f"{cr_menu_path}CrimeMenuScene_Button2.gif")
    turtle.addshape(f"{cr_menu_path}CrimeMenuScene_Button3.gif")
    turtle.addshape(f"{ce_menu_path}CensusMenuScene_Button1.gif")
    turtle.addshape(f"{ce_menu_path}CensusMenuScene_Button2.gif")
    turtle.addshape(f"{ce_menu_path}CensusMenuScene_BackButton.gif")
    turtle.addshape("AreaLookup/AreaLookup_Button1.gif")
    turtle.addshape("AreaLookup/AreaLookup_Button2.gif")
    turtle.addshape("CrimeLookup/CrimeLookup_Button1.gif")
    turtle.addshape("CrimeLookup/CrimeLookup_Button2.gif")


    turtle.addshape("SharedButtons/Area0.gif")
    turtle.addshape("SharedButtons/Area1.gif")
    turtle.addshape("SharedButtons/Area2.gif")
    turtle.addshape("SharedButtons/Year1.gif")
    turtle.addshape("SharedButtons/Year2.gif")
    turtle.addshape("SharedButtons/Graph.gif")
    turtle.addshape("SharedButtons/backarrow.gif")
    turtle.addshape("SharedButtons/Crime.gif")

# Takes two years and creates a tuple with the lower year being the first element
# Returns the year_range as a tuple
def buildYearRange():
    year1 = int(user_inputs["year1"])
    year2 = int(user_inputs["year2"])
    if year1 < year2:
        lo_year = year1
        hi_year = year2
    elif year2 < year1:
        lo_year = year2
        hi_year = year1
    else:
        lo_year = year1
        hi_year = year1

    year_range = (lo_year,hi_year)
    return year_range

# Calculates the correlation matrix
# Used when creating the correlation heatmap for the data
def calculateCorrMatrix():
    data = [row[2:] for row in ce_data_list]
    num_columns = len(ce_header[2:])
    num_rows = len(data)
    correlation_matrix = [[0] * num_columns for _ in range(num_columns)]

    for i in range(num_columns):
        for j in range(num_columns):
            col_i = [float(row[i]) for row in data]
            col_j = [float(row[j]) for row in data]

            #Computes correlation coefficient (Using Pearson's r formula)
            mean_i = sum(col_i) / num_rows
            mean_j = sum(col_j) / num_rows
            numerator = sum((col_i[k] - mean_i) * (col_j[k] - mean_j) for k in range(num_rows))
            denom_i = sum((col_i[k] - mean_i) ** 2 for k in range(num_rows)) ** 0.5
            denom_j = sum((col_j[k] - mean_j) ** 2 for k in range(num_rows)) ** 0.5
            correlation_matrix[i][j] = numerator / (denom_i * denom_j)

    return correlation_matrix

# Listener Function for census heatmap
# Handles all turtle.onclicks(fx) for back button navigation
def censusHeatmapListen():
    menu_btns = global_turtle_dict["census_menu"]["census_heatmap"]
    back_btn = menu_btns["back_button"]
    back_btn.onclick(buildCensusMenu)

# Listener Function for census_menu
# Handles all turtle.onclicks(fx) for census menu
def censusMenuListen():
    menu_btns = global_turtle_dict["census_menu"]
    compare_areas_btn = menu_btns["btn_1"]
    heatmap_btn = menu_btns["btn_2"]
    back_btn = menu_btns["back_button"]
    compare_areas_btn.onclick(buildCompareAreaByCensus)
    heatmap_btn.onclick(buildCensusHeatmap)
    back_btn.onclick(backToMain)

# Checks to see if a given input is within the range of our area data
# Returns an error if area cannot be found, or if the area was already selected
def checkArea(area,num):
    error = ""
    if(area.isdigit()):
        area = int(area)
        if(1 <= area <= 78):
            if(f"area{num}" in user_inputs):
                if area == user_inputs[f"area{num}"]:
                    error = "ERROR: Area already selected"
        else:
            error = "ERROR: Area not found"
    else:
        error = "ERROR: Please type in a number 1-78"
    return error

#Checks to see if a particular crime_num is within the range of our crime data
# Returns an error if crime cannot be found or crime is already selected
def checkCrime(crime_num):
    error = ""
    if(crime_num.isdigit()):
        crime_num = int(crime_num)
        if(1 <= crime_num <= 37):
            if("crime" in user_inputs):
                if crime_num == user_inputs["crime"]:
                    error = "ERROR: Crime already selected"
        else:
            error = "ERROR: Crime not found"
    else:
        error = "ERROR: Please type in a number 1-37"
    return error

# Checks to see if user_inputs contains enough elements to show the graph_btn
def checkGraph():
    onScreen = global_turtle_dict["onScreen"]
    if(onScreen == "compareAreaCrime"):
        if("area1" in user_inputs and "area2" in user_inputs):
            if("year1" in user_inputs and "year2" in user_inputs):
                compare_area_crime_dict = global_turtle_dict["crime_menu"]["compare_area_crime"]
                graph_btn = compare_area_crime_dict["graph_button"]
                graph_btn.showturtle()
                sc.update()
    elif(onScreen == "crimeByYearArea"):
        if("area1" in user_inputs and "crime" in user_inputs):
            if("year1" in user_inputs and "year2" in user_inputs):
                crime_by_year_area_dict = global_turtle_dict["crime_menu"]["crime_by_year_area"]
                graph_btn = crime_by_year_area_dict["graph_button"]
                graph_btn.showturtle()
                sc.update()
    elif(onScreen == "compareAreaCensus"):
        if("area1" in user_inputs and "area2" in user_inputs):
            area_census_dict = global_turtle_dict["census_menu"]["compare_area_census"]
            graph_btn = area_census_dict["graph_button"]
            graph_btn.showturtle()
            sc.update()
    elif(onScreen == "crimeAllAreas"):
        if("year1" in user_inputs and "year2" in user_inputs):
                crime_by_year_area_dict = global_turtle_dict["crime_menu"]["crime_all_areas"]
                graph_btn = crime_by_year_area_dict["graph_button"]
                graph_btn.showturtle()
                sc.update()

# Checks to see if a given year is within the range 2001 to 2024
# Returns an error code if year cannot be found or is not within range
def checkYear(year,num):
    error = ""
    if(year.isdigit()):
        year = int(year)
        if(2001 <= year <= 2024):
            if(num == 1):
                if("year2" in user_inputs and year == user_inputs["year2"]):
                    error = "ERROR: Year1 == Year2, please select a new bound"
            elif(num == 2):
                if("year1" in user_inputs and year == user_inputs["year1"]):
                    error = "ERROR: Year2 == Year1, please select a new bound"
        else:
            error = "ERROR: Year is out of range, select a year between 2001-2024"
    else:
        error = "ERROR: Please enter a number"
    return error

# Clears the screen
#Used whenever changing scenes
def clearScreen():
    sc = global_turtle_dict["Screen"]
    sc.clear()

# Listener function for compare_area_census menu
# Handles all turtle.onclick(fx) for comparea_area_census menu
def compareAreaCensusListen():
    btns_dict = global_turtle_dict["census_menu"]["compare_area_census"]
    area_btn1 = btns_dict["area_btn1"]
    area_btn2 = btns_dict["area_btn2"]
    graph_btn = btns_dict["graph_button"]
    back_btn = btns_dict["back_button"]
    area_btn1.onclick(inputArea1)
    area_btn2.onclick(inputArea2)
    graph_btn.onclick(buildGraph)
    back_btn.onclick(buildCensusMenu)

# Listener function for compare_area_crime menu
# Handles all turtle.onclicks(fx) for compare_crime_area menu
def compareAreaCrimeListen():
    compare_area_crime_dict = global_turtle_dict["crime_menu"]["compare_area_crime"]
    area_btn1 = compare_area_crime_dict["area_btn_1"]
    area_btn2 = compare_area_crime_dict["area_btn_2"]
    year_btn1 = compare_area_crime_dict["year_btn_1"]
    year_btn2 = compare_area_crime_dict["year_btn_2"]
    graph_btn = compare_area_crime_dict["graph_button"]
    back_btn = compare_area_crime_dict["back_button"]
    area_btn1.onclick(inputArea1)
    area_btn2.onclick(inputArea2)
    year_btn1.onclick(inputYear1)
    year_btn2.onclick(inputYear2)
    graph_btn.onclick(buildGraph)
    back_btn.onclick(buildCrimeMenu)

# Listener function for crime in all areas menu
# Handles all turtle.onclicks(fx) for crime_in_all_areas menu
def crimeAllAreasListen():
    btns_dict = global_turtle_dict["crime_menu"]["crime_all_areas"]
    year1_btn = btns_dict["year_btn1"]
    year2_btn = btns_dict["year_btn2"]
    graph_btn = btns_dict["graph_button"]
    back_btn = btns_dict["back_button"]
    year1_btn.onclick(inputYear1)
    year2_btn.onclick(inputYear2)
    graph_btn.onclick(buildGraph)
    back_btn.onclick(buildCrimeMenu)

# Listener function for crime_by_year_area menu
# Handles all turtle.onclicks(fx) for crime_by_year_area menu
def crimeByYearAreaListen():
    btns_dict = global_turtle_dict["crime_menu"]["crime_by_year_area"]
    area_btn = btns_dict["area_button"]
    year1_btn = btns_dict["year_btn1"]
    year2_btn = btns_dict["year_btn2"]
    crime_btn = btns_dict["crime_button"]
    graph_btn = btns_dict["graph_button"]
    back_btn = btns_dict["back_button"]
    area_btn.onclick(inputArea0)
    year1_btn.onclick(inputYear1)
    year2_btn.onclick(inputYear2)
    crime_btn.onclick(inputCrime)
    graph_btn.onclick(buildGraph)
    back_btn.onclick(buildCrimeMenu)

# Listener function for Crime Lookup menu
# Handles all turtle.onclicks() within crime_lookup
def crimeLookupListen():
    btns_dict = global_turtle_dict["crime_lookup"]
    btn1 = btns_dict["btn1"]
    btn2 = btns_dict["btn2"]
    back_btn = btns_dict["back_button"]
    btn1.onclick(searchByNumberCrime)
    btn2.onclick(searchByNameCrime)
    back_btn.onclick(backToMain)

# Listener function for crime_menu
# Handles all turtle.onclick(fx) within crime_menu
def crimeMenuListen():
    menu_btns = global_turtle_dict["crime_menu"]
    compare_area_btn = menu_btns["btn_1"]
    crime_year_area_btn = menu_btns["btn_2"]
    crime_all_areas_btn = menu_btns["btn_3"]
    back_btn = menu_btns["back_button"]
    compare_area_btn.onclick(buildCompareAreaCrime)
    crime_year_area_btn.onclick(buildCrimeByYearArea)
    crime_all_areas_btn.onclick(buildCrimeAllAreas)
    back_btn.onclick(backToMain)

# Filters data by area
# Returns a list of filtered_area_data
def filterDataByAreaCensus(data,area_num):
    filtered_data = [row for row in data if row[0] == str(area_num)]
    for row in filtered_data:
        row.pop(7)
    return filtered_data

# Filter filtered_year_data by community area
# Returns a list only including crime data from a specific area
def filterDataByCommunityArea(data,area_num):
    filtered_data = [row for row in data if row[1] == str(area_num)]
    return filtered_data

# Filter the year and area data by crime type
# Returns a list only including a specific crime_type
def filterDataByCrimeType(data, crime_type):
    filtered_data = [row for row in data if row[2] == crime_type]
    return filtered_data

# Read data from CSV file and filter it down by year
# Returned filtered data by year
def filterDataByYear(year_range):
    data = cr_data_list
    filtered_data = []
    lo_year = int(year_range[0])
    hi_year = int(year_range[1])
    for row in data:
        year = int(row[0])
        if(lo_year <= year <= hi_year):
            filtered_data.append(row)
    return filtered_data

# Finds an area given either its name or associated number
# For use in search functions
# Returns a string containing area_number and area_name
def findArea(info):
    return_info = ""
    if(type(info) == int or info.isdigit()):
        user_num = int(info)
        if(user_num in census_data_dict):
            area_name = census_data_dict[user_num]["area_name"]
            return_info = f"{user_num}: {area_name}"
        else:
            return_info = "{user_num}: Area Not Found"
    elif(type(info) == str):
        user_area = info
        up_user_area = (user_area.upper()).replace(" ", "")
        areaFound = False
        for area_num in census_data_dict:
            area_name = census_data_dict[area_num]["area_name"]
            up_area_name = (area_name.upper()).replace(" ", "")
            if(up_user_area == up_area_name):
                areaFound = True
                return_info = f"{area_num}: {area_name}"
        if(not areaFound):
            return_info = f"{user_area} not found!"
    else:
        return_info = f"Area not found!"
    return return_info

# Finds a specific crime_type given either its name or associated integer
# For use in search functions
# Returns a string including crime_index_num and crime_name
def findCrime(info):
    return_info = ""
    if(info.isdigit()):
        user_num = int(info)
        if(user_num in num_crime_dict):
            crime = num_crime_dict[user_num]
        else:
            crime = "Crime Not Found"
        return_info = f"{user_num}:\n{crime}"
    elif(type(info) == str):
        user_crime = info
        up_user_crime = (user_crime.upper()).replace(" ", "")
        crimeFound = False
        for crime_num in num_crime_dict:
            crime_type = num_crime_dict[crime_num]
            no_spaces_crime_type = crime_type.replace(" ", "")
            if(up_user_crime == no_spaces_crime_type):
                crimeFound = True
                return_info = f"{crime_num}:\n{crime_type}"
        if(not crimeFound):
            return_info = f"{user_crime} not found!"
    else:
        return_info = "Crime not found!"
    
    return return_info

# Processes raw data from a file into a list given a filename
# Returns a list of each line from the file
def getFileDataList(filename):
    data_list = []
    with open(filename) as file:
        raw_data_list = file.readlines()
    for line in raw_data_list:
        data_list.append(line.strip('\n'))
    return data_list

# Finds and sets an area in user_inputs for use in plotting functions
# Searches, errorchecks, and checks to see if the user can graph
def inputArea0(x,y):
    area = turtle.textinput("Area", "Type in a number 1-78(78 being all)")
    if(area):
        error = checkArea(area,0)
        if(error):
            print(error)
            print("Please Try Again!")
        else:
            user_inputs["area1"] = int(area)
    checkGraph()

# Finds and sets an area in user_inputs for use in plotting functions
# Searches, errorchecks, and checks to see if the user can graph
def inputArea1(x,y):
    area = turtle.textinput("Area1","Type in a number 1-78(78 being all)")
    if(area):
        error = checkArea(area,1)
        if(error):
            print(error)
            print("Please Try Again!")
        else:
            user_inputs["area1"] = int(area)
    checkGraph()

# Finds and sets an area in user_inputs for use in plotting functions
# Searches, errorchecks, and checks to see if the user can graph
def inputArea2(x,y):
    area = turtle.textinput("Area2","Type in a number 1-78(78 being all)")
    if(area):
        error = checkArea(area,2)
        if(error):
            print(error)
            print("Please Try Again!")
        else:
            user_inputs["area2"] = int(area)
    checkGraph()

# Finds and sets a crime_type in user_inputs for use in plotting functions
# Searches, errorchecks, and checks to see if the user can graph
def inputCrime(x,y):
    crime_num = turtle.textinput("Crime Type", "Type in a number 1-37(37 being all)")
    if(crime_num):
        error = checkCrime(crime_num)
        if(error):
            print(error)
        else:
            user_inputs["crime"] = crime_num
    checkGraph()

# Finds and sets a year in user_inputs for use in plotting functions
# Searches, errorchecks, and checks to see if the user can graph
def inputYear1(x,y):
    year = turtle.textinput("Year 1","Year must be between 2001-2024")
    if(year):
        error = checkYear(year,1)
        if(error):
            print(error)
            print("Please Try Again!")
        else:
            user_inputs["year1"] = int(year)
    checkGraph()

# Finds and sets a year in user_inputs for use in plotting functions
# Searches, errorchecks, and checks to see if the user can graph
def inputYear2(x,y):
    year = turtle.textinput("Year 2","Year must be between 2001-2024")
    if(year):
        error = checkYear(year,2)
        if(error):
            print(error)
            print("Please Try Again!")
        else:
            user_inputs["year2"] = int(year)
    checkGraph()

# listener function
# Contains the turtle.onclick(fx) functions for all main menu buttons
def mainMenuListen():
    menu_btns = global_turtle_dict["main_menu"]
    crime_btn = menu_btns["btn_1"]
    census_btn = menu_btns["btn_2"]
    area_lookup_btn = menu_btns["btn_3"]
    crime_lookup_btn = menu_btns["btn_4"]
    crime_btn.onclick(buildCrimeMenu)
    census_btn.onclick(buildCensusMenu)
    area_lookup_btn.onclick(buildAreaLookup)
    crime_lookup_btn.onclick(buildCrimeLookup)

# Plots stack plot for census data so user can compare two areas
# Saves plot to a .gif file and changes turtle shape to allow for plot display
def plotCensusStack(area1_num, area2_num):
    column_names = ce_header[2:]
    census_data = ce_data_list
    area1_data = filterDataByAreaCensus(census_data, area1_num)
    area2_data = filterDataByAreaCensus(census_data, area2_num)
    area1_counts = [float(d) for d in area1_data[0][2:]]
    area2_counts = [float(d) for d in area2_data[0][2:]]

    area1_info = findArea(area1_num)
    area2_info = findArea(area2_num)

    fig, ax = plt.subplots(figsize = (12,10),facecolor = "#7b7a77", edgecolor = "#131313")

    ax.bar(range(len(column_names)), area1_counts, label = f"{area1_info}", color = "blue")

    ax.bar(range(len(column_names)), area2_counts, bottom = area1_counts, label = f"{area2_info}", color = "orange")

    ax.set_xticks(range(len(column_names)))
    ax.set_xticklabels(column_names, rotation = 45, ha = "right")
    ax.set_xlabel("Indices")
    ax.set_ylabel("Counts")
    ax.set_title("Census Data Comparison")
    ax.legend()




    plt.tight_layout()
    fig.savefig("Plots/CensusPlot.png")



    rsz_image = scaleImage("Plots/CensusPlot.png",0.5)
    rsz_image.save("Plots/CensusPlot.gif")

    plot_turtle = turtle.Turtle()
    turtle.addshape("Plots/CensusPlot.gif")
    plot_turtle.shape("Plots/CensusPlot.gif")
    plot_turtle.goto(75,-20)
    sc.update()

# Plots correlation heatmap and saves it to a .gif type for use when the associated scene is called
def plotCorrHeatmap():

    correlation_matrix = calculateCorrMatrix()
    header = ce_header
    plt.figure(figsize = (12,10), facecolor = "#7b7a77", edgecolor = "#131313")
    plt.imshow(correlation_matrix, cmap = "coolwarm", interpolation = "nearest")

    for i in range(len(correlation_matrix)):
        for j in range(len(correlation_matrix)):
            plt.text(j,i, "{:.2f}".format(correlation_matrix[i][j]), ha = "center", va = "center", color = "black")
    
    plt.xticks(range(len(header) - 2), header[2:], rotation = 90)
    plt.yticks(range(len(header) - 2), header[2:])
    plt.title("Correlation Heatmap of Census Indicators")
    plt.tight_layout()
    plt.savefig("Plots/CorrHeatmap.png")
    rsz_image = scaleImage("Plots/CorrHeatmap.png",0.5)
    rsz_image.save("Plots/CorrHeatmap.gif", "GIF")



# Plots crime_types within a specific area on a given year_range
def plotCrimeByYearArea(year_range, area_num, crime_num):
    filtered_year_data = filterDataByYear(year_range)
    if(area_num != 78):
        filtered_area_data = filterDataByCommunityArea(filtered_year_data,area_num)
    else:
        filtered_area_data = filtered_year_data
    crime_type = num_crime_dict[int(crime_num)]
    if(crime_type != "ALL"):
        final_data = filterDataByCrimeType(filtered_area_data, crime_type)
    else:
        final_data = filtered_area_data

    lo_year = year_range[0]
    hi_year = year_range[1]

    area_info = findArea(area_num)

    crime_counts = {}
    for row in final_data:
        year = int(row[0])
        count = int(row[3])
        crime_counts[year] = crime_counts.get(year, 0) + count
    
    years = list(crime_counts.keys())
    counts_list = list(crime_counts.values())

    plt.figure(figsize = (12,10),facecolor = "#7b7a77", edgecolor = "#131313")
    plt.bar(years, counts_list)
    plt.xlabel("Year")
    plt.ylabel(f"{crime_type} Count")
    plt.title(f"{crime_type} Count from {lo_year} to {hi_year} in {area_info}")
    plt.savefig("Plots/CrimeByYearArea.png")


    rsz1_image = scaleImage("Plots/CrimeByYearArea.png",0.5)
    rsz1_image.save("Plots/CrimeByYearArea.gif", "GIF")

    plot_turtle = turtle.Turtle()
    turtle.addshape("Plots/CrimeByYearArea.gif")
    plot_turtle.shape("Plots/CrimeByYearArea.gif")
    plot_turtle.goto(75,0)

    sc.update()

# Plots scatterplot for all areas for all crimes within a given range
def plotScatterArea(year_range):
    filtered_year_data = filterDataByYear(year_range)
    lo_year = year_range[0]
    hi_year = year_range[1]
    area_counts = {}
    for row in filtered_year_data:
        area = row[1]
        count = int(row[3])
        if area in area_counts:
            area_counts[area] += count
        else:
            area_counts[area] = count

    areas_list = list(area_counts.keys())
    counts = list(area_counts.values())

    plt.figure(figsize = (12,6),facecolor = "#7b7a77", edgecolor = "#131313")
    plt.scatter(areas_list, counts)
    plt.title(f"Total Crimes Count by Area from {lo_year} to {hi_year}")
    plt.xlabel("Area")
    plt.ylabel("Total Count")

    
    for i in range(len(areas_list)):
        txt = areas_list[i]
        plt.annotate(txt, (areas_list[i], counts[i]), xytext = (5,5), textcoords = "offset points")
    
    plt.grid(True)
    plt.xticks([])
    plt.tight_layout()
    plt.savefig("Plots/ScatterPlot.png")

    rsz1_image = scaleImage("Plots/ScatterPlot.png",0.5)
    rsz1_image.save("Plots/ScatterPlot.gif", "GIF")

    plot_turtle = turtle.Turtle()
    plot_turtle.penup()
    turtle.addshape("Plots/ScatterPlot.gif")
    plot_turtle.shape("Plots/ScatterPlot.gif")
    plot_turtle.goto(75,0)
    sc.update()

# Plots 5 most common crime types in two areas in a range of years
def plotTop5CrimeTypes(year_range,area1,area2):
    filtered_year_data1 = filterDataByYear(year_range)
    filtered_area_data1 = filterDataByCommunityArea(filtered_year_data1,area1)
    
    filtered_year_data2 = filterDataByYear(year_range)
    filtered_area_data2 = filterDataByCommunityArea(filtered_year_data2, area2)

    crime_type_counts1 = {}
    for row in filtered_area_data1:
        crime_type = row[2]
        count = int(row[3])
        crime_type_counts1[crime_type] = crime_type_counts1.get(crime_type,0) + count
    
    crime_type_counts2 = {}
    for row in filtered_area_data2:
        crime_type = row[2]
        count = int(row[3])
        crime_type_counts2[crime_type] = crime_type_counts2.get(crime_type,0) + count
    
    sorted_crime_types1 = sorted(crime_type_counts1.items(), key = sortBySecondElement, reverse = True)[:5]
    sorted_crime_types2 = sorted(crime_type_counts2.items(), key = sortBySecondElement, reverse = True)[:5]

    fig, axs = plt.subplots(1,2, figsize = (12,6), facecolor = "#7b7a77", edgecolor = "#131313")


    area1_info = findArea(area1)
    #Plot1
    crime_types1 = []
    counts1 = []
    for crime_type_count in sorted_crime_types1:
        crime_type,count = crime_type_count
        crime_types1.append(crime_type)
        counts1.append(count)
    axs[0].bar(crime_types1, counts1, color = "lightblue")
    axs[0].set_title(f"Top 5 Crime Types in Community Area {area1_info}")
    axs[0].set_xlabel("Crime Type")
    axs[0].set_ylabel("Count")
    axs[0].tick_params(axis = "x", rotation = 45)

    area2_info = findArea(area2)
    #Plot2
    crime_types2 = []
    counts2 = []
    for crime_type_count in sorted_crime_types2:
        crime_type,count = crime_type_count
        crime_types2.append(crime_type)
        counts2.append(count)
    axs[1].bar(crime_types2, counts2, color = "lightcoral")
    axs[1].set_title(f"Top 5 Crime Types in Community Area {area2_info}")
    axs[1].set_xlabel("Crime Type")
    axs[1].set_ylabel("Count")
    axs[1].tick_params(axis = "x", rotation = 45)

    plt.tight_layout()
    plt.savefig("Plots/CompAreasCrime.png")

    rsz_image = scaleImage("Plots/CompAreasCrime.png", 0.5)
    rsz_image.save("Plots/CompAreasCrime.gif", "GIF")

    plot_turtle = turtle.Turtle()
    plot_turtle.penup()
    turtle.addshape("Plots/CompAreasCrime.gif")
    plot_turtle.shape("Plots/CompAreasCrime.gif")
    plot_turtle.goto(75,0)

    sc.update()

# Read data from CSV file and drop rows with null values
# Returns data and header lists seperately
def read_data_csv(file_path):
    with open(file_path,'r', newline= '') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader if all(row)]
        return header, data


def scaleImage(filepath, scale):
    #Image conversion using PIL
    #PX 12x6in = 1152x576 px
    #1/2PX = 576x288
    #1/3NPX 384x192
    with Image.open(filepath) as image:
        width, height = image.size
        n_height = int(height * scale)
        n_width = int(width * scale)
        rsz_image = image.resize((n_width,n_height))
    return rsz_image

# Scales PCI for use in data analysis and graphing functions
def scalePCI(header, data):
    income_idx = header.index("PER CAPITA INCOME ")

    min_income = float(data[0][income_idx])
    max_income = float(data[0][income_idx])

    for row in data:
        income = float(row[income_idx])
        min_income = min(min_income, income)
        max_income = max(max_income, income)

    for row in data:
        income = float(row[income_idx])
        scaled_income = round(((income - min_income) / (max_income - min_income)) * 100,1) if max_income > min_income else 0
        row.append(str(scaled_income))
    
    header.append("PER CAPITA INCOME SCALED")
    header.remove("PER CAPITA INCOME ")

    return header, data

# Searches for an Area by name
def searchByNameArea(x,y):
    text = global_turtle_dict["area_lookup"]["text"]
    text.clear()
    text.hideturtle()
    text.penup()
    user_area = turtle.textinput("Search By Name", "Enter an area name, case-insensitive")
    if(user_area):
        info = findArea(user_area)
        text.goto(-100,-150)
        text.write(info,align = "left", font = ("times new roman", 32, "bold"))

# Searches for a crime type by name
def searchByNameCrime(x,y):
    text = global_turtle_dict["crime_lookup"]["text"]
    text.clear()
    text.hideturtle()
    text.penup()
    user_crime = turtle.textinput("Search By Crime", "Enter a crime, case-insensitive")
    if(user_crime):
        info = findCrime(user_crime)
        text.goto(-100,-150)
        text.write(info,align = "left", font = ("times new roman", 18, "bold"))

# Searches for an area given its area number
def searchByNumberArea(x,y):
    text = global_turtle_dict["area_lookup"]["text"]
    text.clear()
    text.hideturtle()
    text.penup()
    user_num = turtle.textinput("Search By Number", "Enter a number(1-78)")
    area_name = ""
    if(user_num):
            info = findArea(user_num)
            text.hideturtle()
            text.penup()
            text.goto(-100,-150)
            text.write(info,align = "left", font = ("times new roman", 32, "bold"))

# Searches for a crime_type given its index
def searchByNumberCrime(x,y):
    text = global_turtle_dict["crime_lookup"]["text"]
    text.clear()
    text.hideturtle()
    text.penup()
    user_num = turtle.textinput("Search By Number", "Enter a number(1-37)")
    crime = ""
    if(user_num):
        info = findCrime(user_num)
        text.goto(-100,-150)
        text.write(info,align = "left", font = ("times new roman", 18, "bold"))

# Stand-in for lambda
def sortBySecondElement(x):
    return x[1]


if __name__ == "__main__":
    buildShapes()
    buildScreen()
    buildData()
    buildNumAreaDict()
    buildNumCrimeDict()
    cr_header, cr_data_list = read_data_csv("Data/CrimeData2001-Present.csv")
    ce_header, ce_data_list = read_data_csv("Data/Census2008-2012.csv")
    ce_header, ce_data_list = scalePCI(ce_header, ce_data_list)
    plotCorrHeatmap()
    sc = global_turtle_dict["Screen"]
    buildMainMenu()
    sc.mainloop()