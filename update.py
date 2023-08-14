import os

name = os.environ['NAME']

def update():
    if os.path.exists('./python'):
        os.remove("python")

    import tarfile
    with tarfile.open(name) as f:
        oldname = f.getnames()[0]
        f.extractall('./')
    os.rename(oldname ,"python")
    os.remove(name)

if __name__ == '__main__':
    update()
