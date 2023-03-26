import ftplib
ip = input('Enter IP: \n')
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' + str(hostname) + ' FTP anonymous login succeeded.')
        ftp.quit()
        return True
    except Exception:
        print('\n [-] ' + str(hostname) + ' FTP anonymous login failed.')
        return False
        
if __name__ == '__main__':
    anonLogin(ip)
