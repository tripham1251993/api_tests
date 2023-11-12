import os
import sys


dir_name = os.path.dirname(__file__).replace(f"{os.sep}core_lib", "")
sys.path.append(dir_name)


try:
    import requests
    from core_lib import Logger

except ImportError as imp_err:
    print("There was an error importing files - From %s" % __file__)
    print("\n---{{{ Failed - " + format(imp_err) + " }}}---\n")
    raise


class APICoreLib:

    REQUEST_TIMEOUT_DEFAULT = 120

    def __init__(self, log_level="DEBUG"):
        self.logger = Logger.Logger(
            __name__.split(".")[-1], log_level=log_level
        )
        self.session = requests.Session()
        self.requests_map = {
            "GET": self.session.get,
            "PUT": self.session.put,
            "POST": self.session.post,
            "PATCH": self.session.patch,
            "DELETE": self.session.delete,
        }

    def send_request(
        self, method, url, timeout=REQUEST_TIMEOUT_DEFAULT, **kwargs
    ):
        """
        :return: formated response which contains following keys:
            url, body, code, headers, time
        """
        resp = self.requests_map.get(method.upper())(url, timeout=timeout, **kwargs)
        try:
            body = resp.json()
        except Exception:
            body = resp.content
        formated_response = {
            "url": resp.url,
            "body": body,
            "code": resp.status_code,
            "headers": resp.headers,
            "time": resp.elapsed.total_seconds()
        }
        return formated_response
