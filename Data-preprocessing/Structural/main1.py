import os
from generate_max_angular_momentum import get_keywords_from_geo_file, generate_max_angular_momentum_string
from generate_skf_plath import get_skf_paths_as_string
from params import opt_params  # 导入 opt_params

# 读取 geo.gen 文件并生成 Max Angular Momentum
geo_file_path = r"D:\code\mo\dftb+\Data-preprocessing\Structural\out\geo.gen"  # 替换为你的文件路径
template_path = r"D:\code\mo\dftb+\Data-preprocessing\Structural\dftb_in_template.hsd"  # 使用绝对路径
output_path = r"D:\code\mo\dftb+\Data-preprocessing\Structural\out\dftb_in.hsd"  # 输出文件路径
parameter_sets_path = "D:/code/mo/dftb+/parameter-sets.xlsx"
base_path = "D:/code/mo/dftb+/slako-unpacked/slako"

# 提取关键词并生成 Max Angular Momentum 字符串
keywords = get_keywords_from_geo_file(geo_file_path)
max_am_string = generate_max_angular_momentum_string(keywords)

skf_paths_string = get_skf_paths_as_string(base_path, geo_file_path, parameter_sets_path)

# 更新 MAX_AM 为生成的字符串
opt_params["MAX_AM"] = max_am_string
opt_params["SlaterKosterFiles"] = skf_paths_string

# 为多行字符串添加缩进的辅助函数
def apply_indent_to_multiline_string(multiline_string, indent=" " * 3):
    indented_lines = [f"{indent}{line}" for line in multiline_string.splitlines()]
    return "\n".join(indented_lines)

# 生成输入文件的函数
def generate_dftb_in(template_path, params, output_path):
    try:
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"模板文件 {template_path} 不存在")

        with open(template_path, "r", encoding='utf-8') as template_file:
            template_content = template_file.read()

        # 使用字典替换占位符
        for key, value in params.items():
            # 将值转换为字符串
            if not isinstance(value, str):
                value = str(value)  # 转换为字符串
            # 处理多行字符串的缩进
            if "\n" in value:
                # 如果 value 是多行字符串，则添加缩进
                value = apply_indent_to_multiline_string(value, indent=" " * 3)
            # 替换模板内容中的占位符
            template_content = template_content.replace(f"%{key}%", value)

        # 写入最终的输入文件
        with open(output_path, "w", encoding='utf-8') as output_file:
            output_file.write(template_content)
        print(f"成功生成输入文件：{output_path}")

    except FileNotFoundError as fnf_error:
        print(f"错误：{fnf_error}")
    except Exception as e:
        print(f"生成输入文件时出错：{e}")

# 主函数，根据任务类型生成相应的输入文件
def main(task_type):
    if task_type == "optimize":
        generate_dftb_in(template_path, opt_params, output_path)
    else:
        print("未知的任务类型，请选择 'optimize'、'phonon' 或 'md'。")

# 示例调用
if __name__ == "__main__":
    # 自动化生成结构优化的输入文件
    main("optimize")
# 自动化生成声子谱计算的输入文件
    #main("phonon")
    # 自动化生成分子动力学模拟的输入文件
    #main("md")