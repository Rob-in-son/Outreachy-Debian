import unittest
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
from wiki_news import *  
class TestWebScraperFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_html_success(self, mock_get):
        mock_response = Mock()
        mock_response.text = '<html></html>'
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response
        result = fetch_html('http://test.com')
        self.assertEqual(result, '<html></html>')

    @patch('requests.get')
    def test_fetch_html_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException
        result = fetch_html('http://test.com')
        self.assertIsNone(result)

    def test_correct_relative_links(self):
        soup = BeautifulSoup('<a href="/test"></a>', 'html.parser')
        correct_relative_links(soup)
        self.assertEqual(soup.a['href'], 'https://wiki.debian.org/test')

    def test_convert_html_to_markdown(self):
        soup = BeautifulSoup('<strong>bold</strong>', 'html.parser')
        result = convert_html_to_markdown(soup)
        self.assertEqual(result, '**bold**')

    def test_remove_div(self):
        soup = BeautifulSoup('<div>More Actions: test</div><div>Other text</div>', 'html.parser')
        remove_div(soup, "More Actions:")
        self.assertIsNone(soup.find(string="More Actions: test"))
        self.assertIsNotNone(soup.find(string="Other text"))

    @patch('builtins.open', unittest.mock.mock_open())
    def test_write_to_file(self):
        write_to_file("test content", "test.md")
        open.assert_called_with("test.md", 'w', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
