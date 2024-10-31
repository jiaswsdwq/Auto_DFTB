import os
from generate_max_angular_momentum import get_keywords_from_geo_file, generate_max_angular_momentum_string
from generate_skf_plath import get_skf_paths_as_string
from params import opt_params, phonon_params, md_params  # 导入所有相关的参数
from convert_cif_to_gen import convert_cif_to_gen  # 导入转换函数

# 文件路径
cif_file_path = r"D:\code\mo\dftb+\Data-preprocessing\Structural\1999106-UTSA-16(Zn).cif"  # 替换为你的CIF文件路径
geo_file_path = os.path.join(os.path.dirname(cif_file_path), 'out', 'geo.gen')  # geo.gen 文件路径固定为 geo.gen
template_path = r"D:\code\mo\dftb+\Data-preprocessing\Structural\dftb_in_template.hsd"  # 模板文件路径
base_output_path = r"D:\code\mo\dftb+\Data-preprocessing\Structural\out"  # 输出基础文件夹路径
parameter_sets_path = "D:/code/mo/dftb+/parameter-sets.xlsx"
base_path = "D:/code/mo/dftb+/slako-unpacked/slako"

# 生成 geo.gen 文件并处理后续操作
def generate_geo_and_process(cif_file_path):
    try:
        convert_cif_to_gen(cif_file_path)  # 调用转换函数
        print(f"成功生成 geo.gen 文件：{geo_file_path}")

        # 提取关键词并生成 Max Angular Momentum 字符串
        keywords = get_keywords_from_geo_file(geo_file_path)
        max_am_string = generate_max_angular_momentum_string(keywords)

        skf_paths_string = get_skf_paths_as_string(base_path, geo_file_path, parameter_sets_path)

        # 更新所有参数集中的 MAX_AM 和 SlaterKosterFiles
        opt_params["MAX_AM"] = max_am_string
        opt_params["SlaterKosterFiles"] = skf_paths_string
        phonon_params["MAX_AM"] = max_am_string
        phonon_params["SlaterKosterFiles"] = skf_paths_string
        md_params["MAX_AM"] = max_am_string
        md_params["SlaterKosterFiles"] = skf_paths_string

        return True  # 成功处理返回 True

    except Exception as e:
        print(f"处理 geo.gen 文件时出错：{e}")
        return False  # 处理失败返回 False

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
            if not isinstance(value, str):
                value = str(value)  # 转换为字符串
            if "\n" in value:
                value = apply_indent_to_multiline_string(value, indent=" " * 3)
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
    # 创建任务文件夹
    task_folder = os.path.join(base_output_path, task_type)
    os.makedirs(task_folder, exist_ok=True)  # 如果文件夹不存在则创建

    # 定义输出文件路径
    output_file_name = "dftb_in.dftb"  # 所有任务统一命名为 dftb_in.dftb
    output_path = os.path.join(task_folder, output_file_name)  # 生成输出文件的完整路径

    if task_type == "optimize":
        generate_dftb_in(template_path, opt_params, output_path)
    elif task_type == "phonon":
        generate_dftb_in(template_path, phonon_params, output_path)
    elif task_type == "md":
        generate_dftb_in(template_path, md_params, output_path)
    else:
        print("Unknown task type. Please select 'optimize', 'phonon', or 'md'.")

# 示例调用
if __name__ == "__main__":
    if generate_geo_and_process(cif_file_path):  # 首先生成 geo.gen 并处理后续操作
        main("optimize")
        main("phonon")
        main("md")
