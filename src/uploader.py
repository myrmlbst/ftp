from ftplib import FTP

host = "loremipsum"
user = "dolorsitamet"
password = "consecteturadipiscingelit"

with FTP(host) as ftp:
    # connecting to the server
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    # uploading files
    with open('myUploads.txt', 'rb') as f:
        # read from file and return it to FTP server
        ftp.storbinary("STOP " + 'upload.txt', f)

    ftp.quit()
