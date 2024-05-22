import requests
import pandas as pd


def getMetadata(url, auth, meta_object,payload = {'paging': False}):
    '''
    This function can be used to get any of the DHIS2 metadata objects.
    The metadata objects include 'dataElemnts, OrganisationUnits,categoryCombos,categoryOptionCombos,indicators,datasets etc
    url will be the base url ending with api for example  http//dhis2.org/api change this to your url
    you will need to include a username and password as a tupple ie and assing it to auth ie auth = (username,password)
    payload is default for ensurering that all pages are loaded
    '''

    # using request, data is pulled from the dhis2 instance
    r = requests.get(f'{url}/{meta_object}', auth=auth, params=payload)
    if r.ok == False:
        print(f'The request was not successful it came with the following error\n{r.content}')
        return None
    else:
        return pd.DataFrame(r.json()[meta_object])

def getAnalytics(url, payload, auth):
    '''
    This function can be used to get any of the DHIS2 datavalues from specified datasets.
    url will be the base url ending with api for example  http//dhis2.org/api change this to your url
    you will need to include a username and password as a tupple ie and assing it to auth ie auth = (username,password)
    payload is where you include all the parameters you would like to pass as a dictionary
    payload_datavalues = {'dataSet' : 'datasetID',
                          'startDate' : 'start date in the format yyyy-mm-dd',
                          'endDate': 'start date in the format yyyy-mm-dd',
                          'orgUnit' : 'organisationUnitID you can includemrethat one as one string separated by ege "sklfdsfj,oshfkdsl,rowueiure,"',
                          'children': 'true'}
    '''

    r = requests.get(f'{url}/dataValueSets', auth=auth, params=payload)
    return pd.DataFrame(r.json()['dataValues'])[['dataElement', 'period', 'orgUnit', 'categoryOptionCombo','attributeOptionCombo', 'value']]

if __name__ == '__main__':
    auth=('xxxxx','xxxxx')
    url = 'xxxxx'
    payload = {'dataSet' : 'LipkKq7JANH',
               'startDate' : '2023-10-01',
               'endDate': '2024-09-30',
               'orgUnit' : 'PFu8alU2KWG',
               'children': 'true'}

    metadata_dataElements = getMetadata(url, auth, 'dataElements')
    #print(metadata_dataElements.head())

    dataSet_elements = getAnalytics(url, payload_datavalues, auth)
    print(dataSet_elements.head())

   
