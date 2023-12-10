import requests

teamNamesList = []
teamCountries = []
teamStates = []
teamCities = []

# Reads in the user inputted team number and creates team key
teamNameInput = input("Enter Team Number ")
team_key = 'frc' + str(teamNameInput)

# API call to get the events that the team participated in for 2023
urlEvent = ('https://www.thebluealliance.com/api/v3/team/') + team_key + ('/events/2023')
headers = {
    'accept': 'application/json',
    'X-TBA-Auth-Key': '8KErbOoNp78WyTHjzQpStcBJywncDILZlvaaBXqhHellmPB5wLyojI2Ffv1wp5bH',

}
allEvents = requests.get(urlEvent, headers=headers).json()

# gets the event key and makes API call to get all teams that participated in each event
for item in allEvents:
    event_key = (item['key'])
    urlTeam = ('https://www.thebluealliance.com/api/v3/event/') + event_key + ('/teams')
    headers = {
        'accept': 'application/json',
        'X-TBA-Auth-Key': '8KErbOoNp78WyTHjzQpStcBJywncDILZlvaaBXqhHellmPB5wLyojI2Ffv1wp5bH',

    }

    allTeams = requests.get(urlTeam, headers=headers).json()
    # Takes each team, team country, team state/province, and team city and appends them to their respective lists
    for items in allTeams:
        teamName = (items['nickname'])
        teamCountry = (items['country'])
        teamState = (items['state_prov'])
        teamCity = (items['city'])
        teamNamesList.append(teamName)
        teamCountries.append(teamCountry)
        teamStates.append(teamState)
        teamCities.append(teamCity)

# Eliminates duplicate values within the list
TeamNamesList = list(set(teamNamesList))
teamCountries = list(set(teamCountries))
teamStates = list(set(teamStates))
teamCities = list(set(teamCities))

# Displays the unique countries, states and provinces, and cities
print("Countries")
print(teamCountries)
print("States and Provinces")
print(teamStates)
print("Cities")
print(teamCities)
