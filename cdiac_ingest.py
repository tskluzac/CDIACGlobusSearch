import sys

from gmeta_builder import gmeta_entry
from json_sort import get_list_from_json

import json
import os

# from tqdm import tqdm

import globus_auth
# import paths
# import tika
# tika.initVM()
# from tika import parser, translate
from random import randint
import urllib

globus_url = "https://search.api.globus.org/"
globus_domain = "ripple-test"
##############################
#globus_domain = "cdiac-test"
##############################
def ingest(mdf_source_names, verbose=False):
    ''' Ingests feedstock from file.
        Arguments:
            mdf_source_names (str or list of str): Dataset name(s) to ingest.
            batch_size (int): Max size of a single ingest operation. -1 for unlimited. Default 100.
            verbose (bool): Print status messages? Default False.
        '''
    if verbose:
        print("\nStarting ingest of:\n", mdf_source_names, "\n")

    globus_client = globus_auth.login(globus_url, globus_domain)

    #TODO: Make this slightly more flexible.
    super_list = get_list_from_json()

    for listy in super_list:
        gmeta = gmeta_entry(listy)
        print gmeta

        output = ''

    #print 'indexing it'

    # with open('cdiac_gmeta_index2.json', 'r') as json_data:
    #     gmeta = json.load(json_data)
    #     json_data.close()

        output = globus_client.ingest(gmeta)

        print output


def format_gmeta(data):
    ''' Formats input into GMeta.
    If data is a dict, returns a GMetaEntry.
    If data is a list (must be GMetaEntrys), returns a GMetaList.
    REQUIRED:
        GMetaEntry (dict):
            globus_subject (unique string, should be URI if possible)
            acl (list of UUID strings, or ["public"])
        GMetaList (list):
            Valid list of GMetaEntrys
    '''
    if type(data) is dict:
        # data["mdf-publish.publication.community"] = "Materials Data Facility"  # Community for filtering
        gmeta = {
            "@datatype": "GMetaEntry",
            "@version": "2016-11-09",
            "subject": data.pop("globus_subject"),
            "visible_to": data.pop("acl"),
            "content": data
            }

    elif type(data) is list:
        gmeta = {
            "@datatype": "GIngest",
            "@version": "2016-11-09",
            "ingest_type": "GMetaList",
            "ingest_data": {
                "@datatype": "GMetaList",
                "@version": "2016-11-09",
                "gmeta": data
                }
            }

    else:
        sys.exit("Error: Cannot format '" + str(type(data)) + "' into GMeta.")

    return gmeta



if __name__ == "__main__":

    all_source_names = [

        ]
    ingest(all_source_names, verbose=True)