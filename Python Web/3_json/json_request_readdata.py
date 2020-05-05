# using the requests library to access internet data

#import the requests library
import requests
import json


def main():
    # Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/json"
    result = requests.get(url)

    # TODO: Use the built-in JSON function to return parsed data
    data_object = result.json()
    #imprime el objeto de json
    print(data_object)
    #sin embargo si deseo imprimirlo lo correcto es transformalo
    #a json_string con dumps()
    print(json.dumps(data_object,indent=2))
    # TODO: Access data in the python object
    #to know all the keys of the json object
    print(list(data_object.keys()))

    sub_keys_list = []
    for sub_key in data_object['slideshow']:
        print(sub_key)
        sub_keys_list.append(sub_key)
    
    slides = []
    for titulos in data_object['slideshow'][sub_keys_list[2]]:
        slides.append(titulos)
    
    slide1 = slides[0]
    slide2 = slides[1]

    print("Voy a imprimir los {0} de los # {1} {2}:\n{3}\n{4}".format(sub_keys_list[3],len(data_object['slideshow']['slides']),sub_keys_list[2],slide1['title'], slide2['title']))

if __name__ == "__main__":
    main()
