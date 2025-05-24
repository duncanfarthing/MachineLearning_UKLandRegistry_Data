import os
import requests

def download_file_if_needed(url: str, dest_path: str, overwrite: bool = False):
    """
    Downloads a file from a URL if it doesn't already exist at the destination.

    Parameters:
    - url (str): The URL to download the file from.
    - dest_path (str): The local file path where the file should be saved.
    - overwrite (bool): If True, force re-download even if file exists.
    """
    if os.path.exists(dest_path) and not overwrite:
        print(f"File already exists at {dest_path}. Skipping download.")
        return

    print(f"Downloading from {url} to {dest_path}...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive chunks
                    f.write(chunk)
        print("Download completed.")
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
