from enum import Enum, auto
from src.nodes.htmlnode import LeafNode

class TextType(Enum):
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"
    

class TextNode():
    def __init__(self, type, text, url=None):
        self.text = text
        self.url = url
        self.type = TextType(type)

    
    def __eq__(self, other):
        if self.text == other.text and self.type == other.type and self.url == other.url:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.type}, {self.url})"
    
def text_node_to_html_node(node: TextNode):
    create_leaf = lambda tag, value, props=None: LeafNode(tag, value, props)
    if node.type not in TextType:
        raise ValueError(f"Invalid text type: {node.type}")
    
    if node.type == TextType.text:
        return create_leaf(None, node.text)
    elif node.type == TextType.bold:
        return create_leaf("b", node.text)
    elif node.type == TextType.italic:
        return create_leaf("i", node.text)
    elif node.type == TextType.code:
        return create_leaf("code", node.text)
    elif node.type == TextType.link:
        return create_leaf("a", node.text, {'href': node.url})
    elif node.type == TextType.image:
        return create_leaf("img", "", {'href': node.url, 'alt': node.text})
    else:
        raise ValueError(f"Invalid text type: {node.type}")
    
def split_nodes_delim(old_nodes, delim, text_type):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        elif delim in node.text:
            text = node.text.split(delim)
            
        else:
            raise ValueError(f"Delimiter {delim} not found in text: {node.text}")
            
    return new_nodes