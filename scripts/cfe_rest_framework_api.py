import json
import requests
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = os.path.join(os.getcwd(),"hot.jpg")

headers = {
    "Content-Type": "application/json"
}

data = {
    "username":'arun',
    "password":'arun',
}
r = requests.post(AUTH_ENDPOINT,data =json.dumps(data) ,headers=headers)
token = r.json()['token']
# print(token)


refresh_data = {
    'token': token
}

new_response = requests.post(REFRESH_ENDPOINT,data = json.dumps(refresh_data),headers = headers)
new_token = new_response.json()#['token']
print(new_token)




# get_data = json.dumps({"id":1234})
# post_data = json.dumps({"content":"Everything is planning"})


# def do_img(method ='get',data = {}, is_json=True, img_path =None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(img_path,'rb') as image:
#             file_data = {
#                 'image' : image
#             }
#             r = requests.request(method,ENDPOINT, data =data ,files = file_data, headers=headers)
#     else:
#         r = requests.request(method,ENDPOINT, data =data ,headers=headers)
#     print (r.text)
#     print (r.status_code)
#     return r

# # do_img(method ='post', data = {'user':1,"content":""}, is_json=False,img_path=image_path)


# do_img(method ='put', data = {'id':7,'user':1,"content":"fuck yeah"}, is_json=False,img_path=image_path)

# def do(method ='get',data = {}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method,ENDPOINT, data =data ,headers=headers)
#     print (r.text)
#     print (r.status_code)
#     return r

# # do(method = 'delete' , data={'id':10})