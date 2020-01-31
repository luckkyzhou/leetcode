import requests
import json

def get_data(url):
    data = requests.get(url).json()
    return data

def check_consecutive(s1, s2):
    import datetime
    s1 = datetime.datetime.strptime(s1, "%Y-%m-%d")
    s2 = datetime.datetime.strptime(s2, "%Y-%m-%d")
    return (s2-s1).days == 1

def check_prev(s1, s2):
    import datetime
    s1 = datetime.datetime.strptime(s1, "%Y-%m-%d")
    s2 = datetime.datetime.strptime(s2, "%Y-%m-%d")
    return (s1 - s2).days  >= 1

def find_overlap(res,dates, country):
    if not dates:
        res["countries"].append( {
            "attendeeCount": 0,
            "attendees": [],
            "name": country,
            "startDate": None
        })
    else:
        best_len = 0
        best_date = ""
        for key in dates:
            if not best_date:
                best_len = max(best_len,len(dates[key]))
                best_date = key
            elif len(dates[key]) > best_len :
                best_len =len(dates[key])
                best_date = key
            #Check whether this day is earlier than the best_date we have so far
            elif len(dates[key]) == best_len and check_prev(best_date, key):
                best_date = key

        res["countries"].append({
            "attendeeCount": len(dates[best_date]),
            "attendees": list(dates[best_date]),
            "name": country,
            "startDate": best_date
        })

def post_data(post_url, get_url):
    from collections import defaultdict
    data = get_data(get_url)
    countries = defaultdict(list)

    for person in data["partners"]:
        country = person["country"]
        countries[country].append(person)
    res = {"countries":[]}
    # Sort people by countries
    for country in countries:
        dates = defaultdict(set)
        for person in countries[country]:
            p_date = person["availableDates"]
            for j in range(1, len(p_date)):
                if check_consecutive(p_date[j-1], p_date[j]):
                    dates[p_date[j-1]].add(person["email"])
        # Find overlap
        find_overlap(res, dates, country)

    resp = requests.post(post_url, json=res)
    if resp.status_code != 200:
        print(resp.status_code,resp.content)
    print(resp.status_code == 200)

get_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=1cae96d3904b260d06d0daa7387c"
post_url="https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=1cae96d3904b260d06d0daa7387c"
post_data(post_url, get_url)