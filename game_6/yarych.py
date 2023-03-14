"""Game Yarych"""
import yarych_classes
#встановлюю кімнати і їхній опис
home = yarych_classes.Location("Хата")
home.set_description("Ти у себе вдома. На кухні пахне щойно приготовленою вечерею, десь далеко чути голос мами")

room_pavlo = yarych_classes.Room("Кімната брата Павла")
room_pavlo.set_description("Велика кімната із зазвичай не застеленим ліжком\
, де любить відпочивати Кіт")

school = yarych_classes.Location("Рідна школа")
school.set_description("Тут, як завжди, чути дитячий сміх і подекуди крик вчителів...")

cabinet = yarych_classes.Room("Учительська")
cabinet.set_description("У цьому маленькому приміщенні вчителі пʼють каву\
 та водночас перевіряють контрольні роботи")

music_school = yarych_classes.Location("Музична школа")
music_school.set_description("Стара будівля, моторошно навкруги, багато павутиння. \
Лише десь зверху чути тихенькі дитячі голоси, гру фортепіано та гітари")

main_building = yarych_classes.Location('Народний дім')
main_building.set_description("Ти потрапляєш у велику будівлю з тепер уже світлими кабінетами,\
 десь неподалік чути шарудіння паперу, офіційні розмови")

#зʼєдную кімнати між собою
home.link_room(music_school, "музична школа")
home.link_room(room_pavlo, "кімната Павла")
home.link_room(school, "школа")
home.link_room(main_building, "народний дім")

room_pavlo.link_room(home, "хата")
cabinet.link_room(school, "школа")

school.link_room(music_school, "музична школа")
school.link_room(cabinet, "учительська")
school.link_room(home, "хата")
school.link_room(main_building, "народний дім")

music_school.link_room(home, "хата")
music_school.link_room(school, "школа")
music_school.link_room(main_building, "народний дім")

main_building.link_room(home, "хата")
main_building.link_room(school, "школа")
main_building.link_room(music_school, "музична школа")

#описую ворогів
grandfather = yarych_classes.Enemy('дідо', 'Старенький, який хоче, щоб ти \
якнайбільше уваги приділяв(ла) музиці')
grandfather.set_conversation('Чуєш! Я хотів би, щоб ти брав(ла) участь у хорі!')
grandfather.set_weakness("грамота")
music_school.set_character(grandfather)

mother = yarych_classes.Enemy('Мамочка', 'Вона, як завжди, сидить\
 і чекає доки ти нарешті її послухаєш')
mother.set_conversation('Дитино, поприбирай, будь ласка, у своїй кімнаті')
mother.set_weakness('щоденник')
home.set_character(mother)

teacher = yarych_classes.Enemy('Жанна Олександрівна', 'Добра вчителька української\
 мови, яка вже третій тиждень чекає на твій твір')
teacher.set_conversation('Слава Ісусу Христу! Скільки мені ще чекати на твоє домашнє завдання?')
teacher.set_weakness('твір')
school.set_character(teacher)

director = yarych_classes.Enemy('Наталя Іванівна', 'Головна в ОТГ, завжди\
 вимагає брати в чомусь участь')
director.set_conversation('Дорогий(га)! Так давно тебе не бачила. Звіт уже готовий?')
director.set_weakness('звіт')
main_building.set_character(director)

#описую предмети
award = yarych_classes.Item('грамота', availability = True)
award.set_description('щойно отримана грамота з музичного конкурсу, яка точно сподобається дідові')
home.set_item(award)

diary = yarych_classes.Item('щоденник')
diary.set_description('щоденник з високими оцінками')
room_pavlo.set_item(diary)

report = yarych_classes.Item('звіт', availability = True)
report.set_description('дуже важливий документ - звіт ради школи')
music_school.set_item(report)

essay = yarych_classes.Item('твір')
essay.set_description('домашнє завдання, яке потрібно було здати ще три тижні тому')
cabinet.set_item(essay)

#описую друзів
godmother = yarych_classes.Friend('Мамуся', 'Твоя хресна - вчителька історії,\
 яка готова з будь-чим допомогти у школі')
godmother.set_conversation('Ой, а хто це тут у нас? Знов щось від мене треба?')
godmother.set_help('Добре, допоможу я тобі із цим твором, як ти просив(ла)')
cabinet.set_character(godmother)

brother = yarych_classes.Friend('Павло', 'Брат-добряк, який може вислухати твоє прохання')
brother.set_conversation('О, знов прийшов(ла). Що на цей раз потрібно?')
brother.set_help('Гаразд, зараз принесу свій щоденник, покажеш його мамі,\
 а я поки поприбираю за тебе')
room_pavlo.set_character(brother)

#описую підказки
hint_cabinet = yarych_classes.Hint('Підказка: народний дім')
hint_cabinet.set_description('Тобі потрібно поставити букви у \
правильному порядку, щоб отримати назву предмета')
hint_cabinet.set_hint('ІВЗТ')
cabinet.set_hint(hint_cabinet)

hint_room = yarych_classes.Hint('Підказка: хата')
hint_room.set_description('Тобі потрібно поставити букви у правильному порядку,\
 щоб отримати назву предмета')
hint_room.set_hint('ДЕЩННКИО')
room_pavlo.set_hint(hint_room)
current_room = home
backpack = []

dead = False
print('\nПривіт! Гра полягає в тому, щоб виконати всі завдання, щоб всі персонажі були задоволені.\n\
На кожній локації ти маєш вибір: поговорити з персонажем (команда "говорити"), взяти предмет ("взяти"), вирішити проблему ("вирішувати")\n\
Інколи буде можливо попросити допомоги в друга чи взяти підказку.')
while dead is False:

    print("\n")
    try:
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()

        item = current_room.get_item()
        if item is not None and item.availability is True:
            item.describe()
        if isinstance(current_room, yarych_classes.Room):
            hint = current_room.hint
            hint.describe()

        command = input("> ")

        if command in ["музична школа", "учительська", "народний дім",\
        "хата", "кімната Павла", "школа"]:
            # Move in the given direction
            current_room = current_room.move(command)
        elif command == "говорити":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.talk()
        elif command == "вирішувати":
            if inhabitant is not None and isinstance(inhabitant, yarych_classes.Enemy):
                # Fight with the inhabitant, if there is one
                print("Що використаєш у такій ситуації?")
                fight_with = input()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) is True:
                        # What happens if you win?
                        print("Ура! Ти справився!")
                        current_room.character = None
                        if inhabitant.get_defeated() == 4:
                            print("Вітаю! Ти вирішив усі справи")
                            dead = True
                    else:
                        # What happens if you lose?
                        print("На жаль, ти програв")
                        print("Це кінець гри")
                        dead = True
                else:
                    print("Ти не маєш " + fight_with)
            else:
                print("Тут немає нікого")
        elif command == "взяти":
            if item is not None:
                print("Ти поклав " + item.get_name() + " у свій рюкзак")
                backpack.append(item.get_name())
                current_room.set_item(None)
            else:
                print("Тут немає нічого")
        elif command == "допомогти":
            if isinstance(inhabitant, yarych_classes.Friend):
                inhabitant.help_friend()
                item.availability = True
        elif command == "підказати":
            hint.get_hint()
        else:
            print("Я не знаю, як " + command)
    except AttributeError:
        print('Ти не можеш піти у цю кімнату')
        break
