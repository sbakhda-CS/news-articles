from cortex_client import InputMessage, OutputMessage

# to get an API response
import requests


# does various news filters and returns an OutputMessage object
def main(params):
    # Parse the function params
    msg = InputMessage.from_params(params)

    # Get input parameters
    source = msg.payload.get('source')
    category = msg.payload.get('category')
    country = msg.payload.get('country')
    query = msg.payload.get('query')

    # Get properties
    batch_size = msg.properties.get('batch_size')
    batch_no = msg.properties.get('batch_no')
    api_token = msg.properties.get('api_token')
    filter_type = msg.properties.get('filter_type')

    # get an API response
    response = \
        filter_news(country, category, source, query, batch_size, batch_no, api_token, filter_type)

    # convert response to strings
    url, status, results, error_code, error_message = (str(x) for x in response)

    # return the status and results if no error
    if error_code == "None":
        return OutputMessage.create().with_payload(
                {'status': status + ": " + url, 'results': results}
            ).to_params()
    # return error code and message if error
    else:
        return OutputMessage.create().with_payload(
                {'status': status + ": " + url, 'error_code': error_code, 'error_message': error_message}
            ).to_params()


# INPUTS
# country: the 2-letter ISO 3166-1 code of the country you want to get headlines for
# category: one of 'business', 'sports', 'entertainment', 'general', 'health', 'science', 'technology'
# source: one of the news source list on https://newsapi.org/sources
# query: a URL-encoded keyword query to search. Check https://newsapi.org/ for more information
# batch_size: number of results per request (up to 100)
# batch_no: batch number from which to display results
# api_token: api token for the website newsapi.org
# filter_type: can be one of 'all_filter', 'top_filter', and 'source_filter'

# OUTPUTS
# url: the url of the request
# status: error status of response
# results: array of articles or sources
# error_code: the error code
# error_message: the error message
def filter_news(country, category, source, query, batch_size, batch_no, api_token, filter_type):

    # initialize the url to request
    url = 'https://newsapi.org/v2/'

    # check if batch_size and batch_no are valid
    if batch_size is not None:
        if batch_size > 100: batch_size = 100
        if batch_size < 1: batch_size = 1
    else:
        batch_size = 5
    if batch_no is not None:
        if batch_no < 1: batch_no = 1
    else:
        batch_no = 1

    # check if category is valid
    if category is not None:
        if category not in ['business', 'sports', 'entertainment', 'general', 'health', 'science', 'technology']:
            return url, "error", None, "wrongCategory", \
       "Category must be one of 'business', 'sports', 'entertainment', 'general', 'health', 'science', 'technology'."


    # the top news filter
    if filter_type == 'top_filter':

        url += 'top-headlines?apiKey=' + api_token

        # adding parameters to URL
        if source:
            url += '&sources=' + source
        if country and not source:
            url += '&country=' + country
        if category and not source:
            url += '&category=' + category
        if query:
            url += '&q=' + query
        if batch_size:
            url += '&pageSize=' + str(batch_size)
        if batch_no:
            url += '&page=' + str(batch_no)

        # getting the response and checking for errors
        if not(source or country or category):
            return url, "error", None, "tooFewParams", "Add more parameters, such as country, category, query or  source"

        response = requests.get(url).json()

        e = error_check(url, response)
        if e is not None: return e

    # the news source filter
    elif filter_type == 'source_filter':

        url += 'sources?apiKey=' + api_token

        # adding parameters to URL
        if country:
            url += '&country=' + country
        if category:
            url += '&category=' + category

        # getting the response and checking for errors
        response = requests.get(url).json()

        if query is not None:
            return url, "error", None, "wrongParams", "Query parameter is not applicable for source filter"

        if not(source or country or category):
            return url, "error", None, "tooFewParams", "Add more parameters, such as source, country or category"

        e = error_check(url, response)
        if e is not None: return e

        # filtering batch_size, batch_no, and source from the results
        ss = response.get('sources')

        if source:
            ss = list(filter(lambda x: x.get('id') == source, ss))

        if batch_size < 1 or batch_no < 1:
            beg = 0
        else:
            beg = batch_size * (batch_no - 1)
            if beg > len(ss): beg = 0
        if batch_size > len(ss) or batch_no > len(ss):
            end = len(ss)
        else:
            end = batch_size * batch_no
            if end > len(ss): end = len(ss)

        response['sources'] = ss[beg: end]

    # the 'all' filter
    elif filter_type == 'all_filter':

        url += 'everything?apiKey=' + api_token

        # adding parameters to URL
        if source:
            url += '&sources=' + str(source)
        if query:
            url += '&q=' + str(query)
        if batch_size:
            url += '&pageSize=' + str(batch_size)
        if batch_no:
            url += '&page=' + str(batch_no)

        # getting the response and checking for errors
        if country or category:
            return url, "error", None, "wrongParams", "Country and category parameters are not applicable for all filter"
        if not(source or query):
            return url, "error", None, "tooFewParams", "Add more parameters, such as query and source"

        response = requests.get(url).json()

        e = error_check(url, response)
        if e is not None: return e

    # wrong filter chosen
    else:
        status = "error"
        results = None
        error_code = 'wrongFilter'
        error_message = 'wrong filter'
        return url, status, results, error_code, error_message

    # return the resulting articles or sources
    if response.get('articles'):
        return url, response.get('status'), response.get('articles'), None, None
    elif response.get('sources'):
        return url, response.get('status'), response.get('sources'), None, None

    # return empty array when no results
    # return url, response.get('status'), [], response.get('code'), response.get('message')
    return url, response.get('status'), [], None, response.get('message')


# error checking function
def error_check(url, response):

    # checking if response was received
    if response is None:
        return url, "error", None, "noResponse", "No response was recieved"

    # checking if response had an error
    if response.get('status') == 'error' or \
            not(response.get('code') is None or response.get('message') is  None):
        return url, "error", None, response.get('code'), response.get('message')

    # checking if response contains any results
    if (response.get('articles') is None and len(response.get('sources')) == 0) \
        or (response.get('sources') is None and len(response.get('articles')) == 0) :
        return url, "error", None, "noResults", "No results are available for your request"

    # return None if no errors
    return None