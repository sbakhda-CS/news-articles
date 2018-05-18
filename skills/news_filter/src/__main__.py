from cortex_client import InputMessage, OutputMessage
import requests, json


# the headline function returns the top n headlines for any news source
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

    status, results, error_code, error_message = \
        filter(country, category, source, query, batch_size, batch_no, api_token, filter_type)

    if not error_code:
        return OutputMessage.create().with_payload(
                {'status': status, 'results': results}
            ).to_params()
    else:
        return OutputMessage.create().with_payload(
                {'error_code': error_code, 'error_message': error_message}
            ).to_params()


# source: news source from news api
# n: number of top articles from source
# api: api token for the website newsapi.org
def filter(country, category, source, query, batch_size, batch_no, api_token, filter_type):

    url = 'https://newsapi.org/v2/'

    if filter_type == 'top_filter':
        url += 'top-headlines?apiKey=' + api_token
        if source:
            url += '&source=' + source
        if country and not source:
            url += '&country=' + country
        if category and not source:
            url += '&category=' + category
        if query:
            url += '&query=' + query
        if batch_size:
            url += '&pageSize=' + str(batch_size)
        if batch_no:
            url += '&page=' + str(batch_no)

    elif filter_type == 'source_filter':
        url += 'sources?apiKey=' + api_token
        if country:
            url += '&country=' + country
        if category:
            url += '&category=' + category
        if source:
            pass

    elif filter_type == 'all_filter':
        url += 'everything?apiKey=' + api_token
        if source:
            url += '&source=' + source
        if query:
            url += '&query=' + query
        if batch_size:
            url += '&pageSize=' + str(batch_size)
        if batch_no:
            url += '&page=' + str(batch_no)

    else:
        status = None
        results = None
        error_code = 'wrongFilter'
        error_message = 'wrong filter'
        return status, results, error_code, error_message

    response = requests.get(url).json()

    if response['status'] != 'error' and not (response['code'] or response['message']):
        if response['articles']:
            return response['status'], response['articles'], None, None
        elif response['sources']:
            return response['status'], response['sources'], None, None
    else:
        return None, None, response['code'], response['message']