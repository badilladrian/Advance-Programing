# using the requests library to access internet data

import requests 
from requests.exceptions import HTTPError, Timeout

def main():
    handling_errors()

def handling_errors():
    # Use requests to issue a standard HTTP GET request
    try:
        #url = "http://httpbin.org/status/404"
        url = "http://httpbin.org/delay/5"
        result = requests.get(url, timeout=2)
        result.raise_for_status()
        printResults(result)
    except HTTPError as error:
        print("Error: {0}".format(error))
    except Timeout as error:
        print("There is a timeout error: ", error)
    

def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Returned data: ----------------------")
    print(resData.text)


if __name__ == "__main__":
    main()
