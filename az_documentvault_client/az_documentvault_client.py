import reflex as rx
import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "user-documents"

class AzureUploadState(rx.State):
    conn_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    uploaded_urls: list[str] = []

    async def handle_azure_upload(self, files: list[rx.UploadFile]):
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        for file in files:
            file_data = await file.read()
            
            blob_client = container_client.get_blob_client(file.filename)

            blob_client.upload_blob(file_data, overwrite=True)

            self.uploaded_urls.append(blob_client.url)


def index() -> rx.Component:
    return rx.vstack(
        rx.upload(
            rx.text("Drag files here to upload to Azure"),
            id="azure_upload",
            border="2px dashed blue",
            padding="2em",
        ),
        rx.button(
            "Upload to Cloud",
            on_click=AzureUploadState.handle_azure_upload(
                rx.upload_files(upload_id="azure_upload")
            ),
        ),
        rx.foreach(AzureUploadState.uploaded_urls, rx.text),
    )


app = rx.App()
app.add_page(index)
