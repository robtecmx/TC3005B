import pandas

DF = pandas.read_csv('DB.csv');

print(DF)

for _, row in DF.iterrows():
    print(row);




