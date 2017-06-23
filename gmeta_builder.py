import json
from json_sort import get_list_from_json
from random import randint

#TODO: Add topics into ingest.

def gmeta_entry(metadata_list):

    entry = {
        "ingest_type": "GMetaEntry",
        "ingest_data": {
            "@datatype": "GMetaEntry",
    #"subject": "https://datarepository.org/dataset/101",
    "subject": metadata_list[0],
    "visible_to": ["public"],
    "content": {
        "@context": {
            "cdiac": "http://ewn.testing.nick.globuscs.info/meta/daymet-3.xsd",
            "datacite": "https://schema.labs.datacite.org/meta/kernel-4.0/metadata.xsd"
    },
    "datacite:resourceTypeGeneral": "dataset",
    "datacite:contributor.author": "Oak Ridge National Laboratory",
    "cdiac:headers":metadata_list[1],
    "cdiac:num_headers":len(metadata_list[1]),
    "cdiac:mimetype":metadata_list[2],
    "cdiac:filesize":metadata_list[3],
    "cdiac:extension":metadata_list[4]

    }
    }
    }

    #print(entry)
    return entry