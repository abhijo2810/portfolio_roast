import pandas as pd

def analyze_trades(csv_path):
    df = pd.read_csv(csv_path)

    total_trades = len(df)
    wins = df[df['pnl'] > 0]
    losses = df[df['pnl'] <= 0]
    win_rate = len(wins) / total_trades if total_trades else 0
    profit_factor = wins['pnl'].sum() / abs(losses['pnl'].sum()) if not losses.empty else float('inf')
    avg_risk_reward = df['pnl'].mean() / (df['pnl'].std() + 1e-9)
    max_drawdown = df['pnl'].cumsum().min()

    return {
        "total_trades": total_trades,
        "win_rate": round(win_rate, 2),
        "profit_factor": round(profit_factor, 2),
        "avg_risk_reward": round(avg_risk_reward, 2),
        "max_drawdown": round(max_drawdown, 2)
    }
