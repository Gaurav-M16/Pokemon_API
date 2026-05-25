import requests
import time

class PokemonApi:
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/pokemon/"
        self.response = requests.get(self.url).json()

    def get_data(self,name=''):
        if name == '':
            return self.response 
        else:
            full_url = f"{self.url}/{name}"
            self.response = requests.get(full_url).json()
            return self.response
    
class PokemonTab(PokemonApi):

    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name to continue: ").capitalize()
        greet = f"Hello {self.name}, Welcome to PokeDex 📱\n"
        for i in greet:
            print(i,end='',flush=True)
            time.sleep(0.05)

    def display_name(self):
        print("Following are the name of pokemons available: ")
        counter = 1
        data = self.get_data()
        for i in data['results']:
            print(counter, i['name'])
            counter += 1
            time.sleep(0.5)

    def select_pokemon(self):
        name = input("Enter the pokemon name: ").lower()
        response = self.get_data(name)
        for i in response['forms']:
            print(f"\nName: {i['name']}")

        print("Type/Types: ")
        for l in response['types']:
            print(f"- {l['type']['name']}")

        print(f"Height: {response['height']}")

        print(f"Weight: {response['weight']}")

        print("\nAbilities: ")
        abilities = []
        for j in response['abilities']:
            abilities.append(j['ability']['name'])
        print(", ".join(abilities))
        
        print("\nFirst 10 Moves: ")
        for k in response['moves'][:10]:
            print(f"- {k['move']['name']}")



obj = PokemonTab()
obj.display_name()
obj.select_pokemon()


