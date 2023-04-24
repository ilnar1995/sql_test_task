def numb(num, k=1, n=4):
    result = []
    tokens = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    kol = 0
    for element in num[::k]:
        kol+=1
        if kol > n or element not in tokens:
            break
        if k == -1:
            result = [element] + result
        else:
            result.append(element)
    return result

def convert(numbers):
    n1 = numb(num=numbers[0], k=-1, n=4)
    n2 = numb(num=numbers[1], k=1, n=5)
    if n1 and n2:
        return '{:04}'.format(int(''.join(n1)))+'\\'+'{:05}'.format(int(''.join(n2)))
    else:
        return None

def sersh_spetial_number(arr):
    lst = arr.split(' ')
    new = []
    for s in lst:
        if s.count('\\') == 1:
            numbers = s.split('\\')
            aaaa = convert(numbers)
            if aaaa:
                new.append(aaaa)
    return new

if __name__ == "__main__":
    s = "Адрес 5467\\456. Номер 405\\549"
    result1 = sersh_spetial_number(s)
    print(f"\nИсходный текст: \n   '{s}'")
    if result1:
        print(f"\nСписок особенных номеров: ")
        for r in result1:
            print("   ", r)
    else:
        print(f"\nОсобенных номеров нет ")
