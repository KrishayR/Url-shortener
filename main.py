import pyshorteners

try: 
    #Input
    url = input('Please enter the url: ')

    #Instantiating
    shortener = pyshorteners.Shortener()

    result = shortener.tinyurl.short(url)
    print(result)
except:
    print('Please enter a valid url')
