class Matrics_transpose:
    def transpose(self, array, rows, column):
        new_array = []
        for i in range(column):
            temp_array = []
            for j in range(rows):
                temp_array.append(array[j][i])
            new_array.append(temp_array)

        return new_array



""" taking the column of the orginal array 
    store in a temp array 
    append that to new array"""

rows = int(input())
column = int(input())

array = []
for i in range(rows):
    a = list(map(int, input().split()))
    array.append(a)

object = Matrics_transpose()


print(object.transpose(array, rows, column))