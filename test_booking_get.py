import requests


def test_get_all_bookings():
    response = requests.get('https://restful-booker.herokuapp.com/booking')
    assert response.status_code == 200
    for i in range(len(response.json())):
        assert response.json()[i]["bookingid"] >0

# def test_get_one_booking():
#     response = requests.get('https://restful-booker.herokuapp.com/booking/2659')
#     assert response.status_code == 200
#     assert response.json()["firstname"] == "John"
#     assert response.json()["bookingdates"]["checkin"] == "2018-01-01"
#

def test_create_booking():
    #creare user
    booking_details = {
    "firstname" : "testcurs34657567-34",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post('https://restful-booker.herokuapp.com/booking', json = booking_details)
    print(response.text)
    #verificam userul ce l-am creat
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == "testcurs34657567-34"
    #facem un get pe userul ce l-am creat sa vedem daca apare in baza de date si apare corect
    url_get = "https://restful-booker.herokuapp.com/booking/" + str(response.json()["bookingid"])
    response_get = requests.get(url_get)
    assert response_get.json()["firstname"] == "testcurs34657567-34"