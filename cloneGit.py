from git import Repo, RemoteProgress
import os.path
import os


def git_clone(repo):
    path = os.getcwd() + '/repositorios/' + repo['name']
    Repo.clone_from(repo['url'], path)
    return path