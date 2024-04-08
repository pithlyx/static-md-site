from nodes.textnode import TextNode
from nodes.htmlnode import ParentNode, LeafNode


def main():
    # create dummy text node objects for testing (text, type, url=optional)
    text_nodes = [ 
                  TextNode("Normal Text", "text"),
                  TextNode("Bold Text", "bold"),
                  TextNode("Italic Text", "italic"),
                  TextNode("Code Text", "code"),
                  TextNode("Link Text", "link", "https://www.example.com"),
                  TextNode("Image Text", "image", "https://www.example.com/image.jpg"),
    ]
    # print the text node objects
    for node in text_nodes:
        print(node)
    
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    
    print(node)
    print(node.to_html())
if __name__ == "__main__":
    main()