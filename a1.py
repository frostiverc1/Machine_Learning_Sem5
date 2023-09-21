import pandas as pd
import numpy as np
import math
df=pd.read_excel('D:/ONLINE CLASSES (ENGINEERING)/SEM 5/PROJECTS/19CSE305 MACHINE LEARNING/lab4/lab4-dataset.xlsx')

c1_stud=(df.iloc[0:,2])
c2_buys_comp=(df.iloc[0:,4])
_,counts_c1 = (np.unique(c1_stud, return_counts=True))
_,counts_c2 = (np.unique(c2_buys_comp, return_counts=True))
pr_c1=counts_c1/len(c1_stud)
pr_c2=counts_c2/len(c2_buys_comp)

ent=-(pr_c1[0] * math.log2(pr_c1[0]) + pr_c2 * math.log2(pr_c2[0]))
ent
