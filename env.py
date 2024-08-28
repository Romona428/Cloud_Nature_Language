import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\T14 Gen 3\\Downloads\\my-project-tir102-753ec9549127.json'

# 確認環境變數是否正確
print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))

# 創建 Google Translate 客戶端
translate_client = translate.Client()