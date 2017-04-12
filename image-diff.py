from sys import argv
import mahotas as mh
import mahotas.resize
from matplotlib import pyplot as plt
from matplotlib import style
style.use('seaborn-white')
fig,axes = plt.subplots(1,3)
orig = mh.imread(argv[1])
put = mh.imread(argv[2])
axes[0].imshow(orig)
axes[1].imshow(put)
if orig.shape != put.shape:
    orig = mh.resize.resize_to(orig, put.shape)
diff = (orig != put).any(2)
print("Fraction different: {:.2%}".format(diff.mean()))
axes[2].imshow(diff)
fig.show()
plt.pause(20)
