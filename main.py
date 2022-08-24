#import yaml
#from requests_oauthlib import OAuth2Session
import os
import time
import requests
from util.settings import load_settings
from sharepoint_graph.sites import get_sites, get_lists, get_specific_site,get_list_columns,get_specific_list,get_list_data

import json

# This is necessary because Azure does not guarantee
# to return scopes in the same case and order as requested

TENANT_ID = ''
SITE_ID = ''
CLIENT_ID = ''
CLIENT_SECRET = ''
GRANT_TYPE = 'client_credentials'
LIST_ID = ''
WEB_ID = ''
HOST_NAME = 'azure.sharepoint.com'



def get_token_request(conn):
    d = {'grant_type': GRANT_TYPE,
         'client_id': CLIENT_ID,
         'client_secret': CLIENT_SECRET, 'scope': 'https://graph.microsoft.com/.default'}
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    response = requests.post("https://login.microsoftonline.com/" + TENANT_ID + "/oauth2/v2.0/token", headers=headers, data=d,verify=False)
    return response


if __name__ == '__main__':
    # example using just a simple request to get a access token then get sites
    conn_obj = load_settings("config/oauth_settings.yaml")
    resp = get_token_request(conn_obj)
    access_token = json.loads(resp.text)
    #Load config for SharePoint sites and lists info
    lists_obj = load_settings("config/config.yaml")
    #list_id = lists_obj['lists']["id"]
    #host= os.environ.get(lists_obj['sites']['host_name'])
    #site_id = os.environ.get(lists_obj['sites']["site_id"])
    #web_id = os.environ.get(lists_obj['sites']["web_id"])
    list_id = LIST_ID
    host= HOST_NAME
    site_id = SITE_ID
    web_id = WEB_ID
    #get_sites(site_id, access_token['access_token'])
    #get_specific_site(host,site_id,web_id,access_token['access_token'])
    get_list_columns(host,site_id,web_id,list_id,access_token['access_token'])
    data=get_list_data(host,site_id,web_id,list_id,access_token['access_token'])
