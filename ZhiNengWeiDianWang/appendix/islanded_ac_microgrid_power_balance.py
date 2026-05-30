from pathlib import Path
import csv
import os
import sys

# 若 matplotlib 安装在项目本地 .python_deps，则优先使用本地依赖。
ROOT = Path(__file__).resolve().parents[1]
LOCAL_DEPS = ROOT / ".python_deps"
if LOCAL_DEPS.exists():
    sys.path.insert(0, str(LOCAL_DEPS))

# 避免 matplotlib 访问用户主目录缓存失败。
MPL_CACHE = ROOT / ".matplotlib_cache"
MPL_CACHE.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# 交流小微电网参数及本程序设计假设
P_ESS_MAX = 50.0       # 储能最大充/放电功率，kW
E_ESS = 100.0          # 储能容量，kWh，50 kW x 2 h
P_PV_MAX = 50.0        # 光伏额定功率，kW
P_LOAD_MAX = 50.0      # 重要负荷最大功率，kW
SOC_INIT = 0.60        # 初始 SOC
SOC_MIN = 0.20         # SOC 下限
SOC_MAX = 0.90         # SOC 上限
ETA_CH = 0.95          # 充电效率
ETA_DIS = 0.95         # 放电效率
DT = 1.0               # 控制周期，h


def limit(x, low, high):
    return max(low, min(high, float(x)))


def power_balance_control(P_pv, P_load, SOC, dt=DT):
    """
    离网功率平衡控制。
    P_ess > 0 表示储能放电，P_ess < 0 表示储能充电。
    P_balance_error = P_pv_actual + P_ess - P_load。
    """
    P_pv = limit(P_pv, 0, P_PV_MAX)
    P_load = limit(P_load, 0, P_LOAD_MAX)
    SOC = limit(SOC, 0, 1)

    P_ess = 0.0
    P_curtail = 0.0
    alarm = False

    if P_pv < P_load:
        # 光伏不足：储能放电，SOC 降低。
        deficit = P_load - P_pv
        available = max(0.0, (SOC - SOC_MIN) * E_ESS * ETA_DIS)
        P_dis_max = min(P_ESS_MAX, available / dt)
        P_ess = min(deficit, P_dis_max)
        SOC -= (P_ess * dt / ETA_DIS) / E_ESS
        SOC = max(SOC, SOC_MIN)
        P_pv_actual = P_pv
        P_balance_error = P_pv_actual + P_ess - P_load
        if P_balance_error < -1e-6:
            alarm = True
            status = "功率缺额告警，重要负荷存在供电风险"
        else:
            status = "光伏不足，储能放电补足缺额"

    elif P_pv > P_load:
        # 光伏盈余：先给储能充电，SOC 升高；充电受限后光伏限发。
        surplus = P_pv - P_load
        room = max(0.0, (SOC_MAX - SOC) * E_ESS)
        P_ch_max = min(P_ESS_MAX, room / (ETA_CH * dt))
        P_charge = min(surplus, P_ch_max)
        P_ess = -P_charge
        SOC += (P_charge * dt * ETA_CH) / E_ESS
        SOC = min(SOC, SOC_MAX)
        P_curtail = max(0.0, surplus - P_charge)
        P_pv_actual = P_pv - P_curtail
        P_balance_error = P_pv_actual + P_ess - P_load
        status = "光伏盈余，储能充电" if P_curtail == 0 else "储能充电受限，光伏限发"

    else:
        P_pv_actual = P_pv
        P_balance_error = 0.0
        status = "功率平衡，储能待机"

    return {
        "P_pv": P_pv,
        "P_pv_actual": P_pv_actual,
        "P_load": P_load,
        "P_ess": P_ess,
        "SOC": SOC,
        "P_curtail": P_curtail,
        "P_balance_error": P_balance_error,
        "status": status,
        "alarm": alarm,
    }


def simulate_one_day():
    # 演示数据：夜间无光伏，中午光伏高，晚间储能再次放电。
    P_pv_series = [0, 0, 0, 0, 0, 0, 10, 25, 40, 50, 50, 50,
                   50, 45, 35, 20, 10, 0, 0, 0, 0, 0, 0, 0]
    P_load_series = [35, 35, 35, 35, 35, 35, 40, 40, 35, 25, 10, 10,
                     10, 10, 15, 25, 35, 40, 45, 45, 45, 45, 45, 45]

    rows = []
    SOC = SOC_INIT
    for hour, (P_pv, P_load) in enumerate(zip(P_pv_series, P_load_series)):
        r = power_balance_control(P_pv, P_load, SOC)
        r["hour"] = hour
        rows.append(r)
        SOC = r["SOC"]
    return rows


def save_csv(rows, out_dir):
    path = out_dir / "仿真结果.csv"
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["时间/h", "光伏可发功率/kW", "光伏实际出力/kW", "负荷功率/kW",
                         "储能功率/kW", "SOC/%", "光伏限发功率/kW",
                         "功率平衡误差/kW", "控制状态", "告警状态"])
        for r in rows:
            writer.writerow([
                r["hour"], f"{r['P_pv']:.2f}", f"{r['P_pv_actual']:.2f}",
                f"{r['P_load']:.2f}", f"{r['P_ess']:.2f}", f"{r['SOC'] * 100:.2f}",
                f"{r['P_curtail']:.2f}", f"{r['P_balance_error']:.2f}",
                r["status"], "告警" if r["alarm"] else "正常",
            ])
    return path


def draw_figures(rows, out_dir):
    t = [r["hour"] for r in rows]
    pv = [r["P_pv_actual"] for r in rows]
    load = [r["P_load"] for r in rows]
    ess = [r["P_ess"] for r in rows]
    soc = [r["SOC"] * 100 for r in rows]
    curtail = [r["P_curtail"] for r in rows]
    alarm = [50 if r["alarm"] else 0 for r in rows]

    plt.rcParams["axes.unicode_minus"] = False

    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    ax.plot(t, pv, marker="o", label="PV actual / kW")
    ax.plot(t, load, marker="s", label="Load / kW")
    ax.bar(t, ess, alpha=0.35, label="ESS (+discharge, -charge)")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Power balance of islanded AC microgrid")
    ax.set_xlabel("Time / h")
    ax.set_ylabel("Power / kW")
    ax.set_xticks(t)
    ax.grid(True, linestyle="--", linewidth=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "仿真结果_功率曲线.png")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4), dpi=150)
    ax.plot(t, soc, marker="o", label="SOC / %")
    ax.axhline(SOC_MIN * 100, color="black", linestyle="--", label="SOC min")
    ax.axhline(SOC_MAX * 100, color="black", linestyle=":", label="SOC max")
    ax.set_title("ESS SOC")
    ax.set_xlabel("Time / h")
    ax.set_ylabel("SOC / %")
    ax.set_xticks(t)
    ax.set_ylim(0, 100)
    ax.grid(True, linestyle="--", linewidth=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "仿真结果_SOC曲线.png")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 4), dpi=150)
    ax.bar(t, curtail, alpha=0.55, label="PV curtailment / kW")
    ax.step(t, alarm, where="mid", label="Alarm flag x50")
    ax.set_title("PV curtailment and deficit alarm")
    ax.set_xlabel("Time / h")
    ax.set_ylabel("Curtailment / kW, alarm flag")
    ax.set_xticks(t)
    ax.grid(True, linestyle="--", linewidth=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "仿真结果_限发与告警.png")
    plt.close(fig)


def main():
    out_dir = Path(__file__).resolve().parent
    rows = simulate_one_day()
    save_csv(rows, out_dir)
    draw_figures(rows, out_dir)
    print("仿真完成：已生成 CSV 和三张结果图。")


if __name__ == "__main__":
    main()
