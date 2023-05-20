from mainfile import WikiClient, PlosClient, Worker


def test_worker(monkeypatch):
    execute_counter = 0
    executed_urls = set()

    def mock_make_get_request(*args, **kwargs):
        nonlocal execute_counter
        nonlocal executed_urls
        execute_counter += 1
        executed_urls.add(args[0].base_url)

    monkeypatch.setattr('mainfile.ConcreteBaseClient.make_get_request', mock_make_get_request)  # monkeypatch - подмена

    wiki_url = 'https://test_url_wiki'
    plos_url = 'https://test_url_los'

    wiki_client = WikiClient(wiki_url)
    plos_client = PlosClient(plos_url)

    worker = Worker(wiki_client=wiki_client, plos_client=plos_client)
    worker()

    assert execute_counter == 2
    assert {wiki_url, plos_url} == executed_urls
