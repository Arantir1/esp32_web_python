def web_page():
  red_btn_html = "<p><a href=\"/red/off\"><button class=\"button button2\">RED OFF</button></a></p>" if red_pin_status else "<p><a href=\"/red/on\"><button class=\"button\">RED ON</button></a></p>"
  green_btn_html = "<p><a href=\"/green/off\"><button class=\"button button2\">GREEN OFF</button></a></p>" if green_pin_status else "<p><a href=\"/green/on\"><button class=\"button\">GREEN ON</button></a></p>"
  blue_btn_html = "<p><a href=\"/blue/off\"><button class=\"button button2\">BLUE OFF</button></a></p>" if blue_pin_status else "<p><a href=\"/blue/on\"><button class=\"button\">BLUE ON</button></a></p>"
  html = """
  <!DOCTYPE HTML>
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
      <style> 
          html { font-family: Arial; display: inline-block; margin: 0px auto; text-align: center; }
          h2 { font-size: 3.0rem; } p { font-size: 3.0rem; } .units { font-size: 1.2rem; } 
          .ds-labels { font-size: 1.5rem; vertical-align:middle; padding-bottom: 15px; }
          .button { background-color: #4CAF50; border: none; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
          .button2 {background-color: #555555;}
      </style>
    </head>
    <body>
      <h2>ESP32 WebServer</h2>""" + red_btn_html + green_btn_html + blue_btn_html + """
    </body>
  </html>
  """
  return html
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)
 
while True:
  try:
    if gc.mem_free() < 102000:
      gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    print('Content = %s' % request)

    if request.find('/red/on') != -1:
      print("Turn on RED light")
      red_pin_status = True
      red_pin.value(1)
    elif request.find('/red/off') != -1:
      print("Turn off RED light")
      red_pin_status = False
      red_pin.value(0)

    if request.find('/green/on') != -1:
      print("Turn on GREEN light")
      green_pin_status = True
      green_pin.value(1)
    elif request.find('/green/off') != -1:
      print("Turn off GREEN light")
      green_pin_status = False
      green_pin.value(0)

    if request.find('/blue/on') != -1:
      print("Turn on BLUE light")
      blue_pin_status = True
      blue_pin.value(1)
    elif request.find('/blue/off') != -1:
      print("Turn off BLUE light")
      blue_pin_status = False
      blue_pin.value(0)

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Connection closed')