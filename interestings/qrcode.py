import base64

s = """data:image/png;base64,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"""
s2 = s.split(',', 2)[1]
img_data = base64.b64decode(s2)
# 注意：如果是"data:image/jpg:base64,"，那你保存的就要以jpg格式，
# 如果是"data:image/png:base64,"那你保存的时候就以png格式。
with open('001.png', 'wb') as f:
    f.write(img_data)
print('successful')




