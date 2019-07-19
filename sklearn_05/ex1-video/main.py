from flask import Flask, render_template, Response
import cv2
 
class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0) 
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
 
app = Flask(__name__)
 
@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('index.html')
 
def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数(yield)输出视频流， 每次请求输出的content类型是image/jpeg
        # b'' 表示生成字节数据
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
 
@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')   

# 基于服务器推送的图片刷新技术演示
# https://blog.csdn.net/qq_25349323/article/details/90261549
# 用 Flask 输出视频流
# https://juejin.im/post/5bea86fc518825158c531e9c
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)