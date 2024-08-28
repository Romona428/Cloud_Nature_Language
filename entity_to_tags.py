#pip install google-cloud-translate
import os
import pandas as pd
from google_cnl_api import google_cnl_api
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\T14 Gen 3\\Downloads\\my-project-tir102-753ec9549127.json'

df = pd.read_json('apod_data_1995-06-16_1997-12-31.json')   

# 儲存每次迴圈中創建的 DataFrame 的列表
dataframes = []

# for i in range(1, len(df)):
for i in range(0, 10):
    content_string = df.iloc[i]['explanation']
    fig_date = df.iloc[i]['date']
    print("-----",content_string,"-----")
    tags_list = google_cnl_api(content_string)

    # 初始化翻譯客戶端
    translate_client = translate.Client()
    # 翻譯結果列表
    translated_array = []
    # 將英文翻譯成中文
    for text in tags_list:
        result = translate_client.translate(text, target_language='zh-TW')
        print(result)
        translated_array.append(result['translatedText'])


    print("---------------",i,"------------------")
    print(len(tags_list))
    print(len(translated_array))


    df_tags=pd.DataFrame({
        'tags_en' : tags_list,
        'tags_zhTW' : translated_array 
    })

    # 在 DataFrame 最前面插入一個 date 欄位，值為 fig_date
    df_tags.insert(0, 'date', fig_date)
    # print(df_tags)
    dataframes.append(df_tags)

# 合併所有 DataFrame
df_combined = pd.concat(dataframes, ignore_index=True)

print(df_combined)