import pytest
import requests
import json


class TestEx13:
    user_agent_1 = 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    user_agent_2 = 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'
    user_agent_3 = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    user_agent_4 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'
    user_agent_5 = 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'

    user_agents = [
        user_agent_1,
        user_agent_2,
        user_agent_3,
        user_agent_4,
        user_agent_5
    ]

    @pytest.mark.parametrize('user_agent', user_agents)
    def test_user_agent(self, user_agent):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {"user-agent": user_agent}
        response = requests.get(url, headers=data)
        response_json = json.loads(response.text)

        platform = response_json['platform']
        browser = response_json['browser']
        device = response_json['device']

        if user_agent == self.user_agent_1:
            assert platform == 'Mobile', f"For user_agent_1 field 'platform' is incorrect, must be 'Mobile', but got '{platform}' "
            assert browser == 'No', f"For user_agent_1 field 'browser' is incorrect, must be 'No', but got '{browser}'"
            assert device == 'Android', f"For user_agent_1 field 'device' is incorrect, must be 'Android', but got '{device}'"

        elif user_agent == self.user_agent_2:
            assert platform == 'Mobile', f"For user_agent_2 field 'platform' is incorrect, must be 'Mobile', but got '{platform}'"
            assert browser == 'Chrome', f"For user_agent_2 field 'browser' is incorrect, must be 'Chrome', but got '{browser}'"
            assert device == 'device', f"For user_agent_2 field 'device' is incorrect, must be 'iOS', but got '{device}'"

        elif user_agent == self.user_agent_3:
            assert platform == 'Googlebot', f"For user_agent_3 field 'platform' is incorrect, must be 'Googlebot', but got '{platform}'"
            assert browser == 'Unknown', f"For user_agent_3 field 'browser' is incorrect, must be 'Unknown', but got '{browser}'"
            assert device == 'Unknown', f"For user_agent_3 field 'device' is incorrect, must be 'Unknown', but got '{device}'"

        elif user_agent == self.user_agent_4:
            assert platform == 'Web', f"For user_agent_4 field 'platform' is incorrect, must be 'Web', but got '{platform}'"
            assert browser == 'Chrome', f"For user_agent_4 field 'browser' is incorrect, must be 'Chrome', but got '{browser}'"
            assert device == 'No', f"For user_agent_4 field 'device' is incorrect, must be 'No', but got '{device}'"

        elif user_agent == self.user_agent_5:
            assert platform == 'Mobile', f"For user_agent_5 field 'platform' is incorrect, must be 'Mobile', but got '{platform}'"
            assert browser == 'No', f"For user_agent_5 field 'browser' is incorrect, must be 'No', but got '{browser}'"
            assert device == 'iPhone', f"For user_agent_5 field 'device' is incorrect, must be 'iPhone', but got '{device}'"
