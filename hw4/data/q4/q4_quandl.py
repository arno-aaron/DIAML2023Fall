import nasdaqdatalink
import pandas

nasdaqdatalink.ApiConfig.api_key = "UpwkcUVd6mcdWtpbGkyD"

unemployment_data = nasdaqdatalink.get("ODA/ISR_LUR")

# print(wheat_data)
unemployment_data.to_csv("C:/Users/Aaron/Documents/GitHub/DIAML2023Fall/hw4/data/q4/data.csv")
