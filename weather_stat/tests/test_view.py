from django.test import TestCase


class TestView(TestCase):

    def test_valid_request(self):
        response = self.client.get('/api/get_weather_stat/?start_time=2022-12-28T22:50:09&end_time=2022-12-28T22:50:18')
        self.assertEqual(response.status_code, 200)

    def test_no_valid_start_time_request(self):
        response = self.client.get('/api/get_weather_stat/?start_time=XXXX-12-28T22:50:09&end_time=2022-12-28T22:50:18')
        self.assertEqual(response.status_code, 400)

    def test_no_valid_end_time_request(self):
        response = self.client.get('/api/get_weather_stat/?start_time=2022-12-28T22:50:09&end_time=XXXX-12-28T22:50:18')
        self.assertEqual(response.status_code, 400)

    def test_no_start_time(self):
        response = self.client.get('/api/get_weather_stat/?end_time=2022-12-28T22:50:18')
        self.assertEqual(response.status_code, 400)

    def test_no_end_time(self):
        response = self.client.get('/api/get_weather_stat/?start_time=2022-12-28T22:50:09')
        self.assertEqual(response.status_code, 400)
