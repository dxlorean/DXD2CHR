import requests
import time
import random


url = "https://liste.bdekraken.fr/api/place/tile/draw"
data = {"key": "value"}

headers = {
    'method': "POST",
    "authority": "liste.bdekraken.fr",
    "path":"/api/place/tile/draw",
    "Content-Type": "application/json",
  

    
}
#    { "session": "YmRkZmI4ZDItYWQ2Ni00MDQ2LWFhZWItNDA2M2FiZTliNjVm" },
cookies = [
    { "session":"OGJjNDBiNGMtZDM5Ny00NmRhLTgwMzItNmIxYTJmYjU5NjUw"},
    { "session": "OTcyM2E1MzgtYWNkZC00NmVjLTgxMGUtMDRhNGY5ODFiN2Vk" },
    { "session": "NDIwNDA1OTEtMmJkZS00NDhmLWI0MWEtYzBiNzg5NmM2NWEw" },
    { "session": "YmRkZmI4ZDItYWQ2Ni00MDQ2LWFhZWItNDA2M2FiZTliNjVm" },
    { "session": "OTEwZTQxYjYtNTA1Zi00OWUwLWI4YjEtY2JhZmIxZWIxZjE3"}
]
#response = requests.post(url, json={"x": 167,"y":23,"color":"#be0039"},cookies=cookies)
#print(response.text)
# Send a POST request with JSON data

coordinates_colors = []

#start x:155 6   251  55
'''x0 = 202   B2 coords
y0 = 31
step = 2'''

x0 = 65
y0 = 31
step = 2

# 233 139
def newset(x, y):
    return {"x": x, "y":y, "color": "#ff4500"}


xv = 1
'''for i in range(1000):
        for v in range(step):
            y0+=xv
            coordinates_colors.append(newset(x0,y0))
        step+=1
        for vv in range(step):
            x0-=xv
            coordinates_colors.append(newset(x0,y0))
        step+=1
        for v in range(step):
            y0-=xv
            coordinates_colors.append(newset(x0,y0))
        step+=1
        for vv in range(step):
            x0+=xv
            coordinates_colors.append(newset(x0,y0))
        step+=1'''
        
n = 0
for i in range(10000):
    coordinates_colors.append(newset(random.randint(65,82), random.randint(160,176)))
    



time.sleep(3)




# Loop over the list of coordinates and colors
for item in coordinates_colors:
    # Send a POST request with JSON data
    if n % 4 == 0:
        response = requests.post(url, json=item, cookies=cookies[0])
    elif n % 4 ==1:
        response = requests.post(url, json=item, cookies=cookies[1])
    elif n % 4 == 2:
        response = requests.post(url, json=item, cookies=cookies[2])
    elif n % 4 == 3:
        response = requests.post(url, json=item, cookies=cookies[3])
    elif n % 4 == 4:
        response = requests.post(url, json=item, cookies=cookies[4])
  

    # Print the response content
    print(response.content)
    # Wait for a while before the next request
    time.sleep(2)  # Adjust the sleep time as needed
    n +=1
            
