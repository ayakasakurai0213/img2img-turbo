import matplotlib.pyplot as plt

def plot_image(image_dict: dict):
    keys =[i for i in image_dict.keys()]
    x = 1
    y = len(image_dict)

    fig = plt.figure()
    for i in range(y):
        ax = fig.add_subplot(x, y, i+1)
        ax.set_title(keys[i])
        plt.imshow(image_dict[keys[i]])
    
    plt.show()