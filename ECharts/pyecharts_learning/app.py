from pyecharts import options as opts

#准备绘制饼图需要的数据，需要x轴和y轴的数据，数据格式为列表
from pyecharts.charts import Bar

x = ['餐饮','娱乐','交通','保养','衣服']
y= [1000,500,2000,1000,1000]

#创建对象,可以加一些参数，下面这个参数的意思是图的大小，宽800个像素，高600个像素
bar = Bar(init_opts = opts.InitOpts(width = '800px',height = '600px'))
#添加数据,注意添加y轴数据的时候，必须设置series_name参数，表示图例的名称
bar.add_xaxis(xaxis_data = x)
bar.add_yaxis(series_name = 'zhang某人',y_axis = y)
#添加参数
bar.set_global_opts(title_opts = opts.TitleOpts(title = 'zhang某人的幸福生活'))
#生成html文件,这里是相对路径，文件保存在代码所在目录下
bar.render('第一个bar图.html')
