def test_main(capsys):
    from python_biocat_rest_api_client import main
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"