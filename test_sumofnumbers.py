from sumofnumbers import app
import pytest


class Test_0001_total_endpoint(object):
    '''Tests for total endpoint in sumofnumbers API'''

# The below tests that for a normal argument the correct sum is output with 3 examples
    @pytest.mark.parametrize("test_input,expected", [({'numbers_to_add': [1,2,3]}, 6), ({'numbers_to_add': list(range(10))}, 45), ({'numbers_to_add': list(range(10000001))}, 50000005000000)])
    def test_total(self,test_input,expected):        
        response = app.test_client().post(
            '/total',
            json=(test_input),
            content_type='application/json',
        )
        #data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert response.get_json()['total'] == expected

    #The remaining tests check that the correct error handling response is returned...
    #...if numbers_to_add key is not contained in request
    def test_key_not_present(self):        
        response = app.test_client().post(
            '/total',
            json=({'x': [1,2,3]}),
        )

        assert response.status_code == 400
        assert response.get_json()['bad_request'] == "numbers_to_add key missing from JSON"

    #...if the value of numbers_to_add is not a list
    @pytest.mark.parametrize("test_input,expected", [({'numbers_to_add':'x'}, 'format of numbers_to_add value is x but should be e.g. [1,2,3]'), ({'numbers_to_add': 2}, 'format of numbers_to_add value is 2 but should be e.g. [1,2,3]')])
    def test_value_incorrect_format(self,test_input,expected): 
        response = app.test_client().post(
            '/total',
            json=(test_input),
        )
        assert response.status_code == 400
        assert response.get_json()['bad_request'] == expected

    #...if the list contains something other than int or float
    def test_list_contains_incorrect_type(self): 
        response = app.test_client().post(
            '/total',
            json=({'numbers_to_add': [1,'a',3]})
        )
        assert response.status_code == 400
        assert response.get_json()['bad_request'] == "List of numbers contains something other than integer or float"

    #...if the list is less than 1 number 
    def test_list_is_too_small(self): 
        response = app.test_client().post(
            '/total',
            json=({'numbers_to_add': []})
        )
        assert response.status_code == 400
        assert response.get_json()['bad_request'] == "List of numbers contains 1 number or less"

