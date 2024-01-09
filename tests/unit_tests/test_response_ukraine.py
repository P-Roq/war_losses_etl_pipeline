import pytest
from scrapy.http import HtmlResponse
from oryx_scrape.spiders.ukrainian_losses_spider import Spider 
from tests.mock_webpage_ukraine import mock_html_oryx_ukraine 

@pytest.fixture
def mock_html_response():
    return HtmlResponse(
        url='https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-ukrainian.html',
        body=mock_html_oryx_ukraine,
        encoding='utf-8'
        )

def test_my_spider(mock_html_response):
    spider = Spider()

    results = list(spider.parse(mock_html_response))[0]

    assert isinstance(results, dict)
   
    assert len(results) == 5
    
    @pytest.mark.parametrize("vehicle_type", [key for key in results.keys()])
    def check_if_each_vehicle_type_exists(vehicle_type):
        assert vehicle_type in results.keys()


    @pytest.mark.parametrize("vehicle_type_container", [results[key] for key in results])
    def check_containers_format(vehicle_type_container):
        assert isinstance(vehicle_type_container, dict) 

        assert isinstance(vehicle_type_container['tank'], int)
        assert isinstance(vehicle_type_container['afv'], int)
        assert isinstance(vehicle_type_container['ifv'], int)
        assert isinstance(vehicle_type_container['apc'], int)
        assert isinstance(vehicle_type_container['imv'], int)