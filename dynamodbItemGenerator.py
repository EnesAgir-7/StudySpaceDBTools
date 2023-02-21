# This script is used to set uuid and time stamps for items that are going to be uploaded to dynamodb
# It expects a json containing list of put request for specific dynamodb table

import uuid
import json
from datetime import datetime 

file_name_read = input("Enter the file name to read json: ")
file_name_write = input("Enter the file name tp write json: ")

def SetUpDBItems(data):
    tableName = list(data.keys())[0]
    for putRequest in data[tableName]:
        currentDateTime = datetime.now().isoformat(timespec='milliseconds')
        newItemId = {
            "S": str(uuid.uuid4())
        }
        createdAt = {
            "S": currentDateTime + "Z"
        }
        _lastChangedAt ={
            "N":  str(int(datetime.timestamp(datetime.now()) * 1000))
        }
        putRequest["PutRequest"]["Item"]["id"] = newItemId
        putRequest["PutRequest"]["Item"]["createdAt"] = createdAt
        putRequest["PutRequest"]["Item"]["updatedAt"] = createdAt
        putRequest["PutRequest"]["Item"]["_version"] = {"N": "1"}
        putRequest["PutRequest"]["Item"]["_lastChangedAt"] = _lastChangedAt

        # print(putRequest["PutRequest"]["Item"])
    return data


def write_json_file(data):
    with open(f'{file_name_write}.json', 'w') as json_file:
        json.dump(data, json_file)

if __name__ == '__main__':
    # Read the json file
    with open(f'{file_name_read}.json') as json_file:
        data = json.load(json_file)

    # Create the item in the database
    newData = SetUpDBItems(data)

    # Write the updated data to the json file
    write_json_file(newData)