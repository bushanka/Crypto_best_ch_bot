import pandas as pd


def extract_dat(dat_path):
    data = pd.read_csv(dat_path, encoding='windows-1251')
    return data


if __name__ == '__main__':
    print(extract_dat('D:\\MyDesctopFiles\\business\\Crypto\\BestLoopsBCH\\bch_files\\bm_cy.dat'))
