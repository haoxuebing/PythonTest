import itchat
import numpy
import pandas as pd
from pyecharts import Pie, Map, Style, Page, Bar

def get_attr(friends, key):
    return list(map(lambda user: user.get(key), friends))

def get_friends():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends()
    users = dict(province=get_attr(friends, "Province"),
                 city=get_attr(friends, "City"),
                 nickname=get_attr(friends, "NickName"),
                 sex=get_attr(friends, "Sex"),
                 signature=get_attr(friends, "Signature"),
                 remarkname=get_attr(friends, "RemarkName"),
                 pyquanpin=get_attr(friends, "PYQuanPin"),
                 displayname=get_attr(friends, "DisplayName"),
                 isowner=get_attr(friends, "IsOwner"))
    return users


def sex_stats(users):
    df = pd.DataFrame(users)
    sex_arr = df.groupby(['sex'], as_index=True)['sex'].count()
    data = dict(zip(list(sex_arr.index), list(sex_arr)))
    # data['不知道'] = data.pop(0)
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


# def prov_stats(users):
#       prv = pd.DataFrame(users)
#       prv_cnt = prv.groupby('province', as_index=True)['province'].count().sort_values()
#       attr = list(map(lambda x: x if x != '' else '未知', list(prv_cnt.index)))
#       return attr, list(prv_cnt)  

# def create_charts2():
#     users = get_friends()
#     data = prov_stats(users)
#     attr, value = data
#     chart = Map('中国地图', **style.init_style)
#     chart.add('', attr, value, is_label_show=True, is_visualmap=True, visual_text_color='#000')
#     page.add(chart)
#     chart = Bar('柱状图', **style_middle.init_style)
#     chart.add('', attr, value, is_stack=True, is_convert=True, label_pos='inside', is_legend_show=True,
#             is_label_show=True)
#     page.add(chart)
#     page.render()

create_charts()
