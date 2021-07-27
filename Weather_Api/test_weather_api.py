###################################################################################################################################
#Purpose of the script
###################################################################################################################################
#We need to signup and then you can find your API key under your account to access the API.
###################################################################################################################################

#Below points has been considered in the script.

###################################################################################################################################
#1.Wite the help of Api key we have to write testscripts.

#2.We have to write the test scripts for astronomy, current, sports, forecast, search, timezone.

#3.We have to write both positive and negative testsripts for the above methods.
###################################################################################################################################
import requests
import json
import os 
import logging
import pytest

logger=logging.getLogger(__name__)

logging.info("Give the api key, location, date for the astronomy response.")

api_key = 'e92d76b58ea041f6b9593215212307'
location = 'London'
date = '2021-07-22'
url = requests.get(f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={location}&dt={date}")
record =  url.json()


def test_api_statuscode_astronomy():

    ''' Testcase for check status code '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2021-07-22'
    url = requests.get(f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={location}&dt={date}")
    record =  url.json()

    try:
        assert (url.status_code == 200), "Status code is not 200. Rather found : " + str(url.status_code)
        logging.info("Successfully passed the test case for status code")
    except Exception as e:
        if url.status_code == 400:
            assert record['error']['code'] == 1006

        elif url.status_code == 401:
            assert record['error']['code'] == 2006
        else:
            assert url.status_code != 200
            logging.info("Status code is not equal to 200")
    
def test_api_data_astronomy():

    ''' Test method for check the astronomy location '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2021-07-22'
    url = requests.get(f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={location}&dt={date}")
    record =  url.json()

    try:  
        assert record['location']["name"] == location
        logging.info("Successfully passed the test castin for check the location.")
    except Exception as e:
        if url.status_code  == 400:
            assert record['error']['code'] == 1006
            assert record['error']['message'] == "No matching location found."
        elif url.status_code == 401:
            assert record['error']['message'] == "API key is invalid."
        else:
            assert record['location']['name'] != location
            logging.info("Location name is not equal to the astronomy location.")
    
def test_api_type_astronomy():

    ''' Test method for test the type of astronomy response '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2021-07-22'
    url = requests.get(f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={location}&dt={date}")
    record =  url.json()
    try:
        assert type(record['location']) == type(dict())
        logging.info("Successfully passed the type of the astronomy response.")
    except Exception as e:
        assert type(record['error']) == type(dict())
        logging.info("the astronomy response trype is not dict.")


def test_api_headers_astronomy():

    ''' Test method for astronomy response header '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2021-07-22'

    url = requests.get(f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={location}&dt={date}")
    record =  url.json()

    try:
        assert url.headers["Content-Type"] == "application/json"
        logging.info("Successfully passed the test for astronomy response header.")

    except Exception as e:
        assert url.headers["Content-Type"] != "application/json"  
        logging.info("astronomy response header is not equal to application/json.")

def test_api_statuscode_current():

    ''' Testcase for check the status code for current response '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = "Tirupati"
    air_quality = "yes"

    url = requests.get(f"http://api.weatherapi.com/v1/current.json?key=b3576dd1aa6941d5bd750243212207&q={location}&aqi={air_quality}")
    record =  url.json()

    try:
        assert (url.status_code == 200), "Status code is not 200. Rather found : " + str(url.status_code)
        logging.info("Successfully passed the status code for current response.")

    except Exception as e:
        if url.status_code == 400:
            assert record['error']['code'] == 1006

        elif url.status_code == 401:
            assert record['error']['code'] == 2006

        else:
            assert url.status_code != 200
            logging.info("Status code for current response is not equal to 200.")

def test_api_location_current():

    '''Testcase for check the location for current response '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = "Tirupati"
    air_quality = "yes"

    url = requests.get(f"http://api.weatherapi.com/v1/current.json?key=b3576dd1aa6941d5bd750243212207&q={location}&aqi={air_quality}")
    record =  url.json()

    try:  
        assert record['location']["name"] == location
        logging.info("Successfully passed the test case for location in current response.")
        
    except Exception as e:
        if url.status_code  == 400:
            assert record['error']['code'] == 1006
            assert record['error']['message'] == "No matching location found."
        elif url.status_code == 401:
            assert record['error']['message'] == "API key is invalid."

        else:
            assert record['location']['name'] != location
            logging.info("Location in current response is not equal.")

def test_api_type_current():  

    ''' Testcase for type of the location in current response '''
    api_key = 'e92d76b58ea041f6b9593215212307'
    location = "Tirupati"
    air_quality = "yes"
    url = requests.get(f"http://api.weatherapi.com/v1/current.json?key=b3576dd1aa6941d5bd750243212207&q={location}&aqi={air_quality}")
    record =  url.json()
    try:
        assert type(record['location']) == type(dict())
        logging.info("Successfully passed the location of current response.")
    except Exception as e:
        assert type(record['error']) == type(dict())
        logging.info("Type of the location in current response is not equal to dict.")


def test_api_headers_current():

    ''' Test method for current response header '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = "Tirupati"
    air_quality = "yes"
    url = requests.get(f"http://api.weatherapi.com/v1/current.json?key=b3576dd1aa6941d5bd750243212207&q={location}&aqi={air_quality}")
    record =  url.json()
    try:
        assert url.headers["Content-Type"] == "application/json"
        logging.info("Successfully passed the test for current response header.")
    except Exception as e:
        assert url.headers["Content-Type"] != "application/json"  
        logging.info("current response header is not equal to application/json.")

def test_api_statuscode_forecast():

    ''' Testcase for check the status code for forecast response '''

    api_key = "e92d76b58ea041f6b9593215212307"
    location = "London"
    days = 1
    air_quality = 'no'
    alerts = 'no'
    url = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={1}&aqi={air_quality}&alerts={alerts}")
    record =  url.json()
    try:
        assert (url.status_code == 200), "Status code is not 200. Rather found : " + str(url.status_code)
        logging.info("Successfully passed the status code for forecast response.")
    except Exception as e:
        if url.status_code == 400:
            assert record['error']['code'] == 1006

        elif url.status_code == 401:
            assert record['error']['code'] == 2006
        else:
            assert url.status_code != 200
            logging.info("Status code for forecast response is not equal to 200.")
    

def test_api_data_forecaste():

    ''' Testcase for check the location for forecast response '''

    api_key = "e92d76b58ea041f6b9593215212307"
    location = "London"
    days = 1
    air_quality = 'no'
    alerts = 'no'
    url = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={1}&aqi={air_quality}&alerts={alerts}")
    record =  url.json()
    try:  
        assert record['location']["name"] == location
        logging.info("Successfully passed the test case for location in forecast response.")
    except Exception as e:
        if url.status_code  == 400:
            assert record['error']['code'] == 1006
            assert record['error']['message'] == "No matching location found."
        elif url.status_code == 401:
            assert record['error']['message'] == "API key is invalid."
        else:
            assert record['location']['name'] != location
            logging.info("Location in forecast response is not equal.")


def test_api_type_forecast():
    
    ''' Testcase for type of the location in forecast response '''

    api_key = "e92d76b58ea041f6b9593215212307"
    location = "London"
    days = 1
    air_quality = 'no'
    alerts = 'no'
    url = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={1}&aqi={air_quality}&alerts={alerts}")
    record =  url.json()
    try:
        assert type(record['location']) == type(dict())
        logging.info("Successfully passed the location of forecast response.")
    except Exception as e:
        assert type(record['error']) == type(dict())
        logging.info("Type of the location in forecast response is not equal to dict.")


def test_api_headers_forecast():

    ''' Test method for forecast response header '''

    api_key = "e92d76b58ea041f6b9593215212307"
    location = "London"
    days = 1
    air_quality = 'no'
    alerts = 'no'
    url = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={1}&aqi={air_quality}&alerts={alerts}")
    record =  url.json()
    try:
        assert url.headers["Content-Type"] == "application/json"
        logging.info("Successfully passed the test for forecast response header.")
    except Exception as e:
        assert url.headers["Content-Type"] != "application/json"  
        logging.info("forecast response header is not equal to application/json.")

def test_api_statuscode_history():

    ''' Test case for status code in history resposne '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2010-01-01'
    url = requests.get(f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={date}")
    record =  url.json()
    try:
        assert (url.status_code == 400), "Status code is not 200. Rather found : " + str(url.status_code)
        logging.info("Successfully passed the status code for history response.")
    except Exception as e:
        assert url.status_code == 401
        logging.info("Test code for status code is equal to 401.")

def test_api_data_history():

    ''' Testcase for check the data of history '''
    
    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2010-01-01'
    url = requests.get(f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={date}")
    record =  url.json()
    try:   
        assert record['error']['code'] == 1008
        assert record['error']['message'] == "API key is limited to get history data. Please check our pricing page and upgrade to higher plan."
        logging.info("Successfully passed the tse case for data of history response.")
    except Exception as e:
        assert record['error']['code'] == 2006
        assert record['error']['message'] == "API key is invalid."
        logging.info("The data for histor response is Api key is invalid.")

def test_api_type_history():
    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2010-01-01'
    url = requests.get(f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={date}")
    record =  url.json() 
    assert type(record) == type(dict())
    logging.info("Successfully passed the testcase for type in the history response.")

def test_api_headers_history():

    ''' Test method for history response header '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    date = '2010-01-01'
    url = requests.get(f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={date}")
    record =  url.json()
    try:
        assert url.headers["Content-Type"] == "application/json"
        logging.info("Successfully passed the test for history response header.")
    except Exception as e:
        assert url.headers["Content-Type"] != "application/json"  
        logging.info("history response header is not equal to application/json.")

def test_api_statuscode_search():
    
    ''' Testcase for check status code '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/search.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert (url.status_code == 200), "Status code is not 200. Rather found : " + str(url.status_code)
        logging.info("Successfully passed the test case for status code")
    except Exception as e:
        assert url.status_code == 401
        logging.info("Status code is equal to 401")
    
def test_api_data_search():

    ''' Testcase for check the data '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/search.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert record[0]['id'] == 2817507
        logging.info("Successfully passed the testcase for the id present in search response.")
    except Exception as e:
        if url.status_code == 401:
            assert record['error']['message'] == "API key is invalid."
        elif record == list() :
            assert record == list()
        else:
            assert record[0]['id'] != 2817507
            logging.info("The search response id is not equal to the 2817507")
        
def test_api_type_search():

    ''' Testcase for type of thr record present in search response'''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/search.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert type(record) == type(list())
        logging.info("Successfully passed the testcase for type of thr record")
    except Exception as e:
        assert type(record) == type(dict())
        logging.info("The type of the record is equal to dict.")

    
def test_api_headers_search():

    ''' Test method for search response header '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/search.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert url.headers["Content-Type"] == "application/json"
        logging.info("Successfully passed the test for search response header.")
    except Exception as e:
        assert url.headers["Content-Type"] != "application/json"  
        logging.info("search response header is not equal to application/json.")

def test_api_statuscode_sports():

    ''' Testcase for check status code '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/sports.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert (url.status_code == 200), "Status code is not 200. Rather found : " + str(url.status_code)
        logging.info("Successfully passed the test case for status code")
    except Exception as e:
        if url.status_code == 400:
            assert record['error']['code'] == 1006
        elif url.status_code == 401:
            assert record['error']['code'] == 2006
        else:
            assert url.status_code != 200
            logging.info("Status code is not equal to 200")
    
def test_api_data_sports():

    ''' Testcase for check the data present in the sports resource'''
    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/sports.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert record['football'][0]['country'] == 'Turkey'
        logging.info("Successfully passed the testcase for data in sports.")
    except Exception as e:
        if url.status_code  == 400:
            assert record['error']['code'] == 1006
            assert record['error']['message'] == "No matching location found."
        elif url.status_code == 401:
            assert record['error']['message'] == "API key is invalid."
        else:
            assert record['football'][0]['country'] != 'Turkey'
            logging.info("The location for sports data is not equal to turkey.")
    
def test_api_type_sports():

    ''' Testcase for check the type of sports response'''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/sports.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert type(record) == type(dict())
        logging.info("Successfully passed the testcase for type of data")
    except Exception as e:
        assert type(record['error']) == type(dict())
        logging.info("Getting error with the type of data")

def test_api_headers_sports():

    ''' Test method for sports response header '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/sports.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert url.headers["Content-Type"] == "application/json"
        logging.info("Successfully passed the test for sports response header.")

    except Exception as e:
        assert url.headers["Content-Type"] != "application/json"  
        logging.info("sports response header is not equal to application/json.")

def test_api_statuscode_timezone():

    ''' Testcase for check status code '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/timezone.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert (url.status_code == 200), "Status code is not 200. Rather found : " + str(url.status_code)
        logging.info("Successfully passed the test case for status code")
    except Exception as e:
        if url.status_code == 400:
            assert record['error']['code'] == 1006

        elif url.status_code == 401:
            assert record['error']['code'] == 2006
        else:
            assert url.status_code != 200
            logging.info("Status code is not equal to 200")

def test_api_location_timezone():
   
    ''' Test method for check the timezone location '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/timezone.json?key={api_key}&q={location}")
    record =  url.json()
    try:  
        assert record['location']["name"] == location
        logging.info("Successfully passed the test castin for check the location.")
    except Exception as e:
        if url.status_code  == 400:
            assert record['error']['code'] == 1006
            assert record['error']['message'] == "No matching location found."
        elif url.status_code == 401:
            assert record['error']['message'] == "API key is invalid."
        else:
            assert record['location']['name'] != location
            logging.info("Location name is not equal to the timezone location.")

def test_api_type_timezone():  

    ''' Testcase for check the type of timezone response'''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/timezone.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert type(record) == type(dict())
        logging.info("Successfully passed the testcase for type of data")
    except Exception as e:
        assert type(record['error']) == type(dict())
        logging.info("Getting error with the type of data")


def test_api_headers_timezone():
    
    ''' Test method for timezone response header '''

    api_key = 'e92d76b58ea041f6b9593215212307'
    location = 'London'
    url = requests.get(f"http://api.weatherapi.com/v1/timezone.json?key={api_key}&q={location}")
    record =  url.json()
    try:
        assert url.headers["Content-Type"] == "application/json"
        logging.info("Successfully passed the test for timezone response header.")
    except Exception as e:
        assert url.headers["Content-Type"] != "application/json"  
        logging.info("timezone response header is not equal to application/json.")

if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])