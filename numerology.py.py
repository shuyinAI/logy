from datetime import datetime

def simplify(n):
    n = int(n)
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def format_date(date_input):
    s = ''.join(str(c) for c in date_input if c.isdigit())
    if len(s) == 7:   # 輸入1994510自動補0
        s = s[:4] + '0' + s[4:]
    if len(s) != 8:
        raise ValueError("請輸入8位生日數字（如：19940510）")
    return s

class DestinyCalculator:
    def __init__(self, birth_date):
        ds = format_date(birth_date)
        E = int(ds[0])
        F = int(ds[1])
        G = int(ds[2])
        H = int(ds[3])
        C = int(ds[4])
        D = int(ds[5])
        A = int(ds[6])
        B = int(ds[7])
        self.I = simplify(A + B)
        self.J = simplify(C + D)
        self.K = simplify(E + F)
        self.L = simplify(G + H)
        self.M = simplify(self.I + self.J)
        self.N = simplify(self.K + self.L)
        self.O = simplify(self.M + self.N)
        self.P = simplify(self.M + self.O)
        self.Q = simplify(self.N + self.O)
        self.R = simplify(self.Q + self.P)
        self.X = simplify(self.I + self.M)
        self.W = simplify(self.J + self.M)
        self.S = simplify(self.X + self.W)
        self.V = simplify(self.K + self.N)
        self.U = simplify(self.L + self.N)
        self.T = simplify(self.V + self.U)
        self.Y = simplify(self.I + self.L + self.O)
        today = datetime.now()
        self.flow_year = today.year
        self.flow_number = simplify(sum(int(d) for d in str(self.flow_year)) + simplify(int(ds[4]+ds[5]) + int(ds[6]+ds[7])))

    def get_brief(self):
        palace_nums = [self.I, self.J, self.K, self.L, self.M, self.N, self.O]
        missing = sorted(set(range(1,10)) - set(palace_nums))
        return {
            '主性格': self.O,
            '本源夢想': self.Y,
            '缺失數字': missing,
            '流年數': self.flow_number
        }

    def get_codes(self):
        codes = [
            f"{self.I}{self.J}{self.M}",
            f"{self.K}{self.L}{self.N}",
            f"{self.M}{self.N}{self.O}",
            f"{self.M}{self.O}{self.P}",
            f"{self.N}{self.O}{self.Q}",
            f"{self.Q}{self.P}{self.R}",
            f"{self.I}{self.M}{self.X}",
            f"{self.J}{self.M}{self.W}",
            f"{self.X}{self.W}{self.S}",
            f"{self.K}{self.N}{self.V}",
            f"{self.L}{self.N}{self.U}",
            f"{self.V}{self.U}{self.T}",
            ''.join(str(simplify(int(d) + int(d))) for d in f"{self.M}{self.N}{self.O}")
        ]
        return codes

    def get_five_elements(self):
        nums = [
            self.I, self.J, self.K, self.L, self.M, self.N, self.O,
            self.P, self.Q, self.R, self.S, self.T, self.U, self.V, self.W, self.X
        ]
        five_elements_map = {'金': [1,6], '水': [2,7], '火': [3,8], '木': [4,9], '土': [5]}
        element_count = {k: 0 for k in five_elements_map}
        for v in nums:
            for k, lst in five_elements_map.items():
                if v in lst:
                    element_count[k] += 1
        missing_ele = [k for k, v in element_count.items() if v == 0]
        return {'缺失五行': missing_ele}

# 只要這三個函數，完全只顯示你要的格式：
def show_brief(calc):
    brief = calc.get_brief()
    return (
        f"🎯 主性格數：{brief['主性格']}（查看完整主性格解析，請加LINE好友 👉 https://lin.ee/ymExb9U）\n"
        f"🌱 本源夢想數：{brief['本源夢想']}\n"
        f"🟥 缺失命格數字：{','.join(map(str, brief['缺失數字']))}\n"
        f"📈 今年流年數：{brief['流年數']}\n"
        "其他完整說明請加LINE好友 👉 https://lin.ee/ymExb9U"
    )

def show_codes(calc):
    codes = calc.get_codes()
    return (
        "🔐 你的13組人生密碼：\n" +
        "\n".join([f"{i+1}. {code}" for i, code in enumerate(codes)]) +
        "\n密碼詳解請加LINE好友 👉 https://lin.ee/ymExb9U"
    )

def show_five(calc):
    five = calc.get_five_elements()
    缺失 = five['缺失五行']
    if 缺失:
        缺失提示 = "｜".join(缺失)
    else:
        缺失提示 = "無"
    return (
        f"🔮 缺失五行：{缺失提示}\n"
        "五行解析請加LINE好友 👉 https://lin.ee/ymExb9U"
    )
