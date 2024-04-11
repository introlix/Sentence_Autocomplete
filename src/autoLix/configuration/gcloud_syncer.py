import os
from google.cloud import storage

class GCloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):
       """
         Function to sync files from local machine to Google Cloud Storage
        
        Args:
            gcp_bucket_url (str): Google Cloud Storage bucket URL
            filepath (str): Local file path
            filename (str): Local file name
       """
       client = storage.Client()
       bucket = client.get_bucket(gcp_bucket_url)
       blob = bucket.blob(filename)

       bucket.blob(filename).upload_from_filename(filepath)
    #    command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
    #    os.system(command)

    # write a function to sync folder from gcloud
    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
         """
            Function to sync the folder from the gclooud to local machine

            Args:
                gcp_bucket_url (str): Google Cloud Storage bucket URL
            filename (str): Local file name
                destination (str): Local file path
         """
         command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
         os.system(command)