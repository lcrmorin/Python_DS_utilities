import matplotlib.pyplot as plt
from matplotlib_venn import venn3
 
# Custom text labels: change the label of group A
# TO DO: automatically calculate subsets

v=venn3(subsets = (10, 8, 22, 6, 9, 4, 2), set_labels = ('Group A', 'Group B', 'Group C'))
v.get_label_by_id('A').set_text('My Favourite group!')
plt.show()
