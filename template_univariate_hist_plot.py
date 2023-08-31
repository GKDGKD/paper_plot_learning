import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots
import pandas as pd
from pandas import DataFrame

# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size']   = 14

def univariate_histplot(data:DataFrame, x:str, hue=None, figsize=(10,6), style=['science'], kde=True,
                        saveflag=False, save_dir='./', save_dpi=300, save_type='png'):
    """
    单变量直方图函数。第一次画的
    
    Args:
    data: Dataframe, 必需参数，且必须为DataFrame。
    x: 变量名，str, 必需参数。
    hue: 分组的变量名，str, 一般为类别，如性别、种类等。默认为空。
    figsize: 图片尺寸，默认为(10, 6)。
    style: list, 画图的风格，默认为['science']，可以改为['science', 'ieee']
    kde: bool, 是否添加核密度估计曲线，默认为True.
    saveflag: bool, 是否保存图片，默认为False。
    save_dir: str, 保存路径。
    save_dpi: int, 保存的图片dpi，越高越清晰，图片所占空间也就越大。
    save_type: str, 保存的图片类型，默认为'png'.
    
    """

    if not isinstance(data, DataFrame):
        raise TypeError("Input 'data' must be a pandas DataFrame")
    
    with plt.style.context(style):
        fig, ax = plt.subplots(figsize=figsize, dpi=100, facecolor="w")
        if hue:
            ax = sns.histplot(data=data, x=x, hue=hue, kde=kde, multiple='dodge', shrink=.8)
        else:
            ax = sns.histplot(data=data, x=x, kde=kde)
        # ax.set(xlabel=x, ylabel='Frequency')  
        ax.set_xlabel(x)
        ax.set_ylabel('Frequency')       

    if saveflag:
        save_path = save_dir + 'Hist_' + style[-1] + '.' + save_type
        plt.savefig(save_path, dpi=save_dpi, bbox_inches='tight')
        print(f'Plot has been saved to {save_path}.')

    plt.show()

if __name__ == "__main__":
    iris = sns.load_dataset('iris')
    univariate_histplot(data=iris, x='sepal_width')
    print('Done.')