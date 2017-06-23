import json
from pprint import pprint



def get_list_from_json():
    list_of_lists = []

    with open('metadata_5-15.json', 'r') as f:
        data = json.load(f)

    i=0
    while True:
        try:
            #Get extension, filename, filesize
            extension = data['files'][i]['system']['extension']
            filename = data['files'][i]['system']['file']
            filesize = data['files'][i]['system']['size']
            mimetype = data['files'][i]['system']['mime_type']

            try:
                headers = data['files'][i]['headers']
            except:
                headers=[]

            ### Create URI ###
            #Begin by extracting tskluzac path
            raw_path = data['files'][i]['system']['path'].split('/')
            #print(raw_path)

            globus_url = "globus:45a53408-c797-11e6-9c33-22000a1e3b52/cdiac/cdiac.ornl.gov/pub8old"

            #print(raw_path)

            #Now turn this into CDIAC pub8 path
            j=0 #0(''), 1(home), 2(tskluzac), 3(pub8)--- we may keep 3.
            for item in raw_path:
                if j<3:
                    j+=1
                    continue

                elif item == '':
                    j+=1
                    continue

                else:
                    globus_url = globus_url + "/" + item
                    j+=1


            if extension=='no extension':
                pass

            else:
                globus_url = globus_url + "/" + filename


            #globus_url + "/" + filename

            list = [globus_url, headers, mimetype,filesize, extension]

            list_of_lists.append(list)
            i+=1

        except:
            break


    #print(list_of_lists)
    return list_of_lists

#def entry_builder():

# thing = get_list_from_json()
# for item in thing:
#     print(item[0])
