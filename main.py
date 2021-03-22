import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_url(self, file_name):
        """Метод получает URL для загрузки файла"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Accept': 'application/json', 'Authorization': self.token}
        params = {'path': file_name, 'overwrite': 'true'}
        resp = requests.get(url, params=params, headers=headers).json()
        url_upload = resp['href']

        return url_upload

    def upload(self, file_path, file_name):
        """Метод загружает файл file_path на яндекс диск"""
        url_upload = self.get_url(file_name)
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': self.token}
        resp = requests.put(url_upload, data=open(file_path, 'rb'), headers=headers)
        resp.raise_for_status()
        if resp.status_code == 201:
            print('File upload.')


if __name__ == '__main__':
    uploader = YaUploader('TOKEN')
    uploader.upload('test_file.txt', 'test_file.txt')
