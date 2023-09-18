import nasdaqdatalink
import pandas

nasdaqdatalink.ApiConfig.api_key = "UpwkcUVd6mcdWtpbGkyD"

wheat_data = nasdaqdatalink.get("ODA/PWHEAMT_USD")
oil_data = nasdaqdatalink.get("WGEC/WLD_CRUDE_WTI")
gold_data = nasdaqdatalink.get("BUNDESBANK/BBK01_WT5511")

# print(wheat_data)
wheat_data.to_csv("C:/Users/Aaron/Documents/GitHub/DIAML2023Fall/hw2/quandl/wheat.csv")
oil_data.to_csv("C:/Users/Aaron/Documents/GitHub/DIAML2023Fall/hw2/quandl/oil.csv")
gold_data.to_csv("C:/Users/Aaron/Documents/GitHub/DIAML2023Fall/hw2/quandl/gold.csv")
