import ftplib
import csv
import os
from ftplib import FTP

ftp = FTP('192.168.1.2')
ftp.login('admin', 'TAIL')
ftp.cwd('FILES/LabTestRecording')

def ftp_connect():
    ftp = FTP('192.168.1.2')
    ftp.login('admin', 'TAIL')
    ftp.cwd('FILES/LabTestRecording')


def process_one_file(i):
    ftp_connect()
    file_path = "G:/My Drive/PGE Frequency Response/Umar" + '/' + i
    localfile = open(file_path, 'wb')
    ftp.retrbinary('RETR '+i, localfile.write, 1024)
    localfile.close()

    # filesize_after_download = os.path.getsize(file_path)
  
def start_stream():
    linelist = ftp.nlst()
    for i in linelist:
        process_one_file(i)
    
# while True:
#     start_stream()