import requests
url = "https://aliexpress.ru/item/1005005762010800.html?spm=a2g2w.home.10009201.38.46d95586QL9ZyS&mixer_rcmd_bucket_id=aerabtestalgoRecommendAbV2_testVectorSearchW2vOrdersHome&ru_algo_pv_id=48a555-bbf0ce-061b0e-9725ba-1728129600&scenario=aerA"

response = requests.get(url)

print(response.text)
