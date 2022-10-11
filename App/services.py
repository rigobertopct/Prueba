# import requests
#
# def generate_request(url, params={}):
#     response = requests.get(url, params=params)
#
#     if response.status_code == 200:
#         return response.json()
#
# def get_username(params={}):
#     response = generate_request('https://api.apklis.cu/v2/application/', params)
#     if response:
#        user = response.get('results')
#        apks=[]
#        for m in user:
#            apks.append(m.get('name'))
#        return apks
#
#     return ''
# def saber_clima(params={}):
#     response=generate_request( 'https://www.redcuba.cu/api/weather_get_summary/', params)
#     if response:
#         clima=response.get('results')