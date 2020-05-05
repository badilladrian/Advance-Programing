# using urllib to request data
import urllib.request
# TODO: import the urllib request class
import urllib.parse #to CODE instead of decode at request

def url_simple():
    url = "http://httpbin.org/xml"

    # TODO: open the URL and retrieve some data
    result_simple = urllib.request.urlopen(url)
    # TODO: Print the result code from the request, should be 200 OK
    print("Result code: {0}".format(result_simple.status))

    # TODO: print the returned data headers
    print("Headers: ----------------------")
    print(result_simple.getheaders())

    # TODO: print the returned data itself
    print("Returned data: ----------------------")
    print(result_simple.read().decode('utf-8'))

def url_custom():
    url = "http://httpbin.org/xml"

    #creo un diccionario con los argumentos a enviar
    args = {
        "name": "Adrian Badilla",
        "is_author": True
    }
    
    #my args need to be url-encoded 
    data = urllib.parse.urlencode(args)

    #When I open an URL it retrieves back an HTTP Response
    http_response = urllib.request.urlopen(url + "?" + data)

    print("Result code: {0}".format(http_response.status))
                #the status is a property of the http object

    print("RETURNED DATA:-----------")
    print(http_response.read().decode("utf-8"), "\nURL:  {0} DUE THE FACT THAT \n{1}  QUERY ? ADDED.".format(http_response.url,args))

def url_post():
    #creo un diccionario con los argumentos a enviar
    args = {
        "name": "Adrian Badilla",
        "is_author": True
    }
    #los encondeo en URL
    mis_datos = urllib.parse.urlencode(args)

    url = "http://httpbin.org/post"
    mi_post = mis_datos.encode()
    #ahora los encondeo como datos para enviar

    result = urllib.request.urlopen(url, data=mi_post)

    print("Siempre imprimo el resultado : {0}".format(result.status))
    print("\n\n la data de mi response es:", result.read().decode("UTF-8"))

    
def main():
    url_custom()
    url_post()
    

if __name__ == "__main__":
    main()
