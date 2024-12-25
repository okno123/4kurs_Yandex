import json
import boto3
import requests
from io import BytesIO
import base64


# Получите ваш OAuth токен для доступа к Yandex Cloud
oauth_token = 'y0__wgBEOWrlNgHGMHdEyCfg8_rEVWub8T3zZ0h7bGmGrWgvycFiML0'

import base64
import json
import requests


# Параметры запроса
image_path = "C:/Users/Isusi/OneDrive/Документы/penguins_sample.jpg"  # Путь к вашему изображению
iam_token = 't1.9euelZrGm8fPi8zGl8rKkIuZyJaUyu3rnpWayI3Gl5SSnMaamZmVjJbHxo3l8_c7VlBE-e8iPQAP_t3z93sETkT57yI9AA_-zef1656VmpCLl4-VmcmbmJSTjouMzszO7_zF656VmpCLl4-VmcmbmJSTjouMzszO.NVElBZ8NcG6lS2anwxswS3ghY6VtnVh2CTL4074GI3O6DRklUMmBW4VYmneHqDf23DnG6V68u-iJnKcbfk4nBg'  # URL Yandex OCR API
folder_id = 'b1g50cc61thb5hg8t68t'

url = 'https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText'


# Функция для кодирования изображения в base64
def encode_image(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Отправка запроса с изображением


def send_request():
    # Кодируем изображение
    image_base64 = encode_image(image_path)

    # Формируем тело запроса
    data = {
        "mimeType": "JPEG",  # Тип MIME для JPEG-изображений
        "languageCodes": ["*"],  # Все доступные языки
        "content": image_base64  # Само изображение в формате base64
    }



    headers = {
        'Authorization': f'Bearer {iam_token}',  # Используем IAM-токен
        'Content-Type': 'application/json',
        'x-folder-id': folder_id,  # Указываем идентификатор папки в Яндекс.Облаке
    }

    # Отправка запроса с таймаутом
    response = requests.post(url=url, headers=headers, data=json.dumps(data))

    # Печать ответа от сервера
    print("Response status:", response.status_code)
    print("Response content:", response.content)

    # Обработка ответа

    if response.status_code == 200:
        print("Изображение обработано успешно.")
        result = response.json()
        # Извлекаем только полный текст из ответа
        full_text = result.get("result", {}).get("textAnnotation", {}).get("fullText", "")

        print("Результат текста:", full_text)
        return full_text
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.json())


# Запуск запроса
full_text = send_request()

#print(full_text)
full_text = full_text.replace("\n", " ")
print(full_text)


target_language = 'ru'
texts = full_text


body = {
    "targetLanguageCode": target_language,
    "texts": texts,
    "folderId": folder_id,
}

headers = {
        'Authorization': f'Bearer {iam_token}',  # Используем IAM-токен
        'Content-Type': 'application/json',
        'x-folder-id': folder_id,  # Указываем идентификатор папки в Яндекс.Облаке
    }

response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
    json = body,
    headers = headers
)

print(response.text)








