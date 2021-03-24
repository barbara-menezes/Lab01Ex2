import labTwo
import cloneGit

def main():
    repositories = labTwo.get_repos()
    z = []
    for repo in repositories:
        path = cloneGit.git_clone(repo['url'], repo)
        metrics = calculaMetrics.calculaMetrica(path)
        z.append(repo | metrics)  
    arquivo = pd.DataFrame(z)
    arquivo.to_csv('resultado.csv', index=False)

main()