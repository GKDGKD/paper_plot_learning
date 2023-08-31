import matplotlib.pyplot as plt
import seaborn as sns
import scienceplots
import pandas as pd
from pandas import DataFrame

# plt.rcParams['font.family'] = 'Times New Roman'
# plt.rcParams['font.size']   = 14

def univariate_histplot(data:DataFrame, x:str, hue=None, figsize=(10,6), style=['science'], kde=True, kind='hist',
                        plot_dpi=100, saveflag=False, save_dir='./', save_dpi=300, save_type='png'):
    """
    单变量直方图函数。第一次画的
    
    Args:
    data: Dataframe, 必需参数，且必须为DataFrame。
    x: 变量名，str, 必需参数。
    hue: 分组的变量名，str, 一般为类别，如性别、种类等。默认为空。
    figsize: 图片尺寸，默认为(10, 6)。
    style: list, 画图的风格，默认为['science']，可以改为['science', 'ieee']
    kde: bool, 是否添加核密度估计曲线，默认为True.
    kind: str, 图像类型，hist为直方图，kde为密度图。
    plot_dpi: int, 画图时的dpi。
    saveflag: bool, 是否保存图片，默认为False。
    save_dir: str, 保存路径。
    save_dpi: int, 保存的图片dpi，越高越清晰，图片所占空间也就越大。
    save_type: str, 保存的图片类型，默认为'png'.
    
    """

    if not isinstance(data, DataFrame):
        raise TypeError("Input 'data' must be a pandas DataFrame")

    cols = data.columns
    if x not in cols:
        raise ValueError("Input 'x' must be a column name in data")
    if hue and hue not in cols:
        raise ValueError("Input 'hue' must be a column name in data")
    if not save_dir.endswith('/'):
        save_dir = save_dir + '/'
    if kind not in ['hist', 'kde']:
        raise ValueError("Input 'kind' must be 'hist' or 'kde'")
    
    with plt.style.context(style):
        fig, ax = plt.subplots(figsize=figsize, dpi=plot_dpi, facecolor="w")
        if hue and kind == 'hist':
            ax = sns.histplot(data=data, x=x, hue=hue, multiple='dodge', shrink=.8)
        elif hue and kind == 'kde':
            ax = sns.kdeplot(data=data, x=x, hue=hue, fill=True, alpha=.5)
        else:
            ax = sns.histplot(data=data, x=x, kde=kde)

        ax.set_xlabel('Values') # 画完图后不能再有参数出现
        ax.set_ylabel('Frequency')  

        if saveflag:
            if hue:
                save_path = save_dir + kind + x + '_' + hue + '_' + style[-1] + '.' + save_type
            else:
                save_path = save_dir + kind + x + '_' + style[-1] + '.' + save_type
            plt.savefig(save_path, dpi=save_dpi, bbox_inches='tight')
            print(f'Plot has been saved to {save_path} .')

        plt.show()

if __name__ == "__main__":
    iris = sns.load_dataset('iris')
    univariate_histplot(data=iris, x='sepal_width')
    print('Done.')