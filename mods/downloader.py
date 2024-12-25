class DOWNLOADER:
    # download/upload file or folder
    def download(self, path, file_bytecode):
        try:
            with open(path, 'wb') as file:
                file.write(base64.decodebytes(file_bytecode.encode('utf-8')))
                return "Downloaded: " + path
        except Exception as e:
            return "Error: " + str(e)
        
    def upload(self, path, local_path):
        try:
            with open(local_path, 'rb') as file:
                return base64.encodebytes(file.read()).decode('utf-8')
        except Exception as e:
            return "Error: " + str(e)