import pandas as pd

dict = {"Abisek": [10, 20, 30],
        "errol": [10, 20, 30],
        "jason": [10, 20, 30],
        "Nans": [10, 20, 30]}

df1 = pd.DataFrame(dict, index=["Course1", "Course2", "Course3"])
print(df1)
