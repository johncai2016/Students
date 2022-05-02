from sys import argv
import os
import pytesseract
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, ALL_COMPLETED, as_completed
import re
from PIL import Image
import datetime
import threading

#解压缩的时候本身的文件夹也会被提取出来作为一个目录。      
def get_image_dir(path):
    file_list = os.listdir(path)
    for f in file_list:
        if os.path.isdir(path + "/" + f):
            return f

def extract_data_from_img(student_path):
    route_with_star = '行程码正常'
    #从截图中提取每个学生和家属的数据
    files = os.listdir(student_path)
    for f in files:
        if f.endswith('.txt'):
            continue
        image_name = student_path + '/' + f
        text = pytesseract.image_to_string(Image.open(image_name),lang='chi_sim')
        text = re.sub('[\s+]','',text)

        #检查核酸'结果,姓名一般是2-5个中文字
        person_name = re.search("检测中([\u4E00-\u9FA5]{2,5})采样时间",text,re.S)
        collect_time = re.search("采样时间([0-9]{4}-[0-9]{2}-[0-9]{2})?",text)
        result_time = re.search("检测时间([0-9]{4}-[0-9]{2}-[0-9]{2})?",text)
        #结果只会有检测中和阴性，因为如果是阳性，早被拉走了.
        #提取检测相关信息，如果图片上有采样时间，说明图片是核酸记录
        if collect_time is not None:
            if person_name is not None:
                #目前不知道为啥无法识别‘检测中’的人员姓名
                person_name = str.strip(person_name.group(1))
                if person_name == '':
                    person_name = '无法识别'
                else:
                    person_name = '无法识别'

            collect_time = str.strip(collect_time.group(1))
            if result_time is None:
                result_time = '检测中'
                final_result = '检测中'
            else:
                result_time = str.strip(result_time.group(1))
                final_result = '阴性'                                                                                                                               

            with open(student_path + '/student.txt','a') as f:
                f.write('person_name:' + person_name + '|' + 'collect_time:' + collect_time + '|' + 'final_result:' + final_result + '\r\n')
        
        #检查行程码
        phone = re.search("绿色行程卡(1.*)的动态",text)
        #route_date = datetime.datetime.utcnow()
        with_star_in_result = re.search("中风险",text)
        #目前无法识别行程码时间。
        if phone is not None:
            phone = str.strip(phone.group(1))
            if with_star_in_result is not None:
                route_with_star = '行程码带星'
            with open(student_path + '/route.txt','a') as f:
                f.write('phone:' + phone + '|' + '行程码状态:' + route_with_star + '\r\n')
    
    #如果学生的所有截图都处理完了，标记一下
    with open(student_path + '/done.txt','a') as f:
        f.write('done')

def pinjie():
    path = '/root/john_project/student/download_data/i6erbo0T/学生信息/叶五'
    # 获取当前文件夹中所有JPG图像
    im_list = [Image.open(path + '/' + fn) for fn in os.listdir(path) if fn.endswith('.jpg')]
    # 图片转化为相同的尺寸
    ims = []
    for i in im_list:
        new_img = i.resize((1280, 1280), Image.BILINEAR)
        ims.append(new_img)
        # 单幅图像尺寸
    width, height = ims[0].size
    # 创建空白长图
    result = Image.new(ims[0].mode, (width, height * len(ims)))
     # 拼接图片
    for i, im in enumerate(ims):
        result.paste(im, box=(0, i * height))
    result.save(path + '/res1.jpg')

#pinjie()
#exit()
path = '/root/john_project/student/download_data/i6erbo0T/学生信息/叶五'
image_dir_list = os.listdir(path)
new_path = path + '/' + 'res1.jpg'
text = pytesseract.image_to_string(Image.open(new_path),lang='chi_sim')
text = re.sub('[\s+]','',text)
print(text)
exit()
with open(file=new_path, mode='ab+') as f1:
    f2 = open(path + '/' + '0.jpg','rb')
    f3 = open(path + '/' + '6.jpg','rb')
    c1 = f2.read()
    c2 = f3.read()
    f1.write(c1)
    f1.write(c2)
    f2.close()
    f3.close()
    #for f in image_dir_list:
        #old_file = path + '/' + f
        #with open(file=old_file,mode='rb') as f2:
            #content = f2.read()
            #f1.write(content)
exit()
script_name,unique_id,start_index = argv
start_index = int(start_index)
end_index = start_index + 10
path = './download_data/' +  unique_id
image_dir = get_image_dir(path)
image_dir_list = os.listdir(path + "/" + image_dir)
#student_path = path + '/' + image_dir + '/' + student
students_full_path = []
tasks = []
start = datetime.datetime.now()
for f in image_dir_list:
      full_path = path + '/' + image_dir + '/' + f
      students_full_path.append(full_path)
      t = threading.Thread(target=extract_data_from_img,args=(full_path,))
      t.daemon = False
      t.start()
      tasks.append(t)

end = datetime.datetime.now()
print('All done:' + str(end - start))
