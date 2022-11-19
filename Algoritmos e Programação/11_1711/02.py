def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) : 
  
    
    import requests, json 
  
    
    base_url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"
  
    
    main_url = base_url + "&from_currency =" + from_currency + "&to_currency =" + to_currency + "&apikey =" + api_key 
  
    
    
    req_ob = requests.get(main_url) 
  
    
    
      
    
    result = req_ob.json() 
  
    print(" Result before parsing the json data :\n", result) 
  
      
    print("\n After parsing : \n Realtime Currency Exchange Rate for", 
          result["Realtime Currency Exchange Rate"] 
                ["2. From_Currency Name"], "TO", 
          result["Realtime Currency Exchange Rate"] 
                ["4. To_Currency Name"], "is", 
          result["Realtime Currency Exchange Rate"] 
                ['5. Exchange Rate'], to_currency) 
  
  
  
if __name__ == "__main__" : 
  
    
    from_currency = "USD"
    to_currency = "INR"
  
    
    api_key = "Your_Api_Key"
  
    
    RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) 