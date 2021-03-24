import pandas as pd
import subprocess
import os

def calculaMetrica(path):
    subprocess.call(['java', '-jar', './ck-0.6.4-SNAPSHOT-jar-with-dependencies.jar', path, 'true', '0', 'False'])
    ck_metrics = pd.read_csv("class.csv", usecols = ["cbo", "wmc", "dit", "loc"])
    median = ck_metrics.median()
    return mapRepo(median)

def mapRepo(metrics):
    return {
        "CBO": metrics['cbo'],
        "WMC": metrics['wmc'],
        "DIT": metrics['dit'],
        "LOC": metrics['loc'],
    }