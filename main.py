import labTwo
import cloneGit
import deleteGit

def main():
    repositories = labTwo.get_repos()
    z = []
    for repo in repositories:
        path = cloneGit.git_clone(repo['url'], repo)
        metrics = calculaMetrics.calculaMetrica(path)
        z.append(repo | metrics)  
        deleteGit.clean_all_repositories(path)
    arquivo = pd.DataFrame(z)
    arquivo.to_csv('resultado.csv', index=False)

main()