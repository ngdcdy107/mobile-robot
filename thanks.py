import openai
from noi import noi
from nghe0 import nghe0
noi("Mời bạn nói ")
while True:
    text = nghe0()
    if "Hello" in text or "chào" in text:
        noi("chào bạn")
    elif "tên" in text:
        noi("tôi là trợ lý ảo quán trà ai")
    elif "tạm biệt" in text:
        noi("bye")
        break
    elif "..." in text:
        noi("Xin lỗi,tôi không nghe được rõ")
    else:
        noi("xin lỗi tôi chưa thông minh nên không hiểu câu này")