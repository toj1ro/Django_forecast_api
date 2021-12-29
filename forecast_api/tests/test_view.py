from rest_framework.authtoken.admin import User
from rest_framework.test import force_authenticate, APITestCase
from django.test.client import encode_multipart, RequestFactory
from forecast_api.views import ForecastDetail

view = ForecastDetail.as_view()

factory = RequestFactory()

user = User.objects.get(username='asdf')

token = user.auth_token


class TestView(APITestCase):

    def test_valid_request(self):
        request = factory.get('/api/get_city_forecast/?city=Anna&temp_format=C')
        force_authenticate(request, user=user, token=token)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_no_city_parameter(self):
        request = factory.get('/api/get_city_forecast/?temp_format=C')
        force_authenticate(request, user=user, token=token)
        response = view(request)
        self.assertEqual(response.status_code, 400)

    def test_no_temp_format_parameter(self):
        request = factory.get('/api/get_city_forecast/?city=Anna')
        force_authenticate(request, user=user, token=token)
        response = view(request)
        self.assertEqual(response.status_code, 400)

    def test_not_valid_city(self):
        request = factory.get('/api/get_city_forecast/?city=XXXX&temp_format=C')
        force_authenticate(request, user=user, token=token)
        response = view(request)
        self.assertEqual(response.data, {'cod': '404', 'message': 'city not found'})
