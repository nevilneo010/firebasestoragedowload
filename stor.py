def main():
    from google.cloud import storage
    from firebase import firebase
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="raspi.json"
    firebase = firebase.FirebaseApplication('https://raspi-48bd3.firebaseio.com/')
    client = storage.Client()
    bucket = client.get_bucket('pythonik')
    blob = bucket.get_blob('ss')
    blob.download_to_filename('ss.png')

if __name__  == '__main__':
    main()
#imagePath = "ss.png"
#imageBlob = bucket.blob("ss")
#imageBlob.upload_from_filename(imagePath)