import sys
import re

def replace_punctuation(text):
    # 将中文逗号和句号替换为英文逗号和句号，并在其后添加空格
    text = text.replace('，', ', ').replace('。', '. ')
    return text

def add_space_between(text):
    # 使用正则表达式在中英文之间添加空格
    text = re.sub(r'([A-Za-z0-9]+)([\u4e00-\u9fa5]+)', r'\1 \2', text)
    text = re.sub(r'([\u4e00-\u9fa5]+)([A-Za-z0-9]+)', r'\1 \2', text)
    return text

def brace_formatter(text):
    # 将所有的 "\{" 替换为 "\lbrace"
    text = text.replace("\\{", "\\lbrace ")
    text = text.replace("\\}", "\\rbrace ")
    return text

def main():
    if len(sys.argv) != 2:
        print("用法: python reformat.py <文件名>")
        sys.exit(1)  # 使用 sys.exit() 退出脚本，参数 1 表示错误退出

    input_filename = sys.argv[1]

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # 在中英文之间添加空格
        modified_text = add_space_between(text)

        # 替换文本中的标点符号
        modified_text = replace_punctuation(modified_text)

        # 替换大括号
        modified_text = brace_formatter(modified_text)

        # 将替换后的文本写回当前打开的文件
        with open(input_filename, 'w', encoding='utf-8') as file:
            file.write(modified_text)

    except FileNotFoundError:
        print(f"找不到文件: {input_filename}")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()
