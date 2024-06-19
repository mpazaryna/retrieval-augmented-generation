import pytest
from utils.jina_basic import fetch_data  # Make sure the name matches the module name

def test_fetch_data_read_mode():
    mode = 'r'
    url = 'https://en.wikipedia.org/wiki/Minimum_viable_product'  # Path for a valid URL
    status_code, response_text = fetch_data(mode, url)
    assert status_code == 200
    assert response_text is not None
    assert "Minimum viable product" in response_text

def test_fetch_data_search_mode():
    mode = 's'
    query = 'what is the latest news on yoga'  # Path for a valid URL
    status_code, response_text = fetch_data(mode, query)
    assert status_code == 200
    assert response_text is not None
    
def test_fetch_data_invalid_url():
    mode = 'r'
    url = 'Invalid_url'

    status_code, response_text = fetch_data(mode, url)
    
    assert status_code != 200

if __name__ == "__main__":
    pytest.main()
