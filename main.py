import requests


def superheroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    headers = {'name': 'Hulk'}
    resp = requests.get(url=url, headers=headers)
    dict_superheroes = {}
    for dict_ in resp.json():
        for key in dict_:
            if dict_[key] == 'Hulk':
                Hulk_intelligence = dict_['powerstats']['intelligence']
                dict_superheroes['Hulk'] = Hulk_intelligence
            elif dict_[key] == 'Captain America':
                Captain_A_intelligence = dict_['powerstats']['intelligence']
                dict_superheroes['Captain America'] = Captain_A_intelligence
            elif dict_[key] == 'Thanos':
                Thanos_intelligence = dict_['powerstats']['intelligence']
                dict_superheroes['Thanos'] = Thanos_intelligence
    for items_ in dict_superheroes.items():
        count = 0
        the_smartest = None
        if items_[1] > count:
            count = items_[1]
            the_smartest = items_[0]
    print(f'Самый умный супергерой {the_smartest} его показатель intelligence {count}')


if __name__=='__main__':
    superheroes()


token = ''


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def headers_(self):
        return {'Content-Type': 'application/json', 'Accept': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def _upload_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.headers_()
        params = {'path': path_to_file, 'overwrite': 'true'}
        res = requests.get(upload_url, headers=headers, params=params)
        return res.json()

    def upload(self, path_to_file, file_name):

        href = self._upload_link(path_to_file=path_to_file).get('href','')
        res = requests.put(href, data=open(file_name, 'rb'))
        res.raise_for_status()
        if res.status_code == 201:
            print('Все хорошо')


if __name__ == '__main__':
    uploader = YaUploader(token=token)
    file_list = ['test.txt', 'test2.txt']
    for i in file_list:
        uploader.upload(i, i)

def list_of_questions():
    url1 = 'https://api.stackexchange.com/2.3/questions?todate=1660003200&order=desc&max=1660176000&sort=activity&tagged=python&site=stackoverflow'
    list_of_questions = []
    rec2 = requests.get(url1)
    rec3 = rec2.json()
    list_of_questions.append([i['title'] for i in rec3['items']])
    return list_of_questions

if __name__ == '__main__':
    print(list_of_questions())
















