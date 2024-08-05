
import os
from .constants.templates import templateDict

def fileGenerator(fileName: str, directory:str, template: str):
    
    with open(os.path.join(directory, fileName), "w+") as fp:    
        fp.writelines(templateDict[template].format(name=fileName))
            



