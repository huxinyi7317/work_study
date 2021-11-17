def filebaocun(filepath,nr):
    with open(filepath,'wb',encoding='utf-8') as f:
        f.write(nr)

def fileduqu(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        data = f.read()
    return data

