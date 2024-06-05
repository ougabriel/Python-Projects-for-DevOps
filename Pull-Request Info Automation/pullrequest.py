import requests

response = requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls')

user_details = response.json()
if response.status_code == 200:

    for i in range(len(user_details)):

        print(user_details[i]['user']['login'],user_details[i]['user']['id'])

else:
         print(f'Request failed with status code:{response.status_code}')