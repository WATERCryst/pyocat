from python_biocat_rest_api_client import BiocatRestApiClient


def test_get_state():
    with BiocatRestApiClient('') as client:
        state = client.get_state()
        print(repr(state))
        assert True
