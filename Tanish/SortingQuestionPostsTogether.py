import pandas as pd

df1 = pd.read_csv("C:\\Users\\tanis\\Downloads\\Data\\newquestionposts.csv", sep = '¬', error_bad_lines=False, encoding='ISO-8859-1')
df2 = pd.read_csv("C:\\Users\\tanis\\Downloads\\Data\\questions.csv", sep = ',', error_bad_lines=False, encoding='ISO-8859-1')
df = pd.merge(df1,df2, on='QuestionUno')
print(df[df.Subcategory == "Immigration"])