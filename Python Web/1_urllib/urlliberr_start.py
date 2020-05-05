# handling errors and status codes

# TODO: import the request, error, and status modules
import urllib.request
from urllib.error import HTTPError, URLError
from http import HTTPStatus

def main():
    url = "http://no-such-server.org"      # will generate a URLError
    #url = "http://httpbin.org/status/404"  # will generate an HTTPError
    #url = "http://httpbin.org/html"         # should work with no errors

    try:
        # TODO: use exception handling to attempt the URL access
        result = urllib.request.urlopen(url)
        print("Result code: {0}".format(result.status))

        if (result.getcode() == 200):
            print(result.read().decode('utf-8'))
    #manejamos los errores de HTTP
    except HTTPError as error:
        print("This is an error type:", error)
        print(type(error))
        print(error.headers,error.url,error.msg)
    except URLError as errorURL:
        print("Error de URL", errorURL)

if __name__ == "__main__":
    main()

