'''This program lets the user to type a city from the state of
Espírito Santo (Brazil) and they are able
to see the Covid-19 data from it'''

'''Here are the main cities to check if you're not from Brazil:
- Vila Velha
- Vitória

'''

import csv

def main():
    covid_data = read_file()
    get_city_from_user(covid_data)

def get_city_from_user(covid_data):
    city = input("Type a city (or type 1 to exit): ")

    while city == '':
        city = input("Type a city (or type 1 to exit): ")

    if city == '1':
        exit()
    else:
        print("Let's dive into the COVID19 data of any city in Espírito Santo, a state in Brazil!\n")
        print("City is", city, "-->", "Population:", covid_data[city][0], "/", 
            "Confirmed COVID cases:", covid_data[city][1], "/",
            "Number of deaths:", covid_data[city][2], "/",
            "Death rate: ", covid_data[city][3] , "%")
    


def read_file():
    covid_data = {}

    with open("covid_data.csv", encoding="utf8") as f:
        reader = csv.DictReader(f)


        for line in reader:
            city = line['city']
            confirmed_cases = line['confirmed']
            deaths = line['deaths']
            population = line['estimated_population']
            death_rate = float(line['death_rate']) * 100


            covid_data[city] = [population, confirmed_cases, deaths, death_rate]

    return covid_data



if __name__ == '__main__':
    main()