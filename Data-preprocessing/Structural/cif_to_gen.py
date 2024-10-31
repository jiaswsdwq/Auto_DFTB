from ase.io import read, write
import os

# 定义输入和输出文件路径
input_file = 'D:\code\mo\dftb+\Data-preprocessing\Structural/1999106-UTSA-16(Zn).cif'  # 输入 CIF 文件路径
output_file = 'D:\code\mo\dftb+\Data-preprocessing\Structural\out\geo.gen'  # 输出 GEN 文件路径

# 获取输出文件目录
output_dir = os.path.dirname(output_file)

# 检查输出目录是否存在，如果不存在，则创建
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取 CIF 文件
atoms = read(input_file, format='cif')
# 打印原子信息
print(f"Atoms object info:\n{atoms}")

# 写入 GEN 文件
write(output_file, atoms, format='gen')

print(f"转换完成：'{input_file}' -> '{output_file}'")
