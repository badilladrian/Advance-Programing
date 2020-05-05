# Process JSON data returned from a server

# use the JSON module
import json
from json import JSONDecodeError


def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''
    json_object = parseString_toJsonObj(jsonStr)
    imprimir_json(json_object)

def parseString_toJsonObj(jsonStr):

    try:#if there is an error at the json string
        # parse the JSON data using loads
        data = json.loads(jsonStr)
        return data
    except JSONDecodeError as error:
        print("There is an error at the JSON")
        print("Which is: ", error.msg, "at line: ", error.lineno , "column: ", error.colno)

def imprimir_json(json):
    print("Sandwich: " + json['sandwich'])
    if (json['toasted']):
        print("And it's toasted!")
    for topping in json['toppings']:
        print("Topping: " + topping)


if __name__ == "__main__":
    main()
