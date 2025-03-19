import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)

posts = response.json()
for post in posts[:3]:
    print(f"ID: {post['id']}, Titulo: {post['title']}")