from feather_simple_api.resources.providers.provider_dto import ProviderDto
from feather_simple_api.resources.providers.provider import Provider

complete_data = {
    "name": "Life Insurance",
    "price": 30.5,
    "billing_period": "monthly",
    "for_occupation": "employed",
}


def test_new_provider_model():
    provider = Provider(**complete_data)

    assert provider.name == complete_data["name"]
    assert provider.price == complete_data["price"]
    assert provider.billing_period == complete_data["billing_period"]
    assert provider.for_occupation == complete_data["for_occupation"]


def test_new_provider_dto():
    provider = ProviderDto(**complete_data)

    assert provider.name == complete_data["name"]
    assert provider.price == complete_data["price"]
    assert provider.billing_period == complete_data["billing_period"]
    assert provider.for_occupation == complete_data["for_occupation"]
