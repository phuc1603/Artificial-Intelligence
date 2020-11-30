import random
import math
import time
from copy import deepcopy
# Them cac thu vien neu can

def initState(orders, nStaffs):
    staffs = {}
    for i in range(int(nStaffs)):
        staffs[i] = {}
    for i in range(len(orders)):
        idxStaff = random.sample(range(int(nStaffs)),1)[0]
        staffs[idxStaff].update({i: orders[i]})
    return staffs

def constFunc(staffs, orders, warehousePos):
    heuristic_result = 0
        
    listLoiNhuan = []
    for i in range(len(staffs)):
        posPre = warehousePos
        if not len(staffs[i]):
            return 99999999999

        doanhThu = 0
        chiPhi = 0
        for key in staffs[i]:
            doanhThu += 5 + int(staffs[i][key]['size']) + int(staffs[i][key]['weight'])*2

            chiPhi += math.sqrt((int(posPre[0])-int(staffs[i][key]['pos'][0]))**2 + (int(posPre[1])-int(staffs[i][key]['pos'][1]))**2)
            posPre = staffs[i][key]['pos']
        chiPhi = chiPhi*20/40 + 10
        listLoiNhuan.append(doanhThu - chiPhi)

    for i in range(len(listLoiNhuan)-1):
        for j in range(i+1, len(listLoiNhuan)):
            heuristic_result += abs(listLoiNhuan[i] - listLoiNhuan[j])
        
    return heuristic_result

def simulatedAnnealing(orders, nStaffs, warehousePos):
    global startTime
    temperature = 4000*len(orders)
    alpha = 0.99
    current_state = initState(orders, nStaffs)
    current_cost = constFunc(current_state, orders, warehousePos)
    temp1 = 99999999999
    temp2 = {}

    while time.time() - startTime < 60:
        temperature *= alpha
        next_state = initState(orders, nStaffs)
        next_cost = constFunc(next_state, orders, warehousePos)
        delta_E = next_cost - current_cost

        if delta_E < 0 or random.uniform(0, 10) < math.exp(-delta_E / temperature):
            current_state = next_state
            current_cost = constFunc(current_state, orders, warehousePos)

        if current_cost < temp1:
            temp1 = current_cost
            temp2 = current_state

    result = ''
    for i in temp2:
        line = ''
        for key in temp2[i]:
            line += str(key) + ' '
        result += line.strip() + '\n'
        
    with open('output.txt', 'w') as file:
        file.write(result)
        

def assign(file_input, file_output):
    warehousePos = []
    nOrders = ''
    nStaffs = ''
    orders = {}
    staffs = {}
    with open(file_input, 'r') as file:
        warehousePos = file.readline().split(' ')
        nOrders, nStaffs = file.readline().split(' ')
        idx = 0
        line = file.readline()
        while line:
            line = line.split(' ')
            orders[idx] = {'pos': [line[0], line[1]], 'size': line[2], 'weight': line[3].strip()}
            line = file.readline()
            idx += 1
    # ================================================
    simulatedAnnealing(orders, nStaffs, warehousePos)
    return

startTime = time.time()
assign('input.txt', 'output.txt')