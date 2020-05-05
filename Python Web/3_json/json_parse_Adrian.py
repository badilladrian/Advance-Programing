# Process JSON data returned from a server
"""When a server returns the HTTP request -> response 
it gives back a JSON, which I retrieve as plain text after
is decode. We can take this jsonString and parse it into a 
JSON Object with the json module and the loads() function"""

# TODO: use the JSON module
import json

def main():
    # define a string of JSON code
    jsonStr = '''{
            "mi_nombre" : "Adrian",
            "programador" : true, 
            "skills" : [
                "Python  ",
                "Web Services",
                "REST API"
            ],
            "salary" : 3000
        }'''

    # TODO: parse the JSON data using loads
    data = json.loads(jsonStr)

    # TODO: print information from the data structure
    print("Programmer: " + data['mi_nombre']) #key nombre Adrian
    if (data['programador']): #boolean en javascript
        print("I work for Isthmus") 
    #los array son listas
    for item in data['skills']:
        print(item)

if __name__ == "__main__":
    main()
