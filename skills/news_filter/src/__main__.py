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

    # the top news filter
    if filter_type == 'top_filter':

        url += 'top-headlines?apiKey=' + api_token

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

        if not(source or query or country or category):
            return  url, None, None, "noParams", "Add more parameters, such as country, category, query or  source"

        response = requests.get(url).json()

        e = error_check(url, response)
        if e is not None: return e

    # the news source filter
    elif filter_type == 'source_filter':

        url += 'sources?apiKey=' + api_token
        if country:
            url += '&country=' + country
        if category:
            url += '&category=' + category

        response = requests.get(url).json()

        if query is not None or query != "":
            return url, None, None, "wrongParams", "Query parameter is not applicable for source filter"

        if not(source or country or category):
            return url, None, None, "noParams", "Add more parameters, such as source, country or category"

        e = error_check(url, response)
        if e is not None: return e

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
        if source:
            url += '&source=' + str(source)
        if query:
            url += '&q=' + str(query)
        if batch_size:
            url += '&pageSize=' + str(batch_size)
        if batch_no:
            url += '&page=' + str(batch_no)

        if country or category:
            return url, None, None, "wrongParams", "Country and category parameters are not applicable for all filter"

        if not(source or query):
            return url, None, None, "noParams", "Add more parameters, such as query and source"

        response = requests.get(url).json()

        e = error_check(url, response)
        if e is not None: return e

    # wrong filter chosen
    else:
        status = None
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
    return url, response.get('status'), [], response.get('code'), response.get('message')


# error checking function
def error_check(url, response):

    # checking if response was received
    if response is None:
        return url, None, None, "noResponse", "No response was recieved"

    # checking if response had an error
    if response.get('status') == 'error' or \
            not(response.get('code') is None or response.get('message') is  None):
        return url, None, None, response.get('code'), response.get('message')

    # checking if response contains any results
    if (response.get('articles') is None and len(response.get('sources')) == 0) \
        or (response.get('sources') is None and len(response.get('articles')) == 0) :
        return url, None, None, "noResults", "No results are available for your request"

    # return None if no errors
    return None

#
# print(filter_news(None, None, None, "ben+ka+loda",1,1, "c474c16b92274c538f647d92387b00c7","all_filter"))
# print(filter_news(None, None, None, "ben+ka+loda",1,1, "c474c16b92274c538f647d92387b00c7","source_filter"))
# print(filter_news("in", "technology", "bbc-news" , "IT",10,1, "c474c16b92274c538f647d92387b00c7","top_filter"))

