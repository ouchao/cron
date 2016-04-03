# cron
这是一个linux下创建、修改、删除crontab计划任务。
可以通过命令的形式调用，调用时传入一条json数据。

json数据格式为：

{'id':1,'cmd':'date','every':'2.day','action':'update','at':'hour.12 minute.15 minute.45'}
id：唯一标识
cmd:需要执行的命令或者脚本全路径
every:执行任务的时间周期
分钟   [1-60].minute
小时   [1-24].hour
天     [1-31].day
月     [1-12].month
英文月 jan feb mar apr may jun jul aug sep oct nov dec (and all of those full month names)
星期   sunday, monday, tuesday, wednesday, thursday, friday, saturday
每周   weekday, weekend (case insensitive)
年     [1-9].year

action:对计划任务的操作动作
update:增加
clear：删除
write:
check:检查语法

at:执行周期的更小范围的具体执行时间

示例：
./cron.py "{'id':1,'cmd':'date','every':'2.day','action':'update','at':'hour.12 minute.15 minute.45'}"
表示增加一条计划任务，隔两天执行一次，执行的具体时间是12:15和12:45.






