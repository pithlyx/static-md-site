import re

link_pattern = r"[^!]\[(.*?)\]\((.*?)\)"
image_pattern = r"!\[(.*?)\]\((.*?)\)"
text = "This is a [link](https://www.google.com) and this is an ![image](https://www.google.com)"


tokenized_text = re.sub(image_pattern, r"[alt=\1 , href=\2]", text)
print(tokenized_text)