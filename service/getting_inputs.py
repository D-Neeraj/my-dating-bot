import json


def get_entities():
    data_count = int(input("Enter the no.of.entities to enter:"))
    for i in range(data_count):
        entity_name = input("Entity Name:")
        entity_value = input("Entity Value:")
        synonyms = input("Enter the Synonyms or press 2 to skip:").split(",")
        if "2" not in synonyms:
            data = [{
                "entity_name": entity_name,
                "entity_values": {
                    "value": entity_value,
                    "synonyms": synonyms
                }
            }]
        else:
            synonyms.clear()
            data = [{
                "entity_name": entity_name,
                "entity_values": {
                    "value": entity_value
                }
            }]
        with open(r'C:\Users\Welcome\Chat_Bot\dataset\entity.json', 'a', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def intent_entity():
    data = [
        {
            "intent_name": intent_name,
            "entity_combinations": [
                {
                    "entity_name": entity_name,
                    "utterance": utterance,
                    "responses": responses
                }
            ]
        }
    ]
    with open(r'C:\Users\Welcome\Chat_Bot\dataset\intents.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def entity():
    data = {
               "entity_name": entity_name,
               "utterance": utterance,
               "response": responses
           },
    with open(r'C:\Users\Welcome\Chat_Bot\dataset\intents.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    while True:
        option = input("Press 'E' for Entity or 'I' for Intent or '2' to Exit:")
        if option == "I":
            intent_name = input("Intent_name:")
            count = 0
            while True:
                case = input("Add entity: y for Yes n for No:")
                if case == "y":
                    entity_name = input("Entity name:")
                    utterance = input("Utterance:").split(",")
                    responses = input("response:")
                    if count == 0:
                        intent_entity()
                        count += 1
                    else:
                        entity()
                elif case == "n":
                    break
        elif option == "E":
            get_entities()
        else:
            break
