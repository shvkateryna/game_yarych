"""Yarych classes"""
counter_enemy = 0
class Location():
    """Information about location"""
    def __init__(self, name, description = '', item = None, character = None) -> None:
        self.name = name
        self.item = item
        self.description = description
        self.rooms = []
        self.character = character

    def set_description(self, description):
        """Function for setting description"""
        self.description = description

    def link_room(self, link, side):
        """Link room"""
        self.rooms.append((link, side))

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
        locations = 'Ти можеш піти у такі місця: '
        for i in self.rooms:
            if self.rooms.index(i) == 0:
                locations += i[1]
            else:
                locations += ', ' + i[1]
        print(locations)

    def get_character(self):
        """
        Get character
        """
        return self.character

    def get_item(self):
        """
        Get item
        """
        return self.item

    def move(self, side):
        """
        Move
        """
        for item in self.rooms:
            if item[1] == side:
                return item[0]

class Room(Location):
    """Information about room"""
    def __init__(self, name, character = None, description='', hint = None) -> None:
        super().__init__(name, description, character)
        self.rooms = []
        self.hint = hint

    def set_hint(self, hint):
        """Function for setting hint"""
        self.hint = hint

    def get_hint(self):
        self.hint.get_hint()

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
        print(f'Тут є {self.name}!')
        print(self.description)

    def talk(self):
        """Talk"""
        print(f'[{self.name} говорить]: {self.conversation}')

class Friend(Character):
    """Information about friend"""
    def __init__(self, name, description, conversation = None, help = '') -> None:
        super().__init__(name, description, conversation)
        self.help = help

    def describe(self):
        print('Попроси про допомогу у друга. Для цього напиши: "допомогти"')
        return super().describe()

    def set_help(self, help):
        """Function for setting help"""
        self.help = help

    def help_friend(self):
        """Function returns help"""
        print(self.help)

class Item():
    """Information about item"""
    def __init__(self, name: str, description='', availability = None) -> None:
        self.name = name
        self.description = description
        if availability is None:
            self.availability = False
        self.availability = availability

    def describe(self):
        """Function for describing"""
        print(f'[{self.name}] тут знаходиться\nОпис: {self.description}')

    def get_name(self):
        """Function returns name"""
        return self.name

    def set_description(self, description):
        """Set description"""
        self.description = description

class Hint(Item):
    """Information about hint"""
    def __init__(self, name: str, description='', availability=True, hint = '') -> None:
        super().__init__(name, description, availability)
        self.hint = hint

    def describe(self):
        print('Якщо складно, то скористайся підказкою. Для цього напиши: "підказати"')
        print(self.name)

    def set_hint(self, hint):
        """Function for setting hint"""
        self.hint = hint

    def get_hint(self):
        """Function returns hint"""
        print(self.description)
        print(self.hint)

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
            print(f'Ти поборов {self.name} завдяки такому предмету, як {fight_with}')
            return True
        else:
            print(f'{self.name} добив тебе.')

    def get_defeated(self):
        """Get defeated"""
        return counter_enemy
