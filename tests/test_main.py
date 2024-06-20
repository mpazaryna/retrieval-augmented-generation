import os
import pytest
from utils.utils_pinecone import initialize_chain, get_response

@pytest.fixture
def setup_chain():
    return initialize_chain()

def test_get_response_minimum_viable_products(setup_chain):
    response = get_response(setup_chain, "what are minimum viable products?")
    assert "minimum viable product" in response.lower()

def test_get_response_product_company_gap(setup_chain):
    response = get_response(setup_chain, "what is the product company gap and how can it be solved?")
    assert "product company gap" in response.lower()
