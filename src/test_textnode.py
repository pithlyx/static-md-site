import unittest
from nodes.textnode import text_node_to_html_node, TextNode, TextType
from nodes.htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            TextNode(type='invalid', text='Hello, world!')
    
    def test_text_node_to_html_node(self):
        text_text_node = TextNode(type=TextType.text, text='Hello, world!')
        self.assertEqual(text_node_to_html_node(text_text_node).to_html(), 'Hello, world!')
        bold_text_node = TextNode(type=TextType.bold, text='Hello, world!')
        self.assertEqual(text_node_to_html_node(bold_text_node).to_html(), '<b>Hello, world!</b>')
        italic_text_node = TextNode(type=TextType.italic, text='Hello, world!')
        self.assertEqual(text_node_to_html_node(italic_text_node).to_html(), '<i>Hello, world!</i>')
        code_text_node = TextNode(type=TextType.code, text='print("Hello, world!")')
        self.assertEqual(text_node_to_html_node(code_text_node).to_html(), '<code>print("Hello, world!")</code>')
        link_text_node = TextNode(type=TextType.link, text='GitHub', url='https://github.com')
        self.assertEqual(text_node_to_html_node(link_text_node).to_html(), '<a href="https://github.com">GitHub</a>')
        image_text_node = TextNode(type=TextType.image, text='GitHub Logo', url='https://github.com/logo.png')
        self.assertEqual(text_node_to_html_node(image_text_node).to_html(), '<img href="https://github.com/logo.png" alt="GitHub Logo">')
        
    
if __name__ == '__main__':
    unittest.main()