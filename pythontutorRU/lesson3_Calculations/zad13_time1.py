# С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# По данным числам H, M, S определите угол (в градусах),
# на который повернулаcь часовая стрелка с начала суток и выведите его в виде действительного числа.

H = int(input('H: '))
M = int(input('M: '))
S = int(input('S: '))
print(float((360 / 12) * (H + M / 60 + S / 3600)))