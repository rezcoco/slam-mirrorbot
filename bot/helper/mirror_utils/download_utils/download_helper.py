# An abstract class which will be inherited by the tool specific classes like aria2_helper or mega_download_helper
import threading
from bot.helper.ext_utils.bot_utils import get_readable_file_size


class MethodNotImplementedError(NotImplementedError):
    def __init__(self):
        super(self, 'Not implemented method')


class DownloadHelper:
    def __init__(self, size=0.0):
        self.name = ''  # Name of the download; empty string if no download has been started
        # self.size = 0.0  # Size of the download
        self.downloaded_bytes = 0.0  # Bytes downloaded
        self.speed = 0.0  # Download speed in bytes per second
        self.progress = 0.0 
        self.progress_string = '0.00%'
        self.eta = 0  # Estimated time of download complete
        self.eta_string = '0s'  # A listener class which have event callbacks
        self._resource_lock = threading.Lock()
        self.size = size
        self.status = False
        self.checking = False
        self.MainFolderName = ''
        self.MainFolderLink = ''
        self.DestinationFolderName = ''
        self.DestinationFolderLink = ''


    def get_size(self):
        return get_readable_file_size(int(self.size))
    
    def add_size(self, value):
        self.size += int(value)

    def set_name(self, name=''):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_status(self, stat):
        self.status = stat
    
    def done(self):
        return self.status

    def checkFileExist(self, checking=False):
        self.checking = checking

    def checkFileStatus(self):
        return self.checking

    def SetMainFolder(self, folder_name, link):
        self.MainFolderName = folder_name
        self.MainFolderLink = link

    def SetDestinationFolder(self, folder_name, link):
        self.DestinationFolderName = folder_name
        self.DestinationFolderLink = link

    def add_download(self, link: str, path):
        raise MethodNotImplementedError

    def cancel_download(self):
        # Returns None if successfully cancelled, else error string
        raise MethodNotImplementedError
