import os
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
import pandas as pd

data = pd.read_csv('dac_sample.txt', sep="\t", header = None)
data.columns = ["Label", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", "I13",
                 "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13",
                "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26"]

# Define Clicks as numeric columns
test = data.apply(lambda x: pd.to_numeric(x, errors='ignore'))