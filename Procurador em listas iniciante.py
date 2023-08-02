mochila = ['mochila', 'água', 'papel', 'caneta']
bolsa = ('bolsa', 'lápis', 'caderno', 'livro')
def proc(x):
    it = input('informe o que vc procura: ')

    for item in x:
        if it != item:
            continue
        else:
            print(f'sim, em sua {x[0]} tem {item}')
    if it not in x:
        print(f'este item não consta em sua {x[0]}')

proc(bolsa)
proc(mochila)


