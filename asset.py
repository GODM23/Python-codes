import pandas as pd

# === 1. Load Excel Files ===
sentinel_df = pd.read_excel("Sentinels_Full_Report.xlsx")
to_update_df = pd.read_excel("To be updated.xlsx")

# === 2. Filter only 'Online' assets from Sentinel ===
sentinel_online = sentinel_df[sentinel_df['Management Connectivity'] == 'Online'].copy()

# === 3. Rename columns to align with "To be updated" ===
sentinel_online = sentinel_online.rename(columns={
    'Endpoint Name': 'Hostname',
    'Model Name': 'Manufacturer/Model',
    'Serial Number': 'Serial Number',
    'Last Active': 'Last Active',
    'Last Reported IP': 'IP Address',
    'Management Connectivity': 'Status (Active/Decommissioned)'
})

# === 4. Merge based on 'Hostname' only for Online entries ===
merged_df = pd.merge(
    to_update_df,
    sentinel_online[['Hostname', 'Manufacturer/Model', 'Serial Number', 'Last Active', 'IP Address', 'Status (Active/Decommissioned)']],
    on='Hostname',
    how='left',
    suffixes=('', '_online')
)

# === 5. Update only selected fields if online data exists ===
fields_to_update = [
    'Manufacturer/Model',
    'Serial Number',
    'Last Active',
    'IP Address',
    'Status (Active/Decommissioned)'
]

# Safe update logic
for field in fields_to_update:
    online_col = f"{field}_online"
    if online_col in merged_df.columns:
        merged_df[field] = merged_df[online_col].combine_first(merged_df[field])

# === 6. Clean up extra columns ===
merged_df.drop(columns=[f"{field}_online" for field in fields_to_update if f"{field}_online" in merged_df.columns], inplace=True)

# === 7. Save updated Excel file ===
merged_df.to_excel("To_be_updated_FINAL_OnlineOnly.xlsx", index=False)

print("✅ Update complete. File saved as: To_be_updated_FINAL_OnlineOnly.xlsx")