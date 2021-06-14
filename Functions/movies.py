# Name: movies.py
# Purpose: opens the popular movie booking website
# Version: Python 3.9.5
# 06-05-2021
# Saquib Baig
# Dependencies: webbrowser module



import webbrowser 


country = input("In which country would you like to book movie tickets: ")

us_state_abbrev = {
    'alabama': 'AL',
    'alaska': 'AK',
    'american samoa': 'AS',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'district of Columbia': 'DC',
    'florida': 'FL',
    'georgia': 'GA',
    'guam': 'GU',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new Hampshire': 'NH',
    'new Jersey': 'NJ',
    'new Mexico': 'NM',
    'new York': 'NY',
    'north Carolina': 'NC',
    'north Dakota': 'ND',
    'northern Mariana Islands':'MP',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'puerto Rico': 'PR',
    'rhode Island': 'RI',
    'south Carolina': 'SC',
    'south Dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virgin Islands': 'VI',
    'virginia': 'VA',
    'washington': 'WA',
    'west Virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY'
}


s = True
if country == 'India' or country == 'india':
    city = input("In which city would you like to book tickets: ")
    webbrowser.open('https://in.bookmyshow.com/explore/home/'+city)


elif country == 'US' or country.lower() == 'United States':
    city1 = input("In which city would you like to book tickets: ")
    while s == True:
        state = input("In which state would you like to book tickets: ")
        if state in us_state_abbrev:
            s == False
            shortform = us_state_abbrev[state]
            webbrowser.open("https://www.fandango.com/"+city1+'_'+shortform+'_movietimes')
            break

else:
    print("I am sorry. I will not be able to book tickets in your country.")




