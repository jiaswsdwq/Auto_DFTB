import os
import re
import pandas as pd


# 读取 geo.gen 文件并获取第二行数据
def get_keywords_from_geo_file(geo_file_path):
    with open(geo_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) > 1:
            second_line_data = set(lines[1].strip().split())
            return second_line_data
        else:
            print("geo.gen 文件没有足够的行")
            return None


# 遍历文件夹，查找 .skf 文件并返回路径列表
def find_skf_files(base_path, first_column_value, keywords):
    target_folder = os.path.join(base_path, first_column_value)
    found_files = []  # 用于存储找到的文件路径

    if os.path.exists(target_folder):
        for root, dirs, files in os.walk(target_folder):
            for file in files:
                if file.endswith('.skf'):
                    file_elements = re.findall(r'\b[A-Z][a-z]?\b', file)
                    file_elements_set = set(file_elements)

                    if all(elem in keywords for elem in file_elements_set) and len(file_elements) >= 2:
                        full_path = os.path.abspath(os.path.join(root, file))
                        found_files.append(full_path)  # 添加到找到的文件列表
                        print(full_path)

    return found_files  # 返回找到的文件路径列表


# 获取找到的 skf 文件路径并转换为字符串
def get_skf_paths_as_string(base_path, geo_file_path, parameter_sets_path):
    # 读取 geo.gen 文件中的关键词
    keywords = get_keywords_from_geo_file(geo_file_path)

    if keywords is not None:
        df = pd.read_excel(parameter_sets_path, header=None)
        matched_first_column_values = []

        for index, row in df.iterrows():
            third_col_data = row[2]
            if pd.notna(third_col_data):
                third_col_elements = set(re.findall(r'\b[A-Z][a-z]?\b', third_col_data))
                if keywords.issubset(third_col_elements):
                    first_column_value = row[0]
                    matched_first_column_values.append(first_column_value)
                    print("匹配的第一列数据:", first_column_value)

        # 遍历所有匹配的 first_column_value，查找 .skf 文件
        all_found_files = []
        for first_column_value in matched_first_column_values:
            found_files = find_skf_files(base_path, first_column_value, keywords)
            all_found_files.extend(found_files)  # 添加找到的文件路径到总列表

        # 将找到的文件路径转换为字符串，并添加格式
        if all_found_files:
            formatted_skf_paths = []
            for file_path in all_found_files:
                # 提取文件名（不包括路径和扩展名）
                file_name = os.path.basename(file_path).replace('.skf', '')
                formatted_line = f"{file_name} = \"{file_path}\" "
                formatted_skf_paths.append(formatted_line)

            skf_paths_string = "\n".join(formatted_skf_paths)  # 用换行符连接路径
            return skf_paths_string
        else:
            print("未找到匹配的 .skf 文件。")
            return ""


# 主程序
def main():
    geo_file_path = "D:/code/mo/dftb+/Data-preprocessing/Structural/out/geo.gen"
    parameter_sets_path = "D:/code/mo/dftb+/parameter-sets.xlsx"
    base_path = "D:/code/mo/dftb+/slako-unpacked/slako"

    # 获取 skf 文件路径的字符串
    skf_paths_string = get_skf_paths_as_string(base_path, geo_file_path, parameter_sets_path)

    # 打印或进一步处理 skf_paths_string
    if skf_paths_string:
        print("找到的 .skf 文件路径:\n", skf_paths_string)


if __name__ == "__main__":
    main()
