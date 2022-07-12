import pandas_datareader as pdr
# Request data via Yahoo public API
data = pdr.get_data_yahoo('NVDA')
# Display Info
print(data.info())


print(data)

for row in data:
    print(row)