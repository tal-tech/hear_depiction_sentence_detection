import sys
from module.description import Description

if __name__ == "__main__":
    desc = Description()
    state, description = desc.init()
    print(state, description)
    if state < 0:
        sys.exit(0)

    sentence_list = [
       
        '草地上传来他们一阵阵的欢呼声，如银铃般清脆,如驼铃般悠远，与这美好的 舂色融为了一体。' # 听觉
       
    ]
    state, desc_info = desc.get_all_descriptions(sentence_list)
    if desc_info['num'] == 1:
        print("是听觉描写")
    else:
        print("不是听觉描写")
