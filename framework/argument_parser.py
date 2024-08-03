import re
from typing import Dict, List, NoReturn, Any

def validate_file_name(filename:str)->bool:
    pattern = '^[A-Za-z_][A-za-z0-9_]+$'
    if re.match(pattern, filename):
        return True
    return False


def parse_args(args: List[str])->Dict[str,Any]:
    print(args)
    parsedArgs = {'PROJECT_NAME':"",'DATASET_NAME':"",'MODEL_NAME':""}

    #check for valid project name when arg 0 is create
    if args[0] == "create":
        if len(args)>2:
            if validate_file_name(args[1]):
                parsedArgs['PROJECT_NAME'] = args[1]
            else:
                raise ValueError("Invalid Project Name")
        else:
            raise ValueError("Insufficient arhuments")

    #to check if same argument is not provided multiple times    
    flagDataSet = False
    flagModelSet = False

    #check for valid dataset name when -d arg is provided and valid model name when -m arg is provided
    if args[2]=="-d":
        if validate_file_name(args[3]):
            parsedArgs['DATASET_NAME'] = args[3]
            flagDataSet = True
        else:
            raise ValueError("Invalid Dataset Name")
    if args[4]=="-m":
        if validate_file_name(args[5]):
            parsedArgs['MODEL_NAME'] = args[5]
            flagModelSet = True
        else:
            raise ValueError("Invalid Model Name")
    if args[4]=="-d":
        if flagDataSet==False:
            if validate_file_name(args[5]):
                parsedArgs['DATASET_NAME'] = args[5]
                flagDataSet = True
            else:
                raise ValueError("Invalid Dataset Name")
        else:
            raise ValueError("Dataset already provided")
    if args[2]=="-m":
        if flagModelSet==False:
            if validate_file_name(args[3]):
                parsedArgs['MODEL_NAME'] = args[3]
                flagDataSet = True
            else:
                raise ValueError("Invalid Model Name")
        else:
            raise ValueError("Model already provided")
    
    if len(args)>6:
        raise ValueError("Too many arguments provided")

    print(parsedArgs)
    return parsedArgs