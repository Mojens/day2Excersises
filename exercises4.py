s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'

print(len(s)) # With spaces

print(len(s.replace(' ', ''))) # Without spaces

print(len(s.split())) #only words