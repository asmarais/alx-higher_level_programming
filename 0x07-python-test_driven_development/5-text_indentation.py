def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    separators = ['.', '?', ':']
    lines = []
    line = ''
    
    for char in text:
        line += char
        if char in separators:
            lines.append(line.strip())
            line = ''
    
    if line:
        lines.append(line.strip())
    
    for line in lines:
        print(line)
        print()
