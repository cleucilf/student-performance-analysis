import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/workspaces/student-performance-analysis/data/student-mat (1).csv')

#print(df.info())

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Box Plot representing G3 by Study Time
sns.boxplot(
    x='studytime',
    y='G3',
    data=df,
    palette='muted',
    hue='studytime',
    legend=False
)

plt.title('Box Plot of Final Grades (G3) by Study Time', fontsize=14)
plt.xlabel('Weekly Study Time (1: <2 hrs, 2: 2-5 hrs, 3: 5-10 hrs, 4: >10 hrs)', fontsize=12)
plt.ylabel('Final Grade (G3)', fontsize=12)

plt.tight_layout()
output_path = '/workspaces/student-performance-analysis/student_studytime_boxplot.png'
plt.savefig(output_path, dpi=200)

if os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY'):
    plt.show()
else:
    print(f'Plot saved to: {output_path}')

#Stacked Bar plot

bins = [-1, 9, 13, 16, 20]
labels = ['Fail (0-9)', 'Pass (10-13)', 'Good (14-16)', 'Excellent (17-20)']
df['Grade_Category'] = pd.cut(df['G3'], bins=bins, labels=labels)

# 2. Create a contingency table showing percentages
distribution_df = pd.crosstab(df['studytime'], df['Grade_Category'], normalize='index') * 100

# 3. Plot the stacked bar chart
ax = distribution_df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis', edgecolor='black')

plt.title('Distribution of Grade Categories across Study Time Groups', fontsize=14)
plt.xlabel('Weekly Study Time (1: <2 hrs, 2: 2-5 hrs, 3: 5-10 hrs, 4: >10 hrs)', fontsize=12)
plt.ylabel('Percentage of Students (%)', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Grade Category', bbox_to_anchor=(1.05, 1), loc='upper left')

# Add percentage labels on top of the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if height > 0:
        ax.annotate(f'{height:.1f}%', (x + width/2, y + height/2), ha='center', va='center', color='white', fontweight='bold', fontsize=10)

plt.tight_layout()
output_path = '/workspaces/student-performance-analysis/student_studytime_grade_distribution_stacked_bar.png'
plt.savefig(output_path, dpi=200)

if os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY'):
    plt.show()
else:
    print(f'Plot saved to: {output_path}')