# StudySpaceDBTools

Run the script as follows: `python3 dynamodbItemGenerator.py`.
The script will ask for input and output file name, provide them without specifying the file type for example data.json -> data .

Input file has to be a json containing a list of put request for a specified dynamodb table, that be read by the command `AWS dynamodb batch-write-item`. See following link - <https://docs.aws.amazon.com/cli/latest/reference/dynamodb/batch-write-item.html#examples>
