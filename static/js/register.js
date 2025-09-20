function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function(event){
        //this:代表当前jQuery对象
        var $this = $(this)
        //阻止默认点击事件(提交表单)
        event.preventDefault();
        //获取输入框内容
        var email = $("input[name='email']").val();
        $.ajax({
            url: "/auth/captcha/email?email="+email,
            method: "GET",
            success: function(result){
                var code = result['code'];
                if(code == 200){
                    //制作倒计时
                    var countdown = 5;
                    //取消点击事件
                    $this.off("click")
                    //间隔时间执行函数
                    var timer = setInterval(function(){
                        $this.text(countdown);
                        countdown -= 1;
                        if(countdown <= 0){
                            //清除定时器
                            clearInterval(timer);
                            $this.text("获取验证码");
                            //开启点击事件
                            bindEmailCaptchaClick();
                        }
                    },1000);
                    //alert("邮箱验证发送成功");
                }else{
                    alert(result[message]);
                }
            },
            fail: function(error){
                console.log(error);
            }
        })
    });
}

// 包裹的部分会在整个Dom都加载完成后才会执行
$(function (){
    bindEmailCaptchaClick();
});