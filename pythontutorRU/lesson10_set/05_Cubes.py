# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны
# по цвету. Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
# Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк,
# поэтому вам предлагается помочь им в оставшейся части.
# В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори.
# В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.
# Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков,
# которые есть только у Ани и номера цветов кубиков, которые есть только у Бори.
# Для каждого из множеств выведите сначала количество элементов в нем,
# а затем сами элементы, отсортированные по возрастанию.

a = set([int(a) for a in input('Anya colors: ').split(' ')])
b = set([int(a) for a in input('Boris colors: ').split(' ')])
print(len(a & b), ':', ' '.join([str(a) for a in sorted(a & b)]))
print(len(a - b), ':', *[str(a) for a in sorted(a - b)])
print(len(b - a), ':', *[str(a) for a in sorted(b - a)])