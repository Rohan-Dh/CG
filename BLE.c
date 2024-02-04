import matplotlib.pyplot as plt x1, y1 = map(float, input("Enter the first co-ordinate: ").split())
                                                              x2,
                                                          y2 = map(float, input("Enter the second co-ordinate: ").split())

                                                                              dx = x2 - x1 dy = y2 - y1

                                                                   if abs (dx)> abs(dy) :steps = dx else :steps = dy

                                                                   x_nex = x1 y_nex = y1

                                                                   x_list =[x1] y_list =[y1]

                                                                   slope = abs((y2 - y1) /(x2 - x1))
                                                                       i = 1;

print("k\tpk\t(x(K+1),y(k+1))")

print(f"{dx}\t{dy}")

if slope <= 1:
    p = 2*abs(dy) - abs(dx)
    for x in range(0, int(steps)):
        print(i,"\t", p, "\t", end=" ")
        x_nex +=1
        if p<0:
            p += 2*abs(dy)
        else:
            y_nex -= 1
            p += (2*abs(dy)- 2*abs(dx))
        print(f"{(x_nex,y_nex)}")
        i+=1
        x_list.append(x_nex)
        y_list.append(y_nex)
else:
    p = 2*abs(dx) - abs(dy)
    for x in range(0, int(steps)):
        print(i,"\t", p, "\t", end=" ")
        y_nex += 1
        if p<0:
            p += 2*abs(dx)
        else:
            x_nex += 1
            p += (2*abs(dx) - 2*abs(dy))
        
        i+=1
        print(f"{(x_nex,y_nex)}")
        x_list.append(x_nex)
        y_list.append(y_nex)

print(x_list)
print(y_list)
plt.plot(x_list, y_list, marker= 'o')
plt.show()