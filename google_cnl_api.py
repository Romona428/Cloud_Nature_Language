#TIR102_GROUP2_Projct

import requests
import json

api_key = "AIzaSyAq3DHdffxj"



# 定義請求的 URL 和 API 金鑰
url = f"https://language.googleapis.com/v1/documents:analyzeEntities?key={api_key}"

# 定義請求的標頭和數據
headers = {
    "Content-Type": "application/json"
}

data = {
    "document": {
        "type": "PLAIN_TEXT",
        "content": "Milky Way Over TunisiaWhat makes this storm cloud so colorful? First, the cloud itself is composed of millions of tiny droplets of water and ice. Its bottom is almost completely flat -- but this isn't unusual. Bottom flatness in clouds is generally caused by air temperature dropping as you go up, and that above a specific height, water-saturated air condenses out water droplets. The shape of the cloud middle is caused by a water-droplet-laden column of air being blown upward. Most unusual, though, are the orange and yellow colors. Both colors are caused by the cloud's water drops reflecting sunlight. The orange color in the cloud's middle and bottom sections are reflections of a nearly red sunset. In contrast, the yellow color of the cloud's top results from reflection of light from a not-yet-setting Sun, where some -- but less -- blue light is being scattered away. Appearing to float above the plains in Texas, the featured impressive image of a dynamic cumulonimbus cloud was captured in 2021 while investigating a tornado.

"
    }
}

# 發送 POST 請求
response = requests.post(url, headers=headers, json=data)

# 確保請求成功
response.raise_for_status()

# 將響應內容存儲到變數
response_data = response.json()

# 打印響應內容以檢查
print(json.dumps(response_data, indent=2))

# 如果需要使用響應內容，可以在這裡進行處理
entities = response_data.get("entities", [])
for entity in entities:
    print(f'Entity: {entity["name"]}')
    print(f'Type: {entity["type"]}')
    print(f'Salience: {entity["salience"]}')
    print(f'Metadata:')
    for metadata_name, metadata_value in entity.get("metadata", {}).items():
        print(f'- {metadata_name}: {metadata_value}')
    print()
