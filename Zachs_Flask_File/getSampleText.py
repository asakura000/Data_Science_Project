# script to access sample of 100 texts from excel spreadsheet

import pandas as pd
import numpy as np
from random import choice as c
import random

df = pd.read_excel('100_SAMPLES.xlsx')

# convert text column to a list of 100 strings
samples = df.text.tolist()

# choose 1 at random
sampleOne = c(samples)

# choose 10 at random - for dropdown menu
sampleTen = random.sample(samples, 10)