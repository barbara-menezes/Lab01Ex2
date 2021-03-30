from git import Repo, RemoteProgress
from csv import writer
from datetime import date, datetime
import requests
import time
import json
import os

def executar_query_github(query):
    request = requests.post('https://api.github.com/graphql', json = {'query': query}, headers = headers)
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 502:
      return executar_query_github(query)
    else:
        raise Exception("A query falhou: {}. {}".format(request.status_code, query))

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer d18243107692cb1101066f06ec48a628e7776dd3'
}

query = """
query LabTwo {
  search(query: "language:java,stars:>100,is:public", type: REPOSITORY, first: 10 {endCursorCode}) {
    pageInfo {
      hasNextPage
      endCursor
    }
    nodes {
      ... on Repository {
        name
        stargazerCount
        url
        createdAt
        releases {
          totalCount
        }
        primaryLanguage {
          name: name
        }
      }
    }
  }
}
"""

def formatar_datas(response):
    nodes = response['data']['search']['nodes']
    for i, repositorio in enumerate(nodes):
        dataCriacaoRepo = datetime.strptime(nodes[i]['createdAt'].split('T')[0], '%Y-%m-%d').date()
        nodes[i]['createdAt'] = int(((date.today() - dataCriacaoRepo).days)/365)

def get_repos():
  todos_resultados = []
  end_cursor = ''
  for i in range(100):
    cursor, resultados = formata_query(end_cursor)
    end_cursor = cursor
    todos_resultados += resultados
  return todos_resultados

def formata_query(end_cursor):
  queryVar = query.replace("{endCursorCode}", ', after: "Y3Vyc29yOjQ5MA=="') if end_cursor == "" else query.replace("{endCursorCode}", ', after: "%s"' % end_cursor)
  response = executar_query_github(queryVar)
  formatar_datas(response)
  return response["data"]["search"]["pageInfo"]["endCursor"], response["data"]["search"]["nodes"]