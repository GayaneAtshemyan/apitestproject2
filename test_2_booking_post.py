import requests
import allure


@allure.feature('TEST BOOKING POST - feature')
@allure.suite('TEST BOOKING POST - suite')
class TestBookingPost():

    @allure.title('Test Create Booking')
    @allure.description('This test case verifies that the system successfully create new booking')
    def test_create_booking(self):
        data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(
            'https://restful-booker.herokuapp.com/booking',
            json=data,
            headers=headers
        )
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        response_data = response.json()
        assert 'bookingid' in response_data, "The response does not contain 'bookingid'"

        booking = response_data['booking']
        assert booking['firstname'] == data['firstname'], f"Expected firstname {data['firstname']}, but got {booking['firstname']}"
        assert booking['lastname'] == data['lastname'], f"Expected lastname {data['lastname']}, but got {booking['lastname']}"
        assert booking['totalprice'] == data['totalprice'], f"Expected totalprice {data['totalprice']}, but got {booking['totalprice']}"
        assert booking['depositpaid'] == data['depositpaid'], f"Expected depositpaid {data['depositpaid']}, but got {booking['depositpaid']}"
        assert booking['bookingdates']['checkin'] == data['bookingdates']['checkin'], f"Expected checkin {data['bookingdates']['checkin']}, but got {booking['bookingdates']['checkin']}"
        assert booking['bookingdates']['checkout'] == data['bookingdates']['checkout'], f"Expected checkout {data['bookingdates']['checkout']}, but got {booking['bookingdates']['checkout']}"
        assert booking['additionalneeds'] == data['additionalneeds'], f"Expected additionalneeds {data['additionalneeds']}, but got {booking['additionalneeds']}"