#-*- coding: utf-8 -*-

def run():
    with open('numeros.txt', 'w') as f: # python crea el archivo y no esta
        for i in range(10):
            f.write(str(i))




if __name__ == "__main__":
    run()