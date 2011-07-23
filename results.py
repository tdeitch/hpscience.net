#!/usr/bin/python

# HP Science Results Generator
# Written by Trey Deitch
# Public Domain

# Parameters

# base_dir: the directory in which all files will be written - this must end with '/'
# to create files in the same directory as the script, change to base_dir = '' (empty string)
base_dir = 'results'
largest_conference_size = 5
number_of_districts = 32
number_of_regions = 4
earliest_year = 2005
# to set the latest year that the script should use, uncomment the line below.
# Otherwise, the current year will be used as the upper bound.
# latest_year = 2011
# check whether latest_year has been manually entered
try: latest_year
except NameError:
    import datetime
    latest_year = int(datetime.datetime.now().year)
# years is the range of years for which to generate data, from 2005 to the current year
years = list(range(earliest_year,latest_year+1))
# classifications is just the range of conference sizes, from 1A to 5A
classifications = list(range(1,largest_conference_size+1))
# levels is a list of tuples, and each tuple contains ('level name','s_level_id from the form on the web','number of districts in the level, or blank if the level is state','Name of the units in the level, e.g. district or region')
levels = [('District','D',str(number_of_districts),'District'),('Regional','R',str(number_of_regions),'Region'),('State','S','','')]
# events is a list of tuples, and each tuple contains ('s_event_abbr from the form on the web','the name of the event')
events = [('CAL','Calculator Applications'),('CSC','Computer Science'),('MTH','Mathematics'),('NUM','Number Sense'),('SCI','Science')]
# header is a string containing the head and the top-level navigation
header = '<?php include("/f5/hpscience/public/includes/header.php"); ?>\n<title>HP Science: Results</title>\n<link type="text/css" rel="stylesheet" href="/results/style.css">\n<link type="text/css" rel="stylesheet" media="print" href="/results/print.css">\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"></script>\n</head>\n<body>\n<header>HP Science: Results</header>\n<?php include("/f5/hpscience/public/includes/navigation.php"); ?>\n<div id="buttons"></div>\n'
# footer contains the standard footer used across the website. In the encrypted e-mail code, every '\' must be replaced with '\\'
footer = '<?php include("/f5/hpscience/public/includes/footer.php"); ?>\n<script>\n$(\'#buttons\').append(\'<button style="border:none; background:transparent; cursor:pointer;" id="hide">▾ Hide navigation</button><button style="border:none; background:transparent; cursor:pointer; display:none;" id="show">‣ Show navigation</button>\');\n$("#hide").click(function () {\n$("#hide").hide();\n$("#navigation").hide();\n$("#show").show();\n});\n$("#show").click(function () {\n$("#show").hide();\n$("#navigation").show();\n$("#hide").show();\n});\n</script>\n</footer>\n</body>\n</html>'

# Import path, url, and regex stuff
import os.path
from urllib.parse import urlencode
import httplib2
import re

# Create a http cache directory
h = httplib2.Http('.cache')

# Check to make sure all of the directories we'll be using exist
print('Generating directories')
for year in years:
    for classification in classifications:
        for level in levels:
            dir = os.path.join(base_dir,str(year),str(classification)+'A',level[0].lower())
            if not os.path.exists(dir):
                os.makedirs(dir)
print('All directories generated')

# Check for the required CSS files
print('Generating CSS files')
with open(os.path.join(base_dir,'print.css'), mode='w',encoding='utf-8') as htmlpage:
    htmlpage.write('#navigation, #hide, #show {\ndisplay: none !important;\n}\n\n#print_header {\ndisplay: block;\npage-break-before: always;\n}\n')
with open(os.path.join(base_dir,'style.css'), mode='w',encoding='utf-8') as htmlpage:
    htmlpage.write('#navigation {\ntext-align: center;\ndisplay:block;\nmargin-top: 0;\npadding-top: 0;\n}\n\n#hide,#show {\nfont: normal small Vollkorn,serif;\npadding-bottom: 0;\nmargin-bottom: 0;\n}\n\n#print_header {\ndisplay: none;\n}\n')
print('All CSS files generated')

# Generate the navigation for the html files
top_level_header = '<p id="navigation">'
second_level_header = '<p id="navigation">'
third_level_header = '<p id="navigation">'
fourth_level_header = '<p id="navigation">'
print('Generating headers')
# Generate each year of the top-level header
for year in years[:-1]:
    top_level_header += '<a href="'+str(year)+'/">'+str(year)+'</a> | '
# Generate the last year of top-level header
top_level_header += '<a href="'+str(years[-1])+'/">'+str(years[-1])+'</a></p>\n'
# Generate second-level header
for year in years[:-1]:
    second_level_header += '<a href="../'+str(year)+'/">'+str(year)+'</a> | '
second_level_header += '<a href="../'+str(years[-1])+'/">'+str(years[-1])+'</a><br>\n'
for classification in classifications[:-1]:
    second_level_header += '<a href="./'+str(classification)+'A/">'+str(classification)+'A</a> | '
second_level_header += '<a href="./'+str(classifications[-1])+'A/">'+str(classifications[-1])+'A</a></p>\n'
# Generate third-level header
for year in years[:-1]:
    third_level_header += '<a href="../../'+str(year)+'/">'+str(year)+'</a> | '
third_level_header += '<a href="../../'+str(years[-1])+'/">'+str(years[-1])+'</a><br>\n'
for classification in classifications[:-1]:
    third_level_header += '<a href="../'+str(classification)+'A/">'+str(classification)+'A</a> | '
third_level_header += '<a href="../'+str(classifications[-1])+'A/">'+str(classifications[-1])+'A</a><br>\n'
for level in levels[:-1]:
    third_level_header += '<a href="./'+level[0].lower()+'/">'+level[0]+'</a> | '
third_level_header += '<a href="./'+levels[-1][0].lower()+'/">'+levels[-1][0]+'</a></p>\n'
# Generate fourth-level header
for year in years[:-1]:
    fourth_level_header += '<a href="../../../'+str(year)+'/">'+str(year)+'</a> | '
fourth_level_header += '<a href="../../../'+str(years[-1])+'/">'+str(years[-1])+'</a><br>\n'
for classification in classifications[:-1]:
    fourth_level_header += '<a href="../../'+str(classification)+'A/">'+str(classification)+'A</a> | '
fourth_level_header += '<a href="../../'+str(classifications[-1])+'A/">'+str(classifications[-1])+'A</a><br>\n'
for level in levels[:-1]:
    fourth_level_header += '<a href="../'+level[0].lower()+'/">'+level[0]+'</a> | '
fourth_level_header += '<a href="../'+levels[-1][0].lower()+'/">'+levels[-1][0]+'</a><br>\n'
for event in events[:-1]:
    fourth_level_header += '<a href="./'+event[0].lower()+'.php">'+event[1]+'</a> | '
fourth_level_header += '<a href="./'+events[-1][0].lower()+'.php">'+events[-1][1]+'</a></p>\n'
print('All headers generated')

# Generate index.php files using the headers generated above
print('Generating index.php files')
with open(os.path.join(base_dir,'index.php'), mode='w',encoding='utf-8') as htmlpage:
    # Generate the top-level index.php file
    htmlpage.write(header+top_level_header+'<p>You are here: •</p>\n'+footer)
for year in years:
    # Generate the files for each year
    with open(os.path.join(base_dir,str(year),'index.php'), mode='w',encoding='utf-8') as htmlpage:
        htmlpage.write(header+second_level_header+'<p>You are here: <a href="./">'+str(year)+'</a></p>\n'+footer)
    for classification in classifications:
        # Generate the files for each classification
        with open(os.path.join(base_dir,str(year),str(classification)+'A','index.php'), mode='w',encoding='utf-8') as htmlpage:
            htmlpage.write(header+third_level_header+'<p>You are here: <a href="../">'+str(year)+'</a> ‣ <a href="./">'+str(classification)+'A</a></p>\n'+footer)
        # Generate the files for each contest level
        for level in levels:
            with open(os.path.join(base_dir,str(year),str(classification)+'A',level[0].lower(),'index.php'), mode='w',encoding='utf-8') as htmlpage:
                htmlpage.write(header+fourth_level_header+'<p>You are here: <a href="../../">'+str(year)+'</a> ‣ <a href="../">'+str(classification)+'A</a> ‣ <a href="./">'+level[0]+'</a></p>\n'+footer)
print('All index.php files generated')

# Generate results
for year in years:
    for classification in classifications:
        for level in levels:
            for event in events:
                print(str(year)+' '+str(classification)+'A '+level[0]+' '+event[1])
                people = []
                teams = []
                # The state contest must be handled differently because it takes an empty string in the s_level_num field rather than a number
                if not level[2].isdigit():
                    districts = 1
                else:
                    districts = int(level[2])
                for district in range(1,districts+1):
                    # These parameters come from this page: http://utdirect.utexas.edu/uil/vlcp_results.WBX?s_year=2011&s_meet_abbr=SPM&s_gender=&s_level_id=D&s_level_nbr=10&s_conference=4A&s_area_zone=&s_submit_sw=X
                    # View the page's source to see what parameters are being sent by the form
                    # Again, the state contest must be handled differently because it takes an empty string in the s_level_num field rather than a number
                    if not level[2].isdigit():
                        data = {'s_event_abbr': event[0], 's_year': str(year), 's_conference': str(classification)+'A', 's_level_id': level[1], 's_level_nbr': levels[2], 's_submit_sw': 'X', 's_dept': 'C', 's_meet_abbr': 'SPM'}
                    else:
                        data = {'s_event_abbr': event[0], 's_year': str(year), 's_conference': str(classification)+'A', 's_level_id': level[1], 's_level_nbr': str(district), 's_submit_sw': 'X', 's_dept': 'C', 's_meet_abbr': 'SPM'}
                    # This should get each individual district's results page by submitting the form and decode the delivered page to UTF-8
                    resp, content = h.request('http://utdirect.utexas.edu/uil/vlcp_results.WBX','POST',urlencode(data),headers={'Content-Type': 'application/x-www-form-urlencoded'}) 
                    str_content = content.decode('utf-8')
                    # This regex matches the table containing all of the individual results
                    individual_results_regex = re.compile(r'<h3>Individual Results</h3>(.*)</table>', re.DOTALL)
                    if individual_results_regex.search(str_content):
                        all_individual_results = individual_results_regex.search(str_content).groups()
                        # This line splits the individual results into a list, one entry for each person
                        individual_results_list = all_individual_results[0].split('<tr >')
                        # This regex matches each person's name, school, and score
                        person_regex = re.compile(r'<td  class="fineprnt" nowrap="nowrap">([A-Za-z ,\-]*)</td>\s*<td  class="fineprnt" nowrap="nowrap">([A-Za-z ,\-]*)</td>\s*<td  class="fineprnt" style="text-align:right;" nowrap="nowrap">\s*(\-?\d{1,3})')
                        for person in individual_results_list[2:]:
                            if person_regex.search(person):
                                # This adds each person to the list of people defined above
                                new_person = list(person_regex.search(person).groups())
                                new_person.append(district)
                                people.append(new_person)
                    else:
                        print('    NO INDIVIDUALS/RESULTS FROM '+level[0].upper()+' '+str(district)+' IN '+str(year)+' '+str(classification)+'A '+event[1].upper())
                    # This regex matches the table containing all of the team results
                    team_results_regex = re.compile(r'<h3>Team Results</h3>(.*)</table>', re.DOTALL)
                    if team_results_regex.search(str_content):
                        all_team_results = team_results_regex.search(str_content).groups()
                        # This line splits the team results into a list, with one element for each team
                        team_results_list = all_team_results[0].split('<tr >')
                        # This regex matches each team's name and score
                        team_regex = re.compile(r'<td  class="fineprnt" nowrap="nowrap">([A-Za-z ,\-]*)</td>\s*<td  class="fineprnt" nowrap="nowrap">\d?</td>\s*<td  class="fineprnt" style="text-align:right;" nowrap="nowrap">\s*(-?\d{1,4})')
                        for team in team_results_list[2:]:
                            if team_regex.search(team):
                                # This adds each team to the list of teams defined above
                                new_team = list(team_regex.search(team).groups())
                                new_team.append(district)
                                teams.append(new_team)
                    else:
                        print('    NO TEAMS/RESULTS FROM '+level[0].upper()+' '+str(district)+' IN '+str(year)+' '+str(classification)+'A '+event[1].upper())
                # This sorts each list by score, lowest score first
                for score in people:
                    score[2] = int(score[2])
                for score in teams:
                    score[1] = int(score[1])
                people.sort(key=lambda people: people[2])
                teams.sort(key=lambda teams: teams[1])
                # This generates the navigation
                district_header = '<p id="navigation">\n'
                for nav_year in years[:-1]:
                    district_header += '<a href="../../../'+str(nav_year)+'/'+str(classification)+'A/'+level[0].lower()+'/'+event[0].lower()+'.php">'+str(nav_year)+'</a> | '
                district_header += '<a href="../../../'+str(years[-1])+'/'+str(classification)+'A/'+level[0].lower()+'/'+event[0].lower()+'.php">'+str(years[-1])+'</a><br>\n'
                for nav_classification in classifications[:-1]:
                    district_header += '<a href="../../'+str(nav_classification)+'A/'+level[0].lower()+'/'+event[0].lower()+'.php">'+str(nav_classification)+'A</a> | '
                district_header += '<a href="../../'+str(classifications[-1])+'A/'+level[0].lower()+'/'+event[0].lower()+'.php">'+str(classifications[-1])+'A</a><br>\n'
                for nav_level in levels[:-1]:
                    district_header += '<a href="../'+nav_level[0].lower()+'/'+event[0].lower()+'.php">'+nav_level[0]+'</a> | '
                district_header += '<a href="../'+levels[-1][0].lower()+'/'+event[0].lower()+'.php">'+levels[-1][0]+'</a><br>\n'
                for nav_event in events[:-1]:
                    district_header += '<a href="'+nav_event[0].lower()+'.php">'+nav_event[1]+'</a> | '
                district_header += '<a href="'+events[-1][0].lower()+'.php">'+events[-1][1]+'</a></p>\n'
                # Finally, this writes everything to an html file
                with open(os.path.join(base_dir,str(year),str(classification)+'A',level[0].lower(),event[0].lower()+'.php'), mode='w',encoding='utf-8') as htmlpage:
                    # This writes the header and navigation
                    htmlpage.write(header+district_header)
                    # This writes the breadcrumb
                    htmlpage.write('<p>You are here: <a href="../../../'+str(year)+'/">'+str(year)+'</a> ‣ <a href="../../../'+str(year)+'/'+str(classification)+'A/">'+str(classification)+'A</a> ‣ <a href="./">'+level[0]+'</a> ‣ </p>\n<h2>'+event[1]+'</h2>\n')
                    # This starts the team table
                    htmlpage.write('<h3 id="team"><a name="team">Teams</a></h3>\n<table cellspacing="4"><tr><th>School, City')
                    if level[3]:
                        htmlpage.write(' ('+level[3]+')')
                    htmlpage.write('</th><th>Score</th></tr>\n')
                    for team in teams[::-1]:
                        # This writes each row in the team table
                        htmlpage.write('<tr><td>'+team[0])
                        if level[3]:
                            htmlpage.write(' ('+str(team[2])+')')
                        htmlpage.write('</td><td>'+str(team[1])+'</td></tr>\n')
                    # This closes the team table and opens the individuals table
                    htmlpage.write('</table>\n')
                    htmlpage.write('<div id="print_header">\n<header>HP Science: Results</header>\n')
                    # This writes the breadcrumb
                    htmlpage.write('<p>You are here: <a href="../../../'+str(year)+'/">'+str(year)+'</a> ‣ <a href="../../../'+str(year)+'/'+str(classification)+'A/">'+str(classification)+'A</a> ‣ <a href="./">'+level[0]+'</a> ‣ </p>\n<h2>'+event[1]+'</h2>\n</div>\n')
                    htmlpage.write('<h3 id="individual"><a name="individual">Individuals</a></h3>\n<table cellspacing="4"><tr><th>Name</th><th>School, City')
                    if level[3]:
                        htmlpage.write(' ('+level[3]+')')
                    htmlpage.write('</th><th>Score</th></tr>\n')
                    for person in people[::-1]:
                        # This writes each row in the individual table
                        htmlpage.write('<tr><td>'+person[0]+'</td><td>'+person[1])
                        if level[3]:
                            htmlpage.write(' ('+str(person[3])+')')
                        htmlpage.write('</td><td>'+str(person[2])+'</td></tr>\n')
                    # This closes the individual table and writes the footer
                    htmlpage.write('</table>\n'+footer)
