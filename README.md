# StudySpaceDBTools

#### Prerequisites:
Working installation of Python3.

#### Run the script
Run in terminal: `python3 dynamodbItemGenerator.py`.
The script will ask for input and output file name, provide them without specifying the file type (for example data.json -> data).

The input file has to be a JSON containing a list of 'PutRequest' for a specified dynamodb table. The JSON follows the format that can be read by
the command `aws dynamodb batch-write-item --request-items <item-json>`. Check the data model templates or following link for more details: <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/batch-write-item.html#examples>


## How to upload data to the studyspace aws dynamodb tables
1. Create your data by writing the corresponding JSON. Use the data model templates from the file data_model_templates.md.

2. Run your JSON through the dynamodbItemGenerator. It will automatically set the id's and timestamps, such that the items
become dynamodb-compliant. The script will output your JSON into a new file.

3. Upload the new file to the AWS CloudShell. Then run the command `aws dynamodb batch-write-item --request-items file://my-table-data.json` with
`my-table-data.json` being the file you uploaded.

4. Check that your data was correctly uploaded by checking the corresponding tables in Amplify Studio (AWS Services -> Amplify -> studyspace_mobile_app)
or by directly inspecting the dynamodb tables (AWS Services -> DynamoDB).


New functions to update and delete entries will follow soon.
