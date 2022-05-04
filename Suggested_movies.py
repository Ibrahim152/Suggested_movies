import requests
import json


class movie:

    def __init__(self, name):
        self.__name = name
        self.__api = '434647-class-WNCOKJCW'
        self.__tastediveApi = requests.get('https://tastedive.com/api/similar',
                                           params={'q': self.__name, 'type': 'movies', 'k': self.__api})
        self.__tastediveApi = self.__tastediveApi.text
        self.__tastediveApi = json.loads(self.__tastediveApi)
        self.__lst_of_names = [movie['Name']
                               for movie in self.__tastediveApi['Similar']['Results']]

        self.__omdbapi = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=671045b9',
                                      params={'t': self.__name, 'type': 'movie'})
        self.__omdbapi = json.loads(self.__omdbapi.text)

    def related(self):
        return self.__lst_of_names

    def rateshow(self):
        print('name : {}'.format(self.__omdbapi['Title']))
        rates = self.__omdbapi['Ratings']
        print(rates)
        for rate in rates:
            print(f"{rate['Source']} RATE : {rate['Value']}")

    def rate(self):
        return int(self.__omdbapi['Ratings'][1]['Value'][:-1])


while True:

    name = input('Enter a movie name please:\n')
    if name == '':
        exit()
    name = movie(name)
    rel = name.related()

    x = sorted(rel, key=lambda x: movie(x).rate(), reverse=True)
    for sol in x:
        print(f'{sol} rate: {movie(sol).rate()}')
