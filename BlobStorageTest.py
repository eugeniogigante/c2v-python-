#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eugenio.gigante
#
# Created:     30/03/2021
# Copyright:   (c) eugenio.gigante 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# cmd setx AZURE_STORAGE_CONNECTION_STRING "XxLIHurK4e55eyd0KiPpcjt6Z97Lr9l/X6vKUHTAz3q5S7eh3wNViWVFTD3m4Lwi/o+cBMJ+P5lm4Dm2pCDn0w=="

def listBlobContainer():
    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

    except Exception as ex:
        print('Exception:')
        print(ex)

    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)


def main():
    try:
        print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

    except Exception as ex:
        print('Exception:')
        print(ex)

    # Create a local directory to hold blob data
    #local_path = "./data"
    #os.mkdir(local_path)

    # Create a file in the local data directory to upload and download
    #local_file_name = str(uuid.uuid4()) + ".txt"
    #upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    #file = open(upload_file_path, 'w')
    #file.write("Hello, World!")
    #file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

if __name__ == '__main__':
    #main()
    listBlobContainer()
