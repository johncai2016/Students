<p><b>项目说明:</b></p>
   <p>本项目纯属公益，如果觉得里面的功能可以用上，欢迎使用</p>
   <p>由于疫情，老师需要收集开学前3天学生和同住人员的核酸检测记录，行程码，老师需要核对学生提交的信息是否正确，这需要花费老师很多的时间。</p>
   <p>因为没有办法自动获取到学生和同住人员的核酸记录，行程码信息。所以老师通常需要以小程序接龙的方式让家长提交相应的截图，然后再打开截图查看相关信息是否正确。这个小项目的目标主要就是给老师减轻负担，希望把大部分的数据核查能通过脚本自动完成。</p>
   <p>学生家长提交每天的核酸检测结果(含检测中),行程码，老师需要核对以下信息:</p>
   <p>1. 学生和同住人员数量，比如老师的excel中填写的是4人(含学生本人)，那提交的记录就应该有4份核酸记录，行程码不做数量检查</p>
   <p>2. 检查提交的核酸记录是否在某天之后的，比如必须是2022-4-2后，如果家长提交了3月31号的数据，这种情况要报告出来。</p>
   <p>3. 查找出核酸结果还在'检测中’的学生，因为有时候家长当天做的结果还没有出来，老师需要在第二天提醒学生家长重新提交结果。</p>
   <p>4. 检查学生家长行程码是否带星，主要是因为家长有时候会忘记跟老师报备，行程码带星的学生需要老师特别关注。</p>
   <p><b>准备资料：</b></p>
   <p>1. 家长当天提交截图的zip文件，因为老师都是通过微信接龙小程序完成的，接龙小程序有个功能可以导出所有学生的数据，只需要把所有数据压缩成zip文件即可。</p>
   <p>2. 一个excel表，第一列填写学生姓名，第二列填写同住人员数量(含学生本人)，此excel表不需要表头</p>
   <p>然后即可按照提示的步骤在几分钟内自动完成核查</p>
   <p><b>关于数据安全</b></p>
   <p>所有提交的原始数据，包括中间暂时存入数据库的数据，都可以在完成后点击‘删除数据’，本程序不会保留任何数据。</p>
   <p><b>项目部署</b></p>
   <p>python3 + django 4.0 + tesseract</p>
   <p><b>需要改进的地方</b></p>
   <p>行程码截图中的时间无法识别/核酸结果还在检测中的姓名无法识别，后续看看能不能调用百度的API看看，因为我手动试了百度的OCR识别是可以识别出来的，不过百度的API有调用限制(超过要收钱).</p>
   <p><b>常见问题</b></p>
   <p>1.如何保持后台允许?</p>
   <p>nohub python3 manage.py runserver 0.0.0.0:80 & </p>
   <p>2.如何部署到阿里云上?</p>
   <p>a.在setting中设置ALLOWED_HOSTS = ['你的阿里云公网IP','localhost','127.0.0.1','0.0.0.0:80']</p>
   <p>b.nohub python3 manage.py runserver 0.0.0.0:80 & </p>
   <p>c.检查安全组策略(也就是防火墙规则要放行对应的端口)</p>
   <p>3.文件夹或者文件解压后乱码的问题,可以通过下面的代码解决</p>
   <p>try:
       new_name = old_name.encode('cp437').decode('gbk') </p>
   <p>except:
       new_name = old_name.encode('utf-8').decode('utf-8') </p>
   <p>4.linux下目录是通过'/',但是windows是'\'</p>
   <p>5.图片无法显示的问题</p>
   <p>在urls.py中记得要添加
   from django.conf.urls.static import static
   from django.conf import settings
   urlpatterns = [
    path('upload_zipFile/', views.upload_zipFile),
    path('upload_excelFile/',views.upload_excelFile),
    path('',views.index),
    path('show_issues',views.show_issues),
    path('show_details',views.show_details),
    path('show_route_details',views.show_route_details),
    path('check_family_number',views.check_family_number),
    path('delete_info',views.delete_info),
    path('process_students_data',views.process_students_data),
    path('steps',views.steps),
    path('test',views.test),
    path('remove_expire_data',views.remove_expire_data),
    path('how_to_export_zip',views.how_to_export_zip),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   </p> 
   <p><b>特别感谢:</b></p>
   <p>@小黑的帮忙，我遇到的很多问题不懂都是请教@小黑大佬的，谢谢他告诉我django这个框架,用起来真的很方便,也谢谢他帮我画的流程图，代码基本按这个流程写的(除了下载PDF这部分)</p>
   ![image](https://user-images.githubusercontent.com/23047196/165004913-829a1c89-c02b-4691-807f-4a6eb31ce804.png)

