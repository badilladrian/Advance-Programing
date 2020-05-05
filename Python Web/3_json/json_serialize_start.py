# Process JSON data returned from a server
"""This program does the opposite from what we handled,
it takes a proper dictionary object and transforms it into
a Json String objec with the function dumps()"""

# use the JSON module
import json


def main():
    # define a python ditcionary
    pythonData = {
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": ["Thousand Island Dressing",
                     "Sauerkraut",
                     "Pickles"
                     ],
        "price": 8.99
    }

    # TODO: serialize to JSON using dumps
    my_json_string = json.dumps(pythonData, indent=4)

    # TODO: print the resulting JSON string
    print("JSON Data: --------")
    print(my_json_string)


if __name__ == "__main__":
    main()
