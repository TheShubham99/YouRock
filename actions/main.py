import sys
import json

parsed_json=json.loads(sys.argv[1])

image_url=str(parsed_json['user']['avatarUrl'])
email=str(parsed_json['user']['email'])
username=str(parsed_json['user']['login'])
print(sys.argv[2])
print(image_url)
print(email)
print(username)