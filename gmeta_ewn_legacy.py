import json
from json_sort import get_list_from_json



def gmeta_entry(metadata_list):

    entry = {
      "source_id": "EWN-KDF Portal",
      "ingest_type": "GMetaEntry",

        "@version": "2016-11-09",
        "visible_to": [
          "public"
        ],
        "subject": metadata_list[0],
        "content": {
          "@context": {
            "datacite": "http://schema.datacite.org/meta/kernel-4/metadata.xsd",
            "cdiac": "http://ewn.testing.nick.globuscs.info/meta/daymet-3.xsd"
          },
          "datacite:title": "CDIAC",
          "datacite:publisher": "Oak Ridge National Laboratory Carbon Dioxide Information Analysis Center (ORNL CDIAC)",
          "datacite:contributors": [
            {
              "datacite:contributor": {
                "datacite:contributorName": "United States Department of Energy"
              }}

          ],
          "datacite:identifier": metadata_list[0],
          "datacite:publicationYear": "2017",
          "datacite:dates": [
            {
              "datacite:date": "2017-06-10"
            }
          ],
          "datacite:formats": [
            {
              "datacite:format": metadata_list[4]
            }
          ],
          "datacite:sizes": [
            {
              "datacite:size": metadata_list[3]
            }
          ],
          "datacite:descriptions": [
            {
              "datacite:description": "The Carbon Dioxide Information Analysis Center (CDIAC), located at the U.S. Department of Energy's (DOE) Oak Ridge National Laboratory (ORNL), is the primary climate change data and information analysis center for DOE. CDIAC is supported by DOE's Climate and Environmental Sciences Division within the Office of Biological and Environmental Research (BER). CDIAC's data holdings include estimates of carbon dioxide emissions from fossil-fuel consumption and land-use changes; records of atmospheric concentrations of carbon dioxide and other radiatively active trace gases; carbon cycle and terrestrial carbon management datasets and analyses; and global/regional climate data and time series."
            }
          ],
          "cdiac:start_year": "1972",
          "cdiac:source": "http://cdiac.ornl.gov",
          "cdiac:Version_software": "http://cdiac.ornl.gov",
          "cdiac:Version_data": "http://cdiac.ornl.gov",
          "cdiac:Conventions": "CF-1.6",
          "cdiac:citation": "Please see http://cdiac.ornl.gov/ for current CDIAC data citation information",
          "cdiac:references": "Please see http://cdiac.ornl.gov/ for current information on Daymet references",
          "cdiac:mimetype": metadata_list[2],
          "cdiac:numheaders": len(metadata_list[1]),
          "cdiac:headers": metadata_list[1]

        }
      }

    return entry

def gmeta_list():
    list = get_list_from_json()
    i=0
    print(len(list))

    entries_holder = []

    for entry in list:
        i+=1
        entries_holder.append(gmeta_entry(entry))
    #print(entries_holder)

    the_big_one = {
 "@datatype": "GIngest",
 "@version": "2016-11-09",
 "ingest_type": "GMetaList",
 "ingest_data": {
   "@datatype": "GMetaList",
   "@version": "2016-11-09",
   "gmeta": entries_holder
 }
    }
    with open('cdiac_gmeta_index2.json','w') as f:
        json.dump(the_big_one,f)
    return the_big_one

gmeta_list()