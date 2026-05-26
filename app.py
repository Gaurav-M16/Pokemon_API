import requests
import time

# Parent class for handling API requests
class PokemonApi:

    # Constructor method
    def __init__(self):

        # Base URL of PokeAPI
        self.url = "https://pokeapi.co/api/v2/pokemon/"

        # Getting default response data
        self.response = requests.get(self.url).json()

    # Method to get pokemon data
    def get_data(self, name=''):

        # If no pokemon name is given
        if name == '':

            # Return default pokemon list
            return self.response

        else:

            # Creating URL with pokemon name
            full_url = f"{self.url}/{name}"

            # Sending request to API
            self.response = requests.get(full_url).json()

            # Returning pokemon data
            return self.response


# Child class inheriting PokemonApi
class PokemonTab(PokemonApi):

    # Constructor method
    def __init__(self):

        # Calling parent constructor
        super().__init__()

        # Taking user name input
        self.name = input("Please enter your name to continue: ").capitalize()

        # Greeting message
        greet = f"Hello {self.name}, Welcome to PokeDex 📱\n"

        # Printing greeting slowly for animation effect
        for i in greet:
            print(i, end='', flush=True)
            time.sleep(0.05)

    # Method to display pokemon names
    def display_name(self):

        print("Following are the name of pokemons available: ")

        counter = 1

        # Getting pokemon list data
        data = self.get_data()

        # Looping through pokemon names
        for i in data['results']:

            print(counter, i['name'])

            counter += 1

            # Delay for better display effect
            time.sleep(0.5)

    # Method to select and display pokemon details
    def select_pokemon(self):

        # Taking pokemon name input
        name = input("Enter the pokemon name: ").lower()

        # Getting selected pokemon data
        response = self.get_data(name)

        # Displaying pokemon form names
        for i in response['forms']:
            print(f"\nName: {i['name']}")

        # Displaying pokemon types
        print("Type/Types: ")

        for l in response['types']:
            print(f"- {l['type']['name']}")

        # Displaying height
        print(f"Height: {response['height']}")

        # Displaying weight
        print(f"Weight: {response['weight']}")

        # Displaying abilities
        print("\nAbilities: ")

        abilities = []

        for j in response['abilities']:
            abilities.append(j['ability']['name'])

        print(", ".join(abilities))

        # Displaying first 10 moves
        print("\nFirst 10 Moves: ")

        for k in response['moves'][:10]:
            print(f"- {k['move']['name']}")


# Creating object of PokemonTab class
obj = PokemonTab()

# Displaying pokemon names
obj.display_name()

# Showing selected pokemon details
obj.select_pokemon()