from python_biocat_rest_api_client import BiocatRestApiClient


key = 'bu97qCvehwJiqDL96x0TTzSnZgqlL2zYw4eVA1D6sbxT3qv2SkRCmDGtoUpM_F1E0rVnkJPzf53GIMZEEwjTuA'


def test_get_state():
    with BiocatRestApiClient(key) as client:
        state = client.get_state()
        assert False, repr(state)
