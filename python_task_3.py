def comper_ins_and_list(new_max_instance, arr):
    for i in range(0, len(arr)):
        new_max_instance = comper_two_ins(new_max_instance, arr[i], arr)
    return new_max_instance

def comper_two_ins(ins1, ins2, arr, k=0):
    if ins1[k] == ins2[k]:
        if len(ins1) > k + 1 and len(ins2) > k + 1:
            return comper_two_ins(ins1, ins2, arr, k + 1)
        elif len(ins1) > k + 1 and len(ins2) <= k + 1:
            a = ins1[k+1:]
            b = arr.copy()
            b.remove(ins1)
            if comper_ins_and_list(a, b) == a:
                return ins1
            return ins2
        elif len(ins1) <= k + 1 and len(ins2) > k + 1:
            a = ins2[k+1:]
            b = arr.copy()
            b.remove(ins2)
            if comper_ins_and_list(a, b) == a:
                return ins2
            return ins1
        else:
            return ins1
    elif ins1[k] > ins2[k]:
        return ins1
    else:
        return ins2

def max_number(arr):
    new = []
    if len(arr) == 0:
        return arr
    while len(arr) > 0:
        new_max_instance = arr[0]
        new_max_instance = comper_ins_and_list(new_max_instance, arr)
        new.append(new_max_instance)
        arr.remove(new_max_instance)
    return new


if __name__ == "__main__":
    arr1 = ['11', '234', '005', '89']
    arr2 = ['551', '55', '23']
    arr3 = ['11', '23', '11', '235']
    result1 = int(''.join(max_number(arr1.copy())))
    result2 = int(''.join(max_number(arr2.copy())))
    result3 = int(''.join(max_number(arr3.copy())))
    print('\nисходный список: ', arr1, '\nрезультат: ', result1)
    print('\nисходный список: ', arr2, '\nрезультат: ', result2)
    print('\nисходный список: ', arr3, '\nрезультат: ', result3)
