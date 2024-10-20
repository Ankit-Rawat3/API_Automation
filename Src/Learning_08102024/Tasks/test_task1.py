import pytest
import allure
import requests

# Testcases of get booking request api
req_url = "https://restful-booker.herokuapp.com/booking/"


# ===========================================================================================
@pytest.mark.smoke
@allure.title("TC_01: Verify if with valid booking id user is able to fetch booking details")
@allure.description("Details of booking shall be displayed as per the input given from user")
@allure.severity("Major")
def test_get_booking_valid_bookingid_p():
    response = requests.get(url=req_url + "1")
    print("\n",response.status_code)
    assert response.status_code == 200


# ===========================================================================================
# This testcase is failed to check how it get reported in allure report
@pytest.mark.smoke
@allure.title("TC_02: Verify if with invalid booking id user is able to fetch booking details")
@allure.description("Details of booking shall not be displayed as per the input given from user")
@allure.severity("Critical")
def test_get_booking_invalid_bookingid_n():
    response = requests.get(url=req_url + "9999")
    print("\n", response.status_code)
    assert response.status_code == 200


# ===========================================================================================
@pytest.mark.smoke
@allure.title("TC_03: Verify if with invalid booking id user is able to fetch booking details")
@allure.description("Details of booking shall not be displayed as per the input given from user")
@allure.severity("Medium")
def test_get_booking_invalid_bookingid_alphanumeric_n():
    response = requests.get(url=req_url + "xyz123")
    print("\n", response.status_code)
    assert response.status_code == 404


# ===========================================================================================
@pytest.mark.regression
@allure.title("TC_04: Verify if with invalid booking id user is able to fetch booking details")
@allure.description("Details of booking shall not be displayed as per the input given from user")
@allure.severity("Major")
def test_get_booking_invalid_bookingid_specialchar_n():
    response = requests.get(url=req_url + "@#$%")
    print("\n", response.status_code)
    assert response.status_code == 404


# ===========================================================================================
@pytest.mark.sanity
@allure.title("TC_05: Verify if with invalid booking id user is able to fetch booking details")
@allure.description("Details of booking shall not be displayed as per the input given from user")
@allure.severity("Minor")
def test_get_booking_invalid_bookingid_alphabets_n():
    response = requests.get(url=req_url + "abc")
    print("\n", response.status_code)
    assert response.status_code == 404

# ===========================================================================================

@pytest.mark.sanity
@allure.title("TC_06: Verify if with invalid booking id user is able to fetch booking details")
@allure.description("Details of booking shall not be displayed as per the input given from user")
@allure.severity("Minor")
def test_get_booking_invalid_bookingid_hexcode_n():
    response = requests.get(url=req_url + "0X28872h")
    print("\n", response.status_code)
    assert response.status_code == 200
# ===========================================================================================
@pytest.mark.sanity
@allure.title("TC_07: Verify if with invalid booking id user is able to fetch booking details")
@allure.description("Details of booking shall not be displayed as per the input given from user")
@allure.severity("Minor")
def test_get_booking_invalid_bookingid_asPhonenumber_n():
    response = requests.get(url=req_url + "8553962594")
    print("\n", response.status_code)
    assert response.status_code == 200
# ===========================================================================================

@pytest.mark.sanity
@allure.title("TC_08: Verify if with invalid booking id user is able to fetch booking details")
@allure.description("Details of booking shall not be displayed as per the input given from user")
@allure.severity("Minor")
def test_get_booking_invalid_bookingid_as_mail_n():
    response = requests.get(url=req_url + "king@gmail.com")
    print("\n", response.status_code)
    assert response.status_code == 200
