import requests
 
def send_msg(id, text):
    token = "5526036773:AAE9uX6P6fZQpN8rqBsjpgqQeuVhiJ3ob-g"
    chat_id = id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    return results