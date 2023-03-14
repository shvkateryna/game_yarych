"""Task 5"""
counter_enemy = 0
class Character():
    """Information about character"""
    def __init__(self, name, description, conversation = None) -> None:
        self.name = name
        self.description = description
        self.conversation = conversation

    def set_conversation(self, conversation):
        """Set conversation"""
        self.conversation = conversation

    def describe(self):
        """Describe"""
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self):
        """Talk"""
        print(f'[{self.name} says]: {self.conversation}')

class Enemy(Character):
    """Information about enemy"""
    def __init__(self, name, description, conversation = None, weakness = None) -> None:
        super().__init__(name, description, conversation)
        self.weakness = weakness
        self.counter = counter_enemy

    def set_weakness(self, weakness):
        """Set weakness"""
        self.weakness = weakness

    def fight(self, fight_with):
        """Fight"""
        if self.weakness == fight_with:
            global counter_enemy
            counter_enemy += 1
            print(f'You fend {self.name} off with the {fight_with}')
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer')

    def get_defeated(self):
        """Get defeated"""
        return counter_enemy

class Friend(Character):
    """Information about friend"""
    def __init__(self, name, description, conversation = None, hint = None) -> None:
        super().__init__(name, description, conversation)
        self.hint = hint

    def set_advice(self, hint):
        """Function for setting advice"""
        self.hint = hint

    def talk(self):
        print(f'[{self.name} says]: {self.conversation}\n{self.hint}')

class Item():
    """Information about item"""
    def __init__(self, name: str, description='') -> None:
        self.name = name
        self.description = description

    def describe(self):
        """Function for describing"""
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        """Function returns name of item"""
        return self.name

    def set_description(self, description):
        """Set description"""
        self.description = description

class Room():
    """Information about room"""
    def __init__(self, name:str, description = '', character = None, item = None) -> None:
        self.name = name
        self.description = description
        self.rooms = []
        self.character = character
        self.item = item

    def link_room(self, link, side):
        """Link room"""
        self.rooms.append((link, side))

    def set_description(self, description):
        """Set description"""
        self.description = description

    def set_character(self, character):
        """Set character"""
        self.character = character

    def set_item(self, item):
        """Set item"""
        self.item = item

    def get_details(self):
        """Get description"""
        print(self.name)
        print('--------------------')
        print(self.description)
        for i in self.rooms:
            print(f'The {i[0].name} is {i[1]}')

    def get_character(self):
        """Get character"""
        return self.character

    def get_item(self):
        """Get item"""
        return self.item

    def move(self, side):
        """Move"""
        for item in self.rooms:
            if item[1] == side:
                return item[0]
