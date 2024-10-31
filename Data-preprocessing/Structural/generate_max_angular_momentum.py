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


# 将提取的元素及其最大角动量轨道类型写入文件
def generate_max_angular_momentum_string(keywords):
    # 定义最大角动量轨道类型
    # 假设 s, p, d, f 的对应关系
    max_angular_momentum = {
        "H": "s",
        "He": "s",
        "Li": "s",
        "Be": "s",
        "B": "p",
        "C": "p",
        "N": "p",
        "O": "p",
        "F": "p",
        "Ne": "p",
        "Na": "s",
        "Mg": "s",
        "Al": "p",
        "Si": "p",
        "P": "p",
        "S": "p",
        "Cl": "p",
        "Ar": "p",
        "K": "s",
        "Ca": "s",
        "Sc": "d",
        "Ti": "d",
        "V": "d",
        "Cr": "d",
        "Mn": "d",
        "Fe": "d",
        "Co": "d",
        "Ni": "d",
        "Cu": "d",
        "Zn": "d",
        "Ga": "p",
        "Ge": "p",
        "As": "p",
        "Se": "p",
        "Br": "p",
        "Kr": "p",
        "Rb": "s",
        "Sr": "s",
        "Y": "d",
        "Zr": "d",
        "Nb": "d",
        "Mo": "d",
        "Tc": "d",
        "Ru": "d",
        "Rh": "d",
        "Pd": "d",
        "Ag": "d",
        "Cd": "d",
        "In": "p",
        "Sn": "p",
        "Sb": "p",
        "Te": "p",
        "I": "p",
        "Xe": "p",
        "Cs": "s",
        "Ba": "s",
        "La": "d",
        "Ce": "f",
        "Pr": "f",
        "Nd": "f",
        "Pm": "f",
        "Sm": "f",
        "Eu": "f",
        "Gd": "f",
        "Tb": "f",
        "Dy": "f",
        "Ho": "f",
        "Er": "f",
        "Tm": "f",
        "Yb": "f",
        "Lu": "d",
        "Hf": "d",
        "Ta": "d",
        "W": "d",
        "Re": "d",
        "Os": "d",
        "Ir": "d",
        "Pt": "d",
        "Au": "d",
        "Hg": "d",
        "Tl": "p",
        "Pb": "p",
        "Bi": "p",
        "Po": "p",
        "At": "p",
        "Rn": "p",
        "Fr": "s",
        "Ra": "s",
        "Ac": "d",
        "Th": "f",
        "Pa": "f",
        "U": "f",
        "Np": "f",
        "Pu": "f",
        "Am": "f",
        "Cm": "f",
        "Bk": "f",
        "Cf": "f",
        "Es": "f",
        "Fm": "f",
        "Md": "f",
        "No": "f",
        "Lr": "d",
        "Rf": "d",
        "Db": "d",
        "Sg": "d",
        "Bh": "d",
        "Hs": "d",
        "Mt": "d",
        "Ds": "d",
        "Rg": "d",
        "Cn": "d",
        "Nh": "p",
        "Fl": "p",
        "Mc": "p",
        "Lv": "p",
        "Ts": "p",
        "Og": "p"
    }

    max_am_lines = []

    for element in keywords:
        if element in max_angular_momentum:
            orbital = max_angular_momentum[element]
            max_am_lines.append(f'{element} = "{orbital}"')  # 添加了缩进
        else:
            print(f"{element} 没有定义的轨道类型")

    # 将生成的字符串以换行连接
    return "\n".join(max_am_lines)
