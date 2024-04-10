from enum import Enum, auto
from nodes.htmlnode import LeafNode
import re

class TextType(Enum):
    text = ("", "text", "")
    bold = ("**", "bold", "b")
    italic = ("*", "italic", "i")
    code = ("`", "code", "code")
    link = ("[]()", "link", "link")
    image = ("![]()", "image", "image")

    def __init__(self, delim, desc, tag):
        self.delim = delim
        self.desc = desc
        self.tag = tag



class TextNode():
    def __init__(self, type: TextType, text, url=None):
        self.text = text
        self.url = url
        self.type = type

    
    def __eq__(self, other):
        if self.text == other.text and self.type == other.type and self.url == other.url:
            return True
        return False
    def __repr__(self):
        return f'TextNode("{self.text}", {self.type}, {self.url})'
    
    def to_html_node(node):
        create_leaf = lambda tag, value, props=None: LeafNode(tag, value, props)
        if node.type not in TextType:
            raise ValueError(f"Invalid text type: {node.type}")
        
        if node.type in [TextType.text, TextType.bold, TextType.italic, TextType.code]:
            return create_leaf(node.type.tag, node.text)
        elif node.type == TextType.link:
            return create_leaf("a", node.text, {'href': node.url})
        elif node.type == TextType.image:
            return create_leaf("img", "", {'href': node.url, 'alt': node.text})

