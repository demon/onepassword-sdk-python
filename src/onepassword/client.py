import sys
import platform
from core import *
from secrets_api import Secrets
import asyncio
import weakref

SDK_LANGUAGE = "Python"
SDK_VERSION = "0010001"  # v0.1.0
DEFAULT_INTEGRATION_NAME = "Unknown"
DEFAULT_INTEGRATION_VERSION = "Unknown"
DEFAULT_REQUEST_LIBRARY = "net/http"
DEFAULT_OS_VERSION = "0.0.0"


class Client:
    def __init__(self, auth, integration_name, integration_version):
        self.config = new_default_config(auth=auth, integration_name=integration_name, integration_version=integration_version)
        self.secrets = Secrets(client_id=InitClient(self.config))


def new_default_config(auth, integration_name, integration_version):
    client_config_dict = {
        "serviceAccountToken": auth,
        "programmingLanguage": SDK_LANGUAGE,
        "sdkVersion": SDK_VERSION,
        "integrationName": integration_name,
        "integrationVersion": integration_version,
        "requestLibraryName": DEFAULT_REQUEST_LIBRARY,
        "requestLibraryVersion": str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]),
        "os": platform.system(),
        "osVersion": platform.architecture()[0],
        "architecture": DEFAULT_OS_VERSION,
    }
    return client_config_dict

async def main():
    await InitClient(new_default_config("",DEFAULT_INTEGRATION_NAME,DEFAULT_INTEGRATION_VERSION))

if __name__ == '__main__':
    asyncio.run(main())
