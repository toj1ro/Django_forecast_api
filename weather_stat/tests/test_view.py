import pytest


@pytest.mark.django_db
@pytest.mark.parametrize(
    'start_time, end_time', [
        ('2000-12-01T21:13:11', '2000-12-01T21:15:11'),
        ('2001-10-21T10:45:21', '2002-04-15T13:32:54'),
        ('2004-05-12T04:32:10', '2004-06-12T10:42:12')
    ])
def test_get_weather_stat_valid_data(start_time, end_time, client):
    data = {'start_time': start_time,
            'end_time': end_time}

    response = client.get('/api/get_weather_stat/', data=data)

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_weather_stat_without_start_time(client):
    response = client.get('/api/get_weather_stat/?start_time=&end_time=2004-05-12T04:32:10', )
    error_message = response.json()
    assert error_message == {"start_time": [{"message": "This attribute is required", "code": "required"}]}
    assert response.status_code == 400

@pytest.mark.django_db
def test_get_weather_stat_without_end_time(client):
    response = client.get('/api/get_weather_stat/?start_time=2004-05-12T04:32:10&end_time=', )
    error_message = response.json()
    assert error_message == {"end_time": [{"message": "This attribute is required", "code": "required"}]}
    assert response.status_code == 400

@pytest.mark.django_db
def test_get_weather_stat_not_valid_start_time(client):
    response = client.get('/api/get_weather_stat/?start_time=XUI-05-12T04:32:10&end_time=2004-05-12T04:32:10', )
    error_message = response.json()
    assert error_message == {"start_time": [{
                                                "message": "The requested date and/or time have an incorrect format. The correct format should be YYYY-MM-DDTHH:MM:SS",
                                                "code": "invalid"}]}
    assert response.status_code == 400

@pytest.mark.django_db
def test_get_weather_stat_not_valid_end_time(client):
    response = client.get('/api/get_weather_stat/?start_time=2001-05-12T04:32:10&end_time=XUI-05-12T04:32:10', )
    error_message = response.json()
    assert error_message == {"end_time": [{
                                                "message": "The requested date and/or time have an incorrect format. The correct format should be YYYY-MM-DDTHH:MM:SS",
                                                "code": "invalid"}]}
    assert response.status_code == 400

