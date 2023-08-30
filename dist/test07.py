from pyecharts import options as opts
from pyecharts.charts import Gauge

c = (
    Gauge()
    .add(
        "",
        [("完成率", 66.6)],
        detail_label_opts=opts.GaugeDetailOpts(  # 将title_label_opts修改为detail_label_opts
            font_size=40, color="blue", font_family="Microsoft YaHei"
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-改变轮盘内的字体"))
    .render("gauge_label_title_setting.html")
)
