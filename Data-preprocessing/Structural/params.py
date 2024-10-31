opt_params = {
    "geo.gen": "geo.gen",
    "DRIVER_TYPE": "GeometryOptimization",
    "DRIVER_OPTIONS": """Optimizer = Rational {}
MovedAtoms = 1:-1
MaxSteps = 100
OutputPrefix = "geom.out"
Convergence {GradElem = 1E-4}""",
    "ForceEvaluation": "",  # 加上逗号
    "SCCTOLERANCE": 1.0e-6,  # 去掉引号
    "Filling": "",
    "MAX_AM": "",  # 初始化为一个空字符串，将在后面替换
    "KPoints": "0 0 0 1",
    "SlaterKosterFiles": "",
    "Options": " ",
    "Analysis": "CalculateForces = Yes"
}

phonon_params = {
    "geo.gen": "geo.genS-001",
    "DRIVER_TYPE": "GeometryOptimization",
    "DRIVER_OPTIONS": """Optimizer = Rational {}
MovedAtoms = 1:-1
MaxSteps = 100
OutputPrefix = "geom.out"
Convergence {GradElem = 1E-4}""",
    "ForceEvaluation": "",  # 加上逗号
    "SCCTOLERANCE": 1.0e-6,  # 去掉引号
    "Filling": "",  # 加上逗号
    "MAX_AM": "",  # 初始化为一个空字符串，将在后面替换
    "KPoints": "0 0 0 1",
    "SlaterKosterFiles": "",
    "Options": " ",
    "Analysis": "CalculateForces = Yes"
}

md_params = {
    "geo.gen": "geo.gen",
    "DRIVER_TYPE": "VelocityVerlet",
    "DRIVER_OPTIONS": """TimeStep [fs] = 1.0
Thermostat = NoseHoover {
Temperature [Kelvin] = 400
CouplingStrength [cm^-1] = 3200
ChainLength = 3
Order = 3
IntegratorSteps = 1
  }
  Barostat = {
    Pressure [Pa] = 1.0E5
    Timescale [ ps ] = 0.01
    Isotropic = Yes
}
  Steps = 10000
  MovedAtoms = 1:-1""",
    "ForceEvaluation": "",  # 加上逗号
    "SCCTOLERANCE": 1.0e-6,  # 去掉引号
    "Filling": "",
    "MAX_AM": "",  # 初始化为一个空字符串，将在后面替换
    "KPoints": "0 0 0 1",
    "SlaterKosterFiles": "",
    "Options": """RandomSeed = 3871906
WriteDetailedOut = No""",  # 修正引号和逗号
    "Analysis": "WriteBandOut = No"
}
