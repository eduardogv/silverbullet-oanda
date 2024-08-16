import os


def get_his_data_filename(pair, granularity):
    path = os.path.join("his_data", f"{pair}_{granularity}.pkl")
    return path

def get_instruments_data_filename():
    return "instruments.pkl" #retorna el nombre del archivo que guardaremos

if __name__ == "__main__":
    print (get_his_data_filename("EUR_USD", "H1"))
    print (get_instruments_data_filename())