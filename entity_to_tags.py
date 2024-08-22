#pip install google-cloud-translate
import pandas as pd
from google_cnl_api import google_cnl_api
from google.cloud import translate_v2 as translate

df = pd.read_json('apod_data_2008-01-01_2008-12-31.json')   

# for i in range(1, len(df)):
for i in range(1, 3):

    content_string = df.iloc[i]['explanation']
    print("-----",content_string,"-----")
    tags_list = google_cnl_api(content_string)

# 初始化翻譯客戶端
translate_client = translate.Client()
# 翻譯結果列表
translated_array = []
# # 將每個英文短語翻譯成中文
# for text in tags_list:
#     result = translate_client.translate(text, target_language='zh')
#     translated_array.append(result['translatedText'])