from pathlib import Path
def get_filepath():
    p = Path(__file__)
    return str(p.parent)

if __name__ == '__main__':
    print(f'{get_filepath()}/res/logo.jpeg')