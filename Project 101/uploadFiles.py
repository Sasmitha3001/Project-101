import dropbox
import os

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken

    def uploadFolder(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.accessToken)

        for root,dirs,files in os.walk(fileFrom):
            for fileName in files:
                localPath=os.path.join(root,fileName)
                realtive_path= os.path.relpath(localPath, fileFrom)
            dropbox_path=os.path.join(fileTo,realtive_path)
            f=open(localPath,'rb')
            dbx.files_upload(f.read(),dropbox_path)
def main():
    accessToken='O7dpyWJ6Ch0AAAAAAAAAATvJE7qipXPtiJ_IrJjV3bGizmSADMM8Q0sPt8Z0sdh7'

    transferDbx=TransferData(accessToken)
    fileFrom=str(input("Enter foldr path to be transfered\t"))
    fileTo=str(input("Enter the path to upload in dropbox\t"))

    transferDbx.uploadFolder(fileFrom,fileTo)
    print("File has been moved")

main()

