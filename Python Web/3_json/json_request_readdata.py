# using the requests library to access internet data

#import the requests library
import requests
import json


def main():
    # Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/json"

    response = requests.get(url)

    #built-in JSON function to return parsed data
    json_object = response.json()

    #imprime el objeto de json
    print(json_object.keys())
    
    #sin embargo si deseo imprimirlo lo correcto es transformalo
    #a json_string con dumps()
    json_en_python = json.dumps(json_object,indent=2)
    print(json_en_python)
    
    
    #to know all the keys of the json object
    print(list(json_en_python.keys()))

    sub_keys_list = []
    for sub_key in json_en_python['slideshow']:
        print(sub_key)
        sub_keys_list.append(sub_key)
    
    slides = []
    for titulos in json_en_python['slideshow'][sub_keys_list[2]]:
        slides.append(titulos)
    
    slide1 = slides[0]
    slide2 = slides[1]

    print("Voy a imprimir los {0} de los # {1} {2}:\n{3}\n{4}".format(sub_keys_list[3],len(json_en_python['slideshow']['slides']),sub_keys_list[2],slide1['title'], slide2['title']))

if __name__ == "__main__":
    main()31328-929*
