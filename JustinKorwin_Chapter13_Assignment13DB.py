# this program will create a database of the populations of 10 different cities in florida
# the simulated population growth will be 2% per year for 20 years
# using matplotlib, this program will create a function and then display a graph with the population growth

import numpy as np
import matplotlib.pyplot as plt
# I don't understand what it means to name the database population_JK but the program should function properly otherwise

# creating function to initialize cities and populations
def main1():
    cities = [
        ('Miami', 455924),
        ('Orlando', 281793),
        ('Tampa', 403364),
        ('Jacksonville', 990931),
        ('Tallahassee', 392645),
        ('Fort Lauderdale', 176232),
        ('St. Petersburg', 266417),
        ('Palm Beach', 153380),
        ('Gainesville', 352126),
        ('Sarasota', 464223)
    ]
    return cities

# creating function to create population array
def create_population_array(cities):
    years = np.arange(2023, 2044)
    data = np.array([pop for _, pop in cities]).reshape(-1, 1)
    data = np.tile(data, (1, len(years)))
    return data, years

# creating function to simulate population growth
def simulate_population_growth(data):
    growth_rate = 0.02
    for i in range(1, data.shape[1]):
        data[:, i] = (data[:, i - 1] * (1 + growth_rate)).astype(int)

#  creating function to visualize population growth with a cool graph
def visualize_population_growth(cities, data, years):
    print("Available cities:")
    for i, (city, _) in enumerate(cities):
        print(f"{i + 1}. {city}")

    choice = int(input("Please choose a city by entering its number: ")) - 1
    city = cities[choice][0]

    plt.plot(years, data[choice], marker='o')
    plt.title(f'Population Growth for {city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()

# creating main function that combines all the other functions
def main():
    cities = main1()
    data, years = create_population_array(cities)
    simulate_population_growth(data)
    visualize_population_growth(cities, data, years)
# calling main function so this actually works
main()