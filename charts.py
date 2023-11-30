import matplotlib.pyplot as plt

def generate_charts_pie(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()
    
