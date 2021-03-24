import requests

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
    'Authorization': 'Bearer 9ec6a7dcbe5daab741c35c0e7b375ffefcf04681'
}

query = """
query LabTwo {
  search(query: "language:java,stars:>100", type: REPOSITORY, first: 10 {endCursorCode}) {
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