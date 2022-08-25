Sharepoint Python API App
===========================

:wave: Welcome to the easy to use code base for consuming sharepoint. This code base should help you quickly get it up and running for consuming sharepoint from Azure.

## Description

While working on this we found out there is some core concepts you need to understand about Sharepoint in Azure.

### Sharepoint

#### Scopes

The Microsoft identity platform implements the OAuth 2.0 authorization protocol. OAuth 2.0 is a method through which a third-party app can access web-hosted resources on behalf of a user. Any web-hosted resource that integrates with the Microsoft identity platform has a resource identifier, or Application ID URI.

- .default - To use the authentication based off the application

### Sharepoint API Root Sources

If you need to look specifically at the routes to call, you can check them [Here](https://docs.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0#sharepoint-api-root-resources)

## Pre - Reqs

- Python 3.7

## Usage

### Directory Structure

```
    ├── config
    │   ├── config.yaml
    │   └── oauth_settings.yaml
    ├── sharepoint_graph
    │   └── sites.py
    ├── util
    │   └──settings.py
    ├── main.py
```

### Files explained (variables)

```
main.py

TENANT_ID = '' #Just the tenant ID
SITE_ID = '' #The site id for the sharepoint site
CLIENT_ID = '' #The client id that you get from azure or your sharepoint site
CLIENT_SECRET = '' # #The client secret that you get from azure or your sharepoint site
GRANT_TYPE = 'client_credentials' #The authentication that is being used for getting a token
LIST_ID = '' #The list id of where you would want to get the sharepoint lists
```

```
sharepint_graph/sites.py

graph_url = 'https://graph.microsoft.com/v1.0'

SITES = '/sites'
LISTS = '/lists'
HOST_NAME = 'azure.sharepoint.com'
site_lists_dict = None
COLUMNS = '/columns'
HOST_NAME = ''
SITE_ID = ''
WEB_ID = ''
LIST_ID = ''
```

### Example URL Endpoint Flow

First we need to make a call to get our token.
You can see how to get a token in the [main.py](/main.py) code

```
https://login.microsoftonline.com/{{TenantID}}/oauth2/v2.0/token

```

Now that you have a token, you just need to create the endpoint base then call the sites and start pulling the data as you can see [here](/sharepoint_graph/sites.py).

```
https://graph.microsoft.com/v1.0/sites/{{hostname}},{{SITE_ID}},{{WEB_ID}}/
```

This is a simple python module that can you run it as a lib (just need to make this into a setup.py) or copy this code to your location.

## Install

    pip install -r requirements.txt

You need to start off first doing a virtual env. On mac it is:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

Running the code is very simple, just run python -m main and if everything is set, you can start calling the functions.

## Contributing

Please refer to [Contribution Guidelines](.github/CONTRIBUTING.md) for guidance on contributing to this project.

<table>
   
</table>
