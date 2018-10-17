import numpy
import pandas as pd
from pyecharts import Pie, Map, Style, Page, Bar

def sex_stats(users):
    df = pd.DataFrame(users)
    sex_arr = df.groupby(['sex'], as_index=True)['sex'].count()
    data = dict(zip(list(sex_arr.index), list(sex_arr)))
    data['不告诉你'] = data.pop(0)
    data['帅哥'] = data.pop(1)
    data['美女'] = data.pop(2)
    return data.keys(), data.values()

def create_charts():
    users = get_friends()

page = Page()
style = Style(width=1100, height=600)
style_middle = Style(width=900, height=500)

data = sex_stats(users)
attr, value = data
chart = Pie('微信性别')  # title_pos='center'
chart.add('', attr, value, center=[50, 50],
          radius=[30, 70], is_label_show=True, legend_orient='horizontal', legend_pos='center',
          legend_top='bottom', is_area_show=True)
page.add(chart)
page.render()
