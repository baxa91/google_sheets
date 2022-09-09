from sheets import GoogleSheet


def main():
    gs = GoogleSheet()
    print(gs.get_title()[0][1])


if __name__ == '__main__':
    main()
