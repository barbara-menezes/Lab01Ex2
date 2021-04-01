import labTwo
import cloneGit
import deleteGit
import calculaMetrics
import pandas as pd

def main():
    repositories = labTwo.get_repos()
    z = []
    for repo in repositories:
        try:
            path = cloneGit.git_clone(repo)
            metrics = calculaMetrics.calculaMetrica(path)
            z.append(repo | metrics)  
            deleteGit.clean_all_repositories(path)
        except Exception as e:
            print(e)
    arquivo = pd.DataFrame(z)
    arquivo.to_csv('resultado.csv', index=False)

main()