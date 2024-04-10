from nodes.textnode import TextNode, TextType
import re

def split_delim(text, text_type: TextType):
    nodes = []
    split_text = text.split(text_type.delim)  # Splitting text by delimiter
    for i, text in enumerate(split_text):
        if not text: continue  # Skip empty strings
        nodes.append(TextNode(TextType.text if i % 2 == 0 else text_type, text))  # Alternating node types
    return nodes

def extract_md_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)  # Extracting Markdown links

def parse_link_type(text):
    nodes, last_pos = [], 0  # Initialize nodes list and position tracker
    for link_text, url in extract_md_links(text):
        start_pos = text.find(f"[{link_text}]({url})", last_pos)  # Find link start
        if start_pos > last_pos: nodes.append(TextNode(TextType.text, text[last_pos:start_pos]))  # Pre-link text node
        nodes.append(TextNode(TextType.link, link_text, url))  # Link node
        last_pos = start_pos + len(f"[{link_text}]({url})")  # Update position tracker
    if last_pos < len(text): nodes.append(TextNode(TextType.text, text[last_pos:]))  # Post-link text node
    return nodes

def extract_md_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)  # Extracting Markdown images

def parse_image_type(text):
    nodes, last_pos = [], 0  # Initialize nodes list and position tracker
    for alt_text, url in extract_md_images(text):
        start_pos = text.find(f"![{alt_text}]({url})", last_pos)  # Find image start
        if start_pos > last_pos: nodes.append(TextNode(TextType.text, text[last_pos:start_pos]))  # Pre-image text node
        nodes.append(TextNode(TextType.image, alt_text, url))  # Image node
        last_pos = start_pos + len(f"![{alt_text}]({url})")  # Update position tracker
    if last_pos < len(text): nodes.append(TextNode(TextType.text, text[last_pos:]))  # Post-image text node
    return nodes

def text_to_nodes(text):
    nodes = []  # Initialize final nodes list
    for line in text.split("\n"):  # Process each line
        processed = False  # Flag to mark if line has been processed
        for t in TextType:
            if t == TextType.text: continue  # Skip plain text type
            if t == TextType.image and extract_md_images(line):
                nodes.extend(parse_image_type(line))  # Process images
                processed = True
                break
            if t == TextType.link:
                nodes.extend(parse_link_type(line))  # Process links
                processed = True
                break
            if t.delim in line:
                nodes.extend(split_delim(line, t))  # Process delimiter-based types
                processed = True
                break
        if not processed: nodes.append(TextNode(TextType.text, line))  # Handle plain text
    return nodes

def main():
    text = "This is a plain text TextNode\nThis is a **bold** TextNode\nThis is an *italic* TextNode\nThis is a `code` TextNode\nThis is a [link](http://www.google.com) TextNode\nThis is an ![image](http://www.google.com/image.png) TextNode"
    for node in text_to_nodes(text): print(node.to_html_node().to_html())  # Display HTML representation of each node

if __name__ == "__main__":
    main()
