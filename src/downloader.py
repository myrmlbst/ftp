from ftplib import FTP

host = "loremipsum"
user = "dolorsitamet"
password = "consecteturadipiscingelit"

with FTP(host) as ftp:
    # connecting to the server
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    # downloading files
    with open('myUpload.txt', 'wb') as f: # open up file stream
        ftp.retrbinary("RETR " + 'mytest.txt', f.write, 1024)

    ftp.quit()
