import os
import sys
import threading
import Queue
import logging
from googleplay import GooglePlayAPI
from config import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
download_queue = Queue.Queue()


class DownloaderThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.api = GooglePlayAPI(ANDROID_ID)
        self.api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD)

    def run(self):
        download_apps(self.api)


def get_categories(api):
    logger.info('Getting category names')
    data = api.browse().category
    categories = []
    for i in data:
        temp = str(i.dataUrl.split("cat=")[1])
        categories.append(temp)
    return categories


def get_app_details(api, categories, subcategory, number):
    logger.info('Getting apps\' details for each category')
    apps_list = []
    for category in categories:
        data = api.list(category, subcategory, number)
        for app in data.doc[0].child:
            apps_list.append(app)
    return apps_list


def validate_apps(apps_list, max_size):
    logger.info('Validating Apps')
    for app in apps_list:
        package_name = str(app.docid)
        file_name = DOWNLOAD_PATH + app.title + '.apk'
        size = int(app.details.appDetails.file[0].size)
        if size >= max_size:
            logger.info('App too large')
        else:
            if not os.path.isfile(file_name):
                download_queue.put(package_name)


def download_apps(api):
    logger.info('Downloading Apps')
    while not download_queue.empty():
        package_name = download_queue.get()
        m = api.details(package_name)
        doc = m.docV2
        app_name = doc.title
        vc = doc.details.appDetails.versionCode
        ot = doc.offer[0].offerType
        file_name = DOWNLOAD_PATH + app_name + '.apk'
        data = api.download(package_name, vc, ot)
        open(file_name, "wb").write(data)
        logger.info('App saved as ' + file_name)


if __name__ == "__main__":
    logger.info('Setting up GooglePlayAPI')
    api = GooglePlayAPI(ANDROID_ID)
    api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD)
    cat = get_categories(api)
    apps = get_app_details(api, cat, SUB_CATEGORY, NUMBER)
    if len(sys.argv) == 2:
        validate_apps(apps, int(sys.argv[1]))
    else:
        validate_apps(apps, 10 * 1024 * 1024)
    thread1 = DownloaderThread()
    thread2 = DownloaderThread()
    thread3 = DownloaderThread()
    thread4 = DownloaderThread()
    thread5 = DownloaderThread()

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
