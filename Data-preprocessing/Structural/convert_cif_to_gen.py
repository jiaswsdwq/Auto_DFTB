from ase.io import read, write
import os

def convert_cif_to_gen(input_file):
    """
    将 CIF 文件转换为 geo.gen 文件。

    参数:
    input_file (str): 输入 CIF 文件的路径。
    """

    # 获取输入文件的目录
    input_dir = os.path.dirname(input_file)

    # 定义输出文件路径，始终命名为 geo.gen
    output_dir = os.path.join(input_dir, 'out')
    output_file = os.path.join(output_dir, 'geo.gen')  # 固定命名为 geo.gen

    # 检查输出目录是否存在，如果不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取 CIF 文件
    atoms = read(input_file, format='cif')
    # 打印原子信息
    print(f"Atoms object info:\n{atoms}")

    # 写入 geo.gen 文件
    write(output_file, atoms, format='gen')

    print(f"转换完成：'{input_file}' -> '{output_file}'")


# 如果需要，可以添加一个测试代码段
if __name__ == "__main__":
    # 示例：调用函数进行转换
    convert_cif_to_gen(r'D:\code\mo\dftb+\Data-preprocessing\Structural\1999106-UTSA-16(Zn).cif')
