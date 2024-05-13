from lvl1_12 import morph_analyze
from lvl1_10 import build


def main():
    poses = [pos.POS for pos in morph_analyze().values() if pos.POS]
    build(poses)


if __name__ == '__main__':
    main()
