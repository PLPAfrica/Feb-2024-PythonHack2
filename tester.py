import requests

# Define the URL you want to send the request to
url = "https://api.weatherapi.com/v1/current.json?key=494b6a42823d49b8abe191348242204&q=eldoret"

# Send a GET request to the URL
response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    print("Success!")
    print("Response content:")
    print(response.text)  # Print the response content
else:
    print("Failed to retrieve data from the URL. Status code:", response.status_code)
