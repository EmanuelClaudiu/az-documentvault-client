from django.shortcuts import render
from django.http import HttpResponse
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

load_dotenv()
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
BLOB_SERVICE_CLIENT = BlobServiceClient.from_connection_string(CONNECTION_STRING)

CONTAINER_NAME = "user-documents"
CONTAINER_CLIENT = BLOB_SERVICE_CLIENT.get_container_client(CONTAINER_NAME)

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('document'):
        uploaded_file = request.FILES['document']

        blob_client = CONTAINER_CLIENT.get_blob_client(uploaded_file.name)

        blob_client.upload_blob(uploaded_file.read(), overwrite=True)

        return render(request, "documentvault/index.html", {"message": "Success!"})
    
    return render(request, 'documentvault/index.html')
