# Install the package via: 

`pip install git+https://github.com/Blazkowiz47/torch-framework-python.git#egg=dl_framework_generator`

or 

`pip install dl_framework_generator`

or

`git clone https://github.com/Blazkowiz47/torch-framework-python.git; cd torch-framework-python; pip install -e .`

# Usage: 
To generate a template project, you can run: 
`framework create -p <PROJECT_NAME> -d <SAMPLE_DATASET_NAME>  -m <SAMPLE_MODEL_NAME>`

To add custom datasets into and existing project:
`framework add -d <DATASET_NAME>`

To add custom models into and existing project:
`framework add -m <MODEL_NAME>`



