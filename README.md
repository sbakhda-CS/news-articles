---
title: "News Insights"
date: "2018-02-02"
toc: true
menu:
  main:
    parent: "ml-skills"
    identifier: "news-insights"
    #weight: 4420
---

Discovery News is included with Discovery.
Watson Discovery News is an indexed dataset that is pre-enriched with the following cognitive insights:
Keyword Extraction, Entity Extraction, Semantic Role Extraction, Sentiment Analysis, Relation Extraction, and Category Classification.

Watson Discovery News is updated continuously with new articles.
Discovery News English is updated with approximately 300,000 new articles daily.
Discovery News Spanish is updated with approximately 60,000 new articles daily;
Discovery News Korean with 10,000 new articles daily.
The news sources vary by language, so the query results for each collection will not be identical.

## Use cases

- News alerting - Create news alerts by taking advantage of the support for entities, keywords, categories, and sentiment analysis to watch for both news and how it is perceived.
-  Event detection - The subject/action/object semantic role extraction checks for terms/actions such as "acquisition", "election results", or "IPO".
-  Trending topics in the news - Identify popular topics and monitor increases and decreases in how frequently they (or related topics) are mentioned.

## Inputs
skill takes text as input.A sample example for the input is shown below:

```
  "input_query":"Apple inc","num_of_results":"1",
  "display_crawl_date":1, "display_publication_date":1, "display_url":1, "display_host":1,
  "display_text":1, "display_country":1,
  "display_enriched_title":1, "display_enriched_text":1,
  "display_entities":1, "display_sentiment":1, "display_semantic_roles":1, "display_concepts":1,
  "display_categories":1, "display_relations":1, "display_keywords":1
```

## Outputs

An example output for the News Insights API is shown below:

```
{
	"matching_results": 17032929,
	"passages": [],
	"results": [
		{
			"id": "Nu2IUIxHuqYxC-RX8ZLUdtnCP2rWsKPTaOT-Sd5OVwg5CT5k2muxYzqEFvBmkyH3",
			"result_metadata": {
				"score": 1
			},
			"enriched_title": {
				"entities": [],
				"sentiment": {
					"document": {
						"score": 0,
						"label": "neutral"
					}
				},
				"semantic_roles": [],
				"concepts": [
					{
						"text": "Marketing",
						"relevance": 0.854117,
						"dbpedia_resource": "http://dbpedia.org/resource/Marketing"
					}
				],
				"categories": [
					{
						"score": 0.768898,
						"label": "/careers/career advice"
					},
					{
						"score": 0.636583,
						"label": "/business and industrial/advertising and marketing/marketing"
					},
					{
						"score": 0.0101212,
						"label": "/law, govt and politics/legal issues"
					}
				],
				"relations": [],
				"keywords": [
					{
						"text": "Career Advice",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.91324
					},
					{
						"text": "need",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.625478
					},
					{
						"text": "marketing",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.623263
					}
				]
			},
			"crawl_date": "2018-03-04T06:09:19Z",
			"url": "https://www.reddit.com/r/marketing/comments/81uvw1/in_need_of_some_career_advice/",
			"host": "reddit.com",
			"text": "Hi all, Brief Background: As mentioned above, I would love to hear some input on what steps I can take to get the most out of my marketing degree. I am currently a Senior marketing student with a communication minor and graduate this spring. I am 22 and have worked since I was 16. Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have. I am certified in AdWord fundamentals and am working on Google Analytics and understand getting certifications can be helpful. My biggest issue right now is wanting to apply for full time positions but not graduating until this Spring so I do not know if I will even be considered for the position. Some",
			"main_image_url": "https://www.redditstatic.com/icon.png",
			"country": "US",
			"source_type": "mainstream",
			"language": "en",
			"publication_date": "2018-03-04T00:00:00Z",
			"enriched_text": {
				"entities": [
					{
						"count": 1,
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"text": "director",
						"relevance": 0.52504,
						"type": "JobTitle"
					}
				],
				"sentiment": {
					"document": {
						"score": 0.448422,
						"label": "positive"
					}
				},
				"semantic_roles": [
					{
						"subject": {
							"text": "I"
						},
						"sentence": " As mentioned above, I would love to hear some input on what steps I can take to get the most out of my marketing degree.",
						"object": {
							"text": "to hear some input on what steps I can take to get the most out of my marketing degree",
							"keywords": [
								{
									"text": "marketing degree"
								},
								{
									"text": "input"
								},
								{
									"text": "steps"
								}
							]
						},
						"action": {
							"verb": {
								"text": "love",
								"tense": "future"
							},
							"text": "love",
							"normalized": "love"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " As mentioned above, I would love to hear some input on what steps I can take to get the most out of my marketing degree.",
						"object": {
							"text": "some input on what steps I can take to get the most out of my marketing degree",
							"keywords": [
								{
									"text": "input"
								},
								{
									"text": "steps"
								},
								{
									"text": "marketing degree"
								}
							]
						},
						"action": {
							"verb": {
								"text": "hear",
								"tense": "future"
							},
							"text": "would love to hear",
							"normalized": "would love to hear"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am currently a Senior marketing student with a communication minor and graduate this spring.",
						"object": {
							"text": "a Senior marketing student with a communication minor and graduate this spring",
							"keywords": [
								{
									"text": "Senior marketing student"
								},
								{
									"text": "communication"
								},
								{
									"text": "spring"
								}
							],
							"entities": []
						},
						"action": {
							"verb": {
								"text": "be",
								"tense": "present"
							},
							"text": "am",
							"normalized": "be"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am 22 and have worked since I was 16.",
						"object": {
							"text": "22"
						},
						"action": {
							"verb": {
								"text": "be",
								"tense": "present"
							},
							"text": "am",
							"normalized": "be"
						}
					},
					{
						"subject": {
							"text": "worked"
						},
						"sentence": " I am 22 and have worked since I was 16.",
						"action": {
							"verb": {
								"text": "have",
								"tense": "present"
							},
							"text": "have",
							"normalized": "have"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am 22 and have worked since I was 16.",
						"action": {
							"verb": {
								"text": "work",
								"tense": "past"
							},
							"text": "have worked",
							"normalized": "have work"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am 22 and have worked since I was 16.",
						"object": {
							"text": "16"
						},
						"action": {
							"verb": {
								"text": "be",
								"tense": "past"
							},
							"text": "was",
							"normalized": "be"
						}
					},
					{
						"subject": {
							"text": "Most of the jobs",
							"keywords": [
								{
									"text": "jobs"
								}
							]
						},
						"sentence": " Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"object": {
							"text": "to be in the food industry",
							"keywords": [
								{
									"text": "food industry"
								}
							],
							"entities": []
						},
						"action": {
							"verb": {
								"text": "tend",
								"tense": "past"
							},
							"text": "tended",
							"normalized": "tend"
						}
					},
					{
						"subject": {
							"text": "Most of the jobs",
							"keywords": [
								{
									"text": "jobs"
								}
							]
						},
						"sentence": " Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"action": {
							"verb": {
								"text": "be",
								"tense": "future"
							},
							"text": "tended to be",
							"normalized": "tend to be"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"object": {
							"text": "able to be promoted to a camp director role",
							"keywords": [
								{
									"text": "camp director role"
								}
							],
							"entities": [
								{
									"type": "JobTitle",
									"text": "director"
								}
							]
						},
						"action": {
							"verb": {
								"text": "be",
								"tense": "past"
							},
							"text": "was",
							"normalized": "be"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"object": {
							"text": "promoted to a camp director role",
							"keywords": [
								{
									"text": "camp director role"
								}
							],
							"entities": [
								{
									"type": "JobTitle",
									"text": "director"
								}
							]
						},
						"action": {
							"verb": {
								"text": "be",
								"tense": "past"
							},
							"text": "be",
							"normalized": "be"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"object": {
							"text": "to a camp director role",
							"keywords": [
								{
									"text": "camp director role"
								}
							],
							"entities": [
								{
									"type": "JobTitle",
									"text": "director"
								}
							]
						},
						"action": {
							"verb": {
								"text": "promote",
								"tense": "past"
							},
							"text": "to be promoted",
							"normalized": "to be promote"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am certified in AdWord fundamentals and am working on Google Analytics and understand getting certifications can be helpful.",
						"object": {
							"text": "certified in AdWord fundamentals and am working on Google Analytics and understand getting certifications can be helpful",
							"keywords": [
								{
									"text": "AdWord fundamentals"
								},
								{
									"text": "Google Analytics"
								},
								{
									"text": "certifications"
								}
							],
							"entities": []
						},
						"action": {
							"verb": {
								"text": "be",
								"tense": "present"
							},
							"text": "am",
							"normalized": "be"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am certified in AdWord fundamentals and am working on Google Analytics and understand getting certifications can be helpful.",
						"object": {
							"text": "in AdWord fundamentals",
							"keywords": [
								{
									"text": "AdWord fundamentals"
								}
							]
						},
						"action": {
							"verb": {
								"text": "certify",
								"tense": "past"
							},
							"text": "am certified",
							"normalized": "be certify"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am certified in AdWord fundamentals and am working on Google Analytics and understand getting certifications can be helpful.",
						"action": {
							"verb": {
								"text": "work",
								"tense": "present"
							},
							"text": "am working",
							"normalized": "be work"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " I am certified in AdWord fundamentals and am working on Google Analytics and understand getting certifications can be helpful.",
						"object": {
							"text": "getting certifications can be helpful",
							"keywords": [
								{
									"text": "certifications"
								}
							]
						},
						"action": {
							"verb": {
								"text": "understand",
								"tense": "present"
							},
							"text": "understand",
							"normalized": "understand"
						}
					},
					{
						"subject": {
							"text": "My biggest issue right now",
							"keywords": [
								{
									"text": "biggest issue"
								}
							]
						},
						"sentence": " My biggest issue right now is wanting to apply for full time positions but not graduating until this Spring so I do not know if I will even be considered for the position.",
						"object": {
							"text": "wanting to apply for full time positions",
							"keywords": [
								{
									"text": "time positions"
								}
							]
						},
						"action": {
							"verb": {
								"text": "be",
								"tense": "present"
							},
							"text": "is",
							"normalized": "be"
						}
					},
					{
						"subject": {
							"text": "My biggest issue",
							"keywords": [
								{
									"text": "biggest issue"
								}
							]
						},
						"sentence": " My biggest issue right now is wanting to apply for full time positions but not graduating until this Spring so I do not know if I will even be considered for the position.",
						"object": {
							"text": "to apply for full time positions but not graduating until this Spring so I do not know if I will even be considered for the position",
							"keywords": [
								{
									"text": "time positions"
								},
								{
									"text": "Spring"
								}
							]
						},
						"action": {
							"verb": {
								"text": "want",
								"tense": "present"
							},
							"text": "wanting",
							"normalized": "want"
						}
					},
					{
						"subject": {
							"text": "My biggest issue",
							"keywords": [
								{
									"text": "biggest issue"
								}
							]
						},
						"sentence": " My biggest issue right now is wanting to apply for full time positions but not graduating until this Spring so I do not know if I will even be considered for the position.",
						"object": {
							"text": "for full time positions",
							"keywords": [
								{
									"text": "time positions"
								}
							]
						},
						"action": {
							"verb": {
								"text": "apply",
								"tense": "future"
							},
							"text": "is wanting to apply",
							"normalized": "be want to apply"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " My biggest issue right now is wanting to apply for full time positions but not graduating until this Spring so I do not know if I will even be considered for the position.",
						"object": {
							"text": "if I will even be considered for the position",
							"keywords": [
								{
									"text": "position"
								}
							]
						},
						"action": {
							"verb": {
								"text": "know",
								"tense": "present",
								"negated": true
							},
							"text": "know",
							"normalized": "know"
						}
					},
					{
						"subject": {
							"text": "you"
						},
						"sentence": " What are some of the best qualifications you think a marketing student should have?",
						"object": {
							"text": "a marketing student should have",
							"keywords": [
								{
									"text": "marketing student"
								}
							]
						},
						"action": {
							"verb": {
								"text": "think",
								"tense": "present"
							},
							"text": "think",
							"normalized": "think"
						}
					},
					{
						"subject": {
							"text": "land your first job",
							"keywords": [
								{
									"text": "land"
								},
								{
									"text": "job"
								}
							]
						},
						"sentence": " How did you land your first job?",
						"object": {
							"text": "you"
						},
						"action": {
							"verb": {
								"text": "do",
								"tense": "past"
							},
							"text": "did",
							"normalized": "do"
						}
					},
					{
						"subject": {
							"text": "you"
						},
						"sentence": " How did you land your first job?",
						"object": {
							"text": "your first job",
							"keywords": [
								{
									"text": "job"
								}
							]
						},
						"action": {
							"verb": {
								"text": "land",
								"tense": "past"
							},
							"text": "land",
							"normalized": "land"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " Will I be able to land a full time job even though I graduate in June?",
						"object": {
							"text": "a full time job",
							"keywords": [
								{
									"text": "time job"
								}
							]
						},
						"action": {
							"verb": {
								"text": "land",
								"tense": "future"
							},
							"text": "to land",
							"normalized": "to land"
						}
					},
					{
						"subject": {
							"text": "I"
						},
						"sentence": " Will I be able to land a full time job even though I graduate in June?",
						"action": {
							"verb": {
								"text": "graduate",
								"tense": "present"
							},
							"text": "graduate",
							"normalized": "graduate"
						}
					}
				],
				"concepts": [
					{
						"text": "Full-time",
						"relevance": 0.949344,
						"dbpedia_resource": "http://dbpedia.org/resource/Full-time"
					},
					{
						"text": "Google",
						"relevance": 0.907856,
						"dbpedia_resource": "http://dbpedia.org/resource/Google"
					},
					{
						"text": "Google services",
						"relevance": 0.62752,
						"dbpedia_resource": "http://dbpedia.org/resource/Google_services"
					},
					{
						"text": "Minor league",
						"relevance": 0.614073,
						"dbpedia_resource": "http://dbpedia.org/resource/Minor_league"
					},
					{
						"text": "Food",
						"relevance": 0.612468,
						"dbpedia_resource": "http://dbpedia.org/resource/Food"
					},
					{
						"text": "Web analytics",
						"relevance": 0.597546,
						"dbpedia_resource": "http://dbpedia.org/resource/Web_analytics"
					}
				],
				"categories": [
					{
						"score": 0.658104,
						"label": "/business and industrial/advertising and marketing/marketing"
					},
					{
						"score": 0.419175,
						"label": "/finance/personal finance/insurance/health insurance"
					},
					{
						"score": 0.40555,
						"label": "/technology and computing/computer certification"
					}
				],
				"relations": [
					{
						"type": "hasAttribute",
						"sentence": "I am 22 and have worked since I was 16.",
						"score": 0.973748,
						"arguments": [
							{
								"text": "I",
								"location": [
									274,
									275
								],
								"entities": [
									{
										"type": "Person",
										"text": "your"
									}
								]
							},
							{
								"text": "16",
								"location": [
									280,
									282
								],
								"entities": [
									{
										"type": "Age",
										"text": "16"
									}
								]
							}
						]
					},
					{
						"type": "affectedBy",
						"sentence": "Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"score": 0.567517,
						"arguments": [
							{
								"text": "I",
								"location": [
									378,
									379
								],
								"entities": [
									{
										"type": "Person",
										"text": "your"
									}
								]
							},
							{
								"text": "promoted",
								"location": [
									395,
									403
								],
								"entities": [
									{
										"type": "EventPersonnel",
										"text": "promoted"
									}
								]
							}
						]
					},
					{
						"type": "locatedAt",
						"sentence": "Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"score": 0.649462,
						"arguments": [
							{
								"text": "I",
								"location": [
									378,
									379
								],
								"entities": [
									{
										"type": "Person",
										"text": "your"
									}
								]
							},
							{
								"text": "camp",
								"location": [
									409,
									413
								],
								"entities": [
									{
										"type": "Facility",
										"text": "camp"
									}
								]
							}
						]
					},
					{
						"type": "agentOf",
						"sentence": "Most of the jobs tended to be in the food industry but I did have one job with the YMCA where I was able to be promoted to a camp director role and that is the closest link to professional experience I have.",
						"score": 0.404817,
						"arguments": [
							{
								"text": "director",
								"location": [
									414,
									422
								],
								"entities": [
									{
										"type": "Person",
										"text": "director"
									}
								]
							},
							{
								"text": "promoted",
								"location": [
									395,
									403
								],
								"entities": [
									{
										"type": "EventPersonnel",
										"text": "promoted"
									}
								]
							}
						]
					},
					{
						"type": "agentOf",
						"sentence": "Some of my Questions are:  What are some of the best qualifications you think a marketing student should have?",
						"score": 0.994475,
						"arguments": [
							{
								"text": "my",
								"location": [
									800,
									802
								],
								"entities": [
									{
										"type": "Person",
										"text": "your"
									}
								]
							},
							{
								"text": "Questions",
								"location": [
									803,
									812
								],
								"entities": [
									{
										"type": "EventCommunication",
										"text": "Questions"
									}
								]
							}
						]
					}
				],
				"keywords": [
					{
						"text": "camp director role",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.915342
					},
					{
						"text": "Senior marketing student",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.893768
					},
					{
						"text": "AdWord fundamentals",
						"sentiment": {
							"score": 0.826715,
							"label": "positive"
						},
						"relevance": 0.734724
					},
					{
						"text": "Brief Background",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.730835
					},
					{
						"text": "closest link",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.68823
					},
					{
						"text": "Google Analytics",
						"sentiment": {
							"score": 0.826715,
							"label": "positive"
						},
						"relevance": 0.664929
					},
					{
						"text": "biggest issue",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.656433
					},
					{
						"text": "food industry",
						"sentiment": {
							"score": -0.502425,
							"label": "negative"
						},
						"relevance": 0.651662
					},
					{
						"text": "professional experience",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.645273
					},
					{
						"text": "marketing degree",
						"sentiment": {
							"score": 0.569029,
							"label": "positive"
						},
						"relevance": 0.638288
					},
					{
						"text": "best qualifications",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.628635
					},
					{
						"text": "time positions",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.615585
					},
					{
						"text": "time job",
						"sentiment": {
							"score": 0.600532,
							"label": "positive"
						},
						"relevance": 0.573823
					},
					{
						"text": "spring",
						"sentiment": {
							"score": -0.267563,
							"label": "negative"
						},
						"relevance": 0.358248
					},
					{
						"text": "Hi",
						"sentiment": {
							"score": 0.754777,
							"label": "positive"
						},
						"relevance": 0.330565
					},
					{
						"text": "input",
						"sentiment": {
							"score": 0.569029,
							"label": "positive"
						},
						"relevance": 0.298266
					},
					{
						"text": "certifications",
						"sentiment": {
							"score": 0.826715,
							"label": "positive"
						},
						"relevance": 0.297555
					},
					{
						"text": "YMCA",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.295509
					},
					{
						"text": "steps",
						"sentiment": {
							"score": 0.569029,
							"label": "positive"
						},
						"relevance": 0.294385
					},
					{
						"text": "paths",
						"sentiment": {
							"score": 0.612713,
							"label": "positive"
						},
						"relevance": 0.293082
					},
					{
						"text": "suggestions",
						"sentiment": {
							"score": 0.741537,
							"label": "positive"
						},
						"relevance": 0.287014
					},
					{
						"text": "communication",
						"sentiment": {
							"score": 0,
							"label": "neutral"
						},
						"relevance": 0.282362
					}
				]
			},
			"extracted_metadata": {
				"sha1": "907306c849af4fe197dded5b2cef6b14b0186bff",
				"filename": "1520143759809.zip-4d528b1ab359796ac44936b3f2f8c469.xml",
				"file_type": "json"
			},
			"title": "In need of some Career Advice : marketing"
		}
	]
}
```

## Adding News Insights to an agent
### Prerequisites
* Acquire an API key from IBM Watson for the News Insights API.

### Add the skill
1. Use **Add** > **Skill** to find and add the News Insights Skill.
1. Click the skill to select it, and set the following values in the **Properties** panel:
 
    * **Model**: Select **IBM Watson**.
    * **API Key**: Enter your API Key for the News Insights API.

### Add input and output
1. Add a service input.
1. Give the service a name that is unique inside this agent.
1. Select **text** as the **Input Type**.
1. Select **News Insights Response** as the **Output Type**.
1. Click **Add Service**.

### Wiring
1. Select the News Insights Skill.
2. Wire the skill to the input using the plus icon {{< icon "zmdi zmdi-plus icon-circle blue-bg" >}} next to the input service you just created.
3. Wire the skill to the output using the plus icon {{< icon "zmdi zmdi-plus icon-circle green-bg" >}} next to the output that matches the input name for the skill.

## Product attribution
This service leverages the News Insights API from IBM Watson Services.


## Skill development
This skill utilizes the Cortex function service to execute custom code.
The function should be developed and tested before the skill is published to Cortex.
  
Wrapper scripts are provided to assist in developing and deploying your skill.
* `build-function.sh` packages the function in build/function.zip
* `deploy-function.sh` builds and deploys the function via Cortex's function apis
* `test-function.sh` invokes the deployed function via Cortex's function api
* `deploy-skill.sh` deploys the skill definition to Cortex's skill catalog

For more information: https://docs.cortex.insights.ai