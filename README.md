---
title: "News Articles"
date: "2018-05-21"
toc: true
menu:
  main:
    parent: "ml-skills"
    identifier: "news-articles"
---

News Api is an API to get the latest news articles from over 30,000 sources in various languages and countries. There are 3 main ways to find news from the API:
- finding top headlines
- finding articles
- finding news sources

The News Articles skill uses this API to fetch data about articles and sources

## Use cases
- Latest news: finding the trending articles and topics in different countries and categories
- Keyword search: find articles containing certain keywords
- News Sources: finding sources in different countries and categories

## Properties
The skill takes 4 properties:
- api_tokens: API token for using the website https://newsapi.org/
- filter_type: type of filter, must be one of: 
	1. top_filter: filtering the top headlines based on country, category, source, and/or query
	2. all_filter: filtering all the articles based on source and/or query
	3. source_filter: filtering the news sources based on country, category, and/or source
- batch_size: The response for any query comes in chunks or batches. batch_size is the number of results to be returned per request. Must be between 1 and 100. 
- batch_no: The [batch_no]th batch containing [batch_size] results is returned. Must be at least 1. 

## Inputs
The skill takes up to 4 inputs: 
- country: The 2-letter ISO 3166-1 code of the country you want to get headlines for. Check https://newsapi.org/sources for the complete list. Note: you can't mix this param with the sources param.
- category: Must be one of 'business', 'sports', 'entertainment', 'general', 'health', 'science', 'technology'
- source: Must be one from the list on https://newsapi.org/sources
- query: Keywords or phrases to search for.

	Advanced search is supported here:

	Surround phrases with quotes (") for exact match.
	Prepend words or phrases that must appear with a + symbol. Eg: +bitcoin
	Prepend words that must not appear with a - symbol. Eg: -bitcoin
	Alternatively you can use the AND / OR / NOT keywords, and optionally group these with parenthesis. Eg: crypto AND (ethereum OR litecoin) NOT bitcoin.
	The complete value for the query must be URL-encoded.

## Outputs
The skill returns up to 4 outputs:
- status: the status of the request and the request url. "ok: [url]" if no errors, and "error: [url]" if errors. 
- results: the array of objects returned. Can be an array of article objects or an array of source objects depending on the request. 
- error_code: the error code, if any errors
- error_message: a descriptive error message, if any errors 

### Sample Input: top_filter
```
{
    "payload": {
        "country" : "ru",
        "category": "sports"
    },
    "properties": {
        "api_token": "c474c16b92274c538f647d92387b00c7",
        "filter_type": "top_filter",
        "batch_size": 4,
        "batch_no": 1
    }
}
```

### Sample Output: top_filter

```
{  
   "payload":{  
      "status":"ok: https://newsapi.org/v2/top-headlines?apiKey=c474c16b92274c538f647d92387b00c7&country=ru&category=sports&pageSize=4&page=1",
      "results":"[{'source': {'id': None, 'name': 'Tass.ru'}, 'author': None, 'title': 'Футболист \"Зенита\" Паредес расстроен непопаданием в состав сборной Аргентины на ЧМ-2018', 'description': 'В минувшем сезоне полузащитник провел 28 матчей в составе \"Зенита\" во всех турнирах, отметившись 4 голами и 7 результативными', 'url': 'http://tass.ru/sport/5220005', 'urlToImage': 'https://phototass4.cdnvideo.ru/width/1200_4ce85301/tass/m2/uploads/i/20180521/4702536.jpg', 'publishedAt': '2018-05-21T19:21:25Z'}, {'source': {'id': None, 'name': 'Gazeta.ru'}, 'author': None, 'title': 'Допинг в футболе: о сборной России сняли фильм', 'description': 'Известный немецкий журналист и автор ряда фильмов о допинге в спорте Хайо Зеппельт выпустил свою новую работу, где в центре скандала оказалась российская сборная по футболу. Как утверждает автор фильма, игроки национальной команды принимали запрещенные препар…', 'url': 'https://www.gazeta.ru/sport/2018/05/21/a_11759665.shtml', 'urlToImage': 'https://img.gazeta.ru/files3/743/11759743/RIAN_3209767.HR-pic905-895x505-73754.jpg', 'publishedAt': '2018-05-21T18:56:16Z'}, {'source': {'id': None, 'name': 'Sport-express.ru'}, 'author': None, 'title': 'Английские фанаты готовы устроить \"третью мировую\" на ЧМ-2018', 'description': 'Английские фанаты готовятся к противостояниям с российскими во время ЧМ-2018.', 'url': 'http://www.sport-express.ru/football/world/chempionat-mira-2018/news/angliyskie-fanaty-gotovy-ustroit-tretyu-mirovuyu-na-chm-2018-1411626/', 'urlToImage': 'http://ss.sport-express.ru/userfiles/materials/122/1226526/large.jpg', 'publishedAt': '2018-05-21T18:55:05Z'}, {'source': {'id': None, 'name': 'Sport-express.ru'}, 'author': None, 'title': 'Вернуть былое. Хованцев и Польховский – снова в нашей сборной', 'description': 'Стали известны фамилии старших тренеров на следующий сезон. Есть сюрпризы.', 'url': 'https://www.sport-express.ru/biathlon/reviews/vernut-byloe-hovancev-i-polhovskiy-snova-v-nashey-sbornoy-1411619/', 'urlToImage': 'https://ss.sport-express.ru/userfiles/materials/122/1226520/large.jpg', 'publishedAt': '2018-05-21T18:34:44Z'}]"
   },
   "typeName":"cortex/Any"
}
```


### Sample Input: all_filter
```
{
    "payload": {
        "source":"cnn",
        "query": "trump"
    },
    "properties": {
        "api_token": "c474c16b92274c538f647d92387b00c7",
        "filter_type": "all_filter",
        "batch_no": 1000
    }
}
```

### Sample Output: all_filter
```
{  
   "payload":{  
      "status":"ok: https://newsapi.org/v2/everything?apiKey=c474c16b92274c538f647d92387b00c7&sources=cnn&q=trump&pageSize=5&page=1000",
      "results":"[{'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'AngelaBonachera', 'title': '5 preguntas que Mark Zuckerberg esquivó ante el Capitolio de Estados Unidos', 'description': 'Zuckerberg daba respuestas vagas y con frecuencia les decía a los miembros del Congreso que su equipo las ampliaría más adelante. Estas son algunas de las cuestiones que quedan por saber.', 'url': 'http://cnnespanol.cnn.com/2018/04/12/5-preguntas-que-mark-zuckerberg-esquivo-ante-el-capitolio-de-estados-unidos/', 'urlToImage': 'https://cnnespanol2.files.wordpress.com/2018/04/180411113650-zuckerberg-hearing-041118-780x439.jpg?quality=100&strip=info', 'publishedAt': '2018-04-12T14:59:29Z'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Catherine E. Shoichet, CNN', 'title': 'ICE raided a meatpacking plant. More than 500 kids missed school the next day', 'description': 'Teachers in local schools suddenly found themselves on the front lines of a crisis after immigration authorities swept through a Tennessee meatpacking plant.', 'url': 'https://www.cnn.com/2018/04/12/us/tennessee-immigration-raid-schools-impact/index.html', 'urlToImage': 'https://cdn.cnn.com/cnnnext/dam/assets/180411155138-southeastern-provisions-raid---restricted-super-tease.jpg', 'publishedAt': '2018-04-12T11:01:28Z'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Madison Park, CNN', 'title': 'What cities and states are doing about guns since the Parkland shooting', 'description': \"Local and state lawmakers aren't holding their breath waiting for the federal government to take action on guns. Here are some highlights of what has passed.\", 'url': 'https://www.cnn.com/2018/04/09/us/gun-laws-since-parkland/index.html', 'urlToImage': 'https://cdn.cnn.com/cnnnext/dam/assets/121226212822-new-york-guns-super-tease.jpg', 'publishedAt': '2018-04-09T08:23:11Z'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'CNN Library', 'title': 'CIA Directors Fast Facts', 'description': \"Read CNN's Fast Facts about directors of the CIA. The CIA collects information about foreign governments, organized crime and terrorist groups.\", 'url': 'https://www.cnn.com/2013/11/12/us/cia-directors-fast-facts/index.html', 'urlToImage': 'https://cdn.cnn.com/cnnnext/dam/assets/140526145440-cia-seal-super-tease.png', 'publishedAt': '2018-04-06T13:57:54Z'}, {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Melissa Velásquez Loaiza', 'title': 'Facebook trata de sacudirse los escándalos del pasado y presenta nuevas funciones', 'description': 'La red social trata de seguir adelante luego de una crisis de relaciones públicas por el escándalo de Cambridge Analytica. Facebook presentó nuevas herramientas y nuevas medidas de seguridad. Esto es lo nuevo.', 'url': 'http://cnnespanol.cnn.com/2018/05/02/facebook-trata-de-sacudirse-los-escandalos-del-pasado-y-presenta-nuevas-funciones/', 'urlToImage': 'https://cnnespanol2.files.wordpress.com/2018/05/facebook-f8conference.jpg?quality=100&strip=info&w=1200', 'publishedAt': '2018-05-02T15:41:17Z'}]"
   },
   "typeName":"cortex/Any"
}
```


### Sample Input: source_filter
```
{
    "payload": {
        "country": "in"
    },
    "properties": {
        "api_token": "c474c16b92274c538f647d92387b00c7",
        "filter_type": "source_filter",
        "batch_size": 100,
        "batch_no": 1
    }
}
```

### Sample Output: source_filter
```
{  
   "payload":{  
      "status":"ok: https://newsapi.org/v2/sources?apiKey=c474c16b92274c538f647d92387b00c7&country=in",
      "results":"[{'id': 'google-news-in', 'name': 'Google News (India)', 'description': 'Comprehensive, up-to-date India news coverage, aggregated from sources all over the world by Google News.', 'url': 'https://news.google.com', 'category': 'general', 'language': 'en', 'country': 'in'}, {'id': 'the-hindu', 'name': 'The Hindu', 'description': \"The Hindu. latest news, analysis, comment, in-depth coverage of politics, business, sport, environment, cinema and arts from India's national newspaper.\", 'url': 'http://www.thehindu.com', 'category': 'general', 'language': 'en', 'country': 'in'}, {'id': 'the-times-of-india', 'name': 'The Times of India', 'description': 'Times of India brings the Latest News and Top Breaking headlines on Politics and Current Affairs in India and around the World, Sports, Business, Bollywood News and Entertainment, Science, Technology, Health and Fitness news, Cricket and opinions from leading columnists.', 'url': 'http://timesofindia.indiatimes.com', 'category': 'general', 'language': 'en', 'country': 'in'}]"
   },
   "typeName":"cortex/Any"
}
```

### Prerequisites
* Acquire an API key from News API for News Articles.

## Product attribution
This service uses the News API for datasets and querying requests. 

## Skill development
This skill utilizes the Cortex function service to execute custom code.
The function should be developed and tested before the skill is published to Cortex.
  
Wrapper scripts are provided to assist in developing and deploying your skill.
* `build-function.sh` packages the function in build/function.zip
* `deploy-function.sh` builds and deploys the function via Cortex's function apis
* `test-function.sh` invokes the deployed function via Cortex's function api
* `deploy-skill.sh` deploys the skill definition to Cortex's skill catalog

For more information: https://docs.cortex.insights.ai
