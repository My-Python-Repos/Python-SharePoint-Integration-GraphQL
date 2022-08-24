#from requests_oauthlib import OAuth2Session
import requests
import yaml
import json

graph_url = 'https://graph.microsoft.com/v1.0'

SITES = '/sites'
LISTS = '/lists'
HOST_NAME = 'azure.sharepoint.com'
WEB_ID = ''
site_lists_dict = None
COLUMNS = '/columns'
SITE_ID = ''
WEB_ID = ''
LIST_ID = ''

# EXAMPLE OF AUTH WOULD BE -> Bearer (SOME-TOKEN)'
AUTHORIZATION = ''


# Get sites for sharepoint
def get_sites(site_id: str, token: str):
    '''This function retrives metadata about a particular sharepoint site'''

    headers = {'Authorization': token,'Content-Type': 'application/json'}
    url_format = graph_url + SITES + "/" + site_id
    response = requests.get(url_format, headers=headers,verify=False)

    #print(response.text)
    return response



def get_lists(site_id: str, token: str):
    '''This function is used to retrive the Lists in a SharePoint site'''
    headers = {'Authorization': token}
    url_format = graph_url + SITES + "/" + site_id + '/' + LISTS
    response = requests.get(url_format, headers=headers,verify=False)

    #print(response.text)
    return response


def get_specific_site(host_name: str,site_id: str, web_id:str, token: str):
    '''This function gives all the lists in a particular absolute path using WebID'''
    headers = {'Authorization': token}
    url_format = graph_url + SITES + "/" + HOST_NAME + \
        "," + site_id + "," + web_id + '/' + LISTS
    print(url_format)
    response = requests.get(url_format, headers=headers,verify=False)

    #print(response.text)
    return response


def get_specific_list(host_name: str,site_id: str, web_id:str,list_id: str, token: str):
    '''This function retrives information about a particular list'''
    headers = {'Authorization': token}
    url_format = graph_url + SITES + "/" + HOST_NAME + \
        "," + site_id + "," + web_id + '/' + LISTS + '/' + list_id
    print(url_format)
    response = requests.get(url_format, headers=headers,verify=False)

    #print(response.text)
    return response

def get_list_columns(host_name: str,site_id: str, web_id:str,list_id: str,token: str):
    '''This function retrives column information of a particular list'''
    headers = {'Authorization': token}
    url_format = graph_url + SITES + "/" + HOST_NAME + \
        "," + site_id + "," + web_id + '/' + LISTS + '/' + list_id + COLUMNS
    print(url_format)
    response = requests.get(url_format, headers=headers,verify=False)

    print(response.text)
    return response

def get_list_data(host_name: str,site_id: str, web_id:str,list_id: str,token: str):
    '''This function retrives items(field value set--all columns) for a particular list'''
    headers = {'Authorization': token}
    url_format = graph_url + SITES + "/" + HOST_NAME + \
        "," + site_id + "," + web_id + '/' + LISTS + '/' + list_id + '/items?expand=fields'
    #print(url_format)
    response = requests.get(url_format, headers=headers,verify=False)

    #print(response.text)
    return response.text

def add_list_data(host_name: str,site_id: str, web_id:str,list_id: str,token: str):
    '''This function adds an item to an existing list'''
    addItem={
    "fields": {
        "EEN": "000000000",
        "Name": "Test_Add",
        "Class": 0
        }
        }
    headers = {'Authorization': token}
    url_format = graph_url + SITES + "/" + HOST_NAME + \
        "," + site_id + "," + web_id + '/' + LISTS + '/' + list_id + '/items'
    #print(url_format)
    response = requests.post(url_format, headers=headers,data=json.dumps(addItem),verify=False)

    #print(response.text)
    return response.text
