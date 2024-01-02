import sim, random
import json
def lookup(J):
    with open("lookup.json", 'r') as f:
        lookup = json.load(f)
    if 9800<J<32000:
        J = float(J - J%200 + (0 if J%200<110 else 200))
    else:
        return [0.12,0.6]
    return random.choice(lookup[str(J)])
if __name__=="__main__":
    J = 7000
    [Kp, Kd] = lookup(J)
    sim.main(Kp=Kp, Kd=Kd, J= J, showGraph=True)







# J = {}
# for i in range(101):
#     J[int(10000+200*i)] = i
# # l =[[18.0]]*10
# # l[2]=[17.0]
# # if l[]
# # print(round(9.5,4))

# minJ = [[18.0]]*len(J)
# dupliCount = {}
# updationCount = 0
# data = [_ for _ in mlcdataIterator]
# # print(len(data),len(data[0]))
# # data = sorted(data, key = lambda l: float(l[8]))
# # cw.writerows(data)

# for row in data:
#     #if sT<17 and int(row[1])==0 and float(row[2])<4.0:# and float(float(row[8]))==22000.0:
#     sT = round(float(row[0]),4)
#     if sT<float(minJ[J[int(float(row[8]))]][0]):
#         #print("ST reduced from", minJ[J[int(float(row[8]))]][0]," to ", sT)
#         minJ[J[int(float(row[8]))]] = row
#         updationCount+=1
# for row in data:
#     sT = round(float(row[0]),4)
#     if sT==float(minJ[J[int(float(row[8]))]][0]) and round(float(row[6]),4)!=round(float(minJ[J[int(float(row[8]))]][6]),4) and round(float(row[7]),4)!=round(float(minJ[J[int(float(row[8]))]][7]),4) and int(float(row[8]))==int(float(minJ[J[int(float(row[8]))]][8])):
#         if float(row[8])==10400.0:
#             print(round(float(row[7]),4), round(float(minJ[J[int(float(row[8]))]][7]),4))
#         dupliCount[sT]= dupliCount.get(sT, 0)+1
#         minJ.append(row)
# minJ = sorted(minJ, key = lambda l: float(l[8]))
# for i in range(len(minJ)):
#     cw.writerow(minJ[i])
#     count+=1 


# print(count, "rows shortlisted")
# print(updationCount, "updations count for min")
# print("Duplicount ",sum(dupliCount.values()))
# print(dupliCount)
# # J.sort()
# # maxm = 0
# # for i in range(1,len(J)):
# #     maxm= max(maxm, J[i]-J[i-1])
# # print("Max gap in J ", maxm)

