from PIL import Image
import base64
import pyzbar.pyzbar as pbar

import io

msg = "iVBORw0KGgoAAAANSUhEUgAAATQAAABkCAIAAACHGluLAAABn0lEQVR4nO3TQY7CMBAAQWv//2c4LUIZO7uCSx+qDgiCk4kt9VprrbUev+b31+dcefnr9e/7je8r58XLytP6+XNO/HPEnLIdMXc3R58O5PR9jti+1dzRaeOn59w89rTNm9O73P7NiHl02yfPbd7v93JxO3Su//85fPAm99vZHshpIz8LSBInRIkTosQJUeKEKHFClDghSpwQJU6IEidEiROixAlR4oQocUKUOCFKnBAlTogSJ0SJE6LECVHihChxQpQ4IUqcECVOiBInRIkTosQJUeKEKHFClDghSpwQJU6IEidEiROixAlR4oQocUKUOCFKnBAlTogSJ0SJE6LECVHihChxQpQ4IUqcECVOiBInRIkTosQJUeKEKHFClDghSpwQJU6IEidEiROixAlR4oQocUKUOCFKnBAlTogSJ0SJE6LECVHihChxQpQ4IUqcECVOiBInRIkTosQJUeKEKHFClDghSpwQJU6IEidEiROixAlR4oQocUKUOCFKnBAlTogSJ0SJE6LECVHihChxQpQ4IUqcECVOiBInRIkTop7myuTwxW9FKgAAAABJRU5ErkJggg=="

data = base64.b64decode(msg)
#img = Image.frombytes("RGB", (308, 100), data)
#img.save("test.png")
#with open("t.png", "wb") as f:
#    f.write(data)

test = Image.new("RGB", (600, 300), "white")

img = Image.open(io.BytesIO(data))
img.save("t.png")
test.paste(img, (100, 50))

dbar = pbar.decode(test, symbols=[pbar.ZBarSymbol.CODE128])

print(dbar)
