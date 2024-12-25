import boto3
from botocore.exceptions import NoCredentialsError
from io import BytesIO

# Замените следующие параметры на ваши данные:
endpoint_url = 'https://storage.yandexcloud.net'  # URL Yandex Object Storage
bucket_name = 'storage-bucket-isusisusov'  # Имя вашего бакета
file_name = 'penguins_sample'  # Имя файла, который вы хотите загрузить
image_path = "C:/Users/Isusi/OneDrive/Документы/penguins_sample.jpg"  # Путь к файлу на вашем локальном компьютере

# Создаем сессию с использованием S3 API
s3 = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id='YCAJEoVjFmH3QR5Vh0sVqB12d',  # Ваш Access Key из IAM пользователя
    aws_secret_access_key='YCNDi_JXs5nh9DiPqrtFeKfUXll5LwwvxgITVW51',  # Ваш Secret Key из IAM пользователя
)

# Загрузка файла в бакет
def upload_to_object_storage(bucket_name, file_name, image_path):
    try:
        with open(image_path, 'rb') as file:
            file_data = file.read()

        # Загружаем файл в бакет
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=BytesIO(file_data),
        )

        print(f'File {file_name} uploaded successfully to {bucket_name}')

    except NoCredentialsError:
        print('Credentials not available. Please check your keys.')
    except Exception as e:
        print(f'Error uploading to Yandex Object Storage: {e}')

# Вызов функции для загрузки файла
upload_to_object_storage(bucket_name, file_name, image_path)