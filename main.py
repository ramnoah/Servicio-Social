import pandas as pd
import numpy as np
import utilities as util

siiaPath = r'cargasiia232.xlsx' # ! Change for user path
chPath = r'CH2023-2.xlsx' # ! Change for user path

siia = util.readSiia(siiaPath)
ch = util.readCH(chPath)