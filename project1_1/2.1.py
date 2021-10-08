import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

n=r'D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\login.csv'
path=r''
df=pd.DataFrame(pd.read_csv(n,encoding='gbk'))


def save(data,path):         #保存csv
    data.to_csv(path,encoding='gbk')
def draw(data):
    prince1=[]               #
    prince1.append(every_sum(data,'中国安徽'))
    prince1.append(every_sum(data, '中国澳门'))
    prince1.append(every_sum(data, '中国北京'))
    prince1.append(every_sum(data, '中国福建'))
    prince1.append(every_sum(data, '中国甘肃'))
    prince1.append(every_sum(data, '中国广东'))
    prince1.append(every_sum(data, '中国广西'))
    prince1.append(every_sum(data, '中国贵州'))
    prince1.append(every_sum(data, '中国海南'))
    prince1.append(every_sum(data, '中国河北'))
    prince1.append(every_sum(data, '中国河南'))
    prince1.append(every_sum(data, '中国黑龙江'))
    prince1.append(every_sum(data, '中国湖北'))
    prince1.append(every_sum(data, '中国湖南'))
    prince1.append(every_sum(data, '中国吉林'))
    prince1.append(every_sum(data, '中国江苏'))
    prince1.append(every_sum(data, '中国江西'))
    prince1.append(every_sum(data, '中国辽宁'))
    prince1.append(every_sum(data, '中国内蒙古'))
    prince1.append(every_sum(data, '中国宁夏'))
    prince1.append(every_sum(data, '中国青海'))
    prince1.append(every_sum(data, '中国山东'))
    prince1.append(every_sum(data, '中国山西'))
    prince1.append(every_sum(data, '中国陕西'))
    prince1.append(every_sum(data, '中国上海'))
    prince1.append(every_sum(data, '中国四川'))
    prince1.append(every_sum(data, '中国台湾'))
    prince1.append(every_sum(data, '中国天津'))
    prince1.append(every_sum(data, '中国西藏'))
    prince1.append(every_sum(data, '中国香港'))
    prince1.append(every_sum(data, '中国新疆'))
    prince1.append(every_sum(data, '中国云南'))
    prince1.append(every_sum(data, '中国浙江'))
    prince1.append(every_sum(data, '中国重庆'))
    return prince1
    # n=data['login_place'].str.contains("中国广东")
    # s=0
    # for x in n:
    #     if x==True:
    #         s+=1

def every_sum(data,name):
    n = data['login_place'].str.contains(name)
    s = 0
    for x in n:
        if x == True:
            s += 1
    return s
    # for x in data.index:
    #     if data.loc[x,'login_place'].str.contains("中国黑龙江"):
    #         prince1.append(data.loc[x,'login_place'])
    #     elif data.loc[x,'login_place'].str.contains("中国"):
    #         pass
    # print(prince1)

def main():
    prince=draw(df)

    print(prince)

    name=['安徽','澳门','北京','福建','甘肃','广东','广西','贵州','海南','河北','河南','黑龙江' \
             ,'湖北','湖南','吉林','江苏','江西','辽宁','内蒙古','宁夏','中国青海','山东','山西'\
             ,'陕西','上海','四川','台湾','天津','西藏','香港','新疆','云南','浙江','重庆']
    c = (
        Map()
            .add("登陆次数", [list(z) for z in zip(name, prince)], maptype="china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="热力地图"), visualmap_opts=opts.VisualMapOpts(max_=20000),
        )
            .render(r"D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\projectmap_guangdong.html")
    )
    # c = (
    #     Map()
    #         .add("登陆次数", [list(z) for z in zip(name,prince)], "china")
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
    #         visualmap_opts=opts.VisualMapOpts(max_=20000, is_piecewise=True),
    #     )
    #         .render(r"D:\xinjianqq\赛题a：教育平台的线上课程智能推荐策略\map_visualmap_piecewise.html")
    # )
    print(name)
main()