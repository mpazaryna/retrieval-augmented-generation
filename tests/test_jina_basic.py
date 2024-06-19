import pytest
from utils.jina_basic import fetch_data  # Make sure the name matches the module name

# Test the fetch_data function in read mode with a valid URL
def test_fetch_data_read_mode():
    mode = 'r'
    url = 'https://en.wikipedia.org/wiki/Minimum_viable_product'  # Path for a valid URL
    status_code, response_text = fetch_data(mode, url)
    assert status_code == 200
    assert response_text is not None
    assert "Minimum viable product" in response_text

# Test the fetch_data function in search mode with a valid query
def test_fetch_data_search_mode():
    mode = 's'
    query = 'what is the latest news on yoga'  # Path for a valid URL
    status_code, response_text = fetch_data(mode, query)
    assert status_code == 200
    assert response_text is not None
    
# Test the fetch_data function with an invalid URL
def test_fetch_data_invalid_url():
    mode = 'r'
    url = 'Invalid_url'

    status_code, response_text = fetch_data(mode, url)
    
    assert status_code != 200

# Test the fetch_data function with an invalid mode input
# def test_fetch_data_invalid_mode():
    #mode = 'invalid'
    #input_data = 'test'

    #with pytest.raises(ValueError) as excinfo:
    #    fetch_data(mode, input_data)
    #assert str(excinfo.value) == "Invalid mode. Please enter 'r' or 's'."

def test_invalid_mode():
    mode = 'x'  # Invalid mode
    url_or_query = "test"  # Dummy value for url_or_query
    expected_output = "invalid input"
    
    result = fetch_data(mode, url_or_query)
    print(result)
    assert result == expected_output, f"Expected '{expected_output}', but got '{result}'"
