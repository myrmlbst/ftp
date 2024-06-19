# download files that aren't in the main directory
from ftplib import FTP

host = "loremipsum"
user = "dolorsitamet"
password = "consecteturadipiscingelit"

with FTP(host) as ftp:
    # connecting to the server
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    ftp.cwd("mydir")

    with open('myspecialfile.txt', 'wb') as f:
        ftp. retrbinary('RETR ' + 'otherfile.txt', f.write, 1024)
        
    ftp.quit()
