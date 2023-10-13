# HTML to Markdown Conversion 

This script will convert HTML files to Markdown files abiding to markdown standards.

## Installation

1. Install [Python](https://www.python.org/ftp/python/3.12.0/python-3.12.0-macos11.pkg) on your system
2. Install Mardownify library 

    ```pip3 install markdownify```

## Developer Portal Content Repo(apigee-portal-content)

The content on the existing portal is available in this [repo](https://github.com/bazaarvoice/apigee-portal-content). You can fork the repo and clone it locally to access the html files at ease of the page you want to migrate. 

## Usage
#### html_to_md_folder.py Script
Use above script when you want to convert more than one html file to md file. You would need to place all the html file in a folder and pass folder name as argument in the script. 
You can choose any folder from cloned **apigee-portal-content** repo for testing.  

#### html_to_md_file.py Script 
Use above script when you want to convert one html file to md file. You would need to pass html file path and output path with md file name.
You can choose any file from cloned **apigee-portal-content** repo for testing.

