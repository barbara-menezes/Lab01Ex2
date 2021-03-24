from git import Repo, RemoteProgress
from csv import writer
import calculaMetrics
import datetime
import os.path
import os


def git_clone(url, nomeRepo):
    path = os.getcwd() + '/repositorios/' + nomeRepo
    Repo.clone_from(url, path)
    return path