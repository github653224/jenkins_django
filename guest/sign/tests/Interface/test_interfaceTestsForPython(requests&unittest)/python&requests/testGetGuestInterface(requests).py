# -*- coding:utf-8 -*-
import sys
import requests
import json

reload(sys)
sys.setdefaultencoding('utf-8')


class GuestInterface:
    def __init__(self, url, paramdict):
        self.url = url
        self.param = paramdict

    def testGetGuesttInterface(self):
        print "test start..."
        response = requests.get(self.url, params=self.param)
        result = response.json()
        # {u'status': 200, u'message': u'success', u'data': [{u'phone': u'15210142165', u'email': u'jack1@qq.com', u'realname': u'jack1', u'sign': True}]}
        assert result['status'] == 200
        assert result['message'] == "success"
        if type(result['data']) is dict:
            assert (result['data']['realname']) == "jack1"
            assert result['data']['phone'] == "15210142165"
            assert result['data']['email'] == "jack1@qq.com"
            assert result['data']['sign'] is True

        elif type(result['data']) is list:
            for guest_number in range(len(result['data'])):
                print result['data'][guest_number]
                assert (result['data'][guest_number]['realname']) in ("jack2", "jack1")
                assert result['data'][guest_number]['phone'] in ("15210142165", "15210142166")
                assert result['data'][guest_number]['email'] in ("jack1@qq.com", "jack2@qq.com")
                assert result['data'][guest_number]['sign'] in (True, False)
        print "test done"


if __name__ == "__main__":
    url = "http://127.0.0.1:9000/api/get_guest_list/"
    paramdict={
        "eid": "25",
        "phone": "15210142165"
    }
    event = GuestInterface(url,paramdict)
    event.testGetGuesttInterface()
