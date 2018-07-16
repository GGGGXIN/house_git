from django.shortcuts import render, HttpResponse
from django.views import View
import hashlib
import json


# Create your views here.


class HtmlView(View):
    def get(self, request):
        # 根据具体业务逻辑获取到要播放的视频的vid
        vid = "03b56854c0e149a81c1d6258be4d64c2_0"
        polyv_id = "polyvplayer" + vid
        return render(request, "保利视频.html", locals())


class DemoView(View):
    def get(self, request, *args, **kwargs):
        username = "gaoxin"
        secretkey = "aljdkgapdog"
        vid = request.GET.get("vid")
        t = request.GET.get("t")
        code = request.GET.get("code")
        fontSize = "40"
        fontColor = "0xFFE900"
        speed = "200"
        filter = "on"
        setting = "3"
        alpha = "1"
        filterAlpha = "1"
        filterColor = "0x3914AF"
        blurX = "2"
        blurY = "2"
        tweenTime = "1"
        interval = "5"
        lifeTime = "3"
        strength = "4"
        show = "on"
        msg = "Errormessage!"
        # a = f"xinjie={t}&beautiful={setting}"
        if username == "gaoxin":
            status = 1
        else:
            status = 2
        callback = request.GET.get("callback", "")
        # 适配移动端的 如果是移动端需要加callback参数
        if callback != "":
            sign_str = "vid=" + vid + "&secretkey=" + secretkey + "&username=" + username + "&code=" + code + "&status=" + status + "&t=" + t
            sign = hashlib.md5(sign_str)
            result = {
                "status": status,
                "username": username,
                "sign": sign
            }
            json_ret = json.dumps(result)
            ret = callback + "(" + json_ret + ")"
            return HttpResponse(ret)
        else:
            sign_str = "vid=" + vid + "&secretkey=" + secretkey + "&username=" + username + "&code=" + code + "&status=" + status +"&t=" + t + "&msg=" + msg + "&fontSize=" + fontSize + "&fontColor=" + fontColor + "&speed=" + speed +"&filter=" + filter + "&setting=" + setting + "&alpha=" + alpha + "&filterAlpha=" + filterAlpha +"&filterColor=" + filterColor + "&blurX=" + blurX + "&blurY=" + blurY + "&interval=" + interval +"&lifeTime=" + lifeTime + "&tweenTime=" + tweenTime + "&strength=" + strength + "&show=" + show
            sign = hashlib.md5(sign_str)
            result = {
                "status": status,
                "username": username,
                "sign": sign,
                "msg": msg,
                "fontSize": fontSize,
                "fontColor": fontColor,
                "speed": speed,
                "filter": filter,
                "setting": setting,
                "alpha": alpha,
                "filterAlpha": filterAlpha,
                "filterColor": filterColor,
                "blurX": blurX,
                "blurY": blurY,
                "tweenTime": tweenTime,
                "interval": interval,
                "lifeTime": lifeTime,
                "strength": strength,
                "show": show
            }
            return HttpResponse(json.dumps(result))