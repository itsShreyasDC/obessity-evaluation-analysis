import networkx as nx
import matplotlib.pyplot as plt

def plot_density():
    x=[]
    y=[]
    for i in range(0,11):
        G=nx.read_gml('evolution_'+str(i)+'.gml')
        x.append(i)
        y.append(nx.density(G))
    plt.xlabel('Time')
    plt.ylabel('Density')
    plt.title('Change in density')
    plt.plot(x,y)
    plt.savefig('density.jpg')

def obesity(G):
    num=0
    for each in G.nodes():
        if G.nodes[each]['name']==40:
            num=num+1
    return num

def plot_obesity():
    x=[]
    y=[]
    for i in range(0,11):
        G=nx.read_gml('evolution_'+str(i)+'.gml')
        x.append(i)
        y.append(obesity(G))
    plt.xlabel('Time')
    plt.ylabel('Obesity')
    plt.title('Change in Obesity')
    plt.plot(x,y)
    plt.savefig('obesity_change.jpg')

def nobesity(G):
    num=0
    for each in G.nodes():
        if G.nodes[each]['type']=='person':
            if int(G.nodes[each]['name'])>=30:
                num=num+1
    return num

def plot_nobesity():
    x=[]
    y=[]
    for i in range(0,11):
        G=nx.read_gml('evolution_'+str(i)+'.gml')
        x.append(i)
        y.append(nobesity(G))
        print(y)
    plt.xlabel('Time')
    plt.ylabel('Nearly Obesity')
    plt.title('Change in Nearly Obesity')
    plt.plot(x,y)
    plt.savefig('nearly_obesity_change.jpg')

plot_density()
plot_obesity()
#plot_nobesity()
