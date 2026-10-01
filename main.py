"""Använd kunskaper om klasser för att skapa digitalt bostadsområde i Python.

1. Skapa en klass för hus

Hus klassen ska ha en variabel för väg adress

Hus objekten ska ha en variabel för adress nummer

Hus objekten ska ha en variabel för beskrivning

Hus objekten ska ha en variabel för sekvens av rum

Hus objekten ska ha en funktion som returnerar adress nummer och beskrivning



2. Skapa en klass för rum

Rum objekten ska ha en variabel för namn

Rum objekten ska ha en variabel för beskrivning

Rum objekten ska ha en variabel för sekvens av möbler

Rum objekten ska ha en funktion som returnerar namn och beskrivning



3. Skapa en klass för möbler

Möbel objekten ska ha en variabel för namn

Möbel objekten ska ha en variabel för beskrivning

Möbel objekten ska ha en funktion som returnerar namn och beskrivning

Möbel objekten ska ha en funktion som "använder" möbel objektet



4. Skapa en klass för interaktiva möbler

Interaktiva Möbel objekten ska ha en variabel för namn

Interaktiva Möbel objekten ska ha en variabel för beskrivning

Interaktiva Möbel objekten ska ha en variabel för beskrivning av alternativt tillstånd

Interaktiva Möbel objekten ska ha en funktion som returnerar namn och beskrivning

Interaktiva Möbel objekten ska ha en funktion som "använder" möbel objektet. När man använder funktionen ska variabeln för beskrivning och variabeln för beskrivning av alternativt tillstånd växla



5. Möblera ett hus

Skapa minst 1 hus objekt

Skapa minst 3 rum objekt och tilldela dem till hus objekts variabel för sekvens av rum

Skapa minst 6 möbel objekt och tilldela dem till rum objekts variabel för sekvens av möbler

Skapa minst 3 interaktiva möbel objekt och tilldela dem till rum objekts variabel för sekvens av möbler



6. Skapa en meny

I menyn ska användaren ha valet att kunna få veta beskrivningen på ett hus objekt och dess rum

I menyn ska användaren ha valet att kunna få veta beskrivningen på ett hus objekts rum objekt och dess möbler

I menyn ska användaren ha valet att kunna få veta beskrivningen på ett rum objekts möbelobjekt

I menyn ska användaren ha valet att använda ett möbelobjekt

Använd menyn för att utforska hus(et) skapat i uppgift del 5



a) Granne

Använd git för att dela projektet med gruppmedlemar.

Skapa en git branch för vardera gruppmedlem.

Vardera gruppmedlem ska utföra uppgift del 5 (Var - och hur kåden ska ändras får endast kommuniceras med självdokumenterande kåd)



b) Tornado

importera modulen random

Skapa en funktion för tornado. Tornado funktionen sammlar alla möbler och tilldela dem slumpmässigt mellan alla rum i alla hus

I menyn ska användaren ha valet att använda tornado funktionen

 """

import random


# 1. Skapa en klass för hus
class House:
    def __init__(self, adress, postal_Number, description, sekvens_Of_Rooms):
        self.adress = adress
        self.postal_Number = postal_Number
        self.description = description
        self.sekvens_Of_Rooms = sekvens_Of_Rooms

    def return_Adress_And_Description(self):
        return self.adress, self.description



# 2. Skapa en klass för rum
class Room:
    def __init__(self, name, description, sekvens_Of_Furniture):
        self.name = name
        self.description = description
        self.sekvens_Of_Furniture = sekvens_Of_Furniture

    def return_Name_And_Description(self):
        return self.name, self.description


# 3. Skapa en klass för möbler
class Furniture:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def return_Name_And_Description(self):
        return self.name, self.description

    def use_Furniture(self):
        print(f"Your using {self.name} and its an {self.description}")


chair = Furniture("Chair", "An regular wooden Chair")

chair.use_Furniture()

# 4. Skapa en klass för interaktiva möbler
class Interactive_Furniture(Furniture): # La till Arv av Furniture på denna för att menyn fick en liten överkurs inlagd i säg. Dvs la till att change_place fungerade också på möbel objecten.
    def __init__(self, name, description, description_Of_Alternative_State):
        self.name = name
        self.description = description
        self.description_Of_Alternative_State = description_Of_Alternative_State

    def return_Name_And_Description(self):
        return self.name, self.description

    def change_Place(self):
        temp = ""
        temp = self.description
        self.description = self.description_Of_Alternative_State
        self.description_Of_Alternative_State = temp


interactive_furniture = Interactive_Furniture("Table", "An wooden table with golden markings on", "Its broken")
print(interactive_furniture.return_Name_And_Description())
interactive_furniture.change_Place()
print(interactive_furniture.return_Name_And_Description())

# b) Tornado
def tornado():
    rooms = []
    furnitures = []

    # Samla alla rum och alla möbler
    for room in my_House.sekvens_Of_Rooms:
        rooms.append(room)

        for furniture in room.sekvens_Of_Furniture:
            furnitures.append(furniture)

    # Töm alla rum
    for room in rooms:
        room.sekvens_Of_Furniture.clear()

    # Fördela alla möbler slumpmässigt
    for furniture in furnitures:
        random_room = random.choice(rooms)
        random_room.sekvens_Of_Furniture.append(furniture)





# 5. Möblera ett hus
# Furniture my House
# ==================================================
# a) Granne
# ÄNDRA ENDAST VÄRDENA I DETTA BLOCK
# ==================================================
my_House = House("Felix house", 16258, "An apartment in Vällingby", [])

# Rooms
room1 = Room("Kitchen", "You can cook food here", [])
room2 = Room("Living Room", "An place to have my pc and my birds", [])
room3 = Room("Sleeping Room", "A place to relax and sleep at", [])

my_House.sekvens_Of_Rooms.append(room1)
my_House.sekvens_Of_Rooms.append(room2)
my_House.sekvens_Of_Rooms.append(room3)

# Furniture
furniture1 = Furniture("Table", "An wooden Table")
furniture2 = Furniture("4x Chairs", "4 Wooden Chairs")
furniture3 = Furniture("Sofa", "Its White so dont spil any wine on it")
furniture4 = Furniture("Bed", "An soft bed to sleep at")
furniture5 = Furniture("Tv table", "An table in wood where my Tv stands on")
furniture6 = Furniture("Display Cabinet", "An place to store tresures or alchol")

room1.sekvens_Of_Furniture.extend([furniture1, furniture2])
room2.sekvens_Of_Furniture.extend([furniture3, furniture5, furniture6])
room3.sekvens_Of_Furniture.append(furniture4)

# Interactive furniture
interactive1 = Interactive_Furniture("Tv", "You watch stuff here", "Can be turned ON and OFF")
interactive2 = Interactive_Furniture("Door", "An wooden door", "Can be CLOSED and OPEND")
interactive3 = Interactive_Furniture("Lamp", "You get light from here", "Can be turned ON and OFF")

room1.sekvens_Of_Furniture.extend([interactive2, interactive3])
room2.sekvens_Of_Furniture.extend([interactive3, interactive2, interactive1])
room3.sekvens_Of_Furniture.extend([interactive2, interactive3, interactive1])
# ==================================================
# ÄNDRA INTE KOD UTANFÖR DETTA BLOCK
# ==================================================



# Print out My House
print(my_House.return_Adress_And_Description())

for room in my_House.sekvens_Of_Rooms:
    print(room.return_Name_And_Description())

    for furniture in room.sekvens_Of_Furniture:
        print(furniture.return_Name_And_Description())


# 6. Skapa en meny
meny_not_exit = True
while meny_not_exit == True:
    user_choice = int(input("Show house = 1\n Show house and stuff inside = 2\n Info regarding room furniture object = 3\n Use an Furniture object = 4\n Change place of interactive object = 5\n Tornado = 6\n Exit = 7\n"))
    try:
        choice = int(user_choice)

        if user_choice == 1:
            print(my_House.return_Adress_And_Description())

        elif user_choice == 2:
            for room in my_House.sekvens_Of_Rooms:
                print(room.return_Name_And_Description())

                for furniture in room.sekvens_Of_Furniture:
                    print(furniture.return_Name_And_Description())

        elif user_choice == 3:
            room_choice = int(input("Which room do you wanna check?\n room1 = 1, room2 = 2, room3 = 3\n"))

            try:
                r_choice = int(room_choice)
                if room_choice == 1:
                    for furniture in room1.sekvens_Of_Furniture:
                        print(furniture.return_Name_And_Description())
                elif room_choice == 2:
                    for furniture in room2.sekvens_Of_Furniture:
                        print(furniture.return_Name_And_Description())
                elif room_choice == 3:
                    for furniture in room3.sekvens_Of_Furniture:
                        print(furniture.return_Name_And_Description())
                else:
                    print("That room dont exist!")
            except:
                print("Thats not an alternativ")
                continue
        elif user_choice == 4:
            print("Which rooms furniture do you wanna use?")
            furniture_room_choice = int(input("Which room do you wanna check?\n room1 = 1, room2 = 2, room3 = 3\n"))
            try:
                f_choice = int(furniture_room_choice)

                if furniture_room_choice == 1:
                    for furniture in room1.sekvens_Of_Furniture:
                        print(furniture.return_Name_And_Description(), "\n")

                    furniture_choice = int(input("Which furniture do you wanna select? The top one are number 1"))

                    selected_furniture = room1.sekvens_Of_Furniture[furniture_choice - 1]
                    print(selected_furniture.use_Furniture())


                if furniture_room_choice == 2:
                    for furniture in room2.sekvens_Of_Furniture:
                        print(furniture.return_Name_And_Description(), "\n")

                    furniture_choice = int(input("Which furniture do you wanna select? The top one are number 1"))

                    selected_furniture = room2.sekvens_Of_Furniture[furniture_choice - 1]
                    print(selected_furniture.use_Furniture())

                if furniture_room_choice == 3:
                    for furniture in room3.sekvens_Of_Furniture:
                        print(furniture.return_Name_And_Description(), "\n")

                    furniture_choice = int(input("Which furniture do you wanna select? The top one are number 1"))

                    selected_furniture = room3.sekvens_Of_Furniture[furniture_choice - 1]
                    print(selected_furniture.use_Furniture())

            except:
                print("Thats not an alternativ")

        elif user_choice == 5:
            print("Which rooms furniture do you wanna Switch?")
            switch_furniture_room_choice = int(input("Which room do you wanna check?\n room1 = 1, room2 = 2, room3 = 3\n"))
            try:
                sf_choice = int(switch_furniture_room_choice)

                interactive_furniture = []

                if switch_furniture_room_choice == 1:
                    for furniture in room1.sekvens_Of_Furniture:
                        if isinstance(furniture, Interactive_Furniture):
                            interactive_furniture.append(furniture)
                            print(furniture.return_Name_And_Description())

                    furniture_choice = int(input("Which furniture do you wanna select? The top one are number 1"))

                    selected_furniture = interactive_furniture[furniture_choice - 1]
                    print(selected_furniture.change_Place())

                elif switch_furniture_room_choice == 2:
                    for furniture in room2.sekvens_Of_Furniture:
                        if isinstance(furniture, Interactive_Furniture):
                            interactive_furniture.append(furniture)
                            print(furniture.return_Name_And_Description())

                    furniture_choice = int(input("Which furniture do you wanna select? The top one are number 1"))

                    selected_furniture = interactive_furniture[furniture_choice - 1]
                    print(selected_furniture.change_Place())

                elif switch_furniture_room_choice == 3:
                    for furniture in room3.sekvens_Of_Furniture:
                        if isinstance(furniture, Interactive_Furniture):
                            interactive_furniture.append(furniture)
                            print(furniture.return_Name_And_Description())

                    furniture_choice = int(input("Which furniture do you wanna select? The top one are number 1"))

                    selected_furniture = interactive_furniture[furniture_choice - 1]
                    print(selected_furniture.change_Place())

            except:
                print("Thats not an alternativ")

        elif user_choice == 6:
            tornado()


        elif user_choice == 7:
            meny_not_exit = False
            break
        else:
            break
    except:
        print("Thats not an number")
        continue





