import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Style ──────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor':   '#f9f9f9',
    'axes.spines.top':  False,
    'axes.spines.right':False,
    'axes.grid':        True,
    'grid.color':       'white',
    'grid.linewidth':   1.2,
    'font.family':      'DejaVu Sans',
    'axes.titlesize':   13,
    'axes.labelsize':   11,
    'xtick.labelsize':  10,
    'ytick.labelsize':  10,
})

TEAL   = '#2a7f8f'
NAVY   = '#1a2332'
CORAL  = '#e06b4a'
COLORS = ['#2a7f8f','#1a2332','#e06b4a','#5DCAA5','#F0997B','#378ADD','#639922','#BA7517']

df = pd.read_csv('cafe_sales_2024.csv', parse_dates=['date','timestamp'])

import os
os.makedirs('charts', exist_ok=True)

# ── 1. Monthly Revenue ─────────────────────────────────────────────────────────
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
monthly = df.groupby('month')['revenue'].sum().reindex(month_order)

fig, ax = plt.subplots(figsize=(12, 5))
bars = ax.bar(monthly.index, monthly.values, color=TEAL, width=0.6, zorder=3)
ax.bar_label(bars, labels=[f'£{v/1000:.1f}k' for v in monthly.values], padding=4, fontsize=9, color=NAVY)
ax.set_title('Monthly Revenue — 2024', fontweight='bold', pad=12, color=NAVY)
ax.set_ylabel('Revenue (£)')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x/1000:.0f}k'))
ax.set_xticklabels([m[:3] for m in month_order])
plt.tight_layout()
plt.savefig('charts/01_monthly_revenue.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 saved")

# ── 2. Revenue by Day of Week ──────────────────────────────────────────────────
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
daily_rev = df.groupby('day_of_week')['revenue'].sum().reindex(day_order)

fig, ax = plt.subplots(figsize=(10, 5))
bar_colors = [CORAL if d in ['Saturday','Sunday'] else TEAL for d in day_order]
bars = ax.bar(daily_rev.index, daily_rev.values, color=bar_colors, width=0.6, zorder=3)
ax.bar_label(bars, labels=[f'£{v/1000:.1f}k' for v in daily_rev.values], padding=4, fontsize=9, color=NAVY)
ax.set_title('Total Revenue by Day of Week — weekends highlighted', fontweight='bold', pad=12, color=NAVY)
ax.set_ylabel('Revenue (£)')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x/1000:.0f}k'))
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=TEAL, label='Weekday'), Patch(color=CORAL, label='Weekend')], fontsize=10)
plt.tight_layout()
plt.savefig('charts/02_revenue_by_day.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 saved")

# ── 3. Hourly Footfall Heatmap ─────────────────────────────────────────────────
df['hour_label'] = df['hour'].apply(lambda h: f'{h:02d}:00')
pivot = df.groupby(['day_of_week','hour'])['transaction_id'].nunique().unstack(fill_value=0)
pivot = pivot.reindex(day_order)

fig, ax = plt.subplots(figsize=(14, 5))
sns.heatmap(pivot, cmap='YlOrRd', ax=ax, linewidths=0.3, linecolor='white',
            cbar_kws={'label': 'Transactions'}, fmt='d', annot=False)
ax.set_title('Hourly Footfall Heatmap — transactions by day & hour', fontweight='bold', pad=12, color=NAVY)
ax.set_xlabel('Hour of Day')
ax.set_ylabel('')
hour_labels = [f'{h:02d}:00' for h in sorted(df['hour'].unique())]
ax.set_xticklabels(hour_labels, rotation=45, ha='right', fontsize=9)
plt.tight_layout()
plt.savefig('charts/03_hourly_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3 saved")

# ── 4. Top Products by Revenue ─────────────────────────────────────────────────
top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 7))
bars = ax.barh(top_products.index, top_products.values, color=TEAL, zorder=3)
ax.bar_label(bars, labels=[f'£{v/1000:.1f}k' for v in top_products.values], padding=4, fontsize=9, color=NAVY)
ax.set_title('Revenue by Product — full year 2024', fontweight='bold', pad=12, color=NAVY)
ax.set_xlabel('Total Revenue (£)')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x/1000:.0f}k'))
plt.tight_layout()
plt.savefig('charts/04_top_products.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4 saved")

# ── 5. Revenue by Category ─────────────────────────────────────────────────────
cat_rev = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
total = cat_rev.sum()
pcts = [f'{v/total*100:.1f}%' for v in cat_rev.values]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
cat_colors = COLORS[:len(cat_rev)]
wedges, texts, autotexts = ax1.pie(
    cat_rev.values, labels=cat_rev.index, autopct='%1.1f%%',
    colors=cat_colors, startangle=140, pctdistance=0.75,
    wedgeprops={'linewidth': 1.5, 'edgecolor': 'white'}
)
for t in autotexts: t.set_fontsize(9)
ax1.set_title('Revenue share by category', fontweight='bold', color=NAVY)

bars = ax2.bar(cat_rev.index, cat_rev.values, color=cat_colors, width=0.6, zorder=3)
ax2.bar_label(bars, labels=[f'£{v/1000:.1f}k' for v in cat_rev.values], padding=4, fontsize=9, color=NAVY)
ax2.set_title('Revenue by category (£)', fontweight='bold', color=NAVY)
ax2.set_ylabel('Revenue (£)')
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x/1000:.0f}k'))
ax2.set_xticklabels(cat_rev.index, rotation=20, ha='right')
plt.tight_layout()
plt.savefig('charts/05_category_breakdown.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5 saved")

# ── 6. Weekly Revenue Trend ────────────────────────────────────────────────────
weekly = df.groupby(df['date'].dt.isocalendar().week)['revenue'].sum()

fig, ax = plt.subplots(figsize=(13, 5))
ax.plot(weekly.index, weekly.values, color=TEAL, linewidth=2.5, zorder=3)
ax.fill_between(weekly.index, weekly.values, alpha=0.15, color=TEAL)
ax.axhline(weekly.mean(), color=CORAL, linestyle='--', linewidth=1.5, label=f'Average £{weekly.mean():,.0f}/week')
ax.set_title('Weekly Revenue Trend — 2024', fontweight='bold', pad=12, color=NAVY)
ax.set_xlabel('Week Number')
ax.set_ylabel('Revenue (£)')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'£{x/1000:.1f}k'))
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig('charts/06_weekly_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 6 saved")

# ── Summary stats ──────────────────────────────────────────────────────────────
print("\n========== KEY INSIGHTS ==========")
print(f"Total Revenue:        £{df['revenue'].sum():>12,.2f}")
print(f"Total Transactions:   {df['transaction_id'].nunique():>12,}")
print(f"Avg Basket Value:     £{df.groupby('transaction_id')['revenue'].sum().mean():>12.2f}")
print(f"Best Month:           {monthly.idxmax():>12s}  (£{monthly.max():,.0f})")
print(f"Best Day:             {daily_rev.idxmax():>12s}  (£{daily_rev.max():,.0f})")
print(f"Peak Hour:            {df.groupby('hour')['revenue'].sum().idxmax():>11d}:00")
print(f"Top Product:          {df.groupby('product')['revenue'].sum().idxmax():>12s}")
print(f"Top Category:         {df.groupby('category')['revenue'].sum().idxmax():>12s}")
print("===================================")
