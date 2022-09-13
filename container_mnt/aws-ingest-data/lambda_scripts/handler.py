import requests

def lambda_handler(event, context):
    import requests

    #the required first parameter of the 'get' method is the 'url':
    x = requests.get('https://w3schools.com/python/demopage.htm')

    return { 
        'text' : x.text
    }