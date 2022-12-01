from tkinter import *
from tkinter import messagebox as mb
from math import inf
application = Tk() # Создание окна
application.geometry(f"860x860+310+0") # Размер окна и его расположение
application.resizable(0, 0) #Запрет на изменение размера окна
application.wm_attributes('-topmost', 1) # Окно всегда сверху

canvas = Canvas(application, bg="white", width=856, height=726) # Создание холста

canvas.place(x=0, y=120)
application.title("работа с графами")

label = Label(application) # Создание метки
label.place(x=370, y=125) # Расположение метки
label["text"] = "Имя графа" # Текст метки

global color_vertices_line#для хранения цвета вершин и рёбер
global name_vertex#имя вершины
array_name_vertex = []#массив имен вершин
all_name_garphs = []#для имён графа 

date_vertex_id_X_Y = dict()#словарь для хранения ID рёбер  их координат и имени
global ID# id вершин
ID = 0
#array_all_ID = []


global non_oriented_line#что-то типо счётчика
non_oriented_line = 0
global ID_none_oriented_line# ID для неоринтированных рёбер
ID_none_oriented_line = 0
date_ID_nonorient_line_X_Y = dict()#словарь для хранения ID неориентированных рёбер и для имён и координат вершин с которыми они соединены
global count_unoriented_line#количесвто рёбер
count_unoriented_line = 0

global oriented_line#что-то типо счётчика
oriented_line = 0
global ID_oriented_line# ID для оринтированных рёбер
ID_oriented_line = 0
date_ID_orient_line_X_Y = dict()#словарь для хранения ID ориентированных рёбер и для имён и координат вершин с которыми они соединены


temp_edges = []#список ребёр
global max_node#максимальная степень вершины
max_node = 0
nodes = []#список всех вершин
weight = []
global UNORIN_ORIENT#булевая переменная для проверки на ориентированность графа
UNORIN_ORIENT = 0#если = 0 то граф неориентированный


global result_adjancy_matrix,result_incidency_matrix #матрица смежности
result_adjancy_matrix = []
result_incidency_matrix = []#матрица инцидентности


application.update()
def draw_vertixes():#рисование вершин
    canvas.bind_all("<Button-1>", draw_vertex_on_click)
def draw_vertex_on_click(event):
    global name_vertex
    global color_vertices_line
    r=15
    global ID
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    if mouse_y > 0:

        canvas.create_oval(mouse_x - r, mouse_y - r, mouse_x + r, mouse_y+ r,fill=color_vertices_line, outline="black", width=2)

        print(mouse_x, mouse_y)
  
        ID+=1
        #array_all_ID.append(ID)
        date_vertex_id_X_Y[ID] = [mouse_x, mouse_y, name_vertex]
        print(date_vertex_id_X_Y)
        canvas.create_text(mouse_x, mouse_y, text=name_vertex, font="Arial 14")
def draw_unoriented_line_between_vertex():#рисование неориентированного ребра
    canvas.bind_all("<Button-1>",draw_line_between_vertex_on_click)
def draw_line_between_vertex_on_click(event):
    global x1, y1, x2, y2, non_oriented_line, ID_none_oriented_line, name1, name2
    global count_unoriented_line
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in date_vertex_id_X_Y:
        if mouse_x > date_vertex_id_X_Y[i][0] - 15 and mouse_x < date_vertex_id_X_Y[i][0] + 15 and mouse_y > date_vertex_id_X_Y[i][1] - 15 and mouse_y < date_vertex_id_X_Y[i][1] + 15:
            if non_oriented_line == 0:
                name1 = date_vertex_id_X_Y[i][2]
                x1 = date_vertex_id_X_Y[i][0]
                y1 = date_vertex_id_X_Y[i][1]
                non_oriented_line += 1
                break
            elif non_oriented_line == 1:
                ID_none_oriented_line+=1
                name2 = date_vertex_id_X_Y[i][2]
                x2 = date_vertex_id_X_Y[i][0]
                y2 = date_vertex_id_X_Y[i][1]
                count_unoriented_line+=1
                date_ID_nonorient_line_X_Y[ID_none_oriented_line] = [[x1,y1,name1],[x2,y2,name2]]
                print("date_ID_nonorient_line_X_Y\t",date_ID_nonorient_line_X_Y)
                canvas.create_line(x1, y1, x2, y2, fill=color_vertices_line, width=2)
                non_oriented_line = 0
                break   


def delete_unoriented_line():#удаление неориентированного ребра
    canvas.bind_all("<Button-1>",delete_unoriented_line_on_click)
def delete_unoriented_line_on_click(event):
    global x1, y1, x2, y2, non_oriented_line, ID_none_oriented_line, name1, name2
    global count_unoriented_line
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in date_vertex_id_X_Y:
        if mouse_x > date_vertex_id_X_Y[i][0] - 15 and mouse_x < date_vertex_id_X_Y[i][0] + 15 and mouse_y > date_vertex_id_X_Y[i][1] - 15 and mouse_y < date_vertex_id_X_Y[i][1] + 15:
            if non_oriented_line == 0:
                name1 = date_vertex_id_X_Y[i][2]
                x1 = date_vertex_id_X_Y[i][0]
                y1 = date_vertex_id_X_Y[i][1]
                non_oriented_line += 1
                print("nam1,x1,y1   ",name1,x1,y1)
                break
            elif non_oriented_line == 1:
                name2 = date_vertex_id_X_Y[i][2]
                x2 = date_vertex_id_X_Y[i][0]
                y2 = date_vertex_id_X_Y[i][1]
                print("nam2,x2,y2   ",name2,x2,y2)
                count_unoriented_line-=1
                for key in date_ID_nonorient_line_X_Y:
                    if date_ID_nonorient_line_X_Y[key] == [[x1,y1,name1],[x2,y2,name2]] or date_ID_nonorient_line_X_Y[key] == [[x2,y2,name2],[x1,y1,name1]]:
                        del date_ID_nonorient_line_X_Y[key]
                        break
                print("date_ID_nonorient_line_X_Y in delete\t",date_ID_nonorient_line_X_Y)
                canvas.create_line(x1, y1, x2, y2, fill="white", width=2)
                non_oriented_line = 0
                break
        


def draw_oriented_line_between_vertex():#рисование ориентированного ребра
    canvas.bind_all("<Button-1>",draw_oriented_line_between_vertex_on_click)
def draw_oriented_line_between_vertex_on_click(event):
    global x1, y1, x2, y2, oriented_line, ID_oriented_line, name1, name2
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in date_vertex_id_X_Y:
        if mouse_x > date_vertex_id_X_Y[i][0] - 15 and mouse_x < date_vertex_id_X_Y[i][0] + 15 and mouse_y > date_vertex_id_X_Y[i][1] - 15 and mouse_y < date_vertex_id_X_Y[i][1] + 15:
            if oriented_line == 0:
                name1 = date_vertex_id_X_Y[i][2]
                x1 = date_vertex_id_X_Y[i][0]
                y1 = date_vertex_id_X_Y[i][1]
                oriented_line += 1
                
                break
            elif oriented_line == 1:
                ID_oriented_line+=1
                name2 = date_vertex_id_X_Y[i][2]
                x2 = date_vertex_id_X_Y[i][0]
                y2 = date_vertex_id_X_Y[i][1]
                date_ID_orient_line_X_Y[ID_oriented_line] = [[x1,y1,name1],[x2,y2,name2]]
                print("date_ID_orient_line_X_Y\t",date_ID_orient_line_X_Y)
                canvas.create_line(x1, y1, x2, y2, fill=color_vertices_line, width=2, arrow=LAST)
                oriented_line = 0
                break

def delete_oriented_line():#удаление ориентированного ребра
    canvas.bind_all("<Button-1>",delete_oriented_line_on_click)
def delete_oriented_line_on_click(event):
    global x1, y1, x2, y2, oriented_line, ID_oriented_line, name1, name2
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in date_vertex_id_X_Y:
        if mouse_x > date_vertex_id_X_Y[i][0] - 15 and mouse_x < date_vertex_id_X_Y[i][0] + 15 and mouse_y > date_vertex_id_X_Y[i][1] - 15 and mouse_y < date_vertex_id_X_Y[i][1] + 15:
            if oriented_line == 0:
                name1 = date_vertex_id_X_Y[i][2]
                x1 = date_vertex_id_X_Y[i][0]
                y1 = date_vertex_id_X_Y[i][1]
                oriented_line += 1
                print("nam1,x1,y1   ",name1,x1,y1)
                break
            elif oriented_line == 1:
                name2 = date_vertex_id_X_Y[i][2]
                x2 = date_vertex_id_X_Y[i][0]
                y2 = date_vertex_id_X_Y[i][1]
                print("nam2,x2,y2   ",name2,x2,y2)
                for key in date_ID_orient_line_X_Y:
                    if date_ID_orient_line_X_Y[key] == [[x1,y1,name1],[x2,y2,name2]]:
                        del date_ID_orient_line_X_Y[key]
                        break
                print("date_ID_orient_line_X_Y in delete\t",date_ID_orient_line_X_Y)
                canvas.create_line(x1, y1, x2, y2, fill="white", width=2, arrow=LAST)
                oriented_line = 0
                break


def vertex_name(name, root):#проверка на существование вершины
    global name_vertex
    if name == "":
        mb.showerror("","Вы не ввели имя вершины")
    elif name not in array_name_vertex:
        array_name_vertex.append(name)
        print(array_name_vertex)
        name_vertex = name
        root.destroy()
    else:
        mb.showerror("","Такая вершина уже существует") 
def NAME_VERTEX():#функция для задания имени вершины
    new_application = Tk()
    new_application.title("Задайте имя вершины")
    new_application.resizable(15, 15)
    label = Label(new_application)
    label["text"] = "Введите имя вершины"
    label.grid(row=0, column=0, sticky="ew")
    entry = Entry(new_application)
    entry.grid(row=1, column=0)
    btnGraf = Button(new_application, text="Ввод вершины", command=lambda: vertex_name(entry.get(), new_application))
    btnGraf.grid(row=2, column=0, sticky="ew")
    new_application.mainloop    
def stop_add_vertex():#для остановки действия
    canvas.unbind_all("<Button-1>")
def color_vertex(color):#для изменения цвета вершины
    global color_vertices_line
    color_vertices_line = color
    print(color_vertices_line)


def change_graf_name(name, root):#изменение имени графа
    if name in all_name_garphs:
        mb.showerror("","Такое имя графа уже существует")
    elif name == "":
        mb.showerror("","Вы не ввели имя графа")
    else:
        label["text"] = name
        all_name_garphs.append(name)
        print(all_name_garphs)
        root.destroy()
def graph_name():#изменение имени графа
    new_application = Tk()
    new_application.title("Задайте имя графа")
    new_application.wm_attributes('-topmost', 1)
    new_application.resizable(0, 0)
    label = Label(new_application)
    label["text"] = "Введите имя графа"
    label.grid(row=0, column=0, sticky="ew")
    entry = Entry(new_application)
    entry.grid(row=1, column=0)
    btnGraf = Button(new_application, text="Ввод", command=lambda: change_graf_name(entry.get(), new_application))
    btnGraf.grid(row=2, column=0, sticky="ew")
    new_application.mainloop

    
def delete_vertex():#удаление вершины
    canvas.bind_all("<Button-1>", delete_vertex_on_click)
def delete_vertex_on_click(event):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in date_vertex_id_X_Y:
        if mouse_x > date_vertex_id_X_Y[i][0] - 15 and mouse_x < date_vertex_id_X_Y[i][0] + 15 and mouse_y > date_vertex_id_X_Y[i][1] - 15 and mouse_y < date_vertex_id_X_Y[i][1] + 15:
            global ID
            ID-=1
            canvas.delete(date_vertex_id_X_Y[i][2])
            canvas.create_oval(date_vertex_id_X_Y[i][0] - 15, date_vertex_id_X_Y[i][1] - 15, date_vertex_id_X_Y[i][0] + 15, date_vertex_id_X_Y[i][1] + 15,fill="white", outline="white", width=2)
            
            array_name_vertex.remove(date_vertex_id_X_Y[i][2])
            print("имена вершин: ",array_name_vertex)
            print("словарь вершин: ",date_vertex_id_X_Y[i][2])
            del date_vertex_id_X_Y[i]
            print("оставшийся словарь вершин",date_vertex_id_X_Y)
            break

def rename_vertex():#переименование вершины
    canvas.bind_all("<Button-1>", rename_vertex_on_click)
def rename_vertex_on_click(event):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in date_vertex_id_X_Y:
        if mouse_x > date_vertex_id_X_Y[i][0] - 15 and mouse_x < date_vertex_id_X_Y[i][0] + 15 and mouse_y > date_vertex_id_X_Y[i][1] - 15 and mouse_y < date_vertex_id_X_Y[i][1] + 15:
            new_application = Tk()
            new_application.title("Задайте имя вершины")
            new_application.resizable(15, 15)
            label = Label(new_application)
            label["text"] = "Введите имя вершины"
            label.grid(row=0, column=0, sticky="ew")
            entry = Entry(new_application)
            entry.grid(row=1, column=0)
            print("имена вершин: ",array_name_vertex)
            #print("словарь вершин: ",date_vertex_id_X_Y[i][2])
            print("оставшийся словарь вершин",date_vertex_id_X_Y)
            btnGraf = Button(new_application, text="Ввод вершины", command=lambda: rename_vertex_name(entry.get(), new_application, i))
            btnGraf.grid(row=2, column=0, sticky="ew")
            new_application.mainloop
            break
def rename_vertex_name(name, root, i):
    global color_vertices_line
    if name == "":
        mb.showerror("","Вы не ввели имя вершины")
    elif name in array_name_vertex:
        mb.showerror("","Такое имя вершины уже существует")
    else:
        canvas.delete(date_vertex_id_X_Y[i][2])
        canvas.create_oval(date_vertex_id_X_Y[i][0] - 15, date_vertex_id_X_Y[i][1] - 15, date_vertex_id_X_Y[i][0] + 15, date_vertex_id_X_Y[i][1] + 15,fill=color_vertices_line, outline="black", width=2)
        canvas.create_text(date_vertex_id_X_Y[i][0], date_vertex_id_X_Y[i][1], text=name, font="Arial 14", fill="black")
        array_name_vertex.remove(date_vertex_id_X_Y[i][2])
        date_vertex_id_X_Y[i][2] = name
        array_name_vertex.append(name)
        root.destroy()


def algorithm():#функция для создания окна с алгоритмами
    global max_node, UNORIN_ORIENT,result_adjancy_matrix,result_incidency_matrix
    new_application = Tk() # Создание окна
    new_application.geometry(f"432x470+195+0") # Размер окна и его расположение
    new_application.resizable(0, 0) #Запрет на изменение размера окна
    new_application.wm_attributes('-topmost', 1) # Окно всегда сверху
    new_application.title("запишите свой граф и выберите алгоритм") # Заголовок окна
    canvas = Canvas(new_application, bg="white", width=468, height=403) # Создание холста
    
    entry = Entry(new_application, width=20, font="Arial 16")
    
    
    button_dejkstra = Button(new_application, text="Алгоритм\nДейкстры", command=lambda: deikstra(temp_edges,weight,max_node),width=12, height=2)
    input_value = Button(new_application, text="Ввод графа", command=lambda: graph_info(entry.get(), new_application),width=12, height=2)
    button_reading_file = Button(new_application, text="Чтение из файла", command=lambda: reading_file(new_application),width=12, height=2)

    if UNORIN_ORIENT ==0:
        button_diametr_graph = Button(new_application, text="Диаметр графа", command=lambda: diametr_graph(result_adjancy_matrix),width=12, height=2)
        button_radius_graph = Button(new_application, text="Радиус графа", command=lambda: radius_graph(result_adjancy_matrix),width=12, height=2)
        button_center_graph = Button(new_application, text="Центр графа", command=lambda: center_graph(result_adjancy_matrix),width=12, height=2)
    else:
        button_diametr_graph = Button(new_application, text="Диаметр графа", command=lambda: diametr_graph(result_incidency_matrix),width=12, height=2, state=DISABLED)
        button_radius_graph = Button(new_application, text="Радиус графа", command=lambda: radius_graph(result_incidency_matrix),width=12, height=2, state=DISABLED)
        button_center_graph = Button(new_application, text="Центр графа", command=lambda: center_graph(result_incidency_matrix),width=12, height=2, state=DISABLED)



    #dejkstra.grid(row=1, column=0, sticky="ew")
    #floyd.grid(row=2, column=0, sticky="ew")
    entry.grid(row=0, column=1)
    input_value.grid(row=1, column=1, sticky="ew")
    button_reading_file.grid(row=2, column=1, sticky="ew")

    
    
    button_adjancy_matrix = Button(new_application, text="Матрица\nсмежности", command=lambda: adjancy_matrix(temp_edges,max_node),width=12, height=2)
    button_incidency_matrix = Button(new_application, text="Матрица\nинцидентности", command=lambda: incidency_matrix(temp_edges,max_node, UNORIN_ORIENT,new_application),width=12, height=2)
    button_euleran_circle = Button(new_application, text="Эйлеров\nцикл", command=lambda: euleran_circle(result_adjancy_matrix),width=12, height=2)
    button_quit = Button(new_application, text="Выход", command=new_application.destroy,width=12, height=2)

    print("result_ajancy_matrix",result_adjancy_matrix)
    print("result_incidency_matrix",result_incidency_matrix)
    print("max_node= ", max_node)
    print("nodes= ", nodes)
    print("edges= ", weight)
    button_adjancy_matrix.grid(row=1, column=0, sticky="ew")
    button_incidency_matrix.grid(row=0, column=0, sticky="ew")
    button_euleran_circle.grid(row=2, column=0, sticky="ew")
    button_diametr_graph.grid(row=0, column=2, sticky="ew")
    button_radius_graph.grid(row=1, column=2, sticky="ew")
    button_center_graph.grid(row=2, column=2, sticky="ew")
    button_dejkstra.grid(row=3, column=0, sticky="ew")
    button_quit.grid(row=8, column=0, sticky="ew")
    new_application.mainloop()

def graph_info(information, root):#функция для ввода графа
    file = open("info.txt","w")
    file.write(information)
    file.close()

def reading_file(root):#считывание записанного в файл графа
    global max_node, UNORIN_ORIENT, temp_edges, nodes,weight

    file = open("info.txt","r")

    temp = file.readline()
    information = temp.split(";")
    name_type_graph = information[0]
    nodes_graph = information[1]
    edges_graph = information[2]
    temp_weight = information[3]
    

    UNORIN_ORIENT = 0
    if "UNORIENT" in name_type_graph:
        UNORIN_ORIENT = 0
    elif "ORIENT" in name_type_graph:
        UNORIN_ORIENT = 1

    nodes = nodes_graph.split(",")
    for i in range(len(nodes)):
        nodes[i] = int(nodes[i])
    print("nodes", nodes)


    temp = edges_graph.split(",")
    temp_edges = []
    for i in range(len(temp)):
        temp_edges.append(temp[i].split("->"))
    for i in range(len(temp_edges)):
        for j in range(len(temp_edges[i])):
            temp_edges[i][j] = int(temp_edges[i][j])

    print("temp edges", temp_edges)    
    n = len(temp_edges)
    max_node = 0
    for i in range(len(temp_edges)):
        for j in range(2):
            if temp_edges[i][j] > max_node:
                max_node = temp_edges[i][j]

    weight = temp_weight.split(",")
    for i in range(len(weight)):
        weight[i] = int(weight[i])
    print("max_node= ", max_node)
    print("n= ", n)
    print("nodes= ", nodes)
    print("weight= ", weight)

def adjancy_matrix(nodes,max_node):#функция для матрицы смежности
    global result_adjancy_matrix
    print("Матрица смежности")
    adj = [[0 for i in range(max_node)] for j in range(max_node)]
    for i in range(len(nodes)):
        adj[nodes[i][0]-1][nodes[i][1]-1] = 1
        if UNORIN_ORIENT == 0:
            adj[nodes[i][1]-1][nodes[i][0]-1] = 1
    for i in range(max_node):
        print(adj[i])
    print()
    result_adjancy_matrix = adj
    
   
def incidency_matrix(nodes,max_nodes, UNORIN_ORIENT,root):
    global result_incidency_matrix
    print("Матрица инцидентности")
    if UNORIN_ORIENT == 0:
        inc = [[0 for i in range(len(nodes))] for j in range(max_nodes)]
        for i in range(len(nodes)):
            inc[nodes[i][0]-1][i] = 1
            inc[nodes[i][1]-1][i] = 1
    else:
        inc = [[0 for i in range(len(nodes))] for j in range(max_nodes)]
        for i in range(len(nodes)):
            inc[nodes[i][0]-1][i] = 1
            inc[nodes[i][1]-1][i] = -1
    for i in range(max_nodes):
        print(inc[i])
    print()
    result_incidency_matrix = inc

'''def diametr_graph(matrix):
    diameter = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                diameter = max(diameter, distance(matrix, i, j))
    print("Диаметр графа: ", diameter)

def radius_graph(matrix):
    radius = 1000000
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                radius = min(radius, distance(matrix, i, j))
    print("Радиус графа: ", radius)
def distance(matrix, start, end):
    queue = []
    queue.append(start)
    visited = [0 for i in range(len(matrix))]
    visited[start] = 1
    dist = [0 for i in range(len(matrix))]
    while len(queue) > 0:
        current = queue.pop(0)
        for i in range(len(matrix)):
            if matrix[current][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                dist[i] = dist[current] + 1
    return dist[end]

def center_graph(matrix):
    center = []
    radius = 1000000
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                radius = min(radius, distance(matrix, i, j))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                if radius == distance(matrix, i, j):
                    center.append(i+1)
    print("Центр графа: ", center)'''

def algorithm_Dijkstra(root):
    print("Алгоритм Дейкстры")
def algorithm_Floyd(root):
    print("Алгоритм Флойда")



def adjancy_for_deikstra(nodes, weight, max_node):
    n = len(nodes)
    m = 2
    array_edge = [[0 for i in range(m)] for j in range(n)]
    array_edjancy = [[0 for i in range(max_node)] for j in range(max_node)]
    for i in range(n):
        for j in range(m):
            array_edge[i][j] = nodes[i][j]
    for i in range(max_node):
        for j in range(max_node):
            array_edjancy[i][j] = 0
    for i in range(n):
        x = array_edge[i][0]
        y = array_edge[i][1]
        array_edjancy[x-1][y-1] = weight[i]
        array_edjancy[y-1][x-1] = weight[i]
    return array_edjancy
def deikstra(nodes,weight,max_node):
    adjacencyMatrix = adjancy_for_deikstra(nodes, weight, max_node)
    for start in range(max_node):
        distance = [inf for i in range(max_node)]
        visited = [0 for i in range(max_node)]
        distance[start] = 0
        for i in range(max_node):
            v = -1
            for j in range(max_node):
                if visited[j] == 0 and (v == -1 or distance[j] < distance[v]):
                    v = j
            if distance[v] == inf:
                break
            visited[v] = 1
            for j in range(max_node):
                if adjacencyMatrix[v][j] != 0:
                    to = j
                    len = adjacencyMatrix[v][j]
                    if distance[v] + len < distance[to]:
                        distance[to] = distance[v] + len
        print("vertex\tdistance")
        for i in range(max_node):
            print(i+1,"\t",distance[i])



def DFS(adjacencyMatrix, visited, start=0):
    max_node = len(adjacencyMatrix)
    s = []
    s.append(start)
    while s:
        v = s.pop()
        if not visited[v]:
            visited[v] = 1
            for i in range(max_node):
                if adjacencyMatrix[v][i] and not visited[i]:
                    s.append(i)
def conCompDFS(adjacencyMatrix):
    max_node = len(adjacencyMatrix)
    count = 0
    visited = [0] * max_node
    for i in range(max_node):
        if not visited[i]:
            DFS(adjacencyMatrix, visited, i)
            count += 1
    return count
def euleran_circle(adjacencyMatrix):
    max_node = len(adjacencyMatrix)
    print("conCompDFS(adjacencyMatrix)", conCompDFS(adjacencyMatrix))
    if (conCompDFS(adjacencyMatrix) != 1):
        print("граф не является Эйлеровым")
        mb.showerror("","граф не является Эйлеровым")
    degrees = [0] * max_node
    for i in range(max_node):
        for j in range(max_node):
            if (adjacencyMatrix[i][j]):
                degrees[i] += 1
    for i in range(max_node):
        if (degrees[i] % 2 != 0):
            print("граф не является Эйлеровым")
            mb.showerror("","граф не является Эйлеровым")
    path = []
    s = []
    poz = 0
    s.append(poz)
    while s:
        poz = s[-1]
        temp = False
        for i in range(max_node):
            if (adjacencyMatrix[poz][i]):
                adjacencyMatrix[poz][i] = 0
                adjacencyMatrix[i][poz] = 0
                s.append(i)
                temp = True
                break
        if not temp:
            path.append((poz+1))
            s.pop()
    print("Euleran circle: ",path)




def move_vertex_and_line():
    canvas.bind_all("<Button-3>", move_vertex_on_click)
def move_vertex_on_click(event):
    global name_vertex
    global color_vertices_line
    global ID
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    for i in date_vertex_id_X_Y:
        if mouse_x > date_vertex_id_X_Y[i][0] - 15 and mouse_x < date_vertex_id_X_Y[i][0] + 15 and mouse_y > date_vertex_id_X_Y[i][1] - 15 and mouse_y < date_vertex_id_X_Y[i][1] + 15:
            '''move a vertex'''
            canvas.bind_all("<B1-Motion>", move_vertex)
            name_vertex = i
            color_vertices_line = date_vertex_id_X_Y[i][2]
            ID = date_vertex_id_X_Y[i]
            break
def move_vertex(event):
    global name_vertex
    global color_vertices_line
    global ID
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    canvas.coords(ID, mouse_x - 15, mouse_y - 15, mouse_x + 15, mouse_y + 15)
    canvas.itemconfig(ID, fill=color_vertices_line)
    date_vertex_id_X_Y[name_vertex][0] = mouse_x
    date_vertex_id_X_Y[name_vertex][1] = mouse_y
    

            
'''def move_line():
    canvas.bind_all("<Button-3>", move_line_on_click)
def move_line_on_click(event):'''

            
        
    

    



def main():
    button_vertex = Button(application, text="add vertex", command=draw_vertixes,width=15, height=2)
    button_stop_add_vertex = Button(application, text="stop add and\n delete vertex", command=stop_add_vertex,width=15, height=2)
    button_green = Button(application, text="green", command=lambda: color_vertex("green"),width=15, height=2, bg="green")
    button_blue = Button(application, text="blue", command=lambda: color_vertex("blue"),width=15, height=2, bg="blue")
    button_yellow = Button(application, text="yellow", command=lambda: color_vertex("yellow"),width=15, height=2, bg="yellow")
    button_name_graph = Button(application, text="name graph", command=lambda: graph_name(),width=15, height=2)
    button_name_vertex = Button(application, text="name vertex", command=lambda: NAME_VERTEX(),width=15, height=2)
    button_delete_vertex = Button(application, text="delete vertex", command=lambda: delete_vertex(),width=15, height=2)
    button_rename_vertex = Button(application, text="rename vertex", command=lambda: rename_vertex(),width=15, height=2)
    button_draw_line_between_vertex = Button(application, text="draw unoriented_line\n between vertex", command=lambda: draw_unoriented_line_between_vertex(),width=15, height=2)
    button_draw_oriented_line_between_vertex = Button(application, text="draw oriented\n  between vertex", command=lambda: draw_oriented_line_between_vertex(),width=15, height=2)
    button_move_vertex_with_line = Button(application, text="move vertex \nwith line", command=lambda: move_vertex_and_line(),width=15, height=2)
    button_delete_unoriented_line= Button(application, text="delete unoriented\n line", command=lambda: delete_unoriented_line(),width=15, height=2)
    button_delete_oriented_line= Button(application, text="delete oriented\n line", command=lambda: delete_oriented_line(),width=15, height=2)
    button_algorithm= Button(application, text="algorithm", command=lambda: algorithm(),width=15, height=2)
    button_quit2 = Button(application, text="quit", command=application.destroy,width=15, height=2)
    
    
    button_name_vertex.grid(row=0, column=0)
    button_stop_add_vertex.grid(row=1, column=0)
    button_green.grid(row=0, column=1)
    button_blue.grid(row=0, column=2)
    button_yellow.grid(row=0, column=3)
    button_vertex.grid(row=0, column=4)
    button_draw_line_between_vertex.grid(row=1, column=4)
    button_delete_unoriented_line.grid(row=1,column=5)
    button_delete_oriented_line.grid(row=2,column=5)
    button_draw_oriented_line_between_vertex.grid(row=2, column=4)
    button_delete_vertex.grid(row=0, column=5)
    button_rename_vertex.grid(row=0, column=6)
    button_move_vertex_with_line.grid(row=1, column=6)
    button_name_graph.grid(row=2, column=0)
    button_algorithm.grid(row=2, column=2)
    button_quit2.grid(row=2, column=6)

    

    application.mainloop()
main()