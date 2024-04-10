class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("To be implemented by subclasses")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)
        
    def to_html(self):
        if self.tag is None:
            return self.value
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag == "img":
            return f'<{self.tag}{self.props_to_html()}>'
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children=children, props=props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
    
    