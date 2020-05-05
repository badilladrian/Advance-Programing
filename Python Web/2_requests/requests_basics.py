# using the requests library to access internet data

#import the requests library
import requests as request

def main():
    # TODO: Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/xml"
    response = request.head(url) #HEAD
    printResults(response)

    data_values = {
        "key1": "valor1",
        "llave2": "valor2"
    }
    #PUT
    rput = request.put('https://httpbin.org/put', data = {'key':'mi_valor3'})
    printResults(rput)

    #POST
    rpost = request.post('https://httpbin.org/post',headers={"User-Agent":"Adrian Badilla API / 1.5.9"}, params = data_values)
    printResults(rpost)

    #DELETE
    rdelete = request.delete('https://httpbin.org/delete')
    printResults(rdelete)

    #GET
    rget = request.get('https://httpbin.org/get', params=data_values)
    printResults(rget)

    #OPTIONS
    roptions = request.options('https://httpbin.org/get')
    printResults(roptions)
    
    # TODO: Send some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding


    # TODO: Pass a custom header to the server

    

def printResults(respuesta):
    print("CODE: {0} FROM: {1}".format(respuesta.status_code, respuesta.url))
    print("\n")

    print("Headers: ----------------------")
    print(respuesta.headers)
    print("\n")

    print("Returned data: ----------------------")
    print(respuesta.text, "\n\n")
    print("NEW METHOD CALL ----------------------")


if __name__ == "__main__":
    main()
