import pandas as pd
import sys
import dpre

fp = sys.argv[1]
df = pd.read_csv(fp)

dpre.transform(df)
