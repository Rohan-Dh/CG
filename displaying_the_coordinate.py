# lab - 1

import matplotlib.pyplot as plt
x = float(input("Enter the x co-ordinate: "))
y = float(input("Enter the y co-ordinate: "))

print("Name = Rohan Dhungana")
print("Rollno = 07")
plt.plot(x, y, marker='o')
plt.show()

# import matplotlib.pyplot as plt
# x_co, y_co = map(float, input("Enter the x and y co-ordinate respectively: ").split())

# plt.plot(x_co, y_co, marker=".")
# plt.show()




# lab - 2
# import matplotlib.pyplot as plt

# x1, y1 = map(float, input("Enter the starting co-ordinate of the line: ").split())
# x2, y2 = map(float, input("Enter the ending co-ordinate of the line: ").split())

# rou_x1 = round(x1)
# rou_y1 = round(y1)

# dx = x2 - x1
# dy = y2 - y1

# if dy>dx:
#     steps = dy
# else:
#     steps = dx

# xincr = dx/float(steps)
# yincr = dy/float(steps)

# x_list = [x1]
# y_list = [y1]

# plt.plot(x1, y1,"o")
# print("x\ty\tx-plot\ty-plot\t(x, y)")

# print(f"{x1:.2f}\t{y1:.2f}\t{rou_x1}\t{rou_y1}\t({rou_x1},{rou_y1})")

# for i in range(0, int(steps)):
    
#     x1 = x1 + xincr
#     x_list.append(x1)
#     y1 = y1 + yincr
#     y_list.append(y1)
    
#     rou_x1 = round(x1)
#     rou_y1 = round(y1)
#     plt.plot(rou_x1, rou_y1, marker="o")
#     print(f"{x1:.2f}\t{y1:.2f}\t{rou_x1}\t{rou_y1}\t({rou_x1},{rou_y1})")
    
# print("Name = Rohan Dhungana")
# print("Rollno = 07")
# plt.plot(x_list, y_list)
# plt.show()
# plt.close()




# # lab-3
# import matplotlib.pyplot as plt
# x1, y1 = map(float, input("Enter the first co-ordinate: ").split())
# x2, y2 = map(float, input("Enter the second co-ordinate: ").split())

# dx = abs(x2 - x1)
# dy = abs(y2 - y1)

# x_nex = x1
# y_nex = y1

# x_list=[x1]
# y_list=[y1]

# slope = abs((y2-y1)/(x2-x1))
# i = 1;

# print("k\tpk\t(x(K+1),y(k+1))")

# if slope <= 1:
#     p = 2*dy - dx
#     while(x_nex<x2 and y_nex<y2):
#         print(i,"\t", p, "\t", end=" ")
#         x_nex +=1
#         if p<0:
#             p += 2*dy
#         else:
#             y_nex += 1
#             p += (2*dy- 2*dx)
#         print(f"{(x_nex,y_nex)}")
#         i+=1
#         x_list.append(x_nex)
#         y_list.append(y_nex)
# else:
#     p = 2*dx - dy
#     while(x_nex<x2 and y_nex<y2):
#         print(i,"\t", p, "\t", end=" ")
#         y_nex += 1
#         if p<0:
#             p += 2*dx
#         else:
#             x_nex += 1
#             p += (2*dx - 2*dy)
        
#         i+=1
#         print(f"{(x_nex,y_nex)}")
#         x_list.append(x_nex)
#         y_list.append(y_nex)

# print("Name = Rohan Dhungana")
# print("Rollno = 07")
# plt.plot(x_list, y_list, marker= 'o')
# plt.show()




# Lab - 4
# import matplotlib.pyplot as plt

# def find_symmetry(nex_x, nex_y, center_x, center_y):
#     print(f"({nex_y+center_x},{nex_x+center_y})",end=" ")
#     plt.plot(nex_y+center_x, nex_x+center_y, '.', color='red')
#     print(f"\t({nex_x+center_x},{nex_y+center_y})",end=" ")
#     plt.plot(nex_x+center_x, nex_y+center_y, '.', color='red')
#     print(f"\t({nex_x+center_x},{-nex_y+center_y})",end=" ")
#     plt.plot(nex_x+center_x, -nex_y+center_y, '.', color='red')
#     print(f"\t({nex_y+center_x},{-nex_x+center_y})",end=" ")
#     plt.plot(nex_y+center_x, -nex_x+center_y, '.', color='red')
#     print(f"\t({-nex_y+center_x},{-nex_x+center_y})",end=" ")
#     plt.plot(-nex_y+center_x, -nex_x+center_y, '.', color='red')
#     print(f"\t({-nex_x+center_x},{-nex_y+center_y})",end=" ")
#     plt.plot(-nex_x+center_x, -nex_y+center_y, '.', color='red')
#     print(f"\t({-nex_x+center_x},{nex_y+center_y})",end=" ")
#     plt.plot(-nex_x+center_x, nex_y+center_y, '.', color='red')
#     print(f"\t({-nex_y+center_x},{nex_x+center_y})")
#     plt.plot(-nex_y+center_x, nex_x+center_y, '.', color='red')

# radius = float(input("Enter the radius of the cirlce: "))
# center_x, center_y = map(float, input("Enter the co-ordinate of center of the circle: ").split())
# plt.plot(center_x, center_y, marker='o')

# nex_x = 0
# nex_y = radius

# p = 1 - radius
# k = 0
# print("k\tp\t2x(k+1)\t2y(k+1)\t1st\t\t2nd\t\t3rd\t\t4th\t\t5th\t\t6th\t\t7th\t\t8th")
# print(f"{k}\t{p}\t{2*nex_x}\t{2*nex_y}\t", end="")
# find_symmetry(nex_x, nex_y, center_x, center_y)

# while(nex_x<nex_y):
#     k+=1
#     nex_x +=1
#     if(p<0):
#         p += 2*nex_x +1
#     else:
#         nex_y -=1
#         p+=2*nex_x +1 -2*nex_y
    
#     print(f"{k}\t{p}\t{2*nex_x}\t {nex_y}\t", end="")    
#     find_symmetry(nex_x, nex_y, center_x, center_y)
    
# print("Name = Rohan Dhungana")
# print("Rollno = 07")
# plt.show()
# plt.close()




# Lab - 5
# import matplotlib.pyplot as plt

# def find_symmetry(nex_x, nex_y, cen_x, cen_y):
#     plt.plot(nex_x+cen_x, nex_y+cen_y, marker=".")
#     plt.plot(-nex_x+cen_x, nex_y+cen_y, marker=".")
#     plt.plot(-nex_x+cen_x, -nex_y+cen_y, marker=".")
#     plt.plot(nex_x+cen_x, -nex_y+cen_y, marker=".")
    
# def display(nex_x, nex_y, cen_x, cen_y):
#     print(f"\t({nex_x+cen_x},{nex_y+cen_y})",end="  ")
#     print(f"({-nex_x+cen_x},{nex_y+cen_y})",end="   ")
#     print(f"({-nex_x+cen_x},{-nex_y+cen_y})",end="    ")
#     print(f"({nex_x+cen_x},{-nex_y+cen_y})")
    
# cen_x, cen_y = map(float, input("Enter the center co-ordinate: ").split())
# plt.plot(cen_x, cen_y, marker=".")
# rx, ry = map(float, input("Enter the x and y-radius of ellipse: ").split())

# nex_x = 0
# nex_y = ry

# print('\nFor region 1')
# # for first region
# p1=(ry*ry)-(rx*rx*ry)+(rx*rx*0.25)
# k = 0

# print('Iteration\tp\t(xk+1,yk+1)\t(x,y)\t(-x,y)\t (-x,-y)   (x,-y)')

# while ((2*ry*ry*nex_x)<(2*rx*rx*nex_y)):
#     nex_x += 1
#     k+=1
#     if p1<0:
#         p1=p1+(2*ry*ry*nex_x)+(ry*ry)
#     else:
#         nex_y -= 1
#         p1=p1+(2*ry*ry*nex_x)-(2*rx*rx*nex_y)+(ry*ry)
        
#     print(f"{k}\t\t{int(p1)}\t({int(nex_x)},{int(nex_y)})",end="\t")
#     find_symmetry(nex_x, nex_y, cen_x, cen_y)
#     display(int(nex_x), int(nex_y), int(cen_x), int(cen_y))


# print("\nFor Region 2")
# print('Iteration\tp\t(xk+1,yk+1)\t(x,y)\t(-x,y)\t(-x,-y)\t(x,-y)')
# # for second region
# p1 = (ry*ry*(nex_x+0.5)*(nex_x+0.5))+(rx*rx*(nex_y-1)*(nex_y-1))-(rx*rx*ry*ry)
# k = 0
# while nex_y>=0:
#     nex_y -= 1
#     k+=1
#     if p1>0:
#         p1=p1-(2*rx*rx*(nex_y))+(rx*rx)
#     else:
#         nex_x+=1
#         p1=p1+(2*ry*ry*(nex_x))-(2*rx*rx*nex_y)+(rx*rx)
    
#     print(f"{k}\t\t{p2}\t({int(nex_x)},{int(nex_y)})",end="\t")
#     find_symmetry(nex_x, nex_y, cen_x, cen_y)
#     display(int(nex_x), int(nex_y), int(cen_x), int(cen_y))

# print("Name = Rohan Dhungana")
# print("Rollno = 07")
# plt.show()
# plt.close()