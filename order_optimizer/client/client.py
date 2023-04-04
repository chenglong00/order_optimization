import requests

# Define the API endpoint URL
url = 'http://127.0.0.1:8080/spaceship/optimize'

# Define the list of JSON data to send in the request body
data = [
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
]

# Make a POST request to the API endpoint with the data
response = requests.post(url, json=data)
print(response.json())

url = 'http://127.0.0.1:8080/test'
response = requests.post(url)
print(response.json())

# # Check the status code of the response
# if response.status_code == 200:
#     # Print the response body if the request was successful
#     print(response.json())
# else:
#     # Print an error message if the request failed
#     print('Error:', response)
#     print('Error:', response.status_code)
