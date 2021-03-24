from git import Repo, RemoteProgress
import os.path
import os


def git_clone(url, nomeRepo):
    path = os.getcwd() + '/repositorios/' + nomeRepo
    Repo.clone_from(url, path)
    return path